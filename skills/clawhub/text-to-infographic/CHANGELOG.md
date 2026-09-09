# Changelog

## 0.3.0 (2026-09-02)

Premium visual skin layer: 2 new visual styles (`premium_style` in `visual_system`)
that ride on top of the existing 5 emphasis styles. The skin is **CSS variables
only** — content text, layout, relations, and sankey weights are not touched, so
the "correct, editable, embeddable" narrative is preserved.

- `data-journal` — paper-feel background with subtle grid, serif headline + tabular
  numerals for big metrics, masthead-style double border under the title.
  Best fit: `dashboard` / `timeline` / `sankey`; reinforces "information correct".
- `night-ops` — deep navy background with auto-lightened brand colors so that
  brand hues stay readable on dark surfaces. Includes a print-media override
  that resets variables to light values for paper output. Best fit: `flywheel` /
  `pyramid` / `dashboard`; works especially well as a small-red-book / WeChat
  share image.

Schema / renderer:
- `schemas/infographic-plan.schema.json` adds an optional `premium_style` enum
  (`data-journal` | `night-ops`) under `visual_system`. Backward compatible —
  plans without the field render exactly as before.
- `scripts/render_infographic_html.py`:
  - Variables `var(--panel)` / `var(--text)` / `var(--on-primary)` replace the
    last few hard-coded `#FFFFFF` / `#0F172A` references inside SVG node
    rects/text and the `.ig-tl-badge` / `.ig-note-card` rules, so the dark skin
    is just a `:root` override away. All default values match the previous
    literals, so unstyled plans render pixel-equivalent.
  - `color-mix(... white)` calls now blend with `var(--panel)` so the tint
    naturally follows the active skin.
  - `build_premium_css(premium_style, palette)` appends a CSS block for the
    requested skin; `lighten_hex` / `readable_on` helpers brighten brand colors
    and pick a contrast-safe on-primary text color for `night-ops`.
- `examples/infographic-dashboard-datajournal-demo.json`,
  `examples/infographic-flywheel-nightops-demo.json` — new premium demos.
  `validate_infographic_plan.py` passes 9/9.

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
