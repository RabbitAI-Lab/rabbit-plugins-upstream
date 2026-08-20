#!/usr/bin/env python3
"""
Data Viz Wizard — Transform CSV into stunning interactive Chart.js visualizations.

Usage:
  python viz_wizard.py chart sales.csv --type auto --output chart.html
  python viz_wizard.py dashboard data.csv --output dashboard.html
  python viz_wizard.py csv metrics.csv --type line --x date --y revenue --title 'Revenue Trend'
  cat data.csv | python viz_wizard.py --auto --output viz.html

Pure Python stdlib. No pip install required.
MIT License © Denis Voronin
"""

import argparse
import csv
import sys
import re
import json
import os
from datetime import datetime
from collections import OrderedDict
from textwrap import dedent

# ─── Color Palettes ───────────────────────────────────────────────────────────

PALETTES = {
    "viridis": [
        "#440154", "#482878", "#3E4989", "#31688E", "#26828E",
        "#1F9E89", "#35B779", "#6DCD59", "#B4DE2C", "#FDE725",
    ],
    "sunset": [
        "#3C1C2D", "#6B2737", "#A0333F", "#D44E50", "#F2784B",
        "#F8A358", "#FBC96D", "#F7F7B7", "#D9F0A3", "#A1DAB4",
    ],
    "ocean": [
        "#011A3A", "#013A63", "#0353A4", "#0AA6C2", "#2EC4B6",
        "#5BC0BE", "#6FFFE9", "#5390D9", "#48BFE3", "#56CFE1",
    ],
    "monochrome": [
        "#1a1a2e", "#16213e", "#1e2a45", "#2d3561", "#3a4373",
        "#4a5a8a", "#5e72a4", "#7488b8", "#8da0cc", "#a8b8e0",
    ],
    "neon": [
        "#FF006E", "#FB5607", "#FFBE0B", "#8338EC", "#3A86FF",
        "#06FFA5", "#00F5D4", "#FF4081", "#7B2FF7", "#F72585",
    ],
}

# ─── Column Type Detection ────────────────────────────────────────────────────

DATE_PATTERNS = [
    (r'^\d{4}-\d{2}-\d{2}$', '%Y-%m-%d'),
    (r'^\d{4}/\d{2}/\d{2}$', '%Y/%m/%d'),
    (r'^\d{2}-\d{2}-\d{4}$', '%m-%d-%Y'),
    (r'^\d{2}/\d{2}/\d{4}$', '%m/%d/%Y'),
    (r'^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}', '%Y-%m-%d'),
    (r'^\d{6}$', '%Y%m%d'),
    (r'^\d{8}$', '%Y%m%d'),
    (r'^\d{4}-\d{1,2}-\d{1,2}$', '%Y-%m-%d'),
]


def detect_column_type(name, values):
    """Detect column type: date, numeric, percentage, or categorical."""
    non_empty = [v for v in values if v != '' and v is not None]
    if not non_empty:
        return 'categorical'

    sample = non_empty[:100]

    # Check percentage
    pct_count = sum(1 for v in sample if isinstance(v, str) and v.strip().endswith('%'))
    if pct_count > len(sample) * 0.7:
        return 'percentage'

    # Check date
    date_count = 0
    for v in sample:
        s = str(v).strip()
        for pattern, _ in DATE_PATTERNS:
            if re.match(pattern, s):
                date_count += 1
                break
    if date_count > len(sample) * 0.7:
        return 'date'

    # Check numeric
    num_count = 0
    for v in sample:
        s = str(v).strip().replace(',', '').replace('$', '').replace('€', '').replace('£', '')
        try:
            float(s)
            num_count += 1
        except (ValueError, AttributeError):
            pass
    if num_count > len(sample) * 0.8:
        return 'numeric'

    return 'categorical'


def parse_numeric(value):
    """Parse a value into a float, handling currency, commas, percentages."""
    if value is None or value == '':
        return None
    s = str(value).strip()
    is_pct = s.endswith('%')
    s = s.replace(',', '').replace('$', '').replace('€', '').replace('£', '').replace('%', '')
    try:
        val = float(s)
        if is_pct:
            val = val  # Keep as-is for display; we know it's a percentage from type
        return val
    except ValueError:
        return None


def parse_percentage(value):
    """Parse a percentage value, return float."""
    if value is None or value == '':
        return None
    s = str(value).strip().replace('%', '')
    try:
        return float(s)
    except ValueError:
        return None


def analyze_csv(headers, rows):
    """Analyze CSV columns and return column metadata."""
    columns = OrderedDict()
    for i, h in enumerate(headers):
        col_values = [r[i] if i < len(r) else '' for r in rows]
        col_type = detect_column_type(h, col_values)
        columns[h] = {
            'index': i,
            'type': col_type,
            'values': col_values,
            'unique': len(set(v for v in col_values if v != '')),
        }
    return columns


# ─── Chart Type Selection ─────────────────────────────────────────────────────

