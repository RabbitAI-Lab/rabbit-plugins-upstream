---
name: academic-figures
version: 2.0.1
date: 2026-08-13
author: docsor1212
description: >
  Stop redoing figures. One command renders publication-ready charts: 14 chart
  types (bar, scatter, heatmap, forest, KM, ROC, violin, composite, flow...),
  7 curated themes incl. colorblind-safe Okabe-Ito/GLM, Nature/Lancet journal
  presets, and built-in PDF verification (text-overlap + minimum font-size
  gates) that catches rejection-worthy flaws before you export. 600dpi
  PNG/SVG/PDF/TIFF/EPS output, 100% local, data never leaves your machine.
  Triggers: make figure, generate chart, plot data, bar chart, scatter plot,
  heatmap, forest plot, Kaplan-Meier, ROC curve, survival curve, violin plot,
  composite figure, flow diagram, hatching, journal figure, publication figure,
  colorblind-safe palette, 600dpi export.
metadata:
  clawdbot:
    emoji: "📊"
    category: visualization
requires:
  python: ">=3.8"
  pip: ["matplotlib", "numpy", "pymupdf", "scipy"]
---

# Academic Figures — Publication-Quality Chart Generator

Generate figures from JSON/CSV data. Local execution, no data leaves the machine.

**One command, verified output:**
```bash
python3 scripts/gen_figure.py -t bar -d data.json -o fig.pdf --theme okabe-ito --verify
# exit 0 = rendered + no real text overlap; exit 2 = overlaps found (fix, don't ship)
```

## Quick Start

```bash
# 0️⃣ First run: one-command environment setup (deps/CJK font/font cache/self-check)
python3 scripts/setup_env.py

# 0️⃣ Quick tour: interactive demo (pick a chart type → renders with sample data)
python3 scripts/gen_figure.py --demo --cjk
# See all themes: python3 scripts/gen_figure.py --list-themes
# Limitations of a chart type: python3 scripts/gen_figure.py --explain bar

# Bar chart with default glm palette (muted, colorblind-safe)
python3 scripts/gen_figure.py -t bar -d data.json -o figure.png \
  --title "图2 主标题 / Subtitle" --ylabel "准确率 Accuracy (%)"

# GLM signature style: muted palette + black hatching (print-friendly, colorblind-safe)
python3 scripts/gen_figure.py -t bar -d data.json -o hatch.png --style glm-hatch \
  --show-values --title "ACR50 Response Rates"

# Forest plot for meta-analysis (PDF output)
python3 scripts/gen_figure.py -t forest -d forest.json -o forest.pdf --theme okabe-ito

# Heatmap with CJK support
python3 scripts/gen_figure.py -t heatmap -d data.json -o heatmap.png --cjk \
  --cmap RdBu_r --vmin -20 --vmax 45

# Scatter with trend line, Nature style
python3 scripts/gen_figure.py -t scatter -d data.csv -o scatter.png \
  --xlabel "Baseline (%" --ylabel "Gain (%)" --theme nature

# Kaplan-Meier survival curve with log-rank test
python3 scripts/gen_figure.py -t km -d survival.json -o km.png --theme okabe-ito \
  --title "图3 Kaplan-Meier生存曲线" --xlabel "时间 (月)" --ylabel "生存概率"

# ROC curve with AUC
python3 scripts/gen_figure.py -t roc -d roc.json -o roc.png --theme okabe-ito \
  --title "图4 ROC曲线" --xlabel "1 - 特异度" --ylabel "敏感度"

# Stacked bar chart (subgroup proportions)
python3 scripts/gen_figure.py -t stacked_bar -d subgroups.json -o stacked.png --theme okabe-ito \
  --title "图5 ANCA相关血管炎器官受累"

# Dual Y-axis chart (clinical score + lab marker)
python3 scripts/gen_figure.py -t dual_axis -d dual.json -o dual.png --theme okabe-ito \
  --title "图6 CRP与DAS28随治疗变化"

# TIFF output for Lancet submission (photo content → 300dpi)
python3 scripts/gen_figure.py -t bar -d data.json -o figure.tiff --dpi 300 --theme lancet

# Nature double-column submission: width 183mm, 7pt Helvetica, min text 5pt
python3 scripts/gen_figure.py -t bar -d data.json -o nat.pdf --journal nature --column double
python3 scripts/audit_pdf.py nat.pdf --min-size 5          # font-size gate (5pt for nature)

# Horizontal bar chart with ratio annotations + GLM palette (GLM-5.2 blog style)
python3 scripts/gen_figure.py -t hbar -d throughput.json -o perf.png --theme glm \
  --show-ratio --title "Throughput Improvement" --xlabel "Normalized Throughput"

# Bar chart with hatching patterns (print-friendly, colorblind-safe)
python3 scripts/gen_figure.py -t bar -d data.json -o hatch.png --theme okabe-ito \
  --hatch --show-values --title "ACR50 Response Rates"

# GLM-5.2 blog style: alternating yellow/blue bars with black hatching (single series)
python3 scripts/gen_figure.py -t bar -d data.json -o glm_alt.png --theme glm \
  --hatch --alternate --show-values --title "Publications by Type"

# Multi-panel composite (Panel A+B+C, journal figure layout)
python3 scripts/gen_figure.py -t composite -d composite.json -o figure4.png --theme okabe-ito

# Architecture/flow diagram (research design, CONSORT-style)
python3 scripts/gen_figure.py -t diagram -d flow.json -o flow.png --theme glm --width 12 --height 6

# Supplementary legend (journal format, "Figure 1 |" style), same data JSON
python3 scripts/gen_legend.py -d data.json -t "Response to treatment" -f 1 -o legend.txt
```

