#!/usr/bin/env python3
"""
generate_slides.py - 从 M1 JSON 数据动态生成 7 页 HTML 幻灯片
用法: python3 generate_slides.py --data m1_real.json --output ./gen_output/
更新：
  - 互动量万单位显示从 toFixed(2) 改为 toFixed(0)，所有数字取整不保留小数
  - 涉及 P2/P5/P6 三处 interData 的 .toFixed(2) → .toFixed(0)
  - 放大字号
  - P7/8 折线图改动
  - P4取整
  - 加入数据备注 0528
"""

import argparse
import base64
import json
import math
import os
import sys
from pathlib import Path
from datetime import datetime


# ──────────────────────────────────────────────
# 辅助函数
# ──────────────────────────────────────────────

def b64(path: str, mime: str) -> str:
    with open(path, 'rb') as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def parse_val(s: str) -> float:
    """'94.2K' -> 94200.0, '8.2M' -> 8200000.0"""
    s = s.strip()
    if s.endswith('K'):
        return float(s[:-1]) * 1000
    if s.endswith('M'):
        return float(s[:-1]) * 1_000_000
    return float(s)


#def yoy_prev(cur_str: str, pct_str: str) -> float:
   # """通过当前值和同比百分比反推去年同期值"""
    #cur = parse_val(cur_str)
    #rate = float(pct_str.strip('%')) / 100
    #if rate == -1:
       # return 0
    #return cur / (1 + rate)


def fmt_val(v: float) -> str:
    """94200 -> '94.2K', 8200000 -> '8.2M'"""
    if v >= 1e6:
        return f"{v/1e6:.1f}M"
    if v >= 1e3:
        return f"{v/1e3:.1f}K"
    return f"{v:.0f}"


def nice_max(data: list, n: int = 5) -> float:
    if not data or max(data) == 0:
        return 100
    mx = max(data) * 1.2
    mag = 10 ** (len(str(int(mx))) - 1)
    return math.ceil(mx / mag) * mag


def js_array(lst: list) -> str:
    return json.dumps(lst, ensure_ascii=False)


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


SCALE_JS = """
<script>
function scaleSlide(){var w=document.getElementById('scale-wrapper');if(!w)return;var s=Math.min(window.innerWidth/1280,window.innerHeight/720);w.style.transform='scale('+s+')';}
scaleSlide();window.addEventListener('resize',scaleSlide);
</script>
"""

# 圆形数字标注
CIRCLED = ['①', '②', '③', '④', '⑤', '⑥','⑦','⑧']


# ──────────────────────────────────────────────
# P1 - 封面
# ──────────────────────────────────────────────

def gen_p1(data: dict, assets: dict) -> str:
    meta = data['meta']
    main_event = meta['main_event']
    report_stage = meta['report_stage']
    main_time_range = meta['main_time_range']
    generated_at = meta['generated_at']

    # 从时间范围提取日期
    parts = main_time_range.split('~')
    start_dt = parts[0].strip()[:10]  # '2026-03-28'
    end_dt = parts[1].strip()[:10]    # '2026-04-18'
    start_fmt = start_dt.replace('-', '.')[2:]  # '26.03.28'
    end_fmt = end_dt.replace('-', '.')[2:]       # '26.04.18'
    # 报告月份
    report_month = generated_at[:7].replace('-', '年') + '月'  # '2026年04月'

    bg_b64 = assets['cover_bg']
    logo = assets['logo']
    font = assets['font']
    
    return f"""<!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <style>
        @font-face {{
            font-family: 'TencentW7';
            src: url('{font}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'TencentW7', 'Noto Sans SC', sans-serif;
        }}

        .slide-container {{
            /* width: 1280px; */
            width: 100%;
            height: 720px;
            margin: auto;
            position: relative;
            background-image: url('{bg_b64}');
            background-size: 100% 100%;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        /* 占位误删除 */
        .page-title {{
            position: absolute;
            left: 15.5%;
            top: 10px;
            font-size: 36px;
            font-weight: 600;
            color: #000000;
            z-index: 10;
        }}

        .content {{
            text-align: center;
            color: #000000;
            z-index: 10;
            width: 50%;
            height: 720px;
            margin: px auto;
            box-sizing: border-box;
        }}

        .logobox {{
            width: 360px;
            height: auto;
            margin: auto;
        }}

        .logo {{
            display: block;
            width: 100%;
            height: auto;
        }}


        .main-title {{
            font-size: 72px;
            font-weight: 900;
            margin-bottom: 30px;
            color: #000000;
        }}


        .subtitle {{
            font-size: 48px;
            font-weight: 500;
            margin-bottom: 60px;
            color: #000000;
        }}

        .info {{
            font-size: 24px;
            color: #000000;
            margin-bottom: 15px;
        }}
    </style>
    <title>{main_event} {report_stage}数据分析报告</title>
</head>

<body>
    <div class="slide-container">
        <h1 class="page-title"><!-- 占位误删除  --> </h1>
        <div class="content">
            <div class="logobox">
                <img class="logo" src="{logo}" alt="logo">
            </div>
            <h2 class="subtitle">
                {main_event} {report_stage}<br>数据分析报告
            </h2>
            <p class="info">{report_month}</p>
        </div>
    </div>
</body>
</html>
"""


# ──────────────────────────────────────────────
# P2 - 整体热度概览
# ──────────────────────────────────────────────

def gen_p2(data: dict, assets: dict) -> str:
    meta = data['meta']
    p2 = data['P2']

    main_event = meta['main_event']
    report_stage = meta['report_stage']
    playoff_start = meta['playoff_start']
    main_time_range = meta.get('main_time_range', '')
    yoy_time_range = meta.get('yoy_time_range', '')

    date_obj = datetime.strptime(playoff_start, "%Y-%m-%d")
    result = f"{date_obj.month}.{date_obj.day}"  # 输出 4.11
    print('gen_p2 result=',result)

    #page_title = p2['page_title']
    total_volume = p2['total_volume']
    total_interaction = p2['total_interaction']
    heat_index = p2['heat_index']
    yoy_volume = p2['yoy_volume']
    yoy_interaction = p2['yoy_interaction']
    yoy_heat = p2['yoy_heat_index']
    #yoy_vol_pct = round(((total_volume - yoy_volume)/yoy_volume)*100%)
    #yoy_inter_pct = round(((total_interaction - yoy_interaction)/yoy_interaction)*100%)

    #yoy_vol_pct = p2['yoy_volume_change']
    #yoy_inter_pct = p2['yoy_interaction_change']
    time_range_label = p2['time_range_label']
    #chart_title = p2['chart_title']
    summary = p2['summary']
    vol_data = p2['vol_data']
    inter_data = p2['inter_data']
    date_labels = p2['date_labels']

    index = date_labels.index(result)
    print('gen_p2 index=',index)

    peak_events = p2['peak_events']
    peak_events = sorted(peak_events,key=lambda e: e['idx'])

    # 反推去年同期值
    #yoy_volume = fmt_val(yoy_prev(total_volume, yoy_vol_pct))
    #yoy_interaction = fmt_val(yoy_prev(total_interaction, yoy_inter_pct))
    # 热度没有单独的yoy pct，显示"—"
    #yoy_heat = "—"

    # inter_data 在JS中转万
    inter_data_raw = js_array(inter_data)

    # Y轴最大值
    vol_max = nice_max(vol_data)
    inter_max_raw = max(inter_data)
    inter_max_wan = nice_max([v / 10000 for v in inter_data])
    vol_step = vol_max / 4
    inter_step = inter_max_wan / 4

    # 高点索引
    peak_indices = [e['idx'] for e in peak_events]
    print(f"  ✓ index.html (入口文件)",peak_indices)
    print(f"  peak_indices=",{js_array(peak_indices)})
    


    # 事件列表 HTML   <div class="event-item">①： 1月15日 Viper重回其比赛，JDG战胜TES</div>
    events_html = ''
    for i, e in enumerate(peak_events[:6]):
        num = CIRCLED[i]
        text = e.get('text', e.get('summary', ''))
        date_lbl = e.get('date_label', '')
        events_html += f''' <div class="event-item"><div class="event-number">{num}</div><div class="event-text">{date_lbl} {text}</div> </div>'''

    bg_b64 = assets['cover_bg']
    cover_bg_left = assets['cover_bg_left']
    music = assets['music']
    engage = assets['engage']
    heart = assets['heart']
    VCT_top = assets['VCT_top']
    logo = assets['logo']
    font= assets['font']

    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
  <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
   <style>
      @font-face {{
        font-family: "TencentW7";
        src: url("{font}") format("opentype");
        font-weight: normal;
        font-style: normal;
      }}

      body {{
        margin: 0;
        padding: 0;
        font-family: "TencentW7", "Noto Sans SC", sans-serif;
      }}

      .slide-container {{
        width: 100%;
        height: 720px;
        margin: auto;
        position: relative;
        background-image: url("{cover_bg_left}");
        background-size: 100% 100%;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
      }}

      .logo {{
        position: absolute;
        top: 20px;
        right: 20px;
        width: 113px;
        height: 113px;
        z-index: 0;
      }}

      .page-title {{
        position: absolute;
        left: 15.5%;
        top: 10px;
        font-size: 36px;
        font-weight: 600;
        color: #000000;
        z-index: 10;
      }}

      .content-wrapper {{
        width: 100%;
        height: 640px;
        position: relative;
        z-index: 5;
        padding: 50px 80px 30px 80px;
        box-sizing: border-box;
      }}

      .summary {{
        font-size: 16px;
        color: #333;
        line-height: 1.6;
        margin: 10px 0;
        font-weight: 500;
        padding-right: 140px;
      }}

      .highlight-red {{
        color: #c00000;
        font-weight: 700;
      }}

      .main-content {{
        display: grid;
        grid-template-columns: 280px 1fr;
        gap: 0 20px;
      }}

      .left-column {{
        display: flex;
        flex-direction: column;
      }}

      .data-cards {{
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 12px;
      }}

      .data-card {{
        background: #ffffff;
        border: 3px solid #c00000;
        border-radius: 8px;
        padding: 8px 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }}

      .card-data {{
        display: flex;
        gap: 10px;
        align-items: center;
        flex: 1;
      }}

      .data-group {{
        display: flex;
        flex-direction: column;
      }}

      .data-group-current {{
        min-width: 100px;
      }}

      .data-group-yoy {{
        min-width: 80px;
      }}

      .data-label {{
        font-size: 13px;
        color: #c00000;
        font-weight: 600;
        margin-bottom: 4px;
      }}

      .data-value-large {{
        font-size: 28px;
        font-weight: 900;
        color: #000000;
      }}

      .data-value-small {{
        font-size: 18px;
        font-weight: 700;
        color: #000;
        height: 42px;
        line-height: 42px;
        text-align: center;
      }}

      .card-icon {{
        font-size: 28px;
      }}

      .decoration-image {{
        width: 100%;
        height: 180px;
        border-radius: 8px;
        object-fit: cover;
      }}

      .right-column {{
        display: flex;
        flex-direction: column;
      }}

      .chart-title {{
        font-size: 14px;
        font-weight: 600;
        text-align: right;
        margin-bottom: 5px;
        color: #222;
        padding-right: 100px;
      }}

      .chart-container {{
        padding: 0 20px 10px;
        height: 300px;
      }}

      .chat-y-lable-box {{
        display: flex;
        justify-content: space-between;
        margin: 0 0 5px 300px;
        color: #000000;
        font-weight: 600;
        font-size: 13px;
        padding: 0 17px 0 30px;
      }}

      .chart-canvas {{
        border-bottom: 1px solid #ccc;
        background: #fffbf0;
        height: 300px;
        padding-bottom: 5px;
      }}

      .events-container {{
        padding: 0 20px 5px;
        height: 200px;
        position: relative;
      }}

      .events-grid {{
        background: #fffbf0;
        column-count: 2;
        column-gap: 30px;
        padding: 16px 42px;
        height: 100%;
        box-sizing: border-box;
        column-fill: auto;
        margin-top:5px;
      }}

      .event-item {{
        display: flex;
        align-items: flex-start;
        gap: 8px 16px;
        margin-bottom: 20px;
        break-inside: avoid;
      }}

      .event-number {{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #ffd700;
        color: #000000;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: 700;
        flex-shrink: 0;
      }}

      .event-text {{
        font-size: 13px;
        color: #000000;
        line-height: 1.4;
      }}

      .data-coverage {{
        position: absolute;
        left: 20px;
        bottom: 16px;
        font-size: 10px;
        color: #5b6d7e;
        white-space: nowrap;
      }}
    </style>
  <title>{report_stage}整体热度概览</title>
</head>

<body>
  <div class="slide-container">
    <img
      src="{logo}"
      alt="Logo" class="logo">
    <h1 class="page-title"><span style="margin-right: 20px;">{report_stage}</span>整体热度概览</h1>

    <div class="content-wrapper">
      <div class="summary">
        {summary}
      </div>
      <div class="chart-title">
        <span>2026 {main_event} {report_stage} 声量与互动量趋势（By day） </span>
        <span style="margin:0 20px;"><span style="margin:0 5px; color:#c00000;">——</span>声量</span>
        <span> <span style="margin:0 5px;color:#c00000;">- -</span>互动量</span>
      </div>
      <div class="chat-y-lable-box">
        <span class="y-left">声量</span>
        <span class="y-right">互动量（万）</span>
      </div>
      <div class="main-content">

        <div class="left-column">
          <div class="data-cards">
            <div class="data-card">
              <div class="card-data">
                <div class="data-group data-group-current">
                  <div class="data-label">总声量</div>
                  <div class="data-value-large">{total_volume}</div>
                </div>
                <div class="data-group data-group-yoy">
                  <div class="data-label">25s1常规赛声量</div>
                  <div class="data-value-small">{yoy_volume}</div>
                </div>
              </div>
              <div class="card-icon" style="color: #c00000;">
                <img style="width: 35px;height: auto;" src="{music}">
              </div>
            </div>

            <div class="data-card">
              <div class="card-data">
                <div class="data-group data-group-current">
                  <div class="data-label">总互动量</div>
                  <div class="data-value-large">{total_interaction}</div>
                </div>
                <div class="data-group data-group-yoy">
                  <div class="data-label">25s1常规赛互动</div>
                  <div class="data-value-small">{yoy_interaction}</div>
                </div>
              </div>
              <div class="card-icon" style="color: #c00000;">
                <img style="width: 35px;height: auto;" src="{engage}">
              </div>
            </div>

            <div class="data-card">
              <div class="card-data">
                <div class="data-group data-group-current">
                  <div class="data-label">热度指数</div>
                  <div class="data-value-large">{heat_index}</div>
                </div>
                <div class="data-group data-group-yoy">
                  <div class="data-label">25s1常规赛热度</div>
                  <div class="data-value-small">{yoy_heat}</div>
                </div>
              </div>
              <div class="card-icon" style="color: #c00000;">
                <img style="width: 35px;height: auto;" src="{heart}">
              </div>
            </div>
          </div>

          <img
            src="{VCT_top}"
            alt="装饰图" class="decoration-image">
        </div>

        <div class="right-column">
          <div class="chart-container">
            <div class="chart-canvas"><canvas id="trendChart"></canvas></div>
          </div>

          <div class="events-container">
            <div class="events-grid">
              {events_html}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="data-coverage">数据时间覆盖：{main_time_range}; 去年赛段：{yoy_time_range}</div>
  </div>