def select_best_chart(columns):
    """Smart chart selection based on data characteristics."""
    date_cols = [h for h, c in columns.items() if c['type'] == 'date']
    num_cols = [h for h, c in columns.items() if c['type'] == 'numeric']
    pct_cols = [h for h, c in columns.items() if c['type'] == 'percentage']
    cat_cols = [h for h, c in columns.items() if c['type'] == 'categorical']

    all_num = num_cols + pct_cols

    # If we have a date column and numeric columns -> line chart
    if date_cols and all_num:
        return 'line', date_cols[0], [all_num[0]]

    # If we have categories and numerics
    if cat_cols and all_num:
        # Pie/donut if few categories and one numeric
        first_cat = columns[cat_cols[0]]
        if first_cat['unique'] <= 8 and len(all_num) == 1:
            return 'pie', cat_cols[0], [all_num[0]]
        # Bar chart
        return 'bar', cat_cols[0], [all_num[0]] if all_num else []

    # Two numerics -> scatter
    if len(num_cols) >= 2:
        return 'scatter', num_cols[0], [num_cols[1]]

    # Radar if multiple numerics, no dates
    if len(all_num) >= 4:
        return 'radar', None, all_num[:6]

    # Fallback
    if all_num:
        return 'bar', None, [all_num[0]]

    return 'bar', list(columns.keys())[0] if columns else '', []


# ─── Data Preparation ─────────────────────────────────────────────────────────

def prepare_chart_data(columns, x_col, y_cols, chart_type):
    """Prepare data arrays for charting."""
    labels = []
    datasets = []

    if x_col and x_col in columns:
        labels = columns[x_col]['values']
    else:
        labels = [str(i + 1) for i in range(len(next(iter(columns.values()))['values']))]

    for yc in y_cols:
        if yc not in columns:
            continue
        col = columns[yc]
        if col['type'] == 'percentage':
            vals = [parse_percentage(v) for v in col['values']]
        elif col['type'] == 'numeric':
            vals = [parse_numeric(v) for v in col['values']]
        else:
            vals = [None if v == '' else v for v in col['values']]
        datasets.append({
            'label': yc,
            'data': vals,
            'col_type': col['type'],
        })

    return labels, datasets


def compute_moving_average(data, window):
    """Compute simple moving average."""
    result = []
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            chunk = [d for d in data[i - window + 1:i + 1] if d is not None]
            if chunk:
                result.append(sum(chunk) / len(chunk))
            else:
                result.append(None)
    return result


def compute_trend_line(data):
    """Compute linear trend line using least squares."""
    valid = [(i, d) for i, d in enumerate(data) if d is not None]
    if len(valid) < 2:
        return [None] * len(data)
    xs = [v[0] for v in valid]
    ys = [v[1] for v in valid]
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x * y for x, y in valid)
    sum_xx = sum(x * x for x in xs)
    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        return [None] * len(data)
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    return [slope * i + intercept for i in range(len(data))]


# ─── Aggregation ──────────────────────────────────────────────────────────────

def aggregate_data(columns, x_col, y_col, agg='sum'):
    """Aggregate y_col values grouped by x_col."""
    if x_col not in columns or y_col not in columns:
        return [], []
    x_vals = columns[x_col]['values']
    y_col_info = columns[y_col]
    y_vals_raw = y_col_info['values']

    groups = OrderedDict()
    for i, xv in enumerate(x_vals):
        if xv == '':
            continue
        if xv not in groups:
            groups[xv] = []
        if i < len(y_vals_raw):
            if y_col_info['type'] == 'percentage':
                v = parse_percentage(y_vals_raw[i])
            elif y_col_info['type'] == 'numeric':
                v = parse_numeric(y_vals_raw[i])
            else:
                v = None
            if v is not None:
                groups[xv].append(v)

    labels = list(groups.keys())
    values = []
    for k in labels:
        g = groups[k]
        if not g:
            values.append(0)
        elif agg == 'sum':
            values.append(sum(g))
        elif agg == 'avg':
            values.append(sum(g) / len(g))
        elif agg == 'count':
            values.append(len(g))
        elif agg == 'max':
            values.append(max(g))
        elif agg == 'min':
            values.append(min(g))
        else:
            values.append(sum(g))

    return labels, values


# ─── HTML Generation ──────────────────────────────────────────────────────────