## Chart Types

| Type | Command | Key Features |
|------|---------|-------------|
| Bar | `-t bar` | Grouped bars, error bars, significance brackets, hatching, ratio annotations |
| Horizontal Bar | `-t hbar` | Horizontal bars, ratio annotations |
| Stacked Bar | `-t stacked_bar` | Subgroup proportions, percentage labels, total annotations |
| Heatmap | `-t heatmap` | Cell annotations, custom colormap, colorbar |
| Scatter | `-t scatter` | Trend line, r value, color grouping, mean points, point labels |
| Line | `-t line` | Multiple series, error bands, markers |
| Dual Y-Axis | `-t dual_axis` | Two Y-axes, solid+dashed lines, combined legend |
| Box | `-t box` | Box-and-whisker, jitter points |
| Forest | `-t forest` | CI whiskers, weight bubbles, overall diamond, I², events/total |
| Kaplan-Meier | `-t km` | Step function, censor marks, log-rank test, risk table, median survival |
| ROC | `-t roc` | AUC, 95% CI, optimal cutoff, multi-model comparison |
| Violin | `-t violin` | Density estimation, inner mean/median |
| **Composite** | `-t composite` | Multi-panel (A+B+C), any chart type per panel, journal figure layouts |
| **Diagram** | `-t diagram` | Architecture/flow blocks, arrows, groupings, annotations |

## Color Themes

**Default theme = `glm`** (muted elegant Morandi-style palette, colorblind-safe) — beautiful without being garish; single-series charts get a warm yellow accent so they never look monotonous.

| Theme | Description | Colorblind Safe |
|-------|-------------|----------------|
| `glm` ⭐default | Muted/elegant Morandi palette (steel blue/warm yellow/sage green/dusty purple/coral) — default, aesthetic + safe | ✅ Yes |
| `okabe-ito` | Nature Methods gold standard (Wong 2011) — vivid, journal submission first choice | ✅ Yes |
| `cool` | Elegant cool-toned palette (navy/ocean/teal/slate, hue 190-260°) | ✅ Yes |
| `classic` | Original matplotlib palette (pre-v2.0 default, kept for compatibility) | ❌ |
| `nature` | NPG Nature journal palette | ❌ |
| `lancet` | Lancet medical palette | ❌ |
| `conservative` | Professional muted palette | ❌ |

### Viewing & Choosing Themes (new in v2.0.1)

```bash
# See ALL themes with in-terminal color swatches
python3 scripts/gen_figure.py --list-themes

# Render a theme's swatch preview PNG (for docs/submission materials)
python3 scripts/gen_figure.py --theme-swatch glm -o swatch.png

# Convenient aliases (no need to memorize exact names):
#   okabe → okabe-ito   colorblind → okabe-ito   default/classic → glm
# Case-insensitive + prefix matching (--theme gla → glm)
```

> **⚠️ Recommendation**: For journal submissions use `--theme okabe-ito` (vivid, Nature/Science standard). Nature, Science, Cell, and most major journals now **require** colorblind-accessible figures. Red-green color schemes are a top rejection reason.
>
> **🎨 For everyday work**: the default `glm` is the best balance — muted, elegant, colorblind-safe, and distinctive. Avoid bright red/green/yellow schemes.

### Why Okabe-Ito?

