# 📊 幻灯片生成模块

> 从属于 AHKB-CPS 统一系统。基于知识库或手动输入，生成专业 HTML 幻灯片。
> 🔴 **交互规则**：所有选项必须用数字编号展示，用户输入数字选择，**严禁使用 AskUserQuestion 工具**。

## 模块概述

Author professional HTML presentations as static files. One theme = one look. One layout = one page type. One animation = one entry effect.

### 📖 核心模板

#### `templates/master.html` — 生产母版

- ✅ **36 主题、21 FX 动画、完整 runtime.js + base.css**
- ✅ **保留 SLIDES_START/END 插槽** — `build-ppt.py` 在此插入 AI 生成的 slide
- ✅ **所见即所得编辑模式** — 打开即编辑，点击文字直接修改
- ✅ **质量基准** — 通过 `verify-output.py` 全部检查
- ✅ **CSS 类库** — 提供 `.h1` `.card` `.row` 等20+个内置类（见下方参考表）

```bash
python {skill_dir}/ppt/scripts/build-ppt.py _slides.html -o 成品.html -t "标题"
```

> 🔴 **路径约定**：本文中所有路径均相对于 AHKB-CPS 技能目录（即 `{skill_dir}`），而非工作空间。

### 能力一览

- **36 themes** — minimal-white, editorial-serif, dracula, tokyo-night, nord, glassmorphism, cyberpunk-neon, y2k-chrome, vaporwave, midcentury, corporate-clean, academic-paper, xiaohongshu-white 等
- **15 full-deck templates** — pitch-deck, tech-sharing, course-module, product-launch, weekly-report, xhs-post 等
- **31 layouts** — cover, timeline, chart-bar/line/pie/radar, mindmap, code, comparison, kpi-grid 等
- **27 CSS animations** via `data-anim`
- **21 Canvas FX animations** via `data-fx`
- **Keyboard runtime** — arrows, T (theme), A (anim), F (fullscreen), O (overview), S (presenter mode), E (edit mode), L (laser pointer)
- **Presenter mode** — 4 draggable magnetic cards
- **Edit mode** — text editing, image drag/resize, Ctrl+Z/Y undo/redo, Ctrl+S save

---

## 模块主菜单

```
═══════════════════════════════════════════════════════
        AHKB-CPS：幻灯片生成模块菜单
═══════════════════════════════════════════════════════
  1. 🧠 从知识库生成幻灯片     — AI检索知识库或你指定主题+KB补充
  2. 📄 依据指定的文档生成幻灯片 — 基于知识库中已入库的文档生成
  3. 🔄 转换 MS PPT           — 将现有的PowerPoint文件转为HTML版
  4. ✍️ 独立生成幻灯片          — 不依赖知识库，仅按你的输入自由生成
  e. ↩️ 返回主菜单             — 返回 AHKB-CPS 统一主菜单
═══════════════════════════════════════════════════════
请回复数字 1~4 或 e 选择操作：
```

## 菜单循环规则

- 操作完成后**返回模块主菜单**
- 仅当用户选择 `e` 时才返回 AHKB-CPS 统一主菜单
- 每次返回模块主菜单时，提示用户还可使用其他 AHKB-CPS 模块

---

# 菜单 1 — 🧠 从知识库生成幻灯片

## 检测知识库并选择工作模式

检查 `知识元/` 目录下是否有 ≥1 个 `.md` 文件。

**情况 A：检测到知识库（N 个知识元）** → 向用户展示：

**检测到知识库（N 个知识元），选择生成模式：**

1. 🧠 知识库驱动生成 — AI根据你的自然语言描述自动检索知识库
2. ✏️ 手动输入制作 — 你指定主题，AI先检索知识库补充素材

> 🔴 **两种模式都会检索知识库**。如需完全不依赖知识库，请使用菜单第 4 项。

**情况 B：无知识库** → 告知用户，推荐使用菜单第 4 项。

---

## 🧠 知识库驱动模式

### Step K1 — 对话描述需求 + AI 自动检索

**(a) 用户描述需求**

**问：你想做什么主题的演示文稿？请用一两句话描述。**

