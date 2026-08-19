# Data Type Detection

## How the Dashboard Generator Detects Data Types

The script automatically analyzes each column and classifies it as one of:

### Date Columns
- ISO format: `2026-01-15`, `2026-01-15T10:30:00`
- Slash format: `2026/01/15`
- European format: `15.01.2026`
- Detection: tries multiple date parse formats on first 20 values. If >70% parse → date column.
- Date columns become X-axis labels in time series charts.

### Numeric Columns
- Integers: `42`, `1000`
- Floats: `3.14`, `0.05`
- Detection: tries `float()` on first 20 values. If >70% succeed → numeric column.
- Numeric columns become Y-axis data, KPI cards, and scatter plot points.

### Categorical Columns
- Strings: product names, regions, status codes
- Detection: anything that isn't date or numeric.
- Categorical columns become bar chart groupings and donut chart segments.

## Auto-Chart Selection Logic

1. **Has date + numeric?** → Line chart (time series)
2. **Has categorical + numeric?** → Bar chart (grouped totals)
3. **Has categorical?** → Donut chart (distribution)
4. **Has 2+ numeric?** → Scatter chart (correlation)

## Data Shapes Supported

### Flat JSON Array (most common)
```json
[{"date": "2026-01-01", "value": 100}, {"date": "2026-01-02", "value": 200}]
```

### Nested JSON
Nested objects are flattened with dot notation:
```json
{"user": {"name": "Alice", "stats": {"clicks": 50}}}
→ {"user.name": "Alice", "user.stats.clicks": 50}
```

### CSV
Standard CSV with header row. Column names from header.