The Okabe-Ito palette (`#E69F00, #56B4E9, #009E73, #F0E442, #0072B2, #D55E00, #CC79A7, #000000`) is the gold standard for colorblind-safe scientific visualization:
- Explicitly recommended by **Nature Methods** (Wong 2011, Nat Methods 8:441)
- Default in Wilke's "Fundamentals of Data Visualization"
- All 8 colors distinguishable under protanopia, deuteranopia, and tritanopia
- Visually vibrant — **no aesthetic compromise** vs. traditional palettes

## Journal Submission Presets (v2.0)

`--journal nature|lancet` + `--column single|double` applies the journal's exact
column-width figures, font size, font family and DPI automatically. Widths are from
official author guidelines:

| Journal | Column | Width | Font Size | Min Text | Family | DPI |
|---------|--------|-------|-----------|----------|--------|-----|
| `nature` | single | 89mm (3.50in) | 7pt | **5pt** | Helvetica | 600 |
| `nature` | double | 183mm (7.20in) | 7pt | **5pt** | Helvetica | 600 |
| `lancet` | single | 85mm (3.35in) | 8pt | **6pt** | Arial | 600 |
| `lancet` | double | 183mm (7.20in) | 8pt | **6pt** | Arial | 600 |

Height follows the theme's aspect ratio; any explicit `--width/--height` overrides.
A stderr hint reports the preset and the matching `audit_pdf.py --min-size` gate:

```bash
python3 scripts/gen_figure.py -t forest -d forest.json -o nat.pdf --journal nature --column double
# stderr: Journal preset: nature (double-column, width=7.20in, font=Helvetica 7pt, min text 5pt
#          — verify with audit_pdf.py --min-size 5)
python3 scripts/audit_pdf.py nat.pdf --min-size 5
# OK: no text below 5pt in nat.pdf
```

## Data Validation & Exit Codes (v2.0)

Every run passes through `validate_data(data, chart_type)` — structural validation
covering all 18 type/alias branches. Two severity levels:

| Level | stderr Prefix | Effect | Exit |
|-------|---------------|--------|------|
| **Fatal** | `ERROR:` | Data unusable (e.g. empty series, series length mismatch, missing required keys, ROC AUC outside [0,1]) | `1` (no output written) |
| **Warning** | `WARNING:` | Data accepted with caveats (e.g. missing recommended keys) | `0` |
| **Verify failure** | (from `--verify`) | PDF rendered but pixel-level text overlap detected | `2` |

Examples of fatal errors: bar with `series` of differing lengths; box/violin with
`labels` count ≠ number of groups (see Edge Cases); ROC with `curves[].auc` > 1.

## Verification & Quality Gates (v2.0)

Two mandatory gates for any deliverable figure, plus a third for supplementary
material:

### 1. `--verify` (in-line, on PDF output)

```bash
python3 scripts/gen_figure.py -t km -d survival.json -o km.pdf --theme okabe-ito --verify
# exit 2 + message if pixel-level text overlap found — fix the mechanism, don't special-case.
```

### 2. `audit_pdf.py` — font-size gate (journal minimum text size)

```bash
python3 scripts/audit_pdf.py figure.pdf --min-size 5 --fail-below
# --fail-below: non-zero exit if any text span is smaller than --min-size
# --max-reports N: cap offender listing (default 20)
```

### 3. `verify_overlap_pixel.py` — overlap verifier (run on every delivered PDF)

```bash
python3 scripts/verify_overlap_pixel.py output.pdf
# Output: "文本对=N 候选=M 真实重叠=K" — K MUST be 0.
# Exit signal: 真实重叠=0 = no real ink overlap.
```

**CRITICAL — do NOT trust PyMuPDF bbox overlap reports.** PyMuPDF span/char bboxes
use the font line-height model (Noto CJK 2.856em, DejaVu 1.695em), which
systematically OVERESTIMATES rotated text (at 45°, fs=9 reports 32.3pt vs 16.8pt
real ink) and stacked/rotated labels. Two bboxes intersecting does NOT mean real
overlap — in practice 100% of such reports on this generator's output are false
positives. The verifier resolves this with 3 stages:

1. Full-page render → connected components (large components = gridlines/vector art, filtered)
2. Component centroid assignment to char bboxes
3. For candidate pairs: 600dpi local re-render → min ink distance (separated if > 0.05pt)

**Overlap prevention is built into `gen_figure.py`** (auto 45° x-label rotation for
dense bars, hbar y-label shrink for >12 categories, `_ensure_ylabel_clear()` labelpad
auto-increase). If the verifier ever reports 真实重叠>0, the figure is genuinely broken
— fix the mechanism, do not special-case the figure.