**(b) AI 自动检索知识库**

```bash
python {skill_dir}/core/kb2slides.py search --workspace "<Vault路径>" --query "用户描述的关键词" --top 15
```

**检索范围：**
- **知识元全文**：名称（×5）、summary（×3）、正文（×1）
- **chunks 原文**：heading（×3）、正文（×1）
- **图片资源**：扫描 `图片及其他资源/images/*.ctx`

> 🔴 **必须使用 chunks**：chunks 目录保存了原始文档的完整章节文本
> 🔴 **图片自动检索**：`search` 命令同时返回匹配的图片列表

**(c) 展示检索结果，确认方向**

**(d) AI 读取选中资料**

```bash
python {skill_dir}/core/kb2slides.py get-content --workspace "<Vault路径>" --units "知识元1,知识元2,..."
```

### Step K2-K7 — 观众、风格调性、内容要求、版式布局、页数、补充

按下方 Step 2-7 执行。**Step 5 版式布局选择时，AI 根据知识元标签给出推荐：**

| 知识元主要标签 | 推荐版式 |
|--------------|---------|
| 方法论、原理、概念 | `🎤 Tech Sharing（推荐）` |
| 人物、历史 | `📚 课程教学（推荐）` |
| 大系统观、系统哲学 | `📄 学术 / 报告（推荐）` |
| 默认 | `🧑‍🎨 从零开始（推荐）` |

---

## ✏️ 手动输入模式

### Step 1 — 主题
**问：这份 PPT 讲什么？**

### Step 1.5 — 检索知识库补充素材

```bash
python {skill_dir}/core/kb2slides.py search --workspace "<Vault路径>" --query "用户输入的主题" --top 10
```

> 🔴 **知识库有料就用，没料不勉强。**

### Step 1.6 — 确定幻灯片题目

> 🔴 **必须在此步骤确定幻灯片题目，不得跳过。AI 可以建议题目，但必须经用户同意。**

**请确定幻灯片题目：**

1. ✏️ 我来指定 — 用户直接输入题目
2. 💡 AI 推荐 — AI 根据主题和素材推荐 2~3 个题目供用户选择
3. ➡️ 暂不确定 — 先生成内容，最后根据提纲拟定题目，生成前再确认

> 也可以直接说其他要求或选项

### Step 2 — 观众
1. 👨‍💻 工程师/技术团队 2. 👔 管理层/Executives 3. 💰 VC/投资人
4. 🎓 学生/教学场景 5. 📱 小红书读者/大众 6. ❓ 不确定，帮我推荐

### Step 3 — 风格调性
> 📐 除「📕 小红书图文」为 **3:4 竖版**外，其余均为 **16:9 横版**。

1. 🏢 商务/投资 Pitch 2. 💻 技术分享 3. 📄 学术/报告
4. 🚀 酷炫/发布会 5. 📕 小红书图文（3:4竖版）
6. 🪶 极简干净 7. 🌿 温暖亲和 8. ❓ 不确定，帮我推荐

### Step 4 — 内容要求（三个维度独立选择）

**A. 文字量**：1.🪶精减少文字 2.📄简要 3.📚详细阐述 4.📖大量文本

**B. 字号**：1.🔠超大(H1≥120px) 2.🔠大(H1 80-110px) 3.🔠中(H1 54-72px) 4.🔠小(H1 28-36px) 5.🔠超小(H1 20-26px)

**C. 图片**：1.🖼️主角模式(≥60%) 2.🖼️图文并茂(50/50) 3.🖼️少用图片 4.🖼️自动决定

### Step 5 — 版式布局
1. 🧑‍🎨 从零开始 2. 🎤 Tech Sharing 3. 📈 Pitch Deck 4. 🚀 Product Launch
5. 📋 周报/Weekly 6. 🎬 演讲者模式 7. 📚 课程教学 8. 📱 小红书图文(3:4竖版)

### Step 6 — 页数
**问：大概多少页？**

### Step 7 — 补充
1. ➡️ 没有，直接下一步 2. ✏️ 有，我来输入