def hex_to_rgba(hex_color, alpha=1.0):
    """Convert hex color to rgba string."""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def build_single_chart_config(chart_type, labels, datasets, palette_name, title, options=None):
    """Build a Chart.js config object as a Python dict."""
    palette = PALETTES.get(palette_name, PALETTES['viridis'])
    config = {
        'type': chart_type if chart_type != 'stacked' else 'bar',
        'data': {
            'labels': list(labels),
            'datasets': [],
        },
        'options': {
            'responsive': True,
            'maintainAspectRatio': False,
            'plugins': {
                'title': {
                    'display': bool(title),
                    'text': title or '',
                    'font': {'size': 18, 'weight': 'bold'},
                    'padding': {'top': 10, 'bottom': 20},
                },
                'legend': {
                    'position': 'top',
                    'labels': {'usePointStyle': True, 'padding': 15},
                },
                'tooltip': {'mode': 'index', 'intersect': False},
            },
            'animation': {'duration': 1200, 'easing': 'easeOutQuart'},
        },
    }

    # Stacked option
    if chart_type == 'stacked':
        config['options']['scales'] = {
            'x': {'stacked': True},
            'y': {'stacked': True},
        }

    # Area fill
    if chart_type == 'area':
        config['type'] = 'line'

    for i, ds in enumerate(datasets):
        color = palette[i % len(palette)]
        bg_alpha = 0.6 if chart_type in ('pie', 'donut') else (0.2 if chart_type == 'area' else 0.8)

        dataset_config = {
            'label': ds['label'],
            'data': ds['data'],
            'borderColor': color,
            'backgroundColor': color if chart_type in ('pie', 'donut', 'bar') else hex_to_rgba(color, bg_alpha),
        }

        if chart_type in ('line', 'area'):
            dataset_config['fill'] = chart_type == 'area'
            dataset_config['tension'] = 0.35
            dataset_config['borderWidth'] = 2.5
            dataset_config['pointRadius'] = 4
            dataset_config['pointHoverRadius'] = 7
            dataset_config['pointBackgroundColor'] = color

        if chart_type == 'scatter':
            config['type'] = 'scatter'
            dataset_config['backgroundColor'] = hex_to_rgba(color, 0.7)
            dataset_config['borderColor'] = color
            dataset_config['pointRadius'] = 5

        if chart_type in ('pie', 'donut'):
            # Override: use single dataset with different colors per slice
            colors = [palette[j % len(palette)] for j in range(len(ds['data']))]
            dataset_config['backgroundColor'] = colors
            dataset_config['borderColor'] = '#fff'
            dataset_config['borderWidth'] = 2
            if chart_type == 'donut':
                dataset_config['cutout'] = '55%'

        if chart_type == 'radar':
            config['type'] = 'radar'
            dataset_config['fill'] = True
            dataset_config['backgroundColor'] = hex_to_rgba(color, 0.2)
            dataset_config['pointBackgroundColor'] = color

        if chart_type == 'bar':
            dataset_config['borderRadius'] = 6
            dataset_config['borderWidth'] = 0

        if chart_type == 'stacked':
            dataset_config['borderRadius'] = 4
            dataset_config['borderWidth'] = 0

        config['data']['datasets'].append(dataset_config)

    # Apply extra options
    if options:
        if options.get('moving_average'):
            ma_data = compute_moving_average(datasets[0]['data'], options['moving_average'])
            ma_color = palette[(len(datasets)) % len(palette)]
            config['data']['datasets'].append({
                'label': f'MA({options["moving_average"]})',
                'data': ma_data,
                'borderColor': ma_color,
                'backgroundColor': hex_to_rgba(ma_color, 0.1),
                'borderDash': [6, 4],
                'borderWidth': 2,
                'fill': False,
                'tension': 0.35,
                'pointRadius': 0,
            })

        if options.get('trend'):
            trend_data = compute_trend_line(datasets[0]['data'])
            trend_color = '#ff4444'
            config['data']['datasets'].append({
                'label': 'Trend',
                'data': trend_data,
                'borderColor': trend_color,
                'borderWidth': 2,
                'borderDash': [3, 3],
                'fill': False,
                'pointRadius': 0,
            })

    return config


# ─── Heatmap Grid ─────────────────────────────────────────────────────────────

def build_heatmap_grid(columns, x_col, y_col, value_col, palette_name, title):
    """Build a heatmap grid visualization using a matrix of colored cells."""
    palette = PALETTES.get(palette_name, PALETTES['viridis'])

    if x_col not in columns or y_col not in columns or value_col not in columns:
        return None

    x_unique = list(OrderedDict.fromkeys(columns[x_col]['values']))
    y_unique = list(OrderedDict.fromkeys(columns[y_col]['values']))
    x_unique = [x for x in x_unique if x != '']
    y_unique = [y for y in y_unique if y != '']

    # Build value matrix
    matrix = {}
    val_col = columns[value_col]
    for i in range(len(columns[x_col]['values'])):
        xv = columns[x_col]['values'][i]
        yv = columns[y_col]['values'][i]
        if xv == '' or yv == '' or i >= len(val_col['values']):
            continue
        if val_col['type'] == 'percentage':
            v = parse_percentage(val_col['values'][i])
        else:
            v = parse_numeric(val_col['values'][i])
        if v is not None:
            matrix[(xv, yv)] = v

    return {
        'x_labels': x_unique,
        'y_labels': y_unique,
        'matrix': {f"{k[0]}|{k[1]}": v for k, v in matrix.items()},
        'palette': palette,
        'title': title or f'{value_col} Heatmap',
    }


# ─── HTML Template ────────────────────────────────────────────────────────────

