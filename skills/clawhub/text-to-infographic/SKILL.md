---
name: text-to-infographic
description: 将复杂信息压缩成一张可编辑 overview 图；对含证据 plan 自动在 HTML/PNG 中展示来源编号、指标基期、claim 绑定与注释，并输出可审计 evidence JSON；也支持 SVG / whiteboard / doc adapter 草稿。
version: 0.5.0
metadata: { "openclaw": { "os": ["darwin","linux"], "requires": { "bins": ["python3"] } } }
user-invocable: true
disable-model-invocation: false
---

# text-to-infographic v0.5.0

**v0.5.0：证据不再只藏在 plan。** 含证据的 plan 会自动把 evidence summary 渲染进 HTML（因此打印与 PNG 均可见），并在产物同目录写出 `<infographic_id>.evidence.json`；旧 plan 不新增 sidecar，HTML 保持原样。

## Purpose

Turn user-provided workflows, frameworks, analysis notes, plans, dashboards, or knowledge summaries into a **single-page infographic system** that is optimized for:
- information hierarchy
- correctness
- scanability
- editability
- cross-tool handoff

This skill is intended for overview visuals that will later be embedded into:
- Lark docs
- Lark sheets with inserted whiteboards
- whiteboard canvases
- SVG-based design workflows
- companion docs that hold the detailed explanation

## Best fit

Use this skill when the user wants to:
- explain a process, framework, or decision path in one page
- summarize a complex topic into an overview graphic
- diagnose a problem with cause/effect structure
- compare options or show relationships between entities
- present a roadmap or dashboard that must remain editable later
- prepare a visual artifact first, then let a document carry the details

Common chart families:
- flywheel
- fishbone
- value pyramid
- sankey-like flow
- roadmap
- SaaS dashboard
- process map
- comparison chart

## Not a fit

Do not use this skill when the task is mainly:
- multi-panel storytelling
- character-driven continuity
- joke timing or punchline rhythm
- comic payoff
- picture-book page sequencing

Those should remain in `text-to-comic`.

## Core priorities

Always optimize in this order:
1. information hierarchy
2. correctness
3. scanability
4. editability
5. aesthetics

Do not let decorative styling make the diagram harder to understand.

## Output contract

Represent the plan with `schemas/infographic-plan.schema.json`.

The plan should express:
- top-level message
- layout intent
- visual system intent
- content blocks
- relations between blocks
- delivery targets
- evidence sources, typed metrics, and explicit baselines
- claims bound to evidence and visual blocks
- story arc stages and evidence-aware annotations

Keep the plan **tool-agnostic**:
- do not store absolute x/y coordinates
- do not store whiteboard node IDs
- do not lock the plan to one rendering engine
- let downstream adapters compute actual placement

## Default chart mapping

Use these defaults unless the user clearly asks otherwise:

- `flywheel -> radial + polar + clockwise`
- `fishbone -> spine-branch + cartesian + left-to-right`
- `pyramid -> pyramid + cartesian + top-to-bottom`
- `roadmap -> timeline + cartesian + left-to-right`
- `dashboard -> dashboard + cartesian + left-to-right`

Default delivery mapping:
- `primary_target = html`
- `secondary_targets = ["svg", "doc"]`
- `doc_mode = companion-detail`

The default now renders a **self-contained HTML infographic** as the primary deliverable, because it is:
- zero-dependency and openable anywhere (browser, print-to-PDF, Feishu import)
- editable after the fact (plain HTML/CSS, no external design tool required)
- the fastest path from "validated plan" to "visible artifact"

## Positioning vs. poster-style infographic tools

There are one-click "article → poster" tools (and skill packages) that produce beautiful one-shot HTML posters. This skill deliberately does **not** compete on poster aesthetics. Its differentiators:

