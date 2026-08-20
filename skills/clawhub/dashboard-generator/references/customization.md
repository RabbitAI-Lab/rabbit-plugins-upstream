# Customization Guide

## Color Palettes

| Palette | Vibe | Best For |
|---------|------|----------|
| `aurora` | Purple/teal/pink | Default — modern SaaS dashboards |
| `ocean` | Blues | Finance, water/air metrics, corporate |
| `sunset` | Warm oranges/reds | Marketing, social media, energy |
| `forest` | Greens | Sustainability, health, agriculture |
| `neon` | Cyberpunk bright | Gaming, crypto, developer tools |

## Using Palettes

```bash
python dashboard_gen.py generate data.json --palette ocean --title "Revenue"
python dashboard_gen.py generate data.json --palette neon --title "Crypto Tracker"
```

## Output HTML Structure

The generated dashboard includes:

1. **Header** — title, description, timestamp, palette name
2. **KPI Grid** — auto-computed stats (avg, min, max, trend%) for each numeric column
3. **Charts Grid** — auto-selected charts based on data types
4. **Data Table** — raw data with sortable columns (first 50 rows)

## Chart.js

Dashboards use [Chart.js 4.x](https://chartjs.org) loaded from CDN. All charts are:
- Interactive (hover tooltips, click-to-toggle series)
- Responsive (auto-resize)
- Animated (smooth load transitions)

## Limitations

- Max 8 KPI cards (first 8 numeric columns)
- Max 5 datasets in time series chart
- Max 10 categories in bar chart
- Max 8 segments in donut chart
- Max 50 rows in data table preview
- Max 10 columns in data table

These limits prevent visual clutter. Use `--top N` to adjust category limits.
