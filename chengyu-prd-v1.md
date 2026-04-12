# AI Product Requirements Document

## Daily Chengyu: Ancient Wisdom for Modern Tech Leaders

**Author:** Anja  
**Version:** 1.0  
**Status:** Draft

---

## How can we use AI to help our users?

Use AI to surface ancient Chinese wisdom (chengyu) paired with personal tech and leadership stories, helping intellectuals and tech professionals draw unexpected connections between classical Chinese thought and modern challenges.

---

## 1. About

**TLDR:** A twice-weekly Substack column that pairs Chinese four-character idioms (chengyu) with personal stories from technology, coaching, and immigrant experience. Each post bridges ancient Chinese patterns and modern professional life.

**Problem Space:** Intellectuals in tech who care about culture, depth, and cross-domain thinking have no consistent, high-quality resource that makes classical Chinese wisdom *personally and professionally applicable*. Most chengyu content is either purely academic or purely language-learning focused. Nobody is doing the bridge-building between ancient patterns and modern problems through authentic personal narrative.

---

## 2. Market Insights

**Competitors / Existing Content:**
- chineseidioms.com — 1,000+ entries, educational, no personal narrative
- Chinese-Tools.com — 30,000+ entries, dictionary format only
- Pimsleur / FluentU — language learning lens, not wisdom/leadership lens
- Generic Substack culture writers — broad, not tech-focused

**Gap:** No one is combining chengyu + personal tech/immigration/coaching stories + AI-generated visuals in a consistent content format aimed at intellectually curious professionals.

**Target Persona:**  
Intellectuals with broad interests — curious professionals, technologists, and thought leaders who appreciate philosophy, culture, and ideas that cut across domains. They may or may not have Chinese heritage but are drawn to depth and originality.

---

## 3. The Problem

**Primary Use Cases:**
- Reader wants to understand how ancient wisdom applies to their current professional challenge
- Reader wants culturally rich, intellectually stimulating content that isn't shallow
- Author wants a consistent content vehicle that builds brand authority in tech + culture

**Pain Points:**
- Most chengyu content is either too academic or too basic
- No personal narrative makes it forgettable
- No visual hook to make it shareable
- No consistent cross-domain lens (tech + ancient wisdom)

**Problem Statement:** Intellectuals in tech have no reliable, high-quality content source that translates classical Chinese wisdom into lived, relatable, modern experience — leaving a gap in culturally rich thought leadership content.

---

## 4. The Solution

**Core Concept:** Each post = one chengyu + one personal story from Anja's life (tech, coaching, immigration) that illustrates the idiom's meaning in a modern context.

**Post Structure:**
1. Chinese characters (e.g., 塞翁失馬)
2. Pinyin pronunciation
3. Literal English translation
4. Historical origin / backstory
5. Anja's personal story tying the idiom to a real tech or life moment
6. Takeaway for the reader
7. AI-generated visual that captures the idiom's essence

**AI Components:**
- Data ingestion: Parse GitHub repo (by-syk/chinese-idiom-db) into structured CSV/database
- Content enrichment: Claude fills in missing fields (origin stories, meanings, pinyin) where data is incomplete
- Story matching: Claude and Anja collaboratively match idioms to personal stories
- Image generation: AI-generated visuals for each post
- Substack formatting: Posts formatted in Substack-ready markdown

**Roadmap:**

| Phase | Description | Timeline |
|-------|-------------|----------|
| Phase 1 | Data ingestion: download, parse, clean GitHub idiom repo into CSV | Week 1 |
| Phase 2 | Curation: select 20–30 starter idioms matched to personal stories | Week 1–2 |
| Phase 3 | Content creation: write first 4–6 posts with images | Week 2–3 |
| Phase 4 | Launch on Substack, twice weekly | Week 3+ |
| Phase 5 | Repurpose to LinkedIn and personal website | Ongoing |

---

## 5. Requirements

**Data Pipeline Requirements:**
- Download by-syk/chinese-idiom-db from GitHub
- Parse into CSV with these fields: `idiom_chinese`, `idiom_pinyin`, `idiom_english`, `literal_meaning`, `figurative_meaning`, `historical_origin`, `tags`
- Flag missing fields for manual or AI enrichment
- Store in Google Sheets for collaborative curation

**Content Requirements:**
- Each post 400–700 words
- Personal story is first-person, protagonist is Anja
- Story draws from: tech career, coaching experience, or immigration/cultural identity
- One AI-generated image per post
- Substack-formatted markdown output

**Automation Requirements:**
- Script to pull random (or scheduled) idiom from curated list
- Script to format post template with idiom data
- Optional: Railway deployment for scheduling and automation

**Non-Functional Requirements:**
- Posts must feel human and personal, not AI-generated
- Anja reviews and edits every post before publishing
- Batch create 4–5 posts at a time to avoid daily context-switching

---

## 6. Challenges

**Data Quality:** The GitHub repo may have incomplete English translations or missing origin stories — will need enrichment via Claude or manual research.

**Story Supply:** Personal stories need to be mined carefully. Claude will assist Anja in recalling and structuring relevant memories.

**Consistency:** Twice-weekly cadence requires batching. Risk of burnout if not systematized.

**Validation:** Test with a small audience (5–10 readers) before scaling promotion.

---

## 7. Positioning

| Use Case | Pain Point | Solution |
|----------|------------|----------|
| Intellectual wants culturally rich content | Nothing bridges Chinese wisdom + tech | Personal chengyu column with tech lens |
| Tech professional seeking leadership perspective | Generic leadership content | Ancient wisdom applied to real modern decisions |
| Reader curious about Chinese culture | Academic or language-learning framing | Story-first, personality-driven posts |

---

## 8. Measuring Success

**North Star Metric:** Substack subscriber growth (target: 500 subscribers in 6 months)

**Supporting Metrics:**
- Open rate per post (target: >40%)
- LinkedIn reposts / engagement when cross-posted
- Reader replies and comments (qualitative signal)
- Number of posts published consistently over 90 days

---

## 9. Launching

**Stakeholders:** Anja (author, editor, publisher)

**Platforms:**
- Primary: Substack (existing account, currently empty — repurpose for this project)
- Secondary: LinkedIn (repurpose each post)
- Tertiary: Personal website / new site TBD

**Rollout:**
1. Build data pipeline (Claude Code)
2. Curate first 20 idioms with story angles (Anja + Claude)
3. Write and batch first 6 posts
4. Soft launch — share with close network first
5. Open to public on Substack
6. Begin twice-weekly publishing rhythm

---

*This PRD is a living document. Update as the project evolves.*
