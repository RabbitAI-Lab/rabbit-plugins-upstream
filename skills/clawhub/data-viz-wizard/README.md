# 📊 Data Viz Wizard

> Transform any CSV into stunning interactive charts — instantly.

Data Viz Wizard reads your CSV data and generates **complete standalone HTML files** with beautiful, interactive Chart.js visualizations. No dependencies, no build step — just open the HTML in any browser.

## ✨ Features

- **Auto-detect column types**: dates, numbers, percentages, categories
- **Smart chart selection**: picks the best chart type for your data automatically
- **10 chart types**: line, bar, stacked bar, area, scatter, pie, donut, radar, heatmap-grid
- **Multi-chart dashboards**: generate an entire dashboard from one CSV
- **5 professional palettes**: viridis, sunset, ocean, monochrome, neon
- **Trend lines & moving averages**: built-in analytical overlays
- **Theme toggle**: dark/light mode with persistence
- **PNG export**: download any chart as an image
- **Responsive**: works on desktop and mobile
- **Zero dependencies**: pure Python stdlib, no pip install needed

## 🚀 Quick Start

```bash
# Auto-detect the best chart for your data
python scripts/viz_wizard.py chart sales.csv --type auto --output chart.html

# Generate a full dashboard
python scripts/viz_wizard.py dashboard data.csv --output dashboard.html

# Explicit chart with custom axes
python scripts/viz_wizard.py csv metrics.csv --type line --x date --y revenue --title 'Revenue Trend'

# Pipe data through stdin
cat data.csv | python scripts/viz_wizard.py --auto --output viz.html
```

Open the generated HTML file in any browser. That's it.

## 📋 Commands

| Command | Description |
|---------|-------------|
| `chart <file>` | Single chart with auto type detection |
| `dashboard <file>` | Multi-chart dashboard from one dataset |
| `csv <file>` | Explicit type + column specification |
| _(pipe)_ | `--auto` mode for stdin input |

## 🎨 Color Palettes

| Palette | Best For |
|---------|----------|
| `viridis` | Scientific/data — perceptually uniform |
| `sunset` | Warm, energetic — marketing dashboards |
| `ocean` | Cool, calm — financial/business reports |
| `monochrome` | Clean, minimal — print-friendly |
| `neon` | Vibrant, bold — presentations |

## 📁 Structure

```
data-viz-wizard/
├── SKILL.md                     # Skill definition
├── scripts/
│   └── viz_wizard.py            # Main script (Python stdlib only)
├── references/
│   ├── chart-selection.md       # Chart type decision tree
│   └── palettes.md              # Color palette guide
├── examples/
│   ├── sales.csv                # Sample sales data
│   └── metrics.csv              # Sample metrics data
├── README.md
└── LICENSE
```

## 📝 License

MIT © Denis Voronin
