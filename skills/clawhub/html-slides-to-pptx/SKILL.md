---
name: html-slides-to-pptx
description: >-
  编写可无损还原为 PPTX 的 HTML 幻灯片。先经引导式访谈确认样式/形式/结构并落盘
  deck-brief,再生成完整目录结构(assets/theme.css、slides/*.html、playlist.json),
  每页严格遵循 html-spec.md 规范,经 validate.js 预检零 ERROR 后用 convert.js 转成
  PowerPoint。TRIGGER when: 用户要求"做PPT/幻灯片/slides/演示文稿"、"把内容做成
  HTML幻灯片"、"生成可转PPTX的slides",或调用 /html-slides-to-pptx。DO NOT TRIGGER when:
  只需单页HTML网页、或要做的是 reveal.js/Marp 等其他幻灯片格式。
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - node
        - npm
---

# html-slides · 可无损转 PPTX 的 HTML 幻灯片生成器(引导式访谈版)

## 核心原则

转换器(`scripts/convert.js` + 浏览器端提取管线)只**无损支持 HTML/CSS 的一个子集**。
每页 HTML 必须严格遵循 `reference/html-spec.md` —— 这是契约,不是建议。
写页面之前必须先完成 Step 1 访谈并让用户确认 `slides/deck-brief.md`。

## 首次使用:检查工具依赖

> 以下命令中的 `SKILL_DIR` 指本技能的根目录(即 SKILL.md 所在目录)。
> 技能加载时系统会显示 "Base directory for this skill: <路径>",用该路径替换 `SKILL_DIR`。

```bash
SKILL_DIR="<技能根目录,即 Base directory>"
ls "$SKILL_DIR/scripts/node_modules/playwright" >/dev/null 2>&1 \
  && echo OK || (cd "$SKILL_DIR/scripts" && npm install && npx playwright install chromium)
```
若输出 OK 则跳过安装;否则等待安装完成再继续。

## 工作流程(按顺序执行)

### Step 1 · 引导式访谈 → 需求确认卡

**读 `reference/interview-guide.md` 并严格执行**:五阶段(定位→结构→视觉→版式→输出)
10 问 + 大纲确认,每问有默认值与智能跳过规则。配套查询:
- 叙事骨架:`reference/narrative-skeletons.md`(脚手架非模具;用户可选"自由结构")
- 色板预设:`reference/theme-presets.md`(5 套预设 + 自定义 hex 推导)
- 信息密度:`reference/density-tiers.md`(演讲/混合/阅读 三档参数)

访谈收尾:按 `assets/deck-brief.template.md` 生成确认卡展示给用户,
**用户确认后落盘 `slides/deck-brief.md`** —— 此后它是唯一执行事实源;
后续"改第 N 页/换色板"类迭代直接读它,不重访谈。

### Step 2 · 搭目录结构
在当前工作目录生成:
```
assets/theme.css          # 按 brief 色板:复制 assets/presets/<选定预设>.css(自定义色则按推导值生成)
slides/NN-slug.html       # 每页一个文件,两位数字前缀排序
slides/playlist.json      # 从 assets/playlist.template.json 实例化,playlist 按顺序列全页面
slides/deck-brief.md      # Step 1 落盘的需求确认卡
slides/slides.config.json # 可选:项目级转换配置(键见 scripts/config/default.config.js)
```
目录已存在时,保留用户已有文件,只补缺失项。

### Step 3 · 逐页写 HTML
1. **按 brief 的骨架页序与密度参数写**(要点数/行数/字号是硬约束;超标:演讲/混合档拆页,阅读档精简措辞)
2. **选起点**(三模板 + 片段库 + 配方):
   - `assets/slide-template.html`(方式 A)/ `slide-template-flex.html`(B)/ `slide-template-layout.html`(C)
   - `assets/snippets/`(14 个片段:页头/卡片/KPI/流程步骤/时间线节点/对比卡/代码块/引用块/数据表格/渐变英雄区等,INDEX.md 有参数表)
   - `reference/layout-recipes.md`(三卡片/分栏/统计带/条目堆叠)
2.5 **P2 高级特性**(按需使用,详见 html-spec.md §5):
   - `data-shape="chevron|star5|rightArrow|..."` → 80+ 预设几何(流程图/箭头/星形)
   - `data-chart='{"type":"bar",...}'` → 原生可编辑图表(bar/line/area/pie)
   - `<img data-object="true">` → 原生可编辑图片(object-fit 映射)
   - `<video poster src>` / `<audio src>` → 原生音视频嵌入
   - 转场/母版:由 playlist.json / slides.config.json 配置,非页面内属性
3. **布局选择**:骨架(页头/页脚)用方式 A;成组内容(卡片/格子/条目)优先方式 C 或 B(brief 另有指定时从其指定)
4. **不改结构规则**:
   - 画布 `1920x1080`,`.slide-container` relative + overflow hidden
   - 每个可见元素可归结到 `data-object="true"`;嵌套标记 = ERROR
   - 多行文字显式 `line-height`;字重只用 400/600/700/800/900
   - 文字纯色(半透明先预算混合色);强调条用独立细长 shape;装饰不用伪元素/opacity
   - 纯 `transform:rotate()` 已支持(scale/skew/translate 仍禁);方式 C 子级禁写 position/left/top/width/height
5. 备注按 brief 的备注策略写 `<template data-slide-notes>`

### Step 4 · 预检(必须零 ERROR)
```bash
node "$SKILL_DIR/scripts/validate.js" slides/
```
- ❌ ERROR → 必须修复后重跑,直到 0 ERROR
- ⚠️ WARN → 逐条判断是否可接受(见 html-spec.md 速查表),可接受就在汇报中说明

### Step 5 · 转换
```bash
node "$SKILL_DIR/scripts/convert.js" ./slides ./slides/playlist.json output.pptx
```

### Step 6 · 汇报
告知用户:PPTX 路径、页数、validate 结果(残留 WARN 及理由)、备注写入情况、deck-brief.md 位置。
如用户装了 PowerPoint,可提示可直接打开 output.pptx 检查。

## 转换机制简述(排查问题时读)

- 管线:加载页面 → 等字体就绪+稳定 → 注入提取脚本 → data-layout 解析 → 提取基元 → 截图 pass → pptxgenjs 渲染
- **原生可编辑**(PPT 中可修改):文字/纯色形状/图片/表格/图表/列表/上下标/字距/渐变(opt-in)/预设几何/旋转/虚线边框
- **截图贴回**(不可编辑):渐变(默认)/background-image/SVG/视觉特效/mix-blend-mode/clip-path(2x DPI,截图前隐藏文字避免重影)
- 文字 run 级样式:斜体/下划线/删除线/超链接/text-transform 原生还原;`<sup>`/`<sub>` 原生上下标
- 配置:`config/default.config.js` 是唯一事实源;项目级 `slides/slides.config.json` 覆盖(如 `{"nativeGradient":true}` 开启原生渐变;`{"master":{"pageNumbers":true}}` 开启页码;`{"incrementalCache":false}` 关闭增量缓存)
- 转场:playlist 项 `{"file":"01.html","transition":"fade"}` → p:transition(fade/push/wipe/cover/split)
- 音视频:`<video poster src>` / `<audio src>` → addMedia 原生嵌入
- 增量缓存:HTML 未变时跳过提取/截图(11x 提速);缓存目录 slides/.cache/
- 叠放 = DOM 深度优先顺序;z-index 只影响浏览器合成
- `<template data-slide-notes>` → 写入该页备注
- 创意布局:`reference/creative-layouts.md` 含 8 种模式 + 特性决策树;写页前必读
- 回归:`node "$SKILL_DIR/scripts/test/golden.js" verify` 三层等价(L1 提取+L2 XML+L3 截图);行为契约见 `reference/behavior-baseline.md`

## 文件清单
- `reference/interview-guide.md` — **引导式访谈指南(Step 1 必读)**
- `reference/narrative-skeletons.md` — 4 套叙事骨架(脚手架非模具)
- `reference/theme-presets.md` — 通用色板预设速查 + 自定义推导
- `reference/brand-styles.md` — 11 个品牌风预设档案 + 58 品牌按需蒸馏 SOP
- `reference/density-tiers.md` — 信息密度三档参数
- `reference/html-spec.md` — 编写规范(契约),写页面前必读
- `reference/layout-recipes.md` — 版式配方(方式 B/C 基础骨架)
- `reference/creative-layouts.md` — **创意布局手册**(P2 新特性组合技巧:渐变/预设几何/上下标/原生图表表格/旋转/虚线/阴影的 8 种创意模式 + 特性选择决策树;写页前必读)
- `reference/behavior-baseline.md` — 行为快照与怪癖决策(改转换器前必读)
- `assets/theme.css` — 默认色板;`assets/presets/` — 5 套色板预设
- `assets/deck-brief.template.md` — 需求确认卡模板
- `assets/slide-template{,-flex,-layout}.html` — 三套样板页(方式 A/B/C)
- `assets/snippets/` — 14 个高频片段(页头/卡片/KPI/流程/时间线/对比/代码/引用/表格/渐变英雄区;INDEX.md 索引)
- `assets/playlist.template.json` — playlist 模板
- `scripts/validate.js` — 规范预检器(ERROR/WARN 分级)
- `scripts/convert.js` — 转换 CLI(config/core/extract/render 分层)
- `scripts/test/` — golden 回归 harness、测绘、阶段验收、walkthrough、preset-parity
