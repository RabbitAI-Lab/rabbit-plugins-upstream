# Chart Selection Guide

Decision tree for choosing the right chart type for your data.

## Decision Tree

```
START: What columns do you have?

├── Date + Numeric
│   ├── 1 numeric series → LINE chart
│   ├── 2-3 numeric series → LINE chart (multi-line)
│   ├── Many series over time → AREA chart (stacked)
│   └── Single value over time + volume → AREA chart
│
├── Categorical + Numeric
│   ├── ≤ 8 categories, 1 metric → PIE or DONUT chart
│   ├── ≤ 8 categories, 2+ metrics → STACKED BAR
│   ├── Many categories → BAR chart (horizontal if labels are long)
│   └── Categories need ranking → BAR chart (sorted)
│
├── Numeric + Numeric
│   ├── Looking for correlation → SCATTER chart
│   └── Time-ordered pairs → SCATTER with trend line
│
├── Multiple Metrics (3-8, same scale)
│   ├── Comparing across categories → RADAR chart
│   └── Time series comparison → LINE chart
│
├── Two Categorical + Numeric
│   └── → HEATMAP-GRID (matrix view)
│
└── Percentage data
    ├── Parts of a whole → PIE or DONUT
    └── Over time → LINE chart (with % formatting)
```

## Chart Types Reference

| Chart Type | Best For | Data Shape |
|-----------|----------|------------|
| **Line** | Trends over time | Date × Numeric |
| **Bar** | Category comparison | Category × Numeric |
| **Stacked Bar** | Part-to-whole across categories | Category × Multiple Numerics |
| **Area** | Cumulative trends | Date × Numeric |
| **Scatter** | Correlation analysis | Numeric × Numeric |
| **Pie** | Simple proportions (≤8 slices) | Category × Single Metric |
| **Donut** | Cleaner proportions | Category × Single Metric |
| **Radar** | Multi-dimensional comparison | 3-8 metrics × Categories |
| **Heatmap Grid** | Matrix density/intensity | 2 Categories × Numeric |

## Auto-Detection Logic

The `--type auto` flag uses this priority:

1. **Date column present?** → Line chart (best for time series)
2. **Categorical + 1 numeric, ≤8 categories?** → Pie/Donut
3. **Categorical + numerics?** → Bar chart
4. **2+ numerics, no date?** → Scatter
5. **4+ numerics, no date?** → Radar
6. **Fallback** → Bar chart

## When to Override Auto

- **Stacked bar**: use when you want to show composition across groups
- **Area**: use for cumulative or volume data
- **Radar**: use when comparing 3-8 metrics on a similar scale
- **Heatmap**: use when you have two categorical dimensions and want intensity
