---
name: dashboard-generator
description: "Transform JSON or CSV data into stunning interactive HTML dashboards with auto-detected charts, KPI cards, and dark glass-morphism design. Generates complete standalone HTML with Chart.js."
version: 1.0.0
author: Denis Voronin
license: MIT
metadata:
  hermes:
    tags: [dashboard, data-viz, html, charts, analytics, reporting]
    related_skills: [data-viz-wizard]
---

# Dashboard Generator

## Overview

Turn any JSON or CSV data into a beautiful, interactive HTML dashboard in seconds. No frontend skills required — the script auto-detects data types and picks the best chart types for you.

## When to Use

- You have data (API response, CSV export, metrics) and need a visual dashboard
- You want to share analytics without building a frontend
- Quick reporting: generate a dashboard from raw data for a meeting
- Monitoring: pipe API responses on a schedule to track metrics visually

## Commands

```bash
# From JSON file
python scripts/dashboard_gen.py generate data.json --title "Sales Q3" --output dashboard.html

# From CSV file
python scripts/dashboard_gen.py csv sales.csv --title "Revenue" --output revenue.html

# From stdin (pipe API responses)
cat api_response.json | python scripts/dashboard_gen.py --title "Server Metrics"

# With custom palette
python scripts/dashboard_gen.py generate data.json --palette ocean --title "Analytics"
```

## What It Generates

A standalone HTML file with:
- **KPI cards** — auto-computed min/max/avg/trend for numeric fields
- **Charts** — line for time series, bar for categories, donut for distributions
- **Data table** — sortable, with all raw data
- **Dark glass-morphism design** — looks like Linear/Vercel/Stripe dashboard
- **Chart.js** — fully interactive (hover, zoom, tooltips)

## Palettes

`aurora` (default purple/teal), `ocean` (blues), `sunset` (warm), `forest` (greens), `neon` (cyberpunk)

## Common Pitfalls

1. **Nested JSON not detected.** Flatten nested objects first, or use `--flatten` flag.
2. **Date column not detected.** Ensure dates are in ISO format (YYYY-MM-DD).
3. **Too many series.** Limit to top 10 categories with `--top 10`.

## Verification Checklist

- [ ] HTML file opens in browser
- [ ] Charts render with data
- [ ] KPI cards show correct stats
- [ ] Data table is sortable