{SCALE_JS}
<script>
    const ctx = document.getElementById('trendChart').getContext('2d');
    
    //x轴
    const dateLabels = {js_array(date_labels)};
    
    //声量
    const volData = {js_array(vol_data)};

    //互动量
    const rawInterData = {inter_data_raw};
    const interData =  rawInterData.map(v => +(v/10000).toFixed(0));

    const peakIndices =  {js_array(peak_indices)};
    const volMax = {vol_max};
    const interMax = {inter_max_wan};

    const circledNumbers = ['①', '②', '③', '④', '⑤', '⑥'];

    const dividerIndices = [{index}];

    const phaseLabels = ["常规赛阶段", "淘汰赛阶段"];

    new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: dateLabels,
            datasets: [
                {{
                    label: '声量',
                    data: volData,
                    borderColor: '#c00000',
                    backgroundColor: 'rgba(192, 0, 0, 0.05)',
                    borderWidth: 2.5,
                    borderDash: [],
                    tension: 0.3,
                    pointRadius: 0,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: '#c00000',
                    yAxisID: 'y',
                    fill: true
                }},
                {{
                    label: '互动量',
                    data: interData,
                    borderColor: '#c00000',
                    backgroundColor: 'transparent',
                    borderWidth: 2.5,
                    borderDash: [6, 3],
                    tension: 0.3,
                    pointRadius: 0,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: '#c00000',
                    yAxisID: 'y1',
                    fill: false
                }}
            ]
        }},
        options: {{
            responsive: true,
            maintainAspectRatio: false,
            interaction: {{
                mode: 'index',
                intersect: false
            }},
            plugins: {{
                legend: {{
                    display: false
                }},
                tooltip: {{
                    enabled: true,
                    mode: 'index',
                    intersect: false
                }}
            }},
            scales: {{
                y: {{
                    type: 'linear',
                    position: 'left',
                    beginAtZero: true,
                    max: volMax,
                    grid: {{ color: 'rgba(0, 0, 0, 0.05)' }},
                    ticks: {{
                        font: {{ size: 11, family: 'TencentW7' }},
                        color: '#5b6d7e',
                        stepSize: volMax/4
                    }}
                }},
                y1: {{
                    type: 'linear',
                    position: 'right',
                    beginAtZero: true,
                    max: interMax,
                    grid: {{ display: false }},
                    ticks: {{
                        font: {{ size: 11, family: 'TencentW7' }},
                        color: '#5b6d7e',
                        stepSize: interMax/4
                    }}
                }},
                x: {{
                    grid: {{ display: false }},
                    ticks: {{
                        font: {{ size: 10, family: 'TencentW7' }},
                        color: '#5b6d7e',
                        maxRotation: 0,
                        minRotation: 0
                    }}
                }}
            }}
        }},
        plugins: [
            {{
                id: 'peakMarkers',
                afterDatasetsDraw: (chart) => {{
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(0);

                    peakIndices.forEach((idx, i) => {{
                        const point = meta.data[idx];
                        if (point) {{
                            ctx.save();
                            ctx.font = 'bold 18px TencentW7';
                            ctx.fillStyle = '#ffd700';
                            ctx.textAlign = 'center';
                            ctx.textBaseline = 'bottom';
                            ctx.fillText(circledNumbers[i], point.x, point.y - 8);
                            ctx.restore();
                        }}
                    }});
                }}
            }},
            {{
                id: 'phaseDividers',
                afterDatasetsDraw: (chart) => {{
                    const ctx = chart.ctx;
                    const chartArea = chart.chartArea;
                    const meta = chart.getDatasetMeta(0);

                    dividerIndices.forEach(idx => {{
                        const point = meta.data[idx];
                        if (point) {{
                            ctx.save();
                            ctx.beginPath();
                            ctx.moveTo(point.x, chartArea.top);
                            ctx.lineTo(point.x, chartArea.bottom);
                            ctx.strokeStyle = '#888888';
                            ctx.lineWidth = 1;
                            ctx.setLineDash([4, 4]);
                            ctx.stroke();
                            ctx.restore();
                        }}
                    }});

                    const lineX = meta.data[dividerIndices[0]].x;
                    const phase1Center = (chartArea.left + lineX) / 2;
                    const phase2Center = (lineX + chartArea.right) / 2;                  
                }}
            }}
        ]
    }}); 
</script>
</body>
</html>"""


# ──────────────────────────────────────────────
# P3 - 整体热度分析
# ──────────────────────────────────────────────

def gen_p3(data: dict, assets: dict) -> str:
    meta = data['meta']

    report_stage = meta['report_stage']
    
    p2 = data['P2']
    p3 = data['P3']

    #page_title = p3['page_title']
    #charts_header_title = p3['charts_header_title']
    summary = p3['summary']

    #yoy_vol_pct = round(((p2['total_volume'] - p2['yoy_volume'])/p2['yoy_volume'])*100%)
    #yoy_inter_pct = round(((p2['total_interaction'] - p2['yoy_interaction'])/p2['yoy_interaction'])*100%)
    #yoy_heat_pct = round(((p2['heat_index'] - p2['yoy_heat_index'])/p2['yoy_heat_index'])*100%)
    
    
    yoy_vol_pct = p3['yoy_volume_change']
    yoy_inter_pct = p3['yoy_interaction_change']
    yoy_heat_pct = p3['yoy_heat_change']

    # 反推2025年数值（柱状图用）
    vol_2026 = parse_val(p2['total_volume'])
    inter_2026 = parse_val(p2['total_interaction'])
    heat_2026 = parse_val(p2['heat_index'])

    vol_2025 = parse_val(p2['yoy_volume'])
    inter_2025 = parse_val(p2['yoy_interaction'])
    heat_2025 = parse_val(p2['yoy_heat_index'])

    # 单位
    def bar_unit_val(v):
        if v >= 1e6:
            return v / 1e6, 'M'
        return v / 1e3, 'K'

    vol_2025_disp, vol_unit = bar_unit_val(max(vol_2025, vol_2026))
    vol_2025_v = vol_2025 / (1e6 if vol_unit == 'M' else 1e3)
    vol_2026_v = vol_2026 / (1e6 if vol_unit == 'M' else 1e3)

    inter_2025_disp, inter_unit = bar_unit_val(max(inter_2025, inter_2026))
    inter_2025_v = inter_2025 / (1e6 if inter_unit == 'M' else 1e3)
    inter_2026_v = inter_2026 / (1e6 if inter_unit == 'M' else 1e3)

    heat_2025_disp, heat_unit = bar_unit_val(max(heat_2025, heat_2026))
    heat_2025_v = heat_2025 / (1e6 if heat_unit == 'M' else 1e3)
    heat_2026_v = heat_2026 / (1e6 if heat_unit == 'M' else 1e3)

    yoy_vol_float = float(yoy_vol_pct.strip('%'))
    yoy_inter_float = float(yoy_inter_pct.strip('%'))
    yoy_heat_float = float(yoy_heat_pct.strip('%'))

    # 平台分布数据
    plat_dist = p3['platform_dist']
    plat_labels = ['微博', '抖音', 'B站', '小红书', '其他']
    vol_vals = [plat_dist['volume'].get(k, 0) for k in plat_labels]
    inter_vals = [plat_dist['interaction'].get(k, 0) for k in plat_labels]
    heat_vals = [plat_dist['heat'].get(k, 0) for k in plat_labels]

    cover_bg_left = assets['cover_bg_left']
    logo = assets['logo']
    font= assets['font']

    return f"""
    <!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
    <style>
        @font-face {{
            font-family: 'TencentW7';
            src: url('{font}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'TencentW7', 'Noto Sans SC', sans-serif;
        }}

        .slide-container {{
            width: 100%;
            height: 720px;
            margin: auto;
            position: relative;
            background-image: url('{cover_bg_left}');
            background-size: 100% 100%;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        .logo {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 113px;
            height: 113px;
            z-index: 0;
        }}

        .page-title {{
            position: absolute;
            left: 15.5%;
            top: 10px;
            font-size: 36px;
            font-weight: 600;
            color: #000000;
            z-index: 10;
        }}

        .content-wrapper {{
            width: 100%;
            height: 640px;
            position: relative;
            z-index: 5;
            padding: 50px 80px 30px 80px;
            box-sizing: border-box;
        }}

        .summary {{
            font-size: 16px;
            color: #333;
            line-height: 1.6;
            margin: 10px 0;
            font-weight: 500;
            padding-right: 140px;
        }}

        .highlight-red {{
            color: #c00000;
            font-weight: 700;
        }}

        .chat-content {{
            width: 100%;
            height: auto;
            border: 1px solid #0071bc;
        }}

        .chart-canvas {{
            width: 90%;
            height: auto;
            margin: 0 auto;
        }}

        .charts-header {{
            background-color: #0071bc;
            color: white;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            padding: 8px 0;
            margin-bottom: 10px;
            position: relative;
        }}

        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding-bottom: 5px;
            margin-bottom: 5px;
            position: relative;
        }}

        .charts-grid-frist {{
            left: -34px
        }}

        .chat-divider-line {{
            position: absolute;
            left: calc(-5% + 34px);
            bottom: 0;
            border-bottom: 1px dashed #0071bc;
            width: calc(110% + 2px);
        }}

        .chart-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .chart-title {{
            font-size: 14px;
            font-weight: 500;
            text-align: center;
            margin-top: 8px;
            color: #000000;
        }}

        .bar-container {{
            height: 200px;
            width: 40%;
        }}

        .doughnut-container {{
            height: 200px;
            width: 280px;
        }}

        .section-title {{
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            margin: 5px 0;
        }}

        .legend-small {{
            display: flex;
            gap: 15px;
            position: absolute;
            top: 40px;
            right: 85px;
            font-size: 14px;
            color: #333;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .legend-color {{
            width: 18px;
            height: 12px;
            display: inline-block;
        }}
    </style>
    <title>Stage1 社媒热度分析</title>
</head>