### Step 8 — 提纲确认
```
题目：【Step 1.6确定的题目】  观众：【选项】  风格调性：【选项】  内容要求：【选择】
版式布局：【选项】  页数：【数字】  补充：【内容】
提纲：
1. ...
```

> 🔴 题目必须来自 Step 1.6。如用户选了"暂不确定"，此时 AI 必须根据提纲推荐题目并请用户确认。

---

## Step 8 — 生成与交付（两种模式共用）

> # 🔴 写入 `_slides.html` 前必须检查图片布局！
> ```
> ❌ 纯包裹容器：<figure><img ...></figure> 或 <div class="img-wrapper"><img ...></div>
> ✅ 布局中自然放置：<div class="row"><div>文字</div><img src="img://..."></div>
> ✅ 浮动图片（角落装饰/背景元素）：<img src="img://..." style="position:absolute;...">
> ```
> 🔴 **图片优先放在 flex/grid 容器中**（`.row` / `.grid` / `.two-up` / `.card`），跟随布局流动，不用绝对定位。
> 🔴 **只有跨页浮动或角落装饰**才用 `position:absolute`，直接放在 `<section>` 下。

**构建流程：**

```bash
# 1. 将幻灯片内容写入临时文件
#    图片使用 img:// 占位符语法
# 2. 插入母版
python {skill_dir}/ppt/scripts/build-ppt.py 临时工作文件/_slides.html -o 产品成果/输出文件名.html -t "页面标题" --images-dir "图片及其他资源/images"

# 3. 验证
python {skill_dir}/ppt/scripts/verify-output.py 产品成果/输出文件名.html

# 4. 清理
python -c "import os; os.remove('临时工作文件/_slides.html')"

# 5. 打开浏览器
python -c "import webbrowser; webbrowser.open('产品成果/输出文件名.html')"
```

#### 🔴 生成完成后提示

> ✅ 幻灯片已生成完毕！文件位于 `产品成果/` 目录，已自动打开。
> 
> · ✏️ 移动点击鼠标即可直接修改编辑
> · ▶️ 按播放按钮全屏播放
> · ✏️ 按 **Esc** 返回编辑状态
> · 🎨 按 **T** 循环切换 36 种主题
> · 🎬 按 **S** 演讲者模式（4张磁吸卡片）
> · 🔍 按 **O** 缩略图总览
> · 💾 按 **Ctrl+S** 保存修改（可存为自包含的独立HTML格式，任意复制）

### 🔥 图片处理（不消耗 LLM token）

```html
<img src="img://文件名.gif" alt="描述" style="max-width:400px;">
```

> 🔴 **每页至少配一张图**。**严禁手动转换 base64**。一律使用 `img://` 占位符语法。

---

# 菜单 2 — 📄 依据指定的文档生成幻灯片

## Step A — 文档选择

```bash
python {skill_dir}/core/kb2slides.py list-docs --workspace "<Vault路径>"
```

向用户展示编号列表（支持多选）。

## Step B — 知识库补充（可选）

```bash
python {skill_dir}/core/kb2slides.py search --workspace "<Vault路径>" --query "文档主题关键词" --top 10
```

## Step 2-8 — 与菜单 1 相同

---

# 菜单 3 — 🔄 转换 MS PPT

将 PowerPoint 文件（.pptx）转换为 HTML 幻灯片。

> 🔴 **仅支持知识库中已入库的 PPTX 文档。**

## Step 1 — 文档选择

```bash
python {skill_dir}/core/kb2slides.py list-docs --workspace "<Vault路径>"
```
筛选 `format` 为 `pptx` 或 `ppt` 的文档。

## Step 2-3 — 内容要求 + 补充

## Step 4 — 读取文档内容

```bash
python {skill_dir}/core/kb2slides.py read-doc --workspace "<Vault路径>" --doc "文档路径"
```

## Step 5 — AI 分析内容并设计幻灯片

### 5.2 匹配图片
- **只选用 ≥ 30KB 的图片**
- 每页 **1-3 张**大图
- 🔴 **封面优先用最大图片**

### 5.3 设计幻灯片布局

