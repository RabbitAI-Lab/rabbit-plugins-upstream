---
name: pptx-craft
description: "把结构化数据/看板/报表渲染成【可编辑】PowerPoint(.pptx), 重点=高质量排版(不重叠/有气口/不裁切)。引擎用文本优先多遍布局+模板克隆——你给PPT模板路径, 它自动测量可用区、原生生成内容填进去(零复制粘贴, 继承主题)。触发词: 做一份可编辑PPT / 用我的模板生成PPT / 把这个看板导出成PPT / pptx-craft。注意: 引擎吃数据模型, 不解析HTML。"
agent_created: true
---

# PPT 渲染引擎 (数据模型 → 可编辑PPT · 模板克隆 / 尺寸锚定)

> **原命名 html2ppt 已不准确** —— 本技能并非"解析 HTML 转 PPT", 已正式更名 **`pptx-craft`**。它从一份**数据模型**渲染可编辑 PPT;
> HTML / 画布只是用户在过程中可选的"可视化预览兄弟产物", **不参与引擎输入**。引擎只认数据。

## Positioning (价值观: 数据模型→PPT, 模板为锚点)

- **单一真相源 = 数据模型**, 不是 HTML、不是画布。三者(画布/HTML/PPT)都从同一份数据长出来。
- **PPT 模板是尺寸锚点**。收到请求第一步就确认"有没有专用模板"; 有模板则内容以模板真实可用区为准**原生生成**, 画布/HTML/PPT 尺寸天然一致。
- **"尺寸不匹配能不能自适应"是个伪问题**: 当模板作锚点、内容原生生成时, 没有第二个尺寸需要去匹配 —— 自适应 = 以模板为准直接生成, 而非事后缩放去凑。
- **HTML 是可选的**: 用户可以用 HTML 快速预览版面(尤其技术用户), 也可以直接用画布/表单, 都不影响引擎。引擎吃的是数据。

## Overview

Generate editable, pixel-precise PowerPoint files **without hand-computing absolute
coordinates**. The root cause of "PPT 永远做不好排版、永远元素重复、永远没气口" is that
PPT / pptxgenjs is an absolute-positioning engine: 50+ elements = 200+ hand-written
`(x,y,w,h)`, and one miscalculation cascades into overlap/truncation. Worse, even when
coordinates are correct, the gaps (气口) between elements end up too tight because the
layout is a single sequential pass that packs elements to "minimal fit".

This skill replaces hand coordinates with a **text-first multi-pass layout** that
simulates how a human actually builds a slide:

```
人类工作流                        引擎对应 Pass
─────────────────────────────    ──────────────────────────────
1. 按尺寸/比例画区域边框          Pass0   flex 容器(区域框)
2. 先放文字(占地最大),四周留白;    Pass1   文本优先放置(字体度量测高 + pad 气口)
   放不下则缩字号(不删内容)        Pass2   字号自适应(溢出按比例缩,保最小字号)
3. 再放装饰(条/图)填空余空间       Pass3   装饰按"文字块底部+气口"定位(填空者)
4. 初稿→QA→二稿→QA→终稿           Pass4-5 QA 迭代(留白不足全局缩字号重排,最多3轮)
```

Key guarantee: **no overlap, no truncation, and measured breathing room (气口)** — the
validator refuses to write the file unless every element is in-bounds, non-overlapping
across groups, and cross-group gaps meet a `MIN_BREATH` floor.

## When to use

- User needs an **editable** PPT (not a screenshot image) with **high layout fidelity + 气口**.
- User explicitly wants "方法3" (text-first flex engine + validator) over "方法1" (screenshot).
- User has a dashboard / report / data page — designed in HTML, a design canvas, OR just a
  data model / spreadsheet — and wants it re-rendered as a clean editable slide with proper spacing.
- **模板克隆场景**: 用户有现成 PPT 模板(公司汇报模板等), 要把内容填进去且继承主题/页脚/logo。
- Do NOT use for one-off quick mockups where a screenshot (方法1) is acceptable — that
  is faster and lower-cost.

## Architecture (6 layers)

```
① 输入层   : 数据模型(真相源) + 设计令牌(TOKENS) + 间距令牌(SP) + 密度(DENSITY)
             —— HTML/画布是可选的可视化兄弟产物, 不进引擎输入
② 虚拟画布 : 1440×680 px 抽象坐标空间(可随目标比例重设 VW/VH), 均匀缩放+居中 映射目标可用区
③ 容器系统 : Row/Column + flex 权重, 仅用于"区域框"层级(区域内部改文本优先)
④ 组件库   : KpiCard / CompareCard / build_chart / build_progress  —— 内部文本优先, 装饰填空
⑤ 文本优先布局 : layout_texts() 字体度量测高 + 上下左右 pad 气口 + 字号自适应(保最小,不删内容)
⑥ 校验层   : 写文件前强制 越界 + 跨组重叠 + 留白下限(防拥挤) 检测; 不过则拒绝产出(终稿轮)
⑦ QA迭代器 : 初稿→二稿→终稿, 用留白提示驱动全局字号缩放(G_TS)
```

