# 视觉风格参考指南 (Styles Reference)

## 目录
- [风格1：赛博科技风](#1-赛博科技风-cyberpunktech---默认)
- [风格2：极简优雅风](#2-极简优雅风-minimalist-light)
- [风格3：Apple质感风](#3-notion--apple-质感风-apple-premium)
- [风格4：Cowork轻科技风](#4-cowork-轻科技风-cowork-light-tech)
- [风格5：报纸/杂志风](#5-报纸杂志风-newspaper)
- [风格6：Bloomberg终端风](#6-bloomberg-终端风-bloomberg-terminal)
- [风格7：水墨卷轴风](#7-水墨卷轴风-ink-scroll)
- [风格8：蒸汽朋克风](#8-蒸汽朋克风-steampunk)
- [风格9：小红书风](#9-小红书风-xiaohongshu--rednote)
- [风格10：莫兰迪高级灰风](#10-莫兰迪高级灰风-morandi)
- [风格11：玻璃拟态风](#11-玻璃拟态风-glassmorphism)
- [风格12：故宫风](#12-故宫风-palace)
- [风格13：清新自然绿风](#13-清新自然绿风-fresh)
- [风格14：大地原木风](#14-大地原木风-earthy)
- [风格15：优雅紫梦幻风](#15-优雅紫梦幻风-dreamy)
- [风格16：马卡龙粉彩风](#16-马卡龙粉彩风-macaron)
- [风格17：暗色极简风](#17-暗色极简风-carbon)
- [风格18：活力渐变风](#18-活力渐变风-vivid)
- [通用布局结构](#通用-html-布局骨架)
- [通用排版规范](#通用排版规范)
- [开源CSS工具库参考](#开源css工具库参考)

---

## 1. 赛博科技风 (Cyberpunk/Tech) - 默认

适用：AI、科技分析、硬核知识。

**升级亮点（v2）：** inline SVG 蜂窝六边形背景替换普通网格，`conic-gradient` 扫描环装饰，`text-shadow` 发光字升级。

```css
:root {
    --bg-color: #050812;
    --primary-glow: #00f0ff;
    --secondary-glow: #b900ff;
    --text-main: #f0f4f8;
    --text-muted: #7a8fa6;
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif;
    /* 升级：inline SVG 蜂窝六边形背景 + 细网格叠加 */
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='100'%3E%3Cpath d='M28 66L0 50V18L28 2l28 16v32z' fill='none' stroke='rgba(0%2C240%2C255%2C0.1)' stroke-width='1'/%3E%3C/svg%3E"),
        linear-gradient(rgba(0,240,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,240,255,0.04) 1px, transparent 1px);
    background-size: 56px 100px, 30px 30px, 30px 30px;
    margin: 0; padding: 0;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 40px 32px;
    position: relative;
}
.glass-card {
    background: rgba(12, 18, 32, 0.75);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 0 20px rgba(0,240,255,0.04);
    padding: 28px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
}
/* 卡片顶部扫描线装饰 */
.glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary-glow), transparent);
    opacity: 0.6;
}
.glow-title {
    font-size: 1.8em;
    font-weight: 700;
    color: var(--primary-glow);
    text-shadow: 0 0 20px rgba(0,240,255,0.7), 0 0 40px rgba(0,240,255,0.3);
    letter-spacing: 0.04em;
    margin-bottom: 8px;
}
.subtitle {
    color: var(--text-muted);
    font-size: 0.9em;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.section-title {
    font-size: 1.1em;
    color: var(--primary-glow);
    border-left: 3px solid var(--primary-glow);
    padding-left: 12px;
    margin: 24px 0 12px;
    text-shadow: 0 0 10px rgba(0,240,255,0.4);
}
.highlight {
    background: linear-gradient(135deg, rgba(0,240,255,0.12), rgba(185,0,255,0.08));
    border: 1px solid rgba(0,240,255,0.3);
    border-radius: 8px;
    padding: 16px 20px;
    font-size: 1.0em;
    color: #e0f8ff;
    font-style: italic;
    margin: 16px 0;
}
.tag {
    display: inline-block;
    background: rgba(0,240,255,0.1);
    border: 1px solid rgba(0,240,255,0.3);
    color: var(--primary-glow);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8em;
    margin: 4px;
}
/* 升级：conic-gradient 扫描环 */
.scan-ring {
    width: 48px; height: 48px;
    border-radius: 50%;
    background: conic-gradient(
        var(--primary-glow) 0deg,
        transparent 60deg,
        transparent 360deg
    );
    opacity: 0.5;
    flex-shrink: 0;
}
.divider {
    border: none;
    border-top: 1px solid rgba(0,240,255,0.12);
    margin: 24px 0;
}
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.75em;
    padding-top: 20px;
    letter-spacing: 0.1em;
}
```

---

## 2. 极简优雅风 (Minimalist Light)

适用：文学随笔、日记、人文知识。

**升级亮点（v2）：** 背景加 inline SVG `feTurbulence` noise filter 宣纸微噪点；分割线改为渐变淡出式；引用块加左侧渐变色条。

> **时间轴布局注意**：`.tl-left` 必须设置 `padding-right: 16px`，`.dot` 使用 `right: 0` 定位，避免圆点与年份文字重叠。正文加 `word-break: keep-all` 防止中文在尴尬位置断行。

```css
:root {
    --bg-color: #FDFDFD;
    --text-main: #2C2C2C;
    --text-muted: #8E8E8E;
    --accent: #D32F2F;
    --border: #EAEAEA;
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: "Songti SC", "Noto Serif CJK SC", "Source Han Serif CN", Georgia, serif;
    margin: 0; padding: 0;
    line-height: 1.9;
    /* 升级：inline SVG noise filter 微噪点宣纸感 */
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23noise)' opacity='0.025'/%3E%3C/svg%3E");
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 60px 40px;
}
.title-section {
    text-align: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 48px;
    margin-bottom: 40px;
}
.main-title {
    font-size: 2.2em;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 12px;
    word-break: keep-all;
}
.subtitle {
    color: var(--text-muted);
    font-size: 0.9em;
    letter-spacing: 0.12em;
}
.quote-card {
    border-left: 3px solid var(--accent);
    padding: 16px 24px;
    background: linear-gradient(to right, rgba(211,47,47,0.04), transparent);
    font-style: italic;
    color: #555;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
.section-title {
    font-size: 1.15em;
    font-weight: 700;
    margin: 32px 0 12px;
    color: var(--text-main);
    word-break: keep-all;
}
/* 升级：渐变淡出分割线 */
.divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border) 20%, var(--border) 80%, transparent);
    margin: 32px 0;
}
.divider::before { content: none; }
.divider-dot {
    text-align: center;
    color: var(--text-muted);
    margin: 32px 0;
    letter-spacing: 0.3em;
    font-size: 0.85em;
}
.divider-dot::before { content: "· · ·"; }
p, .body-text {
    word-break: keep-all;
    overflow-wrap: break-word;
}
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.8em;
    padding-top: 48px;
    border-top: 1px solid var(--border);
    margin-top: 48px;
}
```

---

## 3. Notion / Apple 质感风 (Apple Premium)

适用：效率工具、复盘总结、方法论分享。

**升级亮点（v2）：** `backdrop-filter` 毛玻璃卡片；window controls 加高光渐变；highlight 块加彩色渐变左条；tag 加 hover 感微阴影。

```css
:root {
    --bg-color: #F5F5F7;
    --card-bg: #FFFFFF;
    --text-main: #1D1D1F;
    --text-muted: #6E6E73;
    --accent: #0066CC;
    --border: rgba(0,0,0,0.06);
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Segoe UI", Helvetica, Arial, sans-serif;
    margin: 0; padding: 0;
    line-height: 1.7;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 40px 24px;
}
.apple-card {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 18px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
    padding: 28px 30px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.8);
}
.window-controls {
    display: flex; gap: 8px; margin-bottom: 20px;
    align-items: center;
}
/* 升级：window controls 加高光渐变 */
.dot { width: 12px; height: 12px; border-radius: 50%; position: relative; }
.dot::after {
    content: '';
    position: absolute;
    top: 1px; left: 2px;
    width: 6px; height: 4px;
    border-radius: 50%;
    background: rgba(255,255,255,0.5);
}
.dot-red { background: radial-gradient(circle at 35% 35%, #FF7F79, #FF5F56); }
.dot-yellow { background: radial-gradient(circle at 35% 35%, #FFD76B, #FFBD2E); }
.dot-green { background: radial-gradient(circle at 35% 35%, #5DD35D, #27C93F); }
.main-title {
    font-size: 1.8em;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
    word-break: keep-all;
}
.subtitle {
    color: var(--text-muted);
    font-size: 0.9em;
}
.section-title {
    font-size: 0.75em;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 24px 0 8px;
}
/* 升级：highlight 加彩色渐变左条 */
.highlight {
    background: rgba(0,102,204,0.06);
    border-left: 3px solid var(--accent);
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    color: var(--text-main);
    font-weight: 500;
    margin: 12px 0;
    position: relative;
    overflow: hidden;
}
.highlight::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(to bottom, #0066CC, #00AAFF);
}
.tag {
    display: inline-block;
    background: rgba(0,0,0,0.05);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.8em;
    color: var(--text-muted);
    margin: 3px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
}
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 20px 0;
}
p, .body-text { word-break: keep-all; overflow-wrap: break-word; }
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.78em;
    padding-top: 16px;
}
```

---

## 4. Cowork 轻科技风 (Cowork Light Tech)

适用：AI 工具介绍、内部产品手册、工作方法论、企业内部分享。

**升级亮点（v3 · Apple HIG x 小红书蓝）：** 全面对齐 AICowork 真实设计系统——苹果灰白背景 `#f5f5f7`、精确小红书蓝 `#0066cc`、1.5px 精致边框、`#1d1d1f` 苹果同款深黑文字、神经网络节点背景（72节点 `rgba(0,102,204,0.35)`）、磨砂玻璃 Hero 卡片、Eyebrow 全大写宽字距、clamp 响应式字号。

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    /* 品牌蓝（小红书蓝，精确值） */
    --blue:        #0066cc;
    --blue-soft:   #0077ed;
    --blue-light:  rgba(0, 102, 204, 0.06);
    --blue-mid:    rgba(0, 102, 204, 0.18);
    --blue-mid-2:  rgba(0, 102, 204, 0.28);
    /* 背景 & 表面 */
    --bg:          #f5f5f7;
    --surface:     #ffffff;
    /* 边框 */
    --border:      rgba(0, 0, 0, 0.09);
    --border-2:    rgba(0, 0, 0, 0.14);
    --border-hover: rgba(0, 102, 204, 0.28);
    /* 文字（苹果同款深黑） */
    --text:        #1d1d1f;
    --text-2:      #6e6e73;
    --text-3:      #86868b;
    /* 圆角 */
    --radius-xs:   6px;
    --radius-sm:   10px;
    --radius:      14px;
    --radius-lg:   18px;
    --radius-xl:   20px;
    --radius-pill: 999px;
    /* 动效 */
    --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
    --ease-md:  cubic-bezier(0.4, 0, 0.2, 1);
}

body {
    background-color: var(--bg);
    color: var(--text);
    font-family: -apple-system, 'SF Pro Display', 'SF Pro Text',
                 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
    -webkit-font-smoothing: antialiased;
    margin: 0; padding: 0;
    line-height: 1.6;
    /* 神经网络节点背景：72节点分布，rgba(0,102,204) 小红书蓝 */
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ccircle cx='60' cy='60' r='2.2' fill='rgba(0%2C102%2C204%2C0.35)'/%3E%3Cline x1='60' y1='60' x2='120' y2='0'   stroke='rgba(0%2C102%2C204%2C0.07)' stroke-width='1'/%3E%3Cline x1='60' y1='60' x2='0'   y2='120' stroke='rgba(0%2C102%2C204%2C0.07)' stroke-width='1'/%3E%3Cline x1='60' y1='60' x2='120' y2='120' stroke='rgba(0%2C102%2C204%2C0.05)' stroke-width='1'/%3E%3C/svg%3E");
    background-size: 120px 120px;
}

/* 遮罩层：苹果灰白渐变，让节点背景若隐若现 */
body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: linear-gradient(160deg, rgba(245,245,247,0.72) 0%, rgba(245,245,247,0.45) 100%);
    pointer-events: none;
    z-index: 0;
}

.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 44px 28px;
    position: relative;
    z-index: 1;
}

/* ── Hero 区：磨砂玻璃大卡片 ── */
.hero {
    text-align: center;
    padding: clamp(28px, 4vh, 44px) clamp(24px, 3vw, 40px);
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.78);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.7);
    border-radius: var(--radius-xl);
}

/* Eyebrow：全大写 + 宽字距，建立视觉层次 */
.eyebrow {
    font-size: 0.62em;
    font-weight: 800;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin-bottom: 10px;
}

.hero-title {
    font-size: clamp(1.9em, 4.5vw, 2.6em);
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.05em;
    line-height: 1.15;
    margin-bottom: 10px;
    word-break: keep-all;
}

/* Gradient text：标题渐变高亮（Apple HIG 同款） */
.hero-title .accent {
    background: linear-gradient(118deg, #1a4a8c 0%, #0066cc 55%, #0077ed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    color: var(--text-2);
    font-size: clamp(0.82em, 1.1vw, 0.95em);
    letter-spacing: 0.01em;
    line-height: 1.6;
}

/* ── 内容卡片：1.5px 精致边框 ── */
.cowork-card {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: clamp(20px, 2.5vh, 28px) clamp(18px, 2.5vw, 26px);
    margin-bottom: 14px;
    transition:
        border-color 0.25s var(--ease-md),
        box-shadow   0.25s var(--ease-md),
        transform    0.25s var(--ease-md);
}

/* Accent 卡片（蓝色渐变底） */
.cowork-card-accent {
    background: linear-gradient(135deg, #eef5ff 0%, #dbeafe 100%);
    border: 1.5px solid rgba(0, 102, 204, 0.20);
    border-radius: var(--radius-lg);
    padding: clamp(18px, 2.5vh, 24px) clamp(18px, 2.5vw, 28px);
    margin-bottom: 14px;
    box-shadow: 0 4px 20px rgba(0, 102, 204, 0.10);
}

/* Section title：Eyebrow 风格，全大写宽字距 */
.section-title {
    font-size: 0.62em;
    font-weight: 800;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin: 0 0 12px;
}

.card-title {
    font-size: clamp(1.1em, 1.8vw, 1.32em);
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.03em;
    margin-bottom: 6px;
    word-break: keep-all;
    line-height: 1.3;
}

.card-desc {
    font-size: clamp(0.82em, 1.1vw, 0.92em);
    color: var(--text-2);
    line-height: 1.65;
    word-break: keep-all;
}

/* Highlight 引用块 */
.highlight {
    background: var(--blue-light);
    border-left: 3px solid var(--blue);
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    padding: 14px 18px;
    font-size: 0.9em;
    color: var(--text);
    margin: 14px 0;
    line-height: 1.7;
}
.highlight strong { color: var(--blue); }

/* Badge 标签（pill 形） */
.badge {
    display: inline-block;
    background: var(--blue-light);
    color: var(--blue);
    border: 1px solid var(--blue-mid);
    border-radius: var(--radius-pill);
    padding: 3px 11px;
    font-size: 0.78em;
    font-weight: 600;
    margin: 3px 3px 3px 0;
    letter-spacing: 0.02em;
}
.badge-gray {
    display: inline-block;
    background: rgba(0,0,0,0.05);
    color: var(--text-2);
    border: 1px solid var(--border-2);
    border-radius: var(--radius-pill);
    padding: 3px 11px;
    font-size: 0.78em;
    font-weight: 500;
    margin: 3px 3px 3px 0;
}
.badge-green {
    display: inline-block;
    background: rgba(52, 199, 89, 0.08);
    color: #1a7a35;
    border: 1px solid rgba(52, 199, 89, 0.25);
    border-radius: var(--radius-pill);
    padding: 3px 11px;
    font-size: 0.78em;
    font-weight: 600;
    margin: 3px 3px 3px 0;
}

/* 分割线 */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 18px 0;
}

/* 列表：实心蓝点 */
.cowork-list { list-style: none; padding: 0; margin: 0; }
.cowork-list li {
    padding: 9px 0 9px 18px;
    border-bottom: 1px solid var(--border);
    font-size: clamp(0.82em, 1.1vw, 0.9em);
    color: var(--text-2);
    position: relative;
    line-height: 1.6;
    word-break: keep-all;
}
.cowork-list li:last-child { border-bottom: none; }
.cowork-list li::before {
    content: '';
    position: absolute;
    left: 0; top: 50%;
    transform: translateY(-50%);
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--blue);
}

/* 对比表格（两列） */
.compare-row {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
}
.compare-cell {
    flex: 1;
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 14px 16px;
    font-size: 0.85em;
    color: var(--text-2);
    line-height: 1.5;
}
.compare-cell .label {
    font-size: 0.75em;
    font-weight: 700;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 4px;
}

/* 进度条 */
.progress-wrap {
    background: var(--blue-light);
    border-radius: var(--radius-xs);
    height: 5px;
    margin-top: 8px;
    overflow: hidden;
}
.progress-bar {
    height: 100%;
    border-radius: var(--radius-xs);
    background: linear-gradient(90deg, #0066cc, #0077ed);
}

/* 数字卡片（KPI 展示） */
.metric-row {
    display: flex;
    gap: 10px;
    margin-bottom: 14px;
}
.metric-card {
    flex: 1;
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: 16px 14px;
    text-align: center;
}
.metric-card .metric-value {
    font-size: clamp(1.4em, 2.2vw, 1.8em);
    font-weight: 700;
    color: var(--blue);
    letter-spacing: -0.03em;
    line-height: 1;
    margin-bottom: 4px;
}
.metric-card .metric-label {
    font-size: 0.72em;
    color: var(--text-3);
    font-weight: 500;
}

/* Footer */
.footer {
    text-align: center;
    color: var(--text-3);
    font-size: 0.72em;
    padding-top: 24px;
    letter-spacing: 0.08em;
    border-top: 1px solid var(--border);
    margin-top: 8px;
}
```

---

## 5. 报纸/杂志风 (Newspaper)

适用：历史事件、时间轴、人物传记、深度叙事内容。

**升级亮点（v2）：** 背景加 inline SVG 细点阵纹（铅字印刷颗粒感）；报头加双线装饰；时间轴年份列加边框阴影；标签统一大写。

```css
:root {
    --bg-color: #F0EDE4;
    --text-main: #1A1A1A;
    --text-muted: #555550;
    --accent: #1A1A1A;
    --border: #C8C4BA;
    --rule: #1A1A1A;
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: "Georgia", "Songti SC", "Noto Serif CJK SC", serif;
    margin: 0; padding: 0;
    line-height: 1.8;
    /* 升级：铅字印刷颗粒纹 */
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Crect width='1' height='1' x='0' y='0' fill='rgba(0%2C0%2C0%2C0.04)'/%3E%3Crect width='1' height='1' x='2' y='2' fill='rgba(0%2C0%2C0%2C0.03)'/%3E%3C/svg%3E");
    background-size: 4px 4px;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 48px 36px;
}
/* 顶部报头 */
.masthead {
    text-align: center;
    border-top: 4px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    padding: 12px 0 10px;
    margin-bottom: 4px;
}
.masthead-date {
    font-size: 0.72em;
    letter-spacing: 0.15em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 6px;
}
.masthead-title {
    font-size: 2.6em;
    font-weight: 700;
    letter-spacing: -0.01em;
    line-height: 1.1;
    font-family: "Georgia", serif;
    word-break: keep-all;
}
.masthead-sub {
    font-size: 0.82em;
    color: var(--text-muted);
    letter-spacing: 0.08em;
    margin-top: 6px;
    font-style: italic;
}
/* 升级：双线分割 */
.rule-double {
    border: none;
    border-top: 3px double var(--rule);
    margin: 8px 0 20px;
}
.lede {
    font-size: 1.1em;
    font-style: italic;
    color: var(--text-muted);
    border-left: 3px solid var(--rule);
    padding-left: 16px;
    margin: 0 0 24px;
    line-height: 1.7;
    word-break: keep-all;
}
/* 时间轴节点 */
.np-item {
    display: flex;
    gap: 0;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 18px;
}
.np-item:last-child { border-bottom: none; padding-bottom: 0; }
/* 升级：年份列加框感 */
.np-year-col {
    flex-shrink: 0;
    width: 72px;
    padding-right: 16px;
    border-right: 2px solid var(--rule);
    margin-right: 20px;
    padding-top: 2px;
}
.np-year {
    font-size: 1.5em;
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.02em;
}
.np-era {
    font-size: 0.68em;
    color: var(--text-muted);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.np-content {}
.np-headline {
    font-size: 1.1em;
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: 6px;
    letter-spacing: 0.01em;
    word-break: keep-all;
}
.np-body {
    font-size: 0.86em;
    color: #3A3A3A;
    line-height: 1.75;
    word-break: keep-all;
}
.np-tag {
    display: inline-block;
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.7em;
    padding: 1px 7px;
    margin-top: 7px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.editorial {
    border: 1px solid var(--rule);
    padding: 16px 20px;
    margin-top: 24px;
    background: rgba(0,0,0,0.03);
}
.editorial-label {
    font-size: 0.68em;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 8px;
    color: var(--text-muted);
}
.editorial-text {
    font-size: 0.88em;
    font-style: italic;
    line-height: 1.75;
    color: #333;
    word-break: keep-all;
}
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.72em;
    padding-top: 20px;
    border-top: 1px solid var(--border);
    margin-top: 24px;
    letter-spacing: 0.08em;
    font-style: italic;
}
```

**报纸风使用要点：**
- 背景用泛黄纸张色 `#F0EDE4` + 极淡点阵纹（铅字颗粒感）
- 顶部做报头（masthead）：刊名大字 + 副标题 + 双线分割
- 时间轴：年份列 `border-right: 2px solid` 做竖线，右侧内容 `margin-left` 留间距
- 全程黑/灰/米白，靠字重和字号建立层次，禁用彩色块

---

## 6. Bloomberg 终端风 (Bloomberg Terminal)

适用：数据报告、指标对比、金融分析、科技数字内容。

**升级亮点（v2）：** 年份数字加橙色左侧光条；发光文字 `text-shadow` 增强；加扫描线背景纹理；tag 加渐变边框。

```css
:root {
    --bg-color: #0A0A0A;
    --panel-bg: #111111;
    --text-main: #FF6B00;
    --text-white: #E8E8E8;
    --text-muted: #555555;
    --accent: #FF6B00;
    --accent-dim: rgba(255,107,0,0.12);
    --green: #00CC44;
    --border: rgba(255,107,0,0.18);
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: "Courier New", "Courier", "Lucida Console", monospace;
    margin: 0; padding: 0;
    line-height: 1.6;
    /* 升级：CRT扫描线纹理 */
    background-image: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,0,0,0.15) 2px,
        rgba(0,0,0,0.15) 3px
    );
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 32px 28px;
}
.terminal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 20px;
}
.terminal-id { font-size: 0.75em; color: var(--text-muted); letter-spacing: 0.1em; }
.terminal-title {
    font-size: 0.85em;
    color: var(--accent);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-shadow: 0 0 8px rgba(255,107,0,0.5);
}
.terminal-status { font-size: 0.72em; color: var(--green); letter-spacing: 0.08em; }

.bb-headline {
    font-size: 1.4em;
    font-weight: 700;
    color: var(--text-white);
    letter-spacing: 0.04em;
    line-height: 1.3;
    margin-bottom: 4px;
    text-transform: uppercase;
    word-break: keep-all;
}
.bb-subhead {
    font-size: 0.78em;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    margin-bottom: 20px;
}
.bb-rule { border: none; border-top: 1px solid var(--border); margin: 16px 0; }

/* 升级：年份加橙色左侧光条 */
.bb-row {
    display: flex;
    align-items: flex-start;
    gap: 0;
    padding: 12px 0 12px 12px;
    border-bottom: 1px solid rgba(255,107,0,0.08);
    border-left: 2px solid rgba(255,107,0,0.3);
    margin-left: -12px;
    margin-bottom: 4px;
}
.bb-row:last-child { border-bottom: none; }
.bb-num {
    flex-shrink: 0;
    width: 80px;
    font-size: 1.6em;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: -0.02em;
    line-height: 1;
    padding-top: 2px;
    /* 升级：数字发光 */
    text-shadow: 0 0 12px rgba(255,107,0,0.6), 0 0 24px rgba(255,107,0,0.2);
}
.bb-right { flex: 1; }
.bb-label {
    font-size: 0.85em;
    color: var(--text-white);
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.bb-desc {
    font-size: 0.78em;
    color: var(--text-muted);
    line-height: 1.65;
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    word-break: keep-all;
}
/* 升级：tag 加渐变边框效果 */
.bb-tag {
    display: inline-block;
    background: var(--accent-dim);
    color: var(--accent);
    font-size: 0.68em;
    padding: 1px 8px;
    margin-top: 6px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border: 1px solid var(--accent);
    box-shadow: 0 0 6px rgba(255,107,0,0.2);
}
.bb-analysis {
    background: var(--panel-bg);
    border: 1px solid var(--border);
    padding: 14px 16px;
    margin-top: 16px;
}
.bb-analysis-label {
    font-size: 0.68em;
    color: var(--accent);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 8px;
    text-shadow: 0 0 6px rgba(255,107,0,0.4);
}
.bb-analysis-text {
    font-size: 0.78em;
    color: var(--text-muted);
    line-height: 1.7;
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    word-break: keep-all;
}
.bb-analysis-text strong { color: var(--text-white); }
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.68em;
    padding-top: 16px;
    letter-spacing: 0.12em;
    font-family: "Courier New", monospace;
}
```

---

## 7. 水墨卷轴风 (Ink Scroll)

适用：中国历史、文化艺术、人文随笔、东方美学内容。

**升级亮点（v2）：** 多层椭圆渐变增强宣纸晕染感；inline SVG 水墨晕圈装饰；印章伪元素升级；竖向分隔线改为毛笔横扫感渐变。

```css
:root {
    --bg-color: #F5F0E8;
    --text-main: #2A2018;
    --text-muted: #7A6A50;
    --accent: #8B1A1A;
    --ink: #1A1008;
    --border: rgba(42,32,24,0.15);
    --wash: rgba(139,26,26,0.06);
}
body {
    background-color: var(--bg-color);
    color: var(--text-main);
    font-family: "Songti SC", "Noto Serif CJK SC", "Source Han Serif CN", "STSong", Georgia, serif;
    margin: 0; padding: 0;
    line-height: 2.0;
    /* 升级：多层椭圆渐变模拟宣纸晕染 + noise纹 */
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E"),
        radial-gradient(ellipse at 15% 40%, rgba(160,130,80,0.1) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 15%, rgba(140,110,60,0.08) 0%, transparent 45%),
        radial-gradient(ellipse at 50% 80%, rgba(180,150,100,0.06) 0%, transparent 50%);
}
.container {
    max-width: 540px;
    margin: 0 auto;
    padding: 60px 48px;
}
.scroll-header {
    text-align: center;
    margin-bottom: 48px;
    position: relative;
}
/* 升级：印章 + 双竖线 */
.seal {
    display: inline-block;
    border: 2px solid var(--accent);
    color: var(--accent);
    font-size: 0.75em;
    padding: 5px 16px;
    letter-spacing: 0.22em;
    margin-bottom: 20px;
    position: relative;
    box-shadow: inset 0 0 0 1px rgba(139,26,26,0.15);
}
.seal::before, .seal::after {
    content: '';
    position: absolute;
    top: 3px; bottom: 3px;
    width: 1px;
    background: var(--accent);
    opacity: 0.35;
}
.seal::before { left: 5px; }
.seal::after { right: 5px; }
.scroll-title {
    font-size: 2.2em;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: 0.12em;
    line-height: 1.3;
    margin-bottom: 12px;
    word-break: keep-all;
}
.scroll-subtitle {
    font-size: 0.85em;
    color: var(--text-muted);
    letter-spacing: 0.15em;
    font-style: italic;
}
/* 升级：毛笔横扫感分割线 */
.ink-rule {
    border: none;
    height: 1px;
    background: linear-gradient(to right,
        transparent 0%,
        rgba(26,16,8,0.08) 5%,
        rgba(26,16,8,0.22) 15%,
        rgba(26,16,8,0.28) 50%,
        rgba(26,16,8,0.15) 85%,
        rgba(26,16,8,0.04) 95%,
        transparent 100%
    );
    margin: 32px 0;
}
.scroll-item {
    display: flex;
    gap: 24px;
    margin-bottom: 32px;
    align-items: flex-start;
}
.scroll-item:last-child { margin-bottom: 0; }
.scroll-year-col {
    flex-shrink: 0;
    width: 56px;
    text-align: center;
    padding-top: 4px;
}
.scroll-year {
    font-size: 1.1em;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.04em;
    line-height: 1.2;
}
.scroll-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    margin: 8px auto 0;
    opacity: 0.65;
}
.scroll-content { flex: 1; padding-top: 2px; }
.scroll-name {
    font-size: 1.1em;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: 0.05em;
    margin-bottom: 6px;
    word-break: keep-all;
}
.scroll-text {
    font-size: 0.88em;
    color: #4A3C28;
    line-height: 1.9;
    word-break: keep-all;
}
.scroll-tag {
    display: inline-block;
    background: var(--wash);
    border: 1px solid rgba(139,26,26,0.2);
    color: var(--accent);
    font-size: 0.72em;
    padding: 2px 10px;
    margin-top: 8px;
    letter-spacing: 0.1em;
}
.scroll-closing {
    background: rgba(139,26,26,0.04);
    border-left: 2px solid var(--accent);
    padding: 16px 20px;
    margin-top: 32px;
}
.scroll-closing-label {
    font-size: 0.7em;
    color: var(--text-muted);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.scroll-closing-text {
    font-size: 0.9em;
    color: var(--text-muted);
    line-height: 1.85;
    font-style: italic;
    word-break: keep-all;
}
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.72em;
    padding-top: 32px;
    letter-spacing: 0.12em;
    opacity: 0.7;
}
```

---

## 8. 蒸汽朋克风 (Steampunk)

适用：工业历史、科技跃迁、机械美学、复古科技内容。纯CSS实现：齿轮、压力表、铜管、铆钉边框，无外部图片、无emoji。

```css
:root {
    --bg: #1A1008;
    --copper: #B87333;
    --copper-light: #D4944A;
    --copper-dark: #7A4A1A;
    --brass: #C8A830;
    --brass-light: #E8C840;
    --text: #E8D4A0;
    --text-muted: #A08040;
}
body {
    background-color: var(--bg);
    color: var(--text);
    font-family: "PingFang SC", "Georgia", serif;
    margin: 0; padding: 0;
    /* inline SVG 六边形蜂窝铆钉背景 */
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='100'%3E%3Cpath d='M28 66L0 50V18L28 2l28 16v32z' fill='none' stroke='rgba(184%2C115%2C51%2C0.14)' stroke-width='1'/%3E%3Ccircle cx='28' cy='2' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3Ccircle cx='56' cy='18' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3Ccircle cx='56' cy='50' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3Ccircle cx='28' cy='66' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3Ccircle cx='0' cy='50' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3Ccircle cx='0' cy='18' r='2.5' fill='rgba(184%2C115%2C51%2C0.18)'/%3E%3C/svg%3E"),
        repeating-linear-gradient(
            45deg,
            transparent, transparent 8px,
            rgba(184,115,51,0.025) 8px, rgba(184,115,51,0.025) 9px
        );
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 36px 28px;
}
/* 铆钉边框卡片 */
.rivet-card {
    background: linear-gradient(135deg, #1E1408 0%, #150F06 50%, #1E1408 100%);
    border: 2px solid var(--copper);
    border-radius: 4px;
    padding: 28px 28px;
    margin-bottom: 16px;
    position: relative;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.5), 0 4px 20px rgba(0,0,0,0.6), 0 0 0 1px rgba(184,115,51,0.25);
}
.rivet-card::before, .rivet-card::after {
    content: '';
    position: absolute;
    width: 10px; height: 10px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, var(--copper-light), var(--copper-dark));
    box-shadow: 0 1px 3px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.1);
}
.rivet-card::before { top: 8px; left: 8px; }
.rivet-card::after { top: 8px; right: 8px; }
.rivet-bl, .rivet-br {
    position: absolute;
    width: 10px; height: 10px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, var(--copper-light), var(--copper-dark));
    box-shadow: 0 1px 3px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.1);
}
.rivet-bl { bottom: 8px; left: 8px; }
.rivet-br { bottom: 8px; right: 8px; }
.card-top-bar {
    position: absolute;
    top: 0; left: 24px; right: 24px;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--brass) 20%, var(--brass-light) 50%, var(--brass) 80%, transparent);
}
/* 齿轮（clip-path 36点） */
.gear { flex-shrink: 0; position: relative; width: 48px; height: 48px; }
.gear-teeth {
    position: absolute; inset: 0;
    background: radial-gradient(circle at 40% 35%, var(--copper-light), var(--copper-dark));
    clip-path: polygon(
        50% 0%, 56% 8%, 64% 4%, 66% 13%, 75% 11%, 73% 20%,
        82% 22%, 77% 30%, 86% 35%, 78% 41%, 85% 48%, 76% 51%,
        81% 60%, 71% 60%, 72% 70%, 62% 67%, 59% 77%, 50% 72%,
        41% 77%, 38% 67%, 28% 70%, 29% 60%, 19% 60%,
        24% 51%, 15% 48%, 22% 41%, 14% 35%, 23% 30%,
        18% 22%, 27% 20%, 25% 11%, 34% 13%, 36% 4%, 44% 8%
    );
}
.gear-body {
    position: absolute; inset: 6px;
    background: radial-gradient(circle at 40% 35%, var(--copper-light), var(--copper-dark) 60%, #5A3010);
    border-radius: 50%;
}
.gear-hole {
    position: absolute; inset: 14px;
    background: var(--bg);
    border-radius: 50%;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.6);
}
.gear-pin {
    position: absolute; inset: 19px;
    background: radial-gradient(circle at 35% 35%, #D4944A, #5A3010);
    border-radius: 50%;
}
/* 压力表（conic-gradient 刻度盘） */
.gauge { position: relative; width: 60px; height: 60px; flex-shrink: 0; }
.gauge-outer {
    position: absolute; inset: 0;
    border-radius: 50%;
    background: linear-gradient(135deg, #2A1A08, #1A0E04);
    border: 3px solid var(--copper);
    box-shadow: 0 0 0 1px var(--copper-dark), inset 0 0 12px rgba(0,0,0,0.5);
}
.gauge-scale {
    position: absolute; inset: 4px;
    border-radius: 50%;
    border: 1px solid rgba(184,115,51,0.25);
    background: repeating-conic-gradient(
        rgba(200,168,48,0.55) 0deg, rgba(200,168,48,0.55) 2deg,
        transparent 2deg, transparent 30deg
    );
}
.gauge-needle {
    position: absolute;
    bottom: 50%; left: 50%;
    width: 2px; height: 18px;
    background: linear-gradient(to top, var(--copper-dark), #FF4400);
    transform-origin: bottom center;
    transform: translateX(-50%) rotate(-40deg);
    border-radius: 1px;
}
.gauge-center {
    position: absolute; inset: 22px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, var(--copper-light), var(--copper-dark));
}
.gauge-label {
    position: absolute;
    bottom: -18px; left: 50%;
    transform: translateX(-50%);
    font-size: 0.58em;
    color: var(--text-muted);
    letter-spacing: 0.08em;
    white-space: nowrap;
}
/* 装饰横条（铜管分割线） */
.gear-wrap { display: flex; align-items: center; gap: 14px; margin-bottom: 20px; }
.pipe-divider { display: flex; align-items: center; gap: 0; margin: 16px 0; }
.pipe-line {
    flex: 1; height: 6px;
    background: linear-gradient(to bottom,
        var(--copper-dark) 0%, var(--copper-light) 30%,
        var(--copper) 50%, var(--copper-light) 70%, var(--copper-dark) 100%
    );
    border-radius: 3px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.4), inset 0 1px 1px rgba(255,255,255,0.08);
}
.pipe-joint {
    width: 14px; height: 14px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, var(--brass-light), var(--brass), var(--copper-dark));
    box-shadow: 0 2px 4px rgba(0,0,0,0.5);
    flex-shrink: 0;
}
/* 标题与内容 */
.sp-title {
    font-size: 1.65em;
    font-weight: 700;
    color: var(--brass-light);
    text-shadow: 0 0 20px rgba(200,168,48,0.4), 0 2px 4px rgba(0,0,0,0.5);
    letter-spacing: 0.05em;
    line-height: 1.25;
    margin-bottom: 6px;
    word-break: keep-all;
}
.sp-subtitle {
    font-size: 0.8em;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    font-style: italic;
}
/* 时间轴节点 */
.sp-item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 14px; }
.sp-year-col { flex-shrink: 0; width: 62px; text-align: center; }
.sp-year-badge {
    display: inline-block;
    background: linear-gradient(135deg, var(--copper-dark), var(--copper), var(--copper-dark));
    color: var(--brass-light);
    font-size: 0.76em;
    font-weight: 700;
    padding: 4px 6px;
    border: 1px solid var(--brass);
    letter-spacing: 0.03em;
    box-shadow: 0 2px 6px rgba(0,0,0,0.4), inset 0 1px 1px rgba(255,255,255,0.08);
    white-space: nowrap;
}
.sp-content { flex: 1; min-width: 0; }
.sp-name {
    font-size: 0.98em;
    font-weight: 700;
    color: var(--brass-light);
    margin-bottom: 4px;
    letter-spacing: 0.02em;
    word-break: keep-all;
}
.sp-desc {
    font-size: 0.8em;
    color: var(--text-muted);
    line-height: 1.75;
    word-break: keep-all;
    overflow-wrap: break-word;
}
.sp-tag {
    display: inline-block;
    border: 1px solid rgba(184,115,51,0.35);
    color: var(--copper-light);
    font-size: 0.66em;
    padding: 1px 8px;
    margin-top: 5px;
    letter-spacing: 0.08em;
    background: rgba(184,115,51,0.07);
}
.footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.68em;
    padding-top: 16px;
    letter-spacing: 0.12em;
    opacity: 0.65;
}
```

**蒸汽朋克风使用要点：**
- 背景：inline SVG 六边形蜂窝（铆钉节点）+ 斜线底纹叠加，纯CSS无图片依赖
- 卡片：`rivet-card` 四角必须放 `.rivet-bl` `.rivet-br` 子元素（`::before/after` 只做上方两角）
- 齿轮：`.gear` 内放 `.gear-teeth` / `.gear-body` / `.gear-hole` / `.gear-pin` 四层
- 压力表：`.gauge` 内放 `.gauge-outer` / `.gauge-scale` / `.gauge-needle` / `.gauge-center` 四层
- 铜管分割线：`.pipe-divider` 内放 `.pipe-joint` / `.pipe-line` 交替，节数自由
- 正文 `word-break: keep-all` 防止中文在奇怪位置断行
- 年份标签 `.sp-year-badge` 宽度自适应，不要固定宽度防止溢出

---

## 9. 小红书风 (XiaoHongShu / REDNote)

适用：知识分享、生活攻略、干货笔记、好物推荐、任何想在小红书传播的内容。

**两种模式，由用户指定；未指定时默认模式 A：**

| 模式 | 触发词 | 气质 |
|------|-------|------|
| **A — 简洁正式** | "简单"/"正式"/"干净"/"知识感" | 呼吸感强，像写得好的知识笔记 |
| **B — 丰富活泼** | "活泼"/"丰富"/"可爱"/"生活"/"有趣" | 轻快温暖，像让人想收藏的生活攻略 |

**共用设计原则：**
- 背景白/极淡暖粉，**不用深色背景**
- 主色调：柔和珊瑚红 `#FF6B8A`（降饱和度，不用官方高饱和 `#FF2442`）
- 标题用红色，正文用深灰，靠色块和间距分层
- 严禁 emoji，序号用 CSS 圆圈或数字下划线

---

### 模式 A — 简洁正式 CSS（v3）

**主色调：** 小红书官方红 `#FF2442`（用户确认，锁定）  
**v2→v3 变更：** `#FF6B8A` → `#FF2442`，卡片底色调整为 `#FFF5F7`。  
**v2 优化（保留）：** MagicPattern 背景斜纹；加深边框；序号gap加大；标题横线加长渐变；Footer渐变分割线。

```css
:root {
    --bg: #FFFFFF;
    --text-main: #1A1A1A;
    --text-sub: #555555;
    --text-muted: #999999;
    --accent: #FF2442;
    --accent-light: rgba(255, 36, 66, 0.08);
    --accent-border: rgba(255, 36, 66, 0.28);
    --border: rgba(0, 0, 0, 0.06);
}
body {
    background: var(--bg);
    color: var(--text-main);
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif;
    margin: 0; padding: 0;
    line-height: 1.8;
    /* MagicPattern: 极淡45度斜纹，增加纸张质感 */
    background-image: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 12px,
        rgba(255, 36, 66, 0.025) 12px,
        rgba(255, 36, 66, 0.025) 13px
    );
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 48px 36px;
}
/* 标题区 */
.xhs-header {
    margin-bottom: 32px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--accent-border);
}
.xhs-title {
    font-size: 2em;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.25;
    letter-spacing: -0.01em;
    margin-bottom: 8px;
    word-break: keep-all;
    overflow-wrap: break-word;
}
/* 标题下方装饰线（加长到48px，更有分量） */
.xhs-title-line {
    width: 48px;
    height: 3px;
    background: linear-gradient(to right, var(--accent), rgba(255,36,66,0.3));
    border-radius: 2px;
    margin: 10px 0 12px;
}
.xhs-subtitle {
    font-size: 0.88em;
    color: var(--text-muted);
    letter-spacing: 0.04em;
    word-break: keep-all;
}
/* 内容卡片（简洁版：加深边框 + 微粉底） */
.xhs-card {
    background: #FFF5F7;
    border: 1px solid var(--accent-border);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.xhs-card-title {
    font-size: 1.0em;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 6px;
    word-break: keep-all;
    overflow-wrap: break-word;
    display: flex;
    align-items: baseline;
    gap: 12px; /* 加大序号与标题间距 */
}
/* 序号：数字 + 渐变下划线（简洁版） */
.xhs-num {
    font-size: 0.9em;
    font-weight: 700;
    color: var(--accent);
    border-bottom: 2px solid var(--accent);
    line-height: 1;
    padding-bottom: 1px;
    flex-shrink: 0;
    min-width: 16px;
    text-align: center;
}
.xhs-card-body {
    font-size: 0.86em;
    color: var(--text-sub);
    line-height: 1.8;
    word-break: keep-all;
    overflow-wrap: break-word;
}
/* 高亮引用 */
.xhs-quote {
    background: var(--accent-light);
    border-left: 3px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    font-size: 0.88em;
    color: var(--text-sub);
    font-style: italic;
    line-height: 1.75;
    margin: 14px 0;
    word-break: keep-all;
}
/* 标签（简洁版：方形pill粉边） */
.xhs-tag {
    display: inline-block;
    background: rgba(255,107,138,0.06);
    color: var(--text-muted);
    border: 1px solid rgba(255,107,138,0.2);
    border-radius: 4px;
    padding: 2px 9px;
    font-size: 0.75em;
    margin: 3px 3px 0 0;
    letter-spacing: 0.02em;
}
/* 分割线（简洁版：渐变淡出） */
.xhs-divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--accent-border) 20%, var(--accent-border) 80%, transparent);
    margin: 18px 0;
}
/* Footer（简洁版：渐变分割线 + 账号名） */
.xhs-footer {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.75em;
    padding-top: 20px;
    margin-top: 24px;
    letter-spacing: 0.06em;
    border-top: none;
    position: relative;
}
.xhs-footer::before {
    content: '';
    position: absolute;
    top: 0; left: 20%; right: 20%;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--accent-border), transparent);
}
p, li { word-break: keep-all; overflow-wrap: break-word; }
```

---

### 模式 B — 丰富活泼 CSS（v3）

**主色调：** 小红书官方红 `#FF2442`（用户确认，锁定）  
**v2→v3 变更：** `#FF6B8A` → `#FF2442`，背景/卡片底色跟随调整。  
**v2 优化（保留）：** Hero Patterns 圆点纹；Glassmorphism毛玻璃；padding收紧；Footer渐变分割线。

```css
:root {
    --bg: #FFF5F7;
    --card-bg: rgba(255, 230, 235, 0.85); /* 毛玻璃用半透明 */
    --text-main: #1A1A1A;
    --text-sub: #555555;
    --text-muted: #999999;
    --accent: #FF2442;
    --accent-light: rgba(255, 36, 66, 0.10);
    --accent-mid: rgba(255, 36, 66, 0.25);
    --border: rgba(255, 36, 66, 0.18);
}
body {
    background: var(--bg);
    color: var(--text-main);
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif;
    margin: 0; padding: 0;
    line-height: 1.8;
    /* Hero Patterns: 极细圆点纹（手账纸质感） */
    background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='10' cy='10' r='1.2' fill='rgba(255%2C36%2C66%2C0.12)'/%3E%3C/svg%3E");
    background-size: 20px 20px;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 44px 32px;
}
/* 标题区（活泼版） */
.xhs-header {
    text-align: center;
    margin-bottom: 24px;
}
.xhs-title {
    font-size: 2.1em;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.25;
    letter-spacing: -0.01em;
    margin-bottom: 6px;
    word-break: keep-all;
    overflow-wrap: break-word;
}
/* 标题下三段渐变横线装饰 */
.xhs-wave {
    display: flex;
    justify-content: center;
    gap: 4px;
    margin: 10px auto 14px;
}
.xhs-wave span {
    display: inline-block;
    width: 28px;
    height: 4px;
    border-radius: 2px;
}
.xhs-wave span:nth-child(1) { background: var(--accent); opacity: 0.9; }
.xhs-wave span:nth-child(2) { background: var(--accent); opacity: 0.5; width: 14px; }
.xhs-wave span:nth-child(3) { background: var(--accent); opacity: 0.25; width: 7px; }
.xhs-subtitle {
    font-size: 0.88em;
    color: var(--text-muted);
    letter-spacing: 0.04em;
    word-break: keep-all;
}
/* 内容卡片（活泼版：Glassmorphism毛玻璃 + 大圆角 + 微阴影） */
.xhs-card {
    background: var(--card-bg);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 107, 138, 0.22);
    border-radius: 20px;
    padding: 16px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 16px rgba(255, 107, 138, 0.10), inset 0 1px 0 rgba(255,255,255,0.6);
}
.xhs-card-title {
    font-size: 1.0em;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 10px; /* 加大标题与正文间距 */
    word-break: keep-all;
    overflow-wrap: break-word;
    display: flex;
    align-items: center;
    gap: 12px; /* 加大序号与标题间距 */
}
/* 序号：实心圆圈（活泼版） */
.xhs-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--accent);
    color: #FFFFFF;
    font-size: 0.72em;
    font-weight: 700;
    flex-shrink: 0;
    line-height: 1;
}
.xhs-card-body {
    font-size: 0.86em;
    color: var(--text-sub);
    line-height: 1.8;
    word-break: keep-all;
    overflow-wrap: break-word;
}
/* 高亮引用（活泼版） */
.xhs-quote {
    background: rgba(255, 107, 138, 0.08);
    border: 1px dashed var(--accent-mid);
    border-radius: 12px;
    padding: 14px 18px;
    font-size: 0.88em;
    color: var(--text-sub);
    font-style: italic;
    line-height: 1.75;
    margin: 14px 0;
    word-break: keep-all;
    text-align: center;
}
/* 标签（活泼版：pill形粉底红字） */
.xhs-tag {
    display: inline-block;
    background: rgba(255, 107, 138, 0.12);
    color: var(--accent);
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.75em;
    font-weight: 600;
    margin: 3px 3px 0 0;
    letter-spacing: 0.02em;
    box-shadow: 0 1px 4px rgba(255, 107, 138, 0.15);
}
/* 分割线（活泼版：渐变淡出） */
.xhs-divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right,
        transparent,
        var(--accent-mid) 20%,
        var(--accent-mid) 80%,
        transparent
    );
    margin: 20px 0;
}
/* Footer（活泼版：渐变分割线 + 引导语 + 账号名） */
.xhs-footer {
    text-align: center;
    padding-top: 20px;
    margin-top: 16px;
    position: relative;
}
.xhs-footer::before {
    content: '';
    position: absolute;
    top: 0; left: 15%; right: 15%;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--accent-mid), transparent);
}
.xhs-footer-guide {
    font-size: 0.82em;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 6px;
    letter-spacing: 0.04em;
}
.xhs-footer-account {
    font-size: 0.72em;
    color: var(--text-muted);
    letter-spacing: 0.08em;
}
p, li { word-break: keep-all; overflow-wrap: break-word; }
```

**小红书风使用要点（v2）：**
- 未指定模式时默认**模式 A（简洁正式）**，生成后告知用户可切换"活泼版"
- 序号组件：模式A用 `.xhs-num`（数字+下划线），模式B用 `.xhs-num`（实心圆圈）——两种模式 class 名相同，CSS 实现不同
- 标题区：模式A用 `.xhs-title-line`（渐变横线 48px），模式B用 `.xhs-wave`（三段渐变横线居中）
- Footer：模式A `::before` 渐变分割线 + 账号名；模式B `::before` 渐变分割线 + 引导语（不超过12字）+ 账号名
- 严禁 emoji，所有装饰靠 CSS 实现
- **主色调**：两种模式统一用小红书官方红 `#FF2442`（已由用户确认锁定，勿随意改回柔和版）
- 背景：模式A白底 + MagicPattern 淡红斜纹；模式B `#FFF5F7` + Hero Patterns 圆点纹
- 卡片：模式A微粉底 `#FFF5F7` + 加深边框；模式B Glassmorphism 半透明毛玻璃 + 大圆角

---

## 10. 莫兰迪高级灰风 (Morandi)

适用：品牌方法论、复盘总结、人文随笔、生活美学。

**风格亮点：** 低饱和大地灰调（灰绿/灰褐/藕粉），柔和阴影，中等圆角，无强对比，整体安静高级。强调色为莫兰迪灰绿。

```css
/* === 莫兰迪高级灰风 === */
:root {
    --mo-bg: #E8E4DD;
    --mo-surface: #F4F1EC;
    --mo-card: #FBFAF7;
    --mo-accent: #7C8B7E;
    --mo-accent2: #9A8C82;
    --mo-text: #4A453E;
    --mo-muted: #94897C;
    --mo-border: rgba(74,69,62,0.12);
    --mo-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body {
    background-color: var(--mo-bg);
    color: var(--mo-text);
    font-family: var(--mo-ft);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 48px 36px;
    background: var(--mo-surface);
    border: 1px solid rgba(74,69,62,0.08);
    border-radius: 18px;
}
.mo-header { margin-bottom: 32px; }
.mo-title {
    font-size: 2.1em;
    font-weight: 700;
    letter-spacing: -0.01em;
    line-height: 1.25;
    color: var(--mo-text);
    word-break: keep-all; overflow-wrap: break-word;
}
.mo-subtitle {
    color: var(--mo-muted);
    font-size: 0.95em;
    line-height: 1.65;
    margin-top: 12px;
    word-break: keep-all; overflow-wrap: break-word;
}
.mo-section-title {
    font-size: 1.15em;
    font-weight: 600;
    color: var(--mo-text);
    margin: 30px 0 14px;
    padding-left: 12px;
    border-left: 4px solid var(--mo-accent);
    word-break: keep-all;
}
.mo-card {
    background: var(--mo-card);
    border: 1px solid rgba(74,69,62,0.07);
    border-radius: 14px;
    box-shadow: 0 2px 14px rgba(74,69,62,0.06);
    padding: 18px 20px;
    margin: 14px 0;
}
.mo-card-title {
    font-weight: 600;
    color: var(--mo-text);
    line-height: 1.4;
    margin-bottom: 6px;
}
.mo-card-desc {
    color: var(--mo-muted);
    font-size: 0.88em;
    line-height: 1.6;
}
.mo-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(74,69,62,0.07);
}
.mo-item:last-child { border-bottom: none; }
.mo-num {
    flex: none;
    width: 26px; height: 26px;
    background: var(--mo-accent);
    color: #fff;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.82em;
    display: flex; align-items: center; justify-content: center;
}
.mo-item-body { flex: 1; }
.mo-item-title { color: var(--mo-text); font-weight: 500; line-height: 1.45; }
.mo-item-desc { color: var(--mo-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.mo-quote {
    background: rgba(124,139,126,0.08);
    border-left: 3px solid var(--mo-accent);
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    color: var(--mo-text);
    font-size: 0.95em;
    line-height: 1.65;
    margin: 20px 0;
}
.mo-tag {
    display: inline-block;
    background: rgba(124,139,126,0.14);
    color: var(--mo-accent);
    border-radius: 7px;
    font-size: 0.78em;
    font-weight: 600;
    padding: 3px 10px;
    margin: 4px 6px 4px 0;
}
.mo-divider { border: none; height: 1px; background: rgba(74,69,62,0.1); margin: 28px 0; }
.mo-footer {
    background: rgba(124,139,126,0.08);
    border-left: 3px solid var(--mo-accent);
    border-radius: 10px;
    padding: 12px 16px;
    margin-top: 32px;
    color: var(--mo-muted);
    font-size: 0.8em;
    line-height: 1.65;
}
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="mo-header">
        <div class="mo-title">莫兰迪高级灰<br>安静而克制的美学</div>
        <div class="mo-subtitle">低饱和大地灰调，柔和阴影，无强对比——整体呈现一种沉静的高级质感。</div>
    </div>

    <div class="mo-quote">好的设计不是被注意到，而是被感受到。留白与克制，本身就是一种表达。</div>

    <div class="mo-section-title">核心特征</div>
    <div class="mo-card">
        <div class="mo-card-title">灰调配色</div>
        <div class="mo-card-desc">灰绿、灰褐、藕粉为主，饱和度统一压低，避免任何刺眼的高对比。</div>
    </div>
    <div class="mo-card">
        <div class="mo-card-title">柔和层次</div>
        <div class="mo-card-desc">用极淡的阴影和中等圆角营造安静的层次感，而非强边框。</div>
    </div>

    <div class="mo-section-title">适用场景</div>
    <div class="mo-item">
        <div class="mo-num">1</div>
        <div class="mo-item-body">
            <div class="mo-item-title">品牌方法论 / 复盘总结</div>
            <div class="mo-item-desc">安静高级的气质适合承载严肃、克制的内容表达。</div>
        </div>
    </div>
    <div class="mo-item">
        <div class="mo-num">2</div>
        <div class="mo-item-body">
            <div class="mo-item-title">人文随笔 / 生活美学</div>
            <div class="mo-item-desc">低饱和调性天然契合慢节奏、有温度的文字。</div>
        </div>
    </div>

    <div class="mo-divider"></div>
    <div>
        <span class="mo-tag">高级灰</span>
        <span class="mo-tag">低饱和</span>
        <span class="mo-tag">留白克制</span>
        <span class="mo-tag">莫兰迪青</span>
    </div>

    <div class="mo-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 11. 玻璃拟态风 (Glassmorphism)

适用：SaaS 产品官网、活动页、功能介绍、数据展示。

**风格亮点：** 彩色渐变背景 + 半透明磨砂卡片（backdrop-filter blur）+ 细白描边 + 柔和大阴影，卡片浮在渐变上。**注意：渐变必须铺在 body，容器/卡片半透明才能透出彩色。**

```css
/* === 玻璃拟态风 === */
:root {
    --gl-accent: #6D5EF7;
    --gl-accent2: #4EC8E8;
    --gl-text: #1F2433;
    --gl-muted: #5B6072;
    --gl-glass: rgba(255,255,255,0.55);
    --gl-glass-strong: rgba(255,255,255,0.72);
    --gl-border: rgba(255,255,255,0.6);
    --gl-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body {
    /* 渐变铺 body，容器/卡片半透明才能透出彩色 */
    background: linear-gradient(135deg,#E6E9FF 0%,#F3E9FF 35%,#E9F7FF 70%,#FFF0F7 100%);
    background-attachment: fixed;
    color: var(--gl-text);
    font-family: var(--gl-ft);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
    padding: 28px 0;
}
.container {
    max-width: 560px;
    margin: 0 auto;
    padding: 44px 34px;
    background: var(--gl-glass);
    backdrop-filter: blur(22px) saturate(1.5);
    -webkit-backdrop-filter: blur(22px) saturate(1.5);
    border: 1px solid var(--gl-border);
    border-radius: 24px;
    box-shadow: 0 8px 40px rgba(80,70,160,0.16);
}
.gl-header { margin-bottom: 30px; }
.gl-title {
    font-size: 2.1em;
    font-weight: 700;
    letter-spacing: -0.015em;
    line-height: 1.22;
    color: var(--gl-text);
    word-break: keep-all; overflow-wrap: break-word;
}
.gl-title em { color: var(--gl-accent); font-style: normal; }
.gl-subtitle {
    color: var(--gl-muted);
    font-size: 0.95em;
    line-height: 1.65;
    margin-top: 12px;
    word-break: keep-all; overflow-wrap: break-word;
}
.gl-section-title {
    font-size: 1.15em;
    font-weight: 700;
    color: var(--gl-text);
    margin: 30px 0 14px;
    word-break: keep-all;
}
.gl-card {
    background: var(--gl-glass-strong);
    backdrop-filter: blur(16px) saturate(1.4);
    -webkit-backdrop-filter: blur(16px) saturate(1.4);
    border: 1px solid rgba(255,255,255,0.7);
    border-radius: 18px;
    box-shadow: 0 4px 24px rgba(80,70,160,0.12);
    padding: 18px 20px;
    margin: 14px 0;
}
.gl-card-title { font-weight: 600; color: var(--gl-text); line-height: 1.4; margin-bottom: 6px; }
.gl-card-desc { color: var(--gl-muted); font-size: 0.88em; line-height: 1.6; }
.gl-item {
    display: flex; align-items: flex-start; gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.45);
}
.gl-item:last-child { border-bottom: none; }
.gl-num {
    flex: none;
    width: 28px; height: 28px;
    background: linear-gradient(135deg,#6D5EF7,#4EC8E8);
    color: #fff;
    border-radius: 12px;
    font-weight: 700; font-size: 0.82em;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 10px rgba(109,94,247,0.4);
}
.gl-item-body { flex: 1; }
.gl-item-title { color: var(--gl-text); font-weight: 500; line-height: 1.45; }
.gl-item-desc { color: var(--gl-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.gl-quote {
    background: rgba(255,255,255,0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-left: 3px solid var(--gl-accent);
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    color: var(--gl-text);
    font-size: 0.95em; line-height: 1.65;
    margin: 20px 0;
}
.gl-tag {
    display: inline-block;
    background: rgba(109,94,247,0.12);
    color: var(--gl-accent);
    border-radius: 8px;
    font-size: 0.78em; font-weight: 600;
    padding: 3px 10px; margin: 4px 6px 4px 0;
}
.gl-divider { border: none; height: 1px; background: rgba(255,255,255,0.5); margin: 28px 0; }
.gl-footer {
    background: rgba(255,255,255,0.5);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-left: 3px solid var(--gl-accent);
    border-radius: 12px;
    padding: 12px 16px;
    margin-top: 32px;
    color: var(--gl-muted);
    font-size: 0.8em; line-height: 1.65;
}
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="gl-header">
        <div class="gl-title">玻璃拟态<br><em>通透</em>而有层次的现代质感</div>
        <div class="gl-subtitle">彩色渐变背景 + 半透明磨砂卡片，细白描边与柔和大阴影，卡片仿佛浮在渐变之上。</div>
    </div>

    <div class="gl-quote">通透，是现代产品设计的语言。让内容浮起来，让层次自然呼吸。</div>

    <div class="gl-section-title">核心特征</div>
    <div class="gl-card">
        <div class="gl-card-title">磨砂玻璃卡片</div>
        <div class="gl-card-desc">backdrop-filter 模糊背景，半透明白面透出底层彩色渐变，通透有层次。</div>
    </div>
    <div class="gl-card">
        <div class="gl-card-title">细白描边 + 柔阴影</div>
        <div class="gl-card-desc">细腻白色边框勾勒玻璃边缘，大范围柔和阴影让卡片"浮"起来。</div>
    </div>

    <div class="gl-section-title">适用场景</div>
    <div class="gl-item">
        <div class="gl-num">1</div>
        <div class="gl-item-body">
            <div class="gl-item-title">SaaS 产品官网 / 活动页</div>
            <div class="gl-item-desc">现代通透质感天然契合科技产品的调性。</div>
        </div>
    </div>
    <div class="gl-item">
        <div class="gl-num">2</div>
        <div class="gl-item-body">
            <div class="gl-item-title">功能介绍 / 数据展示</div>
            <div class="gl-item-desc">半透卡片让多模块信息层次清晰不拥挤。</div>
        </div>
    </div>

    <div class="gl-divider"></div>
    <div>
        <span class="gl-tag">玻璃拟态</span>
        <span class="gl-tag">彩色渐变</span>
        <span class="gl-tag">磨砂通透</span>
        <span class="gl-tag">SaaS 质感</span>
    </div>

    <div class="gl-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 12. 故宫风 (Palace)

适用：中国历史、文化艺术、国风节日、文博展览。

**风格亮点：** 深棕木底、朱砂红与鎏金字，书法字体点睛（Ma Shan Zheng/ZCOOL XiaoWei，无头环境自动 fallback 到宋体），方形描边序号 + 金色渐变分割线，宫廷庄重华贵。

```css
:root {
    --pl-bg: #0E0604; --pl-surface: #160A06; --pl-card: #1A0A06;
    --pl-crimson: #C0392B; --pl-gold: #C8A45A; --pl-gold-light: #E8C87A;
    --pl-text: #F0E6C8; --pl-muted: #9A8060;
    --pl-serif: "Ma Shan Zheng","ZCOOL XiaoWei","Noto Serif SC","Source Han Serif CN","Songti SC","STSong",Georgia,serif;
}
body { background-color: var(--pl-bg); color: var(--pl-text); font-family: var(--pl-serif); line-height: 1.8; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 38px; background: var(--pl-surface); border: 1px solid rgba(200,164,90,0.22); border-radius: 4px; box-shadow: 0 0 0 4px rgba(200,164,90,0.06); }
.pl-header { margin-bottom: 34px; text-align: center; border-bottom: 1px solid rgba(200,164,90,0.25); padding-bottom: 26px; }
.pl-title { font-size: 2.3em; font-weight: 400; letter-spacing: 0.08em; line-height: 1.35; color: var(--pl-gold-light); word-break: keep-all; }
.pl-title em { color: var(--pl-crimson); font-style: normal; }
.pl-subtitle { color: var(--pl-muted); font-size: 0.95em; line-height: 1.7; margin-top: 14px; letter-spacing: 0.04em; word-break: keep-all; }
.pl-section-title { font-size: 1.25em; font-weight: 400; color: var(--pl-gold); margin: 32px 0 16px; padding-left: 14px; border-left: 3px solid var(--pl-crimson); letter-spacing: 0.06em; word-break: keep-all; }
.pl-card { background: linear-gradient(160deg,#1E0C08 0%,#120602 60%,#1A0A06 100%); border: 1px solid rgba(200,164,90,0.2); border-radius: 4px; box-shadow: 0 2px 16px rgba(0,0,0,0.4); padding: 18px 22px; margin: 14px 0; }
.pl-card-title { font-weight: 400; color: var(--pl-gold-light); line-height: 1.5; margin-bottom: 8px; letter-spacing: 0.04em; }
.pl-card-desc { color: var(--pl-muted); font-size: 0.9em; line-height: 1.7; }
.pl-item { display: flex; align-items: flex-start; gap: 14px; padding: 13px 0; border-bottom: 1px solid rgba(200,164,90,0.14); }
.pl-item:last-child { border-bottom: none; }
.pl-num { flex: none; width: 30px; height: 30px; background: linear-gradient(135deg,rgba(192,57,43,0.35),rgba(192,57,43,0.18)); color: var(--pl-gold-light); border: 1px solid rgba(192,57,43,0.45); border-radius: 3px; font-weight: 400; font-size: 0.9em; display: flex; align-items: center; justify-content: center; }
.pl-item-body { flex: 1; }
.pl-item-title { color: var(--pl-text); font-weight: 400; line-height: 1.5; letter-spacing: 0.03em; }
.pl-item-desc { color: var(--pl-muted); font-size: 0.86em; line-height: 1.7; margin-top: 4px; }
.pl-quote { background: linear-gradient(135deg,rgba(192,57,43,0.10),rgba(192,57,43,0.04)); border-left: 2.5px solid var(--pl-crimson); border-radius: 0 8px 8px 0; padding: 15px 20px; color: var(--pl-gold-light); font-size: 0.98em; line-height: 1.75; margin: 22px 0; letter-spacing: 0.03em; }
.pl-tag { display: inline-block; background: rgba(192,57,43,0.28); color: var(--pl-gold-light); border: 1px solid rgba(200,164,90,0.3); border-radius: 3px; font-size: 0.8em; font-weight: 400; padding: 4px 12px; margin: 4px 6px 4px 0; letter-spacing: 0.04em; }
.pl-divider { border: none; height: 1px; background: linear-gradient(to right,transparent,rgba(200,164,90,0.35),transparent); margin: 30px 0; }
.pl-footer { background: rgba(192,57,43,0.08); border-left: 2.5px solid var(--pl-crimson); border-radius: 6px; padding: 13px 18px; margin-top: 34px; color: var(--pl-muted); font-size: 0.8em; line-height: 1.7; letter-spacing: 0.03em; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="pl-header">
        <div class="pl-title">故宫<em>红墙</em><br>金瓦朱阁的东方气韵</div>
        <div class="pl-subtitle">深棕木底、朱砂红与鎏金字，书法字体点睛，尽显宫廷的庄重华贵。</div>
    </div>
    <div class="pl-quote">红墙金瓦，一砖一瓦皆是千年气韵。</div>
    <div class="pl-section-title">核心特征</div>
    <div class="pl-card"><div class="pl-card-title">鎏金朱红</div><div class="pl-card-desc">鎏金字配朱砂红强调，深棕木底衬托，庄重华贵。</div></div>
    <div class="pl-card"><div class="pl-card-title">书法字韵</div><div class="pl-card-desc">中文书法字体点睛，东方古典气质浓厚。</div></div>
    <div class="pl-section-title">适用场景</div>
    <div class="pl-item"><div class="pl-num">1</div><div class="pl-item-body"><div class="pl-item-title">中国历史 / 文化艺术</div><div class="pl-item-desc">宫廷气质契合传统文化题材。</div></div></div>
    <div class="pl-item"><div class="pl-num">2</div><div class="pl-item-body"><div class="pl-item-title">国风节日 / 文博展览</div><div class="pl-item-desc">庄重华贵提升仪式感。</div></div></div>
    <div class="pl-divider"></div>
    <div>
        <span class="pl-tag">故宫</span>
        <span class="pl-tag">朱砂红</span>
        <span class="pl-tag">鎏金</span>
        <span class="pl-tag">东方美学</span>
    </div>
    <div class="pl-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 13. 清新自然绿风 (Fresh)

适用：健康、环保、生活方式、知识科普、教程攻略。

**风格亮点：** 极浅薄荷底搭配森林绿强调（#2E9E5B），纯白卡片，清爽通透有呼吸感。

```css
:root {
    --fr-bg: #F1F7F0; --fr-surface: #FBFEFA; --fr-card: #FFFFFF;
    --fr-accent: #2E9E5B; --fr-accent2: #6FB98F;
    --fr-text: #1F3A29; --fr-muted: #6B8475;
    --fr-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--fr-bg); color: var(--fr-text); font-family: var(--fr-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--fr-surface); border: 1px solid rgba(0,0,0,0.05); border-radius: 18px; }
.fr-header { margin-bottom: 32px; }
.fr-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--fr-text); word-break: keep-all; overflow-wrap: break-word; }
.fr-title em { color: var(--fr-accent); font-style: normal; }
.fr-subtitle { color: var(--fr-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.fr-section-title { font-size: 1.15em; font-weight: 600; color: var(--fr-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--fr-accent); word-break: keep-all; }
.fr-card { background: var(--fr-card); border: 1px solid rgba(0,0,0,0.05); border-radius: 14px; box-shadow: 0 2px 14px rgba(0,0,0,0.05); padding: 18px 20px; margin: 14px 0; }
.fr-card-title { font-weight: 600; color: var(--fr-text); line-height: 1.4; margin-bottom: 6px; }
.fr-card-desc { color: var(--fr-muted); font-size: 0.88em; line-height: 1.6; }
.fr-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
.fr-item:last-child { border-bottom: none; }
.fr-num { flex: none; width: 28px; height: 28px; background: #2E9E5B; color: #fff; border-radius: 8px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.fr-item-body { flex: 1; }
.fr-item-title { color: var(--fr-text); font-weight: 500; line-height: 1.45; }
.fr-item-desc { color: var(--fr-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.fr-quote { background: rgba(46,158,91,0.10); border-left: 3px solid var(--fr-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--fr-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.fr-tag { display: inline-block; background: rgba(46,158,91,0.12); color: var(--fr-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.fr-divider { border: none; height: 1px; background: rgba(0,0,0,0.08); margin: 28px 0; }
.fr-footer { background: rgba(46,158,91,0.10); border-left: 3px solid var(--fr-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--fr-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="fr-header">
        <div class="fr-title">清新自然<br><em>森林绿</em>的呼吸感</div>
        <div class="fr-subtitle">极浅薄荷底色搭配森林绿强调，清爽通透，天然亲近自然。</div>
    </div>
    <div class="fr-quote">让内容像清晨的森林一样，干净、通透、有生机。</div>
    <div class="fr-section-title">核心特征</div>
    <div class="fr-card"><div class="fr-card-title">森林绿主调</div><div class="fr-card-desc">#2E9E5B 森林绿为核心，浅草绿点缀，饱和适中不刺眼。</div></div>
    <div class="fr-card"><div class="fr-card-title">薄荷浅底</div><div class="fr-card-desc">极浅薄荷背景衬托纯白卡片，清爽有呼吸感。</div></div>
    <div class="fr-section-title">适用场景</div>
    <div class="fr-item"><div class="fr-num">1</div><div class="fr-item-body"><div class="fr-item-title">健康 / 环保 / 生活方式</div><div class="fr-item-desc">自然亲和的调性契合绿色、健康类内容。</div></div></div>
    <div class="fr-item"><div class="fr-num">2</div><div class="fr-item-body"><div class="fr-item-title">知识科普 / 教程攻略</div><div class="fr-item-desc">清爽底色让长文阅读更轻松。</div></div></div>
    <div class="fr-divider"></div>
    <div>
        <span class="fr-tag">清新</span>
        <span class="fr-tag">森林绿</span>
        <span class="fr-tag">自然</span>
        <span class="fr-tag">呼吸感</span>
    </div>
    <div class="fr-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 14. 大地原木风 (Earthy)

适用：手作、咖啡、生活美学、品牌故事、人文叙事。

**风格亮点：** 米色亚麻底搭配赤陶橙（#B5683C）与橄榄棕，奶油白卡片，温暖朴实有手作质地。

```css
:root {
    --ea-bg: #F3ECE1; --ea-surface: #FAF5EC; --ea-card: #FFFDF8;
    --ea-accent: #B5683C; --ea-accent2: #8A8B5C;
    --ea-text: #3D2E22; --ea-muted: #8A7460;
    --ea-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--ea-bg); color: var(--ea-text); font-family: var(--ea-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--ea-surface); border: 1px solid rgba(0,0,0,0.05); border-radius: 18px; }
.ea-header { margin-bottom: 32px; }
.ea-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--ea-text); word-break: keep-all; overflow-wrap: break-word; }
.ea-title em { color: var(--ea-accent); font-style: normal; }
.ea-subtitle { color: var(--ea-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.ea-section-title { font-size: 1.15em; font-weight: 600; color: var(--ea-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--ea-accent); word-break: keep-all; }
.ea-card { background: var(--ea-card); border: 1px solid rgba(0,0,0,0.05); border-radius: 14px; box-shadow: 0 2px 14px rgba(0,0,0,0.05); padding: 18px 20px; margin: 14px 0; }
.ea-card-title { font-weight: 600; color: var(--ea-text); line-height: 1.4; margin-bottom: 6px; }
.ea-card-desc { color: var(--ea-muted); font-size: 0.88em; line-height: 1.6; }
.ea-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
.ea-item:last-child { border-bottom: none; }
.ea-num { flex: none; width: 28px; height: 28px; background: #B5683C; color: #fff; border-radius: 8px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.ea-item-body { flex: 1; }
.ea-item-title { color: var(--ea-text); font-weight: 500; line-height: 1.45; }
.ea-item-desc { color: var(--ea-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.ea-quote { background: rgba(181,104,60,0.10); border-left: 3px solid var(--ea-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--ea-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.ea-tag { display: inline-block; background: rgba(181,104,60,0.12); color: var(--ea-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.ea-divider { border: none; height: 1px; background: rgba(0,0,0,0.08); margin: 28px 0; }
.ea-footer { background: rgba(181,104,60,0.10); border-left: 3px solid var(--ea-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--ea-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="ea-header">
        <div class="ea-title">大地原木<br><em>赤陶</em>的温暖质地</div>
        <div class="ea-subtitle">米色亚麻底搭配赤陶橙与橄榄棕，温暖朴实，有手作的质地感。</div>
    </div>
    <div class="ea-quote">回归土地的颜色，朴素本身就是一种高级。</div>
    <div class="ea-section-title">核心特征</div>
    <div class="ea-card"><div class="ea-card-title">赤陶橙主调</div><div class="ea-card-desc">#B5683C 赤陶橙为核心，橄榄棕辅助，暖调统一。</div></div>
    <div class="ea-card"><div class="ea-card-title">亚麻米底</div><div class="ea-card-desc">米色亚麻背景 + 奶油白卡片，温润不冷硬。</div></div>
    <div class="ea-section-title">适用场景</div>
    <div class="ea-item"><div class="ea-num">1</div><div class="ea-item-body"><div class="ea-item-title">手作 / 咖啡 / 生活美学</div><div class="ea-item-desc">温暖质地契合有温度的慢生活内容。</div></div></div>
    <div class="ea-item"><div class="ea-num">2</div><div class="ea-item-body"><div class="ea-item-title">品牌故事 / 人文叙事</div><div class="ea-item-desc">朴实调性承载真诚的表达。</div></div></div>
    <div class="ea-divider"></div>
    <div>
        <span class="ea-tag">大地色</span>
        <span class="ea-tag">赤陶橙</span>
        <span class="ea-tag">原木</span>
        <span class="ea-tag">手作感</span>
    </div>
    <div class="ea-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 15. 优雅紫梦幻风 (Dreamy)

适用：美妆、时尚、情感、活动海报、邀请函。

**风格亮点：** 极浅薰衣草底搭配品紫渐变（#8B5CF6→#C084FC），纯白卡片，梦幻优雅浪漫。序号用紫色渐变球。

```css
:root {
    --dr-bg: #F6F2FB; --dr-surface: #FCFAFE; --dr-card: #FFFFFF;
    --dr-accent: #8B5CF6; --dr-accent2: #C084FC;
    --dr-text: #2E2541; --dr-muted: #7C7295;
    --dr-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--dr-bg); color: var(--dr-text); font-family: var(--dr-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--dr-surface); border: 1px solid rgba(0,0,0,0.05); border-radius: 18px; }
.dr-header { margin-bottom: 32px; }
.dr-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--dr-text); word-break: keep-all; overflow-wrap: break-word; }
.dr-title em { color: var(--dr-accent); font-style: normal; }
.dr-subtitle { color: var(--dr-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.dr-section-title { font-size: 1.15em; font-weight: 600; color: var(--dr-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--dr-accent); word-break: keep-all; }
.dr-card { background: var(--dr-card); border: 1px solid rgba(0,0,0,0.05); border-radius: 14px; box-shadow: 0 2px 14px rgba(0,0,0,0.05); padding: 18px 20px; margin: 14px 0; }
.dr-card-title { font-weight: 600; color: var(--dr-text); line-height: 1.4; margin-bottom: 6px; }
.dr-card-desc { color: var(--dr-muted); font-size: 0.88em; line-height: 1.6; }
.dr-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
.dr-item:last-child { border-bottom: none; }
.dr-num { flex: none; width: 28px; height: 28px; background: linear-gradient(135deg,#8B5CF6,#C084FC); color: #fff; border-radius: 12px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.dr-item-body { flex: 1; }
.dr-item-title { color: var(--dr-text); font-weight: 500; line-height: 1.45; }
.dr-item-desc { color: var(--dr-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.dr-quote { background: rgba(139,92,246,0.10); border-left: 3px solid var(--dr-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--dr-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.dr-tag { display: inline-block; background: rgba(139,92,246,0.12); color: var(--dr-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.dr-divider { border: none; height: 1px; background: rgba(0,0,0,0.08); margin: 28px 0; }
.dr-footer { background: rgba(139,92,246,0.10); border-left: 3px solid var(--dr-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--dr-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="dr-header">
        <div class="dr-title">优雅紫梦幻<br><em>薰衣草</em>般的柔和</div>
        <div class="dr-subtitle">极浅薰衣草底搭配品紫渐变，梦幻优雅，浪漫而不失质感。</div>
    </div>
    <div class="dr-quote">优雅是一种气质，紫色是它的颜色。</div>
    <div class="dr-section-title">核心特征</div>
    <div class="dr-card"><div class="dr-card-title">品紫渐变</div><div class="dr-card-desc">#8B5CF6 品紫到浅紫渐变，梦幻有层次。</div></div>
    <div class="dr-card"><div class="dr-card-title">薰衣草浅底</div><div class="dr-card-desc">极浅薰衣草背景，纯白卡片，柔和舒适。</div></div>
    <div class="dr-section-title">适用场景</div>
    <div class="dr-item"><div class="dr-num">1</div><div class="dr-item-body"><div class="dr-item-title">美妆 / 时尚 / 情感</div><div class="dr-item-desc">浪漫梦幻契合女性向、情感类内容。</div></div></div>
    <div class="dr-item"><div class="dr-num">2</div><div class="dr-item-body"><div class="dr-item-title">活动海报 / 邀请函</div><div class="dr-item-desc">优雅调性提升仪式感。</div></div></div>
    <div class="dr-divider"></div>
    <div>
        <span class="dr-tag">梦幻</span>
        <span class="dr-tag">品紫</span>
        <span class="dr-tag">薰衣草</span>
        <span class="dr-tag">优雅</span>
    </div>
    <div class="dr-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 16. 马卡龙粉彩风 (Macaron)

适用：甜品、母婴、生活分享、节日祝福、好物种草。

**风格亮点：** 奶油粉底搭配低饱和珊瑚粉（#EB6F8E），纯白卡片，大圆角，甜美柔和可爱不腻。

```css
:root {
    --ma-bg: #FDF2F4; --ma-surface: #FFFAFB; --ma-card: #FFFFFF;
    --ma-accent: #EB6F8E; --ma-accent2: #F5A9C0;
    --ma-text: #4A2F38; --ma-muted: #9C7B85;
    --ma-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--ma-bg); color: var(--ma-text); font-family: var(--ma-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--ma-surface); border: 1px solid rgba(0,0,0,0.05); border-radius: 18px; }
.ma-header { margin-bottom: 32px; }
.ma-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--ma-text); word-break: keep-all; overflow-wrap: break-word; }
.ma-title em { color: var(--ma-accent); font-style: normal; }
.ma-subtitle { color: var(--ma-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.ma-section-title { font-size: 1.15em; font-weight: 600; color: var(--ma-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--ma-accent); word-break: keep-all; }
.ma-card { background: var(--ma-card); border: 1px solid rgba(0,0,0,0.05); border-radius: 14px; box-shadow: 0 2px 14px rgba(0,0,0,0.05); padding: 18px 20px; margin: 14px 0; }
.ma-card-title { font-weight: 600; color: var(--ma-text); line-height: 1.4; margin-bottom: 6px; }
.ma-card-desc { color: var(--ma-muted); font-size: 0.88em; line-height: 1.6; }
.ma-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
.ma-item:last-child { border-bottom: none; }
.ma-num { flex: none; width: 28px; height: 28px; background: #EB6F8E; color: #fff; border-radius: 14px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.ma-item-body { flex: 1; }
.ma-item-title { color: var(--ma-text); font-weight: 500; line-height: 1.45; }
.ma-item-desc { color: var(--ma-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.ma-quote { background: rgba(235,111,142,0.10); border-left: 3px solid var(--ma-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--ma-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.ma-tag { display: inline-block; background: rgba(235,111,142,0.13); color: var(--ma-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.ma-divider { border: none; height: 1px; background: rgba(0,0,0,0.08); margin: 28px 0; }
.ma-footer { background: rgba(235,111,142,0.10); border-left: 3px solid var(--ma-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--ma-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="ma-header">
        <div class="ma-title">马卡龙粉彩<br><em>珊瑚粉</em>的甜美</div>
        <div class="ma-subtitle">奶油粉底搭配低饱和珊瑚粉，甜美柔和，可爱而不腻。</div>
    </div>
    <div class="ma-quote">一点点甜，一点点软，就是恰到好处的可爱。</div>
    <div class="ma-section-title">核心特征</div>
    <div class="ma-card"><div class="ma-card-title">珊瑚粉主调</div><div class="ma-card-desc">#EB6F8E 珊瑚粉低饱和不刺眼，樱粉点缀。</div></div>
    <div class="ma-card"><div class="ma-card-title">奶油粉底</div><div class="ma-card-desc">极浅奶油粉背景，圆润大圆角，甜而不腻。</div></div>
    <div class="ma-section-title">适用场景</div>
    <div class="ma-item"><div class="ma-num">1</div><div class="ma-item-body"><div class="ma-item-title">甜品 / 母婴 / 生活分享</div><div class="ma-item-desc">甜美调性契合温柔、可爱的内容。</div></div></div>
    <div class="ma-item"><div class="ma-num">2</div><div class="ma-item-body"><div class="ma-item-title">节日祝福 / 好物种草</div><div class="ma-item-desc">粉彩色系提升亲和力。</div></div></div>
    <div class="ma-divider"></div>
    <div>
        <span class="ma-tag">马卡龙</span>
        <span class="ma-tag">珊瑚粉</span>
        <span class="ma-tag">甜美</span>
        <span class="ma-tag">粉彩</span>
    </div>
    <div class="ma-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 17. 暗色极简风 (Carbon)

适用：技术文档、开发者内容、数据报告、专业分析。

**风格亮点：** 炭灰深底（#14161A 三档递进）搭配冷调蓝绿（#4FB8C4），克制冷静，暗色护眼，技术专业感强。

```css
:root {
    --cb-bg: #14161A; --cb-surface: #1A1D23; --cb-card: #20242B;
    --cb-accent: #4FB8C4; --cb-accent2: #6CCFA8;
    --cb-text: #D6DAE0; --cb-muted: #8A929E;
    --cb-ft: "Inter","SF Mono","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--cb-bg); color: var(--cb-text); font-family: var(--cb-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--cb-surface); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; }
.cb-header { margin-bottom: 32px; }
.cb-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--cb-text); word-break: keep-all; overflow-wrap: break-word; }
.cb-title em { color: var(--cb-accent); font-style: normal; }
.cb-subtitle { color: var(--cb-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.cb-section-title { font-size: 1.15em; font-weight: 600; color: var(--cb-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--cb-accent); word-break: keep-all; }
.cb-card { background: var(--cb-card); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; box-shadow: 0 2px 14px rgba(0,0,0,0.3); padding: 18px 20px; margin: 14px 0; }
.cb-card-title { font-weight: 600; color: var(--cb-text); line-height: 1.4; margin-bottom: 6px; }
.cb-card-desc { color: var(--cb-muted); font-size: 0.88em; line-height: 1.6; }
.cb-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.07); }
.cb-item:last-child { border-bottom: none; }
.cb-num { flex: none; width: 28px; height: 28px; background: rgba(79,184,196,0.16); color: var(--cb-accent); border-radius: 8px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.cb-item-body { flex: 1; }
.cb-item-title { color: var(--cb-text); font-weight: 500; line-height: 1.45; }
.cb-item-desc { color: var(--cb-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.cb-quote { background: rgba(79,184,196,0.10); border-left: 3px solid var(--cb-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--cb-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.cb-tag { display: inline-block; background: rgba(79,184,196,0.14); color: var(--cb-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.cb-divider { border: none; height: 1px; background: rgba(255,255,255,0.1); margin: 28px 0; }
.cb-footer { background: rgba(79,184,196,0.08); border-left: 3px solid var(--cb-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--cb-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="cb-header">
        <div class="cb-title">暗色极简<br><em>克制</em>的技术美感</div>
        <div class="cb-subtitle">炭灰深底搭配冷调蓝绿，克制冷静，适合技术与专业场景。</div>
    </div>
    <div class="cb-quote">少即是多。深色是专注，蓝绿是理性。</div>
    <div class="cb-section-title">核心特征</div>
    <div class="cb-card"><div class="cb-card-title">炭灰深底</div><div class="cb-card-desc">#14161A 炭灰三档递进，层次清晰不刺眼。</div></div>
    <div class="cb-card"><div class="cb-card-title">冷调蓝绿</div><div class="cb-card-desc">#4FB8C4 克制的强调色，理性专业。</div></div>
    <div class="cb-section-title">适用场景</div>
    <div class="cb-item"><div class="cb-num">1</div><div class="cb-item-body"><div class="cb-item-title">技术文档 / 开发者内容</div><div class="cb-item-desc">暗色护眼，契合工程师审美。</div></div></div>
    <div class="cb-item"><div class="cb-num">2</div><div class="cb-item-body"><div class="cb-item-title">数据报告 / 专业分析</div><div class="cb-item-desc">冷静调性突出严肃内容。</div></div></div>
    <div class="cb-divider"></div>
    <div>
        <span class="cb-tag">暗色</span>
        <span class="cb-tag">极简</span>
        <span class="cb-tag">蓝绿</span>
        <span class="cb-tag">技术感</span>
    </div>
    <div class="cb-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 18. 活力渐变风 (Vivid)

适用：活动、促销、潮流、年轻品牌、音乐娱乐。

**风格亮点：** 紫→粉→橙三色渐变（120°）贯穿标题、序号、强调元素，纯白衬底最大化衬托鲜活，年轻潮流张力十足。标题强调字用渐变文字裁剪。

```css
:root {
    --vv-bg: #FBF9FF; --vv-surface: #FFFFFF; --vv-card: #FFFFFF;
    --vv-accent: #7C3AED; --vv-accent2: #EC4899;
    --vv-text: #1E1B2E; --vv-muted: #6B6480;
    --vv-ft: "Inter","PingFang SC","Helvetica Neue",sans-serif;
}
body { background-color: var(--vv-bg); color: var(--vv-text); font-family: var(--vv-ft); line-height: 1.7; -webkit-font-smoothing: antialiased; }
.container { max-width: 560px; margin: 0 auto; padding: 48px 36px; background: var(--vv-surface); border: 1px solid rgba(0,0,0,0.05); border-radius: 18px; }
.vv-header { margin-bottom: 32px; }
.vv-title { font-size: 2.1em; font-weight: 700; letter-spacing: -0.01em; line-height: 1.25; color: var(--vv-text); word-break: keep-all; overflow-wrap: break-word; }
.vv-title em { color: var(--vv-accent); font-style: normal; }
.vv-subtitle { color: var(--vv-muted); font-size: 0.95em; line-height: 1.65; margin-top: 12px; word-break: keep-all; overflow-wrap: break-word; }
.vv-section-title { font-size: 1.15em; font-weight: 600; color: var(--vv-text); margin: 30px 0 14px; padding-left: 12px; border-left: 4px solid var(--vv-accent); word-break: keep-all; }
.vv-card { background: var(--vv-card); border: 1px solid rgba(0,0,0,0.05); border-radius: 14px; box-shadow: 0 2px 14px rgba(0,0,0,0.05); padding: 18px 20px; margin: 14px 0; }
.vv-card-title { font-weight: 600; color: var(--vv-text); line-height: 1.4; margin-bottom: 6px; }
.vv-card-desc { color: var(--vv-muted); font-size: 0.88em; line-height: 1.6; }
.vv-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }
.vv-item:last-child { border-bottom: none; }
.vv-num { flex: none; width: 28px; height: 28px; background: linear-gradient(120deg,#7C3AED 0%,#EC4899 55%,#F97316 100%); color: #fff; border-radius: 10px; font-weight: 700; font-size: 0.82em; display: flex; align-items: center; justify-content: center; }
.vv-item-body { flex: 1; }
.vv-item-title { color: var(--vv-text); font-weight: 500; line-height: 1.45; }
.vv-item-desc { color: var(--vv-muted); font-size: 0.84em; line-height: 1.6; margin-top: 3px; }
.vv-quote { background: rgba(124,58,237,0.10); border-left: 3px solid var(--vv-accent); border-radius: 0 10px 10px 0; padding: 14px 18px; color: var(--vv-text); font-size: 0.95em; line-height: 1.65; margin: 20px 0; }
.vv-tag { display: inline-block; background: rgba(124,58,237,0.12); color: var(--vv-accent); border-radius: 7px; font-size: 0.78em; font-weight: 600; padding: 3px 10px; margin: 4px 6px 4px 0; }
.vv-divider { border: none; height: 1px; background: rgba(0,0,0,0.08); margin: 28px 0; }
.vv-footer { background: rgba(124,58,237,0.10); border-left: 3px solid var(--vv-accent); border-radius: 10px; padding: 12px 16px; margin-top: 32px; color: var(--vv-muted); font-size: 0.8em; line-height: 1.65; }
p { word-break: keep-all; overflow-wrap: break-word; }
.vv-title em { background: linear-gradient(120deg,#7C3AED 0%,#EC4899 55%,#F97316 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: transparent; font-style: normal; }
.vv-section-title { border-left-color: #EC4899; }
```

**HTML 结构示例：**

```html
<div class="container">
    <div class="vv-header">
        <div class="vv-title">活力<em>渐变</em><br>年轻而有张力</div>
        <div class="vv-subtitle">紫→粉→橙三色渐变，充满活力与张力，年轻潮流的视觉语言。</div>
    </div>
    <div class="vv-quote">用色彩表达能量，让每一屏都有张力。</div>
    <div class="vv-section-title">核心特征</div>
    <div class="vv-card"><div class="vv-card-title">三色渐变</div><div class="vv-card-desc">紫粉橙 120° 渐变贯穿标题、序号、强调元素。</div></div>
    <div class="vv-card"><div class="vv-card-title">纯白衬底</div><div class="vv-card-desc">纯白背景最大化衬托渐变的鲜活。</div></div>
    <div class="vv-section-title">适用场景</div>
    <div class="vv-item"><div class="vv-num">1</div><div class="vv-item-body"><div class="vv-item-title">活动 / 促销 / 潮流</div><div class="vv-item-desc">高饱和渐变抓眼球，适合营销传播。</div></div></div>
    <div class="vv-item"><div class="vv-num">2</div><div class="vv-item-body"><div class="vv-item-title">年轻品牌 / 音乐娱乐</div><div class="vv-item-desc">张力十足契合年轻受众。</div></div></div>
    <div class="vv-divider"></div>
    <div>
        <span class="vv-tag">活力</span>
        <span class="vv-tag">三色渐变</span>
        <span class="vv-tag">潮流</span>
        <span class="vv-tag">年轻</span>
    </div>
    <div class="vv-footer">text-to-elegant-image @ claude-4.8-opus</div>
</div>
```

---

## 通用 HTML 布局骨架

生成 HTML 时使用此骨架，替换 `[STYLE]` 为上方对应风格的 CSS，`[CONTENT]` 为处理后的内容：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>长图</title>
    <style>
    /* === 重置 === */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    ul, ol { padding-left: 1.5em; }
    img { max-width: 100%; }

    /* === 风格样式（从上方复制对应风格） === */
    [STYLE]
    </style>
</head>
<body>
    <div class="container">
        [CONTENT]
    </div>
</body>
</html>
```

---

## 通用排版规范

- **宽度**：容器最大 560px，留两侧 padding（24-40px）
- **行高**：正文 1.7-1.9，标题 1.2-1.4
- **字号层级**：大标题 1.8-2.2em → 小标题 1.1-1.2em → 正文 1em → 辅助 0.8em
- **换行保护**：所有正文和标题加 `word-break: keep-all; overflow-wrap: break-word`，防止中文在标点或奇怪位置断行
- **图片缩放**：不使用外部图片；图标用 CSS 形状或 inline SVG data URI 替代（**不使用 emoji**）
- **输出路径**：PNG 统一存放至输出目录（默认 `./output`，可用 `T2EI_OUTPUT_DIR` 环境变量配置）
- **截图高度**：`export_image.js` 自动测量 `.container` 真实高度并精确裁剪，无需手动控制

---

## 开源CSS工具库参考

> 以下工具已验证可在 Puppeteer 无头环境使用（inline / data URI 方式，不依赖 CDN）。

### 1. Hero Patterns（SVG 背景纹理库）
- **地址**：https://heropatterns.com/
- **用法**：将生成的 `background-image: url("data:image/svg+xml,...")` 直接内联到 CSS，零外部依赖
- **适合风格**：报纸风（细点阵纹）、水墨风（云纹）、蒸汽朋克（六边形铆钉铺地）、赛博风（蜂窝网格）
- **注意**：选好颜色和不透明度后复制 CSS code，不要用 `<img>` 方式引入

### 2. MagicPattern CSS Backgrounds（纯 CSS 渐变纹理）
- **地址**：https://www.magicpattern.design/tools/css-backgrounds
- **用法**：生成器产出纯 CSS `background-image: repeating-linear-gradient(...)` 代码，直接复制使用
- **适合场景**：快速生成斜纹、方格、点阵、波浪等背景纹理，不需要 SVG
- **适合风格**：极简风（微噪点）、Cowork 风（点阵）、Bloomberg 风（扫描线）

### 3. Glassmorphism CSS（毛玻璃效果）
- **核心属性**：`backdrop-filter: blur(10-15px)` + `background: rgba(255,255,255,0.1-0.25)` + `border: 1px solid rgba(255,255,255,0.2)`
- **浏览器支持**：Chrome 76+、Safari 9+、Firefox 103+（Puppeteer Chrome 146 完全支持）
- **适合场景**：用于赛博风 `.glass-card`（已使用）、Apple风卡片（已使用）；可做第9种"Aurora毛玻璃风"
- **注意**：需要有背景内容才能看到 blur 效果；纯色背景下无效果

### 4. CSS Shapes / clip-path 技术（纯CSS绘制复杂图形）
- **参考**：MDN clip-path docs、CyberTechUI（Dev.to 2026-01）
- **核心技术**：`clip-path: polygon(...)` 36点路径绘制齿轮；`conic-gradient` 绘制仪表盘刻度；`radial-gradient` 模拟金属质感
- **已用于**：蒸汽朋克风的齿轮、压力表、铆钉（完整示例见风格8）
- **扩展方向**：复杂星形、六边形卡片、斜角切口效果（`.card { clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 16px, 100% 100%, 0 100%) }`）

### ⚠️ 不适用的框架（禁止使用）
以下框架依赖 CDN 外部资源，Puppeteer 无头环境无法加载，**不要引入**：
- NES.css、XP.css、98.css、RPGUI — 依赖 CDN 字体/图片
- Bootstrap、Tailwind CDN 版 — 外部样式表