> # 🔴🔴 图片布局规范 🔴🔴
> ```
> ❌ 纯包裹容器：<figure><img src="img://a.jpg"></figure>
>                    <div class="img-wrapper"><img src="img://a.jpg"></div>
>
> ✅ 放在布局容器中：<div class="row"><div>文字</div><img src="img://a.jpg" style="width:800px;"></div>
> ✅ 浮动元素：<img src="img://a.jpg" style="position:absolute;left:900px;top:200px;width:600px;">
> ```
> 🔴 图片优先放在 `.row` / `.grid` / `.two-up` / `.card` 等布局容器中，作为正常的 flex/grid 子元素，随布局流动。
> 🔴 浮动图片（跨页背景、角落装饰等）直接放在 `<section>` 下，用 `position:absolute` 定位。

| 页面类型 | 布局思路 |
|---------|---------|
| 封面 | 图片满铺背景或大幅主视觉 |
| 目录 | 网格/列表，3-4 列 |
| 章节过渡 | 大号章节标题居中，配大幅背景图 |
| 内容-要点 | 左图右文或上图下文 |
| 内容-图文 | 图片占主导（>50% 页面积） |
| 结尾 | 简洁收尾 |

> 🔴 使用 CSS 变量引用颜色（`var(--text-1)`、`var(--bg)`、`var(--surface)` 等），**严禁硬编码颜色值（如 `#333`、`white`）**——硬编码颜色在切换主题后不可见
> 🔴 图片用 `img://` 占位符，**绝不手动转 base64**

## Step 6 — 生成并构建

```bash
python {skill_dir}/ppt/scripts/build-ppt.py 临时工作文件/_slides_pptx.html -o 产品成果/输出文件名.html -t "页面标题" --images-dir "<Vault路径>/图片及其他资源/images"
python {skill_dir}/ppt/scripts/verify-output.py 产品成果/输出文件名.html
python -c "import os; os.remove('临时工作文件/_slides_pptx.html')"
python -c "import webbrowser; webbrowser.open('产品成果/输出文件名.html')"
```

---

# 菜单 4 — ✍️ 独立生成幻灯片

> 🔴 **菜单 4 与知识库完全无关。** 不做知识库检测，不做知识库检索。

流程与菜单 1 手动模式相同，但**跳过 Step 1.5**。

---

# 🎤 Presenter Mode（演讲者模式）

按 S 打开演讲者窗口：CURRENT / NEXT / SPEAKER SCRIPT / TIMER（4张磁吸卡片）

# ✏️ Edit Mode（编辑模式）

按 E 切换：文本就地编辑、图片拖拽缩放、Ctrl+Z/Y 撤销/恢复、Ctrl+S 保存

---

# 🖼️ 图片使用规范

## 🔴 图片规则

**1. 引用方式**：一律使用 `img://文件名` 占位符，`build-ppt.py --images-dir` 自动转 base64。**严禁手动转换**。

**2. 布局方式**：
- **图文并排** → `<div class="row"><div>文字</div><img src="img://..."></div>` — 图片作为 flex/grid 子元素，随布局流动
- **卡片配图** → `<div class="card"><img src="img://...">文字</div>` — 图片在卡片内自然排列
- **浮动装饰** → `<img src="img://..." style="position:absolute;...">` — **仅限跨页背景或角落装饰**，直接放在 `<section>` 下

**3. 禁止的写法**：
- ❌ `<figure><img ...></figure>` — 无意义的纯包裹标签
- ❌ `<div class="img-wrapper"><img ...></div>` — 纯包裹容器
- ❌ `object-fit: cover/contain` + `aspect-ratio` — 会使主题切换后图片比例错乱

**4. 样式直接加在 `<img>` 上**：`border-radius`、`clip-path`、`box-shadow` 等直接写在 `<img>` 的 style 属性中。

**5. 视频同样处理**。

---

## Authoring rules（重要）

### 不可违反的规则
- **🛑 页面上不能出现工具品牌文字**
- **📁 输出到 产品成果/ 目录**
- **🔌 零外部依赖**（Google Fonts `@import` 除外）
- **🖼️ 所有图片必须通过 img:// 占位符引用**