> **气口(呼吸感)是怎么解决的 (v3 三条杠杆)**:
> 1. **文本优先 + 字体度量**: 文字先"占地"，上下左右按 `pad` 留气口、多文字间按 `breath` 留气口，
>    尺寸由字体度量真实估算（宁多勿少，文字绝不裁切），不再"塞满即止"。
> 2. **间距令牌 + 密度系数**: 所有 gap/padding 取自 `SP` 阶梯表，由 `DENSITY` 整体缩放
>    （1.0 紧凑 / 1.2 舒适 / 1.4 宽松）—— 调一个旋钮即可整体松紧，不用逐块挪。
> 3. **QA 迭代器**: 若终稿仍有留白提示，全局缩小字号 `G_TS`（每轮 -0.06）重排，最多 3 轮，
>    用"规则+迭代"替代"人眼反复截图调"。

## Workflow

### ⚠️ Step 0 — 确认有无专用 PPT 模板 (MANDATORY, 任何技能请求的第一步)
收到技能请求时, **第一件事**就是问用户: **"你有没有专用 PPT 模板？"**
不要先谈 HTML 尺寸、不要先问画布比例 —— 模板才是唯一锚点。这个回答决定整个输入契约与引擎首动作。

**为什么先问模板 (尺寸一致性的根因)**:
PPT 翻车第一因是"生成物与目标模板尺寸/比例不一致 → 复制进去变小/错位"。当模板作锚点,
内容永远按模板本身的真实可用区**原生生成**, 不存在"另一个尺寸去匹配"的对象 ——
于是"HTML尺寸和PPT尺寸不匹配、能不能自适应"这个伪问题从根上消失: **自适应不是去匹配, 而是以模板为准直接生成。**

**Branch A — 无专用模板 (`use_generic: true`)**
- WB 自行设计/加载**内置通用模板**(默认标准16:9, 33.87×19.05cm, 含内置主题token)。
- 引擎动作: 新建 `Presentation` + 设尺寸 + 文本优先多遍 + QA。
- 仅需确认输出比例(默认16:9), 无需路径。

**Branch B — 有专用模板 (`has_template: true`)** — 用户只需提供:
1. **`template_path`** (必填): 真实 `.pptx` 模板路径。
2. **`start_page`** (可选, 默认自动探测首个"正文页"): 内容从这一页开始生成; 模板封面/目录/结构页(P1-3等)一律不动。
- **可用区由 WB 自动测量, 用户无需画框、无需报尺寸**:
  引擎加载模板 → 扫描目标页**及其版式(layout)/母版(master)的已有形状** → 按规则算可用区:
  - 左右: 按 PPT 模板尺寸各留 `MARGIN_CM`(默认1cm) → `x∈[M, W-M]`。
  - 上下: 在模板已有元素基础上算(内容不得压已有元素), 各留 `MARGIN_CM`:
    * 排除面积≈整页的形状(全屏背景图), 避免误判为障碍物;
    * 形状中心在上半=页眉区取 `max(页眉底)+M`, 在下半=页脚区取 `min(页脚顶)-M`;
    * 无页脚页 bottom 回退 `H-M`; 溢出续页时对后续页用同规则重算。
  - **必须同时扫描 `slide.shapes` + `slide.slide_layout.shapes`**(页眉页脚通常在版式上, 漏扫会压页脚)。
- 引擎动作: `Presentation(template_path)` → 克隆 → 在算出的可用区**原生生成**内容(直接 add 进 spTree, 零复制粘贴)。主题/字体/页脚/logo 全继承。
- (可选硬覆盖) 极少数模板自动测量不准时, 才退化为用户在模板里标命名形状 `CONTENT_AREA` 或手填包围盒 `(x_cm,y_cm,w_cm,h_cm)`。

> 经验: 曾用「缩放粘贴」(整页生成→×0.796缩放进可用区) 导致"整体小一圈"; 正确范式是**虚拟画布直接映射到可用区 + 原生生成**, 字号走 px→pt 不随区域缩小。

Reference sizes (used by Branch A default or as sanity check):
| Type | Width × Height | Ruler range | Aspect |
|------|---------------|-------------|--------|
| Standard 16:9 | 33.87 × 19.05 cm | -16~+16 / -9~+9 | 1.78:1 |
| Standard 4:3 | 25.4 × 19.05 cm | -12~+12 / -9~+9 | 1.33:1 |
| Custom ultra-wide | 31 × 14 cm | -15~+15 / -6~+6 | 2.21:1 |

