---
name: order-analytics
description: 订单数据业务分析仪表盘生成器。当用户提供订单Excel/CSV数据（含日期、金额、用户ID、场地/商品、时段等字段），需要生成业务分析报告、经营诊断、用户留存/频次分析、时段热力图、趋势对比、运营方案时，使用本技能。适用场景：场馆运营（羽毛球/网球/篮球/游泳）、餐饮门店、零售订单、服务业预约等任何有订单记录的业务场景。支持自定义配色（上传Logo图片或提供HEX/RGB色值）或选择预设主题。触发词：订单分析、经营诊断、用户分析、场次分析、留存分析、趋势分析、运营仪表盘、业务报告、数据报告。
---

# 订单业务分析仪表盘技能

## 概述

将原始订单数据转化为**交互式HTML分析报告**，6个Tab完整覆盖趋势→对比→时段→用户→流量→运营方案，支持桌面和手机端。**全程使用整月日均口径**，不做半月/等长截取对比。

> 📎 完整案例：`references/example-badminton.html` — 星辰羽毛球馆，紫色主题，6Tab

---

## 第一步：确认输入与配置

开始前确认以下信息（已在对话中提供则直接使用）：

### 1.1 数据文件
- 格式：`.xlsx`（用 `calamine` 引擎）/ `.csv`
- 必须字段：**订单日期、订单金额（或实收金额）、用户标识（手机号/用户ID）**
- 可选字段：场地/商品/服务类型、时段、订单状态、优惠金额

### 1.2 配色方案（四选一）
```
A. 上传Logo图片 → 运行 scripts/extract_colors.py 提取主色
B. 提供HEX色值 → 如 #7B5EA7（主色）+ #5B8DD9（辅色）
C. 提供RGB色值 → 如 rgb(123,94,167)
D. 选择预设主题（见 references/color-themes.md）：
   1. 紫蓝（精品/运动）  2. 橙绿（活力/场馆）
   3. 深蓝（科技/金融）  4. 米棕（优雅/餐饮）  5. 深色（夜间/高端）
```

### 1.3 业务场景说明（影响 Tab5 内容）
- 是否已开通大众点评商户通？
  - **已开通** → Tab5 展示点评流量分析（渠道来源、转化漏斗、团购表现、评价口碑）
  - **未开通** → Tab5 展示开通调研分析（新客来源现状、开通收益测算）
- 是否有竞品信息？→ Tab6 运营方案末尾加竞品对比表

---

## 第二步：数据处理

> 完整规范见 `references/data-processing.md`

### 2.1 读取与字段识别
```python
import pandas as pd
df = pd.read_excel(path, engine='calamine')  # 或 read_csv

FIELD_PATTERNS = {
    'date':    ['预订日期','下单时间','订单日期','日期','date','order_date'],
    'amount':  ['订单最终金额','实收金额','订单金额','金额','amount','price'],
    'user_id': ['手机号','用户ID','会员号','user_id','phone'],
    'item':    ['场地','商品','服务','项目','item','product'],
    'slot':    ['预订时段','时段','slot','time_slot'],
}
```

### 2.2 核心计算口径（⚠️ 关键原则）

**所有月度对比一律使用整月日均，不得用绝对总场次比较不同天数的月份。**

```python
# 整月日均（排除节假日锁场期，如春节）
monthly = df_clean.groupby('month').agg(
    op_days=('date', lambda x: x.dt.date.nunique()),
    total_orders=('amount','count'),
    total_rev=('amount','sum'),
    active_users=('user_id','nunique'),
)
monthly['daily_orders'] = (monthly['total_orders'] / monthly['op_days']).round(1)
monthly['daily_rev']    = (monthly['total_rev']    / monthly['op_days']).round(0)
```

**新老用户判断：**
```python
old_pool_months = sorted(df['month'].unique())[:3]  # 前3个月为老用户基准
old_pool = set(df[df['month'].isin(old_pool_months)]['user_id'])
```

**新用户次月留存：**
```python
first_order = df.groupby('user_id')['date'].min()
for mo, next_mo in zip(months[:-1], months[1:]):
    new_this = {u for u in set(df[df['month']==mo]['user_id'])
                if u not in old_pool and first_order[u] >= pd.Timestamp(f'{mo}-01')}
    retained  = new_this & set(df[df['month']==next_mo]['user_id'])
    retention = len(retained) / len(new_this)
```

