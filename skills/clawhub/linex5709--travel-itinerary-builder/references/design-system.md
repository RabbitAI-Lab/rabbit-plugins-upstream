# CSS 设计系统与 HTML 架构参考

从 `assets/template.html` 提取的核心设计常量与组件结构。

## CSS 变量系统

```css
:root {
  --blue: #3b82f6;        /* 主色：按钮、高亮、badge */
  --blue-dark: #2563eb;   /* 深蓝：文字强调 */
  --blue-light: #eff6ff;  /* 浅蓝背景 */
  --blue-50: #dbeafe;     /* 边框色 */
  --amber: #fbbf24;       /* 强调色：高能日标记 */
  --amber-light: #fef3c7; /* 浅琥珀背景 */
  --amber-text: #92400e;  /* 琥珀色文字 */
  --slate-50 ~ slate-900; /* 灰度系统：背景→文字 */
  --green: #22c55e;       /* 正向指标 */
  --radius: 1.5rem;       /* 卡片/按钮圆角 */
  --radius-lg: 2.5rem;    /* 大卡片圆角 */
}
```

## 响应式断点

```css
@media (max-width: 768px) {
  .overview-card { grid-template-columns: 1fr; }   /* 概览卡变单列 */
  .logistics-grid { grid-template-columns: 1fr; }   /* 工具箱变单列 */
  .spot-body { padding: 20px; }                      /* 卡片内边距缩小 */
  .day-intro h3 { font-size: 1.3rem; }              /* 标题缩小 */
  .header-tag { display: none; }                     /* 标签隐藏 */
}
```

## 关键组件类名映射

| 组件 | CSS 类 | 用途 |
|------|--------|------|
| 粘性顶栏 | `header` / `.header-inner` | logo + 标题 + 日期标签 |
| 概览卡片 | `.overview-card` | 2列网格，深色背景，含统计小盒 |
| 统计小盒 | `.stat-box` | 深色背景上的白色数字+灰色标签 |
| 日期导航 | `.day-nav` / `.day-btn` / `.day-btn.active` | 横向滚动按钮组 |
| 日期引言 | `.day-intro` | 蓝色左边框 + badge + 标题 + 时间线 |
| Badge | `.badge-blue` / `.badge-amber` | 日期/航班标签 |
| 时间线 | `.timeline-box` | 浅蓝背景的内联时间概览 |
| 景点卡片 | `.spot-card` | 白色圆角卡片，hover 图片放大 |
| 图片区 | `.spot-img-wrap` / `.spot-img` | 280px 高，object-fit: cover |
| 浮层名称 | `.spot-img-name` | 毛玻璃效果，图片左下角 |
| 时间标签 | `.time-badge` | 浅蓝圆角胶囊 |
| 交通指引 | `.transport-box` | 浅蓝边框的信息框 |
| 推荐理由 | `.spot-reason` / `.r-label` | 蓝色大写标签 + 段落 |
| 步骤列表 | `.spot-how` / `.step-item` / `.step-num` | 蓝色圆形编号 + 文字 |
| 贴士卡片 | `.tips-box` | 灰色背景 + 图标 + 标签 |
| 工具箱 | `.logistics` / `.logistics-card` | 3列网格（移动端1列） |

## CSS 条形图实现

不使用 Chart.js，纯 CSS：

```javascript
function renderChart() {
  var html = '';
  for (var i = 0; i < chartData.labels.length; i++) {
    html += '<div class="chart-row">';
    html += '<span class="chart-label">' + chartData.labels[i] + '</span>';
    html += '<div class="chart-bar-track">';
    // 底层：趣味指数（半透明、绝对定位）
    html += '<div class="chart-bar-fun" style="width:' + chartData.fun[i] + '%;..."></div>';
    // 上层：体能指数
    html += '<div class="chart-bar-energy" style="width:' + chartData.energy[i] + '%;..."></div>';
    html += '</div></div>';
  }
  c.innerHTML = html;
}
```

能量数据格式：
```javascript
var chartData = {
  labels: ['D1','D2','D3','D4','D5','D6'],
  energy: [40, 75, 90, 55, 70, 50],  // 体能消耗 1-100
  fun: [65, 90, 88, 100, 95, 80]     // 趣味冒险 1-100
};
```

## JS 交互逻辑

1. `renderDay(n)` — 切换日期，自动滚动到内容区
2. `esc(s)` — HTML 转义，防止 XSS
3. 图片加载失败降级：`onerror` → SVG 占位图（灰底+景点名）
4. 所有 JS 为原生 ES5，不使用 let/const/箭头函数以确保最大兼容性

## 图片标签写法

```html
<img class="spot-img" src="路径" alt="名称" loading="lazy"
  onerror="this.src='data:image/svg+xml,...占位SVG...'">
```