### Step 1 — Define tokens and data (single source)
Set `TOKENS` (colors/fonts/radii) and a `DASHBOARD_DATA`-style model. This is the **single
source of truth** — keep it consistent with any HTML/canvas sibling so all outputs stay
aligned (but HTML/canvas are optional previews, not inputs). If the data is "live", pass a
snapshot at export time (PPT is a period snapshot, not realtime).

### Step 2 — Build the virtual canvas + coordinate mapper
Use `VW,VH` as the virtual pixel canvas. **VW/VH should be derived from the target available
area's aspect ratio** (not hardcoded to one size) so the layout re-flows natively:
- **Branch A (generic)**: `VW,VH` → slide size aspect; `SCALE = min(SLIDE_W/VW, SLIDE_H/VH)`, `OFFX` centers.
- **Branch B (template clone)**: set `VW=1440, VH=round(area_h/area_w*1440)`, `SCALE=area_w/VW`,
  and `OFFX/OFFY` = available-area top-left EMU — content placed *inside the frame*, natively.
Map with **uniform scale + area anchoring** (no vertical squeeze). Helpers `X/Y/W_/H_/FS` convert virtual px → EMU/pt.
Slide size: `prs.slide_width = Emu(target_cm * 360000)` (Branch A only; Branch B reuses template size).

### Step 3 — Lay out regions with flex containers (never raw coordinates)
Use `hbox(deck, box, items, gap, pad)` and `vbox(deck, box, items, gap, pad)` to carve
**region frames** only. Each item is `{"flex": n, "size": px, "group": "g", "build": fn}`.
The engine computes child positions from weights — change a parent's height and children
reflow. **Note**: flex is used for the region level; inside each card the layout switches
to text-first (Step 4).

### Step 4 — Compose with the component library (TEXT-FIRST inside)
Call `KpiCard`, `CompareCard`, `build_progress`, `build_chart`. Each card:
1. draws its background rect,
2. calls `layout_texts(deck, items, box, pad, breath, ...)` which:
   - measures each text block height via `text_h()` (font metrics, CJK-aware),
   - places text top-down with `pad` (outer) + `breath` (between) 气口,
   - if total exceeds box height, binary-searches a uniform `scale` to shrink all fonts
     (each keeps its `min_fs` — **content never deleted**),
   - returns the `leftover` space below the text,
3. draws decorative elements (bars/chips/legend) into that `leftover` space — decorations
   are "fillers", never the cause of overlap.

This is the core fix for "标题贴边 / 标签没气口 / 批次条拥挤": text owns the space first,
decorations fill what's left.

### Step 5 — Run the validator BEFORE saving
`validate(deck.recs)` returns `(errors, warnings)` and checks three things:
1. **越界** — every element within the target area bounds;
2. **跨组重叠** — any two elements of *different* groups that geometrically intersect
   (same-group = text nested in its card, which is allowed);
3. **留白下限 (防拥挤)** — any two *adjacent* cross-group elements whose edge-to-edge gap
   is `< MIN_BREATH` (default 10px) is reported as a warning.

If `errors` non-empty → **raise, do not write the file**. Warnings do not block (tuning
hints for `DENSITY`/`G_TS`) but a clean run reports "留白校验通过".

### Step 5b — Tune 气口 (no coordinate edits)
Three knobs, in increasing strength:
- `SP_RAW` ladder + `DENSITY` (1.0/1.2/1.4) — global spacing scale; `sp(k)` = `SP_RAW[k]*DENSITY`.
- `pad` / `breath` args inside `layout_texts` — per-card inner 气口.
- `G_TS` (driven by QA iterator) — global font-size scale when gaps still too tight.

The engine also emits `preview.svg` (virtual-coord 1:1) so you can
eyeball 气口 without opening PowerPoint.

### Step 6 — Render and save
`deck.render(slide)` iterates recorded ops into python-pptx shapes. Set slide background
fill, then `prs.save(out)`.
- **Branch A**: save as a new standalone file.
- **Branch B**: save the cloned template (content already inside the available area) — the
  output file is the user's template, filled.

## The bundled engine

`scripts/pptx_flex_engine.py` is a complete, runnable reference implementation (the
switch-migration dashboard case) using the v3 text-first multi-pass architecture.

- Run directly: `python scripts/pptx_flex_engine.py` → produces `migration-dashboard-m3-v4.pptx`
  + `migration-dashboard-m3-preview.svg` (standard 16:9, 33.87×19.05cm single-page editable deck).