1. **Editable, structured plan first.** The plan is a first-class artifact (JSON schema + validation), not an intermediate nobody can touch. Users can fix a fact, change a block, or re-layout without regenerating from scratch.
2. **Information correctness over visual wow.** Text budgets, relation integrity, sankey weights, and "no fake precision" rules are enforced before rendering. A wrong number in a pretty poster is still wrong.
3. **Feishu / office-native embedding.** Self-contained HTML imports cleanly into Feishu docs and prints to PDF without toolchain dependencies.
4. **Companion document by design.** Detailed rationale lives in the companion doc; the infographic stays scannable. Poster tools usually lack this split.

Use this framing when users compare against poster-generators: we sell *correct, editable, embeddable overviews*, not decorations.

## Workflow

### 1. Analyze the request

Identify:
- the user’s main message
- the audience
- the chart family that best fits the structure
- whether the output is for explanation, summary, comparison, diagnosis, planning, persuasion, or dashboarding

If multiple chart families are plausible, present the best default and one backup option.

### 2. Build the infographic plan

Create:
- `message`
- `layout`
- `visual_system`
- `blocks`
- `relations`
- `delivery`
- optional `data_sources`, `metrics`, `claims`, `story_arc`, and `annotations` for evidence-first stories

Rules:
- every block must have a stable `block_id`
- keep text short enough to scan quickly
- use `payload` for chart-family-specific details when needed
- express relationships explicitly with `relations`
- give every source, metric, claim, story stage, and annotation a stable ID
- bind metrics to sources, claims to evidence and blocks, and comparative metrics to a distinct baseline period
- use annotations for caveats, methodology, definitions, and source notes instead of hiding them in decorative copy

### 3. Validate the plan

Use `scripts/validate_infographic_plan.py`.

Minimum checks:
- schema subset compliance
- unique `block_id`
- relation endpoints resolve to existing blocks
- sankey relations include `weight`
- text stays within reasonable density
- default layout and delivery mapping can be applied cleanly
- source IDs, metric IDs, claim IDs, story stages, annotation targets, and block bindings resolve
- metrics with deltas and comparison/trend claims declare a distinct baseline period

### 4. Render the HTML artifact (primary deliverable)

Use `scripts/render_infographic_html.py` to produce a **self-contained HTML infographic** from the validated plan. `--out` is an *output directory*; the file name is derived from the plan slug:

```bash
python3 scripts/render_infographic_html.py examples/infographic-flywheel-demo.json --out /tmp/render/
# -> /tmp/render/growth_flywheel_ai_workspace_demo.html
```

The renderer supports 6 layouts (radial, spine-branch, pyramid, timeline, dashboard, sankey), a visual system built from `palette` + `emphasis_style` CSS variables, and honors `delivery.primary_target = html` by default. For evidence-aware plans it also renders a print-visible evidence summary and writes `<infographic_id>.evidence.json` beside the HTML; PNG export captures the same summary and writes the same sidecar beside the image.

### Premium visual skin (optional)

A plan can optionally opt into one of two premium skins via
`visual_system.premium_style`:

- `data-journal` — paper-feel + serif big numbers + masthead double rule; best for dashboard / timeline / sankey.
- `night-ops` — deep-navy dark mode with auto-lightened brand colors; best for flywheel / pyramid / dashboard, especially for share images.

Skins are pure CSS layers (`:root` variable overrides + a few component rules);
plan content, layout, and `relations` are not touched, so editability and
information correctness are preserved. Plans without `premium_style` render
exactly as before.

Rules:
- never render an unvalidated plan; the renderer re-validates before emitting
- keep the HTML single-file and zero-dependency (inline CSS, no CDN links, no JS required)
- make it print-friendly and Feishu-import friendly (fixed-width layout, `lang="zh-CN"` when content is Chinese)

### 5. Export a PNG share image (optional, for social/blog embedding)

Use `scripts/render_infographic_png.py` to capture the rendered HTML as a PNG via headless Chrome (CDP). Zero Python dependencies; requires a system Chrome/Chromium (`CHROME_PATH` env var override available).

