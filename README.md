# Daily Chengyu: Ancient Wisdom for Modern Tech Leaders

A twice-weekly Substack column pairing Chinese four-character idioms (chengyu) with personal stories from technology, coaching, and immigrant experience.

## About This Project

This project bridges ancient Chinese patterns and modern professional challenges through authentic personal narrative and AI-assisted content creation.

**Target Audience:** Intellectuals in tech—curious professionals and thought leaders who appreciate philosophy, culture, and cross-domain thinking.

## Project Structure

```
DailyChengYu/
├── chengyu-prd-v1.md          # Product Requirements Document
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── scripts/
│   ├── parse_idioms.py        # Phase 1: Parse idiom data from GitHub
│   └── [Phase 2-4 scripts TBD]
│
└── data/
    ├── raw/                    # Downloaded raw data
    │   └── chinese-idioms-12976.txt
    ├── processed/              # Parsed and cleaned CSV
    │   └── idioms_parsed.csv
    └── validation_report.txt   # Data quality report
```

## Phases & Roadmap

| Phase | Task | Status |
|-------|------|--------|
| **1** | Data ingestion: download and parse idiom repo | 🚧 In Progress |
| **2** | Curation: match idioms to personal stories | ⏳ Pending |
| **3** | Content creation: write posts with images | ⏳ Pending |
| **4** | Launch: publish on Substack twice weekly | ⏳ Pending |
| **5** | Repurpose: LinkedIn and personal site | ⏳ Pending |

## Phase 1: Data Ingestion

### Overview
Download and parse the Chinese idiom database from [by-syk/chinese-idiom-db](https://github.com/by-syk/chinese-idiom-db), transforming 12,976+ idiom entries into a curated CSV for collaborative editing.

### How to Run

```bash
# Navigate to project directory
cd DailyChengYu

# Run the parsing script
python scripts/parse_idioms.py
```

### What It Does

1. **Downloads** the raw idiom data (first run only, ~1MB)
2. **Parses** the 12,976 idioms into structured records
3. **Transforms** fields into target schema:
   - `idiom_chinese` — Chinese characters
   - `idiom_pinyin` — Romanized pronunciation
   - `idiom_english` — English translation (flagged for enrichment)
   - `literal_meaning` — Definition in Chinese
   - `figurative_meaning` — Deep meaning (flagged for enrichment)
   - `historical_origin` — Source or backstory
   - `tags` — Categorization tags

4. **Cleans** data by removing duplicates and flagging incomplete entries
5. **Generates** a validation report showing data quality
6. **Outputs** `/data/processed/idioms_parsed.csv` ready for curation

### Output Files

After running the script:

- **`data/processed/idioms_parsed.csv`** — Main output (all 12,976 idioms)
  - Ready to upload to Google Sheets for collaborative curation
  - Some fields marked with `[NEEDS_TRANSLATION]` or `[NEEDS_ENRICHMENT]` for Phase 2

- **`data/validation_report.txt`** — Quality assurance report
  - Shows parsing statistics
  - Lists incomplete records
  - Provides data completeness score

### Next Steps

1. Review `data/processed/idioms_parsed.csv` locally
2. Upload to Google Sheets for collaborative curation with Anja
3. Select 20–30 starter idioms matched to personal stories
4. Proceed to Phase 2: Content Creation

---

## Development Notes

### Technology Stack
- **Language:** Python 3
- **Data Processing:** csv module (standard library)
- **Future Phases:** Anthropic Claude API, Google Sheets API, Substack

### Key Decisions
- Using standard library for Phase 1 (no external dependencies needed)
- CSV as intermediate format (easy to collaborate on in Google Sheets)
- Flagging missing fields for enrichment rather than auto-generating content

---

## Contributing

This is a personal project by Anja. For questions or suggestions, please reach out directly.

---

*Last updated: 2026-04-11*
