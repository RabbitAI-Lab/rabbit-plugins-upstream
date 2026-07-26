# 配色主题规范

## 1. 预设主题（直接复制使用）

### 主题1 — 紫蓝（精品/运动，技能示例主题）
此主题来自「星辰羽毛球馆」案例，参考图片：薰衣草色运动服+星空深紫背景。

```css
:root{
  --bg:#F5F3FA; --s1:#FFFFFF; --s2:#EDE8F5; --bd:#D8D0EC;
  --c1:#7B5EA7; --c2:#5B8DD9; --c3:#9B7DC7; --c4:#A390C8;
  --red:#B04848; --t:#1A1525; --mu:#7A6E90; --mu2:#C8C0DC; --tx:#2D2640;
}
```
- Hero: `background:linear-gradient(135deg,#5B3A8A,#6B4A9A,#4A3A7A); border-bottom:3px solid #3D2A6A`
- Tab:  `background:#4A3080; border-bottom:3px solid #35206A`
- Tab激活: `border-bottom-color:#CDB8F5`
- 图表配色: `C1='#7B5EA7', C2='#5B8DD9', C3='#9B7DC7', C4='#A390C8', RED='#B04848', PUR='#A040A0'`
- 新用户色: `C2+'55'`（蓝色），老用户色: `C1+'66'`（紫色）

### 主题2 — 橙绿（活力/运动场馆）
```css
:root{
  --bg:#F8F6F2; --s1:#FFFFFF; --s2:#F4F1EC; --bd:#E8E3DA;
  --c1:#4A7C59; --c2:#C97040; --c3:#D4884A; --c4:#5A8A6A;
  --red:#B04848; --t:#1A1A1A; --mu:#666666; --mu2:#CCCCCC; --tx:#333333;
}
```
- Hero: `background:linear-gradient(135deg,#B8694A,#A85C40,#985234); border-bottom:3px solid #8A4A2C`
- Tab:  `background:#4E7A62; border-bottom:3px solid #3A6550`
- Tab激活: `border-bottom-color:#C97040`
- 图表配色: `C1='#4A7C59', C2='#C97040', C3='#D4884A', C4='#5A8A6A', RED='#B04848'`

### 主题3 — 深蓝（科技/金融）
```css
:root{
  --bg:#F0F4FA; --s1:#FFFFFF; --s2:#E8EEFA; --bd:#D0DAEE;
  --c1:#2563EB; --c2:#F59E0B; --c3:#FBB040; --c4:#3B82F6;
  --red:#DC2626; --t:#0F172A; --mu:#64748B; --mu2:#CBD5E1; --tx:#1E293B;
}
```
- Hero: `background:linear-gradient(135deg,#1E3A8A,#1E40AF); border-bottom:3px solid #1A3570`
- Tab:  `background:#1E4080; border-bottom:3px solid #1A3570`

### 主题4 — 米棕（精品/餐饮/咖啡）
```css
:root{
  --bg:#FAF8F4; --s1:#FFFFFF; --s2:#F4F0E8; --bd:#E4DCCB;
  --c1:#8B6F47; --c2:#C4813D; --c3:#D4956A; --c4:#A08060;
  --red:#A84040; --t:#2C1F12; --mu:#7A6550; --mu2:#D0C4B0; --tx:#3D2E1C;
}
```
- Hero: `background:linear-gradient(135deg,#7A5A38,#5A3A20); border-bottom:3px solid #4A2A10`
- Tab:  `background:#6B5540; border-bottom:3px solid #5A4530`

### 主题5 — 深色（夜间/高端）
```css
:root{
  --bg:#0F1A0D; --s1:#162014; --s2:#1E2E1A; --bd:#2A4024;
  --c1:#4ADE80; --c2:#FB923C; --c3:#FACC15; --c4:#34D399;
  --red:#F87171; --t:#D8F0D0; --mu:#7AAA68; --mu2:#2A4024; --tx:#C8E8C0;
}
```
- Hero: `background:linear-gradient(135deg,#0D1F0A,#0F1A0D); border-bottom:3px solid #080F06`
- Tab:  `background:#1A3020; border-bottom:3px solid #0D2018`
- 热力图颜色需调整（深色背景）：使用更亮的颜色

---

## 2. 从Logo图片提取颜色

