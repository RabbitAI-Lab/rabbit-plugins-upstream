# -*- coding: utf-8 -*-
"""全国 33 城跨城对比大屏生成器（2026-08-11）
基于：27城状态报告 + skill 最新分类（杭州 E→B+）+ 深润川/晟悦/悦海棠 案例
输出：output_cross/全国33城房源采集对比大屏.html
"""
import json
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / "output_cross"

# ---------- 主数据：33 城（含最新分类更新） ----------
# cls: A=纯匿名可自动化 B=项目级可采待本机 C=差环境 D=需小程序/登录 E=反爬阻断
CITIES = [
    # A 类 10 城
    {"城市": "深圳", "区域": "大湾区", "cls": "A", "套数": 616, "样本": "晟悦家园", "入口": "fdc.zjj.sz.gov.cn", "状态": "已跑通", "备注": "每日自动化；8 Sheet 报告+交互看板", "下一步": "维持"},
    {"城市": "成都", "区域": "西南", "cls": "A", "套数": 300, "样本": "青江名邸", "入口": "blmp.cdzjryb.com", "状态": "已跑通", "备注": "infoDetail→roompricezjw 公开页", "下一步": "可复用脚本扩采"},
    {"城市": "佛山", "区域": "大湾区", "cls": "A", "套数": 2138, "样本": "晓棠名邸/观颂苑", "入口": "fsfc.fszj.foshan.gov.cn", "状态": "已跑通", "备注": "整栋表格接口；顶部统计为占位符", "下一步": "扩大样本"},
    {"城市": "珠海", "区域": "大湾区", "cls": "A", "套数": 112, "样本": "中珠领域花苑", "入口": "zjj.zhuhai.gov.cn", "状态": "已跑通", "备注": "公示文章 HTML 表；缺销售状态", "下一步": "关联预销售专网"},
    {"城市": "南京", "区域": "长三角", "cls": "A", "套数": 312, "样本": "3项目", "入口": "www.njhouse.com.cn", "状态": "已跑通", "备注": "纯 requests 匿名 POST", "下一步": "全量扩采"},
    {"城市": "重庆", "区域": "西南", "cls": "A", "套数": 55, "样本": "4楼栋", "入口": "www.cq315house.com", "状态": "已跑通", "备注": "ASP.NET PageMethod", "下一步": "全量扩采"},
    {"城市": "苏州", "区域": "长三角", "cls": "A", "套数": 5651, "样本": "30批次", "入口": "fg.suzhou.gov.cn", "状态": "已跑通", "备注": "发改委公示表+PDF；2019-2022历史存量", "下一步": "声明口径"},
    {"城市": "西安", "区域": "西北", "cls": "A", "套数": 2146, "样本": "多项目", "入口": "zjj.xa.gov.cn", "状态": "已跑通", "备注": "三层 GET 匿名；备案价下放区县", "下一步": "按区全量"},
    {"城市": "武汉", "区域": "华中", "cls": "A", "套数": 331, "样本": "保利城四期", "入口": "spfxm.whfgxx.org.cn:8083", "状态": "已跑通", "备注": "五层 GET；GB2312 编码坑", "下一步": "全量扩采"},
    {"城市": "郑州", "区域": "华中", "cls": "A", "套数": 123, "样本": "3证3栋", "入口": "218.28.223.8", "状态": "已跑通", "备注": "Playwright 渲染+requests 逐套；仅单价无面积", "下一步": "全量扩采"},
    # B 类 2 城（杭州今日升级）
    {"城市": "杭州", "区域": "长三角", "cls": "B", "套数": 463, "样本": "悦海棠轩", "入口": "www.tmsf.com", "状态": "项目级可采", "备注": "阿里云WAF已破；顶象拦逐套；今日 E→B+", "下一步": "本机住宅IP过顶象→固化采集器"},
    {"城市": "无锡", "区域": "长三角", "cls": "B", "套数": 59, "样本": "诗语溪园", "入口": "pub.wxhouse.com", "状态": "方法已验证", "备注": "iframe 直链；沙箱IP被拉黑", "下一步": "本机跑 extract_wuxi.py"},
    # C 类 1 城
    {"城市": "宁波", "区域": "长三角", "cls": "C", "套数": 11, "样本": "东宸誉府", "入口": "newhouse.cnnbfdc.com", "状态": "价格受阻", "备注": "单价以 PNG 渲染（html2img）", "下一步": "本机装 Tesseract 跑 OCR"},
    # D 类 12 城
    {"城市": "合肥", "区域": "长三角", "cls": "D", "套数": 0, "样本": "—", "入口": "drc.hefei.gov.cn", "状态": "需小程序", "备注": "逐套价仅微信「合肥住房」小程序", "下一步": "不纳入持续"},
    {"城市": "东莞", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "莞e住建小程序", "状态": "需小程序", "备注": "一房一价迁移至小程序", "下一步": "不纳入持续"},
    {"城市": "肇庆", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "粤安居", "状态": "需登录", "备注": "逐套在企业登录后", "下一步": "不纳入持续"},
    {"城市": "中山", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "jsj.zs.gov.cn", "状态": "备案价不公开", "备注": "备案价仅现场公示/依申请", "下一步": "不纳入持续"},
    {"城市": "清远", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "粤安居", "状态": "需登录", "备注": "粤安居 Vue SPA 空响应", "下一步": "不纳入持续"},
    {"城市": "潮州", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "粤安居", "状态": "需登录", "备注": "粤安居 Vue SPA 空响应", "下一步": "不纳入持续"},
    {"城市": "茂名", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "粤安居", "状态": "需登录", "备注": "粤安居 Vue SPA 空响应", "下一步": "不纳入持续"},
    {"城市": "惠州", "区域": "大湾区", "cls": "D", "套数": 0, "样本": "—", "入口": "粤省事小程序", "状态": "需小程序", "备注": "逐套备案价待实测", "下一步": "不纳入持续"},
    {"城市": "廊坊", "区域": "京津冀", "cls": "D", "套数": 0, "样本": "—", "入口": "房源超市小程序", "状态": "需小程序", "备注": "网页仅合同备案查询", "下一步": "不纳入持续"},
    {"城市": "天津", "区域": "京津冀", "cls": "D", "套数": 0, "样本": "—", "入口": "证载二维码扫码", "状态": "需扫码", "备注": "微信扫码查逐套", "下一步": "不纳入持续"},
    {"城市": "贵阳", "区域": "西南", "cls": "D", "套数": 0, "样本": "—", "入口": "yfyj.gyfc.net", "状态": "需注册登录", "备注": "楼盘表需注册", "下一步": "不纳入持续"},
    {"城市": "济南", "区域": "华东", "cls": "D", "套数": 0, "样本": "观山隐秀(证级)", "入口": "zwfw.jinan.gov.cn", "状态": "证级可采", "备注": "无官方逐套制度；证级API可采", "下一步": "济南模板复用"},
    # E 类 8 城
    {"城市": "北京", "区域": "京津冀", "cls": "E", "套数": 0, "样本": "—", "入口": "zjw.beijing.gov.cn", "状态": "未深入", "备注": "待定位销控表子系统", "下一步": "按探测SOP定性"},
    {"城市": "广州", "区域": "大湾区", "cls": "E", "套数": 0, "样本": "—", "入口": "zfcj.gz.gov.cn", "状态": "未深入", "备注": "阳光家缘待实测", "下一步": "按探测SOP定性"},
    {"城市": "石家庄", "区域": "京津冀", "cls": "E", "套数": 0, "样本": "—", "入口": "zjj.sjz.gov.cn", "状态": "未深入", "备注": "楼盘销售状态可查", "下一步": "按探测SOP定性"},
    {"城市": "常州", "区域": "长三角", "cls": "E", "套数": 0, "样本": "—", "入口": "zfhcxjsj.changzhou.gov.cn", "状态": "未深入", "备注": "备案公示待实测", "下一步": "按探测SOP定性"},
    {"城市": "保定", "区域": "京津冀", "cls": "E", "套数": 0, "样本": "—", "入口": "保定房产信息网", "状态": "未深入", "备注": "销售状态可查", "下一步": "按探测SOP定性"},
    {"城市": "江门", "区域": "大湾区", "cls": "E", "套数": 0, "样本": "—", "入口": "jmzjj.jiangmen.cn:8085", "状态": "瑞数412", "备注": "瑞数五秒盾，stealth 失败", "下一步": "同上海瑞数SOP"},
    {"城市": "上海", "区域": "长三角", "cls": "E", "套数": 0, "样本": "—", "入口": "www.fangdi.com.cn", "状态": "瑞数412", "备注": "三轮攻坚失败；证级源 fgwapp 可采", "下一步": "本机headed+独立IP或JS逆向"},
    {"城市": "南通", "区域": "长三角", "cls": "E", "套数": 0, "样本": "—", "入口": "域名被出售", "状态": "不可达", "备注": "ntfdc.com 被出售劫持", "下一步": "放弃"},
]

