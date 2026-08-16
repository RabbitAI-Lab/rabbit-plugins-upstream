---
name: style-extractor
version: 2.0.0
title: "Style Extractor — UI 视觉风格提取与 Design Token 系统构建"
description: "从 URL、截图或前端项目源码中逆向提取 UI 视觉风格，产出三层 Design Token 系统（Primitive → Semantic → Component），封装为可复用的 WorkBuddy 通用风格技能。"
author: namepain
type: command
category: development
tags:
  - ui
  - design-system
  - design-tokens
  - css
  - visual-style
invocation: "/style-extractor"
difficulty: intermediate
permissions:
  read:
    - project files
    - web pages
  write:
    - project files
  network: required
examples:
  - input: "/style-extractor https://linear.app 的设计风格"
    output: "抓取页面 CSS → 提取设计变量 → 生成三层 Token → 封装 brand-style-linear 技能"
  - input: "/style-extractor 这张截图里的 UI 风格给我封装成 skill"
    output: "多模态分析截图 → 推断配色/排版/间距 → 标志为证据 A 级 → 生成技能供用户确认"
  - input: "/style-extractor ./my-nextjs-app 的 tailwind 主题"
    output: "扫描 tailwind.config + globals.css → 提取 Primitive 色阶/Semantic 角色 → 生成品牌技能"
agent_created: true
---

# Style Extractor

Extract a complete design system from any web page, image, or codebase and package it as a reusable WorkBuddy style skill.

## Overview

This skill provides a multi-phase pipeline with optional mode splitting:

| Phase | Mode | Output |
|-------|------|--------|
| Phase 1 — Audit | Audit-only mode | Evidence inventory, raw values, duplicates, drift, exceptions |
| Phase 2 — Design | Design mode | Three-layer tokens (Primitive → Semantic → Component), naming, theme mappings |
| Phase 3 — Package | Generate mode | Complete WorkBuddy style skill with all references |
| Phase 4 — Verify | Verify mode | Format, reference, theme, and state validation + optional demo page |

By default, run all phases. The user can request audit-only, design-only, or verify-only mode.

## Core Principles

### Evidence Grading

Every extracted value MUST be tagged with one of four evidence levels:

| Grade | Label | Meaning |
|-------|-------|---------|
| **D** | 已定义 (Defined) | Found in existing CSS variables, theme config, or design token files |
| **M** | 已测量 (Measured) | Confirmed from source code references, browser computed styles, or rendered output |
| **I** | 有依据的归纳 (Inferred) | Reasonably deduced from repeated patterns across multiple pages/components |
| **A** | 暂时假设 (Assumed) | Best guess based on limited data; MUST be explicitly flagged for user review |

Never present an assumed value as a confirmed fact. The evidence grade determines how aggressively the token can be used in migration.

### Three-Layer Token Architecture

Tokens are organized into three layers, NOT a flat list:

```
Primitive (原材料)    →  color.blue.600, space.4, radius.md, font.size.lg
                            ↑ reference only — do not use in components directly
Semantic (设计角色)   →  color.action.primary, color.bg.surface, space.container.padding
                            ↑ components use these
Component (组件特化)  →  button.primary.bg.default, input.border.focus, dialog.shadow
                            ↑ only when semantic tokens are insufficient
```

**Why three layers matters:**
- `#FFFFFF` in light theme = page background; in dark theme = inverse text. Same primitive value, DIFFERENT semantic roles. If merged into one flat `--white`, theme switching breaks.
- `color.blue.600` could be used for buttons, links, and focus rings. If a component references the primitive directly, changing the brand color requires hunting down every usage. If it references `color.action.primary` (which maps to `color.blue.600`), it changes everywhere at once.

**Layer decision rules:**
- Primitive: Raw materials (color scales, spacing steps, font sizes, radius steps, duration values). Named by what they ARE, not where they're used.
- Semantic: Design roles (backgrounds, text levels, borders, actions, statuses). Named by what they DO. Must reference primitives, never copy values.
- Component: Per-component overrides that can't be expressed by semantic tokens alone. Only create when a component has a genuinely independent design decision.

**Do NOT create a component token when:**
- The component value equals a semantic token → just use the semantic token directly
- The component value could be expressed by combining existing semantic tokens
- You're creating an alias that adds no governance value (e.g., `card.background.default` when it's always `color.bg.surface`)

## Quick Start

When the user provides an input, determine the type and follow the corresponding workflow:

