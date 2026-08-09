---
name: html-report
version: 2.0.0
description: "Generate HTML visualization reports. Simple mode: single-page responsive (Tailwind+Mermaid). Complex mode: multi-page fixed 1017x720px with 13+ SVG charts and Chrome screenshot."
tags: [report, visual, data, template-based, presentation]
---

# HTML Report — 可视化报告生成器

支持两种模式，根据场景自动选择：

| 模式 | 场景 | 输出 |
|------|------|------|
| **Simple 模式** | 快速分析报告、代码审查、项目健康度 | 单页响应式 HTML（Tailwind + Mermaid） |
| **Complex 模式** | 正式汇报、演示文稿、多页报告 | 多页固定尺寸 HTML（1017×720px + Chrome 截图） |

---

## 模式选择规则

| 用户意图 | 推荐模式 |
|----------|----------|
| "快速报告"/"分析报告"/"审查报告" | Simple |
| "汇报"/"演示"/"多页报告"/"PPT 风格" | Complex |
| 不确定 | 询问用户 |

---

## Simple 模式：快速响应式报告

### 技术栈

- **布局**: Tailwind CSS (CDN)
- **图表**: Mermaid.js (CDN)
- **输出**: 单个 `.html` 文件，零依赖

### 核心组件

1. **执行摘要区** — 一段话总结报告核心发现
2. **核心发现卡片网格** — 响应式网格布局，带强度徽章
3. **Mermaid 图表** — 架构图/流程图/时序图/类图
4. **Before/After 对比** — 红绿双栏对比
5. **推荐列表** — 带 Strong/Worth/Speculative 徽章

### 强度徽章系统

| 徽章 | 颜色 | 含义 |
|------|------|------|
| **Strong** | `bg-green-100 text-green-800` | 明确改进，强烈推荐执行 |
| **Worth exploring** | `bg-yellow-100 text-yellow-800` | 有价值但需评估上下文 |
| **Speculative** | `bg-gray-100 text-gray-600` | 理论上有好处，实际效果不确定 |

### Mermaid 图表类型

| 类型 | 用途 | 语法 |
|------|------|------|
| 架构图 | 系统组件关系 | `graph TD` |
| 流程图 | 业务流程 | `flowchart LR` |
| 时序图 | 交互流程 | `sequenceDiagram` |
| 类图 | 领域模型 | `classDiagram` |
| 依赖关系 | 模块依赖 | `graph LR` |

### 适用场景

| 场景 | 报告重点 |
|------|----------|
| **架构分析** | 依赖图 + 模块边界 + 耦合度评估 + 改进建议 |
| **代码审查报告** | 问题卡片 + Before/After + 推荐行动 |
| **项目健康度** | 指标仪表盘 + 趋势 + 风险灯 + 优先级排序 |
| **重构方案** | 现状分析 + 目标架构 + 迁移路径 + 风险评估 |

### 模板文件

详见 `templates/simple/base.html`

---

## Complex 模式：多页固定尺寸报告

### 技术栈

- **画布**: 1017×720px 固定尺寸
- **四区结构**: Header 72px + Content 580px + Summary 48px + Footer 20px
- **图表**: 13+ SVG 图表（折线/柱状/雷达/甘特/圆环/散点/流程/树状/热力/瀑布/双轴等）
- **配色**: 7套主题配色
- **截图**: Chrome/Puppeteer

### 三条铁律

1. **画布锁定 1017×720px** — 不得溢出
2. **四区高度精确求和 = 720px** — 72+580+48+20
3. **不得使用 LibreOffice 渲染** — 必须使用 Chrome/Puppeteer 截图

### 10 个专项文件

| 文件 | 职责 | 使用场景 |
|------|------|----------|
| `01-canvas.md` | 画布尺寸、四区结构、溢出规则 | 每页开始前 |
| `02-design-system.md` | Tc 模板流程、基础模板基因库 | 规划阶段 |
| `03-layout.md` | Lc 布局流程、空间计算 | 每页选布局时 |
| `04-color-font.md` | 7套配色、字体规则、语义色系统 | 每页设定样式时 |
| `05-content.md` | 反偷懒约束、内容密度、基础SVG图表库 | 写内容时 |
| `06-workflow.md` | 主题拆解规划、渲染验证、质量清单 | 开始和结束时 |
| `07-special-pages.md` | 封面/目录/章节分隔/结尾页规范 | 生成特殊页面时 |
| `08-svg-extended.md` | 扩展SVG图表库（圆环/散点/流程/树状等） | 需要复杂图表时 |
| `09-components.md` | 页眉/摘要栏/卡片变体/徽章/图标 | 每页组件选用时 |
| `10-diagram-types.md` | 业务图谱库（架构图/流程图/层级图等） | 用户要求业务图谱时 |

### 图表选型速查

