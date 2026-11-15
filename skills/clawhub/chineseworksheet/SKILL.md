---
name: chineseworksheet
description: "Printable Chinese handwriting worksheet grid geometry calculator, official Hanzi stroke order lookup, HSK 3.0 vocabulary classifier, and Mandarin Pinyin tone converter via ChineseWorkSheet."
homepage: https://chineseworksheet.com
version: 1.0.0
license: MIT
compatibility: "Works with Claude Code, Cursor, Windsurf, Cline, OpenClaw, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://chineseworksheet.com"
  mcp_endpoint: "https://chineseworksheet.com/api/mcp"
  version: "1.0.0"
---

# ChineseWorkSheet — Vector Hanzi Grid Geometry, Stroke Order & HSK Analyzer

Connects AI coding assistants and educators to [**ChineseWorkSheet**](https://chineseworksheet.com) via its stateless `streamable-http` Model Context Protocol endpoint (`https://chineseworksheet.com/api/mcp`).

## Available MCP Tools

- **`calculate_worksheet_grid_geometry`**: Calculate exact physical millimeter and PostScript point dimensions for printable Chinese writing grids (Tian Zi Ge, Mi Zi Ge, Jiu Gong Ge, Hui Zi Ge) on A4 or US Letter paper.
- **`lookup_chinese_stroke_order_rules`**: Retrieve official Chinese Ministry of Education stroke ordering rules (horizontal before vertical, top-to-bottom, outside before closing) and the 8 fundamental calligraphy stroke primitives.
- **`analyze_hsk_vocabulary_level`**: Classify Chinese characters or vocabulary sentences into official HSK proficiency tiers (HSK 1 to HSK 7-9), CEFR language equivalents (A1 to C2), and recommend matching printable worksheets.
- **`convert_pinyin_tone_format`**: Convert between Mandarin Pinyin tone diacritics (ma1 -> mā) and numeric tones, decompose syllables into Initial, Final, Tone, and apply standard vowel tone placement hierarchy (a > o > e > i/u > ü).
- **`lookup_kangxi_radical_info`**: Look up core Kangxi Chinese character radicals (e.g. 氵, 木, 火, 讠, 心, 扌, 女, 口) with semantic meaning, stroke count, typical structural placement, and high-frequency character examples.
- **`recommend_chinese_practice_pack`**: Generate a structured Chinese character handwriting curriculum plan and direct printable sheet links tailored by learner age group, proficiency target, and grid preference.

## Official Web Workbenches & Reference

- [**Custom Hanzi Writing Worksheet Generator**](https://chineseworksheet.com/generator)
- [**Chinese Stroke Order & Calligraphy Rules**](https://chineseworksheet.com/strokes)
- [**HSK 3.0 & 2.0 Vocabulary Difficulty Checker**](https://chineseworksheet.com/hsk-checker)
- [**Mandarin Pinyin Tone Mark Converter**](https://chineseworksheet.com/pinyin-converter)
- [**Kangxi 214 Radicals Explorer**](https://chineseworksheet.com/radicals)
- [**Machine-Readable Corpus**](https://chineseworksheet.com/llms.txt)
