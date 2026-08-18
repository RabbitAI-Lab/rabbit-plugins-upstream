---
name: generate-html-ppt
description: When the user asks to create an HTML PPT, presentation slides, or a deck, or convert an existing PowerPoint (.pptx) file, use this skill to generate a modern, responsive HTML presentation based on design system specifications (design.md). This includes Chinese requests such as 做PPT、幻灯片、演示文稿、网页版PPT、PPT转换.
---

# HTML PPT Generation Skill

When the user requests an HTML presentation or PPT, follow these instructions to create it.

## Overview

Presentations are generated using a **Design System Specification (`design.md`)** architecture combined with **Progressive Disclosure**. Rather than relying on rigid, hardcoded HTML templates, visual styles are authored as comprehensive design recipes specifying fonts, color palettes, elevation shadows, typography scales, layout rules, and animation patterns.

### Core Principles
1. **Design System Specification (`design.md`) Architecture**: Access over 34+ distinct aesthetic design recipes (e.g., Beautiful Modern, Swiss International, Cyberpunk Dark, 8-Bit Orbit, Emerald Editorial, Neo Grid, Monochrome, Retro Zine) defined in `designs/bold-template-pack/` and `designs/STYLE_PRESETS.md`.
2. **Progressive Disclosure**: High token efficiency. First read `designs/bold-template-pack/selection-index.json` to match styles based on text metadata. Only after the style is chosen, read that specific template's single `design.md` file to construct the presentation.
3. **Fixed 16:9 Stage (NON-NEGOTIABLE)**: Every slide canvas is authored inside a 1920×1080 stage scaled uniformly to the viewport using JavaScript (`updateScale()`). Content never reflows per device.
4. **Seamless Viewport Rule (视口无缝融合规范)**: All presentations must use CSS variables (`--viewport-bg`) on `body` / `.deck-viewport` and dynamic JavaScript (`updateViewportBg()`) to synchronize the outer screen background with the active slide's background.
5. **Text-First Workflow**: Preserves the signature 3-stage user workflow: **Text-based requirement alignment ➔ Design-guided wireframing (灰度骨架确认) ➔ Guided batch content filling ➔ Verification**.

---

## Phase 0: Mode Detection

Determine what the user wants:
- **Mode A: New Presentation** — Create a presentation from scratch. Go to Phase 1.
- **Mode B: PPT Conversion** — Convert a PowerPoint (`.pptx`) file to HTML. Go to Phase 4.
- **Mode C: Cover Generation** — Generate multi-platform social media covers based on a PPT or article. Go to Phase 5.

Do not generate all slides in a single pass, and do not start building content before the wireframe is confirmed.

---

## Phase 1: Outline & Style Alignment (Text & Visual Preview Protocol)

1. **Requirements Alignment (7-Question Checklist)**
   Clarify requirements via text conversation:
   1. **Style Preference & First-Time Guidance (风格偏好与初用指南)** — Match against available design recipes (Default: Beautiful Modern. Alternatives: Swiss Minimalist, Cyberpunk Dark, 8-Bit Orbit, Emerald Editorial, etc.).
      *For first-time or undecided users*: Proactively offer to generate a quick **Visual Style Preview (风格视觉预览)** before building the full presentation to avoid wasting tokens if the aesthetic isn't right.
   2. **Audience & Scenario** — Pitch deck / Conference talk / Internal report / Teaching-Tutorial.
   3. **Presentation Length** — Short (5-10) / Medium (10-20) / Long (20+).
   4. **Raw Materials** — Documents, notes, topic outline.
   5. **Visual Assets** — Logos, screenshots, diagrams.
   6. **Theme & Density Mode**:
      - *Low density / Speaker-led*: Large headings, minimal text, generous negative space, 1-3 bullets max.
      - *High density / Reading-first*: Detailed grids, comparisons, tables, 4-8 bullets per slide.
   7. **Hard Constraints** — Specific brand colors, typography requirements, or deadline constraints.

2. **Brand Asset Protocol (品牌嗅探)**
   **CRITICAL RULE**: If the user provides a specific company or brand, extract core brand colors (HEX/RGB) and typography via search or local files, injecting them into the selected `design.md` CSS variables (e.g. `--brand-accent`).

3. **Style Matching & Visual Preview Protocol (风格匹配与视觉预览协议)**
   Read `designs/bold-template-pack/selection-index.json`. Recommend 2-3 candidate style options tailored to the topic mood and presentation scenario.
   **CRITICAL REQUIREMENT (主动提示视觉预览与低成本确认)**:
   - **Proactive Prompting (主动提示)**: The AI MUST explicitly ask the user whether they want to view a visual style preview first or proceed directly. Present two clear paths:
     - **Option A (Direct Proceed / 直接生成)**: Directly proceed with the top recommended style (e.g., Beautiful Modern or Cyberpunk Dark).
     - **Option B (Visual Preview / 视觉预览对比 - Recommended for first-time users)**: Rapidly generate a 1 to 3 slide visual style comparison card (`style-preview.html` or mockup images) rendered with actual topic content for visual confirmation before constructing the full presentation.
   - **How to execute Option B (1-3 Slide Visual Style Comparison)**:
     - *Method 1 (Multi-Slide / Candidate Card HTML Preview - Recommended)*: Generate a lightweight `style-preview.html` containing 1 to 3 candidate slide preview cards (e.g., Slide 1 Cover, Slide 2 Key Concepts/Timeline, Slide 3 Architecture/Data) rendered with their exact CSS variables, Google Fonts, color tokens, and layout cards. Allow the user to specify how many slide preview cards (1-3) they wish to view.
     - *Method 2 (Style Preview Images)*: Use `generate_image` tool to render 16:9 visual mockup images for candidate styles.
   - Confirm the user's selected style choice after previewing before proceeding to Phase 2.

