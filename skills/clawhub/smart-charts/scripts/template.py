"""HTML 模板生成器。将 ECharts option 转为独立的交互式 HTML 文件。"""

import json
import re
import html as html_module
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime


ECHARTS_VERSION = '5.4.3'
ECHARTS_WORDCLOUD_VERSION = '2.1.0'
# ECharts JS 内联到 HTML（避免 file:// 跨域加载失败，确保离线自包含）
_STATIC_DIR = Path(__file__).resolve().parent.parent / 'assets'
ECHARTS_LOCAL = _STATIC_DIR / 'echarts.min.js'
ECHARTS_WORDCLOUD_LOCAL = _STATIC_DIR / 'echarts-wordcloud.min.js'

# 缓存 ECharts JS 内容（避免每次生成图表都读文件）
_ECHARTS_JS_CACHE: Optional[str] = None
_WORDCLOUD_JS_CACHE: Optional[str] = None

# tooltip formatter 占位符：json.dumps 会将其序列化为字符串，
# _save_html 中再将带引号的占位符替换为真正的 JS 函数，避免 ECharts 把函数当纯文本渲染。
TOOLTIP_FORMATTER_AXIS = '__TOOLTIP_FORMATTER_AXIS__'

# bubble symbolSize 占位符：同上，json.dumps 会把 JS 函数序列化为字符串，
# 需在 _save_html 中替换为真正的 JS 函数，否则 ECharts 无法执行导致气泡不渲染。
BUBBLE_SYMBOLSIZE_PLACEHOLDER = '__BUBBLE_SYMBOLSIZE__'

# bubble tooltip formatter 占位符：ECharts 字符串模板不支持 {c[0]} 数组索引，
# 必须使用函数 formatter 才能正确显示数组数据的各字段值。
BUBBLE_TOOLTIP_PLACEHOLDER = '__BUBBLE_TOOLTIP__'


def _load_echarts_js() -> str:
    """读取并缓存 ECharts JS 内容，用于内联到 HTML。"""
    global _ECHARTS_JS_CACHE
    if _ECHARTS_JS_CACHE is None:
        _ECHARTS_JS_CACHE = ECHARTS_LOCAL.read_text(encoding='utf-8')
    return _ECHARTS_JS_CACHE


def _load_wordcloud_js() -> str:
    """读取并缓存 wordcloud 插件 JS 内容，用于内联到 HTML。"""
    global _WORDCLOUD_JS_CACHE
    if _WORDCLOUD_JS_CACHE is None:
        _WORDCLOUD_JS_CACHE = ECHARTS_WORDCLOUD_LOCAL.read_text(encoding='utf-8')
    return _WORDCLOUD_JS_CACHE


class HTMLTemplateMixin:
    """HTML 模板生成方法，由 ChartGenerator 继承。"""

    def _tooltip_formatter_axis_js(self, texts: Dict[str, str]) -> str:
        no_data = texts['tooltip_no_data']
        return (
            "function(params) {\n"
            "                var res = params[0].axisValue + '<br/>';\n"
            "                params.forEach(function(p) {\n"
            f"                    var val = (p.value === null || p.value === undefined || p.value === 'NaN' || p.value === 'Infinity') ? '{no_data}' : p.value;\n"
            "                    res += p.marker + p.seriesName + ': ' + val + '<br/>';\n"
            "                });\n"
            "                return res;\n"
            "            }"
        )

    def _save_html(self, option: Dict, title: str, width: int, height: int, chart_type: str = '', data_points: int = 0, texts: Dict[str, str] = None) -> Path:
        import hashlib
        self._ensure_output_dir()
        content_str = json.dumps(option, ensure_ascii=False, sort_keys=True)
        suffix = hashlib.md5(content_str.encode()).hexdigest()[:6]
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)[:30]
        filename = f"{safe_title}_{suffix}.html"
        path = self.output_dir / filename

        # XSS 防护：转义所有用户输入插入 HTML 的部分
        esc_title = html_module.escape(title)
        esc_safe_title = html_module.escape(safe_title)

        option_json = json.dumps(option, ensure_ascii=False, indent=2, allow_nan=False)

        # 将占位符字符串替换为真正的 JS 函数（去掉 json.dumps 添加的引号）
        formatter_js = self._tooltip_formatter_axis_js(texts)
        option_json = option_json.replace(
            f'"{self._TOOLTIP_FORMATTER_AXIS}"',
            formatter_js
        )

        # bubble symbolSize 占位符替换为真正的 JS 函数
        if self._bubble_symbolsize_js:
            option_json = option_json.replace(
                f'"{self._BUBBLE_SYMBOLSIZE_PLACEHOLDER}"',
                self._bubble_symbolsize_js
            )
            self._bubble_symbolsize_js = None

        # bubble tooltip formatter 占位符替换为真正的 JS 函数
        if self._bubble_tooltip_js:
            option_json = option_json.replace(
                f'"{self._BUBBLE_TOOLTIP_PLACEHOLDER}"',
                self._bubble_tooltip_js
            )
            self._bubble_tooltip_js = None

        # ECharts JS 内联到 HTML（避免 file:// 跨域加载失败，确保离线自包含）
        echarts_js = _load_echarts_js()

        # wordcloud 插件（仅 wordcloud 图表类型需要，同样内联）
        wordcloud_script = ''
        if chart_type == 'wordcloud':
            wordcloud_js = _load_wordcloud_js()
            wordcloud_script = f'<script>{wordcloud_js}</script>'

        # 宽高比，用于响应式高度计算
        aspect_ratio = width / height if height > 0 else 16 / 9

        # 数据点过多时：容器加横向滚动兜底 + 显示提示
        scroll_hint_html = ''
        if data_points and data_points > self.DATAZOOM_THRESHOLD:
            min_chart_width = data_points * self.MIN_PX_PER_POINT
            chart_style = (
                f"width: 100%; aspect-ratio: {aspect_ratio:.4f}; min-height: 300px; "
                f"min-width: {min_chart_width}px;"
            )
            wrapper_style = "width: 100%; position: relative; overflow-x: auto; overflow-y: hidden;"
            scroll_hint_html = f'<div class="scroll-hint">{html_module.escape(texts["scroll_hint"])}</div>'
        else:
            chart_style = f"width: 100%; aspect-ratio: {aspect_ratio:.4f}; min-height: 300px;"
            wrapper_style = "width: 100%; position: relative;"

        btn_save = html_module.escape(texts['btn_save'])
        btn_fullscreen = html_module.escape(texts['btn_fullscreen'])
        footer_text = html_module.escape(texts['footer'])
        edit_hint = html_module.escape(texts['edit_hint'])
        title_updated_msg = html_module.escape(texts['title_updated'])
        html_lang = 'zh-CN' if texts is self._TEXTS['zh'] else 'en'

        html = f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc_title}</title>
