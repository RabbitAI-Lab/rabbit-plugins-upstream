# 片段库索引(复制 → 替换 {{参数}} → validate)

> v1 不建模板引擎:直接复制片段内容进页面,替换 `{{参数}}` 即可。
> 每个片段文件头部注释都自带参数表与 z 序约定。
> 片段全部通过 validate(0 ERROR);组合后仍须整页跑一遍 validate。

| 片段 | 用途 | 布局方式 | 主要参数 |
|---|---|---|---|
| `page-header.html` | 页头区:红装饰线+眉题+主标题+副标题+页码 | A 绝对定位 | KICKER / TITLE / SUBTITLE / PAGE_NUM |
| `card-accent-top.html` | 顶部强调条卡片(标题+正文+注释) | A 绝对定位 | X/Y/W/H / ACCENT / KICKER / TITLE / BODY / FOOTNOTE |
| `badge-center.html` | 单行垂直居中徽章 | A 绝对定位 | X/Y/W/H / BG / FG / TEXT / RADIUS |
| `gradient-bar.html` | 渐变横条+叠字(截图安全) | A 绝对定位 | X/Y/W/H / FROM→TO / TEXT |
| `stat-number.html` | 混合字号大数字格(KPI 单元) | 置于 grid 格内 | VALUE / UNIT / COLOR / LABEL |
| `layer-row.html` | 横条目(序号圆+标题+副题) | A 定位 + 对象内 flex | X/Y/W/H / NUM / ACCENT / TITLE / SUB |
| `hero-gradient.html` | 渐变英雄区(全宽渐变+叠加标题+装饰条) | A 绝对定位 | H / GRAD_ANGLE / GRAD_COLORS / KICKER / TITLE / SUBTITLE |
| `kpi-card.html` | KPI 卡片(渐变底+大数字+上标+增量) | A 绝对定位 | X/Y/W/H / GRAD_FROM→TO / LABEL / VALUE / UNIT / DELTA |
| `flow-step.html` | 流程步骤(chevron 几何+编号文字) | A 绝对定位 | X/Y/W/H / BG / NUM / TITLE |
| `timeline-node.html` | 时间线节点(渐变圆+旋转年份+说明) | A 绝对定位 | X/Y / GRAD_FROM→TO / YEAR / YEAR_ROTATE / TITLE / SUB |
| `compare-card.html` | 对比卡(单边强调+标题+列表) | A 绝对定位 | X/Y/W/H / ACCENT / BADGE / TITLE / ITEMS |
| `code-block.html` | 代码展示(深色渐变+虚线边框+pre/code) | A 绝对定位 | X/Y/W/H / BG_FROM→TO / TITLE / CODE |
| `quote-block.html` | 引用块(渐变左边框+斜体+超链接) | A 绝对定位 | X/Y/W / GRAD_FROM→TO / QUOTE / AUTHOR / LINK |
| `data-table.html` | 数据表格(交替底纹+深色表头+右对齐数字) | A 绝对定位 | X/Y/W / HEAD_COLOR / ZEBRA |

## z 序与叠放约定

1. **PPTX 叠放 = DOM 顺序**(先画在下);片段内部的 z-index 仅为浏览器合成服务
2. 层次惯例:底卡 `z-index:1` < 强调条/徽章底 `z-index:5` < 文字 `z-index:10` < 截图区叠字 `z-index:11`
3. 组合多个片段时,按"底→顶"的阅读顺序写 DOM;同容器内元素重叠时尤其如此(勿靠 z-index 补救)

## 组合建议

- **内容区成组元素优先方式 B/C**:3 张 `card-accent-top` 建议改用 `columns`/`flex` 容器排布(见 layout-recipes 配方 1),卡片用"底卡+流式内部"写法,坐标免算
- `layer-row` 多条堆叠:方式 B 用 `flex-direction:column` 容器,方式 C 用 `data-layout="stack"` + `data-layout-h`
- `stat-number` 必须放在某个已标记格子/卡片内部(它是内容片段,不是独立 data-object)
- `gradient-bar` 上的文字保持在**独立 textbox** 里(截图前文字会被临时隐藏,不会烙进 PNG)
- **P2 新片段组合**(见 `creative-layouts.md`):
  - `hero-gradient` + `kpi-card` ×3 → 数据仪表盘封面
  - `flow-step` ×N + `compare-card` ×2 → 流程对比页
  - `timeline-node` ×4 + `quote-block` → 发展历程页
  - `code-block` + `compare-card` → 技术方案页
  - `data-table` + `stat-number` → KPI 汇报页

## 占位符规范

`{{X}} {{Y}} {{W}} {{H}}` 含单位(如 `100px`);`calc()` 已预写在需要偏移的位置(如卡内边距 30px)。
替换时**整页内唯一**:先全局替换 `{{X}}` 再复制下一张卡,避免串值。