SINGLE_CHART_HTML = dedent("""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
  :root {
    --bg: #ffffff;
    --card-bg: #f8f9fa;
    --text: #1a1a2e;
    --text-muted: #6c757d;
    --border: #dee2e6;
    --accent: #4361ee;
    --shadow: rgba(0,0,0,0.08);
  }
  [data-theme="dark"] {
    --bg: #0d1117;
    --card-bg: #161b22;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --border: #30363d;
    --accent: #58a6ff;
    --shadow: rgba(0,0,0,0.3);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
    min-height: 100vh;
  }
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    border-bottom: 1px solid var(--border);
    background: var(--card-bg);
  }
  .header h1 { font-size: 1.4rem; }
  .controls { display: flex; gap: 8px; }
  .btn {
    background: var(--accent);
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 600;
    transition: opacity 0.2s, transform 0.1s;
  }
  .btn:hover { opacity: 0.85; }
  .btn:active { transform: scale(0.96); }
  .btn-secondary {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text);
  }
  .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 24px;
  }
  .chart-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 2px 12px var(--shadow);
    border: 1px solid var(--border);
  }
  .chart-wrapper {
    position: relative;
    height: 500px;
  }
  .footer {
    text-align: center;
    padding: 16px;
    color: var(--text-muted);
    font-size: 0.8rem;
  }
  @media (max-width: 768px) {
    .chart-wrapper { height: 350px; }
    .header h1 { font-size: 1.1rem; }
  }
</style>
</head>
<body data-theme="light">
  <div class="header">
    <h1>📊 __TITLE__</h1>
    <div class="controls">
      <button class="btn btn-secondary" onclick="toggleTheme()" id="themeBtn">🌙 Dark</button>
      <button class="btn" onclick="downloadChart()">⬇ PNG</button>
    </div>
  </div>
  <div class="container">
    <div class="chart-card">
      <div class="chart-wrapper">
        <canvas id="mainChart"></canvas>
      </div>
    </div>
  </div>
  <div class="footer">Generated by Data Viz Wizard • Chart.js</div>

<script>
  const chartConfig = __CHART_CONFIG__;
  const heatmapData = __HEATMAP_DATA__;
  let chart;
  let isHeatmap = heatmapData !== null;

  function getThemeColors() {
    const styles = getComputedStyle(document.body);
    return {
      text: styles.getPropertyValue('--text').trim(),
      muted: styles.getPropertyValue('--text-muted').trim(),
      border: styles.getPropertyValue('--border').trim(),
    };
  }

  function applyTheme(config) {
    const c = getThemeColors();
    if (!config.options) config.options = {};
    if (!config.options.plugins) config.options.plugins = {};
    // Apply font colors
    if (!config.options.scales) config.options.scales = {};
    for (const axis of ['x', 'y']) {
      if (!config.options.scales[axis]) continue;
      if (!config.options.scales[axis].ticks) config.options.scales[axis].ticks = {};
      if (!config.options.scales[axis].grid) config.options.scales[axis].grid = {};
      config.options.scales[axis].ticks.color = c.muted;
      config.options.scales[axis].grid.color = c.border;
      if (!config.options.scales[axis].title) config.options.scales[axis].title = {};
      config.options.scales[axis].title.color = c.muted;
    }
    if (config.options.plugins.legend) {
      if (!config.options.plugins.legend.labels) config.options.plugins.legend.labels = {};
      config.options.plugins.legend.labels.color = c.text;
    }
    if (config.options.plugins.title) {
      config.options.plugins.title.color = c.text;
    }
    return config;
  }

  function createChart() {
    const ctx = document.getElementById('mainChart').getElement ? null : document.getElementById('mainChart').getContext('2d');
    if (chart) chart.destroy();

    if (isHeatmap) {
      // Render heatmap as custom canvas
      const canvas = document.getElementById('mainChart');
      drawHeatmap(canvas, heatmapData);
      return;
    }

    const config = JSON.parse(JSON.stringify(chartConfig));
    applyTheme(config);
    chart = new Chart(ctx, config);
  }

  function drawHeatmap(canvas, data) {
    canvas.style.height = '100%';
    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);

    const W = rect.width, H = rect.height;
    const padLeft = 100, padTop = 50, padBottom = 30, padRight = 30;
    const cols = data.x_labels.length;
    const rows = data.y_labels.length;
    const cellW = (W - padLeft - padRight) / cols;
    const cellH = (H - padTop - padBottom) / rows;
    const palette = data.palette;
    const themeColors = getThemeColors();

    // Get min/max
    const vals = Object.values(data.matrix);
    const minV = Math.min(...vals);
    const maxV = Math.max(...vals);

    function getColor(val) {
      const t = (val - minV) / (maxV - minV || 1);
      const idx = Math.round(t * (palette.length - 1));
      return palette[idx];
    }

    // Draw cells
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const xv = data.x_labels[c];
        const yv = data.y_labels[r];
        const key = xv + '|' + yv;
        const val = data.matrix[key];
        const x = padLeft + c * cellW;
        const y = padTop + r * cellH;
        if (val !== undefined) {
          ctx.fillStyle = getColor(val);
        } else {
          ctx.fillStyle = themeColors.border;
        }
        ctx.fillRect(x + 2, y + 2, cellW - 4, cellH - 4);

        // Value text
        if (val !== undefined) {
          ctx.fillStyle = '#fff';
          ctx.font = '12px sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(val.toFixed(1), x + cellW/2, y + cellH/2);
        }
      }
    }

    // Labels
    ctx.fillStyle = themeColors.muted;
    ctx.font = '11px sans-serif';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (let r = 0; r < rows; r++) {
      ctx.fillText(data.y_labels[r], padLeft - 8, padTop + r * cellH + cellH/2);
    }
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (let c = 0; c < cols; c++) {
      const label = data.x_labels[c];
      ctx.save();
      ctx.translate(padLeft + c * cellW + cellW/2, padTop + rows * cellH + 8);
      if (cols > 10) ctx.rotate(-0.4);
      ctx.fillText(label, 0, 0);
      ctx.restore();
    }
  }

  function toggleTheme() {
    const body = document.body;
    const current = body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', next);
    document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️ Light' : '🌙 Dark';
    localStorage.setItem('viz-theme', next);
    createChart();
  }

  function downloadChart() {
    const canvas = document.getElementById('mainChart');
    const link = document.createElement('a');
    link.download = 'chart.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  }

  // Restore theme
  const savedTheme = localStorage.getItem('viz-theme');
  if (savedTheme) {
    document.body.setAttribute('data-theme', savedTheme);
    document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀️ Light' : '🌙 Dark';
  }

  // Wait for Chart.js to load
  window.addEventListener('load', createChart);
  let resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { if (isHeatmap) createChart(); }, 200);
  });
</script>
</body>
</html>
""")