<script>{echarts_js}</script>
{wordcloud_script}
<style>
* {{ box-sizing: border-box; }}
body {{ font-family: 'Microsoft YaHei', 'PingFang SC', 'Hiragino Sans GB', 'Noto Sans CJK SC', sans-serif; margin: 0; padding: 20px; background: #f8f9fa; }}
.container {{ max-width: {width}px; width: 100%; margin: 0 auto; background: #fff; padding: 30px;
             border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
.header {{ text-align: center; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 2px solid #4CAF50; }}
.title {{ font-size: clamp(16px, 4vw, 24px); font-weight: 700; color: #2E7D32; margin: 0;
          cursor: text; outline: none; border-bottom: 2px dashed transparent; transition: border-color 0.2s; }}
.title:hover {{ border-bottom-color: #ccc; }}
.title:focus {{ border-bottom-color: #4CAF50; }}
.edit-hint {{ font-size: 11px; color: #bbb; margin-top: 4px; transition: color 0.3s; }}
.subtitle {{ font-size: 12px; color: #999; }}
.chart-wrapper {{ {wrapper_style} }}
.chart {{ {chart_style} }}
.scroll-hint {{ text-align: center; font-size: 12px; color: #888; margin: 8px 0; }}
.controls {{ text-align: center; margin: 15px 0; }}
.btn {{ display: inline-block; padding: 6px 16px; background: #4CAF50; color: #fff;
        border: none; border-radius: 4px; cursor: pointer; font-size: 13px; margin: 0 4px; }}
.btn:hover {{ background: #45a049; }}
.footer {{ margin-top: 25px; padding-top: 15px; border-top: 1px solid #eee; text-align: center;
          font-size: 11px; color: #aaa; }}
@media (max-width: 640px) {{
  .container {{ padding: 15px; }}
  .chart {{ min-height: 250px; }}
}}
@media print {{ .controls {{ display: none; }} .container {{ box-shadow: none; }} }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1 class="title" contenteditable="true" title="{edit_hint}">{esc_title}</h1>
    <div class="edit-hint">{edit_hint}</div>
    <div class="subtitle">Smart Charts &middot; {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
  </div>
  <div class="controls">
    <button class="btn" onclick="saveAsImage()">{btn_save}</button>
    <button class="btn" onclick="toggleFull()">{btn_fullscreen}</button>
  </div>
  {scroll_hint_html}
  <div class="chart-wrapper">
    <div id="chart" class="chart"></div>
  </div>
  <div class="footer">{footer_text} &middot; ECharts 5.4.3</div>
</div>
<script>
var chartDom = document.getElementById('chart');
var chart = echarts.init(chartDom);
chart.setOption({option_json});
window.addEventListener('resize', function() {{ chart.resize(); }});
new ResizeObserver(function() {{ chart.resize(); }}).observe(chartDom);
// {texts['comment_download_name']}
var currentDownloadName = '{esc_safe_title}';
function saveAsImage() {{
  var url = chart.getDataURL({{ type: 'png', pixelRatio: 2, backgroundColor: '#fff' }});
  var a = document.createElement('a'); a.href = url; a.download = currentDownloadName + '.png'; a.click();
}}
function toggleFull() {{
  var el = document.getElementById('chart');
  if (!document.fullscreenElement) el.requestFullscreen();
  else document.exitFullscreen();
}}
// {texts['comment_title_edit']}
// {texts['comment_title_sync']}
var titleEl = document.querySelector('.title');
var editHintEl = document.querySelector('.edit-hint');
var originalTitle = titleEl.textContent;
titleEl.addEventListener('keydown', function(e) {{
  if (e.key === 'Enter') {{ e.preventDefault(); titleEl.blur(); }}
  if (e.key === 'Escape') {{ titleEl.textContent = originalTitle; titleEl.blur(); }}
}});
titleEl.addEventListener('blur', function() {{
  var newTitle = titleEl.textContent.trim();
  if (newTitle && newTitle !== originalTitle) {{
    originalTitle = newTitle;
    chart.setOption({{ title: {{ text: newTitle }} }});
    currentDownloadName = newTitle.replace(/[\\\\/:*?"<>|]/g, '_').substring(0, 30);
    editHintEl.textContent = '{title_updated_msg}';
    editHintEl.style.color = '#4CAF50';
    setTimeout(function() {{ editHintEl.style.color = ''; }}, 3000);
  }} else {{
    titleEl.textContent = originalTitle;
  }}
}});
</script>
</body>
</html>"""
        path.write_text(html, encoding='utf-8')
        return path
