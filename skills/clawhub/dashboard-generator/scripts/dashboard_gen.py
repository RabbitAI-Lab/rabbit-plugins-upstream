#!/usr/bin/env python3
"""
Dashboard Generator — JSON/CSV → stunning interactive HTML dashboard.

Usage:
    python dashboard_gen.py generate data.json --title "Sales" --output dash.html
    python dashboard_gen.py csv sales.csv --title "Revenue"
    cat data.json | python dashboard_gen.py --title "Metrics"
"""
import argparse
import csv
import json
import os
import statistics
import sys
from datetime import datetime
from html import escape
from io import StringIO

PALETTES = {
    "aurora": ["#8b5cf6", "#06b6d4", "#ec4899", "#f59e0b", "#10b981", "#6366f1", "#ef4444", "#14b8a6"],
    "ocean": ["#0ea5e9", "#2563eb", "#06b6d4", "#3b82f6", "#1d4ed8", "#0284c7", "#7dd3fc", "#60a5fa"],
    "sunset": ["#f59e0b", "#ef4444", "#ec4899", "#f97316", "#eab308", "#dc2626", "#fb7185", "#fbbf24"],
    "forest": ["#10b981", "#059669", "#16a34a", "#22c55e", "#4ade80", "#15803d", "#86efac", "#65a30d"],
    "neon": ["#d946ef", "#22d3ee", "#a3e635", "#fb923c", "#f43f5e", "#818cf8", "#fde047", "#34d399"],
}

def detect_column_type(values):
    """Detect if a column is date, numeric, or categorical."""
    non_null = [v for v in values if v is not None and v != ""]
    if not non_null:
        return "null"
    # Try date
    date_count = 0
    for v in non_null[:20]:
        try:
            if isinstance(v, str):
                for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M", "%Y/%m/%d", "%d.%m.%Y"):
                    try:
                        datetime.strptime(v[:19], fmt)
                        date_count += 1
                        break
                    except ValueError:
                        pass
        except Exception:
            pass
    if date_count > len(non_null[:20]) * 0.7:
        return "date"
    # Try numeric
    num_count = 0
    for v in non_null[:20]:
        try:
            float(v)
            num_count += 1
        except (ValueError, TypeError):
            pass
    if num_count > len(non_null[:20]) * 0.7:
        return "numeric"
    return "categorical"


def flatten_json(items):
    """Flatten list of JSON objects into rows."""
    if isinstance(items, dict):
        # Single object — wrap in list
        if any(isinstance(v, list) for v in items.values()):
            for v in items.values():
                if isinstance(v, list) and v:
                    return flatten_json(v)
            return [items]
        return [items]
    if isinstance(items, list):
        rows = []
        for item in items:
            if isinstance(item, dict):
                flat = {}
                def _flatten(obj, prefix=""):
                    for k, v in obj.items():
                        key = f"{prefix}.{k}" if prefix else k
                        if isinstance(v, dict):
                            _flatten(v, key)
                        else:
                            flat[key] = v
                _flatten(item)
                rows.append(flat)
            else:
                rows.append({"value": item})
        return rows
    return [{"value": items}]


def parse_csv(text):
    """Parse CSV text into list of dicts."""
    reader = csv.DictReader(StringIO(text))
    return list(reader)


def compute_stats(values):
    """Compute min, max, avg, trend for numeric values."""
    nums = []
    for v in values:
        try:
            nums.append(float(v))
        except (ValueError, TypeError):
            pass
    if not nums:
        return None
    avg = statistics.mean(nums)
    trend = 0
    if len(nums) >= 4:
        half = len(nums) // 2
        first_half = statistics.mean(nums[:half])
        second_half = statistics.mean(nums[half:])
        if first_half > 0:
            trend = ((second_half - first_half) / first_half) * 100
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": avg,
        "count": len(nums),
        "trend": trend,
    }


