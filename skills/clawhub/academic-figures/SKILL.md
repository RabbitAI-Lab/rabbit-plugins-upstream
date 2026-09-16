---
name: academic-figures
description: >-
  Publication-ready scientific figures from one command: 22 chart types (bar,
  grouped bar, scatter, heatmap, forest plot, Kaplan-Meier survival, ROC,
  violin, box, composite panels, PRISMA 2020 flow, funnel, Bland-Altman, PCA,
  venn, clustered heatmap, dual-axis), 9 themes incl. colorblind-safe
  Okabe-Ito and NEJM/Lancet/Science journal palettes, 9 journal submission
  presets, YAML figure pipeline (a whole paper in one command), multi-format
  export (TIFF/PNG/PDF in one run), Python API, reviewer-style --annotate
  arrows, PDF text-overlap + font-size gates, 600dpi output. 100% local —
  data never leaves your machine.
when_to_use: >-
  Use when making or generating any figure or chart from data: bar chart,
  scatter plot, heatmap, forest plot, Kaplan-Meier / survival curve, ROC curve,
  violin / box plot, composite multi-panel figure, flow diagram, PRISMA /
  systematic review flow, meta-analysis funnel, venn / Euler diagram, PCA,
  Bland-Altman; when exporting publication- or journal-ready figures (600dpi,
  colorblind-safe); or when turning a JSON/CSV/Excel data file into an
  academic figure.
---

<!--
═══════════ 元数据归档（2026-09-13 frontmatter 规范化）═══════════
ZCode 技能自动发现只识别 frontmatter 白名单键：
  name / description / when_to_use / license / metadata
且 description 超过 1024 字符会被静默丢弃（v2.x 自动发现失效根因：
v2.4 描述 1035 字符、v2.5 初版 1253 字符，均超限）。以下键自
frontmatter 移出归档，信息不丢失：
  version: 2.6.0
  date: 2026-09-15
  author: docsor1212
  metadata: {clawdbot: {emoji: "📊", category: visualization}}
  requires: {python: ">=3.8", pip: [matplotlib, numpy, pymupdf, scipy, openpyxl]}
运行依赖见 requirements.txt 与 scripts/setup_env.py；版本史见文末 Version History。
═════════════════════════════════════════════════════════════════
-->

# Academic Figures — Publication-Quality Chart Generator

Generate figures from JSON/CSV data. Local execution, no data leaves the machine.

**One command, verified output:**
```bash
python3 scripts/gen_figure.py -t bar -d data.json -o fig.pdf --theme okabe-ito --verify
# exit 0 = rendered + no real text overlap; exit 2 = overlaps found (fix, don't ship)
```

## Quick Start