| 数据特征 | 图表类型 | 文件 |
|---------|---------|------|
| 趋势/时间序列 | 折线面积图 | 05 图表2 |
| 量级对比（同类） | 横条图/柱状图 | 05 图表1/6 |
| 多维度评估 | 雷达图 | 05 图表3 |
| 时间节点 | 时间轴 | 05 图表4 |
| 进度/计划 | 甘特图 | 05 图表5 |
| 占比/构成 | 圆环图 | 08 图表7 |
| 相关性分析 | 散点图 | 08 图表8 |
| 步骤/决策流 | 流程图 | 08 图表9 |
| 层级/树状 | 树状图 | 08 图表10 |
| 二维密度 | 热力矩阵 | 08 图表11 |
| 累计变化 | 瀑布图 | 08 图表12 |
| 双量级叠加 | 双轴图 | 08 图表13 |
| 系统组件/微服务 | 分层架构图 | 10 一 |
| 跨部门流程 | 泳道图 | 10 二 |
| 转化率/用户路径 | 漏斗图 | 10 三 |
| 流量/预算分配 | Sankey桑基图 | 10 四 |
| KPI目标对比 | Bullet子弹图 | 10 五 |
| 市场占比/资产组合 | Treemap树图 | 10 六 |
| 组织/优先级 | 金字塔/2×2矩阵 | 10 七 |
| 风险评估/任务分配 | 风险矩阵/RACI | 10 八 |

### 报告结构

```
P00  封面页（Cover）        → 07-special-pages.md CV变体
P01  目录页（可选）          → 07-special-pages.md TC变体
──── 章节分隔（可选）        → 07-special-pages.md CD变体
P01+ 内容页 × N            → 主流程
──── 章节分隔（可选）        → 07-special-pages.md CD变体
PN   结尾页（End）          → 07-special-pages.md EP变体
```

### 生成流程

```
阶段一：规划
├─ 读 02-design-system.md → 自创 Tc 专属模板
├─ 读 03-layout.md → 了解 Lc 自创布局机制
├─ 读 06-workflow.md → 拆解主题→12维度，规划每页三元素
└─ 读 07-special-pages.md → 确认是否需要封面/目录/章节/结尾页

阶段二：逐页生成
每页生成时：
├─ 读 01-canvas.md → 确定四区 CSS 骨架
├─ 读 02-design-system.md → 应用 Tc 模板的背景/卡片/页眉 CSS
├─ 读 03-layout.md → 自创本页 Lc 布局
├─ 读 04-color-font.md → 选配色方案 + 字体
├─ 读 05-content.md → 填内容，选基础SVG图表
├─ 读 08-svg-extended.md → 需要复杂图表时（可选）
├─ 读 09-components.md → 选择页眉变体/摘要栏/卡片变体
└─ 读 10-diagram-types.md → 用户要求业务图谱时（可选）

阶段三：验证与收尾
└─ 读 06-workflow.md → 运行截图验证，对照质量清单
```

### 质量清单

- [ ] 每页尺寸严格 1017×720px
- [ ] 四区高度求和 = 720px（72+580+48+20）
- [ ] 无内容溢出或截断
- [ ] 配色方案一致（使用同一主题变量）
- [ ] 摘要栏有实质内容（非空）
- [ ] 图表类型与数据特征匹配
- [ ] 中文字体正确渲染
- [ ] 页码连续且正确

---

## 文件结构

```
html-report/
├── SKILL.md                          # 本文档
├── templates/
│   ├── simple/
│   │   └── base.html                 # Simple 模式模板（Tailwind + Mermaid）
│   └── complex/
│       ├── 01-canvas.md              # 画布尺寸规范
│       ├── 02-design-system.md       # Tc 模板流程
│       ├── 03-layout.md              # Lc 布局流程
│       ├── 04-color-font.md          # 7套配色 + 字体
│       ├── 05-content.md             # 内容密度 + 基础SVG图表
│       ├── 06-workflow.md            # 生成流程 + 质量清单
│       ├── 07-special-pages.md       # 封面/目录/章节/结尾页
│       ├── 08-svg-extended.md        # 扩展SVG图表库
│       ├── 09-components.md          # 页眉/摘要栏/卡片变体
│       └── 10-diagram-types.md       # 业务图谱库
```

---

## 错误处理与降级策略

### Simple 模式

| 场景 | 降级方案 |
|------|----------|
| Tailwind CDN 不可用 | 内联基础 CSS，保持布局 |
| Mermaid 图表渲染失败 | 退回到纯文本 pre 标签 |
| 报告内容过长 | 拆分为多个 section，保持单页 |

### Complex 模式

| 场景 | 降级方案 |
|------|----------|
| 内容溢出画布 | 精简文字、缩小图表、拆分到下一页 |
| Chrome 未安装 | 提示用户安装，或直接输出 HTML 文件 |
| SVG 图表不显示 | 验证 SVG 语法，检查命名空间 |
| 中文乱码 | CSS 中指定 `font-family: 'Microsoft YaHei', sans-serif` |
| 截图失败 | 使用 Chrome CLI (--headless --screenshot) 替代 Puppeteer |

---

## 注意事项

- Simple 模式：报告必须是单个自包含 HTML 文件，所有样式通过 Tailwind CDN 内联
- Complex 模式：每页严格 1017×720px，四区高度精确求和
- 颜色语义一致：红色=问题/风险，绿色=改进/健康，黄色=警告/待观察
- 响应式布局（Simple 模式）：确保移动端可读
- 中文字体：Complex 模式必须指定 `Microsoft YaHei`

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.0.0 | 2026-07-31 | 合并 html-report + html-report-generator，支持 Simple/Complex 双模式 |
| v1.0.0 | 2026-06-29 | 初始版本（Tailwind + Mermaid 单页报告） |

---

*Version 2.0.0 — 合并 html-report + html-report-generator，双模式输出*
