# Dashboard Generator 📊

> Transform JSON or CSV data into stunning interactive HTML dashboards. No frontend skills required.

## The Problem

You have data — API responses, CSV exports, metrics, logs. You need a visual dashboard to understand it, share it, or present it. Building a frontend takes hours. Spreadsheet charts are ugly.

## The Solution

One command → beautiful standalone HTML dashboard with:
- 📊 Auto-detected charts (line, bar, donut, scatter)
- 📈 KPI cards with trends
- 🌙 Dark glass-morphism design (Linear/Vercel aesthetic)
- 📋 Sortable data table
- 🎨 5 color palettes

## Quick Start

```bash
# From JSON
python scripts/dashboard_gen.py generate examples/sample_sales.json --title "Q1 Sales" --output sales.html

# From CSV
python scripts/dashboard_gen.py csv data.csv --title "Revenue" --palette ocean

# From stdin
cat api_response.json | python scripts/dashboard_gen.py --title "Live Metrics"
```

Open the generated HTML in any browser. No server needed.

## Installation

```bash
git clone https://github.com/voronindenis5/dashboard-generator.git
cd dashboard-generator
python scripts/dashboard_gen.py generate examples/sample_sales.json
```

## License

MIT © Denis Voronin