| Input Type | Detection | Workflow Section |
|---|---|---|
| URL | starts with `http://` or `https://` | [URL Extraction](#url-extraction) |
| Screenshot / Image | file path ending in `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif` | [Screenshot Extraction](#screenshot-extraction) |
| Project Directory | local folder path | [Project Source Extraction](#project-source-extraction) |

If input type is ambiguous, ask the user to clarify.

## Phase 0 — Determine Output Name and Mode

Before extraction:
1. Ask the user: **"What should I name this style? (e.g., `notion`, `stripe`, `my-brand`)"**
2. The output skill directory will be named `brand-style-{name}`
3. If only one style is being extracted and the user doesn't specify, infer from the source
4. If the user wants audit-only, stop after Phase 2. If verify-only, start from Phase 4.

## Phase 1 — Audit: Ingest and Inventory

### URL Extraction

When input is a URL:

1. **Fetch the page:** Use WebFetch to retrieve the HTML content of the target URL
2. **Fetch CSS:** Use WebFetch on any linked CSS file URLs found in the HTML
3. **Catalog raw values** with evidence grades:
   - **Colors:** All hex/rgb/hsl values, noting which come from `--*` variables (grade D), which are inline (grade M), and which are computed (grade M)
   - **Typography:** Font families, sizes, weights, line-heights, letter-spacing — note `@font-face` vs system stack vs Google Fonts
   - **Spacing:** Padding/margin patterns, gap values, typical container widths
   - **Shadows:** box-shadow values with color, offset, blur, spread
   - **Border Radius:** All border-radius values, noting which elements use them
   - **Layout:** Flex/grid patterns, column counts, responsive breakpoints
   - **Components:** Recurring patterns with their CSS properties

**Tailwind Detection:** If the page uses Tailwind CSS, map utility classes to computed values and document both the class name and the equivalent CSS. Grade these as D (defined in config) or M (observed in DOM).

**CSS Variable Detection:** If the page uses CSS custom properties, extract the full variable hierarchy. These are grade D. Note any variables that reference other variables (e.g., `--color-text-primary: var(--gray-900)`).

### Screenshot Extraction

When input is a screenshot/image:

1. **Read the image:** Use the Read tool to analyze the screenshot visually
2. **Extract visual properties** (all grade I or A — inferred from visual, not exact):
   - **Color palette:** Dominant colors, accent colors, background/surface colors, text colors
   - **Typography:** Font styles observed, size hierarchy, weight usage
   - **Spacing:** Visual spacing patterns, content density
   - **Shape language:** Rounded vs sharp corners, shadow usage, border treatment
   - **Component patterns:** Cards, buttons, navigation, forms
3. **Explicitly flag** that screenshot extraction yields inferred values (grade I/A). Invite the user to refine exact hex codes and font names.

### Project Source Extraction

When input is a local project directory:

1. **Discover style files:** Use Glob to find:
   - `**/*.css`, `**/*.scss`, `**/*.less` → grade D/M
   - `tailwind.config.{js,ts,mjs,cjs}` → grade D
   - `**/theme.{js,ts,tsx}`, `**/tokens.{js,ts,json}` → grade D
   - `**/GlobalStyles.{js,ts,tsx}`, `**/styled.{js,ts,tsx}` → grade M
2. **Read key files:** Prioritize theme/config files (grade D), then component styles (grade M)
3. **Parse and catalog:**
   - **Tailwind config:** `theme.extend.colors`, `theme.extend.fontFamily`, etc. → grade D
   - **CSS variables:** All `:root { }` blocks → grade D, but note if variables reference other variables
   - **Theme objects:** JS/TS theme definitions → grade D
   - **Global styles:** body defaults, heading resets → grade M
4. **If the project can run**, open key pages and record computed styles (upgrade M → D where confirmed)
5. **If the project cannot run**, explicitly state this and keep browser-dependent values at grade I

## Phase 2 — Design: Identify Patterns, Drift, and Exceptions

After cataloging raw values, analyze them. See `references/common-pitfalls.md` for what to avoid.

### Step 1: Find Duplicates and Conflicts

Output a structured issues list:
1. **同值异名 (Same value, different names):** Multiple variable names resolving to the same value and same semantic role — candidates for merging
2. **同名异值 (Same name, different values):** Same variable name expressing different meanings across themes, scopes, or files — these MUST stay separate
3. **近似重复 (Near duplicates):** Values like 15px/16px/17px or similar grays — investigate whether the difference is intentional (font metrics, component sizing, responsive) or drift
4. **语义误绑 (Semantic misbinding):** Same current value but different semantic roles (e.g., `#FFFFFF` as both page background and inverse text) — these MUST become separate semantic tokens
5. **硬编码逃逸 (Hardcoded escapes):** Raw values used in components even though variables exist — flag for migration
6. **组件漂移 (Component drift):** Same component type with different sizing/colors/spacing across pages — identify the canonical version

### Step 2: Build Three-Layer Tokens

**Primitive tokens** — raw materials only:
```
color.blue.50  → #E8F3FF    color.blue.500  → #165DFF    color.blue.900  → #001B4D
color.gray.50  → #F7F8FA    color.gray.500  → #86909C    color.gray.900  → #1D2129
space.1  → 4px    space.2  → 8px    space.4  → 16px    space.6  → 24px
radius.sm → 2px  radius.md → 4px   radius.lg → 8px
font.size.sm → 12px   font.size.base → 14px   font.size.lg → 16px
```

**Semantic tokens** — design roles referencing primitives:
```
color.action.primary      → color.blue.500
color.action.primary.hover → color.blue.400
color.bg.page             → color.gray.50 (light) / color.gray.900 (dark)
color.bg.surface          → white (light) / color.gray.800 (dark)
color.text.primary        → color.gray.900 (light) / white (dark)
color.text.secondary      → color.gray.500
color.border.default      → color.gray.200
space.container.padding   → space.6
shadow.overlay            → {specific shadow}
```

Show theme mappings for light/dark if applicable. When the same primitive maps to different semantics in different themes, this is exactly why the three-layer system exists — document it explicitly.

**Component tokens** — only where necessary:
```
button.primary.bg.default  → color.action.primary
button.primary.bg.hover    → color.action.primary.hover
input.border.focus         → color.action.primary (with alpha)
dialog.shadow              → shadow.overlay
table.row.height.compact   → 36px
```

If a component token simply equals a semantic token (e.g., `card.bg → color.bg.surface`), do NOT create it — just document that cards use `color.bg.surface`.

### Step 3: Handle Exceptions

Some values are genuinely local and should NOT become tokens:
- One-off decorative gradients
- Chart/dataviz algorithm-generated colors
- Third-party component internal styles
- Experimental/A-B test variants

Document these in the output's Known Gaps / Exceptions section with justification.

## Phase 3 — Package: Generate the Output Style Skill

Generate the output style skill using the templates in `assets/style-skill-template/`.

### Output Skill Structure

```
brand-style-{name}/
├── SKILL.md                       # YAML frontmatter + three-layer overview + quick reference
├── references/
│   ├── colors.md                  # Primitive color scales + Semantic color roles + theme mappings
│   ├── typography.md              # Primitive font scale + Semantic text roles
│   ├── spacing.md                 # Primitive spacing/radius/shadow scales + Semantic layout tokens
│   ├── components.md              # Component tokens and patterns
│   └── known-gaps.md              # Unresolved discrepancies, exceptions, assumptions
```

### Output Format

See `references/output-format.md` for the detailed specification. Key requirements:

**SKILL.md:** Must include YAML frontmatter with structured token data. See the template.

**All reference files:** Every token table must include an **Evidence** column (D/M/I/A).

**known-gaps.md:** Required. Documents:
- Conflicts between documentation and source code (and which was chosen)
- Values that couldn't be confirmed
- Assumptions that need user review
- Genuine exceptions with justification

### Post-Generation Validation

After generating all files, run the validations in `references/validation-checklist.md`:

1. **Format:** YAML parses cleanly; all required frontmatter fields present
2. **References:** Every `{colors.xxx}` style reference resolves to a defined token
3. **Color validity:** All hex values are legitimate 3/6/8-digit hex
4. **Layer consistency:** Semantic tokens reference primitives (not copy values); component tokens reference semantics (not primitives directly)
5. **No cross-contamination:** No tokens, brand names, or rules from other design systems
6. **Section completeness:** All required sections present and in order

Report: file path, total lines, token counts per layer, grades distribution, validation results, and remaining Known Gaps.

## Phase 4 — Verify: Demo and Refine

After generating the skill, optionally validate it's actually usable:

1. **Generate a demo page** that exercises the tokens: background layers, text hierarchy, buttons (all variants), form elements, cards, navigation, and data display
2. **Check:** Does the demo look like the source? Are any values clearly wrong?
3. **Offer to refine:** "Would you like me to adjust any colors, fonts, or values?"

## Common Pitfalls to Avoid

These are the five most common extraction mistakes. See `references/common-pitfalls.md` for full details.

1. **Treating frequency as correctness.** A value appearing 50 times may just be copy-paste legacy. A value appearing once (e.g., brand title font) may be critical.
2. **Force-merging near-duplicates.** 15px/16px/17px differences may come from font metrics, component sizing, or responsive breakpoints. Investigate before averaging.
3. **Skipping browser rendering.** Source code values can be overridden by specificity, theme scopes, or runtime injection. Static analysis alone is incomplete.
4. **Renaming without aliasing.** Changing `#165DFF` to `color-blue-500` is just a rename. The real value is mapping it to semantic roles that survive theme changes.
5. **Mass-replacing the entire codebase.** Start with one representative page. Verify it handles all states and themes. Then expand.

## References

- `references/extraction-checklist.md` — Comprehensive token extraction checklist with evidence grading
- `references/output-format.md` — Detailed specification for output file format and three-layer structure
- `references/validation-checklist.md` — Post-generation validation steps and criteria
- `references/common-pitfalls.md` — The five most common extraction mistakes and how to avoid them
- `assets/style-skill-template/` — Template directory for generated style skills