```bash
python3 scripts/render_infographic_png.py examples/infographic-flywheel-demo.json --out /tmp/png/
# -> /tmp/png/growth_flywheel_ai_workspace_demo.png  (2000 x 1247 @ 2x by default)
```

Tuning:
- `--width 1000` — CSS viewport width (default 1000)
- `--scale 2` — device pixel ratio / 2x crisp output (default 2). Use `--scale 1` for smaller files.

Use PNG when the destination is:
- 小红书 / 公众号 / Twitter / 博客头图（不需要 SVG 的可编辑性）
- 飞书文档中作为静态图插入
- 任何不能内嵌 HTML 的载体

The HTML remains the source of truth; PNG is a derived share image. The plan JSON can be re-rendered to either.

### 6. Produce adapter drafts (optional)

Use `scripts/build_infographic_adapters.py`.

The adapter layer can additionally emit:
- SVG draft structure
- whiteboard draft structure
- doc summary / outline

When the environment exposes tool-specific capabilities such as `lark-cli`, `@larksuite/whiteboard-cli`, SVG workflows, or Feishu doc APIs, use the validated plan as the source of truth and map it into those tools. Adapter drafts are secondary; the HTML artifact is the default visible output.

### 6. Deliver the artifact

Prefer a compact deliverable bundle:
- rendered self-contained HTML infographic (primary)
- `<infographic_id>.evidence.json` for evidence-aware plans only
- validated infographic plan JSON
- adapter drafts (optional)
- a short doc summary
- any user-facing notes about assumptions or omitted detail

## Hard constraints

### Readability over decoration

Prefer fewer blocks with stronger grouping over dense pages full of tiny nodes.

### Companion document strategy

The infographic should explain the whole picture quickly.
Detailed rationale, definitions, and edge cases should go into the companion doc.

### No fake precision

If exact numbers or structure are missing, keep the visual honest:
- label assumptions clearly
- avoid invented metrics
- avoid implying precise proportions without data

### Evidence-first data storytelling

When the plan makes factual, trend, or comparison claims:
- register provenance in `data_sources`; non-derived sources need `url` or `citation`
- store numeric observations in `metrics` and bind each metric to one or more source IDs
- include `baseline.value` and a distinct `baseline.period` whenever a metric has `delta` or supports a comparison/trend claim
- bind every claim to at least one metric or source and at least one visual block
- order claims with `story_arc.stages`; use `annotations` for methodology and caveats
- never put an unsupported number only in block copy; the evidence objects are the source of truth

The evidence fields remain optional, so legacy infographic plans stay valid and do not emit an evidence sidecar. Use them whenever the requested output is a data story or makes evidence-dependent claims.

### Sankey rule

When `chart_family = sankey`, every relation must include a numeric `weight`.

## Files in this package

- `schemas/infographic-plan.schema.json`
- `examples/*.json`
- `scripts/validate_infographic_plan.py`
- `scripts/render_infographic_html.py`
- `scripts/render_infographic_png.py`  *(requires system Chrome/Chromium)*
- `scripts/build_infographic_adapters.py`
- `scripts/test_evidence_rendering.py`

## Quick commands

Validate all examples:

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
python3 -m unittest scripts/test_evidence_rendering.py -v
```

Render a self-contained HTML infographic (primary output; `--out` is a directory):

```bash
python3 scripts/render_infographic_html.py \
  examples/infographic-flywheel-demo.json \
  --out /tmp/render/
```

Export a PNG share image (optional, requires Chrome/Chromium):

```bash
python3 scripts/render_infographic_png.py \
  examples/infographic-flywheel-demo.json \
  --out /tmp/png/
```

Build adapter drafts for one example (optional):

```bash
python3 scripts/build_infographic_adapters.py \
  examples/infographic-flywheel-demo.json \
  --pretty
```
