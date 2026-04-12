#!/usr/bin/env python3
"""
Parse idiom data from by-syk/chinese-idiom-db repository
Downloads and transforms raw idiom data into structured CSV format
"""

import csv
import os
import sys
import urllib.request
from pathlib import Path
from collections import defaultdict


class IdiomParser:
    """Parse and transform idiom data from GitHub repository."""
    
    # GitHub raw content URL for the idiom database
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/by-syk/chinese-idiom-db/master/chinese-idioms-12976.txt"
    
    # Target CSV fields
    TARGET_FIELDS = [
        'idiom_chinese',
        'idiom_pinyin', 
        'idiom_english',
        'literal_meaning',
        'figurative_meaning',
        'historical_origin',
        'tags'
    ]
    
    def __init__(self, raw_data_path: str, processed_data_path: str, report_path: str):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        self.report_path = report_path
        self.validation_stats = defaultdict(int)
        
    def download_raw_data(self) -> bool:
        """Download raw idiom data from GitHub repository."""
        print(f"Downloading raw idiom data from GitHub...")
        try:
            urllib.request.urlretrieve(self.GITHUB_RAW_URL, self.raw_data_path)
            print(f"✓ Downloaded to {self.raw_data_path}")
            return True
        except Exception as e:
            print(f"✗ Failed to download: {e}")
            return False
    
    def parse_raw_data(self) -> list:
        """
        Parse the raw text file into structured idiom records.
        
        Source format: ID,"Chinese","pinyin","definition","source","example","abbreviation"
        """
        idioms = []
        duplicate_check = set()
        
        print(f"\nParsing raw data from {self.raw_data_path}...")
        
        try:
            with open(self.raw_data_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                
                for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                    if len(row) < 3:  # Need at least ID, Chinese, Pinyin
                        self.validation_stats['rows_skipped_malformed'] += 1
                        continue
                    
                    try:
                        # Parse source fields
                        idiom_id = row[0].strip() if len(row) > 0 else ""
                        chinese = row[1].strip() if len(row) > 1 else ""
                        pinyin = row[2].strip() if len(row) > 2 else ""
                        definition_cn = row[3].strip() if len(row) > 3 else ""
                        source = row[4].strip() if len(row) > 4 else ""
                        example = row[5].strip() if len(row) > 5 else ""
                        abbreviation = row[6].strip() if len(row) > 6 else ""
                        
                        # Skip if missing critical fields
                        if not chinese or not pinyin:
                            self.validation_stats['rows_skipped_missing_critical'] += 1
                            continue
                        
                        # Check for duplicates
                        if chinese in duplicate_check:
                            self.validation_stats['duplicates_removed'] += 1
                            continue
                        duplicate_check.add(chinese)
                        
                        # Transform to target format
                        idiom_record = {
                            'idiom_id': idiom_id,
                            'idiom_chinese': chinese,
                            'idiom_pinyin': pinyin,
                            'idiom_english': '[NEEDS_TRANSLATION]',  # Flag for enrichment
                            'literal_meaning': definition_cn,
                            'figurative_meaning': '[NEEDS_ENRICHMENT]',  # Flag for enrichment
                            'historical_origin': source,
                            'example': example,
                            'tags': abbreviation if abbreviation else 'untagged'
                        }
                        
                        idioms.append(idiom_record)
                        self.validation_stats['rows_parsed_success'] += 1
                        
                        # Track missing data
                        if not definition_cn:
                            self.validation_stats['missing_literal_meaning'] += 1
                        if not source:
                            self.validation_stats['missing_historical_origin'] += 1
                        if not example:
                            self.validation_stats['missing_example'] += 1
                            
                    except Exception as e:
                        self.validation_stats['rows_error'] += 1
                        print(f"  ✗ Error parsing row {row_num}: {e}")
                        continue
        
        except FileNotFoundError:
            print(f"✗ File not found: {self.raw_data_path}")
            return []
        except Exception as e:
            print(f"✗ Error reading file: {e}")
            return []
        
        print(f"✓ Parsed {len(idioms)} idiom records")
        return idioms
    
    def save_to_csv(self, idioms: list) -> bool:
        """Save parsed idioms to CSV file with proper quoting."""
        print(f"\nSaving to {self.processed_data_path}...")
        
        try:
            os.makedirs(os.path.dirname(self.processed_data_path), exist_ok=True)
            
            # Include example field in output (useful but not in final target yet)
            csv_fields = self.TARGET_FIELDS
            
            # Use QUOTE_ALL to ensure all fields are quoted for safety and readability
            with open(self.processed_data_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=csv_fields, quoting=csv.QUOTE_ALL)
                writer.writeheader()
                
                for idiom in idioms:
                    row = {field: idiom.get(field, '') for field in csv_fields}
                    writer.writerow(row)
            
            print(f"✓ Saved {len(idioms)} records to CSV")
            return True
        
        except Exception as e:
            print(f"✗ Failed to save CSV: {e}")
            return False
    
    def generate_validation_report(self, total_idioms: int) -> None:
        """Generate validation report showing data quality."""
        print(f"\nGenerating validation report...")
        
        report_lines = [
            "=" * 60,
            "PHASE 1 DATA INGESTION VALIDATION REPORT",
            "=" * 60,
            "",
            "PARSING STATISTICS:",
            f"  Rows successfully parsed:        {self.validation_stats['rows_parsed_success']:>6}",
            f"  Rows skipped (malformed):       {self.validation_stats['rows_skipped_malformed']:>6}",
            f"  Rows skipped (missing critical):{self.validation_stats['rows_skipped_missing_critical']:>6}",
            f"  Duplicates removed:             {self.validation_stats['duplicates_removed']:>6}",
            f"  Rows with parsing errors:       {self.validation_stats['rows_error']:>6}",
            "",
            "DATA COMPLETENESS:",
            f"  Missing literal meanings:       {self.validation_stats['missing_literal_meaning']:>6}",
            f"  Missing historical origins:     {self.validation_stats['missing_historical_origin']:>6}",
            f"  Missing examples:               {self.validation_stats['missing_example']:>6}",
            "",
            "SUMMARY:",
            f"  Total idioms in output CSV:     {total_idioms:>6}",
            f"  Data completeness score:        {self._calculate_completeness(total_idioms):.1%}",
            "",
            "NEXT STEPS:",
            "  1. Review CSV in data/processed/idioms_parsed.csv",
            "  2. Upload to Google Sheets for collaborative curation",
            "  3. Proceed to Phase 2: Story matching and content creation",
            "",
            "=" * 60,
        ]
        
        report_text = "\n".join(report_lines)
        print(report_text)
        
        # Save to file
        try:
            os.makedirs(os.path.dirname(self.report_path), exist_ok=True)
            with open(self.report_path, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"✓ Report saved to {self.report_path}")
        except Exception as e:
            print(f"✗ Failed to save report: {e}")
    
    def _calculate_completeness(self, total_idioms: int) -> float:
        """Calculate overall data completeness percentage."""
        if total_idioms == 0:
            return 0.0
        
        # All target fields should be filled, but some are enrichment flags
        # Count: Chinese, Pinyin, Literal meaning, Origin = 4 critical fields
        missing_critical = (
            self.validation_stats['missing_literal_meaning'] +
            self.validation_stats['missing_historical_origin']
        )
        
        completeness = 1.0 - (missing_critical / (total_idioms * 2))
        return max(0.0, min(1.0, completeness))  # Clamp between 0-1
    
    def run(self) -> bool:
        """Execute full parsing pipeline."""
        print("\n" + "=" * 60)
        print("PHASE 1: DATA INGESTION PIPELINE")
        print("=" * 60)
        
        # Download data
        if not os.path.exists(self.raw_data_path):
            if not self.download_raw_data():
                print("\nNote: Download failed. You can manually place the file at:")
                print(f"  {self.raw_data_path}")
                print("\nOr download from:")
                print(f"  {self.GITHUB_RAW_URL}")
                return False
        else:
            print(f"✓ Using existing raw data file: {self.raw_data_path}")
        
        # Parse data
        idioms = self.parse_raw_data()
        if not idioms:
            print("✗ No idioms parsed. Aborting.")
            return False
        
        # Save to CSV
        if not self.save_to_csv(idioms):
            return False
        
        # Generate report
        self.generate_validation_report(len(idioms))
        
        print("\n✓ Phase 1 complete! Ready for Phase 2 (curation)")
        return True


def main():
    """Main entry point."""
    # Get project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    raw_data_path = os.path.join(project_root, 'data/raw/chinese-idioms-12976.txt')
    processed_data_path = os.path.join(project_root, 'data/processed/idioms_parsed.csv')
    report_path = os.path.join(project_root, 'data/validation_report.txt')
    
    parser = IdiomParser(raw_data_path, processed_data_path, report_path)
    success = parser.run()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
