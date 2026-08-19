---
name: data-viz
description: 数据可视化。读 CSV/JSON 数据集，自动推断列类型，纯 Python 生成 SVG 图表（直方图/散点/柱状/折线）与 HTML 看板，无 matplotlib/pandas 依赖。当用户需要"画个图""数据可视化""做个图表""看分布""dashboard"时使用。
agent_created: true
visibility: public
---

# Data-Viz · 数据可视化

把一张数据集快速变成可读的图表看板——无需安装重型绘图库，纯标准库即可离线运行，适合在受限/沙箱环境中产出可视化。

## 何时用
- "把这份销售数据画个图"、"看看分布"、"做个 dashboard"、"这两列有关系吗？"
- 需要离线、零依赖地生成图表（环境无法 pip install matplotlib 时尤其有用）。

## 用法
`python scripts/viz.py --data <file.csv|.json> --out <输出目录> [--topn 12]`

自动产出：
- 每个数值列的**直方图**（分布）
- 数值列两两**散点图**（前 2 对）
- 分类列 × 数值列的**柱状图**（各类均值，取 topn）
- `index.html` 聚合看板 + `summary.json`（列类型推断与各列统计量）

## 设计要点
- `scripts/viz.py` 用标准库 `csv` 读数据，自写 SVG 渲染（坐标轴、柱、点、线）。
- 列类型推断：某列可解析为数值的比例 >80% 即判为数值列。
- 输出为静态 SVG+HTML，可直接在浏览器打开或嵌入报告。

## 自进化
内置 learner（`scripts/learner.py`）。每次可视化后调用：
`python scripts/learner.py record --skill data-viz --op "<操作>" --result success|fail --detail "<说明>"`
据此复盘图表选择是否合理（例如某图无信息量时换类型）。
