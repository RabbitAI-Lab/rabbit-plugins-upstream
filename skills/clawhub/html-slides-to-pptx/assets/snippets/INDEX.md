# 片段库索引(复制 → 替换 {{参数}} → validate)

> v1 不建模板引擎:直接复制片段内容进页面,替换 `{{参数}}` 即可。
> 每个片段文件头部注释都自带参数表与 z 序约定。
> **选片段前先看页面形态:`reference/page-archetypes.md`(20 原型)与设计纪律 `reference/design-principles.md`。**
> 带 ⚠️ 的片段有使用限制(去 AI 味纪律),超限场景禁用。

## 原型直出片段(2026-08-02 新增,去 AI 味主力)

| 片段 | 用途 | 填充 | 主要参数 |
|---|---|---|---|
| `agenda-list.html` | 议程条目:大数字编号裸排(原型 3) | 满填 | NUM / TITLE / SUB / H / BORDER |
| `section-divider.html` | 章节分隔:超大编号+章节名(原型 4) | airy | NUM / TITLE / SUB |
| `big-statement.html` | 大字观点页(原型 5) | airy | STATEMENT / PROOF |
| `quote-hero.html` | 引用页:巨引号+正体(原型 6) | airy | QUOTE / ATTRIBUTION / MARK_COLOR |
| `editorial-columns.html` | 编辑式双栏文字(原型 7 内容区) | 满填 | COL1 / COL2 |
| `image-bleed.html` | 全出血大图页(原型 11) | 出血 | IMG / HEADLINE / SUB / VEIL |

## 基础构件片段

| 片段 | 用途 | 布局方式 | 主要参数 |
|---|---|---|---|
| `page-header.html` | ⚠️ 页头三件套(**仅章节首页/封面**) | A 绝对定位 | KICKER / TITLE / SUBTITLE / PAGE_NUM |
| `card-accent-top.html` | ⚠️ 顶部强调条卡片(**仅真并列实体;每 deck ≤2 页矩阵**) | A 绝对定位 | X/Y/W/H / ACCENT / KICKER / TITLE / BODY / FOOTNOTE |
| `badge-center.html` | 单行垂直居中徽章(仅状态标注) | A 绝对定位 | X/Y/W/H / BG / FG / TEXT / RADIUS |
| `gradient-bar.html` | ⚠️ 渐变横条+叠字(**仅封面/分隔/收尾**) | A 绝对定位 | X/Y/W/H / FROM→TO / TEXT |
| `stat-number.html` | 混合字号大数字格(原型 17 单元) | 置于 grid/columns 列内 | VALUE / UNIT / COLOR / LABEL |
| `layer-row.html` | ⚠️ 序号圆横条目(**仅流程/步骤类**) | A 定位 + 对象内 flex | X/Y/W/H / NUM / ACCENT / TITLE / SUB |
| `data-table.html` | 数据表格(交替底纹+深色表头+右对齐数字) | A 绝对定位 | X/Y/W / HEAD_COLOR / ZEBRA |
| `code-block.html` | 代码展示(深色渐变+虚线边框+pre/code) | A 绝对定位 | X/Y/W/H / BG_FROM→TO / TITLE / CODE |
| `flow-step.html` | 流程步骤 chevron(步骤有箭头语义时;每 deck ≤1 页) | A 绝对定位 | X/Y/W/H / BG / NUM / TITLE |
| `compare-card.html` | 对比卡(单边强调+标题+列表) | A 绝对定位 | X/Y/W/H / ACCENT / BADGE / TITLE / ITEMS |

## 限用/弃用片段

| 片段 | 状态 | 说明 |
|---|---|---|
| `hero-gradient.html` | ⚠️ 仅封面/分隔/收尾 | 渐变英雄区(内容页禁用) |
| `kpi-card.html` | ⚠️ 仅仪表盘(阅读/混合档) | 演讲档 KPI 用 stat-number 裸排 |
| `timeline-node.html` | ⚠️ 默认用原型 14 替代 | 仅用户明确要求"活泼风"时 |
| `quote-block.html` | ⛔ 已弃用 | 渐变左边框+斜体 = AI 指纹;用 `quote-hero.html` |

## z 序与叠放约定

1. **PPTX 叠放 = DOM 顺序**(先画在下);片段内部的 z-index 仅为浏览器合成服务
2. 层次惯例:底卡 `z-index:1` < 强调条/徽章底 `z-index:5` < 文字 `z-index:10` < 截图区叠字 `z-index:11`
3. 组合多个片段时,按"底→顶"的阅读顺序写 DOM;同容器内元素重叠时尤其如此(勿靠 z-index 补救)

## 组合建议

- **满填纪律**:内容带必须铺满内容区(320-940,利用率 ≥85%);条目/卡片少就放大字号与间距(scale-to-fill),不许留白在底部
- `agenda-list` 多条堆叠:方式 B 用 `flex-direction:column` 容器免算 top;方式 C 用 `data-layout="stack"`
- `stat-number` 必须放在某个已标记格子/列内部(它是内容片段,不是独立 data-object)
- 成组内容优先方式 B/C(见 layout-recipes);页面骨架(标题/页码)用方式 A
- **装饰预算**:每页装饰元素 ≤2 件(装饰线/徽章/渐变条/图形点缀各计 1 件);每页高亮 ≤1 处

## 占位符规范

`{{X}} {{Y}} {{W}} {{H}}` 含单位(如 `100px`);`calc()` 已预写在需要偏移的位置(如卡内边距 30px)。
替换时**整页内唯一**:先全局替换 `{{X}}` 再复制下一张卡,避免串值。
