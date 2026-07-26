# HTML报告模板规范

## 1. 完整CSS（基于紫蓝主题，替换 :root 变量即可换主题）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{业务名称} · 经营诊断报告</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;600&family=Noto+Sans+SC:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

/* ── 色彩变量（替换此块即可换主题）── */
:root{
  --bg:#F5F3FA; --s1:#FFFFFF; --s2:#EDE8F5; --bd:#D8D0EC;
  --c1:#7B5EA7; --c2:#5B8DD9; --c3:#9B7DC7; --c4:#A390C8;
  --red:#B04848; --t:#1A1525; --mu:#7A6E90; --mu2:#C8C0DC; --tx:#2D2640;
}

*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--t);font-family:'Noto Sans SC',sans-serif;
     font-size:13px;line-height:1.7;min-height:100vh;
     -webkit-font-smoothing:antialiased;letter-spacing:.01em}

/* HERO */
.hero{padding:28px 20px 22px;
      background:linear-gradient(135deg,#5B3A8A 0%,#6B4A9A 40%,#4A3A7A 100%);
      border-bottom:3px solid #3D2A6A;position:relative;overflow:hidden}
.hero::after{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 80% 40%,rgba(180,160,255,.15),transparent 60%);
  pointer-events:none}
.hi{position:relative;z-index:1}
.hl{font-size:10px;letter-spacing:.18em;color:rgba(255,255,255,.75);
    text-transform:uppercase;margin-bottom:8px}
h1{font-family:'Noto Serif SC',serif;font-size:26px;font-weight:600;
   color:#FFF;line-height:1.2;text-shadow:0 2px 8px rgba(0,0,0,.2)}
h1 em{font-style:normal;color:#CDB8F5}
.hsub{font-size:11px;color:rgba(255,255,255,.65);margin-top:6px;
      line-height:1.65;font-weight:300}
.kpis{display:flex;gap:14px;margin-top:14px;flex-wrap:wrap}
.kpi{display:flex;flex-direction:column;gap:2px}
.kv{font-family:'DM Mono',monospace;font-size:16px;font-weight:500;color:#FFF;
    text-shadow:0 1px 4px rgba(0,0,0,.25)}
.kv.dn{color:#FFD0D8}.kv.up{color:#C8E8FF}
.kl{font-size:10px;color:rgba(255,255,255,.72)}

/* TABS */
.tabs{display:flex;background:#4A3080;border-bottom:3px solid #35206A;
      padding:0 10px;overflow-x:auto;-webkit-overflow-scrolling:touch}
.tab{background:none;border:none;color:rgba(255,255,255,.55);
     font-family:'Noto Sans SC',sans-serif;font-size:12px;
     padding:11px 13px;cursor:pointer;border-bottom:2px solid transparent;
     white-space:nowrap;transition:all .15s}
.tab:hover{color:#FFF}.tab.on{color:#FFF;border-bottom-color:#CDB8F5;font-weight:500}

/* PAGES */
.pg{display:none;padding:22px 16px}.pg.on{display:block}
.pt{font-family:'Noto Serif SC',serif;font-size:18px;font-weight:600;
    color:#2D1A4A;margin-bottom:3px}
.ps{font-size:11px;color:var(--mu);margin-bottom:18px;line-height:1.6}

/* GRIDS — auto-fit，天然响应式 */
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-bottom:14px}
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:14px}
.full{grid-column:1/-1}

/* CARD */
.card{background:var(--s1);border:1px solid var(--bd);border-radius:10px;
      padding:18px;box-shadow:0 1px 4px rgba(90,50,150,.06)}
.ct{font-size:10px;font-weight:500;letter-spacing:.09em;color:#9A90B0;
    text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:7px}
.ct::before{content:'';display:inline-block;width:2px;height:10px;
            background:var(--c1);border-radius:2px;flex-shrink:0}
.ct.bl::before{background:var(--c2)}.ct.ye::before{background:#D4A040}
.ct.tl::before{background:var(--c4)}.ct.re::before{background:var(--red)}

/* STAT STRIP */
.strip{display:flex;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.st{flex:1;min-width:130px;background:var(--s1);border:1px solid var(--bd);
    border-radius:9px;padding:13px 15px;position:relative;overflow:hidden}
.st::after{content:'';position:absolute;top:0;left:0;right:0;
           height:2px;background:var(--c1);opacity:.7}
.st.bl::after{background:var(--c2)}.st.ye::after{background:#D4A040}
.st.tl::after{background:var(--c4)}.st.re::after{background:var(--red)}
.sv{font-family:'DM Mono',monospace;font-size:17px;font-weight:500;
    color:var(--t);margin-bottom:3px}
.sl{font-size:10px;color:var(--mu)}
.sd{font-size:10px;color:var(--red);margin-top:3px}.sd.pos{color:var(--c1)}

/* 5列对比卡（Tab2 整月对比，也可用于Tab5 KV）*/
/* 使用 auto-fit 而非 repeat(5,1fr)，手机上自动折为2列或1列 */
.cbox{background:var(--s2);border:1px solid var(--bd);border-radius:9px;
      padding:14px;text-align:center}
.cbox.c1{border-color:rgba(123,94,167,.45);border-top:3px solid var(--c1)}
.cbox.c2{border-color:rgba(91,141,217,.35);border-top:3px solid var(--c2)}
.cbox.c3{border-color:rgba(180,100,80,.35);border-top:3px solid var(--c2)}
.cbox.c4{border-color:rgba(176,72,72,.4);border-top:3px solid var(--red)}
.cbl{font-size:10px;letter-spacing:.07em;color:var(--mu);
     text-transform:uppercase;margin-bottom:7px}
.cbv{font-family:'DM Mono',monospace;font-size:20px;font-weight:500;
     color:var(--t);margin-bottom:2px}
.cbs{font-size:11px;color:var(--mu);margin-bottom:5px}
.cbr{margin-top:7px}
.cbn{font-family:'DM Mono',monospace;font-size:14px;color:var(--t);
     line-height:1;margin-bottom:1px}
.cbd{font-size:10px;color:var(--mu);margin-top:6px}
.cbd.dn{color:var(--red)}.cbd.pos{color:var(--c1)}
hr.sep{margin:7px 0;border:none;border-top:1px solid var(--bd)}

/* SECTION DIVIDER */
.sdiv{font-size:10px;font-weight:600;letter-spacing:.13em;text-transform:uppercase;
      color:var(--c1);margin:18px 0 12px;padding-bottom:5px;border-bottom:1px solid var(--bd)}

/* INSIGHT BOXES */
.ins{background:rgba(123,94,167,.05);border:1px solid rgba(123,94,167,.18);
     border-left:3px solid var(--c1);border-radius:8px;
     padding:12px 15px;font-size:12px;color:var(--tx);line-height:1.85;margin-bottom:12px}
.ins.bl{background:rgba(91,141,217,.05);border-color:rgba(91,141,217,.18);border-left-color:var(--c2)}
.ins.dn{background:rgba(176,72,72,.04);border-color:rgba(176,72,72,.18);border-left-color:var(--red)}
.ins.ye{background:rgba(212,160,64,.05);border-color:rgba(212,160,64,.2);border-left-color:#D4A040}
.it{font-size:10px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
    margin-bottom:5px;color:var(--c1)}
.ins.bl .it{color:var(--c2)}.ins.dn .it{color:var(--red)}.ins.ye .it{color:#C49030}
.ins strong{color:var(--c1);font-weight:600}
.ins.bl strong{color:var(--c2)}.ins.dn strong{color:var(--red)}.ins.ye strong{color:#C49030}
/* 绿色strong（Tab3 逆势增长框）*/
.ins-green strong{color:var(--c1)!important}

/* DATA TABLE */
.dtbl-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%}
.dtbl{width:100%;border-collapse:collapse;font-size:12px;min-width:360px}
.dtbl th{text-align:left;padding:8px 11px;background:var(--s2);color:var(--c1);
         font-size:10px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;
         border-bottom:1px solid var(--bd)}
.dtbl td{padding:9px 11px;border-bottom:1px solid rgba(100,80,150,.07);
         vertical-align:top;line-height:1.5}
.dtbl tr:nth-child(even) td{background:rgba(123,94,167,.03)}
.dtbl tr:hover td{background:rgba(91,141,217,.05)}
.dtbl td.dn{color:var(--red);font-weight:500}
.dtbl td.up{color:var(--c1);font-weight:500}
.dtbl td.bold{font-weight:600;color:var(--c1)}
.bdg{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600}
.bdg-r{background:rgba(176,72,72,.12);color:var(--red);border:1px solid rgba(176,72,72,.3)}
.bdg-p{background:rgba(123,94,167,.12);color:var(--c1);border:1px solid rgba(123,94,167,.3)}
.bdg-b{background:rgba(91,141,217,.12);color:var(--c2);border:1px solid rgba(91,141,217,.3)}

/* HEATMAP */
.hm-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%}
.hm{display:grid;grid-template-columns:52px repeat(14,minmax(26px,1fr));
    gap:2px;min-width:480px}
.hmh{text-align:center;font-size:9px;color:#9A8AB0;
     font-family:'DM Mono',monospace;padding:2px 0}
.hml{font-family:'DM Mono',monospace;font-size:10px;color:var(--mu);
     display:flex;align-items:center}
.hmc{border-radius:3px;padding:5px 2px;text-align:center;
     font-family:'DM Mono',monospace;font-size:10px;font-weight:600;
     cursor:default;transition:transform .1s}
.hmc:hover{transform:scale(1.1);z-index:5;position:relative}

/* STRATEGY CARDS */
.sps{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
     gap:12px;margin-bottom:14px}
.sc{background:var(--s1);border:1px solid var(--bd);border-radius:10px;
    padding:17px;position:relative;overflow:hidden;
    box-shadow:0 1px 4px rgba(90,50,150,.05)}
.sc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.sc.p0::before{background:linear-gradient(90deg,#A040A0,#7B5EA7)}
.sc.p1::before{background:linear-gradient(90deg,#5B8DD9,#7B5EA7)}
.sc.p1b::before{background:linear-gradient(90deg,#5B8DD9,#4070C0)}
.sc.p2::before{background:linear-gradient(90deg,#9B7DC7,#7B5EA7)}
.p0 .spt{color:#A040A0}.p1 .spt{color:var(--c1)}
.p1b .spt{color:var(--c2)}.p2 .spt{color:var(--c3)}
.p0 .sph{color:#A040A0}.p1 .sph{color:var(--c1)}
.p1b .sph{color:var(--c2)}.p2 .sph{color:var(--c3)}
.spt{font-size:10px;font-weight:600;letter-spacing:.08em;margin-bottom:7px}
.sph{font-family:'Noto Serif SC',serif;font-size:13px;font-weight:600;margin-bottom:8px}
.spb{font-size:12px;color:#5A5070;line-height:1.85}
.spb li{margin-left:14px;margin-bottom:3px}
.spb strong{color:var(--c1);font-weight:600}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin-top:9px}
.tag{font-size:10px;padding:2px 8px;border-radius:10px;
     background:var(--s2);color:var(--mu);border:1px solid var(--bd)}

/* KV ROW（Tab5 点评概览数字）*/
.kv-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
        gap:10px;margin-bottom:14px}
.kv-box{background:var(--s2);border:1px solid var(--bd);border-radius:9px;
        padding:16px;text-align:center}
.kvn{font-family:'DM Mono',monospace;font-size:24px;font-weight:400;
     color:var(--c1);margin-bottom:4px}
.kvl{font-size:11px;color:var(--mu)}

/* FUNNEL（Tab5 已开通点评场景）*/
.funnel{display:flex;flex-direction:column;gap:6px;margin:10px 0}
.f-row{display:flex;align-items:center;gap:10px}
.f-bar-wrap{flex:1;height:28px;background:var(--s2);border-radius:5px;overflow:hidden}
.f-bar{height:100%;border-radius:5px;display:flex;align-items:center;
       padding-left:10px;font-size:11px;font-weight:500;color:#FFF;
       font-family:'DM Mono',monospace;transition:width .6s ease}
.f-lbl{font-size:11px;color:var(--mu);min-width:60px;text-align:right}
.f-num{font-family:'DM Mono',monospace;font-size:12px;font-weight:500;
       color:var(--t);min-width:40px}

hr.dv{border:none;border-top:1px solid var(--bd);margin:18px 0}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--mu2);border-radius:3px}

/* ── MOBILE ── */
@media (max-width:600px){
  .hero{padding:16px 14px}
  h1{font-size:19px}
  .hsub{font-size:10px}
  .kpis{gap:10px}
  .kv{font-size:14px}
  .tabs{padding:0 4px}
  .tab{font-size:11px;padding:9px 9px}
  .pg{padding:14px 12px}
  .pt{font-size:15px}
  .ps{font-size:10px}
  .g2,.g3{grid-template-columns:1fr}
  .sps{grid-template-columns:1fr}
  .kv-row{grid-template-columns:1fr}
  .strip{flex-direction:column}
  .st{min-width:100%;flex:none}
  .card{padding:13px}
  .ins{font-size:11px;padding:10px 12px}
  .dtbl{font-size:11px}
  .dtbl th,.dtbl td{padding:6px 8px}
  .hm{grid-template-columns:40px repeat(14,minmax(22px,1fr))}
  .hmc{font-size:8.5px;padding:4px 1px}
  .cbv{font-size:17px}
  .kvn{font-size:20px}
  .sph{font-size:12px}
  .spb{font-size:11px}
  hr.dv{margin:12px 0}
}
</style>
```

---

## 2. JS 基础配置（Chart.js，复制到 `<script>` 开头）

```javascript
// 全局主题色（从CSS变量读取，换主题时自动跟随）
const CS = getComputedStyle(document.documentElement);
const C1  = CS.getPropertyValue('--c1').trim();
const C2  = CS.getPropertyValue('--c2').trim();
const C3  = CS.getPropertyValue('--c3').trim();
const C4  = CS.getPropertyValue('--c4').trim();
const RED = CS.getPropertyValue('--red').trim();
const PUR = '#A040A0';  // 用于折线点评等紫色细节

// Chart.js 默认值
Chart.defaults.color        = '#8A80A0';  // 调整为当前主题 --mu 色
Chart.defaults.borderColor  = '#D8D0EC';  // 调整为当前主题 --bd 色
Chart.defaults.font.family  = "'Noto Sans SC', sans-serif";
Chart.defaults.font.size    = 11;

// 基础配置对象（复用）
const B = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: '#1A1525',  // --t 深色
      borderColor: C1,
      borderWidth: 1,
      titleColor: '#E8E0F5',
      bodyColor: '#B0A8CC',
      padding: 10,
      cornerRadius: 6
    }
  },
  scales: {
    x: { grid: { color: '#EDE8F5' }, ticks: { color: '#8A80A0' } },
    y: { grid: { color: '#EDE8F5' }, ticks: { color: '#8A80A0' } }
  }
};

// 图例配置
const LG = { display: true, labels: { color: '#8A80A0', boxWidth: 11, font: { size: 10 } } };

// 渐变辅助（用于折线填充）
function makeGrad(ctx, color, alpha1 = 0.28, alpha2 = 0.04) {
  const g = ctx.createLinearGradient(0, 0, 0, 200);
  g.addColorStop(0, color + Math.round(alpha1 * 255).toString(16).padStart(2, '0'));
  g.addColorStop(1, color + Math.round(alpha2 * 255).toString(16).padStart(2, '0'));
  return g;
}

// 热力图颜色
function heatmapColor(pctChange) {
  if (pctChange >= 15)  return 'rgba(60,120,80,.85)';
  if (pctChange >= 0)   return 'rgba(80,140,100,.55)';
  if (pctChange >= -20) return 'rgba(180,150,40,.60)';
  if (pctChange >= -40) return 'rgba(180,80,50,.65)';
  return 'rgba(150,40,120,.75)';
}

// Tab切换
function show(id, btn) {
  document.querySelectorAll('.pg').forEach(p => p.classList.remove('on'));
  document.querySelectorAll('.tab').forEach(b => b.classList.remove('on'));
  document.getElementById(id).classList.add('on');
  btn.classList.add('on');
}
```

---

## 3. 时段折线图（带全列 Tooltip）

```javascript
// ⚠️ 必须设置 interaction.mode:'index' 才能悬浮显示所有月份
new Chart(ctx, {
  type: 'line',
  data: { labels: hLbl, datasets: [
    { label:'11月', data:hNov, borderColor:'#B0A0D0', borderWidth:1.5, pointRadius:2, borderDash:[4,3], tension:.35 },
    { label:'12月', data:hDec, borderColor:C1, borderWidth:2.5, pointRadius:3, pointBackgroundColor:C1, tension:.35 },
    { label:'1月',  data:hJan, borderColor:C3, borderWidth:2, pointRadius:2, borderDash:[3,2], tension:.35 },
    { label:'2月',  data:hFeb, borderColor:C2, borderWidth:2, pointRadius:2, borderDash:[5,3], tension:.35 },
    { label:'3月',  data:hMar, borderColor:RED, borderWidth:2.5, pointRadius:3, pointBackgroundColor:RED, tension:.35 },
  ]},
  options: {
    ...B,
    maintainAspectRatio: false,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      ...B.plugins,
      legend: { ...LG, position: 'top' },
      tooltip: {
        ...B.plugins.tooltip,
        mode: 'index',
        intersect: false,
        callbacks: {
          title: items => `${items[0].label}  日均场次`,
          label: item  => `  ${item.dataset.label}：${item.raw} 场/日`
        }
      }
    }
  }
});
```

---

## 4. 热力图生成函数

```javascript
function buildHeatmap(containerId, months, hourlyData, hChg, hours) {
  const con = document.getElementById(containerId);
  const hLbl = hours.map(h => h + '时');

  // 表头
  const emptyCell = document.createElement('div');
  emptyCell.className = 'hmh';
  con.appendChild(emptyCell);
  hLbl.forEach(lbl => {
    const d = document.createElement('div');
    d.className = 'hmh';
    d.textContent = lbl;
    con.appendChild(d);
  });

  // 数据行
  months.forEach(([label, vals]) => {
    const lb = document.createElement('div');
    lb.className = 'hml';
    lb.textContent = label;
    con.appendChild(lb);

    vals.forEach((v, i) => {
      const cell = document.createElement('div');
      cell.className = 'hmc';
      cell.style.background = heatmapColor(hChg[i]);
      cell.style.color = '#FFFFFF';
      cell.style.fontWeight = '600';
      cell.textContent = v.toFixed(1);
      cell.title = `${label} ${hours[i]}时 日均${v}场 · 12→3月${hChg[i] >= 0 ? '+' : ''}${hChg[i]}%`;
      con.appendChild(cell);
    });
  });
}

// 调用示例
buildHeatmap('hm',
  [['11月',hNov],['12月',hDec],['1月',hJan],['2月',hFeb],['3月',hMar]],
  hourlyData, hChg, Array.from({length:14}, (_,i)=>i+8)
);
```

---

## 5. 输出验证函数

```javascript
// 在 HTML 生成后运行（Python端）
function verifyHTML(html) {
  const errors = [];
  const canvas = new Set([...html.matchAll(/<canvas id="([^"]+)"/g)].map(m=>m[1]));
  const jsRef  = new Set([...html.matchAll(/getElementById\('([^']+)'\)/g)].map(m=>m[1]));
  const orphan = [...jsRef].filter(id => !canvas.has(id) && id !== 'hm');
  if (orphan.length) errors.push(`孤立JS引用: ${orphan}`);
  if (!html.includes('@media (max-width')) errors.push('缺移动端@media');
  ['上半月','等长15天','半月'].forEach(bad => {
    if (html.includes(bad)) errors.push(`过时表述: ${bad}`);
  });
  return errors;
}
```

---

## 6. Tab5 点评流量分析 — HTML结构

### 已开通商户通版本
```html
<!-- KV 概览数字 -->
<div class="kv-row">
  <div class="kv-box"><div class="kvn">112</div><div class="kvl">月新客/月</div></div>
  <div class="kv-box"><div class="kvn">4.8</div><div class="kvl">综合评分</div></div>
  <div class="kv-box"><div class="kvn">¥8,036</div><div class="kvl">点评渠道净收入</div></div>
</div>

<!-- 转化漏斗 -->
<div class="funnel">
  <div class="f-row">
    <div class="f-lbl">店铺浏览</div>
    <div class="f-bar-wrap">
      <div class="f-bar" style="width:100%;background:linear-gradient(90deg,var(--c1),var(--c3))">1,240</div>
    </div>
  </div>
  <div class="f-row">
    <div class="f-lbl">查看团购</div>
    <div class="f-bar-wrap">
      <div class="f-bar" style="width:54.8%;background:linear-gradient(90deg,var(--c2),var(--c4))">680 <span style="font-size:9px;opacity:.8">55%</span></div>
    </div>
  </div>
  <!-- width = 当层值/最大值 × 100% -->
</div>
```

### 未开通商户通版本（调研分析）
```html
<!-- 替换为：当前新客渠道饼图 + 开通收益测算表 -->
<canvas id="c_source"></canvas>  <!-- 饼图 -->
<div class="ins ye">测算：开通后月净新增¥X vs 当前¥Y</div>
```