DASHBOARD_HTML = dedent("""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
  :root {
    --bg: #ffffff;
    --card-bg: #f8f9fa;
    --text: #1a1a2e;
    --text-muted: #6c757d;
    --border: #dee2e6;
    --accent: #4361ee;
    --shadow: rgba(0,0,0,0.08);
  }
  [data-theme="dark"] {
    --bg: #0d1117;
    --card-bg: #161b22;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --border: #30363d;
    --accent: #58a6ff;
    --shadow: rgba(0,0,0,0.3);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
    min-height: 100vh;
  }
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    border-bottom: 1px solid var(--border);
    background: var(--card-bg);
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .header h1 { font-size: 1.4rem; }
  .controls { display: flex; gap: 8px; }
  .btn {
    background: var(--accent);
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 600;
    transition: opacity 0.2s, transform 0.1s;
  }
  .btn:hover { opacity: 0.85; }
  .btn:active { transform: scale(0.96); }
  .btn-secondary {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text);
  }
  .stats-row {
    display: flex;
    gap: 16px;
    padding: 24px;
    max-width: 1400px;
    margin: 0 auto;
    flex-wrap: wrap;
  }
  .stat-card {
    flex: 1;
    min-width: 200px;
    background: var(--card-bg);
    border-radius: 12px;
    padding: 20px;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px var(--shadow);
    text-align: center;
  }
  .stat-card .label {
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }
  .stat-card .value {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--accent);
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 0 24px 24px;
    max-width: 1400px;
    margin: 0 auto;
  }
  .grid .full { grid-column: 1 / -1; }
  .chart-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 2px 12px var(--shadow);
    border: 1px solid var(--border);
  }
  .chart-card h3 {
    font-size: 1rem;
    margin-bottom: 12px;
    color: var(--text-muted);
  }
  .chart-wrapper {
    position: relative;
    height: 320px;
  }
  .grid .full .chart-wrapper { height: 420px; }
  .footer {
    text-align: center;
    padding: 20px;
    color: var(--text-muted);
    font-size: 0.8rem;
  }
  @media (max-width: 768px) {
    .grid { grid-template-columns: 1fr; }
    .chart-wrapper { height: 280px; }
    .header h1 { font-size: 1.1rem; }
  }
</style>
</head>
<body data-theme="light">
  <div class="header">
    <h1>📊 __TITLE__</h1>
    <div class="controls">
      <button class="btn btn-secondary" onclick="toggleTheme()" id="themeBtn">🌙 Dark</button>
    </div>
  </div>
  <div class="stats-row" id="statsRow"></div>
  <div class="grid" id="grid">
    __CHART_SLOTS__
  </div>
  <div class="footer">Generated by Data Viz Wizard • Chart.js</div>

<script>
  const charts = __CHARTS_JSON__;
  let chartInstances = [];

  function getThemeColors() {
    const styles = getComputedStyle(document.body);
    return {
      text: styles.getPropertyValue('--text').trim(),
      muted: styles.getPropertyValue('--text-muted').trim(),
      border: styles.getPropertyValue('--border').trim(),
    };
  }

  function applyTheme(config) {
    const c = getThemeColors();
    if (!config.options) config.options = {};
    if (!config.options.plugins) config.options.plugins = {};
    if (!config.options.scales) config.options.scales = {};
    for (const axis of ['x', 'y']) {
      if (!config.options.scales[axis]) continue;
      if (!config.options.scales[axis].ticks) config.options.scales[axis].ticks = {};
      if (!config.options.scales[axis].grid) config.options.scales[axis].grid = {};
      config.options.scales[axis].ticks.color = c.muted;
      config.options.scales[axis].grid.color = c.border;
    }
    if (config.options.plugins.legend && config.options.plugins.legend.labels) {
      config.options.plugins.legend.labels.color = c.text;
    }
    if (config.options.plugins.title) {
      config.options.plugins.title.color = c.text;
    }
    return config;
  }

  function createCharts() {
    chartInstances.forEach(c => c.destroy());
    chartInstances = [];
    charts.forEach((cfg, i) => {
      const canvas = document.getElementById('chart_' + i);
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const config = JSON.parse(JSON.stringify(cfg));
      applyTheme(config);
      chartInstances.push(new Chart(ctx, config));
    });
    renderStats();
  }

  function renderStats() {
    const colors = getThemeColors();
    const row = document.getElementById('statsRow');
    row.innerHTML = '';
    charts.forEach((cfg, i) => {
      const ds = cfg.data.datasets[0];
      if (!ds || !ds.data || !ds.data.length) return;
      const vals = ds.data.filter(v => v !== null && v !== undefined);
      if (!vals.length) return;
      const total = vals.reduce((a, b) => a + b, 0);
      const avg = total / vals.length;
      const max = Math.max(...vals);
      const label = cfg.options?.plugins?.title?.text || ds.label || 'Chart ' + (i+1);
      const card = document.createElement('div');
      card.className = 'stat-card';
      const isPct = cfg._isPercentage;
      const fmt = (v) => isPct ? v.toFixed(1) + '%' : v.toLocaleString(undefined, {maximumFractionDigits: 0});
      card.innerHTML = `
        <div class="label">${label} — Sum</div>
        <div class="value">${fmt(total)}</div>
      `;
      row.appendChild(card);
    });
  }

  function toggleTheme() {
    const body = document.body;
    const current = body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', next);
    document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️ Light' : '🌙 Dark';
    localStorage.setItem('viz-theme', next);
    createCharts();
  }

  const savedTheme = localStorage.getItem('viz-theme');
  if (savedTheme) {
    document.body.setAttribute('data-theme', savedTheme);
    document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀️ Light' : '🌙 Dark';
  }

  window.addEventListener('load', createChartsWithTheme);
</script>
</body>
</html>
""")


