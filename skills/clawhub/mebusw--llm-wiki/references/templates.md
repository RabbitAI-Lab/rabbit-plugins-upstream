# LLM-Wiki senario templates references

> When generating the file, replace the placeholders in the `<!-- ... -->` comments with the actual content entered by the user.

---

## 公共基础组件（所有场景共用）

### BASE_SCHEMA_TYPES（基础页面类型表）
```
| entity     | wiki/entities/    | Named things (people, tools, organizations, datasets) |
| concept    | wiki/concepts/    | Ideas, techniques, phenomena, frameworks              |
| source     | wiki/sources/     | Papers, articles, talks, books, blog posts            |
| query      | wiki/queries/     | Open questions under active investigation             |
| comparison | wiki/comparisons/ | Side-by-side analysis of related entities             |
| synthesis  | wiki/synthesis/   | Cross-cutting summaries and conclusions               |
| overview   | wiki/            | High-level project summary (one per project)          |
| domain     | wiki/domains/    | Topic index page that aggregates content by subject   |
```

### BASE_NAMING（命名规范）
```
- Files: `kebab-case.md`
- Entities: match official name where possible (e.g., `openai.md`, `gpt-4.md`)
- Concepts: descriptive noun phrases (e.g., `chain-of-thought.md`)
- Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
- Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)
- Domains: short topic phrases in kebab-case (e.g., `deep-learning.md`, `software-engineering.md`)
```

### BASE_FRONTMATTER（前置元数据规范）
All pages must contain YAML frontmatter：
```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview | domain
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填，引用 wiki/domains/ 下索引页

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Source pages also includes:
```yaml
authors: []
year: YYYY
url: ""
venue: ""
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty    # 顶层领域留空 / null
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```


> ⚠️ **Frontmatter prohibits the use of wikilinks**: Fields such as `original_file` and `source` that need to reference other pages should be annotated with `[[wikilink]]` in the main text, or replaced with a regular string. Obsidian cannot render `[[...]]` in YAML.
> ⚠️ **Every content page MUST declare `domains:`** — without it, the page is invisible to domain navigation and the LINT will flag it.

### BASE_INDEX_FORMAT（**双层索引，根治膨胀**）
```
`wiki/index.md` 列出 **顶层领域**（没有 parent 的领域），不列具体页面。

# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 312 across 14 domains.

## Top-level Domains
- [[deep-learning]] — 神经网络与表示学习 (24 pages)
- [[software-engineering]] — 软件开发方法与工程实践 (31 pages)
- [[ai-ethics]] — 人工智能伦理与社会影响 (8 pages)

## Recently Updated
- 2026-05-30 [[transformer]] — added CoT citations
- 2026-05-28 [[karpathy]] — new entity page
```

每个 `wiki/domains/{domain}.md` 列出该领域内的全部内容（按类型分组）：
```
# Deep Learning

> Brief description. 24 pages, last updated 2026-05-30.

## Concepts
- [[transformer]] — 自注意力序列模型
- [[cnn]] — 卷积神经网络

## Entities
- [[openai]] — 主要研究机构
- [[ilya-sutskever]] — 关键人物

## Sources
- [[vaswani-2017-attention]] — 奠基论文

## Synthesis
- [[frontier-models-2024]] — 跨领域综述

