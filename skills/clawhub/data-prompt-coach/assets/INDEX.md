# INDEX — 16 原子方法论引用图

> v3.1 教程蒸馏升级：M12-M16 由蒸馏入口从 6 篇真实教程中萃取，2026-07-22 挂载。

## 方法论清单

| # | 名称 | 文件 | 何时用 |
|---|------|------|--------|
| M1 | 黄金五要素 | [M1-golden-five-elements.md](../references/methods/M1-golden-five-elements.md) | 采集/提取类 |
| M2 | 防幻觉三招 | [M2-anti-hallucination-trio.md](../references/methods/M2-anti-hallucination-trio.md) | 涉及金额/人数/结论 |
| M3 | 80/20 协作 | [M3-80-20-collaboration.md](../references/methods/M3-80-20-collaboration.md) | 写 SQL/代码 |
| M4 | 任务拆解 | [M4-task-decomposition.md](../references/methods/M4-task-decomposition.md) | 复杂多步任务 |
| M5 | 两级标签体系 | [M5-two-level-taxonomy.md](../references/methods/M5-two-level-taxonomy.md) | 分类标注 |
| M6 | 分批处理 | [M6-batch-processing.md](../references/methods/M6-batch-processing.md) | >1000 条 |
| M7 | 验真闭环 | [M7-verification-loop.md](../references/methods/M7-verification-loop.md) | 任何关键输出 |
| M8 | 目标导向 | [M8-goal-oriented-prompt.md](../references/methods/M8-goal-oriented-prompt.md) | 深度分析 |
| M9 | 分步提问 | [M9-stepwise-questioning.md](../references/methods/M9-stepwise-questioning.md) | 高要求报告 |
| M10 | SQL 4 必看 | [M10-sql-four-checks.md](../references/methods/M10-sql-four-checks.md) | 审查 SQL |
| M11 | 大文件阈值 | [M11-large-file-threshold.md](../references/methods/M11-large-file-threshold.md) | 大数据量 |
| **M12** | **下钻触发** | [M12-drill-down-trigger.md](../references/methods/M12-drill-down-trigger.md) | **探索性分析（涌现维度）** |
| **M13** | **中间逻辑可追溯** | [M13-intermediate-logic-traceability.md](../references/methods/M13-intermediate-logic-traceability.md) | **AI 分析可信度** |
| **M14** | **增量同步** | [M14-incremental-sync.md](../references/methods/M14-incremental-sync.md) | **定期运行任务** |
| **M15** | **迭代式可视化** | [M15-iterative-visualization.md](../references/methods/M15-iterative-visualization.md) | **图表制作** |
| **M16** | **多维数据联动** | [M16-multi-dim-linkage.md](../references/methods/M16-multi-dim-linkage.md) | **多维关系展现** |

## 引用图

```mermaid
graph TD
    M1[M1 黄金五要素] --> M2[M2 防幻觉三招]
    M1 --> M4[M4 任务拆解]
    M2 --> M7[M7 验真闭环]
    M4 --> M1
    M4 --> M2
    M5[M5 两级标签体系] --> M6[M6 分批处理]
    M5 --> M2
    M6 --> M5
    M3[M3 80/20 协作] --> M10[M10 SQL 4 必看]
    M3 --> M7
    M8[M8 目标导向] --> M11[M11 大文件阈值]
    M8 --> M9[M9 分步提问]
    M9 --> M8
    M10 --> M3
    M11 --> M8
    M7 --> M2
    M12[M12 下钻触发] --> M8
    M12 --> M16[M16 多维联动]
    M13[M13 逻辑可追溯] --> M2
    M13 --> M9
    M14[M14 增量同步] --> M6
    M14 --> M7
    M15[M15 迭代式可视化] --> M8
    M15 --> M16
    M16 --> M15
```

## 关键引用关系

- **M1→M2**：采集/提取类场景，五要素之后必须叠加防幻觉三招
- **M4→M1/M2**：拆解后每一步都套五要素+三招
- **M5→M6**：标签体系定好后才用分批策略
- **M3→M10**：SQL 协作姿势的具体审查点
- **M8→M9/M11**：深度分析场景，目标导向+分步提问+大文件阈值组合使用
- **M12→M8/M16**（v3.1 新增）：探索性分析下钻后常用目标导向 + 多维联动展示
- **M13→M2/M9**（v3.1 新增）：可追溯性需要防幻觉证据 + 分步追问
- **M14→M6/M7**（v3.1 新增）：定期同步常配合分批处理 + 验真抽查
- **M15↔M16**（v3.1 新增）：可视化迭代与多维联动相互配合
- **M13 与 M9 联动**（v3.1 新增）：分步提问深挖时，每步结果都要可追溯
- **M14 与 M2 联动**（v3.1 新增）：增量同步失败兜底需 M2 防幻觉（不脑补缺数据）

## 7 场景常用组合

| 场景 | 规模 | 组合 |
|------|------|------|
| 1 采集 | 任意 | M1+M2+M7 |
| 1 采集（定期） | 任意 | M1+M2+M7+M14 |
| 2 提取 | <100 份 | M1+M2 |
| 2 提取 | >100 份 | M1+M2+M6 |
| 3 SQL | 任意 | M3+M10+M2 |
| 4 核对 | 任意 | M2+M7（顶配） |
| 4 核对（含 AI 分析） | 任意 | M2+M7+M13 |
| 5 标注 | <1000 条 | M5+M2 |
| 5 标注 | >1000 条 | M5+M6+M2 |
| 6 周报 | 任意 | M1+M7+M4 |
| 6 周报（含洞察） | 任意 | M1+M7+M4+M12+M13 |
| 7 深度报告 | <5000 行 | M8+M9 |
| 7 深度报告 | <5000 行 + 可视化 | M8+M9+M15+M16 |
| 7 深度报告 | >10万行 | M8+M9+M11 |
| 7 深度报告 | >10万行 + 可视化 | M8+M9+M11+M15+M16 |
| 7 深度报告（探索性） | 任意 | M8+M9+M12+M13 |