**逐小时日均（整月，带 tooltip index mode）：**
```python
for mo in months:
    m = df_clean[df_clean['month']==mo]
    days = m['date'].dt.date.nunique()
    hourly[mo] = {h: round(len(m[m['hour']==h])/days, 2) for h in range(8,22)}

hchg = {h: round((hourly[last_mo][h]-hourly[ref_mo][h]) /
                  max(hourly[ref_mo][h],0.01)*100, 1)
        for h in range(8,22)}
```

---

## 第三步：配色主题

> 完整代码见 `references/color-themes.md`

### 3.1 预设主题速查

**主题1 — 紫蓝（本技能示例主题）**
```css
:root{
  --bg:#F5F3FA; --s1:#FFFFFF; --s2:#EDE8F5; --bd:#D8D0EC;
  --c1:#7B5EA7; --c2:#5B8DD9; --c3:#9B7DC7; --c4:#A390C8;
  --red:#B04848; --t:#1A1525; --mu:#7A6E90; --mu2:#C8C0DC; --tx:#2D2640;
}
/* Hero */ background: linear-gradient(135deg,#5B3A8A,#6B4A9A,#4A3A7A);
/* Tab  */ background: #4A3080; border-bottom: 3px solid #35206A;
/* Chart colors: C1='#7B5EA7', C2='#5B8DD9', RED='#B04848', PUR='#A040A0' */
```

**主题2 — 橙绿**
```css
:root{--bg:#F8F6F2;--s1:#FFFFFF;--s2:#F4F1EC;--bd:#E8E3DA;
  --c1:#4A7C59;--c2:#C97040;--c3:#D4884A;--c4:#5A8A6A;
  --red:#B04848;--t:#1A1A1A;--mu:#666666;--mu2:#CCCCCC;--tx:#333333}
/* Hero */ background:linear-gradient(135deg,#B8694A,#985234);
/* Tab  */ background:#4E7A62; border-bottom:3px solid #3A6550;
```

**主题3–5** → 见 `references/color-themes.md`

---

## 第四步：HTML报告结构

> 完整CSS组件库 + JS配置见 `references/html-template.md`

### 4.1 六Tab标准结构

| Tab | 标题 | 主要内容 |
|-----|------|---------|
| t1 | 📊 总体趋势 | 日均实收折线、场次+用户双轴柱、频次堆叠、新老用户堆叠、留存率、老用户活跃率 |
| t2 | 🔍 月度环比 | **5列整月对比卡** + 日均场次/实收 + 时段分类柱 + 工作日/周末 + 频次 + 新老用户 |
| t3 | ⏱ 时段分析 | 5期整月折线（tooltip mode:index）+ 热力图 + 时段分类柱 + 双侧洞察框 |
| t4 | 👤 用户结构 | 新老堆叠柱、频次分布、留存率、老用户活跃率 |
| t5 | 📍 点评流量 | **已开通**：来源饼+转化漏斗+团购表+评价分布+趋势图 / **未开通**：现状+测算 |
| t6 | 🎯 运营方案 | 3+3张策略卡（P0/P1/P2）+ 可选竞品对比表 |

### 4.2 关键组件规范

**Tab2 — 5列整月对比卡（用 auto-fit，不用固定4列）：**
```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:14px">
  <div class="cbox c1"><!-- 最早月：基准 --></div>
  <div class="cbox c1">...</div>
  <div class="cbox c2">...</div>
  <div class="cbox c3">...</div>
  <div class="cbox c4"><!-- 最新月：红/绿标注变化 --></div>
</div>
```

**Tab3 — 时段折线 Tooltip（必须 mode:index）：**
```javascript
options: {
  interaction: { mode: 'index', intersect: false },
  plugins: {
    tooltip: {
      mode: 'index', intersect: false,
      callbacks: {
        title: items => `${items[0].label}  日均场次`,
        label: item  => `  ${item.dataset.label}：${item.raw} 场/日`
      }
    }
  }
}
```