### Quality gates are testable

The repo ships regression suites so gates can be re-verified after any change:

```bash
python3 tests/run_tests.py          # 50 unittest tests — all must pass
# evals/evals.json: 8 behavioral evals (exit codes, CJK auto-load, presets, legend audit…)
```

## Supplementary Legends (v2.0)

Journals that forbid in-figure legends (e.g. Nature) need a separate legend block.
`gen_legend.py` renders a journal-format legend ("Figure 1 | title…") from the SAME
data JSON used for the figure, so legend text always matches series/colors:

```bash
python3 scripts/gen_legend.py -d data.json -t "Response to treatment" -f 1 -o legend.txt
# -d/--data: same JSON as gen_figure.py   -t/--title: legend title
# -f/--figure: figure number (default 1)  --type: chart type (default bar)
# --error-type: error-bar description (default "s.e.m.")   -o: output (default stdout)
```

## CJK / Chinese Support

Pass `--cjk` to auto-detect and load system CJK fonts. Zero manual configuration needed.

```bash
python3 scripts/gen_figure.py -t bar -d data.json -o fig.png --cjk
```

Font detection priority: Noto Sans CJK → PingFang → Microsoft YaHei → WQY → AR PL → Droid.

For custom font: `--cjk-font /path/to/font.ttf`

**CJK auto-detection is recursive** (v1.6.2+): `_scan_cjk()` walks the entire data
dict — values **and keys** (v2.0), including nested composite panels and diagram
text — so a Chinese series name like `"对照组"` triggers font loading on its own.
CJK detection covers **supplementary planes** (Ext-B..F `U+20000–U+2EBEF`,
Ext-G `U+30000–U+3134F`) in addition to the basic BMP block (v2.0).

## Output Formats

| Format | Extension | DPI | Best For |
|--------|-----------|-----|----------|
| PNG | `.png` | 600 (default) | General use, presentations |
| SVG | `.svg` | Vector | Web, editable graphics |
| **PDF** | `.pdf` | Vector | **Journal submissions (preferred)** |
| TIFF | `.tiff` | 600 (override: `--dpi 300`) | Nature/Lancet photo requirements |
| EPS | `.eps` | Vector | Legacy journal requirements |

> **Tip**: Nature and Science prefer **PDF/EPS vector** for line art. Use `.pdf` or `.eps` extension.

### DPI Standards (2026)

| Content Type | Required DPI | How |
|-------------|-------------|-----|
| Line art (graphs, charts) | 600-1000+ | Default is 600; use `--dpi 1000` for strict journals |
| Photos / micrographs | 300-600 | Use `--dpi 300` |
| Mixed (graphs + photos) | 600 | Default |
| Vector (PDF/SVG/EPS) | N/A | Resolution-independent |

## Data Input

JSON (full features) or CSV (basic). See `references/data-formats.md` for complete schema per chart type.

**JSON bar chart example:**
```json
{
  "labels": ["Group A", "Group B"],
  "series": {"Treatment": [75, 82], "Control": [68, 70]},
  "errors": {"Treatment": [3, 2], "Control": [2, 1]},
  "significance": {"Treatment:0": "***", "Control:1": "NS"}
}
```

## Key Flags

| Flag | Description |
|------|-------------|
| `--title "text"` | Figure title. Supports `\n` for newline |
| `--xlabel`, `--ylabel` | Axis labels |
| `--width N`, `--height N` | Figure size in inches |
| `--format F` | Force output format: png, svg, pdf, tiff, eps |
| `--dpi N` | Override DPI for raster output |
| `--show-values` | Show numeric labels on bars |
| `--no-trend` | Hide trend line (scatter) |
| `--no-legend` | Hide legend |
| `--cmap NAME` | Colormap (heatmap; default is data-driven: all-positive → warm YlOrRd, has negatives → RdBu_r diverging; explicit value overrides) |
| `--vmin`, `--vmax` | Value range (heatmap) |
| `--horizontal` | Horizontal bar chart (alias: `-t hbar`) |
| `--hatch` | Add hatching patterns to bars (print-friendly, black lines, 10 patterns cycle) |
| `--alternate` | GLM-5.2 blog style: alternate first two theme colors per bar (single series) |
| `--show-ratio` | Show ratio annotations (e.g., "4.96x") on grouped bars |
| `--ratio-base N` | Base series index for ratio calculation (default: 0) |
| `--cjk` | Force-load CJK font (also auto-detected from data) |
| `--cjk-font PATH` | Custom CJK font file |
| `--journal nature\|lancet` | Apply journal presets (width/font/DPI, see above) |
| `--column single\|double` | Column layout for `--journal` (default: double) |
| `--verify` | Run pixel-level overlap verification on PDF output; exit 2 on overlaps |