def generate_single_chart_html(config, heatmap_data, title):
    """Generate complete HTML for a single chart."""
    html = SINGLE_CHART_HTML
    html = html.replace('__TITLE__', title or 'Chart')
    html = html.replace('__CHART_CONFIG__', json.dumps(config, default=str))
    html = html.replace('__HEATMAP_DATA__', json.dumps(heatmap_data, default=str) if heatmap_data else 'null')
    return html


def generate_dashboard_html(charts_config, title):
    """Generate multi-chart dashboard HTML."""
    html = DASHBOARD_HTML
    html = html.replace('__TITLE__', title or 'Dashboard')

    # Generate chart slots
    slots = []
    for i, cfg in enumerate(charts_config):
        is_full = i == 0  # First chart is full width
        full_class = ' full' if is_full else ''
        chart_title = cfg.get('options', {}).get('plugins', {}).get('title', {}).get('text', f'Chart {i+1}')
        slots.append(f"""\
    <div class="chart-card{full_class}">
      <h3>{chart_title}</h3>
      <div class="chart-wrapper">
        <canvas id="chart_{i}"></canvas>
      </div>
    </div>""")

    html = html.replace('__CHART_SLOTS__', '\n'.join(slots))

    # Add createChartsWithTheme function
    script_extra = """
  function createChartsWithTheme() {
    chartInstances.forEach(c => c.destroy());
    chartInstances = [];
    charts.forEach((cfg, i) => {
      const canvas = document.getElementById('chart_' + i);
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const config = JSON.parse(JSON.stringify(cfg));
      applyTheme(config);
      chartInstances.push(new Chart(ctx, config));
    });
    renderStats();
  }
"""
    html = html.replace("window.addEventListener('load', createChartsWithTheme);",
                        script_extra + "\n  window.addEventListener('load', createChartsWithTheme);")

    html = html.replace('__CHARTS_JSON__', json.dumps(charts_config, default=str))
    return html


# ─── Dashboard Generation ─────────────────────────────────────────────────────