4. **Draft Narrative Arc Outline**
   Draft a slide-by-slide outline using a classic Narrative Arc:
   - **Hook** (1 slide)
   - **Context** (1-2 slides)
   - **Core** (3-5 slides)
   - **Shift** (1 slide)
   - **Takeaway** (1-2 slides)

---

## Phase 1.5: Image Generation & Screenshot Beautification

Prepare visual assets before building wireframes:
- If screenshots are provided, consult `references/screenshot-framing.md`.
- If AI images or diagrams are needed, consult `references/image-prompts.md`.

---

## Phase 2: Design-System-Guided Wireframing (灰度骨架确认)

1. **Single-Point Reading of `design.md`**
   Read **ONLY** the single `design.md` specification corresponding to the selected style (e.g. `designs/bold-template-pack/templates/<slug>/design.md` or `designs/STYLE_PRESETS.md`). Extract:
   - Font family imports (Google Fonts / Fontshare)
   - Color tokens (`:root` CSS variables)
   - Typography scale & clamp values
   - Elevation shadows, borders, card styles
   - Animation classes & micro-interactions

2. **Build Stage Wireframe HTML File (骨架代码)**
   Generate the single-file HTML presentation structure:
   - Embed full contents of `designs/viewport-base.css` in the `<style>` block.
   - Include the extracted `design.md` CSS design system tokens and classes.
   - Set up the 1920×1080 `.deck-stage` canvas and scaling script (`updateScale()`, `updateViewportBg()`).
   - Create slide containers (`<div class="slide" id="s{N}">...</div>`).
   - Include slide titles, structural grid/card layout classes, and placeholder text/images.
   - **Apply Layout Density Strategy (防止中间尴尬中空与过度拉伸)**:
     - *space-between 滥用规避*: 严禁对内容高度较矮（<200px）的中间组件无脑使用 `.between` (`space-between`)，否则会导致元素被甩到最顶和最底，中间形成 200~400px 巨大尴尬空白。
     - *垂直集中分组 (Scheme 1 / center-group)*: 优先使用 `.slide-content.center-group` (`justify-content: center; gap: 40px;`) 或 `.slide-content` (`justify-content: flex-start; gap: 40px;`)，紧密分组标题、中间连通桥与卡片，四周留出自然呼吸 Margins。
     - *中间连通桥 (Middle Bridge Block)*: 
       - 封面/Hero Slide：在标题与底部 Stats 之间加入 `.hero-middle-bridge` 芯片标签行（如 `✦ Viewport 视口无缝同步` 等），消除中空断层。
       - 步骤/流程 Slide：三段式 Pipeline 卡片内务必填充充实的内容要点列表 (Bullet points)，充实卡片纵向高度。
   - **DO NOT fill detailed paragraphs yet.**

3. **Stop & Present Wireframe for Approval (骨架确认)**
   Show the wireframe HTML to the user and explain the layout structure. **STOP and wait for user approval** before proceeding to fill detailed content.

---

## Phase 2.5: Content Batch Filling

Once the wireframe is approved:
1. Batch-fill complete copy, data tables, code snippets, and visual assets into each slide structure.
2. Adhere to the selected density mode (Low density vs. High density).
3. Ensure no text or cards overflow their slide boundaries at 1920×1080 resolution.

---

## Phase 3: Verify and Open

1. **Verify Presentation Features**:
   - Fixed 16:9 stage scaling (`updateScale()` on window resize).
   - Seamless Viewport Background synchronization (`--viewport-bg`).
   - All `.anim` elements trigger entry animations correctly.
   - Zero text clipping, zero vertical scrolling inside slides, zero panel overlap.
2. **Open in Browser**:
   - Ensure the completed HTML file is opened in the browser for user review.

---

## Reference Documents & Supporting Assets

All relative paths from skill root:

- `designs/bold-template-pack/selection-index.json` — Compact metadata index of 34 bold design templates.
- `designs/bold-template-pack/templates/*/design.md` — Detailed Design System recipes (read only the selected one).
- `designs/viewport-base.css` — Mandatory 16:9 stage scaling and seamless viewport CSS base.
- `designs/STYLE_PRESETS.md` — Core safe preset recipes (Beautiful Modern, Swiss Style, Cyberpunk Dark).
- `designs/animation-patterns.md` — Animation and micro-interaction guide.
- `references/checklist.md` — Presentation quality checklist.
- `references/screenshot-framing.md` — Screenshot framing and mockup guide.
- `references/image-prompts.md` — Prompt generation guide for presentation visuals.
- `scripts/extract-pptx.py` — PowerPoint content extraction script.
