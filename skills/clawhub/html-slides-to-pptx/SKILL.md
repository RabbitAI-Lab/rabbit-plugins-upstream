---
name: html-slides-to-pptx
description: >-
  编写可无损还原为 PPTX 的 HTML 幻灯片。先经引导式访谈确认样式/形式/结构并落盘
  deck-brief,再生成完整目录结构(assets/theme.css、slides/*.html、playlist.json),
  每页严格遵循 html-spec.md 规范,经 validate.js 预检零 ERROR 后用 convert.js 转成
  PowerPoint。TRIGGER when: 用户要求"做PPT/幻灯片/slides/演示文稿"、"把内容做成
  HTML幻灯片"、"生成可转PPTX的slides",或调用 /html-slides-to-pptx。DO NOT TRIGGER when:
  只需单页HTML网页、或要做的是 reveal.js/Marp 等其他幻灯片格式。
version: 1.1.0
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

**读 `reference/interview-guide.md` 并严格执行**:六阶段(定位→结构→视觉→版式→输出)
16 问 + 大纲确认,每问有默认值与智能跳过规则。配套查询:
- 叙事骨架:`reference/narrative-skeletons.md`(脚手架非模具;用户可选"自由结构")
- 色板预设:`reference/theme-presets.md`(5 套预设 + 自定义 hex 推导)
- 信息密度:`reference/density-tiers.md`(演讲/混合/阅读 三档参数)
- **内容深化:`reference/content-deepening.md`**(Q3b 档位触发:四步追问审素材 → 多角色深化 → 决策委员会审大纲;大纲 v2 才进 Q5 确认)

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
slides/slides.config.json # 项目级转换配置(键见 scripts/config/default.config.js)
```
目录已存在时,保留用户已有文件,只补缺失项。

**slides.config.json 按 brief 生成**:
```json
{
  "design": {
    "tier": "presentation | mixed | reading",
    "minBodyPx": 14,
    "fillThreshold": 0.85,
    "airyPages": ["01-cover.html", "05-statement.html"]
  }
}
```
- `design.tier` 由 brief 使用场景映射(演讲→presentation/混合→mixed/阅读→reading);
  配置后 validate 的设计检查(文字适配/字号下限/画布填充/对齐)才启用
- `airyPages` 填 brief 中的 airy 页文件名(封面/分隔/大字观点/引用/收尾)
- 其余常用键:`applyFontMap`(brief 演示机字体决定)、`nativeGradient`(原生渐变)、`master`(页码页脚)

### Step 3 · 逐页写 HTML
1. **按 brief 的骨架页序与密度参数写**(要点数/行数/字号/填充率是硬约束;超标:演讲/混合档拆页,阅读档精简措辞)
2. **先读设计契约,再选页面形态**:
   - `reference/design-principles.md` — 设计总纲(版面分区/字号阶/scale-to-fill/去 AI 味 12 条反模式),**写页前必读**
   - `reference/page-archetypes.md` — **20 个页面原型(首选起点)**:按 brief 大纲表给每页指派的原型,复制骨架改内容
   - `assets/slide-template.html`(方式 A 要点列表)/ `slide-template-flex.html`(B 不对称分栏)/ `slide-template-layout.html`(C 大数字带)
   - `assets/snippets/`(20 个片段:议程/分隔/大字观点/引用/编辑双栏/出血大图 + 页头/卡片/KPI/流程/时间线/对比/代码/表格等,INDEX.md 有参数表与使用限制)
   - `reference/layout-recipes.md`(容器内部写法:三卡片/分栏/统计带/条目堆叠)
2.5 **P2 高级特性**(按需使用,详见 html-spec.md §5;**用法克制,以 design-principles 为准**):
   - `data-shape="chevron|star5|rightArrow|..."` → 80+ 预设几何(流程图/箭头/星形)
   - `data-chart='{"type":"bar",...}'` → 原生可编辑图表(bar/line/area/pie)
   - `<img data-object="true">` → 原生可编辑图片(object-fit 映射;图片政策见 brief)
   - `<video poster src>` / `<audio src>` → 原生音视频嵌入
   - 转场/母版:由 playlist.json / slides.config.json 配置,非页面内属性
3. **布局选择**:骨架(页标题/页码)用方式 A;成组内容(条目/分栏/数字带)优先方式 C 或 B(brief 另有指定时从其指定)
4. **不改结构规则**:
   - 画布 `1920x1080`,`.slide-container` relative + overflow hidden
   - 每个可见元素可归结到 `data-object="true"`;嵌套标记 = ERROR
   - 多行文字显式 `line-height`;字重只用 400/600/700/800/900
   - 文字纯色(半透明先预算混合色);装饰预算每页 ≤2 件;默认左对齐
   - 纯 `transform:rotate()` 已支持(scale/skew/translate 仍禁);方式 C 子级禁写 position/left/top/width/height
5. 备注按 brief 的备注策略写 `<template data-slide-notes>`

### Step 3.5 · 视觉自查(写完页先过自己这关)
```bash
node "$SKILL_DIR/scripts/preview.js" slides/
```
把每页截成 PNG(slides/.preview/),**逐张看图**,按四条自查:
1. **填充率**:内容带是否撑满 320-940?底部留白大 → 回 Step 3 按 scale-to-fill 放大字号/行距
2. **字号**:正文是否明显偏小(<22px 观感)→ 对照 brief 字号参数
3. **对齐**:卡片/条目边缘是否齐;间距是否一致 → 修正坐标或改方式 B/C
4. **去 AI 味**:对照 brief 的约束清单(kicker/结论条/渐变条是否超编;装饰 ≤2 件;高亮 ≤1 处)
发现问题**就地修复并重截**,直到四关全过,再进 Step 4。

### Step 4 · 预检(必须零 ERROR)
```bash
node "$SKILL_DIR/scripts/validate.js" slides/
```
- ❌ ERROR → 必须修复后重跑,直到 0 ERROR
- ⚠️ WARN → 逐条判断是否可接受(见 html-spec.md 速查表),可接受就在汇报中说明
- 设计 WARN(文字适配/字号下限/画布填充/对齐,由 slides.config.json 的 design 键启用)→ 优先按 scale-to-fill 修复,这正是视觉质量的自动守门员

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
- 特性速查:`reference/creative-layouts.md` 查渐变/几何/图表等写法(含使用限制);页面形态以 page-archetypes.md 为准
- 回归:`node "$SKILL_DIR/scripts/test/golden.js" verify` 三层等价(L1 提取+L2 XML+L3 截图);行为契约见 `reference/behavior-baseline.md`

## 文件清单
- `reference/interview-guide.md` — **引导式访谈指南(Step 1 必读;6 阶段 16 问)**
- `reference/content-deepening.md` — **内容深化手册(四步追问/多角色/决策委员会;大纲确认前)**
- `reference/design-principles.md` — **设计总纲(版面分区/字号阶/scale-to-fill/去 AI 味 12 条;写页前必读)**
- `reference/page-archetypes.md` — **20 个页面原型库(写页首选起点)**
- `reference/narrative-skeletons.md` — 4 套叙事骨架(脚手架非模具;推荐原型列)
- `reference/theme-presets.md` — 通用色板预设速查 + 自定义推导
- `reference/brand-styles.md` — 11 个品牌风预设档案 + 58 品牌按需蒸馏 SOP
- `reference/density-tiers.md` — 信息密度三档参数(含填充下限与 scale-to-fill)
- `reference/html-spec.md` — 编写规范(转换契约),写页面前必读
- `reference/layout-recipes.md` — 版式配方(方式 B/C 基础骨架)
- `reference/creative-layouts.md` — 特性速查手册(渐变/预设几何/上下标/图表/旋转/虚线/阴影写法;含使用限制)
- `reference/behavior-baseline.md` — 行为快照与怪癖决策(改转换器前必读)
- `assets/theme.css` — 默认色板+版面变量;`assets/presets/` — 16 套色板预设
- `assets/deck-brief.template.md` — 需求确认卡模板
- `assets/slide-template{,-flex,-layout}.html` — 三套样板页(方式 A/B/C,各演示一个原型)
- `assets/snippets/` — 20 个片段(6 原型直出 + 基础构件;INDEX.md 索引与使用限制)
- `assets/playlist.template.json` — playlist 模板
- `scripts/validate.js` — 规范预检器(ERROR/WARN 分级;design profile 启用设计检查)
- `scripts/preview.js` — 视觉自查截图(Step 3.5;slides/*.html → .preview/*.png)
- `scripts/convert.js` — 转换 CLI(config/core/extract/render 分层)
- `scripts/test/` — golden 回归 harness、测绘、阶段验收、walkthrough、preset-parity