## Related
- Parent: [[machine-learning]]
- Children: [[transformers]], [[cnns]]
```

### BASE_META_FORMAT（领域元数据注册表）
`wiki/domains/_meta.json` 记录所有领域、父子关系、统计、演化历史：
```json
{
  "version": 1,
  "domains": {
    "deep-learning": {
      "parent": "machine-learning",
      "description": "神经网络与表示学习",
      "created": "2026-01-15",
      "updated": "2026-05-30",
      "page_count": 24
    },
    "machine-learning": {
      "parent": null,
      "description": "机器学习总体",
      "created": "2026-01-15",
      "updated": "2026-04-12",
      "page_count": 3
    }
  },
  "history": [
    {"date": "2026-01-15", "action": "create", "domain": "machine-learning", "reason": "INIT 初始领域"},
    {"date": "2026-01-15", "action": "create", "domain": "deep-learning", "reason": "INIT 初始领域"},
    {"date": "2026-04-12", "action": "split", "from": "machine-learning", "to": "deep-learning", "reason": "概念数超过 20"}
  ]
}
```

> **关键约定**：`_meta.json` 是领域层的真实状态。`wiki/index.md` 是它的渲染结果。每次领域有变动（创建 / 重命名 / 拆分 / 合并 / 删除），**先**更新 `_meta.json`，**再**渲染 `index.md`，**最后**通知相关领域索引页。

### BASE_LOG_FORMAT
```
`wiki/log.md` records activity in reverse chronological order:
## YYYY-MM-DD
- Action taken / finding noted
```

### BASE_CROSSREF（跨引用规则）
```
- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in **its domain index page** (`wiki/domains/{domain}.md`), not directly in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources in the `## Related` section
- **Every content page MUST be reachable from at least one domain index** — otherwise LINT will flag it as orphaned
```

### BASE_RELATED_SECTION（相关页面规范）

`related:` will **not be placed in the YAML frontmatter** (Obsidian cannot render wikilinks in the YAML formatter). Instead, use a related page section at the end of the page body.

```markdown
## Related
- [[page-slug]] — Briefly explain the reason for the association (optional)
- [[another page]]
```

This section must be included on every page. If there is no related content, write `N/A`.

### BASE_CONTRADICTION（矛盾处理）
```
When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists
```

---

## Senario A: Research🔬

`extraDirs: ["wiki/methodology", "wiki/findings", "wiki/thesis"]`

`initialDomains: ["<主题领域>", "methodology", "open-questions"]`  ← INIT 时按用户输入替换

### schema.md
```markdown
# Wiki Schema — Research Deep-Dive

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity     | wiki/entities/    | Named things (people, tools, organizations, datasets) |
| concept    | wiki/concepts/    | Ideas, techniques, phenomena, frameworks |
| source     | wiki/sources/     | Papers, articles, talks, books, blog posts |
| query      | wiki/queries/     | Open questions under active investigation |
| comparison | wiki/comparisons/ | Side-by-side analysis of related entities |
| synthesis  | wiki/synthesis/   | Cross-cutting summaries and conclusions |
| overview   | wiki/             | High-level project summary (one per project) |
| **domain**     | wiki/domains/    | Topic index page that aggregates content by subject |
| thesis     | wiki/thesis/      | Working hypothesis and its evolution over time |
| methodology | wiki/methodology/ | Research methods, protocols, and study designs |
| finding    | wiki/findings/    | Individual empirical results or observations |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible (e.g., `openai.md`, `gpt-4.md`)
- Concepts: descriptive noun phrases (e.g., `chain-of-thought.md`)
- Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
- Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)
- Theses: hypothesis as slug (e.g., `scaling-improves-reasoning.md`)
- Methodologies: method name (e.g., `systematic-review.md`, `ablation-study.md`)
- Findings: descriptive slug (e.g., `larger-models-better-few-shot.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填：所属领域

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Thesis pages also include:
```yaml
confidence: low | medium | high
status: speculative | supported | refuted | settled
```

Finding pages also include:
```yaml
source: "[[source-slug]]"
confidence: low | medium | high
replicated: true | false | null
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```

## Index Format (双层索引)

`wiki/index.md` **只列顶层领域**，不列具体页面。每个领域自己的 `wiki/domains/{domain}.md` 列出该领域内的全部内容。`wiki/domains/_meta.json` 是真实状态。

示例 `wiki/index.md`：
```markdown
# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 312 across 14 domains.

## Top-level Domains
- [[deep-learning]] — 神经网络与表示学习 (24 pages)
- [[software-engineering]] — 软件开发方法与工程实践 (31 pages)
- [[ai-ethics]] — 人工智能伦理与社会影响 (8 pages)

## Recently Updated
- 2026-05-30 [[transformer]] — added CoT citations
```

示例 `wiki/domains/deep-learning.md`：
```markdown
---
title: Deep Learning
type: domain
parent: machine-learning
children: [transformers, cnns]
description: 神经网络与表示学习
created: 2026-01-15
updated: 2026-05-30
---

# Deep Learning

## Concepts
- [[transformer]] — 自注意力序列模型
- [[cnn]] — 卷积神经网络

## Entities
- [[openai]] — 主要研究机构

## Sources
- [[vaswani-2017-attention]] — 奠基论文

## Findings
- [[larger-models-better-few-shot]] — 规模律相关结果

## Methodology
- [[ablation-study]] — 消融研究方法

## Related
- Parent: [[machine-learning]]
- Children: [[transformers]], [[cnns]]
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD
- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources in the `## Related` section
- Findings link back to their source via the `source:` frontmatter field
- Thesis pages reference supporting and refuting findings in the `## Related` section
- Methodology pages are cited by the findings that used them

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Research-Specific Conventions

- Keep the thesis pages updated as evidence accumulates — they are living documents
- Every finding should assess replication status when known
- Methodology pages explain the *why* (rationale) not just the *how*
- Distinguish between direct evidence and inference in finding pages

## Language Rule
- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English. Wiki page titles, content, and descriptions should all be in the same language as the source material.
```

### purpose.md
```markdown
# Project Purpose — Research Deep-Dive

## Research Question

<!-- State the central question this research aims to answer. Be specific and falsifiable. -->

>

## Hypothesis / Working Thesis

<!-- Your current best guess. This will evolve — update it as evidence accumulates. -->

>

## Background

<!-- What prior work or context motivates this research? What gap does it fill? -->

## Sub-questions

<!-- Break down the main question into tractable sub-questions. -->

1.
2.
3.
4.

## Scope

**In scope:**
-

**Out of scope:**
-

## Methodology

<!-- How will you investigate this? What types of sources or experiments are relevant? -->

-

## Success Criteria

<!-- How will you know when you have a satisfying answer? -->

-

## Current Status

> Not started — update this section as research progresses.
```

---

## Senario B: Reading📚

`extraDirs: ["wiki/characters", "wiki/themes", "wiki/plot-threads", "wiki/chapters"]`

`initialDomains: ["<书名或题材>", "themes", "characters"]`  ← INIT 时按用户输入替换

### schema.md
```markdown
# Wiki Schema — Reading a Book

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity      | wiki/entities/     | Named things (people, tools, organizations, datasets) |
| concept     | wiki/concepts/     | Ideas, techniques, phenomena, frameworks |
| source      | wiki/sources/      | Papers, articles, talks, books, blog posts |
| query       | wiki/queries/      | Open questions under active investigation |
| comparison  | wiki/comparisons/  | Side-by-side analysis of related entities |
| synthesis   | wiki/synthesis/    | Cross-cutting summaries and conclusions |
| overview    | wiki/              | High-level project summary (one per project) |
| **domain**  | wiki/domains/      | Topic index page that aggregates content by subject |
| character   | wiki/characters/   | People and figures in the book |
| theme       | wiki/themes/       | Recurring ideas, motifs, and symbolic threads |
| plot-thread | wiki/plot-threads/ | Storylines or narrative arcs being tracked |
| chapter     | wiki/chapters/     | Per-chapter notes and summaries |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible
- Concepts: descriptive noun phrases
- Sources: `author-year-slug.md`
- Queries: question as slug
- Characters: character name in kebab-case (e.g., `elizabeth-bennet.md`)
- Themes: thematic noun phrase (e.g., `social-class-mobility.md`, `deception-vs-honesty.md`)
- Plot threads: arc description (e.g., `darcys-redemption-arc.md`)
- Chapters: `ch-NN-slug.md` (e.g., `ch-01-opening-scene.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填：所属领域

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Character pages also include:
```yaml
first_appearance: "Ch. N"
role: protagonist | antagonist | supporting | minor
```

Chapter pages also include:
```yaml
chapter: N
pages: "1-24"
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```

## Index Format (双层索引)

`wiki/index.md` **只列顶层领域**，不列具体页面。每个领域自己的 `wiki/domains/{domain}.md` 列出该领域内的全部内容。`wiki/domains/_meta.json` 是真实状态。

示例 `wiki/index.md`：
```markdown
# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 312 across 14 domains.

## Top-level Domains
- [[pride-and-prejudice]] — 傲慢与偏见整书主题 (18 pages)
- [[regency-romance]] — 时代背景 (6 pages)
- [[austen-themes]] — 奥斯汀作品母题 (4 pages)

## Recently Updated
- 2026-05-30 [[elizabeth-bennet]] — added Ch.34 observations
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD
- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources in the `## Related` section
- Chapter notes reference characters appearing in that chapter in the `## Related` section
- Theme pages link to the chapters where the theme is most prominent
- Plot thread pages list chapters that advance the arc

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Reading-Specific Conventions

- Chapter pages are written during or immediately after reading — capture fresh reactions
- Distinguish between plot summary and personal interpretation in chapter notes
- Theme pages should track *development* across the book, not just state that a theme exists
- Flag unresolved plot threads with status: `open` until resolved
- Note page numbers for important quotes to enable re-finding later

## Language Rule
- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English.
```

### purpose.md
```markdown
# Project Purpose — Reading

## Book Details

**Title:**
**Author:**
**Year:**
**Genre:**

## Why I'm Reading This

<!-- What drew you to this book? What do you hope to get from it? -->

## Key Themes to Track

<!-- What thematic threads do you expect or want to follow? -->

1.
2.
3.

## Questions Going In

<!-- What do you want answered or explored by the end? -->

1.
2.

## Reading Pace

**Started:**
**Target finish:**
**Current chapter:**

## First Impressions

<!-- Update after first chapter or first sitting. -->

>

## Final Takeaways

<!-- Fill in when finished. What did this book teach you? -->

>
```

---

## Senario C: Personal Growth 🌱

`extraDirs: ["wiki/goals", "wiki/habits", "wiki/reflections", "wiki/journal"]`

`initialDomains: ["<生活领域1>", "<生活领域2>", "self-knowledge"]`  ← INIT 时按用户输入替换

### schema.md
```markdown
# Wiki Schema — Personal Growth

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity     | wiki/entities/     | Named things (people, tools, organizations, datasets) |
| concept    | wiki/concepts/     | Ideas, techniques, phenomena, frameworks |
| source     | wiki/sources/      | Papers, articles, talks, books, blog posts |
| query      | wiki/queries/      | Open questions under active investigation |
| comparison | wiki/comparisons/  | Side-by-side analysis of related entities |
| synthesis  | wiki/synthesis/    | Cross-cutting summaries and conclusions |
| overview   | wiki/              | High-level project summary (one per project) |
| **domain** | wiki/domains/      | Topic index page that aggregates content by subject |
| goal       | wiki/goals/        | Specific outcomes you are working toward |
| habit      | wiki/habits/       | Recurring behaviours and their tracking |
| reflection | wiki/reflections/  | Periodic reviews and lessons learned |
| journal    | wiki/journal/      | Freeform daily or session entries |

## Naming Conventions

- Files: `kebab-case.md`
- Goals: outcome as slug (e.g., `run-a-marathon.md`, `learn-spanish.md`)
- Habits: behaviour name (e.g., `daily-meditation.md`, `morning-pages.md`)
- Reflections: type + date (e.g., `weekly-2024-03.md`, `quarterly-2024-q1.md`)
- Journal: date slug (e.g., `2024-03-15.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填：所属领域

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Goal pages also include:
```yaml
target_date: YYYY-MM-DD
status: active | paused | achieved | abandoned
progress: 0-100
```

Habit pages also include:
```yaml
frequency: daily | weekly | monthly
streak: N
status: active | paused | dropped
```

Reflection pages also include:
```yaml
period: weekly | monthly | quarterly | annual
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```

## Index Format (双层索引)

`wiki/index.md` **只列顶层领域**，不列具体页面。每个领域自己的 `wiki/domains/{domain}.md` 列出该领域内的全部内容。`wiki/domains/_meta.json` 是真实状态。

示例 `wiki/index.md`：
```markdown
# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 187 across 9 domains.

## Top-level Domains
- [[career]] — 职业发展 (32 pages)
- [[health]] — 身体健康 (18 pages)
- [[mindset]] — 认知与心理 (24 pages)
- [[relationships]] — 人际关系 (15 pages)

## Recently Updated
- 2026-05-30 [[2026-q1-review]] — Q1 季度回顾
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD
- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Reflection pages reference the goals and habits reviewed during that period
- Goals link to the habits that support them in the `## Related` section
- Journal entries can reference goals and reflections inline with `[[slug]]`

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Personal Growth Conventions

- Be honest in journal and reflection entries — this wiki is for you, not an audience
- Update goal progress fields regularly; stale data is worse than no data
- Distinguish between outcome goals (what you want) and process goals (what you will do)
- Reflect on *why* habits succeed or fail, not just whether they did
- Use the synthesis directory for cross-cutting insights that span multiple goals or periods

## Language Rule
- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English.
```

### purpose.md
```markdown
# Project Purpose — Personal Growth

## Focus Areas

<!-- What areas of your life or self are you actively working on? -->

1.
2.
3.

## Motivation

<!-- Why now? What prompted you to start this wiki? -->

## Current Goals (Summary)

<!-- High-level list — create detailed goal pages in wiki/goals/ -->

- [ ]
- [ ]
- [ ]

## Active Habits

<!-- High-level list — create detailed habit pages in wiki/habits/ -->

-
-

## Review Cadence

**Daily journal:** Yes / No
**Weekly reflection:**
**Monthly reflection:**
**Quarterly reflection:**

## Guiding Principles

<!-- What values or principles guide your growth work? -->

1.
2.
3.

## This Year's Theme

<!-- One phrase or sentence that captures your intention for the year. -->

>
```

---

## Senario D：Business / Team💼

`extraDirs: ["wiki/meetings", "wiki/decisions", "wiki/projects", "wiki/stakeholders"]`

`initialDomains: ["<业务领域1>", "<业务领域2>", "operations"]`  ← INIT 时按用户输入替换

### schema.md
```markdown
# Wiki Schema — Business / Team

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity      | wiki/entities/     | Named things (people, tools, organizations, datasets) |
| concept     | wiki/concepts/     | Ideas, techniques, phenomena, frameworks |
| source      | wiki/sources/      | Papers, articles, talks, books, blog posts |
| query       | wiki/queries/      | Open questions under active investigation |
| comparison  | wiki/comparisons/  | Side-by-side analysis of related entities |
| synthesis   | wiki/synthesis/    | Cross-cutting summaries and conclusions |
| overview    | wiki/              | High-level project summary (one per project) |
| **domain**  | wiki/domains/      | Topic index page that aggregates content by subject |
| meeting     | wiki/meetings/     | Meeting notes, agendas, and action items |
| decision    | wiki/decisions/    | Architectural or strategic decisions (ADR-style) |
| project     | wiki/projects/     | Project briefs, status, and retrospectives |
| stakeholder | wiki/stakeholders/ | People, teams, and organisations involved |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible
- Concepts: descriptive noun phrases
- Sources: `author-year-slug.md`
- Meetings: `YYYY-MM-DD-slug.md` (e.g., `2024-03-15-sprint-planning.md`)
- Decisions: `NNN-slug.md` (e.g., `001-adopt-typescript.md`)
- Projects: descriptive slug (e.g., `payments-redesign.md`)
- Stakeholders: name or team in kebab-case (e.g., `alice-chen.md`, `platform-team.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填：所属领域

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Meeting pages also include:
```yaml
date: YYYY-MM-DD
attendees: []
action_items: []
```

Decision pages also include:
```yaml
status: proposed | accepted | deprecated | superseded
deciders: []
date: YYYY-MM-DD
supersedes: ""   # slug of ADR this replaces, if any
```

Project pages also include:
```yaml
status: planned | active | on-hold | complete | cancelled
owner: ""
start_date: YYYY-MM-DD
target_date: YYYY-MM-DD
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```

## Index Format (双层索引)

`wiki/index.md` **只列顶层领域**，不列具体页面。每个领域自己的 `wiki/domains/{domain}.md` 列出该领域内的全部内容。`wiki/domains/_meta.json` 是真实状态。

示例 `wiki/index.md`：
```markdown
# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 412 across 16 domains.

## Top-level Domains
- [[platform-team]] — 平台团队工作 (58 pages)
- [[product-strategy]] — 产品战略 (24 pages)
- [[customer-research]] — 用户研究 (31 pages)
- [[engineering-practices]] — 工程实践 (45 pages)

## Recently Updated
- 2026-05-30 [[2026-05-28-sprint-review]] — Sprint review 记录
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD
- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Meeting notes reference attendees via `attendees:` frontmatter and `[[stakeholder-slug]]` links
- Decision pages link to the meetings where the decision was discussed
- Project pages link to their key decisions in the `## Related` section
- Stakeholder pages list projects and decisions they are involved in

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Business-Specific Conventions

- Write meeting notes during or within 24 hours — memory fades fast
- Action items must have a named owner and due date to be actionable
- Decision pages capture *context and consequences*, not just the decision itself
- Deprecated decisions should link to the decision that superseded them
- Projects should have a retrospective section added on completion

## Language Rule
- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English.
```

### purpose.md
```markdown
# Project Purpose — Business / Team

## Business Context

**Organisation / Team:**
**Domain:**
**Time period covered:**

## Objectives

<!-- What are the top-level business objectives this wiki supports? -->

1.
2.
3.

## Key Projects

<!-- High-level list — create detailed pages in wiki/projects/ -->

-
-

## Key Stakeholders

<!-- Who are the primary people or teams involved? -->

-
-

## Open Decisions

<!-- Decisions currently in flight — create ADR pages in wiki/decisions/ -->

-
-

## Metrics / Success Criteria

<!-- How does the team measure progress toward its objectives? -->

-

## Constraints and Risks

<!-- Known constraints (budget, time, org) and risks to track -->

-

## Review Cadence

**Weekly sync notes:**
**Monthly status update:**
**Quarterly retrospective:**
```

---

## Senario E：general 📄

`extraDirs: []`

`initialDomains: ["<主题领域1>", "<主题领域2>"]`  ← INIT 时按用户输入替换

### schema.md
```markdown
# Wiki Schema

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity     | wiki/entities/    | Named things (people, tools, organizations, datasets) |
| concept    | wiki/concepts/    | Ideas, techniques, phenomena, frameworks |
| source     | wiki/sources/     | Papers, articles, talks, books, blog posts |
| query      | wiki/queries/     | Open questions under active investigation |
| comparison | wiki/comparisons/ | Side-by-side analysis of related entities |
| synthesis  | wiki/synthesis/   | Cross-cutting summaries and conclusions |
| overview   | wiki/             | High-level project summary (one per project) |
| **domain** | wiki/domains/     | Topic index page that aggregates content by subject |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible (e.g., `openai.md`, `gpt-4.md`)
- Concepts: descriptive noun phrases (e.g., `chain-of-thought.md`)
- Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
- Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
domains: [domain-slug-1, domain-slug-2]   # ★ 必填：所属领域

created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Source pages also include:
```yaml
authors: []
year: YYYY
url: ""
venue: ""
```

Domain pages also include:
```yaml
parent: parent-domain-slug-or-empty
children: [child-1, child-2]
aliases: [alias-1, alias-2]
description: 一句话描述本领域
```

## Index Format (双层索引)

`wiki/index.md` **只列顶层领域**，不列具体页面。每个领域自己的 `wiki/domains/{domain}.md` 列出该领域内的全部内容。`wiki/domains/_meta.json` 是真实状态。

示例 `wiki/index.md`：
```markdown
# Wiki Index

> Last updated: YYYY-MM-DD. Pages total: 87 across 5 domains.

## Top-level Domains
- [[machine-learning]] — 机器学习 (32 pages)
- [[philosophy]] — 哲学 (18 pages)
- [[cooking]] — 烹饪 (12 pages)
- [[travel]] — 旅行 (15 pages)
- [[music-theory]] — 音乐理论 (10 pages)

## Recently Updated
- 2026-05-30 [[sourdough]] — updated hydration notes
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD
- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources in the `## Related` section

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Language Rule
- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English.
```

### purpose.md
```markdown
# Project Purpose

## Goal

<!-- What are you trying to understand or build? -->

## Key Questions

<!-- List the primary questions driving this project -->

1.
2.
3.

## Scope

**In scope:**
-

**Out of scope:**
-

## Thesis

<!-- Your current working hypothesis or conclusion (update as the project progresses) -->

> TBD
```

---

## 领域层（Domain Layer）—— 独立于场景的通用组件

> 本节是 LLM Wiki 架构的核心创新，借鉴自 dragonfly-llmwiki 的领域系统。**所有场景共用**——本节优先于场景模板，场景模板中提到的领域行为以本节为准。

### 为什么需要领域层

| 不用领域层（传统 wiki） | 用领域层（本系统） |
|---|---|
| `index.md` 列出所有页面 | `index.md` 只列 5–20 个领域 |
| 100 页 → 100 行 | 100 页 → 5–10 个领域条目 |
| 1000 页 → 1000 行（**不可读**） | 1000 页 → 20 个领域条目（**依旧可读**） |
| 难以跨主题聚合 | 一个领域聚合概念/实体/来源/分析 |
| 主题混乱时无法重组 | 领域可拆分/合并/重命名 |

### 领域三件套

每次**新建**或**演化**领域时，必须同步维护以下三个文件：

1. **`wiki/domains/{domain-slug}.md`** — 领域索引页（人类可读）
2. **`wiki/domains/_meta.json`** — 注册表（机器可读的真实状态）
3. **`wiki/index.md`** — 顶层领域列表（`_meta.json` 的渲染输出）

**任何一处变动都必须在另外两处同步。** 改动顺序：`_meta.json` → 索引页 → `index.md`。

### 领域索引页完整模板

```markdown
---
title: Deep Learning
type: domain
parent: machine-learning
children: [transformers, cnns, recurrent-nets]
aliases: [DL, deep-learning]
description: 神经网络与表示学习
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Deep Learning

> 神经网络与表示学习 — 24 pages, last updated 2026-05-30

## Concepts
- [[transformer]] — 自注意力序列模型
- [[cnn]] — 卷积神经网络
- [[rnn]] — 循环神经网络

## Entities
- [[openai]] — 主要研究机构
- [[ilya-sutskever]] — 关键人物
- [[yann-lecun]] — CNN 发明者

## Sources
- [[vaswani-2017-attention]] — 奠基论文
- [[he-2016-resnet]] — 残差网络

## Methodology
- [[ablation-study]] — 消融研究方法

## Findings
- [[scaling-laws-empirical]] — 规模律实证

## Synthesis
- [[frontier-models-2024]] — 跨领域综述

## Related Domains
- Parent: [[machine-learning]]
- Children: [[transformers]], [[cnns]], [[recurrent-nets]]
- Siblings: [[nlp]], [[computer-vision]]

## Changelog
- 2026-04-12: split out from [[machine-learning]] (概念数 > 20)
- 2026-01-15: created
```

### `_meta.json` 完整模板

```json
{
  "version": 1,
  "domains": {
    "machine-learning": {
      "parent": null,
      "description": "机器学习总体",
      "created": "2026-01-15",
      "updated": "2026-04-12",
      "page_count": 3
    },
    "deep-learning": {
      "parent": "machine-learning",
      "description": "神经网络与表示学习",
      "created": "2026-01-15",
      "updated": "2026-05-30",
      "page_count": 24
    },
    "transformers": {
      "parent": "deep-learning",
      "description": "基于自注意力的序列模型",
      "created": "2026-04-12",
      "updated": "2026-05-30",
      "page_count": 8
    }
  },
  "history": [
    {
      "date": "2026-01-15",
      "action": "create",
      "domain": "machine-learning",
      "reason": "INIT 初始领域"
    },
    {
      "date": "2026-01-15",
      "action": "create",
      "domain": "deep-learning",
      "reason": "INIT 初始领域"
    },
    {
      "date": "2026-04-12",
      "action": "split",
      "from": "deep-learning",
      "to": ["transformers", "recurrent-nets"],
      "reason": "概念数超过 20，主题可清晰切分"
    }
  ]
}
```

### 领域演化操作

| 操作 | 触发条件 | `_meta.json` action | 额外动作 |
|------|---------|---------------------|---------|
| 创建 | 新主题不属于任何现有领域 | `create` | 新建索引页 + 注册 |
| 重命名 | 同义词 / 命名不规范 | `rename` | 旧名进入 `aliases`；其他页面 `domains:` 同步更新 |
| 拆分 | 概念 > 20 且子主题清晰 | `split` | 新领域 + 父领域保留；被拆走的页面 `domains:` 同步 |
| 合并 | 重叠 > 30% 或都 < 3 个 | `merge` | 保留目标领域；源领域页面 `domains:` 同步；源领域可保留为 alias 或删除 |
| 删除 | 领域为空且不再需要 | `delete` | 仅在 `_meta.json` 中移除，不删索引页（保留作历史） |

### 演化操作示例

**场景**：领域 `ai` 概念数达到 25，提议拆分为 `ai-fundamentals`、`deep-learning`、`ai-applications`。

**步骤**（每步必须先告知用户）：

1. 列出 25 个概念及其新归属
2. 用户确认后：
   - 创建 `wiki/domains/ai-fundamentals.md`、`deep-learning.md`、`ai-applications.md`
   - 更新 `wiki/domains/ai.md`：移除被拆走的概念，只保留剩余
   - 更新 `_meta.json`：
     ```json
     {"date": "2026-06-01", "action": "split", "from": "ai", "to": ["ai-fundamentals", "deep-learning", "ai-applications"], "reason": "概念数 > 20"}
     ```
   - 更新每个被拆走页面的 `domains:` 字段（替换 `ai` 为新领域）
   - 重建 `wiki/index.md`
3. 在 `wiki/log.md` 追加：
   ```
   ## [2026-06-01] lint | 拆分领域 ai → ai-fundamentals, deep-learning, ai-applications
   原因：概念数 25 > 20，主题可清晰切分
   影响：23 个页面更新 domains 字段
   ```

### 场景 → 初始领域映射表（INIT 时使用）

| 场景 | 推荐初始领域（用户可改写） |
|------|---------------------------|
| Research | 用户填写的主题领域 + `methodology` + `open-questions` |
| Reading | 书名/题材 + `themes` + `characters` |
| Personal Growth | 用户填写的 1-3 个生活领域 + `self-knowledge` |
| Business/Team | 业务领域 1-N + `operations` |
| General | 用户填写的 1-N 个主题领域 |

> **关键**：场景专属子目录（methodology / characters / meetings / goals 等）是**类型**层，**领域**层是正交的话题分类。一个 methodology 页面可以属于任何领域；一个领域可以同时包含 concept、entity、source、methodology 等多种类型页面。

### 为什么这套架构能"支持比原文更多的数据量"

原始 LLM Wiki 的方案（dragonfly-llmwiki）：
- `wiki/index.md` 只列顶层领域 → 稳定的小文件
- `wiki/domains/{name}.md` 列具体页面 → 局部大但局部可控
- 领域可演化 → 适应增长

本系统在此基础上**强化了**：
- 增加了 `_meta.json` 真实状态层（机器可校验，避免 LLM 改 index 时漏改 meta）
- 领域健康检查内置到 LINT 操作（自动发现需拆/合/重命名的情况）
- 演化操作标准化（动作 + 日期 + 原因 + 影响记录在 `history`，可审计）
- 所有内容页强制 `domains:` 字段（防止"在 wiki 但不在任何领域"的孤儿）

**理论上支持**：任意数量的页面（领域数增长很慢——可能数月一个；内容页增长很快）。1000 页面 / 20 领域，index.md 仍只有 20 行。