运行 `scripts/extract_colors.py`：

```bash
python3 scripts/extract_colors.py /path/to/logo.png --output css
```

输出示例：
```
提取颜色: #7B5EA7 (主), #5B8DD9 (辅)
:root {
  --c1: #7B5EA7;
  --c2: #5B8DD9;
  ...
}
```

---

## 3. 从HEX/RGB手动构建主题

给定主色 `primary` 和辅色 `accent`，套用如下规则：

```
--bg:  primary 极浅化 (lighten 90%+, desaturate)
--s1:  #FFFFFF
--s2:  primary 浅化 (lighten 85%)
--bd:  primary 浅化 (lighten 70%)
--c1:  primary  (主色，老用户/主指标/卡片左边条)
--c2:  accent   (辅色，新用户/次指标/强调)
--c3:  accent 浅一档
--c4:  primary 浅一档
--t:   非常深的同色系色（正文）
--mu:  中灰偏主色调（次要文字）

Hero bg:  primary 深化渐变（-10% → -20% → -30% lightness）
Tab bg:   primary 深化 -20%
```

Python 辅助函数：
```python
def lighten(hex_color, amount):
    """amount: 0.0-1.0，越大越浅"""
    r,g,b = int(hex_color[1:3],16), int(hex_color[3:5],16), int(hex_color[5:7],16)
    r = int(r + (255-r)*amount)
    g = int(g + (255-g)*amount)
    b = int(b + (255-b)*amount)
    return f"#{r:02X}{g:02X}{b:02X}"

def darken(hex_color, amount):
    r,g,b = int(hex_color[1:3],16), int(hex_color[3:5],16), int(hex_color[5:7],16)
    return f"#{int(r*(1-amount)):02X}{int(g*(1-amount)):02X}{int(b*(1-amount)):02X}"
```

---

## 4. 图表颜色使用约定

| 用途 | 颜色 |
|------|------|
| 老用户 | `C1+'66'`（主色，稍透明） |
| 新用户 | `C2+'55'`（辅色，稍透明） |
| 主折线/主柱 | `C1`（实色边框）|
| 次折线/辅助 | `C2` |
| 频次1次 | `C1+'44'`（淡） |
| 频次2次 | `C3+'cc'` |
| 频次3-5次 | `C2+'cc'` 或 `PUR+'cc'` |
| 高频5次+ | `RED+'cc'` |
| 日均实收折线 | `PUR`（紫色，区别于场次） |
| 留存率（高）| `C3`（浅色辅） |
| 留存率（低）| `RED` |
| 图表网格线 | `'#EDE8F5'`（主题1）/ `'#EEEEEE'`（其他浅色主题） |
| 刻度文字 | `'#8A80A0'`（主题1）/ `'#666666'`（其他） |

---

## 5. 热力图颜色（浅色主题通用）

```javascript
function heatmapColor(pctChange) {
  if (pctChange >= 15)  return 'rgba(60,120,80,.85)';   // 强增长 深绿
  if (pctChange >= 0)   return 'rgba(80,140,100,.55)';   // 微增   中绿
  if (pctChange >= -20) return 'rgba(180,150,40,.60)';   // 轻跌   黄
  if (pctChange >= -40) return 'rgba(180,80,50,.65)';    // 中跌   橙红
  return 'rgba(150,40,120,.75)';                          // 重跌   深紫/深红
}
// 热力图单元格文字颜色: '#FFFFFF'，fontWeight:'600'
```

深色主题（主题5）需改用更亮的版本：
```javascript
function heatmapColorDark(pctChange) {
  if (pctChange >= 15)  return 'rgba(80,220,120,.85)';
  if (pctChange >= 0)   return 'rgba(80,180,100,.6)';
  if (pctChange >= -20) return 'rgba(240,200,50,.65)';
  if (pctChange >= -40) return 'rgba(240,120,50,.7)';
  return 'rgba(240,80,80,.8)';
}
```

---

## 6. 字体配置

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;600&family=Noto+Sans+SC:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

/* 标题（.pt, h1）*/  font-family: 'Noto Serif SC', serif;
/* 正文（body）  */  font-family: 'Noto Sans SC', sans-serif;
/* 数字（.sv等）*/  font-family: 'DM Mono', monospace;
```
