# text-to-infographic v0.2.1

中文 | [English](#english)

## 中文

`text-to-infographic` 是一个**独立的 infographic-first skill 包**，目标不是讲故事，而是把复杂信息压缩成一张适合嵌入：
- 飞书文档
- 飞书表格 + 画板
- 白板
- SVG 设计流

中的 **overview 图**。

它优先解决的是：
- information hierarchy
- 可编辑性
- 可扫描性
- 多工具协同编排

而不是 comic / picture-book 那种叙事节奏。

### 适合的图表

- 增长飞轮
- 鱼骨分析
- 价值金字塔
- 桑基图
- 产品路线图
- SaaS 仪表盘
- 流程图
- 框架图
- 对比图

### 工具链定位

这个包采用 **内容/布局 schema + adapter** 的结构：

- `schemas/infographic-plan.schema.json`
  - 定义结构化 infographic plan
- `scripts/validate_infographic_plan.py`
  - 校验 schema 子集、默认映射、引用完整性、文本预算
- `scripts/render_infographic_html.py`
  - 从 plan 渲染**自包含 HTML 成品**（零依赖、可打印、可嵌入飞书）
- `scripts/render_infographic_png.py`
  - 从 plan 导出 **PNG 分享图**（调用系统 Chrome via CDP，零 Python 依赖）
- `scripts/build_infographic_adapters.py`
  - 从 plan 生成最小 adapter 草稿（SVG / whiteboard / doc）

可对接的下游工具：
- `lark-cli`
- `@larksuite/whiteboard-cli`
- SVG 自由设计工作流
- 飞书文档 v2 API

当前版本默认输出**自包含 HTML 成品图**（主交付），并保留 adapter 草稿作为可选扩展，不把 schema 直接绑定到任何单一工具的底层节点结构。

### 目录结构

```text
.
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── skill-card.md
├── schemas/
│   └── infographic-plan.schema.json
├── examples/
│   ├── infographic-demo.json
│   ├── infographic-flywheel-demo.json
│   ├── infographic-fishbone-demo.json
│   ├── infographic-pyramid-demo.json
│   ├── infographic-sankey-demo.json
│   ├── infographic-roadmap-demo.json
│   └── infographic-dashboard-demo.json
└── scripts/
    ├── validate_infographic_plan.py
    ├── render_infographic_html.py
    ├── render_infographic_png.py
    └── build_infographic_adapters.py
```

### 默认映射

默认布局映射：
- `flywheel -> radial + polar + clockwise`
- `fishbone -> spine-branch + cartesian + left-to-right`
- `pyramid -> pyramid + cartesian + top-to-bottom`
- `roadmap -> timeline + cartesian + left-to-right`
- `dashboard -> dashboard + cartesian + left-to-right`

默认交付映射：
- `primary_target=html`
- `secondary_targets=["svg","doc"]`
- `doc_mode=companion-detail`

默认产出**自包含 HTML 成品**，因为它是：零依赖随处可开（浏览器 / 打印 PDF / 飞书导入）、可事后编辑（纯 HTML/CSS）、从「校验过的 plan」到「看得见的图」最快的路径。

### 定位：不做海报，做「可编辑、信息正确、可嵌入」的 overview

市面上有大量一键「文章 → 海报」工具（包括 skill 包），用一次性 HTML 海报的视觉冲击取胜。本 skill **不与海报视觉正面竞争**，差异化在于：

1. **结构化 plan 是一等公民**（JSON schema + 校验），用户可改一个事实、挪一个块、换一种布局，不必推倒重来。
2. **信息正确优先于视觉炫**：渲染前强制文本预算、引用完整性、sankey weight、「不做虚假精确」。海报里放错的数字依然是错的。
3. **飞书办公原生**：自包含 HTML 干净地导入飞书文档、无依赖打印 PDF。
4. **默认伴生文档**：详细论证进 companion doc，图保持可扫描。海报工具通常没有这一层拆分。

### 直接上传说明

这个目录已经按独立 skill root 收口，可直接作为：
- GitHub 仓库根目录
- ClawHub 本地发布目录

推荐做法：
- GitHub：把当前目录内容放到公开仓库根目录，仓库名建议也叫 `text-to-infographic`
- ClawHub：在当前目录执行 `clawhub skill publish . ...`

更多命令见：
- `PUBLISHING.md`

### 快速开始

校验全部 examples：

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
```

渲染某个 plan 为自包含 HTML 成品（主交付，`--out` 为输出目录，文件名取 plan slug）：

```bash
python3 scripts/render_infographic_html.py \
  examples/infographic-flywheel-demo.json \
  --out /tmp/render/
```

导出 PNG 分享图（小红书/公众号/推文配图，需要系统安装 Chrome/Chromium）：

```bash
python3 scripts/render_infographic_png.py \
  examples/infographic-flywheel-demo.json \
  --out /tmp/png/
# -> /tmp/png/growth_flywheel_ai_workspace_demo.png  (默认 2000xN @ 2x)
```

调整宽度与清晰度：`--width 1000`（CSS 视口宽）、`--scale 2`（DPR，1/2/3）。`CHROME_PATH` 环境变量可指定非默认位置的 Chrome。

为某个 plan 生成 adapter 草稿（可选）：

```bash
python3 scripts/build_infographic_adapters.py \
  examples/infographic-flywheel-demo.json \
  --pretty
```

### 输出示例

渲染器内置 6 种布局，均支持中文与英文内容，视觉系统由 `palette`（brand/mono/duo/triad/custom）+ `emphasis_style`（clean/editorial/playful/technical/luxury）驱动：

| 布局 | 用途示例 | 实现方式 |
| --- | --- | --- |
| `radial` | 增长飞轮 | SVG 圆环 + 顺时针箭头 + 中心摘要 |
| `spine-branch` | 鱼骨分析 | SVG 主脊 + 分支 |
| `pyramid` | 价值金字塔 | CSS 梯形堆叠 |
| `timeline` | 路线图 | CSS 时间轴 |
| `dashboard` | SaaS 指标卡 | CSS Grid 卡片 |
| `sankey` | 流量/占比 | 内联 SVG 流线，线宽按 `weight` |

默认输出 HTML（`primary_target=html`），`--out` 指定输出目录（文件名取 plan slug），`--stdout` 直接输出到 stdout，`--schema` 可指定自定义 schema 路径（默认用包内 schema）。

默认会输出：
- `normalized-plan.json`
- `svg-draft.json`
- `whiteboard-draft.json`
- `doc-outline.json`
- `doc-summary.md`

### 发布建议

如果你要发 GitHub：
- 直接把当前目录作为独立 package 发布即可

如果你要发 ClawHub：
- 建议直接以当前目录作为 skill root
- `SKILL.md` 已独立命名为 `text-to-infographic`
- 当前目录不依赖上层 `text-to-comic` 结构

---

## English

`text-to-infographic` is a standalone **infographic-first skill package** for compressing complex information into a single overview visual that can later be embedded into:
- Lark docs
- Lark sheets + whiteboards
- whiteboard canvases
- SVG-based design workflows

Its priorities are:
- information hierarchy
- editability
- scanability
- cross-tool orchestration

instead of comic-like narrative flow.

### Included chart families

- flywheel
- fishbone
- value pyramid
- sankey
- roadmap
- SaaS dashboard
- process map
- comparison chart

### What is included

- a portable infographic schema
- seven example plans
- a validator script
- a renderer that emits self-contained HTML infographics (primary output)
- a PNG exporter (headless Chrome via CDP, zero Python deps) for share images
- an adapter-draft builder for SVG / whiteboard / doc outputs

Default delivery: `primary_target=html` — a zero-dependency, print-friendly, Feishu-importable single file. The plan stays a first-class editable artifact, so facts, blocks, and layout can be changed without regenerating from scratch. This is what distinguishes the package from one-shot poster generators: *correct, editable, embeddable overviews*, not decorations.

### Direct upload layout

This folder is prepared as a standalone skill root and can be used directly as:
- a GitHub repository root
- a local ClawHub publish directory

See `PUBLISHING.md` for exact commands.

### Quick commands

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
python3 scripts/render_infographic_html.py examples/infographic-roadmap-demo.json --out /tmp/render/
python3 scripts/render_infographic_png.py    examples/infographic-roadmap-demo.json --out /tmp/png/
python3 scripts/build_infographic_adapters.py examples/infographic-roadmap-demo.json --pretty
```