- **Before running, resolve Step 0**:
  - Branch A (no template): the script's defaults already target standard 16:9 — just run.
  - Branch B (has template): pass `template_path` (+ optional `start_page`); the engine
    **auto-measures the template's available area** (scans slide + layout shapes) and fills
    it natively — no `CONTENT_AREA` box or manual dimensions needed.
- Adapt: replace `KPI / CMP / BATCHES / DAYS` data + `build_*` functions with target content;
  keep `TOKENS`, `hbox/vbox`, `layout_texts`, `Deck`, and `validate` unchanged.
- Prereqs: `python-pptx` (`pip install python-pptx`). Uses `Microsoft YaHei` for editable
  Chinese text on Windows.

## Key rules (non-obvious, learned from real failures)

- **🔴 Step 0 is mandatory — 第一件事就问"有专用模板吗?"**: 模板是尺寸锚点。Branch A 自设计通用16:9;
  Branch B 用户给 `template_path`(+可选 `start_page`), **WB 自动扫描模板算可用区**(无需画框/报尺寸),
  原生生成进 spTree。模板克隆让 PowerPoint 复制粘贴过时(无坐标漂移, 风格自动继承)。
  → 因此"画布/HTML/PPT 尺寸一致性"由模板锚点天然保证, "尺寸不匹配"伪问题消失。
- **可用区自动测量规则**: 扫描 `slide.shapes` + `slide.slide_layout.shapes` + (必要时) `slide.master.shapes`;
  排除全屏背景; 上下按已有元素留 `MARGIN_CM`; **漏扫 layout 会压页脚**(页眉页脚多在版式上)。
- **content_area 是盒不是尺寸**(仅当自动测量不准时作硬覆盖): 手填须问左上偏移。
- **Never hand-write `(x,y,w,h)` for leaf elements** — declare structure, let the engine compute.
- **Text-first, not decoration-first**: always place text (with 气口) before bars/chips;
  decorations fill leftover space. This is what killed the "标题贴边/标签没气口" bugs.
- **Font metrics over eyeballing**: `text_h()` estimates CJK-aware line height; tune the
  `0.98/0.55/0.30` width factors if a font renders differently, but keep them conservative
  (prefer slightly-too-tall over clipping).
- **Auto-shrink but never delete**: `min_fs` per text item guarantees content survives
  even when the frame is tight — the QA iterator then relaxes spacing globally.
- **Always give each card a distinct `group`** so the validator can tell nested-text from
  real overlap. Forgetting this yields false overlap errors or missed collisions.
- **Uniform scale + area anchoring** (not non-uniform): prevents the vertical
  squeeze that makes PPT feel tighter than the HTML source.
- **Method 1 vs 3 split**: method 1 (screenshot) for urgent/low-stakes reporting;
  method 3 (this engine) for anything where the user must edit text in PowerPoint or
  demands zero-drift layout with proper 气口.

## 产品命名体系 (上传 WB 用, 2026-07-22 定稿)

为把"个人孵化 → 多场景覆盖 → 产品/专家化"这条路径固化, 命名分三层, 彼此解耦:

| 层级 | 名称 (id) | 显示名 | 角色 |
|------|-----------|--------|------|
| **SKILL** (引擎) | `pptx-craft` | PPT匠·可编辑生成引擎 | 数据模型→可编辑PPT + 文本优先多遍 + QA + 模板克隆 |
| **EXPERT TEAM** (专家团) | `ppt-studio` | PPT工作室 | 编排多个子专家, 拆解需求并派活 |
| 子专家 (团队内角色) | 见下 | 版式专家 / 数据专家 / QA专家 / 主题专家 | 各管布局 / 适配 / 校验 / 美化 |

- **技能 `pptx-craft` 是地基**: 不挑使用者, 只吃结构化数据 (人格无关)。
- **专家团 `ppt-studio` 是人格封装**: 同一引擎, 不同上车点 ——
  - `技术流专家` (吃 HTML / 数据模型, 适合你本人)
  - `零代码专家` (吃画布 / 表单, 适合非技术同事)
- **子专家 = 把"文本优先多遍"的每一遍拆成独立角色**, 由 `ppt-studio` 编排专家串起来:
  - 版式专家 (布局/flex/气口) · 数据专家 (源适配器: HTML/画布/表单→数据模型) ·
    QA专家 (校验/迭代) · 主题专家 (美化/模板主题 token)。

> 命名原则: 名称落到"能力本质"(数据驱动 / 可编辑 / 工艺感), 而非"输入介质"(HTML);
> 因此**强烈建议不要回退到 html2ppt 这类介质名**, 以免重新埋下"引擎解析 HTML"的预期坑。