```bash
# v2.7: raw per-subject survival data -> automatic multi-variable Cox -> HR forest (with PH test)
python3 scripts/gen_figure.py -t forest --data patient.csv --stats cox \
  --cox-time time --cox-event event --cox-cols "age,sex,treat"

# v2.7: aspect-ratio presets (16:9 slides / 9:16 mobile / 1:1 square; width still from journal preset)
python3 scripts/gen_figure.py -t bar --data d.json --size 16:9
```
```bash
# 0️⃣ First run: one-command environment setup (deps/CJK font/font cache/self-check)
python3 scripts/setup_env.py

# 0️⃣ Quick tour: interactive demo (pick a chart type → renders with sample data)
python3 scripts/gen_figure.py --demo --cjk
# See all themes: python3 scripts/gen_figure.py --list-themes
# Limitations of a chart type: python3 scripts/gen_figure.py --explain bar

# Not sure which chart type fits your data? Let the analyzer recommend one
python3 scripts/gen_figure.py --suggest -d data.json

# PRISMA 2020 systematic-review flow diagram (arithmetic auto-validated)
python3 scripts/gen_figure.py -t prisma -d prisma.json -o flow.pdf --theme okabe-ito

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

# Journal presets — 9 journals incl. Chinese CMA / CN-core (CJK font auto-on)
python3 scripts/gen_figure.py -t hbar -d data.json -o fig.pdf --journal cn-core --cjk

# Excel input (--sheet selects the sheet; requires openpyxl)
python3 scripts/gen_figure.py -t bar -d data.xlsx -o fig.png --verify

# Auto significance brackets (box/violin) + accessibility alt text sidecar
python3 scripts/gen_figure.py -t violin -d groups.json -o viol.pdf --stats auto --alt

# Scenario templates: copy one, swap in your real numbers
ls templates/
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
| **PRISMA Flow** | `-t prisma` | PRISMA 2020 review flow; counts auto-validated (must add up), EN/ZH wording via `lang` |

## Limits & Compatibility (read before first run)

**Data volume**: cluster_heatmap <=3000 rows; pca <=200 feature columns; venn 2-3 sets;
paired/bland_altman require equal-length pairs; km has no hard cap (50k rows render in ~3s).
**Flag compatibility**: `--stats` box/violin only; `--compare` roc only (needs labels+scores);
`--egger` funnel only; `--hatch` bar family only; `--sheet` xlsx only; `--journal` locks width
(`--width` is overridden, `--height` still applies).
**Output**: prefer PDF/EPS for submission vector figures; raster defaults 600dpi (line art) / 300 (photos).

Full matrix: `references/limits.md`. FAQ: `references/faq.md`. Over-limit inputs are rejected with a Chinese error message
plus a fix suggestion — no half-finished figures are ever written.

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
| `nejm` 🆕v2.5 | NEJM journal palette (brick red/steel blue/orange/green, 8 colors) | ❌ |
| `science` 🆕v2.5 | Science (AAAS) journal palette (navy/red/green/purple, 10 colors) | ❌ |
| `conservative` | Professional muted palette | ❌ |

**Journal linkage (v2.5)**: `--journal nejm|lancet|science|nature` auto-applies the matching color theme when no explicit `--theme` is given (layout presets unchanged; explicit `--theme` always wins).

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

`--journal <name>` + `--column single|double` applies the journal's exact
column-width figures, font size, font family and DPI automatically. Widths are from
official author guidelines (re-check the latest guide before submission).

**9 presets (v2.2)**: `nature`, `lancet`, `science`, `cell`, `nejm`, `jama`,
`ieee` + Chinese journals **`cma`** (中华医学会系列) and **`cn-core`** (中文核心
学报通用) — the two Chinese presets auto-enable the CJK font.

| Journal | Single | Double | Font | Min Text | Family | DPI |
|---------|--------|--------|------|----------|--------|-----|
| `nature` | 89mm | 183mm | 7pt | **5pt** | Helvetica | 600 |
| `lancet` | 85mm | 183mm | 8pt | **6pt** | Arial | 600 |
| `science` | 55mm | 120mm | 7pt | 5pt | Helvetica | 600 |
| `cell` | 85mm | 176mm | 8pt | 6pt | Arial | 300 |
| `nejm` | 89mm | 190mm | 8pt | 6pt | Helvetica | 300 |
| `jama` | 89mm | 183mm | 8pt | 6pt | Arial | 600 |
| `ieee` | 89mm | 181mm | 8pt | 6pt | Times New Roman | 600 |
| `cma` | 80mm | 170mm | 8pt | 6pt | Arial (+CJK) | 600 |
| `cn-core` | 80mm | 170mm | 9pt | 6pt | Arial (+CJK) | 300 |

Height follows the theme's aspect ratio; any explicit `--width/--height` overrides.
A stderr hint reports the preset and the matching `audit_pdf.py --min-size` gate:

```bash
python3 scripts/gen_figure.py -t forest -d forest.json -o nat.pdf --journal nature --column double
# stderr: Journal preset: nature (double-column, width=7.20in, font=Helvetica 7pt, min text 5pt
#          — verify with audit_pdf.py --min-size 5)
python3 scripts/audit_pdf.py nat.pdf --min-size 5
# OK: no text below 5pt in nat.pdf
# Chinese journal: CJK font auto-on, Chinese titles/labels render correctly
python3 scripts/gen_figure.py -t hbar -d cn.json -o cn.pdf --journal cn-core --cjk
```

## Auto Significance (--stats auto, v2.2)

For `box` / `violin` (raw-data charts): `--stats auto` compares every series
against the first — Shapiro normality test decides Welch t-test vs
Mann-Whitney U — and draws comparison brackets with `*`/`**`/`***`/n.s. above.
A per-comparison report (method, p, stars) prints to stderr.

```bash
python3 scripts/gen_figure.py -t violin -d groups.json -o viol.pdf --stats auto --verify
# stderr: stats (violin): Control vs Treatment: Welch t, p=0.0031 -> **
```

## Meta Analysis Workstation (v2.4)

- **KM auto median survival**: per-group median survival time with 95% CI
  (Greenwood log-log; verified identical to lifelines on 20 randomized datasets),
  annotated in-plot alongside the log-rank box. `--no-median` opts out; curves
  that never reach 50% are honestly labeled "未到达" (not reached).
- **forest --sensitivity**: leave-one-out sensitivity analysis — omits each study
  in turn, re-pools with DerSimonian-Laird, and renders N extra rows below the
  main plot. Needs `se_list` or symmetric CIs.
- Library exceptions now carry Chinese explanations (e.g. KeyError → "缺少必需字段").

## Submission Polish (v2.5)

Full polish kit (--annotate/--legend-loc/--legend-outside/NEJM·Science theme pairing) moved to `references/advanced.md`.
## Statistics Deep-Dive (v2.3)

Full deep-dive usage (Tukey/Dunn details, leave-one-out sensitivity, paired DeLong) moved to `references/advanced.md`.
## Alt Text (--alt, v2.2)

`--alt` writes an accessibility description file `<output>.alt.txt` next to the
figure — derived from the data itself (chart type, groups, medians/AUC/overall
effect, PRISMA counts, panel titles). Springer Nature, NSF and most major
publishers require alt text for accessibility compliance.

```bash
python3 scripts/gen_figure.py -t km -d km.json -o km.png --alt
# stderr: Alt text: km.alt.txt
```

## Scenario Templates (v2.6: all 22 chart types)

`templates/` ships 22 end-to-end templates (data JSON + ready-to-run command +
caption template), one per chart type: 16 clinical-scenario templates (01–16:
meta-analysis forest, RCT bar, KM survival, diagnostic ROC, correlation
heatmap, PRISMA review, dose-response line, panel composite, survey stacked
bar, Chinese-journal hbar, grouped bar, grouped scatter, box, violin,
dual-axis, study-design diagram) plus 6 chart-type quick templates
(bland_altman, cluster_heatmap, funnel, paired, pca, venn). Full index:
`templates/README.md`.

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
python3 tests/run_tests.py          # 96 unittest tests — all must pass
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

JSON (full features) or CSV/TSV (basic) or **Excel .xlsx/.xls (v2.2** — first
row is the header; `--sheet <name>` selects a sheet; requires `openpyxl`**)**.
See `references/data-formats.md` for complete schema per chart type.
Calling from Python (subprocess or import): see `references/python-api.md` (v2.6).

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
| `--multi-format F1,F2` | One run, many formats (v2.6): `-o fig1 --multi-format tiff,png,pdf` → fig1.tiff/fig1.png/fig1.pdf |
| `--pipeline analysis.yaml` | Whole-paper batch (v2.6): YAML/JSON with `defaults` + `figures` list; one command renders all, writes .batch-report.json |
| `--dpi N` | Override DPI for raster output |
| `--show-values` | Show numeric labels on bars |
| `--no-trend` | Hide trend line (scatter) |
| `--no-legend` | Hide legend |
| `--cmap NAME` | Colormap (heatmap; default is data-driven: all-positive → warm YlOrRd, has negatives → RdBu_r diverging; explicit value overrides) |
| `--vmin`, `--vmax` | Value range (heatmap) |
| `--sheet NAME` | Excel sheet name for .xlsx data (v2.2) |
| `--stats auto` | Box/violin significance brackets: each series vs first, auto test selection (v2.2) |
| `--alt` | Write `<output>.alt.txt` accessibility description (v2.2) |
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
| `--suggest` | Analyze the data file and print ranked chart-type recommendations + a ready-to-run command |
| `--annotate "x,y:text"` | Arrow annotation at data coords, repeatable; category axes accept tick labels (v2.5) |
| `--legend-loc LOC` | Explicit legend position (nine-scheme, e.g. `lower right`) (v2.5) |
| `--legend-outside` | Legend outside the plot; composite figures get one shared legend (v2.5) |
| `--area` | venn only: area-proportional Euler mode (v2.5) |

## FAQ (v2.0.1)

**Q: How stable is rendering? Will large data crash it?**
Since v2.7: pre-render memory guard (warns above ~1M data points with slimming advice); deterministic
output (same input -> byte-identical file, locked by regression test); 200-chart stress soak and
low-memory simulation pass. Even on failure you get a Chinese diagnosis + original error + targeted
tips; set `AF_DEBUG=1` for the full technical traceback.

**Q: Preprocessing columns like -log10(FDR)?**
-log10(0) = inf — clip first (e.g. `min(fdr, 1e-300)`) or color scales will explode.

**Q: --xlabel/--ylabel text with spaces or a leading dash fails?**
The shell splits after spaces — use the equals form: `--xlabel="Improvement (%)"`;
text starting with `-` MUST use the equals form (e.g. `--ylabel="-log10(P)"`).
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

> v2.7: `scripts/journal/*.json` = single source for journal presets; `references/changelog.md` = full history; `references/advanced.md` = deep-dive & polish kit.

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
│   └── setup_env.py         ← One-command env setup (deps/CJK font/cache/self-check, v2.0.1)
├── tests/
│   └── run_tests.py         ← 180 unittest regression tests (v2.6.0)
├── evals/
│   └── evals.json           ← 8 behavioral evals (exit codes, CJK, presets, v2.0)
├── examples/
│   └── example_*.json       ← Run-ready sample datasets for all 22 chart types
└── references/
    ├── data-formats.md      ← JSON/CSV schema per chart type
    ├── python-api.md        ← Call from Python: subprocess / import (v2.6)
    ├── faq.md               ← High-frequency Q&A + error-message lookup
    ├── pitfalls.md          ← Common errors and white-bg rule
    └── reverse-engineering-colors.md  ← Extract exact colors from reference images
```

## Version History

Full changelog: see `references/changelog.md` (bilingual).

- **v2.7.0** (2026-09-16) — Stability + Cox workstation: --stats cox fits multi-variable Cox from raw per-subject data (with PH test); --size aspect presets; exception handler v3 (Chinese diagnosis + tips + AF_DEBUG); deterministic output; package hygiene (zero duplicate files, journal/*.json single source); five field-report fixes.
- **v2.6.0** (2026-09-15) — Pipeline release: --multi-format, --pipeline, python-api.md, km CSV interception, Chinese validation messages, 22-type templates, forest ref_line auto by measure.
- **v2.5.0** (2026-09-14) — Submission polish: --annotate, NEJM/Science themes, venn Euler approximation, --legend-loc/outside, expanded exception mapping.