### 必须执行的步骤
1. 写入 `<section class="slide">` HTML 到临时文件
2. 运行 `build-ppt.py` 插入母版
3. 运行 `verify-output.py`（全部 PASS 才能交付）

### 🔴 强制规则
- **必须使用 CSS 变量**（`var(--text-1)`、`var(--bg)`、`var(--accent)` 等），**严禁硬编码颜色值**。硬编码颜色在主题切换后不可见。
- **必须使用内置 CSS 类**（见下方参考表），禁止纯行内样式从零构建。行内样式仅用于定位（`position`、`left`、`top`、`width`、`height`）和微调。
- **🧱 通用排版规则**：垂直方向填满 ≥80%、不超出画布、紧凑间距
- **🖼️ 图片主角原则**：图片占 slide 面积 ≥50%、图片最大化

### CSS 类快速参考

> 🔴 以下类由 master.html 母版提供，**必须优先使用**。仅在不满足需求时才用行内样式补充。

**标题与文本：**

| 类名 | 用途 | 关键样式 |
|------|------|---------|
| `.h1` | 主标题 | 72px, 800重, 紧凑行高 |
| `.h2` | 二级标题 | 54px, 700重 |
| `.lede` | 引导语/摘要 | 22px, 浅色, 最大62字符宽 |
| `.eyebrow` | 标签/分类 | 13px, 大写, 字间距 |
| `.kicker` | 强调标签 | 14px, accent色, 大写 |
| `.dim` | 次要文字 | 灰色 |
| `.gradient-text` | 渐变文字 | 使用 `--grad` 渐变 |
| `.mono` / `.serif` | 等宽/衬线字体 | — |

**卡片与容器：**

| 类名 | 用途 |
|------|------|
| `.card` | 标准卡片（背景+边框+圆角+阴影） |
| `.card-soft` | 柔和卡片（次级背景色） |
| `.card-outline` | 线框卡片（透明背景+粗边框） |
| `.card-accent` | 顶部accent色条卡片 |

**布局：**

| 类名 | 用途 |
|------|------|
| `.row` | 水平排列（flex, gap 24px, 子元素居中） |
| `.grid` | 网格排列（grid, gap 24px） |
| `.g2` / `.g3` / `.g4` | 网格快捷列数（2/3/4列） |
| `.center` | flex纵列居中（column, 居中+文本居中） |
| `.cover-center` | 封面专用居中（column, 居中, 大标题82px） |
| `.two-up` | 左右两栏（grid, 1:1, 填满高度） |
| `.fill` | 填充剩余空间（flex:1） |

**间距：**

| 类名 | 效果 |
|------|------|
| `.mt-s` / `.mt-m` / `.mt-l` | 上边距 8/18/32px |
| `.mb-s` / `.mb-m` / `.mb-l` | 下边距 8/18/32px |

**装饰与动画：**

| 类名 | 用途 |
|------|------|
| `.divider` / `.divider-accent` | 分割线 |
| `.pill` / `.pill-accent` | 标签/徽章 |
| `.anim-fade-up` / `.anim-zoom-pop` 等 | 入场动画（27种，见 demo.html） |

**slide 属性：**

| 属性 | 用途 | 示例 |
|------|------|------|
| `data-title` | slide 标题（编辑模式显示） | `data-title="封面"` |
| `data-fx` | Canvas背景特效 | `data-fx="gradient-blob"` |
| `data-anim` | CSS入场动画 | `data-anim="anim-fade-up"` |

**常用 CSS 变量：**

| 变量 | 用途 |
|------|------|
| `--text-1` / `--text-2` / `--text-3` | 文字颜色（主/次/三级） |
| `--bg` | 页面背景色 |
| `--surface` / `--surface-2` | 卡片/面板背景色 |
| `--accent` / `--accent-2` / `--accent-3` | 强调色 |
| `--border` / `--border-strong` | 边框色 |
| `--radius` / `--radius-sm` / `--radius-lg` | 圆角 |
| `--shadow` / `--shadow-lg` | 阴影 |

