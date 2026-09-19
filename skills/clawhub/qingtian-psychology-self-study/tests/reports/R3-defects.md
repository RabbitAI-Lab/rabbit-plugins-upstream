# R3 缺陷报告 · 量表测评链路验证

**轮次**：R3（第 3 轮）
**测试焦点**：assessment/ 量表测评链路真实跑通（计分引擎、报告生成器、RUNBOOK 一致性）
**前置版本**：v1.0.2
**修复后版本**：v1.0.3

## 基线核查
- RUNBOOK.md、score_and_report.py、scoring_engine.py、report_generator.py 接口匹配。
- 19 个量表 JSON 结构完整（items/dimensions/bands/safety 齐全）。
- 计分引擎健壮：含反向计分、缺失检测、危机判定（q9 触发）。

## 真实运行
- 构造两份作答：用例 A（PHQ-9 全 1 分，应触发危机）、用例 B（全 0 分，不触发）。
- 运行 `score_and_report.py PHQ-9 <answers.json> <out_dir>`：
  - 用例 A：总分 9 → 轻度抑郁，`crisis_flag=true`（q9 命中），HTML 报告 + `RESULT_JSON` 正常。
  - 用例 B：总分 0 → 无/极轻度，未触发。
- 闭环验证通过：计分 → 危机判定 → HTML 报告 → RESULT_JSON 输出均正常。

## 缺陷清单

### D12（P2，数据风险）
- **现象**：报告文件名时间戳仅精确到分钟 `strftime('%Y%m%d_%H%M')`（report_generator.py:422）。
  同一分钟内多次测评会生成同名文件，**互相覆盖旧报告**，progress.json 记录的路径随之失效。
- **影响**：用户在 1 分钟内重测或补测时，历史报告丢失，趋势对比断档。
- **修复**：改为秒级 `strftime('%Y%m%d_%H%M%S')`。
- **验证**：连跑两次（用例 A、B）确认生成两个不同秒级文件，无覆盖。

## 修复汇总
| 缺陷 | 严重度 | 修复 | 状态 |
|------|--------|------|------|
| D12 报告文件名分钟级覆盖 | P2 | 秒级时间戳 | ✅ 已修复并验证 |

## 遗留/下轮
- R4 转入组队系统（team-learning 模块 + group 字段读写 + meeting/review 处理器 + 里程碑）。