def generate_dashboard(columns, palette_name, title):
    """Generate a multi-chart dashboard from columns."""
    charts = []

    date_cols = [h for h, c in columns.items() if c['type'] == 'date']
    num_cols = [h for h, c in columns.items() if c['type'] == 'numeric']
    pct_cols = [h for h, c in columns.items() if c['type'] == 'percentage']
    cat_cols = [h for h, c in columns.items() if c['type'] == 'categorical']
    all_num = num_cols + pct_cols

    # Chart 1: Line chart over time (or primary numeric)
    if date_cols and all_num:
        x_col = date_cols[0]
        y_cols = all_num[:3]
        labels, datasets = prepare_chart_data(columns, x_col, y_cols, 'line')
        # Aggregate if multiple rows per date
        if cat_cols:
            # Aggregate by date
            agg_labels = []
            agg_datasets = []
            for yc in y_cols:
                l, v = aggregate_data(columns, x_col, yc, 'sum')
                if not agg_labels:
                    agg_labels = l
                agg_datasets.append({'label': yc, 'data': v, 'col_type': columns[yc]['type']})
            labels, datasets = agg_labels, agg_datasets
        cfg = build_single_chart_config('line', labels, datasets, palette_name,
                                        f'{", ".join(y_cols)} over time')
        # Mark percentage
        for ds in cfg['data']['datasets']:
            ds_y = ds['label']
            if ds_y in pct_cols:
                cfg['_isPercentage'] = True
        charts.append(cfg)

    # Chart 2: Bar chart by category
    if cat_cols and all_num:
        cat = cat_cols[0]
        for yc in all_num[:2]:
            labels, values = aggregate_data(columns, cat, yc, 'sum')
            if labels:
                ds = [{'label': yc, 'data': values, 'col_type': columns[yc]['type']}]
                cfg = build_single_chart_config('bar', labels, ds, palette_name, f'{yc} by {cat}')
                if yc in pct_cols:
                    cfg['_isPercentage'] = True
                charts.append(cfg)

    # Chart 3: Pie/Donut of category distribution
    if cat_cols and all_num:
        cat = cat_cols[0]
        yc = all_num[0]
        labels, values = aggregate_data(columns, cat, yc, 'sum')
        if labels and len(labels) <= 10:
            ds = [{'label': yc, 'data': values, 'col_type': columns[yc]['type']}]
            cfg = build_single_chart_config('donut', labels, ds, palette_name, f'{yc} Distribution')
            charts.append(cfg)

    # Chart 4: Radar chart comparing multiple metrics (if 3+ numerics)
    if len(all_num) >= 3 and len(all_num) <= 8:
        # Use categories for radar, or just use all metrics
        if cat_cols:
            cat = cat_cols[0]
            if columns[cat]['unique'] <= 6:
                radar_labels = [v for v in columns[cat]['values'] if v != '']
                radar_labels = list(dict.fromkeys(radar_labels))[:6]
                radar_datasets = []
                for yc in all_num[:4]:
                    vals = []
                    for cl in radar_labels:
                        agg_labels, agg_vals = aggregate_data(columns, cat, yc, 'avg')
                        if cl in agg_labels:
                            idx = agg_labels.index(cl)
                            vals.append(agg_vals[idx])
                        else:
                            vals.append(0)
                    radar_datasets.append({'label': yc, 'data': vals, 'col_type': columns[yc]['type']})
                cfg = build_single_chart_config('radar', radar_labels, radar_datasets, palette_name, 'Metric Comparison')
                charts.append(cfg)

    # Chart 5: Area chart
    if date_cols and all_num:
        x_col = date_cols[0]
        yc = all_num[0]
        if cat_cols:
            labels, values = aggregate_data(columns, x_col, yc, 'sum')
        else:
            labels, datasets = prepare_chart_data(columns, x_col, [yc], 'area')
            labels = list(labels)
            values = datasets[0]['data']
        ds = [{'label': yc, 'data': values, 'col_type': columns[yc]['type']}]
        cfg = build_single_chart_config('area', labels, ds, palette_name, f'{yc} Trend')
        charts.append(cfg)

    # Chart 6: Scatter
    if len(num_cols) >= 2:
        x_c, y_c = num_cols[0], num_cols[1]
        x_vals = [parse_numeric(v) for v in columns[x_c]['values']]
        y_vals = [parse_numeric(v) for v in columns[y_c]['values']]
        scatter_data = [{'x': x_vals[i], 'y': y_vals[i]} for i in range(min(len(x_vals), len(y_vals)))
                        if x_vals[i] is not None and y_vals[i] is not None]
        if scatter_data:
            ds = [{'label': f'{y_c} vs {x_c}', 'data': scatter_data, 'col_type': 'numeric'}]
            cfg = {
                'type': 'scatter',
                'data': {'datasets': [{
                    'label': f'{y_c} vs {x_c}',
                    'data': scatter_data,
                    'backgroundColor': PALETTES[palette_name][0],
                    'borderColor': PALETTES[palette_name][0],
                }]},
                'options': {
                    'responsive': True,
                    'maintainAspectRatio': False,
                    'plugins': {
                        'title': {'display': True, 'text': f'{y_c} vs {x_c}', 'font': {'size': 14}},
                        'legend': {'position': 'top'},
                    },
                    'scales': {
                        'x': {'title': {'display': True, 'text': x_c}},
                        'y': {'title': {'display': True, 'text': y_c}},
                    },
                    'animation': {'duration': 1000, 'easing': 'easeOutQuart'},
                },
            }
            charts.append(cfg)

    if not charts:
        # Fallback: just bar chart of first numeric
        if all_num:
            labels, datasets = prepare_chart_data(columns, None, [all_num[0]], 'bar')
            cfg = build_single_chart_config('bar', labels, datasets, palette_name, all_num[0])
            charts.append(cfg)

    return generate_dashboard_html(charts, title or 'Data Dashboard')


# ─── CSV Reading ──────────────────────────────────────────────────────────────

