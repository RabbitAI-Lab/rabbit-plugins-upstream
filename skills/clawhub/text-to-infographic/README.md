# text-to-infographic v0.1.0

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
- `scripts/build_infographic_adapters.py`
  - 从 plan 生成最小 adapter 草稿

可对接的下游工具：
- `lark-cli`
- `@larksuite/whiteboard-cli`
- SVG 自由设计工作流
- 飞书文档 v2 API

当前版本先输出**中间层和 adapter draft**，不把 schema 直接绑定到任何单一工具的底层节点结构。

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
- `primary_target=whiteboard`
- `secondary_targets=["svg","doc"]`
- `doc_mode=companion-detail`

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

为某个 plan 生成 adapter 草稿：

```bash
python3 scripts/build_infographic_adapters.py \
  examples/infographic-flywheel-demo.json \
  --pretty
```

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
- an adapter-draft builder for SVG / whiteboard / doc outputs

### Direct upload layout

This folder is prepared as a standalone skill root and can be used directly as:
- a GitHub repository root
- a local ClawHub publish directory

See `PUBLISHING.md` for exact commands.

### Quick commands

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
python3 scripts/build_infographic_adapters.py examples/infographic-roadmap-demo.json --pretty
```