### slide 写法示例

参照 demo.html 的 slide 结构，**图片作为 flex/grid 子元素随布局流动，不用绝对定位**：

```html
<!-- 封面 -->
<section class="slide is-active" data-title="封面" data-fx="gradient-blob">
  <div class="cover-center fill">
    <h1 class="h1">主标题</h1>
    <p class="lede mt-m">副标题或说明</p>
  </div>
</section>

<!-- 内容页（左文右图）—— 图片作为 .row 的 flex 子元素 -->
<section class="slide" data-title="主题名称">
  <div class="row fill" style="gap:48px;">
    <div class="fill">
      <span class="eyebrow">分类标签</span>
      <h2 class="h2 mt-s">内容标题</h2>
      <p class="lede mt-m">引导文字，使用 .lede 类保证排版一致性。</p>
    </div>
    <img src="img://配图.jpg" alt="" style="width:800px;border-radius:var(--radius);">
  </div>
</section>

<!-- 内容页（上图下文）—— 图片作为 .grid 子元素 -->
<section class="slide" data-title="图文展示">
  <div class="grid fill" style="grid-template-rows:auto 1fr;gap:24px;">
    <img src="img://配图.jpg" alt="" style="width:100%;max-height:600px;border-radius:var(--radius);">
    <div>
      <h2 class="h2">标题</h2>
      <p class="lede mt-m">说明文字</p>
    </div>
  </div>
</section>

<!-- 卡片网格（带图片） -->
<section class="slide" data-title="要点">
  <h2 class="h2">要点标题</h2>
  <div class="grid g3 fill">
    <div class="card">
      <img src="img://icon1.jpg" alt="" style="width:100%;border-radius:var(--radius-sm);margin-bottom:12px;">
      <h3 class="h3">卡片1</h3>
      <p class="dim mt-s">说明文字</p>
    </div>
    <div class="card">
      <img src="img://icon2.jpg" alt="" style="width:100%;border-radius:var(--radius-sm);margin-bottom:12px;">
      <h3 class="h3">卡片2</h3>
      <p class="dim mt-s">说明文字</p>
    </div>
    <div class="card">
      <img src="img://icon3.jpg" alt="" style="width:100%;border-radius:var(--radius-sm);margin-bottom:12px;">
      <h3 class="h3">卡片3</h3>
      <p class="dim mt-s">说明文字</p>
    </div>
  </div>
</section>

<!-- 浮动图片（仅限跨页背景/角落装饰）—— 绝对定位，直接放在 <section> 下 -->
<section class="slide" data-title="装饰">
  <img src="img://装饰.png" alt="" style="position:absolute;right:40px;bottom:40px;width:200px;">
  <div class="center fill">
    <h1 class="h1">核心观点</h1>
  </div>
</section>
```

---

## Quick start

```bash
python {skill_dir}/ppt/scripts/build-ppt.py 临时工作文件/_slides.html -o 产品成果/我的幻灯片.html -t "页面标题" --images-dir "图片及其他资源/images"
python {skill_dir}/ppt/scripts/verify-output.py 产品成果/我的幻灯片.html
python -c "import os; os.remove('临时工作文件/_slides.html')"
python -c "import webbrowser; webbrowser.open('产品成果/我的幻灯片.html')"
```

参见：[templates/demo.html](templates/demo.html) · [references/themes.md](references/themes.md) · [references/layouts.md](references/layouts.md) · [references/animations.md](references/animations.md) · [references/full-decks.md](references/full-decks.md) · [references/presenter-mode.md](references/presenter-mode.md) · [references/authoring-guide.md](references/authoring-guide.md)

## Keyboard cheat sheet

```
← → Space PgUp PgDn Home End    导航
F                               全屏
S                               演讲者模式
O                               缩略图总览
T                               循环切换主题
A                               当前页演示动画
E                               编辑/播放模式切换
L                               激光笔
Ctrl+Z Ctrl+Y                   撤销/恢复
Ctrl+S                          保存为 HTML
```

---

# 返回

**用户选择 `e` 时：返回 AHKB-CPS 统一主菜单。**
