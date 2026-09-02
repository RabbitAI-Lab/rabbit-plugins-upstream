# Changelog

## 0.2.1

Added PNG export for share/social/blog embedding (小红书 / 公众号 / Twitter / blog hero images).

Added:
- `scripts/render_infographic_png.py`: plan JSON → self-contained HTML → PNG via headless Chrome (CDP). Zero Python dependencies; requires a system Chrome/Chromium (`CHROME_PATH` env var override). Default 2x device pixel ratio for crisp output (e.g. 2000px wide for a 1000-CSS-px plan).
- Minimal stdlib WebSocket client (RFC 6455) inside the script for CDP communication — no extra Python packages needed.

Tuning:
- `--width 1000` (CSS viewport width)
- `--scale 2` (device pixel ratio, 1/2/3)

Roadmap (planned for 0.3.0+):
- visual style upgrades (premium emphasis variants) while keeping information correctness as the priority
- `text → plan` auto-construction from articles / notes (closes the input side of the loop)

## 0.2.0

Closed the loop from "validated plan" to "visible artifact": the skill now renders a **self-contained HTML infographic** as the default primary deliverable.

Added:
- `scripts/render_infographic_html.py`: plan JSON → single-file, zero-dependency HTML (inline CSS, no CDN, no JS required; print-friendly; Feishu/Lark import friendly; `lang` set per content)
- 6 layouts: `radial` (SVG ring + clockwise arrows + center takeaway), `spine-branch` (SVG fishbone), `pyramid` (CSS tiers), `timeline` (CSS axis), `dashboard` (CSS grid metric cards), `sankey` (inline SVG flows sized by `weight`)
- visual system mapping: `palette` (brand/mono/duo/triad/custom) and `emphasis_style` (clean/editorial/playful/technical/luxury) → CSS variables
- renderer CLI: `--out`, `--stdout`, `--schema`; renderer re-validates the plan before emitting

Changed:
- default delivery: `primary_target` `whiteboard` → `html` (`secondary_targets=["svg","doc"]`, `doc_mode="companion-detail"` unchanged)
- `schemas/infographic-plan.schema.json`: `delivery.primary_target` and `secondary_targets.items` now accept `"html"`
- SKILL.md workflow: Render HTML artifact is step 4 (primary), adapter drafts demoted to optional step 5
- README / skill-card updated: positioning section explains differentiation vs. one-shot poster-style infographic tools (editable plan + information correctness + Feishu embed + companion doc)

Why:
- v0.1.0 produced only intermediate plan + adapter drafts — no finished graphic, which is the root cause of 0 installs
- HTML is the fastest default path: open anywhere, print to PDF, import into Feishu docs

## 0.1.0

Initial standalone release of `text-to-infographic`.

Included:
- independent `SKILL.md` with infographic-first positioning
- `schemas/infographic-plan.schema.json`
- seven example infographic plans
- `scripts/validate_infographic_plan.py`
- `scripts/build_infographic_adapters.py`
- package-level README, skill card, and MIT-0 license

Design choices:
- one schema first, not multiple execution schemas
- no absolute coordinates in the plan layer
- adapter drafts for SVG / whiteboard / doc workflows
- strong separation from `text-to-comic`
