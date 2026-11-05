# reading-notes-master

[![License: MIT-0](https://img.shields.io/badge/License-MIT--0-yellow.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-2.7.0-blue.svg)](./SKILL.md)
[![Format](https://img.shields.io/badge/format-AgentSkill-orange.svg)](./SKILL.md)

**Publication-grade visual reading-notes generator** — turn any book's key ideas into beautiful, slide-style reading notes (HTML / PDF / PPTX / long image).

出版级可视化读书笔记生成器 —— 把任何一本书的精华转化为精美排版的幻灯片式读书笔记（HTML / PDF / PPTX / 长图）。

> Every design rule in this skill is **measured, not guessed**: distilled from 31 high-quality real-world reading-notes decks (~2,500 pages) via programmatic analysis (pypdf font/size mining, pypdfium2 color quantization, image-density metrics), then upgraded with publication-grade design tokens from awesome-design-md (Notion × Claude design systems).

## Features

- **9 page modules** — cover / author timeline / endorsements / why-read / TOC / part divider / content pages / golden-quote page / mindmap & review
- **6 narrative archetypes** — A Narrative · B Tool & Method · C Structured Doc (8-block exam template) · D Data Recap · E Endorsement-led · F Thematic Grouping, with a decision tree
- **20 measured theme palettes** mapped to book genres (investing red, finance-history teal, strategy blue, psychology warm-earth, dark-mode sci-fi …)
- **10+6 chart components** — timeline, stage band, side-by-side duel, framework diagram, numbered cards, mindmap, quadrant, data chart … with a selection decision tree; v2.1 adds 6 emotion-marketing components (toggle-switch panel / five-color spectrum band / value ladder / virality loop / weight tree / six-fear word tags)
- **v2 design tokens** (Stitch 9-section format) — warm ink `rgba(30,26,22,.95)`, whisper borders, 3-level soft shadow stack (≤5% per layer), progressive negative letter-spacing, 4-weight type system, radius ladder 8/12/16, warm-paper alternation `.alt`, pill badges, serif golden quotes (weight 500)
- **16:9 HTML template v2.0** — one `:root` swap to re-skin (theme layer), tokens locked (texture layer)
- **v2.1 emotion-marketing knowledge base** — five emotional switches (痛点 pain / 痒点 itch / 爽点 joy / 燃点 burn / 爆点 boom) × five-color emotion spectrum (wine-red / warm-orange / gold / scarlet / violet) × proven case library (Wanglaoji 200×, Meituan 3-in-1, Snow Flower replica …) × 5×4 observation matrix — in `references/emotion-marketing.md`
- **v2.2 consulting-grade page craft** — four narrative storylines with per-page `adds` discipline / judgment-sentence title rules + strong-word list / page-role table / five-zone page skeleton with single-takeaway & density tiers / relation→chart selection table with data contracts / 13 anti-pattern red lines / waterfall reconciliation contract / diagram semantic contracts / module-fill P-D-F-X-V protocol / 16:9 capacity-first hard grid / 4-gate acceptance + 12-question page audit — distilled from consulting-report-forge v1.8.0 (Apache-2.0) and reorganized for argumentative reading-notes pages — in `references/consulting-craft.md`
- **Export pipelines** — Chrome headless → PDF, python-pptx → PPTX, long-image, A4 variant
- **v2.3 graphics asset pipeline** — replicate-or-generate dual track for any chart/diagram/image in your notes: Path A replication (PyMuPDF layered extraction → sn-image-base VLM vision → Real-ESRGAN 4× super-resolution via `scripts/superres.sh` → bitmap→vector tracing via `scripts/bitmap2vector.sh`, vtracer color / potrace B&W) and Path B generation (mermaid→SVG/PNG/PDF via `scripts/mermaid-export.sh`, markdown→mindmap via markmap, text→SVG charts via `scripts/clip-chart.sh`, plus cognigraph-mcp-server integration for MCP hosts — 4 tools: mindmap / relationship graph / knowledge graph); all tools version-pinned with SHA256-verified test artifacts and a 10-pitfall ops library — in `references/graphics-toolchain.md`
- **v2.4 design-intelligence front-loading (Step 0)** — full ingestion of four design skills (92 files / 1.5 MB) under `references/design-intelligence/`: ① **ui-ux-pro-max** BM25 search engine (67 UI styles / 161 palettes / 57 font pairings / 13 stack rulebooks / UX guidelines / chart selection / landing patterns + `--design-system` generator; pure-stdlib local CSV engine, English-keyword search) ② **ui-ux-pro-max-cn** Chinese localization rules (Chinese font stacks / color culture / WeChat mini-program specs / Element Plus·Ant Design·Vant stacks / 5 industry rules / Chinese delivery checklist) ③ **awesome-design-md** 54 real-brand DESIGN.md specs (Vercel / Stripe / Linear / Notion / Claude / Apple / BMW / SpaceX …) ④ **awesome-design** 20+ design-skill selection navigator. Tone-setting upgrades from "look up the built-in mapping table" to "search the design-intelligence library first, then decide" — see `references/design-intelligence/INDEX.md`
- **v2.5 mental-models composition library + text-to-image spec** — full ingestion of 《万物皆模型》100 thinking models (each with one-line definition / content signal words / composition key points) organized into **10 canonical diagram families** (PY pyramid / MX matrix / CY cycle / CV curve / FL flow / CP contrast / NW network / MC mechanism / DK decision / TR tree); when note content hits a model's signal, the skill calls that model's standard diagram composition (signal → model → diagram-type three-step routing, full 101-entry signal quick-reference covering all 100 models, "diagram-content contract" QA). New text-to-image spec: five-element prompt formula (subject imagery + diagram geometry + style tokens + theme color + negative constraints), 10 family prompt templates, hard cap of ≤5 generated images per deck (cover 1 + hero ≤2 + quote background ≤2) — structured diagrams stay HTML/SVG, text-to-image only for atmosphere assets (cover / hero / quote background / section divider) — see `references/mental-models-library/INDEX.md` and `models-catalog.md`
- **v2.6 NG portrait magazine layout** — a full **magazine-grade portrait** pipeline for photography / nature / history / biography / art books, reverse-engineered from a real 148-page wildlife photography book → 60-page published-grade delivery (0 broken images / 0 clipping / 0 squeeze, PDF+PPTX 11.1MB each): 660×960px canvas (=495×720pt = 6.875×10in), NG yellow-box palette (ink `#231F20` + yellow `#FFD201` + gold/bronze/wine/red + 3-step warm paper), serif-headline / sans-label / DIN-numeral three-font-stack, black-bar+gold-star running heads; **12 magazine page templates** (cover / black TOC / chapter divider / full-bleed photo / article page with 2-column serif body + drop cap / anatomy annotation / statgrid / field-guide entries / timeline / price bars / mindmap / black quote page); **page-map method** (finished pages = ⅓~½ of source book); **Python generator sharding** (≤20KB per fragment to survive Write truncation); **6-step build pipeline** (merge → Playwright triple validation broken-img/clipping/squeeze → @2x screenshots → PDF with `in` units → PPTX with JPEG q87 rebuild −75% size → package) with a 6-entry pitfall library — see `references/ng-magazine-layout.md` and `templates/ng-magazine/` (mag.css + build-template.py + generator-template.py)
- **v2.7 HBR landscape magazine layout** — a full **magazine-grade landscape** pipeline for business journals / magazine anthologies / multi-theme collections, reverse-engineered from a real 88-page *Harvard Business Review 2025 Best-Of* delivery (source 12 issues / 2,291 pages → 88 pages = 46% of single-issue average, 0 overflow / 0 empty page / constant MediaBox, PDF 11.7MB + 88-page PPTX 16:9 dual acceptance): 612×756pt canvas (=8.5×10.5in US magazine trim), masthead-red `#E41824` + art-gold `#F09C18` + ink `#231F20` + cream `#F4F1EA` four-color DNA, sans+serif two-font-stack; **12 magazine page types** (full-bleed cover with 6-cell cover strip / 150pt giant-number chapter divider with vertical EN / asymmetric editorial opener 310pt photo column / full-page chart from original magazine / 100pt giant stat / two-column text / full-bleed photo feature / full-bleed quote / grouped TOC / 4×3 issue-overview grid + 3 SVG mega-chart components); **11-page fixed chapter rhythm** (divider→editorial→chart→stat→text×3→photo→quote→editorial flip→text); **Chrome headless print pipeline** (gradient scrims MUST be pre-rendered PNG — CSS linear-gradient over photos forces Chrome to rasterize photos into tiling Patterns, ×2.4 size); **PDF triple acceptance** (MediaBox constant / zero text overflow / zero empty page) + XObject content-hash dedup slimming (18.3→11.7MB, no in-page lossy recompression) + **PPTX same-source 16:9 rebuild**; 8-entry pitfall library — see `references/hbr-magazine-layout.md` and `templates/hbr-magazine/` (mag.css + generator-template.py + build-template.py + scrim/)

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

Say any trigger phrase to your agent: **读书笔记 / 生成笔记 / 可视化读书笔记 / reading notes / 读书笔记PPT / 读书报告 / 精华笔记 / 营销笔记 / 情绪开关 / marketing notes / 咨询级笔记 / consulting-grade notes / 设计系统 / 品牌风格 / 中文产品设计 / design system / brand style / 竖版笔记 / 杂志风笔记 / 国家地理风格 / magazine layout / portrait notes / 横版杂志 / 商业杂志版式 / 哈佛商业评论风格 / HBR风 / 期刊复刻 / landscape magazine / HBR layout**, then provide the book's raw materials (key points, golden quotes, structure).

Seven-step workflow (v2.4 adds Step 0, v2.6 adds Step 0.5 format routing, v2.7 upgrades Step 0.5 to three-way routing):

0. **Design-intelligence front-load** — detect language/audience → run `references/design-intelligence/ui-ux-pro-max/scripts/search.py "<english query>"` → load brand DESIGN.md if specified → produce a **Design Decision Sheet** (style / palette / fonts / do's & don'ts); full routing & fallbacks in `references/design-intelligence/INDEX.md`
0.5. **Pick format (v2.7 three-way)** — photography / nature / history / biography books with rich imagery → **NG portrait magazine pipeline** (`references/ng-magazine-layout.md`); business journals / magazine anthologies / multi-theme collections wanting an "original-issue replica / best-of" feel → **HBR landscape magazine pipeline** (`references/hbr-magazine-layout.md`: 612×756pt, 12 page types, 11-page chapter rhythm, Chrome headless build); single-thread methodology / data books for projection → 16:9 slides workflow below
1. **Pick archetype** — `references/content-framework.md` §3 decision tree
2. **Set tone** — Design Decision Sheet first, then `references/design-system.md` §3.2 (20-palette mapping table); marketing / emotion content → `references/emotion-marketing.md` §1 five-color spectrum directly; Chinese audience → `design-intelligence/ui-ux-pro-max-cn/SKILL.md` rules
3. **Lay out pages** — copy sections from `templates/reading-notes-template.html` (12 page types), alternate `.alt` warm-paper pages every 2–3 content pages; match content signals against the mental-models library (`references/mental-models-library/`) and compose the standard diagram for each hit model; plan ≤5 atmosphere assets (cover / hero / quote background / section divider) per the v2.5 text-to-image spec
4. **Fill components** — pick charts via `references/chart-catalog.md` decision tree (cross-validate data charts with `--domain chart`)
5. **Export** — follow `templates/output-pipelines.md`

## Structure

```
reading-notes-master/
├── SKILL.md                          # entry: workflow, checklist, error handling
├── references/
│   ├── design-tokens.md              # v2 publication-grade tokens (Stitch 9 sections)
│   ├── design-system.md              # layout / fonts / type ladder / 20 theme palettes
│   ├── visual-grammar.md             # v2 chart-first visual grammar (text budgets, text→chart mapping)
│   ├── content-framework.md          # 9 modules / 8-block template / 6 archetypes
│   ├── chart-catalog.md              # 10+6 chart components + decision trees
│   ├── case-patterns.md              # 31-corpus style archive + reuse rules
│   ├── emotion-marketing.md          # v2.1 emotion-marketing methodology library (5 switches × cases × matrix)
│   ├── consulting-craft.md           # v2.2 consulting-grade page craft (storylines × titles × data contracts × QA gates)
│   ├── graphics-toolchain.md         # v2.3 graphics asset pipeline (dual track × 7-tool registry × MCP × pitfalls)
│   ├── ng-magazine-layout.md         # v2.6 NG portrait magazine layout handbook (params / 12 page templates / page-map / generator sharding / build pipeline / pitfalls)
│   ├── hbr-magazine-layout.md        # v2.7 HBR landscape magazine layout handbook (three-way routing / 612x756pt anchors / 12 page types / 11-page chapter rhythm / Chrome headless build / pitfalls)
│   └── design-intelligence/          # v2.4 full ingestion of four design skills (INDEX.md is the entry)
│       ├── INDEX.md                  # four-layer architecture / Step 0 routing / commands / fallbacks / provenance
│       ├── ui-ux-pro-max/            # BM25 design-intelligence engine (scripts + 31 CSVs + upstream refs)
│       ├── ui-ux-pro-max-cn/         # Chinese localization design rules (pure markdown)
│       ├── awesome-design-md/        # 54 real-brand DESIGN.md specs
│       └── awesome-design/           # 20+ design-skill selection navigator
│   └── mental-models-library/        # v2.5 100 thinking models composition library (INDEX.md is the entry)
│       ├── INDEX.md                  # four-step usage / 30 signal quick-reference / text-to-image prompt spec
│       └── models-catalog.md         # 100 model profiles (definition/signals/family/composition) + 10 family templates
├── scripts/                          # v2.3 ready-to-run wrappers (auto tool discovery)
│   ├── bitmap2vector.sh              # bitmap→SVG tracing (vtracer color / potrace B&W)
│   ├── superres.sh                    # Real-ESRGAN 4× super-resolution (upscayl-bin)
│   ├── mermaid-export.sh              # mermaid→SVG/PNG/PDF (reuses local Chrome, no Chromium download)
│   └── clip-chart.sh                  # .clp text→SVG charts (asmuth/clip)
├── templates/
│   ├── reading-notes-template.html   # 16:9 publication-grade HTML skeleton v2.0
│   ├── output-pipelines.md           # PDF / PPTX / long-image export commands
│   ├── ng-magazine/                  # v2.6 NG portrait magazine assets
│   │   ├── mag.css                   # full design system (palette / 3 font stacks / 12 page components, battle-tested)
│   │   ├── build-template.py         # 6-step build pipeline (validate / screenshot / PDF / PPTX / package, pitfalls fixed)
│   │   └── generator-template.py     # generator skeleton (HD/FT/FOLIO + P.append, ≤20KB sharding)
│   └── hbr-magazine/                 # v2.7 HBR landscape magazine assets
│       ├── mag.css                   # full design system (masthead 4 colors / 2 font stacks / 12 page types / print rules)
│       ├── generator-template.py     # 12 page-type builders + 3 SVG mega-charts + P.append pattern
│       ├── build-template.py         # 6-step build (merge inline CSS / Chrome headless / triple acceptance / dedup slim / PPTX / package)
│       └── scrim/                    # 4 pre-rendered scrim PNGs (anti-Pattern key asset) + make_scrims.py regenerator
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
