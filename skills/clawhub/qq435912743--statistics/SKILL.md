---
name: statistics
description: 统计分析。对 CSV/JSON 数据集做描述统计（均值/中位数/分位数/标准差）、数值列 Pearson 相关矩阵，以及两样本 Welch t 检验（不等方差），纯 Python 无 scipy/numpy 依赖。当用户需要"做个统计""算相关性""两组有显著差异吗""描述性统计""假设检验"时使用。
agent_created: true
visibility: public
---

# Statistics · 统计分析

让 agent 具备严谨的量化分析能力：从一张表快速得到可信的统计结论，无需依赖 scipy/numpy。

## 何时用
- "算一下相关性"、"这两组有显著差异吗"、"做个描述统计"、"假设检验"
- 需要离线、零依赖地完成常见统计分析。

## 用法
`python scripts/stats.py --data <file.csv|.json> --out summary.json [--group 列] [--value 数值列]`

产出：
- **描述统计**：每数值列的 n / 均值 / 中位数 / 标准差 / 最小最大 / 四分位（p25/p75）
- **相关矩阵**：数值列两两 Pearson 相关系数
- **Welch t 检验**（可选）：给定 `--group` 与 `--value`，对两组做不等方差 t 检验，返回 t、自由度、均值差

## 设计要点
- `scripts/stats.py` 全部用标准库 `statistics` / `math` 实现；分位数用线性插值；t 检验用 Welch–Satterthwaite 自由度，对小样本稳健。
- Pearson 相关系数手写，避免 numpy 依赖。

## 自进化
内置 learner（`scripts/learner.py`）。每次分析后调用：
`python scripts/learner.py record --skill statistics --op "<操作>" --result success|fail --detail "<说明>"`
据此复盘：是否漏报异常值、是否该换非参数检验等。