## FAQ (v2.0.1)

1. **ModuleNotFoundError on first run?** Run `python3 scripts/setup_env.py` — installs deps (matplotlib/numpy/pymupdf/scipy), detects a CJK font, clears the font cache, and self-checks.
2. **Chinese renders as boxes/tofu?** Usually a font-cache issue: run `python3 scripts/setup_env.py` (auto-clears cache), or delete `~/.cache/matplotlib` manually and retry. A CJK font must be installed (Linux: `fonts-noto-cjk`; macOS/Windows ship with one).
3. **Does CSV support error bars?** No — CSV has only label + value columns. Error bars/significance need JSON `errors`/`significance` fields. The CLI error includes this hint automatically.
4. **How do I see all themes quickly?** `python3 scripts/gen_figure.py --list-themes` (in-terminal color swatches) or `--theme-swatch glm -o swatch.png` for a preview PNG.
5. **Can't remember theme names?** Aliases: `okabe`/`colorblind`→okabe-ito, `default`/`classic`→glm; case-insensitive with prefix matching (`--theme gla` → glm).
6. **How to get started fast?** `python3 scripts/gen_figure.py --demo --cjk` — interactive menu, renders with built-in data; `--explain <type>` shows that type's limitations and recommended usage.

## Edge Cases (v2.0, learned from regression tests)

1. **Box/Violin `labels` = group names.** `labels` is validated against the **number
   of series/groups**, not the number of values. `{"labels": ["A","B"], "series": [[..],[..]]}`
   is correct; a per-value label list will fail validation.
2. **ROC AUC bounds are checked per curve.** `curves[].auc` must be in [0,1]; the
   check covers each model curve, not only a top-level `auc`.
3. **Composite legends never double the period.** Legend text ends in exactly one `.`
   (the `_fmt_n` formatter already appends a period — no extra one added).
4. **CJK in dict keys.** A Chinese key in `series`/`groups` triggers CJK font loading
   via key scan; without it the series label renders as tofu boxes in the legend.
5. **CJK supplementary planes.** Rare CJK ideographs in Ext-B..G blocks (e.g. 㐀, 𠀀)
   are detected; verify glyph coverage with `detect_cjk_font.py` before publishing.

## Accessibility & Alt Text

When submitting to journals, provide **alt text** for each figure describing what the figure shows. Example:
> "Bar chart showing Treatment group (mean 75, SD 3) vs Control group (mean 68, SD 2). Error bars represent standard deviation. Asterisks indicate statistical significance (p < 0.001)."

Springer Nature, NSF, and most major publishers require alt text for accessibility compliance.

## When Agent Generates Figures (Not CLI)

If creating a figure via Python script rather than CLI:

1. Always call `detect_cjk_font()` first if any label may contain CJK
2. Use `fontproperties=font_prop` on all text-setting calls with CJK content
3. Set `plt.rcParams['axes.unicode_minus'] = False` (prevents minus sign boxes)
4. **Use Okabe-Ito colors** for any multi-category plot
5. Verify output: file size > 20KB for multi-label charts indicates font loaded
6. Preferred output: **PDF** for submissions, PNG at 600 DPI for previews
7. **Hatching preference**: User prefers hatched/striped bar patterns (`--hatch`) for
   print-friendliness and visual distinction between series. Hatch lines are
   **black** (`edgecolor='black'`). Do NOT manually override `edgecolor` when hatching
   is active — the `gen_bar` function handles it.
8. **White background mandatory**: This is a publication-quality figure generator for
   journal submissions. ALL output must use white background (`facecolor='white'`).
   Dark/black backgrounds are NEVER acceptable. Do not add dark themes or dark
   background options.
9. **Validation**: run `validate_data(data, chart_type)` and check for fatal messages
   before rendering (same gates as the CLI).
10. **Verify**: run `verify_overlap_pixel.py` on any PDF before delivery.

## Design Principles