CLS_INFO = {
    "A": {"name": "A · 纯匿名可自动化", "color": "#EAF3DE", "stroke": "#3B6D11", "text": "#173404"},
    "B": {"name": "B · 项目级可采·待本机", "color": "#E6F1FB", "stroke": "#185FA5", "text": "#042C53"},
    "C": {"name": "C · 差一次性环境", "color": "#FAEEDA", "stroke": "#BA7517", "text": "#412402"},
    "D": {"name": "D · 需小程序/登录", "color": "#FAECE7", "stroke": "#993C1D", "text": "#4A1B0C"},
    "E": {"name": "E · 反爬阻断", "color": "#FCEBEB", "stroke": "#A32D2D", "text": "#501313"},
}

cities_json = json.dumps(CITIES, ensure_ascii=False)
cls_info_json = json.dumps(CLS_INFO, ensure_ascii=False)
total_cities = len(CITIES)
a_cnt = sum(1 for c in CITIES if c["cls"] == "A")
b_cnt = sum(1 for c in CITIES if c["cls"] == "B")
c_cnt = sum(1 for c in CITIES if c["cls"] == "C")
d_cnt = sum(1 for c in CITIES if c["cls"] == "D")
e_cnt = sum(1 for c in CITIES if c["cls"] == "E")
total_units = sum(c["套数"] for c in CITIES)

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全国 33 城房源备案价采集对比大屏</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1"></script>
<style>
:root {{
    --bg: #f5f6f8; --card: #ffffff; --text: #1f2937; --muted: #6b7280;
    --pos: #1D9E75; --neg: #D85A30; --radius: 10px; --gap: 14px;
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system,'Segoe UI','Microsoft YaHei',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }}
.wrap {{ max-width:1440px; margin:0 auto; padding:16px; }}
.header {{ background:linear-gradient(135deg,#0f2a4a,#10345e); color:#fff; padding:22px 28px; border-radius:var(--radius); margin-bottom:var(--gap); }}
.header h1 {{ font-size:22px; font-weight:600; }}
.header .sub {{ font-size:12.5px; opacity:.8; margin-top:4px; }}
.kpi-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:var(--gap); margin-bottom:var(--gap); }}
.kpi {{ background:var(--card); border-radius:var(--radius); padding:14px 18px; box-shadow:0 1px 2px rgba(0,0,0,.06); }}
.kpi .l {{ font-size:12px; color:var(--muted); }}
.kpi .v {{ font-size:24px; font-weight:700; margin-top:2px; }}
.kpi .d {{ font-size:12px; color:var(--muted); margin-top:2px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(400px,1fr)); gap:var(--gap); margin-bottom:var(--gap); }}
.card {{ background:var(--card); border-radius:var(--radius); padding:16px 20px; box-shadow:0 1px 2px rgba(0,0,0,.06); }}
.card h3 {{ font-size:14px; font-weight:600; margin-bottom:12px; color:var(--text); }}
.card canvas {{ max-height:300px; }}
.table-sec {{ background:var(--card); border-radius:var(--radius); padding:16px 20px; box-shadow:0 1px 2px rgba(0,0,0,.06); overflow-x:auto; }}
.table-sec h3 {{ font-size:14px; font-weight:600; margin-bottom:12px; }}
.filters {{ display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-bottom:var(--gap); }}
.filters select, .filters input {{ padding:6px 10px; border:1px solid #cbd5e1; border-radius:6px; background:#fff; color:var(--text); font-size:13px; }}
.filters label {{ font-size:12px; color:var(--muted); }}
table.data {{ width:100%; border-collapse:collapse; font-size:12.5px; }}
table.data th {{ text-align:left; padding:8px 10px; border-bottom:2px solid #e2e8f0; color:var(--muted); font-weight:600; font-size:12px; white-space:nowrap; cursor:pointer; user-select:none; }}
table.data td {{ padding:7px 10px; border-bottom:1px solid #f1f2f4; white-space:nowrap; }}
table.data tr:hover td {{ background:#f8fafc; }}
.cls-badge {{ display:inline-block; padding:2px 10px; border-radius:10px; font-size:11.5px; font-weight:600; }}
.pager {{ display:flex; gap:10px; align-items:center; margin-top:12px; font-size:13px; color:var(--muted); }}
.pager button {{ padding:4px 12px; border:1px solid #cbd5e1; border-radius:6px; background:#fff; cursor:pointer; font-size:13px; }}
.footer {{ font-size:12px; color:var(--muted); text-align:center; padding:14px 0 6px; }}
@media(max-width:800px){{ .grid{{grid-template-columns:1fr;}} .kpi-row{{grid-template-columns:repeat(2,1fr);}} }}
</style>
</head>
<body>
<div class="wrap">
  <div class="header">
    <h1>全国 33 城 · 房源备案价采集对比大屏</h1>
    <div class="sub">数据基准：2026-08-11 跨城市采集收官 ｜ A10 + B+2 + C1 + D12 + E8 ｜ 已采房源 ≈{total_units:,} 套（A 类为实测样本，苏州 5,651 / 西安 2,146 领跑）</div>
  </div>

  <div class="kpi-row">
    <div class="kpi"><div class="l">覆盖城市</div><div class="v">{total_cities} 城</div><div class="d">33 城全定性</div></div>
    <div class="kpi"><div class="l">纯匿名可自动化</div><div class="v">{a_cnt} 城</div><div class="d">已固化采集器</div></div>
    <div class="kpi"><div class="l">待本机环境</div><div class="v">{b_cnt + c_cnt} 城</div><div class="d">杭州/无锡/宁波</div></div>
    <div class="kpi"><div class="l">需小程序/登录</div><div class="v">{d_cnt} 城</div><div class="d">不纳入持续</div></div>
    <div class="kpi"><div class="l">反爬阻断</div><div class="v">{e_cnt} 城</div><div class="d">瑞数/不可达</div></div>
    <div class="kpi"><div class="l">已采房源</div><div class="v">≈{total_units:,} 套</div><div class="d">A 类实测样本</div></div>
  </div>

  <div class="grid">
    <div class="card"><h3>城市分类分布</h3><canvas id="c-cls"></canvas></div>
    <div class="card"><h3>各城采集套数（A/B 类）</h3><canvas id="c-units"></canvas></div>
  </div>

  <div class="filters">
    <label>分类</label><select id="f-cls" onchange="dash.apply()"><option value="all">全部分类</option><option value="A">A · 可自动化</option><option value="B">B · 待本机</option><option value="C">C · 差环境</option><option value="D">D · 需小程序</option><option value="E">E · 反爬</option></select>
    <label>区域</label><select id="f-region" onchange="dash.apply()"><option value="all">全部区域</option></select>
    <label>关键词</label><input id="f-kw" placeholder="搜城市/入口/备注" oninput="dash.apply()" style="width:180px;">
  </div>

  <div class="table-sec">
    <h3>33 城明细（点击表头排序）</h3>
    <table class="data" id="t-main"><thead></thead><tbody></tbody></table>
    <div class="pager"><button onclick="dash.prev()">‹ 上一页</button><span id="pg-info"></span><button onclick="dash.next()">下一页 ›</button></div>
  </div>

  <div class="footer">全国 33 城房源备案价采集对比大屏 ｜ 生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')} ｜ 数据来源：各地住建局/房产交易官方平台实测 ｜ 采集套数为实测样本量，非城市全量 ｜ 来源标注：[官方平台实测 2026-08-11]</div>
</div>

<script>
const CITIES = {cities_json};
const CLS = {cls_info_json};
const C = ['#3B6D11','#185FA5','#BA7517','#993C1D','#A32D2D'];

function fmt(v) {{ return Number(v||0).toLocaleString('zh-CN'); }}
class Dashboard {{
  constructor() {{
    this.raw = CITIES; this.f = {{cls:'all', region:'all', kw:''}};
    this.page = 0; this.pageSize = 20; this.sort = null; this.sortDir = 'asc';
    this.populateRegion();
    this.initCharts();
    this.apply();
  }}
  populateRegion() {{
    const rs = [...new Set(this.raw.map(c=>c['区域']))].sort();
    rs.forEach(r=>{{const o=document.createElement('option'); o.value=r; o.textContent=r; document.getElementById('f-region').appendChild(o);}});
  }}
  get filtered() {{
    const kw = this.f.kw.toLowerCase();
    return this.raw.filter(c =>
      (this.f.cls==='all'||c['cls']===this.f.cls) &&
      (this.f.region==='all'||c['区域']===this.f.region) &&
      (!kw || (c['城市']+c['入口']+c['备注']+c['样本']).toLowerCase().includes(kw)));
  }}
  apply() {{
    this.f.cls = document.getElementById('f-cls').value;
    this.f.region = document.getElementById('f-region').value;
    this.f.kw = document.getElementById('f-kw').value;
    this.page = 0;
    this.updateCharts(); this.renderTable();
  }}
  initCharts() {{
    this.clsChart = new Chart(document.getElementById('c-cls'), {{type:'doughnut', data:{{labels:[],datasets:[{{data:[],backgroundColor:['#3B6D11','#185FA5','#BA7517','#993C1D','#A32D2D'],borderColor:'#fff',borderWidth:2}}]}}, options:{{responsive:true,maintainAspectRatio:false,cutout:'55%',plugins:{{legend:{{position:'right'}}}}}}}});
    this.unitsChart = new Chart(document.getElementById('c-units'), {{type:'bar', data:{{labels:[],datasets:[{{data:[],backgroundColor:'#185FA5',borderWidth:1}}]}}, options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true,ticks:{{callback:v=>fmt(v)}}}}}}}}}});
  }}
  updateCharts() {{
    const d = this.filtered;
    const clsCnt = {{}};
    d.forEach(c=>clsCnt[c['cls']]=(clsCnt[c['cls']]||0)+1);
    const keys = Object.keys(clsCnt).sort();
    this.clsChart.data.labels = keys.map(k=>CLS[k].name);
    this.clsChart.data.datasets[0].data = keys.map(k=>clsCnt[k]);
    this.clsChart.data.datasets[0].backgroundColor = keys.map(k=>({{A:'#3B6D11',B:'#185FA5',C:'#BA7517',D:'#993C1D',E:'#A32D2D'}}[k]));
    this.clsChart.update('none');
    const withUnits = d.filter(c=>c['套数']>0).sort((a,b)=>b['套数']-a['套数']).slice(0,15);
    this.unitsChart.data.labels = withUnits.map(c=>c['城市']);
    this.unitsChart.data.datasets[0].data = withUnits.map(c=>c['套数']);
    this.unitsChart.update('none');
  }}
  renderTable() {{
    let d = [...this.filtered];
    if (this.sort) {{
      d.sort((a,b)=>{{const av=a[this.sort], bv=b[this.sort]; if(av==null)return 1; if(bv==null)return -1;
        return this.sortDir==='asc'?(av<bv?-1:av>bv?1:0):(av<bv?1:av>bv?-1:0);}});
    }}
    const cols = ['城市','区域','cls','状态','套数','样本','入口','备注','下一步'];
    const total = d.length, pages = Math.max(1, Math.ceil(total/this.pageSize));
    this.page = Math.min(this.page, pages-1);
    const start = this.page*this.pageSize, end = Math.min(start+this.pageSize, total);
    const pageData = d.slice(start, end);
    const ths = cols.map(c=>`<th onclick="dash.sortBy('${{c}}')">${{c==='cls'?'分类':c}}${{this.sort===c?(this.sortDir==='asc'?' ▲':' ▼'):''}}</th>`).join('');
    document.querySelector('#t-main thead').innerHTML = `<tr>${{ths}}</tr>`;
    document.querySelector('#t-main tbody').innerHTML = pageData.map(c=>{{
      const ci = CLS[c['cls']]||{{}};
      return `<tr><td style="font-weight:600;">${{c['城市']}}</td><td>${{c['区域']}}</td><td><span class="cls-badge" style="background:${{ci.color}};color:${{ci.text}};border:1px solid ${{ci.stroke}};">${{c['cls']}}</span></td><td>${{c['状态']}}</td><td>${{c['套数']>0?fmt(c['套数']):'—'}}</td><td>${{c['样本']}}</td><td style="color:var(--muted);font-size:11.5px;">${{c['入口']}}</td><td>${{c['备注']}}</td><td style="color:#185FA5;">${{c['下一步']}}</td></tr>`;
    }}).join('');
    document.getElementById('pg-info').textContent = `第 ${{this.page+1}}/${{pages}} 页 · 共 ${{total}} 城`;
  }}
  sortBy(c) {{ if(this.sort===c) this.sortDir=this.sortDir==='asc'?'desc':'asc'; else {{this.sort=c;this.sortDir='asc';}} this.renderTable(); }}
  prev() {{ if(this.page>0){{this.page--;this.renderTable();}} }}
  next() {{ const pages=Math.max(1,Math.ceil(this.filtered.length/this.pageSize)); if(this.page<pages-1){{this.page++;this.renderTable();}} }}
}}
const dash = new Dashboard();
</script>
</body>
</html>"""

out = OUT / "全国33城房源采集对比大屏.html"
out.write_text(html, encoding="utf-8")
print(f"已生成: {out.name} ({out.stat().st_size/1024:.0f} KB)")
print(f"统计: A={a_cnt} B={b_cnt} C={c_cnt} D={d_cnt} E={e_cnt} 总套数={total_units}")