<body>
    <div class="slide-container">
        <img src="{logo}"
            alt="Logo" class="logo">
        <h1 class="page-title"><span style="margin-right: 20px;">{report_stage}</span>社媒热度分析</h1>

        <div class="content-wrapper">
            <div class="summary">
                {summary}
            </div>

            <div class="chat-content">
                <div class="charts-header">
                    <div>
                        <span style="margin-right: 10px;">{report_stage}</span>社媒热度整体同比
                    </div>

                    <div class="legend-small">
                        <div class="legend-item" style="margin-right: 15px;">
                            <span class="legend-color" style="background-color: #0071bc;"></span>
                            <span>2025 {report_stage}</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-color" style="background-color: #001f60;"></span>
                            <span>2026 {report_stage}</span>
                        </div>
                    </div>
                </div>

                <div class="chart-canvas">
                      <div class="charts-grid charts-grid-frist">
                        <div class="chart-item">
                            <div class="bar-container"><canvas id="volumeBar"></canvas></div>
                            <div class="chart-title">总声量</div>
                        </div>
                        <div class="chart-item">
                            <div class="bar-container"><canvas id="interactionBar"></canvas></div>
                            <div class="chart-title">总互动量</div>
                        </div>
                        <div class="chart-item">
                            <div class="bar-container"><canvas id="heatBar"></canvas></div>
                            <div class="chart-title">总热度</div>
                        </div>
                        <div class="chat-divider-line"></div>
                    </div>

                    <div class="section-title">渠道社媒数据分布</div>
                    <div class="charts-grid" style="border-bottom: none;">
                        <div class="chart-item">
                            <div class="doughnut-container"><canvas id="volumeDoughnut"></canvas></div>
                        </div>
                        <div class="chart-item">
                            <div class="doughnut-container"><canvas id="interactionDoughnut"></canvas></div>
                        </div>
                        <div class="chart-item">
                            <div class="doughnut-container"><canvas id="heatDoughnut"></canvas></div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        Chart.register(ChartDataLabels);

        const platformColors = {{
            '微博': '#c00000',
            '抖音': '#00bfff',
            'B站': '#7cb342',
            '小红书': '#ff8888',
            '其他': '#cccccc'
        }};

        function createBarChart(canvasId, value2025, value2026, yoyChange, unit) {{
            const ctx = document.getElementById(canvasId).getContext('2d');
            const changeColor = yoyChange >= 0 ? '#c00000' : '#00b050';
            const sign = yoyChange >= 0 ? '+' : '';

            const maxValue = Math.max(value2025, value2026);
            const yAxisMax = maxValue * 1.2;

            new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: [''],
                    datasets: [
                        {{
                            label: '2025',
                            data: [value2025],
                            backgroundColor: '#0071bc',
                            borderWidth: 0,
                            barPercentage: 1,
                            categoryPercentage: 1,
                        }},
                        {{
                            label: '2026',
                            data: [value2026],
                            backgroundColor: '#001f60',
                            borderWidth: 0,
                            barPercentage: 1,
                            categoryPercentage: 1,
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    layout: {{ padding: {{ top: 60 }} }},
                    plugins: {{
                        legend: {{ display: false }},
                        datalabels: {{ display: false }}
                    }},
                    scales: {{
                        y: {{
                            display: false,
                            beginAtZero: true,
                            max: yAxisMax
                        }},
                        x: {{ display: false }}
                    }},
                }},
                plugins: [{{
                    id: 'customLabels',
                    afterDatasetsDraw: (chart) => {{
                        const ctx = chart.ctx;
                        const meta2025 = chart.getDatasetMeta(0).data[0];
                        const meta2026 = chart.getDatasetMeta(1).data[0];

                        ctx.save();
                        ctx.font = 'bold 13px TencentW7';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'bottom';


                        ctx.fillStyle = '#000000';
                        ctx.fillText(value2025 + unit, meta2025.x, meta2025.y - 5);

                        const valueText = value2026 + unit;
                        ctx.fillStyle = '#000000';
                        ctx.fillText(valueText, meta2026.x, meta2026.y - 5);


                        const percentText = sign + yoyChange + '%';
                        const centerX = (meta2025.x + meta2026.x) / 2;
                        const topY = Math.min(meta2025.y, meta2026.y);
                        ctx.fillStyle = changeColor;
                        ctx.fillText(percentText, centerX, topY - 25);

                        ctx.restore();
                    }}
                }}]
            }});
        }}

        
        //中间位置，饼状图：总声量
        createBarChart('volumeBar', {vol_2025_v:.2f}, {vol_2026_v:.2f}, {yoy_vol_float:.1f}, '{vol_unit}');
        
        //中间位置，饼状图：总互动量
        createBarChart('interactionBar', {inter_2025_v:.2f}, {inter_2026_v:.2f}, {yoy_inter_float:.1f}, '{inter_unit}');
        
        //中间位置，饼状图：总热度
        createBarChart('heatBar', {heat_2025_v:.2f}, {heat_2026_v:.2f}, {yoy_heat_float:.1f}, '{heat_unit}');

        const volumeData = {js_array(vol_vals)};
        const interactionData = {js_array(inter_vals)};
        const heatData = {js_array(heat_vals)};

        const labels = ['微博', '抖音', 'B站', '小红书', '其他'];
        const colors = labels.map(l => platformColors[l]);


        function createDoughnutChart(canvasId, data, centerText) {{
            new Chart(document.getElementById(canvasId), {{
                type: 'doughnut',
                data: {{
                    labels: labels,
                    datasets: [{{
                        data: data,
                        backgroundColor: colors,
                        borderWidth: 2,
                        borderColor: '#fff'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '60%',
                    plugins: {{
                        legend: {{
                            display: true,
                            position: 'right',
                            labels: {{
                                font: {{ size: 12, family: 'TencentW7' }},
                                color: '#000000',
                                padding: 8,
                                boxWidth: 12
                            }}
                        }},
                        datalabels: {{
                            color: '#000',
                            font: {{size: 12, weight: 'bold', family: 'TencentW7' }},
                            formatter: (value) => value >= 1 ? Math.round(value) + '%' : ''
                        }}
                    }}
                }},
                plugins: [{{
                    id: 'centerText',
                    afterDraw: (chart) => {{
                        const ctx = chart.ctx;
                        const centerX = chart.chartArea.left + (chart.chartArea.right - chart.chartArea.left) / 2;
                        const centerY = chart.chartArea.top + (chart.chartArea.bottom - chart.chartArea.top) / 2;

                        ctx.save();
                        ctx.font = 'bold 14px TencentW7';
                        ctx.fillStyle = '#000000';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillText(centerText, centerX, centerY);
                        ctx.restore();
                    }}
                }}]
            }});
        }}

        // 分别创建三个环形图，中间文字对应设置
        createDoughnutChart('volumeDoughnut', volumeData, '声量');
        createDoughnutChart('interactionDoughnut', interactionData, '互动量');
        createDoughnutChart('heatDoughnut', heatData, '热度值');
    </script>
</body>

</html>

    """


# ──────────────────────────────────────────────
# P4 - 重点平台表现
# ──────────────────────────────────────────────

def gen_p4(data: dict, assets: dict) -> str:
    p4 = data['P4']
    meta = data['meta']
    report_stage = meta['report_stage']


    #page_title = p4['page_title']
    #charts_header_title = p4['charts_header_title']
    summary = p4['summary']
    channel_growth = p4['channel_growth']
    channel_heat = p4['channel_heat']

    cover_bg_left = assets['cover_bg_left']
    logo = assets['logo']
    font= assets['font']
    weibo_icon = assets['weibo_icon']
    douyin_icon = assets['douyin_icon']
    bilibili_icon = assets['bilibili_icon']
    xiaohongshu_icon = assets['xiaohongshu_icon']
  

    # 构建 channel 映射
    growth_map = {item['channel']: item['growth_rate'] for item in channel_growth}
    heat_map = {item['channel']: (item['heat_now'], item['heat_yoy']) for item in channel_heat}

    channels = [
        {'name': '微博', 'icon': weibo_icon, 'canvas': 'weiboChart'},
        {'name': '抖音', 'icon': douyin_icon, 'canvas': 'douyinChart'},
        {'name': 'B站',  'icon': bilibili_icon, 'canvas': 'bilibiliChart'},
        {'name': '小红书', 'icon': xiaohongshu_icon, 'canvas': 'xiaohongshuChart'},
    ]

    channels_html = ''
    chart_calls = ''
    for ch in channels:
        name = ch['name']
        gr = growth_map.get(name, 0)
        heat_now, heat_yoy = heat_map.get(name, (0, 0))
        gr_class = 'growth-positive' if gr >= 0 else 'growth-negative'
        gr_sign = '+' if gr >= 0 else ''
        channels_html += f'''
                <div class="channel-item">
                    <div class="channel-header">
                        <div class="channel-name">
                            <img src="{ch["icon"]}" alt="{name}" class="channel-icon">
                            <span>{name}</span>
                        </div>
                        <div class="channel-growth {gr_class}">{gr_sign}{gr:.0f}%</div>
                    </div>
                    <div class="chart-wrapper"><canvas id="{ch["canvas"]}"></canvas></div>
                    <div class="chat-name">{name}</div>
                </div>'''

        # JS：热度单位自动换算为K
        chart_calls += f"""    createChannelChart('{ch["canvas"]}', {heat_yoy:.0f}, {heat_now:.0f});\n"""

    return f"""
    <!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <style>
        @font-face {{
            font-family: 'TencentW7';
            src: url('{font}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'TencentW7', 'Noto Sans SC', sans-serif;
        }}

        .slide-container {{
            width: 100%;
            height: 720px;
            margin: auto;
            position: relative;
            background-image: url('{cover_bg_left}');
            background-size: 100% 100%;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        .logo {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 113px;
            height: 113px;
            z-index: 0;
        }}

        .page-title {{
            position: absolute;
            left: 15.5%;
            top: 10px;
            font-size: 36px;
            font-weight: 600;
            color: #000000;
            z-index: 10;

        }}

        .content-wrapper {{
            width: 100%;
            height: 640px;
            position: relative;
            z-index: 5;
            padding: 50px 80px 30px 80px;
            box-sizing: border-box;
        }}

        .summary {{
            font-size: 16px;
            color: #333;
            line-height: 1.6;
            margin-top: 30px;
            margin-bottom: 32px;
            font-weight: 500;
            padding-right: 140px;
        }}

        .highlight-red {{
            color: #c00000;
            font-weight: 700;
        }}

        .chat-content {{
            width: 100%;
            height: auto;
            border: 1px solid #0071bc;
        }}



        .charts-header {{
            background-color: #0071bc;
            color: white;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            padding: 8px 0;
            margin-bottom: 10px;
            position: relative;
        }}

        .legend-small {{
            display: flex;
            gap: 15px;
            position: absolute;
            top: 43px;
            right: 85px;
            font-size: 14px;
            color: #333;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .legend-color {{
            width: 18px;
            height: 12px;
            display: inline-block;
        }}


        .chart-canvas {{
            height: 375px;
            margin: 35px auto;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            padding: 0 20px;
            box-sizing: border-box;
        }}

        .channel-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .channel-header {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 12px;
        }}

        .channel-icon {{
            width: 60px;
            height: 60px;
            margin-bottom: 8px;
        }}

        .channel-name {{
            font-size: 18px;
            font-weight: 700;
            color: #000000;
            margin-bottom: 6px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 20px;
        }}

        .channel-growth {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 8px;
        }}

        .growth-positive {{
            color: #c00000;
        }}

        .growth-negative {{
            color: #00b050;
        }}

        .chart-wrapper {{
            width: 50%;
            height: 280px;
        }}

        .chat-name {{
            margin-top: -20px;
            color: #333;
            font-size: 15px;
        }}
    </style>
    <title>{report_stage} 社媒热度分渠道同比</title>
</head>

<body>
    <div class="slide-container">
        <img src="{logo}"
            alt="Logo" class="logo">
        <h1 class="page-title"><span style="margin-right: 20px;">{report_stage}</span>社媒热度分渠道同比</h1>

        <div class="content-wrapper">
            <div class="summary">
                {summary}
            </div>
            <div class="chat-content">
                <div class="charts-header">{report_stage} 社媒热度分渠道同比
                    <div class="legend-small">
                        <div class="legend-item">
                            <span class="legend-color" style="background-color: #0071bc;"></span>
                            <span>2025 {report_stage}</span>
                        </div>
                        <div class="legend-item">
                            <span class="legend-color" style="background-color: #001f60;"></span>
                            <span>2026 {report_stage}</span>
                        </div>
                    </div>
                </div>
                <div class="chart-canvas">
                   {channels_html}
                </div>
            </div>
        </div>
    </div>


    <script>
        function createChannelChart(canvasId, heat2025, heat2026) {{
            const ctx = document.getElementById(canvasId).getContext('2d');
            const maxValue = Math.max(heat2025, heat2026);
            const yAxisMax = maxValue * 1.1;

            new Chart(ctx, {{
                type: 'bar',
                data: {{
                    labels: [''],
                    datasets: [
                        {{
                            label: '2025',
                            data: [heat2025],
                            backgroundColor: '#0071bc',
                            borderWidth: 0,
                            barPercentage: 1,
                            categoryPercentage: 1,
                        }},
                        {{
                            label: '2026',
                            data: [heat2026],
                            backgroundColor: '#001f60',
                            borderWidth: 0,
                            barPercentage: 1,
                            categoryPercentage: 1,
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    layout: {{ padding: {{ top: 10 }} }},
                    plugins: {{
                        legend: {{ display: false }},
                        datalabels: {{ display: false }}
                    }},
                    scales: {{
                        y: {{
                            display: false,
                            beginAtZero: true,
                            max: yAxisMax 
                        }},
                        x: {{
                            grid: {{ display: false }},
                            ticks: {{ font: {{ size: 12, family: 'TencentW7', weight: '700' }}, color: '#000000' }}
                        }}
                    }}
                }},
                plugins: [{{
                    id: 'customLabels',
                    afterDatasetsDraw: (chart) => {{
                        const ctx = chart.ctx;
                        chart.data.datasets.forEach((dataset, datasetIndex) => {{
                            const meta = chart.getDatasetMeta(datasetIndex);
                            meta.data.forEach((bar, index) => {{
                                const value = dataset.data[index];
                                ctx.save();
                                ctx.font = 'bold 13px TencentW7';
                                ctx.textAlign = 'center';
                                ctx.textBaseline = 'bottom';
                                ctx.fillStyle = '#000000';
                                ctx.fillText((value / 1000).toFixed(0) + 'K', bar.x, bar.y - 5);
                                ctx.restore();
                            }});
                        }});
                    }}
                }}]
            }});
        }}

        //页面下方柱形图，微博，抖音，B站，小红书 
    {chart_calls}
    </script>
</body>

</html>
    """



# ──────────────────────────────────────────────
# P5 - 抖音平台热度分析
# ──────────────────────────────────────────────

def gen_p5(data: dict, assets: dict) -> str:
    p5 = data['P5']
    
    meta = data['meta']
    main_event = meta['main_event']
    report_stage = meta['report_stage']

    dy_total_volume = p5['dy_total_volume']
    dy_total_interaction = p5['dy_total_interaction']
    dy_heat_index = p5['dy_heat_index']
    dy_yoy_volume = p5['dy_yoy_volume']
    dy_yoy_interaction = p5['dy_yoy_interaction']
    dy_yoy_heat_index = p5['dy_yoy_heat_index']
    summary = p5['summary']
    #chart_title = p5['chart_title']
    #page_title = p5['page_title']
    
    dy_vol_data = p5['dy_vol_data']
    dy_inter_data = p5['dy_inter_data']
    dy_date_labels = p5['dy_date_labels']
    dy_peak_events = p5['dy_peak_events']
    dy_peak_events  = sorted(dy_peak_events,  key=lambda e: e['idx'])

    vol_max = nice_max(dy_vol_data)
    inter_max_wan = nice_max([v / 10000 for v in dy_inter_data])

    cover_bg_left = assets['cover_bg_left']
    music = assets['music']
    engage = assets['engage']
    heart = assets['heart']
    VCT_top = assets['VCT_top']
    logo = assets['logo']
    font =assets['font']
    

    weibo_icon = assets['weibo_icon']
    douyin_icon = assets['douyin_icon']
    bilibili_icon = assets['bilibili_icon']
    xiaohongshu_icon = assets['xiaohongshu_icon']
    
    # 构建标注列表
    annotations = []
    for i, item in enumerate(dy_peak_events[:6]):  # 最多取6条
      num = CIRCLED[i]
      idx = item["idx"]
      date_label = item["date_label"]
      text = item["text"]

      annotations.append({
          "idx": idx,
          "text": [f"{num}{date_label}", text],
          "fullText": f"{num}{date_label} {text}"
      })

    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <style>
      @font-face {{
        font-family: "TencentW7";
        src: url("{font}") format("opentype");
        font-weight: normal;
        font-style: normal;
      }}

      body {{
        margin: 0;
        padding: 0;
        font-family: "TencentW7", "Noto Sans SC", sans-serif;
      }}

      .slide-container {{
        width: 100%;
        height: 720px;
        margin: auto;
        position: relative;
        background-image: url("{cover_bg_left}");
        background-size: 100% 100%;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
      }}

      .logo {{
        position: absolute;
        top: 20px;
        right: 20px;
        width: 113px;
        height: 113px;
        z-index: 0;
      }}

      .page-title {{
        position: absolute;
        left: 15.5%;
        top: 10px;
        font-size: 36px;
        font-weight: 600;
        color: #000000;
        z-index: 10;
      }}

      .content-wrapper {{
        width: 100%;
        height: 640px;
        position: relative;
        z-index: 5;
        padding: 50px 80px 30px 80px;
        box-sizing: border-box;
        display: flex;
        gap: 30px;
      }}

      .left-panel {{
        width: 320px;
        display: flex;
        flex-direction: column;
      }}

      .panel-header {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 5px;
      }}

      .douyin-logo {{
        width: 50px;
        height: 50px;
      }}

      .panel-title {{
        font-size: 24px;
        font-weight: 700;
        color: #000000;
      }}

      .divider {{
        height: 6px;
        background: #000000;
        width: 235px;
        margin-bottom: 30px;
      }}

      .data-cards {{
        display: flex;
        flex-direction: column;
        gap: 16px;
        margin-bottom: 20px;
      }}

      .data-card {{
        background: #ffffff;
        border: 3px solid #c00000;
        border-radius: 8px;
        padding: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }}

      .card-data {{
        display: flex;
        gap: 20px;
        align-items: center;
        flex: 1;
      }}

      .data-group {{
        display: flex;
        flex-direction: column;
      }}

      .data-group-current {{
        min-width: 100px;
      }}

      .data-group-yoy {{
        min-width: 80px;
      }}

      .data-label {{
        font-size: 13px;
        color: #c00000;
        font-weight: 600;
        margin-bottom: 4px;
      }}

      .data-value-large {{
        font-size: 28px;
        font-weight: 900;
        color: #000000;
      }}

      .data-value-small {{
        font-size: 18px;
        font-weight: 700;
        color: #000;
        height: 42px;
        line-height: 42px;
        text-align: center;
      }}

      .card-icon {{
        font-size: 32px;
      }}

      .summary-box {{
        background: #f5f5f5;
        border-radius: 8px;
        padding: 16px;
        font-size: 14px;
        color: #000000;
        line-height: 1.6;
        margin: auto;
      }}

      .right-panel {{
        flex: 1;
        display: flex;
        flex-direction: column;
      }}

      .chart-title {{
        font-size: 16px;
        color: #3e3e3e;
        font-weight: 900;
        margin-bottom: 16px;
        text-align: center;
      }}

      .chart-wrapper {{
        width: 100%;
        height: 475px;
        position: relative;
      }}

      .hover-tooltip {{
        position: absolute;
        background: rgba(255, 255, 255, 0.98);
        border: 2px solid #999999;
        border-radius: 6px;
        padding: 10px 12px;
        font-size: 13px;
        color: #000000;
        pointer-events: none;
        display: none;
        z-index: 2000;
        max-width: 200px;
        line-height: 1.4;
      }}

      .chat-title-mark {{
        margin: 10px 50px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
      }}

      .mark-dispaly {{
        width: 135px;
        display: flex;
        align-items: center;
      }}

      .mark-dis-y {{
        display: inline-block;
        width: 30px;
        height: 10px;
        background: #7f7f7f;
        margin-right: 10px;
      }}

      .mark-dis-r {{
        display: inline-block;
        width: 30px;
        height: 6px;
        background: #595959;
        margin-right: 10px;
      }}

      .chat-y-lable-box {{
        width: 100%;
        box-sizing: border-box;
        color: #000000;
        font-weight: 800;
        font-size: 13px;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        align-items: center;
        padding: 0 10px;
      }}
    </style>
    <title>抖音舆情数据表现-核心平台</title>
</head>

<body>
    <div class="slide-container">
        <img src="{logo}"
            alt="Logo" class="logo">
        <h1 class="page-title">抖音舆情数据表现-核心平台</h1>

        <div class="content-wrapper">
            <div class="left-panel">
                <div class="panel-header">
                    <img src="{douyin_icon}"
                        alt="抖音" class="douyin-logo">
                    <div class="panel-title">数据概览</div>
                </div>
                <div class="divider"></div>

                <div class="data-cards">
                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">总声量</div>
                                <div class="data-value-large">{dy_total_volume}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛声量</div>
                                <div class="data-value-small">{dy_yoy_volume}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{music}"
                                alt="icon">
                        </div>
                    </div>

                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">总互动量</div>
                                <div class="data-value-large">{dy_total_interaction}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛互动</div>
                                <div class="data-value-small">{dy_yoy_interaction}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{engage}"
                                alt="icon">
                        </div>
                    </div>

                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">热度指数</div>
                                <div class="data-value-large">{dy_heat_index}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛热度</div>
                                <div class="data-value-small">{dy_yoy_heat_index}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{heart}"
                                alt="icon">
                        </div>
                    </div>
                </div>

                <div class="summary-box">
                    {summary}
                </div>
            </div>

            <div class="right-panel">
                <div class="chart-title">2026 {main_event} {report_stage} 声量与互动量趋势（By day）- 抖音</div>
                <div class="chat-title-mark">
                    <div class="mark-dispaly">
                        <span class="mark-dis-y"></span>
                        <span>总声量</span>
                    </div>
                    <div class="mark-dispaly">
                        <span class="mark-dis-r"></span>
                        <span>总互动量</span>
                    </div>
                </div>
                <div class="chart-wrapper" id="chartWrapper">
                    <div class="chat-y-lable-box">
                        <div class="y-left" style="text-align: left;">声量</div>
                        <div class="y-right" style="text-align: right;">互动量（万）</div>
                    </div>
                    <canvas id="trendChart"></canvas>
                    <div id="hoverTooltip" class="hover-tooltip"></div>
                </div>
            </div>
        </div>
    </div>


    <script>
        const canvas = document.getElementById('trendChart');
        const ctx = canvas.getContext('2d');
        const hoverTooltip = document.getElementById('hoverTooltip');

        const dateLabels = {js_array(dy_date_labels)};
        const volData = {js_array(dy_vol_data)};
        const rawInterData = {js_array(dy_inter_data)};
        const interData = rawInterData.map(v => +(v/10000).toFixed(0));

        const volMax = {vol_max};
        const interMax = {inter_max_wan};

        const annotations = {json.dumps(annotations, ensure_ascii=False)};
        let annotationBoxes = [];

        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: dateLabels,
                datasets: [
                    {{
                        label: '声量',
                        data: volData,
                        borderColor: '#7f7f7f',
                        backgroundColor: '#7f7f7f',
                        borderWidth: 1,
                        borderDash: [],
                        tension: 0.3,
                        pointRadius: 0,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: '#7f7f7f',
                        yAxisID: 'y',
                        fill: true,
                        order: 2
                    }},
                    {{
                        label: '互动量',
                        data: interData,
                        borderColor: '#595959;',
                        backgroundColor: 'transparent',
                        borderWidth: 2,
                        borderDash: [6, 3],
                        tension: 0.3,
                        pointRadius: 0,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: '#595959;',
                        yAxisID: 'y1',
                        fill: false,
                        order: 1
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                interaction: {{ mode: 'index', intersect: false }},
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        enabled: true,
                        mode: 'index',
                        intersect: false,
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleFont: {{ size: 13, family: 'TencentW7', weight: 'bold' }},
                        bodyFont: {{ size: 12, family: 'TencentW7', weight: 'bold' }},
                        callbacks: {{
                            title: function (context) {{ return '日期: ' + context[0].label; }},
                            label: function (context) {{
                                let label = context.dataset.label + ': ';
                                if (context.datasetIndex === 0) {{
                                    label += Math.round(context.parsed.y);
                                }} else {{
                                    label += Math.round(context.parsed.y) + '万';
                                }}
                                return label;
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        type: 'linear',
                        position: 'left',
                        beginAtZero: true,
                        max: volMax,
                        grid: {{ color: 'rgba(0, 0, 0, 0.05)' }},
                        ticks: {{
                            font: {{ size: 11, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            stepSize:volMax/4
                        }}
                    }},
                    y1: {{
                        type: 'linear',
                        position: 'right',
                        beginAtZero: true,
                        max: interMax,
                        grid: {{ display: false }},
                        ticks: {{
                            font: {{ size: 11, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            stepSize:interMax/4,
                            callback: function (value) {{
                                return value + '万';
                            }}
                        }}
                    }},
                    x: {{
                        grid: {{ display: false }},
                        ticks: {{
                            font: {{ size: 10, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            maxRotation: 0,
                            minRotation: 0
                        }}
                    }}
                }}
            }},
            plugins: [{{
                id: 'peakAnnotations',
                afterDatasetsDraw: (chart) => {{
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(0);
                    const meta2 = chart.getDatasetMeta(1);
                    const chartArea = chart.chartArea;
                    annotationBoxes = [];

                    // 1. 在循环外定义常量
                    const boxW = 140;
                    const boxH = 35;
                    const usedAreas = [];

                    const MIN_SAFE_X = 180; // 硬性安全线：确保弹窗左侧不进入灰色区
                    
                    annotations.forEach(anno => {{
                        const point = meta.data[anno.idx];
                        if (point) {{
                            // 1. 初始化变量：初始就卡死在 MIN_SAFE_X 之后
                            let boxX = Math.max(point.x + 10, MIN_SAFE_X);
                            let boxY = point.y - 45;

                            let attempts = 0;
                            let hasCollision = true;

                            // 2. 避让逻辑：全程只操作 boxX 和 boxY
                            while (hasCollision && attempts < 15) {{
                              // 检查是否撞到了已经画好的其他弹窗
                              const hitOtherBox = usedAreas.some((area) => {{
                                return (
                                  boxX < area.x + area.w + 8 &&
                                  boxX + boxW > area.x - 8 &&
                                  boxY < area.y + area.h + 8 &&
                                  boxY + boxH > area.y - 8
                                );
                              }});

                              // 【核心优化】：检查当前弹窗是否压住了它自己的数据点
                              // 定义一个“点保护区”，即点周围 15px 的范围
                              const pointProtectionZone = 15;
                              const hitSelfPoint =
                                boxX < point.x + pointProtectionZone &&
                                boxX + boxW > point.x - pointProtectionZone &&
                                boxY < point.y + pointProtectionZone &&
                                boxY + boxH > point.y - pointProtectionZone;

                              hasCollision = hitOtherBox || hitSelfPoint;

                              if (hasCollision) {{
                                // 阶段 1: 优先向上死磕 (前 3 次)
                                if (attempts < 3) {{
                                  if (boxY - 35 > chartArea.top) {{
                                    boxY -= 35;
                                  }}
                                }}
                                // 阶段 2: 左右交替横移探测 (3-12 次)
                                else if (attempts < 12) {{
                                    // direction 为 1(右) 或 -1(左)
                                    const direction = (attempts % 2 === 0) ? 1 : -1;
                                    // 随着次数增加，横移距离从 60px 扩大到 120px 等
                                    const multiplier = Math.ceil((attempts - 3) / 2);
                                    const step = multiplier * 35;
                                    
                                    boxX = point.x + (direction * step);
                                    boxY = point.y - 35; // 既然横移了，重置高度重新从上方尝试
                                }}
                                // 阶段 3: 实在不行向下排队 (12 次以后)
                                else {{
                                    boxY = point.y + 25 + ((attempts - 12) % 4) * 40;
                                    boxX = point.x + 10; // 回归默认 X
                                }}

                                // --- 边界实时修正 (防止避让时飞出画布) ---
                                if (boxX + boxW > chartArea.right) boxX = chartArea.right - boxW - 5;
                                if (boxX < MIN_SAFE_X) boxX = MIN_SAFE_X;
                                if (boxY < chartArea.top) boxY = chartArea.top + 5;
                                if (boxY + boxH > chartArea.bottom) boxY = chartArea.bottom - boxH - 5;

                                attempts++;
                              }}
                            }}

                            // 4. 存入最终坐标
                            usedAreas.push({{ x: boxX, y: boxY, w: boxW, h: boxH }});

                            // --- 核心修正 3: 绘图必须引用计算后的 boxX 和 boxY ---
                            ctx.save();    

                            ctx.fillStyle = '#999999';
                            ctx.beginPath();
                            ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
                            ctx.fill();

                            ctx.strokeStyle = '#999999';
                            ctx.lineWidth = 1;
                            ctx.setLineDash([4, 4]);
                            ctx.beginPath();
                            ctx.moveTo(point.x, point.y);
                            ctx.lineTo(boxX + boxW / 2, boxY + boxH / 2);
                            ctx.stroke();
                            ctx.setLineDash([]);

                            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
                            ctx.strokeStyle = '#999999';
                            ctx.lineWidth = 1;
                            ctx.setLineDash([4, 4]);
                            ctx.beginPath();
                            ctx.roundRect(boxX, boxY, boxW, boxH, 4);
                            ctx.fill();
                            ctx.stroke();
                            ctx.setLineDash([]);

                            ctx.fillStyle = '#000000';
                            ctx.font = '11px TencentW7';
                            ctx.textAlign = 'left';
                            ctx.textBaseline = 'top';
                            
                            const paddingX = 4        // 左右边距
                            const lineHeight = 13;     // 行高（文字11px + 上下间距3px）
                            const maxWidth = boxW - (paddingX * 2);

                            // 1. 自动换行处理 (保持不变)
                            let allRenderLines = [];
                            const sourceTexts =  [anno.fullText];
                            sourceTexts.forEach(textSegment => {{
                                let characters = textSegment.split('');
                                let currentLine = '';
                                for (let i = 0; i < characters.length; i++) {{
                                    let testLine = currentLine + characters[i];
                                    if (ctx.measureText(testLine).width > maxWidth && i > 0) {{
                                        allRenderLines.push(currentLine);
                                        currentLine = characters[i];
                                    }} else {{
                                        currentLine = testLine;
                                    }}
                                }}
                                allRenderLines.push(currentLine);
                            }});

                            // 2. 核心修正：计算垂直居中的起始 Y
                            // 总高度 = 行数 * 行高
                            const totalTextHeight = allRenderLines.length * lineHeight;

                            // 计算公式：框顶坐标 + (框高度 - 文字总高度) / 2
                            // 这样得出的 startY 就是第一行文字顶部的绝对坐标
                            const startY = boxY + (boxH - totalTextHeight) / 2;

                            // 3. 绘制文字
                            allRenderLines.forEach((line, index) => {{
                                // 每一行的坐标 = 起始坐标 + (第几行 * 行高)
                                ctx.fillText(line, boxX + paddingX, startY + (index * lineHeight));
                            }});

                            annotationBoxes.push({{
                                x: boxX,
                                y: boxY,
                                width: boxW,
                                height: boxH,
                                fullText: anno.fullText
                            }});
                            ctx.restore();
                        }}
                    }});

                    meta2.data.forEach((point, index) => {{
                        ctx.save();
                        ctx.fillStyle = '#595959';
                        ctx.beginPath();
                        ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);
                        ctx.fill();
                        ctx.restore();
                    }});

                }}
            }}]
        }});

        canvas.addEventListener('mousemove', (e) => {{
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            let hoveredBox = null;
            annotationBoxes.forEach(box => {{
                if (x >= box.x && x <= box.x + box.width && y >= box.y && y <= box.y + box.height) {{
                    hoveredBox = box;
                }}
            }});

            if (hoveredBox) {{
                hoverTooltip.innerHTML = hoveredBox.fullText;
                hoverTooltip.style.display = 'block';
                hoverTooltip.style.left = (e.clientX - rect.left + 10) + 'px';
                hoverTooltip.style.top = (e.clientY - rect.top + 10) + 'px';
                canvas.style.cursor = 'pointer';
            }} else {{
                hoverTooltip.style.display = 'none';
                canvas.style.cursor = 'default';
            }}
        }});

        canvas.addEventListener('mouseleave', () => {{
            hoverTooltip.style.display = 'none';
        }});
    </script>
</body>

</html>

"""

# ──────────────────────────────────────────────
# p6 - 微博平台热度分析
# ──────────────────────────────────────────────

def gen_p6(data: dict, assets: dict) -> str:
    p6 = data['P6']
    meta = data['meta']

    main_event = meta['main_event']
    report_stage = meta['report_stage']


    wb_total_volume = p6['wb_total_volume']
    wb_total_interaction = p6['wb_total_interaction']
    wb_heat_index = p6['wb_heat_index']
    wb_yoy_volume = p6['wb_yoy_volume']
    wb_yoy_interaction = p6['wb_yoy_interaction']
    wb_yoy_heat_index = p6['wb_yoy_heat_index']
    summary = p6['summary']
    #chart_title = p6['chart_title']
    #page_title = p6['page_title']
    
    wb_vol_data = p6['wb_vol_data']
    wb_inter_data = p6['wb_inter_data']
    wb_date_labels = p6['wb_date_labels']
    wb_peak_events = p6['wb_peak_events']
    wb_peak_events  = sorted(wb_peak_events,  key=lambda e: e['idx'])


    vol_max = nice_max(wb_vol_data)
    inter_max_wan = nice_max([v / 10000 for v in wb_inter_data])

    cover_bg_left = assets['cover_bg_left']
    music = assets['music']
    engage = assets['engage']
    heart = assets['heart']
    VCT_top = assets['VCT_top']
    logo = assets['logo']
    font= assets['font']
    

    weibo_icon = assets['weibo_icon']
    douyin_icon = assets['douyin_icon']
    bilibili_icon = assets['bilibili_icon']
    xiaohongshu_icon = assets['xiaohongshu_icon']
    

    # 构建标注列表
    annotations = []
    for i, item in enumerate(wb_peak_events[:6]):  # 最多取6条
      num = CIRCLED[i]
      idx = item["idx"]
      date_label = item["date_label"]
      text = item["text"]

      annotations.append({
          "idx": idx,
          "text": [f"{num}{date_label}", text],
          "fullText": f"{num}{date_label} {text}"
      })

    return f"""
    <!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <style>
        @font-face {{
            font-family: 'TencentW7';
            src: url('{font}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'TencentW7', 'Noto Sans SC', sans-serif;
        }}


        .slide-container {{
            width: 100%;
            height: 720px;
            margin: auto;
            position: relative;
            background-image: url('{cover_bg_left}');
            background-size: 100% 100%;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }}

        .logo {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 113px;
            height: 113px;
            z-index: 0;
        }}

        .page-title {{
            position: absolute;
            left: 15.5%;
            top: 10px;
            font-size: 36px;
            font-weight: 600;
            color: #000000;
            z-index: 10;
        }}

        .content-wrapper {{
            width: 100%;
            height: 640px;
            position: relative;
            z-index: 5;
            padding: 50px 80px 30px 80px;
            box-sizing: border-box;
            display: flex;
            gap: 30px;
        }}


        .left-panel {{
            width: 320px;
            display: flex;
            flex-direction: column;
        }}

        .panel-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 5px;
        }}

        .douyin-logo {{
            width: 50px;
            height: 50px;
        }}

        .panel-title {{
            font-size: 24px;
            font-weight: 700;
            color: #000000;
        }}

        .divider {{
            height: 6px;
            background: #c00000;
            width: 235px;
            margin-bottom: 30px;
        }}

        .data-cards {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .data-card {{
            background: #ffffff;
            border: 3px solid #c00000;
            border-radius: 8px;
            padding: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .card-data {{
            display: flex;
            gap: 20px;
            align-items: center;
            flex: 1;
        }}

        .data-group {{
            display: flex;
            flex-direction: column;
        }}

        .data-group-current {{
            min-width: 100px;
        }}

        .data-group-yoy {{
            min-width: 80px;
        }}

        .data-label {{
            font-size: 13px;
            color: #c00000;
            font-weight: 600;
            margin-bottom: 4px;
        }}

        .data-value-large {{
            font-size: 28px;
            font-weight: 900;
            color: #000000;
        }}

        .data-value-small {{
            font-size: 18px;
            font-weight: 700;
            color: #000;
            height: 42px;
            line-height: 42px;
            text-align: center;
        }}


        .card-icon {{
            font-size: 32px;
        }}

        .summary-box {{
            background: #f5f5f5;
            border-radius: 8px;
            padding: 16px;
            font-size: 14px;
            color: #000000;
            line-height: 1.6;
            margin: auto;
        }}

        .right-panel {{
            flex: 1;
            display: flex;
            flex-direction: column;
        }}

        .chart-title {{
            font-size: 16px;
            color: #3e3e3e;
            font-weight: 900;
            margin-bottom: 16px;
            text-align: center;
        }}

        .chart-wrapper {{
            width: 100%;
            height: 475px;
            position: relative;
        }}

        .hover-tooltip {{
            position: absolute;
            background: rgba(255, 255, 255, 0.98);
            border: 2px solid #999999;
            border-radius: 6px;
            padding: 10px 12px;
            font-size: 13px;
            color: #000000;
            pointer-events: none;
            display: none;
            z-index: 2000;
            max-width: 200px;
            line-height: 1.4;
        }}

        .chat-title-mark {{
            margin: 10px 50px;
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }}

        .mark-dispaly {{
            width: 135px;
            display: flex;
            align-items: center;
        }}

        .mark-dis-y {{
            display: inline-block;
            width: 30px;
            height: 10px;
            background: #ffcc66;
            margin-right: 10px;
        }}

        .mark-dis-r {{
            display: inline-block;
            width: 30px;
            height: 6px;
            background: #ff9a36;
            margin-right: 10px;
        }}

        .chat-y-lable-box {{
            width: 100%;
            box-sizing: border-box;
            color: #000000;
            font-weight: 800;
            font-size: 13px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            align-items: center;
            padding: 0 10px;
        }}
    </style>
    <title>微博舆情数据表现-核心平台</title>
</head>

<body>
    <div class="slide-container">
        <img src="{logo}"
            alt="Logo" class="logo">
        <h1 class="page-title">微博舆情数据表现-核心平台</h1>

        <div class="content-wrapper">
            <div class="left-panel">
                <div class="panel-header">
                    <img src="{weibo_icon}"
                        alt="抖音" class="channel-icon">
                    <div class="panel-title" style="color: #c00000;">数据概览</div>
                </div>
                <div class="divider"></div>

                <div class="data-cards">
                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">总声量</div>
                                <div class="data-value-large">{wb_total_volume}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛声量</div>
                                <div class="data-value-small">{wb_yoy_volume}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{music}"
                                alt="icon">
                        </div>
                    </div>

                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">总互动量</div>
                                <div class="data-value-large">{wb_total_interaction}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛互动</div>
                                <div class="data-value-small">{wb_yoy_interaction}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{engage}"
                                alt="icon">
                        </div>
                    </div>

                    <div class="data-card">
                        <div class="card-data">
                            <div class="data-group data-group-current">
                                <div class="data-label">热度指数</div>
                                <div class="data-value-large">{wb_heat_index}</div>
                            </div>
                            <div class="data-group data-group-yoy">
                                <div class="data-label">25s1常规赛热度</div>
                                <div class="data-value-small">{wb_yoy_heat_index}</div>
                            </div>
                        </div>
                        <div class="card-icon" style="color: #c00000;">
                            <img style="width: 35px;height: auto;" src="{heart}"
                                alt="icon">
                        </div>
                    </div>
                </div>

                <div class="summary-box">
                    {summary}
                </div>
            </div>

            <div class="right-panel">
                <div class="chart-title">2026{main_event}{report_stage}声量与互动量趋势（By day）- 微博</div>
                <div class="chat-title-mark">
                    <div class="mark-dispaly">
                        <span class="mark-dis-y"></span>
                        <span>声量</span>
                    </div>
                    <div class="mark-dispaly">
                        <span class="mark-dis-r"></span>
                        <span>互动量</span>
                    </div>
                </div>
                <div class="chart-wrapper" id="chartWrapper">
                    <div class="chat-y-lable-box">
                        <div class="y-left" style="text-align: left;">声量</div>
                        <div class="y-right" style="text-align: right;">互动量（万）</div>
                    </div>
                    <canvas id="trendChart"></canvas>
                    <div id="hoverTooltip" class="hover-tooltip"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('trendChart');
        const ctx = canvas.getContext('2d');
        const hoverTooltip = document.getElementById('hoverTooltip');

        const dateLabels = {js_array(wb_date_labels)};
        const volData = {js_array(wb_vol_data)};
        const rawInterData = {js_array(wb_inter_data)};
        const interData = rawInterData.map(v => +(v/10000).toFixed(0));
        const volMax = {vol_max};
        const interMax = {inter_max_wan};

        const annotations = {json.dumps(annotations, ensure_ascii=False)};

        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: dateLabels,
                datasets: [
                    {{
                        label: '声量',
                        data: volData,
                        borderColor: '#ffcc66',
                        backgroundColor: '#ffcc66',
                        borderWidth: 1,
                        borderDash: [],
                        tension: 0.3,
                        pointRadius: 0,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: '#ffcc66',
                        yAxisID: 'y',
                        fill: true,
                        order: 2
                    }},
                    {{
                        label: '互动量',
                        data: interData,
                        borderColor: '#ff9a36',
                        backgroundColor: 'transparent',
                        borderWidth: 2,
                        borderDash: [6, 3],
                        tension: 0.3,
                        pointRadius: 0,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: '#ff9a36',
                        yAxisID: 'y1',
                        fill: false,
                        order: 1
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                interaction: {{ mode: 'index', intersect: false }},
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        enabled: true,
                        mode: 'index',
                        intersect: false,
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleFont: {{ size: 13, family: 'TencentW7', weight: 'bold' }},
                        bodyFont: {{ size: 12, family: 'TencentW7', weight: 'bold' }},
                        callbacks: {{
                            title: function (context) {{ return '日期: ' + context[0].label; }},
                            label: function (context) {{
                                let label = context.dataset.label + ': ';
                                if (context.datasetIndex === 0) {{
                                    label += Math.round(context.parsed.y);
                                }} else {{
                                    label += Math.round(context.parsed.y) + '万';
                                }}
                                return label;
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        type: 'linear',
                        position: 'left',
                        beginAtZero: true,
                        max: volMax,
                        grid: {{ color: 'rgba(0, 0, 0, 0.05)' }},
                        ticks: {{
                            font: {{ size: 11, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            stepSize: volMax/4
                        }}
                    }},
                    y1: {{
                        type: 'linear',
                        position: 'right',
                        beginAtZero: true,
                        max: interMax,
                        grid: {{ display: false }},
                        ticks: {{
                            font: {{ size: 11, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            stepSize: interMax/4,
                            callback: function (value) {{
                                return value + '万';
                            }}
                        }}
                    }},
                    x: {{
                        grid: {{ display: false }},
                        ticks: {{
                            font: {{ size: 10, family: 'TencentW7', weight: 'bold' }},
                            color: '#5b6d7e',
                            maxRotation: 0,
                            minRotation: 0
                        }}
                    }}
                }}
            }},
            plugins: [{{
                id: 'peakAnnotations',
                afterDatasetsDraw: (chart) => {{
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(0);
                    const meta2 = chart.getDatasetMeta(1);
                    const chartArea = chart.chartArea;
                    annotationBoxes = [];

                    // 1. 在循环外定义常量
                    const boxW = 140;
                    const boxH = 35;
                    const usedAreas = [];

                    const MIN_SAFE_X = 180; // 硬性安全线：确保弹窗左侧不进入灰色区
                    annotations.forEach(anno => {{
                        const point = meta.data[anno.idx];
                        if (point) {{
                            // 1. 初始化变量：初始就卡死在 MIN_SAFE_X 之后
                            let boxX = Math.max(point.x + 10, MIN_SAFE_X);
                            let boxY = point.y - 45;

                            let attempts = 0;
                            let hasCollision = true;

                            // 2. 避让逻辑：全程只操作 boxX 和 boxY
                            while (hasCollision && attempts < 15) {{
                              // 检查是否撞到了已经画好的其他弹窗
                              const hitOtherBox = usedAreas.some((area) => {{
                                return (
                                  boxX < area.x + area.w + 8 &&
                                  boxX + boxW > area.x - 8 &&
                                  boxY < area.y + area.h + 8 &&
                                  boxY + boxH > area.y - 8
                                );
                              }});

                              // 【核心优化】：检查当前弹窗是否压住了它自己的数据点
                              // 定义一个“点保护区”，即点周围 15px 的范围
                              const pointProtectionZone = 15;
                              const hitSelfPoint =
                                boxX < point.x + pointProtectionZone &&
                                boxX + boxW > point.x - pointProtectionZone &&
                                boxY < point.y + pointProtectionZone &&
                                boxY + boxH > point.y - pointProtectionZone;

                              hasCollision = hitOtherBox || hitSelfPoint;

                              if (hasCollision) {{
                                // 阶段 1: 优先向上死磕 (前 3 次)
                                if (attempts < 3) {{
                                  if (boxY - 35 > chartArea.top) {{
                                    boxY -= 35;
                                  }}
                                }}
                                // 阶段 2: 左右交替横移探测 (3-12 次)
                                else if (attempts < 12) {{
                                    // direction 为 1(右) 或 -1(左)
                                    const direction = (attempts % 2 === 0) ? 1 : -1;
                                    // 随着次数增加，横移距离从 60px 扩大到 120px 等
                                    const multiplier = Math.ceil((attempts - 3) / 2);
                                    const step = multiplier * 35;
                                    
                                    boxX = point.x + (direction * step);
                                    boxY = point.y - 35; // 既然横移了，重置高度重新从上方尝试
                                }}
                                // 阶段 3: 实在不行向下排队 (12 次以后)
                                else {{
                                    boxY = point.y + 25 + ((attempts - 12) % 4) * 40;
                                    boxX = point.x + 10; // 回归默认 X
                                }}

                                // --- 边界实时修正 (防止避让时飞出画布) ---
                                if (boxX + boxW > chartArea.right) boxX = chartArea.right - boxW - 5;
                                if (boxX < MIN_SAFE_X) boxX = MIN_SAFE_X;
                                if (boxY < chartArea.top) boxY = chartArea.top + 5;
                                if (boxY + boxH > chartArea.bottom) boxY = chartArea.bottom - boxH - 5;

                                attempts++;
                              }}
                            }}

                            usedAreas.push({{ x: boxX, y: boxY, w: boxW, h: boxH }});

                            ctx.save();

                            ctx.fillStyle = '#ffcc66';
                            ctx.beginPath();
                            ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
                            ctx.fill();

                            ctx.strokeStyle = '#999999';
                            ctx.lineWidth = 1;
                            ctx.setLineDash([4, 4]);
                            ctx.beginPath();
                            ctx.moveTo(point.x, point.y);
                            ctx.lineTo(boxX + boxW / 2, boxY + boxH / 2);
                            ctx.stroke();
                            ctx.setLineDash([]);

                            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
                            ctx.strokeStyle = '#999999';
                            ctx.lineWidth = 1;
                            ctx.setLineDash([4, 4]);
                            ctx.beginPath();
                            ctx.roundRect(boxX, boxY, boxW, boxH, 4);
                            ctx.fill();
                            ctx.stroke();
                            ctx.setLineDash([]);

                            ctx.fillStyle = '#000000';
                            ctx.font = '11px TencentW7';
                            ctx.textAlign = 'left';
                            ctx.textBaseline = 'top';
                            
                            const paddingX = 4;        // 左右边距
                            const lineHeight = 13;     // 行高（文字11px + 上下间距3px）
                            const maxWidth = boxW - (paddingX * 2);

                            // 1. 自动换行处理 (保持不变)
                            let allRenderLines = [];
                            const sourceTexts =  [anno.fullText];
                            sourceTexts.forEach(textSegment => {{
                                let characters = textSegment.split('');
                                let currentLine = '';
                                for (let i = 0; i < characters.length; i++) {{
                                    let testLine = currentLine + characters[i];
                                    if (ctx.measureText(testLine).width > maxWidth && i > 0) {{
                                        allRenderLines.push(currentLine);
                                        currentLine = characters[i];
                                    }} else {{
                                        currentLine = testLine;
                                    }}
                                }}
                                allRenderLines.push(currentLine);
                            }});

                            // 2. 核心修正：计算垂直居中的起始 Y
                            // 总高度 = 行数 * 行高
                            const totalTextHeight = allRenderLines.length * lineHeight;

                            // 计算公式：框顶坐标 + (框高度 - 文字总高度) / 2
                            // 这样得出的 startY 就是第一行文字顶部的绝对坐标
                            const startY = boxY + (boxH - totalTextHeight) / 2;

                            // 3. 绘制文字
                            allRenderLines.forEach((line, index) => {{
                                // 每一行的坐标 = 起始坐标 + (第几行 * 行高)
                                ctx.fillText(line, boxX + paddingX, startY + (index * lineHeight));
                            }});

                            annotationBoxes.push({{
                                x: boxX,
                                y: boxY,
                                width: boxW,
                                height: boxH,
                                fullText: anno.fullText
                            }});
                            ctx.restore();
                        }}
                    }});

                    meta2.data.forEach((point, index) => {{
                        ctx.save();
                        ctx.fillStyle = '#ff9a36';
                        ctx.beginPath();
                        ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);   //互动量圆点设置
                        ctx.fill();
                        ctx.restore();
                    }});

                }}
            }}]
        }});

        canvas.addEventListener('mousemove', (e) => {{
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            let hoveredBox = null;
            annotationBoxes.forEach(box => {{
                if (x >= box.x && x <= box.x + box.width && y >= box.y && y <= box.y + box.height) {{
                    hoveredBox = box;
                }}
            }});

            if (hoveredBox) {{
                hoverTooltip.innerHTML = hoveredBox.fullText;
                hoverTooltip.style.display = 'block';
                hoverTooltip.style.left = (e.clientX - rect.left + 10) + 'px';
                hoverTooltip.style.top = (e.clientY - rect.top + 10) + 'px';
                canvas.style.cursor = 'pointer';
            }} else {{
                hoverTooltip.style.display = 'none';
                canvas.style.cursor = 'default';
            }}
        }});

        canvas.addEventListener('mouseleave', () => {{
            hoverTooltip.style.display = 'none';
        }});
    </script>
</body>

</html>
"""


# ──────────────────────────────────────────────
# P7 / P8 通用：竞品对比页
# ──────────────────────────────────────────────

def gen_compare_page(data: dict, assets: dict, page: str) -> str:
    """page: 'P7' or 'P8'"""
    is_p7 = (page == 'P7')
    pd = data[page]
    meta = data['meta']
    main_event = meta['main_event']

    slot_event_name = pd['slot_event_name']

    #page_title = pd['page_title']

    summary = pd['summary']
    main_summary = pd['main_summary']

    if is_p7:
        slot_summary = pd['slot1_summary']
        slot_platform_dist = pd['slot1_platform_dist']
        slot_vol_data = pd['slot1_heat_data']
        slot_peaks = pd['slot1_peaks']
        slot_color = '#9370db'
        

        slot_row_class = 'slot-row-kpl'
        page_title = f"{slot_event_name}整体社媒热度概览"
    else:
        slot_summary = pd['slot2_summary']
        slot_platform_dist = pd['slot2_platform_dist']
        slot_vol_data = pd['slot2_heat_data']
        slot_peaks = pd['slot2_peaks']
        slot_color = '#1e90ff'
        slot_row_class = 'slot-row-vct'
        page_title = f"{slot_event_name}整体社媒热度概览"

    main_vol_data = pd['main_heat_data']
    date_labels = pd['date_labels']
    main_peaks = pd['main_peaks']
    main_peaks = sorted(main_peaks,key=lambda e: e['idx'])
    slot_peaks= sorted(slot_peaks,key=lambda e: e['idx'])

    # 圆环图数据
    plat_labels = ['微博', '抖音', 'B站', '小红书','快手', '其他']
    vol_vals = [slot_platform_dist['volume'].get(k, 0) for k in plat_labels]
    inter_vals = [slot_platform_dist['interaction'].get(k, 0) for k in plat_labels]
    heat_vals = [slot_platform_dist['heat'].get(k, 0) for k in plat_labels]

    # 折线图 Y 轴
    all_data = main_vol_data + slot_vol_data
    y_max = nice_max(all_data)
    y_step = y_max / 4

    # 构建LPL标注
    lpl_annotations = []
    for i, e in enumerate(main_peaks[:3]):
        idx = e['idx']
        date_lbl = e.get('date_label', '')
        text = e.get('text', e.get('summary', ''))
        num = CIRCLED[i]
        lpl_annotations.append({
            'idx': idx,
            'text': [f"{num}{date_lbl}", text],
            'fullText': f"{num}{date_lbl} {text}"
        })

    # 构建竞品标注
    slot_annotations = []
    for i, e in enumerate(slot_peaks[:3]):
        idx = e['idx']
        date_lbl = e.get('date_label', '')
        text = e.get('text', e.get('summary', ''))
        num = CIRCLED[i + 3]
        slot_annotations.append({
            'idx': idx,
            'text': [f"{num}{date_lbl}", text],
            'fullText': f"{num}{date_lbl} {text}"
        })

    cover_bg_left = assets['cover_bg_left']
    logo = assets['logo']
    font= assets['font']
    

    # 对比表
    compare_row_slot = f"""
                                <tr class="{slot_row_class}">
                                    <td>{slot_event_name}</td>
                                    <td>{slot_summary['volume']}</td>
                                    <td>{slot_summary['interaction']}</td>
                                    <td>{slot_summary['heat_index']}</td>
                                </tr>"""
    compare_row_main = f"""
                                <tr class="lpl-row">
                                    <td>{main_event}</td>
                                    <td>{main_summary['volume']}</td>
                                    <td>{main_summary['interaction']}</td>
                                    <td>{main_summary['heat_index']}</td>
                                </tr>"""

    return f"""<!DOCTYPE<html lang="zh">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
    <style>
      @font-face {{
        font-family: "TencentW7";
        src: url("{font}") format("opentype");
        font-weight: normal;
        font-style: normal;
      }}

      body {{
        margin: 0;
        padding: 0;
        font-family: "TencentW7", "Noto Sans SC", sans-serif;
      }}

      .slot-row-kpl{{
        color: #7030a0;
      }}

      .slot-row-vct{{
         color: #1e90ff;
      }}
      
      .slide-container {{
        width: 100%;
        height: 720px;
        margin: auto;
        position: relative;
        background-image: url("{cover_bg_left}");
        background-size: 100% 100%;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
      }}

      .logo {{
        position: absolute;
        top: 20px;
        right: 20px;
        width: 113px;
        height: 113px;
        z-index: 0;
      }}

      .page-title {{
        position: absolute;
        left: 15.5%;
        top: 10px;
        font-size: 36px;
        font-weight: 600;
        color: #000000;
        z-index: 10;
      }}

      .content-wrapper {{
        width: 100%;
        height: 640px;
        position: relative;
        z-index: 5;
        padding: 50px 80px 30px 80px;
        box-sizing: border-box;
      }}

      .chat-content {{
        width: 100%;
        height: auto;
        margin: 0 auto;
      }}

      .summary {{
        font-size: 16px;
        color: #333;
        line-height: 1.6;
        margin: 10px 0;
        font-weight: 500;
        padding-right: 140px;
      }}

      .highlight-red {{
        color: #c00000;
        font-weight: 700;
      }}

      .middle-section {{
        display: flex;
        gap: 15px;
        margin-bottom: 15px;
      }}

      .compare-table-wrapper {{
        flex: 0 0 380px;
      }}

      .compare-table {{
        width: 100%;
        height: 100%;
        background: #fff;
        border-radius: 8px;
        padding: 10px 10px 18px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        box-sizing: border-box;
      }}

      .compare-table table {{
        width: 100%;
        border-collapse: collapse;
      }}

      .compare-table th {{
        font-size: 18px;
        font-weight: 700;
        color: #000000;
        text-align: center;
        padding: 15px 6px;
        border-bottom: 1px solid #e0e0e0;
      }}

      .compare-table td {{
        font-size: 18px;
        font-weight: 900;
        text-align: center;
        padding: 20px 6px;
      }}

      .compare-table td:first-child {{
        font-size: 18px;
        font-weight: 700;
      }}

      .kpl-row {{
        color: #7030a0;
      }}

      .lpl-row {{
        color: #c00000;
      }}

      .doughnut-section {{
        flex: 1;
        display: flex;
        align-items: center;
        background: #fff;
        border-radius: 8px;
        padding: 15px 20px;
        box-sizing: border-box;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      }}

      .charts-container {{
        flex: 1;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
      }}

      .doughnut-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .doughnut-title {{
        font-size: 14px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 6px;
      }}

      .doughnut-container {{
        width: 100%;
        height: 160px;
        max-width: 160px;
      }}

      .global-legend {{
        display: flex;
        flex-direction: column;
        gap: 6px;
        margin-left: 20px;
        font-size: 12px;
      }}

      .legend-item {{
        display: flex;
        align-items: center;
        gap: 6px;
      }}

      .legend-color {{
        width: 10px;
        height: 10px;
        display: inline-block;
      }}

      .trend-chart-wrapper {{
        height: 220px;
        position: relative;
      }}

      .hover-tooltip {{
        position: absolute;
        background: rgba(255, 255, 255, 0.98);
        border: 2px solid #999999;
        border-radius: 6px;
        padding: 10px 12px;
        font-size: 13px;
        color: #000000;
        pointer-events: none;
        display: none;
        z-index: 2000;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        max-width: 200px;
        line-height: 1.4;
      }}

      .bottom-section {{
        width: 100%;
        height: 300px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        background: #fff;
        border-radius: 8px;
        padding: 10px;
        box-sizing: border-box;
      }}

      .chat-title-mark {{
        margin: 0 0 5px 5px;
        font-size: 10px;
        font-weight: 900;
      }}
    </style>
    <title>{page_title}</title>
  </head>

  <body>
    <div class="slide-container">
      <img
        src="{logo}"
        alt="Logo"
        class="logo"
      />
      <h1 class="page-title">{page_title}</h1>

      <div class="content-wrapper">
        <div class="chat-content">
          <div class="summary">
            {summary}
          </div>
          <div class="middle-section">
            <div class="compare-table-wrapper">
              <div class="compare-table">
                <table>
                  <thead>
                    <tr>
                      <th></th>
                      <th>声量</th>
                      <th>互动量</th>
                      <th>热度值</th>
                    </tr>
                  </thead>
                   <tbody>{compare_row_slot}{compare_row_main}
                </table>
              </div>
            </div>

            <div class="doughnut-section">
              <div class="charts-container">
                <div class="doughnut-item">
                  <div class="doughnut-title">{slot_event_name} 声量平台分布</div>
                  <div class="doughnut-container">
                    <canvas id="volumeChart"></canvas>
                  </div>
                </div>
                <div class="doughnut-item">
                  <div class="doughnut-title">{slot_event_name} 互动量平台分布</div>
                  <div class="doughnut-container">
                    <canvas id="interactionChart"></canvas>
                  </div>
                </div>
                <div class="doughnut-item">
                  <div class="doughnut-title">{slot_event_name} 热度值平台分布</div>
                  <div class="doughnut-container">
                    <canvas id="heatChart"></canvas>
                  </div>
                </div>
              </div>
              <div class="global-legend">
                <div class="legend-item">
                  <span class="legend-color" style="background: #c00000"></span>
                  微博
                </div>
                <div class="legend-item">
                  <span class="legend-color" style="background: #00bfff"></span>
                  抖音
                </div>
                <div class="legend-item">
                  <span class="legend-color" style="background: #00b050"></span>
                  B站
                </div>
                <div class="legend-item">
                  <span class="legend-color" style="background: #ff6b9d"></span>
                  小红书
                </div>
                <div class="legend-item">
                  <span class="legend-color" style="background: #89cff0"></span>
                  快手
                </div>
                <div class="legend-item">
                  <span class="legend-color" style="background: #cccccc"></span>
                  其他
                </div>
              </div>
            </div>
          </div>
          <div class="bottom-section">
            <div
              class="chart-title"
              style="
                font-size: 14px;
                font-weight: 700;
                text-align: center;
                margin-bottom: 12px;
              "
            >
              {main_event} vs {slot_event_name} 热度趋势对比
            </div>
            <div class="chat-title-mark">
              <span>热度值</span>
            </div>

            <div class="trend-chart-wrapper" id="trendWrapper">
              <canvas id="trendChart"></canvas>
              <div id="hoverTooltip" class="hover-tooltip"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    
    <script>
      Chart.register(ChartDataLabels);

      const platformColors = {{
        微博: "#c00000",
        抖音: "#00bfff",
        B站: "#00b050",
        小红书: "#ff6b9d",
        快手: "#89cff0",
        其他: "#cccccc",
      }};

      const labels = ["微博", "抖音", "B站", "小红书", "快手", "其他"];
      const colors = labels.map(l => platformColors[l]);

      const doughnutOptions = {{
        responsive: true,
        maintainAspectRatio: false,
        layout: {{
          padding: {{
            top: 5,
            bottom: 5,
            left: 5,
            right: 5,
          }},
        }},
        plugins: {{
          legend: {{ display: false }},
          datalabels: {{
            color: "#000000",
            font: {{ size: 9, weight: "bold", family: "TencentW7" }},
            formatter: (value) => (value >= 5 ? Math.round(value) + "%" : ""),
          }},
        }},
      }};

        new Chart(document.getElementById('volumeChart'), {{
            type: 'doughnut',
            data:{{labels:labels, datasets:[{{data:{js_array(vol_vals)}, backgroundColor:colors, borderWidth:2, borderColor:'#fff'}}]}},
            options: doughnutOptions
        }});

        new Chart(document.getElementById('interactionChart'), {{
            type: 'doughnut',
            data:{{labels:labels, datasets:[{{data:{js_array(inter_vals)}, backgroundColor:colors, borderWidth:2, borderColor:'#fff'}}]}},
            options: doughnutOptions
        }});

        new Chart(document.getElementById('heatChart'), {{
            type: 'doughnut',
            data:{{labels:labels, datasets:[{{data:{js_array(heat_vals)}, backgroundColor:colors, borderWidth:2, borderColor:'#fff'}}]}},
            options: doughnutOptions
        }});

        const canvas = document.getElementById('trendChart');
        const ctx = canvas.getContext('2d');
        const hoverTooltip = document.getElementById('hoverTooltip');

        const dateLabels = {js_array(date_labels)};
        const lplData  = {js_array(main_vol_data)};
        const kplData  = {js_array(slot_vol_data)};
        const yMax = {y_max};
        const yStep = {y_step};
        const slotColor = {js_str(slot_color)};
        const slotName = {js_str(slot_event_name)};
        const mainName = {js_str(main_event)};

        const lplPeaks = {json.dumps(lpl_annotations, ensure_ascii=False)};
        const kplPeaks =  {json.dumps(slot_annotations, ensure_ascii=False)};

        let annotationBoxes = [];

      const chart = new Chart(ctx, {{
        type: "line",
        data: {{
          labels: dateLabels,
          datasets: [
            {{
              label: mainName,
              data: lplData,
              borderColor: "#c00000",
              backgroundColor: "transparent",
              borderWidth: 2.5,
              tension: 0.3,
              pointRadius: 0,
              pointHoverRadius: 5,
              fill: false,
            }},
            {{
              label: slotName,
              data: kplData,
              borderColor: "{slot_color}",
              backgroundColor: "transparent",
              borderWidth: 2.5,
              tension: 0.3,
              pointRadius: 0,
              pointHoverRadius: 5,
              fill: false,
            }},
          ],
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          layout: {{ padding: {{ top: 30 }}}},
          interaction: {{ mode: "index", intersect: false }},
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              enabled: true,
              backgroundColor: "rgba(0, 0, 0, 0.8)",
              titleFont: {{ size: 13, family: "TencentW7" }},
              bodyFont: {{ size: 12, family: "TencentW7" }},
              callbacks: {{
                title: function (context) {{
                  return "日期: " + context[0].label;
                }},
                label: function (context) {{
                  return context.dataset.label + ": " + Math.round(context.parsed.y);
                }},
              }},
            }},
            datalabels: {{ display: false }},
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              max: yMax,
              grid: {{ color: "rgba(0, 0, 0, 0.05)" }},
              ticks: {{
                font: {{ size: 11, family: "TencentW7", weight: "bold" }},
                color: "#5b6d7e",
                stepSize: yStep,
              }},
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ size: 10, family: "TencentW7", weight: "bold" }},
                color: "#5b6d7e",
                maxRotation: 0,
                minRotation: 0,
              }},
            }},
          }},
        }},
        plugins: [
          {{
            id: "peakAnnotations",
            afterDatasetsDraw: (chart) => {{
              const ctx = chart.ctx;
              const chartArea = chart.chartArea;
              annotationBoxes = [];

              // 1. 在循环外定义常量
              const boxW = 140;
              const boxH = 35;
              const usedAreas = [];

              const MIN_SAFE_X = 80; // 硬性安全线：确保弹窗左侧不进入灰色区

              const lplMeta = chart.getDatasetMeta(0);
              lplPeaks.forEach((anno) => {{
                const point = lplMeta.data[anno.idx];
                if (point) {{
                  const pointProtectionW = 20; // 增加宽度保护，防止侧面擦边
                  const pointProtectionH = 20; // 增加高度保护

                  const pointObstacle = {{
                    x: point.x - pointProtectionW / 2,
                    y: point.y - pointProtectionH / 2,
                    w: pointProtectionW,
                    h: pointProtectionH
                  }};
                  
                  // 注意：这里不要直接 push，因为 usedAreas 是在所有 anno 之间共享的。
                  // 我们需要一个包含【已绘制弹框】和【当前数据点障碍物】的临时判定数组。
                  const currentObstacles = [...usedAreas, pointObstacle];

                  // 1. 初始化变量：初始就卡死在 MIN_SAFE_X 之后
                  let boxX = Math.max(point.x + 10, MIN_SAFE_X);
                  let boxY = point.y - 50;

                  let attempts = 0;
                  let hasCollision = true;

                 // 2. 避让逻辑：左 -> 上 -> 右 -> 下
                  while (hasCollision && attempts < 30) {{
                    // 增加碰撞检测的容差，boxH 是 35，我们检测间距至少要 40 才能不重叠
                    const hitOtherBox = currentObstacles.some((area) => {{
                      return (
                        boxX < area.x + area.w + 8 && // 水平间距加大
                        boxX + boxW > area.x - 8 &&
                        boxY < area.y + area.h + 8 && // 垂直间距加大
                        boxY + boxH > area.y - 8
                      );
                    }});

                    const pointPadding = 12;
                    const hitSelfPoint =
                      boxX < point.x + pointPadding &&
                      boxX + boxW > point.x - pointPadding &&
                      boxY < point.y + pointPadding &&
                      boxY + boxH > point.y - pointPadding;

                    hasCollision = hitOtherBox || hitSelfPoint;

                    if (hasCollision) {{
                      if (attempts < 8) {{
                        // 第一阶段：向左探测
                        // 关键：不要只停在点左边，要根据 attempts 往左深处走
                        boxX = point.x - 20 - boxW - (attempts * 40); 
                        boxY = point.y - 45; 
                      }} else if (attempts < 18) {{
                        // 第二阶段：向上探测
                        // 关键：步长必须大于 boxH (35px)，这里用 50px 确保拉开距离
                        boxX = point.x + 10;
                        boxY = point.y - 45 - ((attempts - 7) * 50); 
                      }} else if (attempts < 25) {{
                        // 第三阶段：向右探测
                        boxX = point.x + 40 + ((attempts - 17) * 60);
                        boxY = point.y - 45;
                      }} else {{
                        // 第四阶段：向下排队
                        boxY = point.y + 35 + ((attempts - 24) * 45);
                        boxX = point.x + 10;
                      }}

                      // --- 边界强制修正 ---
                      if (boxX < MIN_SAFE_X) {{
                        // 如果向左走碰壁了，就停在 180
                        boxX = MIN_SAFE_X;
                        // 此时如果 hasCollision 依然为真，attempts 会继续增加
                        // 最终会跳出“向左”阶段，进入“向上”阶段，从而解决在 180 处的堆叠
                      }}
                      
                      if (boxX + boxW > chartArea.right) boxX = chartArea.right - boxW - 5;
                      if (boxY < chartArea.top) boxY = chartArea.top + 5;
                      if (boxY + boxH > chartArea.bottom) boxY = chartArea.bottom - boxH - 5;

                      attempts++;
                    }}
                  }}

                  // 3. 边界卡死
                  if (boxX + boxW > chartArea.right)
                  {{
                      boxX = chartArea.right - boxW - 5;
                  }}
                      
                  if (boxX < MIN_SAFE_X) boxX = MIN_SAFE_X;

                  // 如果弹框底部超出了图表区域底部，将其往上推
                  if (boxY + boxH > chartArea.bottom) {{
                    boxY = chartArea.bottom - boxH - 5;
                  }}
                  // 如果弹框顶部超出了图表区域顶部，将其往下推
                  if (boxY < chartArea.top) {{
                    boxY = chartArea.top + 5;
                  }}

                  // 4. 存入最终坐标
                  usedAreas.push({{ x: boxX, y: boxY, w: boxW, h: boxH }});

                  // --- 核心修正 3: 绘图必须引用计算后的 boxX 和 boxY ---
                  ctx.save();  

                  ctx.fillStyle = "#c00000";
                  ctx.beginPath();
                  ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
                  ctx.fill();

                  ctx.strokeStyle = "#c00000";
                  ctx.lineWidth = 1;
                  ctx.setLineDash([4, 4]);
                  ctx.beginPath();
                  ctx.moveTo(point.x, point.y);
                  ctx.lineTo(boxX + boxW / 2, boxY + boxH / 2);
                  ctx.stroke();
                  ctx.setLineDash([]);

                  ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
                  ctx.strokeStyle = "#c00000";
                  ctx.setLineDash([4, 4]);
                  ctx.beginPath();
                  ctx.roundRect(boxX, boxY, boxW, boxH, 4);
                  ctx.fill();
                  ctx.stroke();
                  ctx.setLineDash([]);

                  ctx.fillStyle = "#000000";
                  ctx.font = "10px TencentW7";
                  ctx.textAlign = "left";
                  ctx.textBaseline = "top";
                  
                  const paddingX = 6;        // 左右边距
                  const lineHeight = 13;     // 行高（文字11px + 上下间距3px）
                  const maxWidth = boxW - (paddingX * 2);

                  // 1. 自动换行处理 (保持不变)
                  let allRenderLines = [];
                  const sourceTexts =  [anno.fullText];
                  sourceTexts.forEach(textSegment => {{
                      let characters = textSegment.split('');
                      let currentLine = '';
                      for (let i = 0; i < characters.length; i++) {{
                          let testLine = currentLine + characters[i];
                          if (ctx.measureText(testLine).width > maxWidth && i > 0) {{
                              allRenderLines.push(currentLine);
                              currentLine = characters[i];
                          }} else {{
                              currentLine = testLine;
                          }}
                      }}
                      allRenderLines.push(currentLine);
                  }});

                  // 2. 核心修正：计算垂直居中的起始 Y
                  // 总高度 = 行数 * 行高
                  const totalTextHeight = allRenderLines.length * lineHeight;

                  // 计算公式：框顶坐标 + (框高度 - 文字总高度) / 2
                  // 这样得出的 startY 就是第一行文字顶部的绝对坐标
                  const startY = boxY + (boxH - totalTextHeight) / 2;

                  // 3. 绘制文字
                  allRenderLines.forEach((line, index) => {{
                      // 每一行的坐标 = 起始坐标 + (第几行 * 行高)
                      ctx.fillText(line, boxX + paddingX, startY + (index * lineHeight));
                  }});

                  annotationBoxes.push({{
                    x: boxX,
                    y: boxY,
                    width: boxW,
                    height: boxH,
                    fullText: anno.fullText,
                  }});
                  ctx.restore();
                }}
              }});

              const kplMeta = chart.getDatasetMeta(1);
              kplPeaks.forEach((anno) => {{
                const point = kplMeta.data[anno.idx];
                if (point) {{
                  const pointProtectionW = 20; // 增加宽度保护，防止侧面擦边
                  const pointProtectionH = 20; // 增加高度保护

                  const pointObstacle = {{
                    x: point.x - pointProtectionW / 2,
                    y: point.y - pointProtectionH / 2,
                    w: pointProtectionW,
                    h: pointProtectionH
                  }};
                  
                  // 注意：这里不要直接 push，因为 usedAreas 是在所有 anno 之间共享的。
                  // 我们需要一个包含【已绘制弹框】和【当前数据点障碍物】的临时判定数组。
                  const currentObstacles = [...usedAreas, pointObstacle];

                  // 1. 初始化变量：初始就卡死在 MIN_SAFE_X 之后
                  let boxX = Math.max(point.x + 10, MIN_SAFE_X);
                  let boxY = point.y - 50;

                  let attempts = 0;
                  let hasCollision = true;

                  
                 // 2. 避让逻辑：左 -> 上 -> 右 -> 下
                  while (hasCollision && attempts < 30) {{
                    // 增加碰撞检测的容差，boxH 是 35，我们检测间距至少要 40 才能不重叠
                    const hitOtherBox = currentObstacles.some((area) => {{
                      return (
                        boxX < area.x + area.w + 8 && // 水平间距加大
                        boxX + boxW > area.x - 8 &&
                        boxY < area.y + area.h + 8 && // 垂直间距加大
                        boxY + boxH > area.y - 8
                      );
                    }});

                    const pointPadding = 12;
                    const hitSelfPoint =
                      boxX < point.x + pointPadding &&
                      boxX + boxW > point.x - pointPadding &&
                      boxY < point.y + pointPadding &&
                      boxY + boxH > point.y - pointPadding;

                    hasCollision = hitOtherBox || hitSelfPoint;

                    if (hasCollision) {{
                      if (attempts < 8) {{
                        // 第一阶段：向左探测
                        // 关键：不要只停在点左边，要根据 attempts 往左深处走
                        boxX = point.x - 20 - boxW - (attempts * 40); 
                        boxY = point.y - 45; 
                      }} else if (attempts < 18) {{
                        // 第二阶段：向上探测
                        // 关键：步长必须大于 boxH (35px)，这里用 50px 确保拉开距离
                        boxX = point.x + 10;
                        boxY = point.y - 45 - ((attempts - 7) * 50); 
                      }} else if (attempts < 25) {{
                        // 第三阶段：向右探测
                        boxX = point.x + 40 + ((attempts - 17) * 60);
                        boxY = point.y - 45;
                      }} else {{
                        // 第四阶段：向下排队
                        boxY = point.y + 35 + ((attempts - 24) * 45);
                        boxX = point.x + 10;
                      }}

                      // --- 边界强制修正 ---
                      if (boxX < MIN_SAFE_X) {{
                        // 如果向左走碰壁了，就停在 180
                        boxX = MIN_SAFE_X;
                        // 此时如果 hasCollision 依然为真，attempts 会继续增加
                        // 最终会跳出“向左”阶段，进入“向上”阶段，从而解决在 180 处的堆叠
                      }}
                      
                      if (boxX + boxW > chartArea.right) boxX = chartArea.right - boxW - 5;
                      if (boxY < chartArea.top) boxY = chartArea.top + 5;
                      if (boxY + boxH > chartArea.bottom) boxY = chartArea.bottom - boxH - 5;

                      attempts++;
                    }}
                  }}

                  // 3. 边界卡死
                  if (boxX + boxW > chartArea.right)
                  {{
                      boxX = chartArea.right - boxW - 5;
                  }}
                      
                  if (boxX < MIN_SAFE_X) boxX = MIN_SAFE_X;

                  // 如果弹框底部超出了图表区域底部，将其往上推
                  if (boxY + boxH > chartArea.bottom) {{
                    boxY = chartArea.bottom - boxH - 5;
                  }}
                  // 如果弹框顶部超出了图表区域顶部，将其往下推
                  if (boxY < chartArea.top) {{
                    boxY = chartArea.top + 5;
                  }}

                  // 4. 存入最终坐标
                  usedAreas.push({{ x: boxX, y: boxY, w: boxW, h: boxH }});

                  // --- 核心修正 3: 绘图必须引用计算后的 boxX 和 boxY ---
                  ctx.save();  

                  ctx.fillStyle = "{slot_color}";
                  ctx.beginPath();
                  ctx.arc(point.x, point.y, 5, 0, 2 * Math.PI);
                  ctx.fill();

                  ctx.strokeStyle = "{slot_color}";
                  ctx.lineWidth = 1;
                  ctx.setLineDash([4, 4]);
                  ctx.beginPath();
                  ctx.moveTo(point.x, point.y);
                  ctx.lineTo(boxX + boxW / 2, boxY + boxH / 2);
                  ctx.stroke();
                  ctx.setLineDash([]);

                  ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
                  ctx.strokeStyle = "{slot_color}";
                  ctx.setLineDash([4, 4]);
                  ctx.beginPath();
                  ctx.roundRect(boxX, boxY, boxW, boxH, 4);
                  ctx.fill();
                  ctx.stroke();
                  ctx.setLineDash([]);

                  ctx.fillStyle = "#000000";
                  ctx.font = "10px TencentW7";
                  ctx.textAlign = "left";
                  ctx.textBaseline = "top";
                  

                  const paddingX = 6;        // 左右边距
                  const lineHeight = 13;     // 行高（文字11px + 上下间距3px）
                  const maxWidth = boxW - (paddingX * 2);

                  // 1. 自动换行处理 (保持不变)
                  let allRenderLines = [];
                  const sourceTexts =  [anno.fullText];
                  sourceTexts.forEach(textSegment => {{
                      let characters = textSegment.split('');
                      let currentLine = '';
                      for (let i = 0; i < characters.length; i++) {{
                          let testLine = currentLine + characters[i];
                          if (ctx.measureText(testLine).width > maxWidth && i > 0) {{
                              allRenderLines.push(currentLine);
                              currentLine = characters[i];
                          }} else {{
                              currentLine = testLine;
                          }}
                      }}
                      allRenderLines.push(currentLine);
                  }});

                  // 2. 核心修正：计算垂直居中的起始 Y
                  // 总高度 = 行数 * 行高
                  const totalTextHeight = allRenderLines.length * lineHeight;

                  // 计算公式：框顶坐标 + (框高度 - 文字总高度) / 2
                  // 这样得出的 startY 就是第一行文字顶部的绝对坐标
                  const startY = boxY + (boxH - totalTextHeight) / 2;

                  // 3. 绘制文字
                  allRenderLines.forEach((line, index) => {{
                      // 每一行的坐标 = 起始坐标 + (第几行 * 行高)
                      ctx.fillText(line, boxX + paddingX, startY + (index * lineHeight));
                  }});

                  annotationBoxes.push({{
                    x: boxX,
                    y: boxY,
                    width: boxW,
                    height: boxH,
                    fullText: anno.fullText,
                  }});
                  ctx.restore();
                }}
              }});
            }},
          }},
        ],
      }});

      canvas.addEventListener("mousemove", (e) => {{
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        let hoveredBox = null;
        annotationBoxes.forEach((box) => {{
          if (
            x >= box.x &&
            x <= box.x + box.width &&
            y >= box.y &&
            y <= box.y + box.height
          ) {{
            hoveredBox = box;
          }}
        }});

        if (hoveredBox) {{
          hoverTooltip.innerHTML = hoveredBox.fullText;
          hoverTooltip.style.display = "block";
          hoverTooltip.style.left = e.clientX - rect.left + 10 + "px";
          hoverTooltip.style.top = e.clientY - rect.top + 10 + "px";
          canvas.style.cursor = "pointer";
        }} else {{
          hoverTooltip.style.display = "none";
          canvas.style.cursor = "default";
        }}
      }});

      canvas.addEventListener("mouseleave", () => {{
        hoverTooltip.style.display = "none";
      }});
    </script>
  </body>
</html>
"""


# ──────────────────────────────────────────────
# 主函数
# ──────────────────────────────────────────────

def load_assets(base_dir: str) -> dict:
    """一次性加载所有素材，返回 base64 字典"""
    img_dir = os.path.join(base_dir, 'assets', 'images')
    font_dir = os.path.join(base_dir, 'assets', 'fonts')

    print(f"  ✓ {font_dir} ({font_dir})")
    assets = {
        'font':      b64(os.path.join(font_dir, '腾讯体-W7_副本.OTF'), 'font/otf'),
        'cover_bg':  b64(os.path.join(img_dir, 'cover_bg.png'), 'image/png'),
        'cover_bg_left':  b64(os.path.join(img_dir, 'cover_bg_left.jpg'), 'image/jpeg'),
        'music':  b64(os.path.join(img_dir, 'music.png'), 'image/png'),
        'heart':  b64(os.path.join(img_dir, 'heart.png'), 'image/png'),
        'engage':  b64(os.path.join(img_dir, 'engage.png'), 'image/png'),
        'VCT_top':  b64(os.path.join(img_dir, 'VCT_top.png'), 'image/png'),
        'weibo_icon':   b64(os.path.join(img_dir, 'weibo_icon.png'), 'image/png'),
        'douyin_icon':   b64(os.path.join(img_dir, 'douyin_icon.png'), 'image/png'),
        'bilibili_icon': b64(os.path.join(img_dir, 'bilibili_icon.png'), 'image/png'),
        'xiaohongshu_icon':  b64(os.path.join(img_dir, 'xiaohongshu_icon.png'), 'image/png'),
        'logo':      b64(os.path.join(img_dir, 'logo.png'), 'image/png'),
    }
    return assets


def main():
    parser = argparse.ArgumentParser(description='从 M1 JSON 生成社媒监测报告（单个 HTML）')
    parser.add_argument('--data', required=True, help='M1 JSON 文件路径')
    parser.add_argument('--output', required=True, help='输出目录')
    args = parser.parse_args()

    # 读取 JSON
    data_path = args.data
    if not os.path.isabs(data_path):
        data_path = os.path.join(os.getcwd(), data_path)
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 确定 base_dir（素材相对于脚本所在目录）
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 加载素材
    print("正在加载素材（base64 编码）...")
    assets = load_assets(base_dir)
    print(f"  字体: {len(assets['font'])//1024}KB (b64)")
    print(f"  封面背景: {len(assets['cover_bg'])//1024}KB (b64)")


    # 创建输出目录
    out_dir = args.output
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(os.getcwd(), out_dir)
    os.makedirs(out_dir, exist_ok=True)

    # 生成各页内容
    print("生成各页内容...")
    page_files = [
        ('p1.html', lambda: gen_p1(data, assets)),
        ('p2.html', lambda: gen_p2(data, assets)),
        ('p3.html', lambda: gen_p3(data, assets)),
        ('p4.html', lambda: gen_p4(data, assets)),
        ('p5.html', lambda: gen_p5(data, assets)),
        #('p6.html', lambda: gen_p6(data, assets)),
        ('p7.html', lambda: gen_compare_page(data, assets, 'P7')),
        ('p8.html', lambda: gen_compare_page(data, assets, 'P8')),
    ]

    for fname, gen_fn in page_files:
        out_path = os.path.join(out_dir, fname)
        html = gen_fn()
        # 如果返回的是 HTML 片段（section/div 开头），套上完整包装
        if not html.strip().startswith('<!DOCTYPE'):
            font_b64 = assets['font']
            html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://static-oss.deepminingai.com/web/static/js/tailwindcss@3.4.16.min.js"></script>
    <script src="https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js"></script>
    <style>
        @font-face {{
            font-family: 'TencentW7';
            src: url('{font_b64}') format('opentype');
            font-weight: normal;
            font-style: normal;
        }}
        html, body {{ margin:0; padding:0; width:100%; height:100%; background:#fff; font-family:'TencentW7','Noto Sans SC',sans-serif; }}
    </style>
</head>
<body>
{html}
</body>
</html>"""
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        size_kb = os.path.getsize(out_path) // 1024
        print(f"  ✓ {fname} ({size_kb} KB)")

    # 生成 index.html（7个 iframe 纵向排列）
    meta = data['meta']
    title = f"{meta['main_event']}{meta['report_stage']}社媒监测报告"
    page_names = [f for f, _ in page_files]

    iframes_html = '\n'.join([
        f' <div class="slide-frame"><iframe src="{fname}" scrolling="no" style="width:100%;height:720px;border:none;display:block;"></iframe></div>'
        for fname in page_names
    ])

    index_html = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* 1. 页面基础重置 */
        body, html {{
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            width: 100%;
            display: flex;
            justify-content: center; /* 页面整体居中 */
        }}

        /* 2. 外部容器：垂直排列幻灯片 */
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0px 0;
            gap: 1px; /* 强制页面之间留出物理间距，绝不重叠 */
        }}

        /* 3. 页面隔离层：核心“笼子” */
        .slide-frame {{
            position: relative;
            width: 1280px;  /* PPT 原始宽度 */
            height: 720px; /* PPT 原始高度 */
            overflow: hidden; /* 强制裁剪任何溢出的内容[cite: 10, 11] */
            background: #fff;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
            border-radius: 4px;
            /* 确保缩放时以左上角为基准，避免位移 */
            transform-origin: top center;
        }}

        /* 4. iframe 强制铺满且禁止交互溢出 */
        iframe {{
            width: 100%;
            height: 100%;
            border: none;
            display: block; /* 消除行内元素底部的像素间隙[cite: 10] */
            pointer-events: auto; /* 保证内部图表可以点击 */
        }}
    </style>
</head>
<body>

<div class="container" id="report-container">
{iframes_html}
</div>


<script>
    /**
     * 自动缩放脚本：
     * 解决 iframe 缩放后在文档流中留下的“空白占位”问题。
     */
    function adjustScale() {{
    const frames = document.querySelectorAll('.slide-frame');
    const screenWidth = window.innerWidth * 0.98;

    frames.forEach(frame => {{
        const scale = Math.min(screenWidth / 1280, 1);
        frame.style.transform = `scale(${{scale}})`;

        // 计算缩放后减少的高度
        const originalHeight = 720;
        const scaledHeight = originalHeight * scale;
        
        // 这里的 10 是你想要的页面之间的实际视觉间距
        const desiredGap = 2; 
        
        // 核心公式：通过负 margin 顶上去，消除缩放留白[cite: 10]
        // 计算公式：-(原始高度 - 缩放后高度) + 想要保留的缝隙
        const offset = -(originalHeight - scaledHeight) + desiredGap;
        frame.style.marginBottom = `${{offset}}px`;
    }});
}}

    // 初始化与窗口大小改变时触发
    window.addEventListener('resize', adjustScale);
    window.addEventListener('load', adjustScale);
</script>

</body>
</html>"""

    index_path = os.path.join(out_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"  ✓ index.html (入口文件)")

    print(f"\n✅ 完成！输出目录：{out_dir}")
    print("   打开 index.html，向下滚动依次浏览7页。")


if __name__ == '__main__':
    main()