1. **White background is non-negotiable.** This skill exists for journal submissions (Nature, Lancet, Science). `save_kwargs["facecolor"]` is hardcoded to `'white'`. Never add dark theme support.
2. **Hatching = black lines on colored fill.** When `--hatch` is active, hatch lines are black (`edgecolor='black'`), guaranteeing visibility on any fill color without dark backgrounds. Each series cycles a distinct pattern for black-and-white print.
3. **glm is the default; okabe-ito for submissions.** Default theme is `glm` (muted, colorblind-safe). Always recommend `--theme okabe-ito` for journal submission colorblind safety. `cool` is suitable for all-cool-toned content.

## CJK Pitfalls

1. **Unicode superscripts/subscripts may be missing from CJK fonts.** Characters like `⁹` (U+2079), `³` (U+00B3), `²` (U+00B2) often produce "Glyph X missing" warnings with Noto Sans CJK. Use plain-text alternatives: `10^9/L` instead of `×10⁹/L`. Check `detect_cjk_font.py` output for glyph coverage before publishing.
2. **Chinese lab report PDFs from hospital LIS systems produce non-standard text layouts.** `page.find_tables()` typically returns 0 tables. `page.get_text()` yields column-mixed text (header rows interleaved with data rows) rather than row-aligned output. A 6-line-per-item sequential parser will fail. The reliable approach is: extract full text blob → apply indicator-specific regex patterns (see `references/chinese-lab-report-extraction.md`).

## Diagram (Flow Chart) Pitfalls

1. **Never use `#FFFFFF` for block colors** — white blocks are invisible on the mandatory white background. Use the theme palette or any visible hex color.
2. **Don't place intermediate blocks between two connected blocks on the same axis** — the arrow routing algorithm picks the nearest edge based on center coordinates. A block wedged between two vertically-connected blocks will cause arrows to connect to the wrong block. Instead, merge side-info into the target block's `sublabel`.
3. **CONSORT-style exclusion boxes** should be horizontally offset (same Y, different X) from the main vertical flow, with a horizontal arrow connecting them.

## Negative Triggers (DO NOT trigger this skill for)

- SVG medical diagrams (→ medical-svg)
- Terminal/CLI charts (→ data-viz)
- Spectrogram/time-frequency (→ pywayne-plot)
- HTML slide presentations (→ html-presentation-restyler)
- Pure data analysis without visualization (→ data-analysis)

## File Structure

```
academic-figures/
├── SKILL.md                 ← English documentation (this file)
├── SKILL_ZH.md              ← Chinese documentation
├── scripts/
│   ├── gen_figure.py        ← Main generator (matplotlib+numpy)
│   ├── gen_legend.py        ← Supplementary legend generator (journal format, v2.0)
│   ├── audit_pdf.py         ← Font-size auditor (--min-size gate, v2.0)
│   ├── detect_cjk_font.py   ← CJK font auto-detector
│   ├── verify_overlap_pixel.py ← Pixel-level label overlap verifier (run on every PDF)
│   └── extract_lab_pdf.py   ← Chinese hospital lab report PDF → JSON extractor
├── tests/
│   └── run_tests.py         ← 50 unittest regression tests (v2.0)
├── evals/
│   └── evals.json           ← 8 behavioral evals (exit codes, CJK, presets, v2.0)
└── references/
    ├── data-formats.md      ← JSON/CSV schema per chart type
    ├── pitfalls.md          ← Common errors and white-bg rule
    ├── reverse-engineering-colors.md  ← Extract exact colors from reference images
    └── chinese-lab-report-extraction.md ← Technique: parsing non-standard LIS PDFs
```

## Version History