**Tab5已开通 — 转化漏斗：**
```html
<div class="funnel">
  <div class="f-row">
    <div class="f-lbl">店铺浏览</div>
    <div class="f-bar-wrap">
      <div class="f-bar" style="width:100%;background:linear-gradient(90deg,var(--c1),var(--c3))">1,240</div>
    </div>
  </div>
  <!-- width = 当层值 / 最大值 × 100% -->
</div>
```

**热力图颜色（适配浅色主题）：**
```javascript
function heatmapColor(v) {
  if (v >= 15)  return 'rgba(60,120,80,.85)';
  if (v >= 0)   return 'rgba(80,140,100,.55)';
  if (v >= -20) return 'rgba(180,150,40,.60)';
  if (v >= -40) return 'rgba(180,80,50,.65)';
  return 'rgba(150,40,120,.75)';  // 重跌用品牌深色
}
```

**所有网格用 auto-fit（手机天然折叠）：**
```css
.g2   { grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); }
.sps  { grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); }
/* 5列对比卡 */ grid-template-columns: repeat(auto-fit, minmax(130px,1fr));
```

**@media(max-width:600px) 必须包含：**
```css
@media (max-width:600px) {
  .g2,.g3 { grid-template-columns:1fr; }
  .sps    { grid-template-columns:1fr; }
  .strip  { flex-direction:column; }
  .st     { min-width:100%; flex:none; }
  /* 图表高度 ≤ 200px */
}
```

### 4.3 表格和热力图必须滚动包裹
```html
<!-- 表格 -->
<div class="dtbl-wrap">  <!-- overflow-x:auto -->
  <table class="dtbl" style="min-width:360px">...</table>
</div>

<!-- 热力图 -->
<div class="hm-wrap">  <!-- overflow-x:auto -->
  <div id="hm" class="hm" style="min-width:480px">...</div>
</div>
```

---

## 第五步：运营方案（Tab6）

### 优先级框架（3+3卡片）

```
第一行:
  P0 🔥  本周 — 最紧急（通常：流失用户召回 / 时段分流对冲）
  P1 ⚡  2周  — 中优先（通常：新客留存链路 / 特定时段产品）
  P1 ⚡  2周  — 中优先（通常：平台流量优化）

第二行:
  P1b📊  1个月 — 场景专项（如：拼场机制 / 企业团建）
  P2 📈  长效  — 固定档位 / 月卡产品
  P2 📈  差异化 — 教练课 / 独家产品线
```

每张卡：优先级标签 + 标题（颜色跟随优先级）+ 行动要点（**strong高亮数字**）+ 标签组

### 价格三原则
1. 对冲竞品：下午/闲时次卡低于竞品同类 5–10%
2. 保护黄金时段：晚场保持折扣，竞品晚场通常更贵
3. 首单吸引：体验价低于竞品但高于边际成本

---

## 第六步：输出检查

```python
import re

def verify(html):
    errors = []
    # Canvas vs JS 完整性
    canvas = set(re.findall(r'<canvas id="([^"]+)"', html))
    js_ref = set(re.findall(r"getElementById\('([^']+)'\)", html))
    orphan = js_ref - canvas - {'hm'}
    if orphan: errors.append(f"孤立JS引用: {orphan}")
    # 过时表述
    for bad in ['上半月', '等长15天', '等长时间段', '半月']:
        if bad in html: errors.append(f"过时表述: {bad}")
    # 移动端
    if '@media (max-width' not in html: errors.append("缺移动端@media")
    # 热力图包裹
    if 'id="hm"' in html:
        idx = html.find('id="hm"')
        if 'overflow-x:auto' not in html[max(0,idx-200):idx]:
            errors.append("热力图缺滚动包裹")
    return errors
```

---

## 参考文件

| 文件 | 内容 |
|------|------|
| `references/data-processing.md` | 字段识别、多行拆分、所有指标计算完整代码 |
| `references/color-themes.md` | 5套预设主题CSS + 从Logo/色值构建主题工具函数 |
| `references/html-template.md` | 完整CSS组件库 + Chart.js基础配置 + 验证函数 |
| `references/example-badminton.html` | 星辰羽毛球馆完整案例（紫色主题，6Tab，可直接参考） |
| `scripts/extract_colors.py` | 从Logo图片提取主色调工具 |
