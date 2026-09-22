# ima-skills-1.1.9 — 设计切片

> **采样日期**：2026-09-05｜**触发**：用户钦定"归纳skill设计原则"模式首发（skill-rebuild 元设计升维）。
> **对象**：ima-skills-1.1.9（腾讯 ima 管理式 skill：knowledge-base + notes 双子模块 + 共享脚本层，suite 轻量档但按重量级纪律打造）。

## 这个 skill 好在哪里（元设计视角）

1. **不可逆优先门禁**：把"哪些操作要门"归结为**可逆性**单一判据——GATE 编号 + STOP 语义 + 默认拒绝 + 禁止软化话术，判据比清单更有产能。
2. **错误即修复指引**：把 agent 当"错误的第一个读者"来设计错误消息——每条 msg = 原因 + 修复动作 + 替代渠道。
3. **内外语言分层**：对用户说用户语言，对系统说系统语言，绝不混流。

**架构特征**：路由层（只管去哪/别去错/跨模块）→ 模块层 → 规范层（API 细节按需读）→ 脚本层（凭证/更新/预检共享）→ 元数据层（发布信息与运行时信息分置）；token 成本严格按需发生。三条元设计解释了 14 条亮点的系统性来源。

## 采到什么

| 产物 | 内容 | 去向 |
|------|------|------|
| [1-highlights.md](1-highlights.md) | 14 条亮点 A-401~A-414 | design-blocks-library 条目区 + B0X 聚合索引 |
| [2-principles.md](2-principles.md) | 3 条元设计 DP-001~003（本次第一产出） | design-principles-library |
| — | P0 三项改造（GATE 模板 / 三层路由表 / 双层错误+验收条） | blueprint-template / designer-guide / blocks.py（v3.5.0） |
| — | F3 版本自感知立项（A-411 工程化） | outputs/f3-version-self-awareness-proposal.md（待批） |

## 入库状态

✅ 已入库（v3.5.0）：14 亮点 + 3 原则全量落库，B0X 索引与来源标注已更新。
**明确不收录**：COS 细节 / MediaType 枚举 / PS 5.1 检测代码（领域特定）；双 meta 文件制（绑定其发布生态，按 SkillHub 体系自定）。
