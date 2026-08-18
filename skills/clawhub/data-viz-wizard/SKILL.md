---
name: data-viz-wizard
version: 1.0.0
author: Denis Voronin
license: MIT
description: Transform CSV data into stunning interactive chart visualizations with Chart.js
category: data-science
tags:
  - csv
  - charts
  - visualization
  - chartjs
  - dashboard
  - data-viz
---

# Data Viz Wizard

Transform any CSV file into stunning, interactive HTML chart visualizations powered by Chart.js.

## Quick Start

```bash
# Auto-detect best chart type
python scripts/viz_wizard.py chart sales.csv --type auto --output chart.html

# Generate a full dashboard with multiple charts
python scripts/viz_wizard.py dashboard data.csv --output dashboard.html

# Specify exact chart type and axes
python scripts/viz_wizard.py csv metrics.csv --type line --x date --y revenue --title 'Revenue Trend'

# Pipe data via stdin
cat data.csv | python scripts/viz_wizard.py --auto --output viz.html
```

## Commands

| Command | Description |
|---------|-------------|
| `chart <file>` | Generate a single chart (best auto-detected type) |
| `dashboard <file>` | Generate multi-chart dashboard from same dataset |
| `csv <file>` | Explicit chart with specified type and columns |
| _(stdin pipe)_ | `--auto` mode reads CSV from stdin |

## Flags

| Flag | Description |
|------|-------------|
| `--type` | Chart type: `auto`, `line`, `bar`, `stacked`, `area`, `scatter`, `pie`, `donut`, `radar`, `heatmap-grid` |
| `--x` | Column name for X-axis |
| `--y` | Column name(s) for Y-axis (comma-separated) |
| `--output` / `-o` | Output HTML file path |
| `--title` | Chart title |
| `--palette` | Color palette: `viridis`, `sunset`, `ocean`, `monochrome`, `neon` |
| `--trend` | Add trend line |
| `--moving-average` / `-ma` | Window size for moving average |
| `--theme` | `dark`, `light`, or `auto` (toggleable) |
| `--auto` | Full auto-mode (stdin) |

## Column Auto-Detection

The wizard auto-detects column types:
- **Date**: ISO dates, `YYYY-MM-DD`, `MM/DD/YYYY`, etc.
- **Numeric**: integers, floats, currency
- **Percentage**: values with `%` suffix
- **Categorical**: strings, low-cardinality text

## Output Features

Every generated HTML includes:
- Smooth Chart.js animations
- Professional color palettes
- Dark/light theme toggle ( persisted)
- Download chart as PNG button
- Responsive resize
- Smart tooltips (currency, percentage, date formatting)

## References

- [Chart Selection Guide](references/chart-selection.md) — Decision tree for choosing the right chart type
- [Color Palettes](references/palettes.md) — Palette definitions and when to use each
