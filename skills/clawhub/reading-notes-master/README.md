# reading-notes-master

[![License: MIT-0](https://img.shields.io/badge/License-MIT--0-yellow.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](./SKILL.md)
[![Format](https://img.shields.io/badge/format-AgentSkill-orange.svg)](./SKILL.md)

**Publication-grade visual reading-notes generator** — turn any book's key ideas into beautiful, slide-style reading notes (HTML / PDF / PPTX / long image).

出版级可视化读书笔记生成器 —— 把任何一本书的精华转化为精美排版的幻灯片式读书笔记（HTML / PDF / PPTX / 长图）。

> Every design rule in this skill is **measured, not guessed**: distilled from 31 high-quality real-world reading-notes decks (~2,500 pages) via programmatic analysis (pypdf font/size mining, pypdfium2 color quantization, image-density metrics), then upgraded with publication-grade design tokens from awesome-design-md (Notion × Claude design systems).

## Features

- **9 page modules** — cover / author timeline / endorsements / why-read / TOC / part divider / content pages / golden-quote page / mindmap & review
- **6 narrative archetypes** — A Narrative · B Tool & Method · C Structured Doc (8-block exam template) · D Data Recap · E Endorsement-led · F Thematic Grouping, with a decision tree
- **20 measured theme palettes** mapped to book genres (investing red, finance-history teal, strategy blue, psychology warm-earth, dark-mode sci-fi …)
- **10 chart components** — timeline, stage band, side-by-side duel, framework diagram, numbered cards, mindmap, quadrant, data chart … with a selection decision tree
- **v2 design tokens** (Stitch 9-section format) — warm ink `rgba(30,26,22,.95)`, whisper borders, 3-level soft shadow stack (≤5% per layer), progressive negative letter-spacing, 4-weight type system, radius ladder 8/12/16, warm-paper alternation `.alt`, pill badges, serif golden quotes (weight 500)
- **16:9 HTML template v2.0** — one `:root` swap to re-skin (theme layer), tokens locked (texture layer)
- **Export pipelines** — Chrome headless → PDF, python-pptx → PPTX, long-image, A4 variant

## Install

**ClawHub:**

```bash
clawhub install reading-notes-master
```

**Manual (WorkBuddy / OpenClaw / any AgentSkills runtime):**

```bash
git clone https://github.com/yjkj999999/reading-notes-master.git
cp -r reading-notes-master ~/.workbuddy/skills/   # or ~/.openclaw/skills/
```

## Usage

Say any trigger phrase to your agent: **读书笔记 / 生成笔记 / 可视化读书笔记 / reading notes / 读书笔记PPT / 读书报告 / 精华笔记**, then provide the book's raw materials (key points, golden quotes, structure).

Five-step workflow:

1. **Pick archetype** — `references/content-framework.md` §3 decision tree
2. **Set tone** — theme color from `references/design-system.md` §3.2 (20-palette mapping table)
3. **Lay out pages** — copy sections from `templates/reading-notes-template.html` (12 page types), alternate `.alt` warm-paper pages every 2–3 content pages
4. **Fill components** — pick charts via `references/chart-catalog.md` decision tree
5. **Export** — follow `templates/output-pipelines.md`

## Structure

```
reading-notes-master/
├── SKILL.md                          # entry: workflow, checklist, error handling
├── references/
│   ├── design-tokens.md              # v2 publication-grade tokens (Stitch 9 sections)
│   ├── design-system.md              # layout / fonts / type ladder / 20 theme palettes
│   ├── content-framework.md          # 9 modules / 8-block template / 6 archetypes
│   ├── chart-catalog.md              # 10 chart components + decision trees
│   └── case-patterns.md              # 31-corpus style archive + reuse rules
├── templates/
│   ├── reading-notes-template.html   # 16:9 publication-grade HTML skeleton v2.0
│   └── output-pipelines.md           # PDF / PPTX / long-image export commands
├── demo/
│   └── toyota-one-page-thinking-notes.html   # 12-page full demo (v2 tokens)
├── LICENSE                           # MIT-0
└── README.md
```

## Demo

Open `demo/toyota-one-page-thinking-notes.html` in Chrome — a 12-page publication-grade reading note of *《丰田一页纸极简思考法》* (One Page Thinking @ Toyota), built entirely with the v2 token set. Print to PDF via `Cmd+P` (page size pre-configured via `@page`).

## Author

**WANG DONG JIE (yjkj999999)** · [ClawHub profile](https://clawhub.com/yjkj999999) · CFO-level expert system builder, 30+ MIT-0 agent skills published.

## License

MIT-0 (MIT No Attribution) — free to use, modify, redistribute, no attribution required.