def read_csv_file(filepath):
    """Read CSV from file path."""
    with open(filepath, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    return headers, rows


def read_csv_stdin():
    """Read CSV from stdin."""
    reader = csv.reader(sys.stdin)
    headers = next(reader)
    rows = list(reader)
    return headers, rows


# ─── Main / CLI ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Data Viz Wizard — Transform CSV into interactive Chart.js visualizations.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
            Examples:
              viz_wizard.py chart sales.csv --type auto --output chart.html
              viz_wizard.py dashboard data.csv --output dashboard.html
              viz_wizard.py csv metrics.csv --type line --x date --y revenue --title 'Revenue Trend'
              cat data.csv | viz_wizard.py --auto --output viz.html
        """)
    )
    parser.add_argument('command', nargs='?', default=None,
                        choices=['chart', 'dashboard', 'csv'],
                        help='Command: chart, dashboard, or csv')
    parser.add_argument('input', nargs='?', default=None,
                        help='Input CSV file (use --auto for stdin)')
    parser.add_argument('--type', default='auto',
                        help='Chart type: auto, line, bar, stacked, area, scatter, pie, donut, radar, heatmap-grid')
    parser.add_argument('--x', default=None, help='X-axis column name')
    parser.add_argument('--y', default=None, help='Y-axis column name(s), comma-separated')
    parser.add_argument('--output', '-o', default='viz_output.html', help='Output HTML file path')
    parser.add_argument('--title', default=None, help='Chart title')
    parser.add_argument('--palette', default='viridis',
                        choices=list(PALETTES.keys()),
                        help='Color palette')
    parser.add_argument('--trend', action='store_true', help='Add trend line')
    parser.add_argument('--moving-average', '-ma', type=int, default=None,
                        help='Moving average window size')
    parser.add_argument('--theme', default='auto', choices=['dark', 'light', 'auto'],
                        help='Initial theme')
    parser.add_argument('--auto', action='store_true', help='Auto mode (read CSV from stdin)')
    parser.add_argument('--aggregate', default=None, choices=['sum', 'avg', 'count', 'max', 'min'],
                        help='Aggregation method when grouping')

    args = parser.parse_args()

    # Read data
    if args.auto or (not args.input and not sys.stdin.isatty()):
        headers, rows = read_csv_stdin()
    elif args.input:
        headers, rows = read_csv_file(args.input)
    else:
        parser.print_help()
        sys.exit(1)

    if not headers or not rows:
        print("Error: No data found in CSV.", file=sys.stderr)
        sys.exit(1)

    # Analyze columns
    columns = analyze_csv(headers, rows)

    # Set default theme
    theme = args.theme if args.theme != 'auto' else 'light'

    # Determine command
    command = args.command
    if not command:
        command = 'chart'

    # ─── Dashboard ───
    if command == 'dashboard' or (command == 'chart' and args.type == 'auto' and not args.x and not args.y and len(columns) > 3):
        html = generate_dashboard(columns, args.palette, args.title)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Dashboard generated: {args.output}")
        print(f"  Charts: {len(html.split('chart_')) - 1} visualizations")
        print(f"  Open in browser: file://{os.path.abspath(args.output)}")
        return

    # ─── Single Chart ───
    chart_type = args.type

    # Auto-select chart type and columns
    if chart_type == 'auto':
        chart_type, auto_x, auto_y = select_best_chart(columns)
        x_col = args.x or auto_x
        y_cols = [y.strip() for y in (args.y or ','.join(auto_y)).split(',') if y.strip()]
    else:
        x_col = args.x
        y_cols = [y.strip() for y in args.y.split(',')] if args.y else []

    # Auto-fill columns if not specified
    if not x_col:
        for h, c in columns.items():
            if c['type'] in ('date', 'categorical'):
                x_col = h
                break
    if not y_cols:
        for h, c in columns.items():
            if c['type'] in ('numeric', 'percentage') and h != x_col:
                y_cols.append(h)
        if not y_cols and columns:
            # Use second column
            keys = list(columns.keys())
            if len(keys) > 1:
                y_cols = [keys[1]]
            else:
                y_cols = [keys[0]]

    # Validate columns
    if x_col and x_col not in columns:
        print(f"Warning: Column '{x_col}' not found. Available: {list(columns.keys())}", file=sys.stderr)
        x_col = list(columns.keys())[0] if columns else None

    y_cols = [y for y in y_cols if y in columns]
    if not y_cols:
        print("Error: No valid Y-axis columns found.", file=sys.stderr)
        sys.exit(1)

    # Handle heatmap-grid
    if chart_type == 'heatmap-grid':
        num_cols_avail = [h for h, c in columns.items() if c['type'] in ('numeric', 'percentage')]
        cat_cols_avail = [h for h, c in columns.items() if c['type'] == 'categorical']
        if len(cat_cols_avail) >= 2 and num_cols_avail:
            hm = build_heatmap_grid(columns, cat_cols_avail[0], cat_cols_avail[1],
                                    num_cols_avail[0], args.palette, args.title)
            if hm:
                html = generate_single_chart_html({}, hm, args.title or 'Heatmap')
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"✓ Heatmap generated: {args.output}")
                return

    # Aggregate if needed
    x_col_info = columns.get(x_col, {})
    needs_agg = False
    if x_col and x_col_info.get('type') == 'categorical':
        # Check if there are duplicate x values
        x_vals = [v for v in x_col_info.get('values', []) if v != '']
        if len(x_vals) != len(set(x_vals)):
            needs_agg = True
        # Also aggregate if there are categorical columns we're not using
        cat_cols = [h for h, c in columns.items() if c['type'] == 'categorical' and h != x_col]
        if cat_cols:
            needs_agg = True

    if needs_agg and x_col:
        agg_labels = None
        agg_datasets = []
        for yc in y_cols:
            l, v = aggregate_data(columns, x_col, yc, args.aggregate or 'sum')
            if agg_labels is None:
                agg_labels = l
            agg_datasets.append({'label': yc, 'data': v, 'col_type': columns[yc]['type']})
        labels = agg_labels if agg_labels else []
        datasets = agg_datasets
    else:
        labels, datasets = prepare_chart_data(columns, x_col, y_cols, chart_type)

    # Build chart config
    options = {}
    if args.trend:
        options['trend'] = True
    if args.moving_average:
        options['moving_average'] = args.moving_average

    title = args.title or (f'{", ".join(y_cols)}' + (f' by {x_col}' if x_col else ''))

    config = build_single_chart_config(chart_type, labels, datasets, args.palette, title, options)

    # Generate HTML
    html = generate_single_chart_html(config, None, title)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Chart generated: {args.output}")
    print(f"  Type: {chart_type}")
    print(f"  X-axis: {x_col or 'auto'}")
    print(f"  Y-axis: {', '.join(y_cols)}")
    print(f"  Palette: {args.palette}")
    if args.trend:
        print(f"  Trend line: enabled")
    if args.moving_average:
        print(f"  Moving average: {args.moving_average}")
    print(f"  Open in browser: file://{os.path.abspath(args.output)}")


if __name__ == '__main__':
    main()