def generate_html(data, title, palette_name="aurora", description=""):
    """Generate complete standalone HTML dashboard."""
    colors = PALETTES.get(palette_name, PALETTES["aurora"])

    if not data:
        return "<html><body><h1>No data</h1></body></html>"

    # Get all column names
    columns = list(data[0].keys()) if data else []
    col_types = {}
    for col in columns:
        values = [row.get(col) for row in data]
        col_types[col] = detect_column_type(values)

    date_cols = [c for c, t in col_types.items() if t == "date"]
    num_cols = [c for c, t in col_types.items() if t == "numeric"]
    cat_cols = [c for c, t in col_types.items() if t == "categorical"]

    # KPI cards for numeric columns
    kpi_cards = []
    for col in num_cols[:8]:
        stats = compute_stats([row.get(col) for row in data])
        if stats:
            trend_icon = ""
            trend_color = ""
            if stats["trend"] > 0:
                trend_icon = "↗"
                trend_color = "#10b981"
            elif stats["trend"] < 0:
                trend_icon = "↘"
                trend_color = "#ef4444"
            kpi_cards.append({
                "label": col.replace("_", " ").title(),
                "avg": f"{stats['avg']:,.1f}" if stats['avg'] < 10000 else f"{stats['avg']:,.0f}",
                "min": f"{stats['min']:,.1f}",
                "max": f"{stats['max']:,.1f}",
                "trend": f"{stats['trend']:+.1f}%",
                "trend_icon": trend_icon,
                "trend_color": trend_color,
                "color": colors[len(kpi_cards) % len(colors)],
            })

    # Charts configuration
    charts = []

    # Time series chart
    if date_cols and num_cols:
        date_col = date_cols[0]
        labels = []
        sorted_data = sorted(data, key=lambda r: str(r.get(date_col, "")))
        for row in sorted_data:
            d = str(row.get(date_col, ""))
            labels.append(d[:10] if len(d) > 10 else d)

        datasets = []
        for i, num_col in enumerate(num_cols[:5]):
            values = []
            for row in sorted_data:
                try:
                    values.append(float(row.get(num_col, 0)))
                except (ValueError, TypeError):
                    values.append(0)
            datasets.append({
                "label": num_col.replace("_", " ").title(),
                "data": values,
                "borderColor": colors[i % len(colors)],
                "backgroundColor": colors[i % len(colors)] + "20",
            })
        charts.append({
            "type": "line",
            "title": f"{num_cols[0].title()} over Time",
            "labels": labels,
            "datasets": datasets,
            "id": "timeseries",
        })

    # Category bar chart
    if cat_cols and num_cols:
        cat_col = cat_cols[0]
        num_col = num_cols[0]
        cat_totals = {}
        for row in data:
            cat = str(row.get(cat_col, "Unknown"))
            try:
                val = float(row.get(num_col, 0))
            except (ValueError, TypeError):
                val = 0
            cat_totals[cat] = cat_totals.get(cat, 0) + val
        sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)[:10]
        charts.append({
            "type": "bar",
            "title": f"{num_col.title()} by {cat_col.title()}",
            "labels": [c[0] for c in sorted_cats],
            "datasets": [{
                "label": num_col.title(),
                "data": [c[1] for c in sorted_cats],
                "borderColor": colors[0],
                "backgroundColor": [colors[i % len(colors)] + "80" for i in range(len(sorted_cats))],
            }],
            "id": "category",
        })

    # Distribution donut chart
    if cat_cols:
        cat_col = cat_cols[0]
        counts = {}
        for row in data:
            cat = str(row.get(cat_col, "Unknown"))
            counts[cat] = counts.get(cat, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:8]
        if len(sorted_counts) > 1:
            charts.append({
                "type": "doughnut",
                "title": f"{cat_col.title()} Distribution",
                "labels": [c[0] for c in sorted_counts],
                "datasets": [{
                    "data": [c[1] for c in sorted_counts],
                    "backgroundColor": [colors[i % len(colors)] for i in range(len(sorted_counts))],
                }],
                "id": "distribution",
            })

    # Scatter chart (two numeric columns)
    if len(num_cols) >= 2:
        points = []
        for row in data:
            try:
                x = float(row.get(num_cols[0], 0))
                y = float(row.get(num_cols[1], 0))
                points.append({"x": x, "y": y})
            except (ValueError, TypeError):
                pass
        if points:
            charts.append({
                "type": "scatter",
                "title": f"{num_cols[0].title()} vs {num_cols[1].title()}",
                "labels": [],
                "datasets": [{
                    "label": f"{num_cols[0]} vs {num_cols[1]}",
                    "data": points,
                    "borderColor": colors[2],
                    "backgroundColor": colors[2] + "80",
                }],
                "id": "scatter",
            })

    # Build HTML
    kpi_html = ""
    for i, kpi in enumerate(kpi_cards):
        kpi_html += f'''
        <div class="kpi-card" style="border-left: 3px solid {kpi['color']}">
            <div class="kpi-label">{kpi['label']}</div>
            <div class="kpi-value">{kpi['avg']}</div>
            <div class="kpi-stats">
                <span class="kpi-trend" style="color: {kpi['trend_color']}">{kpi['trend_icon']} {kpi['trend']}</span>
                <span class="kpi-range">min {kpi['min']} / max {kpi['max']}</span>
            </div>
        </div>'''

    charts_js = ""
    chart_canvases = ""
    for chart in charts:
        chart_canvases += f'<div class="chart-wrapper"><h3>{chart["title"]}</h3><canvas id="{chart["id"]}"></canvas></div>'

        config = {
            "type": chart["type"],
            "data": {
                "labels": chart.get("labels", []),
                "datasets": chart["datasets"],
            },
            "options": {
                "responsive": True,
                "maintainAspectRatio": False,
                "plugins": {"legend": {"position": "bottom", "labels": {"color": "#94a3b8"}}},
                "scales": {
                    "x": {"ticks": {"color": "#94a3b8"}, "grid": {"color": "#1e293b"}},
                    "y": {"ticks": {"color": "#94a3b8"}, "grid": {"color": "#1e293b"}},
                } if chart["type"] not in ("doughnut", "pie") else {},
            },
        }
        # For scatter, use linear scales
        if chart["type"] == "scatter":
            config["options"]["scales"] = {
                "x": {"type": "linear", "position": "bottom", "ticks": {"color": "#94a3b8"}, "grid": {"color": "#1e293b"}},
                "y": {"ticks": {"color": "#94a3b8"}, "grid": {"color": "#1e293b"}},
            }

        charts_js += f'''
        new Chart(document.getElementById('{chart["id"]}'), {json.dumps(config)});'''

    # Data table
    table_html = "<table class='data-table'><thead><tr>"
    for col in columns[:10]:
        table_html += f"<th>{escape(col)}</th>"
    table_html += "</tr></thead><tbody>"
    for row in data[:50]:
        table_html += "<tr>"
        for col in columns[:10]:
            val = row.get(col, "")
            table_html += f"<td>{escape(str(val))}</td>"
        table_html += "</tr>"
    table_html += "</tbody></table>"

    now = datetime.now().strftime("%b %d, %Y at %H:%M")

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    background: #0f172a; color: #e2e8f0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    min-height: 100vh; padding: 24px;
}}
.dashboard {{ max-width: 1400px; margin: 0 auto; }}
.header {{ margin-bottom: 32px; }}
.header h1 {{
    font-size: 2rem; font-weight: 800;
    background: linear-gradient(135deg, {colors[0]}, {colors[1]});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.header .subtitle {{ color: #94a3b8; margin-top: 4px; font-size: 0.9rem; }}
.header .timestamp {{ color: #64748b; font-size: 0.8rem; margin-top: 2px; }}

.kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 32px; }}
.kpi-card {{
    background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px);
    border-radius: 12px; padding: 20px;
    transition: transform 0.2s, box-shadow 0.2s;
}}
.kpi-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,0,0,0.3); }}
.kpi-label {{ color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }}
.kpi-value {{ font-size: 1.8rem; font-weight: 700; margin: 4px 0; }}
.kpi-stats {{ display: flex; gap: 12px; font-size: 0.8rem; align-items: center; }}
.kpi-trend {{ font-weight: 600; }}
.kpi-range {{ color: #64748b; }}

.charts-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 24px; margin-bottom: 32px; }}
.chart-wrapper {{
    background: rgba(30, 41, 59, 0.5); backdrop-filter: blur(8px);
    border-radius: 12px; padding: 24px; border: 1px solid rgba(148, 163, 184, 0.1);
}}
.chart-wrapper h3 {{ color: #cbd5e1; font-size: 1rem; margin-bottom: 16px; }}
.chart-wrapper canvas {{ max-height: 300px; }}

.table-wrapper {{
    background: rgba(30, 41, 59, 0.5); backdrop-filter: blur(8px);
    border-radius: 12px; padding: 24px; border: 1px solid rgba(148, 163, 184, 0.1);
    overflow-x: auto;
}}
.table-wrapper h3 {{ color: #cbd5e1; font-size: 1rem; margin-bottom: 16px; }}
.data-table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; }}
.data-table th {{
    text-align: left; padding: 10px 12px; color: #94a3b8;
    border-bottom: 2px solid #334155; cursor: pointer; white-space: nowrap;
}}
.data-table th:hover {{ color: #e2e8f0; }}
.data-table td {{ padding: 8px 12px; border-bottom: 1px solid #1e293b; color: #cbd5e1; }}
.data-table tr:hover {{ background: rgba(148, 163, 184, 0.05); }}

@media (max-width: 768px) {{
    .charts-grid {{ grid-template-columns: 1fr; }}
    .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
</style>
</head>
<body>
<div class="dashboard">
    <div class="header">
        <h1>{escape(title)}</h1>
        <div class="subtitle">{escape(description or f"Dashboard from {len(data)} records × {len(columns)} columns")}</div>
        <div class="timestamp">Generated {now} · Palette: {palette_name}</div>
    </div>

    <div class="kpi-grid">{kpi_html}</div>

    <div class="charts-grid">{chart_canvases}</div>

    <div class="table-wrapper">
        <h3>Raw Data ({len(data)} rows)</h3>
        {table_html}
    </div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {{
    {charts_js}
}});
</script>
</body>
</html>'''
    return html


def main():
    parser = argparse.ArgumentParser(
        description="Transform JSON/CSV data into stunning HTML dashboards.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--title", default="Dashboard", help="Dashboard title")
    parser.add_argument("--description", default="", help="Dashboard description")
    parser.add_argument("--palette", default="aurora", choices=list(PALETTES.keys()), help="Color palette")
    parser.add_argument("--output", "-o", default="dashboard.html", help="Output HTML file")
    sub = parser.add_subparsers(dest="command")
    gen = sub.add_parser("generate", help="Generate from JSON file")
    gen.add_argument("input", help="JSON file path")
    gen.add_argument("--title", default="Dashboard")
    gen.add_argument("--description", default="")
    gen.add_argument("--palette", default="aurora", choices=list(PALETTES.keys()))
    gen.add_argument("--output", "-o", default="dashboard.html")
    csv_p = sub.add_parser("csv", help="Generate from CSV file")
    csv_p.add_argument("input", help="CSV file path")
    csv_p.add_argument("--title", default="Dashboard")
    csv_p.add_argument("--description", default="")
    csv_p.add_argument("--palette", default="aurora", choices=list(PALETTES.keys()))
    csv_p.add_argument("--output", "-o", default="dashboard.html")

    args = parser.parse_args()

    # Determine input
    if args.command == "generate":
        input_file = args.input
    elif args.command == "csv":
        input_file = args.input
    elif args.input:
        input_file = args.input
    else:
        # Read stdin
        input_text = sys.stdin.read()
        try:
            data = json.loads(input_text)
            data = flatten_json(data) if isinstance(data, (list, dict)) else [{"value": data}]
        except json.JSONDecodeError:
            data = parse_csv(input_text)
        html = generate_html(data, args.title, args.palette, args.description)
        Path = __import__("pathlib").Path
        Path(args.output).write_text(html)
        print(f"✅ Dashboard saved to {args.output} ({len(data)} rows)")
        return

    # Read file
    with open(input_file, "r") as f:
        text = f.read()

    if input_file.endswith(".json"):
        data = json.loads(text)
        data = flatten_json(data) if isinstance(data, (list, dict)) else [{"value": data}]
    elif input_file.endswith(".csv"):
        data = parse_csv(text)
    else:
        # Try JSON first, then CSV
        try:
            data = json.loads(text)
            data = flatten_json(data) if isinstance(data, (list, dict)) else [{"value": data}]
        except json.JSONDecodeError:
            data = parse_csv(text)

    html = generate_html(data, args.title, args.palette, args.description)
    from pathlib import Path
    Path(args.output).write_text(html)
    print(f"✅ Dashboard saved to {args.output} ({len(data)} rows, {len(data[0].keys()) if data else 0} columns)")


if __name__ == "__main__":
    main()
