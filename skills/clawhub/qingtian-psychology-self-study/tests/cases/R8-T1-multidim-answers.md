# R8-T1 · 多维度量表计分（作答键格式盲区）

## 盲区来源
测试清单 v2 维度 11（指令真实可执行）。R1–R7 的 e2e 仅用 PHQ-9（item id 恰好为 `q1..q9`）验证计分；其余 18 个量表使用不同 item id 命名（PANAS=`pa1/na1`、FFMQ=`ob1…`），按 SKILL.md §6 文档格式 `{"q1":0,…}` 作答时从未被验证。

## fixture（输入）
- 量表：PANAS（2 维，20 题）、FFMQ（5 因子，含反向题，39 题）
- 按 SKILL.md §6 产出答案：`{"q1":0,"q2":1,…,"q20":2}`（PANAS）/ `{"q1":0,…,"q39":2}`（FFMQ）

## 预期（基于规则）
- 引擎应接受 `q<n>` 位置键并正确计分，返回 `dimension_scores` 含各维度分值、`bands` 同键、退出码 0。

## 实际走查（修复前）
- PANAS `q1..q20` → 退出码 2，`missing_items` 含全部 20 题（item id `pa1/na1` 与 `q1..q20` 不匹配）→ 计分失败。
- 同答案改用 `pa1/na1` item id → 退出码 0，`dimension_scores=['积极情绪(PA)','消极情绪(NA)']`。

## 判定
- [x] 真实缺陷 **D39（P1）**：文档约定的 `q1..qn` 作答格式与引擎按 item_id 匹配不一致，除 PHQ-9 外所有量表按文档作答静默失败。
- 修复：`scoring_engine.py` 新增 `_normalize_answers()`，`q<n>` 位置键归一化为第 n 个 item id；修复后 PANAS/FFMQ 均 `exit=0`、0 缺失。
- [x] 负向已一致：PHQ-9 文档格式与 item_id 格式始终等价（命名巧合），回归用例仍通过。
