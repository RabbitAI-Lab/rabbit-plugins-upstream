# 2-principles.md — ima-skills-1.1.9 元设计切片（设计原则候选 → 已入库）

> **定位**：本切片的**第一产出**——元设计（设计观）。亮点条目管"单点怎么抄"，本文件管"为什么 ima 能系统性想到"。
> **落库去向**：三条原则已入 [`references/design-principles-library.md`](../../references/design-principles-library.md)（DP-001~003）；支撑亮点见同目录 [`1-highlights.md`](1-highlights.md)。
> **来源**：skill-rebuild absorb_export 交接件 `absorbed-ima-skills.json` 的 `meta_designs` 字段（v3.5.0 起接口原生支持）。

## DP-001 · 不可逆优先门禁

- **原则**：操作的可逆性决定确认等级——不可逆 → 前置硬门（GATE 编号 + STOP 语义 + 默认拒绝 + 禁止软化）+ 语义消歧必问；可逆 → 放行。**判据（可逆性）比清单更有产能**。
- **解释亮点**：A-403 GATE 安全门、A-404 可逆性决定确认等级、A-405 隐私输出分级、A-407 环境陷阱前置、A-409 fail-with-direction。
- **已反哺**：B04 GATE 门禁清单模板（blueprint-template / designer-guide / blocks.py 三处，v3.5.0 P0 改造）。

## DP-002 · 错误即修复指引

- **原则**：每一层错误的 msg 都是给 agent 的行动指令：原因 + 修复动作 + 替代渠道——拒绝永远带指路，把死路变指路牌。
- **解释亮点**：A-408 双层错误分类、A-409 fail-with-direction、A-410 错误码表带建议处理列、A-411 版本自感知、A-414 依赖声明带 reason。
- **已反哺**：B07 Failure Handling 双层错误分类 + B08 错误验收条（v3.5.0 P0 改造）；A-411 工程化出口 = [outputs/f3-version-self-awareness-proposal.md](../../outputs/f3-version-self-awareness-proposal.md)。

## DP-003 · 内外语言分层

- **原则**：面向用户的输出永远用用户语言（名称/批量汇总/人话错误/按场景降级隐私粒度），面向系统的处理永远用系统语言（内部 ID/cursor/JSON），两者绝不混流。
- **解释亮点**：A-405 隐私输出分级、A-409 fail-with-direction、A-410 错误码人话化、A-413 UX 输出规范。
- **已反哺**：设计原则库种子（② 设计观注入候选；落地模板待下一轮按命中情况补入 B06 输出约定）。

---

**双向挂接说明**：本案例支撑的原则 ↑；每条 DP 在 design-principles-library 的条目区反向链接回本文件。后续蓝图若因某条原则改变了 `03-观点.md` / `06-决策.md` 的决策，在该处标注"引用 DP-XXX"——原则使用率可追踪。