- **v2.0.1** (2026-08-13) — UX improvements (targeting SkillHub official review T5.0/R4.5/A4.4/C4.8/E4.6 gaps):
  - **Default theme changed to `glm`** (muted Morandi, colorblind-safe; old `default` renamed `classic`, kept for compatibility).
  - New: `--list-themes` (in-terminal color swatches), `--theme-swatch <theme> -o out.png`, `--style glm-hatch` (GLM signature style one-liner), `--demo` (interactive menu, 12 built-in sample datasets), `--explain <type>` (limitations/notes), theme aliases + case/prefix tolerance (`okabe`/`colorblind`/`glm-blog`/`default`→glm).
  - `--hatch` extended to stacked_bar and forest (overall diamond).
  - **Heatmap default colormap fix**: when `--cmap` is omitted the default is now RdBu_r (red-blue diverging) — previously the kwargs default silently fell through to matplotlib's viridis (yellow-green); explicit `--cmap` still overrides.
  - **Data-driven heatmap colormap (added)**: all-positive data now auto-switches to warm YlOrRd sequential (removes the "broken band" look from RdBu_r's white midpoint on low positive cells); diverging RdBu_r only for data with negatives; vmin/vmax follow data range. Regression tests ×2.
  - Error messages for known limits (e.g., CSV+error bars) now include HINT with the fix.
  - New `scripts/setup_env.py`: one-command env setup (deps/CJK font/font-cache cleanup/self-check).
  - New `examples/`: 5 sample data JSONs + 7 theme swatch previews + README.
  - Docs: new FAQ section (font cache/deps/CSV limits/theme cheatsheet).
- **v2.0.0** (2026-08-12) — Hardening release: data validation layer, journal presets, verification tooling, regression/evals suites.
  - `validate_data()`: structural validation across all 18 type/alias branches, called centrally from `main()`; fatal → `ERROR:` + exit 1 (no output), warning → `WARNING:` (accepted). Examples: empty series, length-mismatched series, box/violin labels ≠ group count, missing required keys, ROC `curves[].auc` outside [0,1].
  - `--journal nature|lancet` + `--column single|double`: official column widths (nature 89/183mm, lancet 85/183mm), font size (7/8pt), family (Helvetica/Arial), 600dpi.
  - `--verify`: in-line pixel-level overlap check on PDF output, exit 2 on real overlaps.
  - `scripts/audit_pdf.py`: font-size audit with `--min-size`/`--fail-below`/`--max-reports` — journal minimum text gate (nature 5pt, lancet 6pt).
  - `scripts/gen_legend.py`: journal-format supplementary legends from the same data JSON.
  - `legend_audit()`: empty-legend detection for Python-API misuse.
  - Bug fixes: box/violin `labels` validated as group names (series count, not value count); ROC AUC bounds checked per curve; `has_cjk()` extended to supplementary planes (Ext-B..F U+20000–U+2EBEF, Ext-G U+30000–U+3134F); composite legend double-period removed; `_scan_cjk()` now scans dict **keys** too (Chinese series names trigger font loading).
  - `tests/run_tests.py`: 50 unittest tests (14 chart-type CLI smoke tests + validate_data units + CSV edge cases + CJK + legend audit + PDF audit + legend gen).
  - `evals/evals.json`: 8 behavioral evals, each validated against real CLI behavior (exit codes, CJK auto-load, nature double=183mm, no-false-warning legend audit, CSV long-format, box group labels, KM legend formatting).
- **v1.6.6** (2026-08-12) — Scatter readability fixes: (1) `gen_scatter` now renders point labels from `data["labels"]` (one per x/y point, alternating above/below with growing offset so clustered points like years 1950/1953/1955 don't collide); (2) trend line now carries `label='Linear trend'` so the legend explains the dashed regression line instead of leaving it unlabeled. Rebuilt demo3 with full annotations (title, axis labels, point labels, legend) — verified 0 real overlaps.
- **v1.6.5** (2026-08-12) — Documentation: made overlap verification a mandatory step for PDF delivery. Added "Verification" section to SKILL.md/SKILL_ZH.md (3-stage pixel verifier usage + warning that PyMuPDF bbox intersections are line-height-model artifacts, 100% false positives on this generator's output), added `verify_overlap_pixel.py` to file-structure docs, and added `pymupdf`/`scipy` to the `requires` pip list (verifier dependencies). Demo figures regenerated with real KEGG pathway gene counts (demo2) and ChEMBL pchembl values (demo3) after the previous demo datasets were found to contain degenerate synthetic values (all-50 gene counts / all-4.0 max_phase) that compressed axes into misleading density.
- **v1.6.4** (2026-08-12) — Verifier fix: `confirm_min_dist` now uses unique assignment (a component whose centroid falls in both spans' candidate windows is assigned to the nearer origin) instead of shared assignment, eliminating false positives for rotated y-axis labels (e.g. scatter `(max phase)` label vs top tick `4.00` — claimed overlap was verifier cross-assignment, not real ink contact). Re-verified all 14 production figures + 4 demo figures: **0 real overlaps**. Added `_ensure_ylabel_clear()` safety net to `gen_figure.py` (auto-increases y-label labelpad when matplotlib's measured bbox actually collides with tick labels; inert when no conflict, as in all current figures).
- **v1.6.3** (2026-08-12) — Label overlap verification closed at pixel level. Root cause of all reported "overlaps": PyMuPDF span/char bboxes use the font line-height model (Noto CJK 2.856em, DejaVu 1.695em), which systematically overestimates rotated text (45°: 32.3pt claimed vs 16.8pt real ink for fs=9) and stacked labels (char row bbox spans full line height). Verified all 14 production figures with a 3-stage pixel verifier (connected components → component centroid ownership → min ink distance at 600dpi): **0 real ink overlaps**. matplotlib `get_window_extent` (20.9pt vs 16.8pt real) is slightly conservative, so the anti-overlap mechanism is correct as-is. Verifier at `scripts/verify_overlap_pixel.py`. Removed dead `math` import from `gen_figure.py`.
- **v1.6.2** (2026-08-11) — Fixed two quality issues found in production use. (1) CJK detection is now recursive: `_text_has_cjk()` scans the entire data dict including nested composite panels/diagram text, so Chinese titles inside composite panels correctly trigger Noto Sans CJK loading (previously they rendered as tofu boxes). (2) Automatic label anti-overlap: x-axis labels rotate 45° when >8 bars or >12-char labels (bar) / >10 points (line) / >6 columns or >14-char labels (heatmap); hbar y-labels shrink one point when >12 categories; composite panels pass `alternate` through to hbar subplots.
- **v1.6.1** (2026-08-07) — Brightened GLM theme yellow from `#D49356` to `#D79D55` (true mean pixel value of the GLM-5.2 blog chart, sampled from 143k yellow pixels; previous value was an unrepresentatively dark sample). All alternate-style bar charts now render with the brighter warm yellow.
- **v1.6.0** (2026-08-07) — Added `--alternate` flag: GLM-5.2 blog style blue/yellow alternating bars for single-series bar/hbar charts (`--theme glm --hatch --alternate` reproduces the blog's yellow+black-hatch look: `#D79D55` yellow / `#70A0D0` blue alternating per bar with black hatch lines). Colors come from the first two theme colors, so it also works with `cool`/`okabe-ito` themes.
- **v1.5.2** (2026-06-18) — Added `cool` theme: 8-color cool-toned palette (navy `#1B4965`, ocean `#2E6F9E`, sky `#4FA3C5`, dark teal `#3D8080`, medium teal `#62A0A8`, steel `#5B7BA0`, slate `#7B9AB5`, pale steel `#9DB5CC`), all hues in 190-260° range, colorblind-safe. Created in response to user rejecting warm/saturated palettes and requesting 素雅冷色调配色.
- **v1.5.1** (2026-06-18) — Bug fixes: `gen_km()` crashes when `median_survival` value is `null` (median not reached); `gen_scatter()` crashes when `groups` array length exceeds `x`/`y` length (composite panels). Both fixed with null/length guards. Added `cool` theme (navy/ocean/teal/slate cool-toned palette, colorblind-safe). See `references/pitfalls.md`.
- **v1.5.0** (2026-06-17) — Added 3 new chart types: horizontal bar charts (hbar, with ratio annotations like "4.96x"), multi-panel composite figures (Panel A+B+C with GridSpec, any chart type per panel), architecture/flow diagrams (colored blocks, arrows, groupings, annotations); added GLM theme (muted/dusty palette pixel-extracted from GLM-5.2 blog: `#70A0D0` blue + `#D79D55` yellow, mean pixel values); added bar hatching with BLACK lines on ALL bars (print-friendly, 9 patterns: `//`, `\\`, `||`, `--`, `++`, `xx`, etc.); added `--hatch`, `--show-ratio`, `--ratio-base`, `--horizontal` CLI flags; **white background mandatory** for all themes (publication standard); see `references/reverse-engineering-colors.md` for pixel extraction technique
- **v1.4.0** (2026-05-17) — Added 4 new chart types: Kaplan-Meier survival curves (log-rank test, risk tables, median survival, censor marks), ROC curves (AUC, 95% CI, optimal cutoff, multi-model comparison), stacked bar charts (compositional data, percentage labels), dual Y-axis line charts (clinical score + lab marker); expanded data validation for new types
- **v1.3.0** (2026-05-17) — Added Okabe-Ito colorblind-safe theme (Nature Methods standard); DPI upgraded 300→600 for line art; added PDF/TIFF/EPS output; enhanced forest plot (weight bubbles, I² heterogeneity, events/total, separator line); accessibility alt-text guidance; smart DPI by content type
- **v1.2.0** (2026-05-16) — Added version metadata, requires declaration, negative triggers, file structure docs
- **v1.1.0** — Added auto CJK detection, CSV long-format auto-conversion, empty data validation
- **v1.0.0** — Initial release: 7 chart types, 4 themes, CJK support, statistical annotations
