---
name: text-to-infographic
description: 将复杂信息压缩成适合嵌入飞书文档、表格或画板的一张 overview 图；输出结构化 infographic plan，并可生成 SVG / whiteboard / doc adapter 草稿。
version: 0.1.0
metadata: { "openclaw": { "os": ["darwin","linux"], "requires": { "bins": ["python3"] } } }
user-invocable: true
disable-model-invocation: false
---

# text-to-infographic v0.1.0

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
- `primary_target = whiteboard`
- `secondary_targets = ["svg", "doc"]`
- `doc_mode = companion-detail`

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

Rules:
- every block must have a stable `block_id`
- keep text short enough to scan quickly
- use `payload` for chart-family-specific details when needed
- express relationships explicitly with `relations`

### 3. Validate the plan

Use `scripts/validate_infographic_plan.py`.

Minimum checks:
- schema subset compliance
- unique `block_id`
- relation endpoints resolve to existing blocks
- sankey relations include `weight`
- text stays within reasonable density
- default layout and delivery mapping can be applied cleanly

### 4. Produce adapter drafts

Use `scripts/build_infographic_adapters.py`.

The adapter layer should emit at least:
- SVG draft structure
- whiteboard draft structure
- doc summary / outline

When the environment exposes tool-specific capabilities such as `lark-cli`, `@larksuite/whiteboard-cli`, SVG workflows, or Feishu doc APIs, use the validated plan as the source of truth and map it into those tools.

### 5. Deliver the artifact

Prefer a compact deliverable bundle:
- validated infographic plan JSON
- adapter drafts
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

### Sankey rule

When `chart_family = sankey`, every relation must include a numeric `weight`.

## Files in this package

- `schemas/infographic-plan.schema.json`
- `examples/*.json`
- `scripts/validate_infographic_plan.py`
- `scripts/build_infographic_adapters.py`

## Quick commands

Validate all examples:

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
```

Build adapter drafts for one example:

```bash
python3 scripts/build_infographic_adapters.py \
  examples/infographic-flywheel-demo.json \
  --pretty
```
