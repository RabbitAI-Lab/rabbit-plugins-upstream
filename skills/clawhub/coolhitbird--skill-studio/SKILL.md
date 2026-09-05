---
name: skill-studio
description: 用 5种设计模式诊断并生成 Agent Skill。触发：创建/新建/重构/审计 skill。覆盖诊断→架构→起草→校验→打包。
version: 1.0.0
agent_created: true
---

# Skill Studio（元技能）

> 用本技能创建或重构任何 skill 的标准入口。**开工先加载 `references/sop.md`**，所有铁律、决策树、熔断、验收门槛详节在其中。

## 何时使用

| 用户说 | 动作 |
|---|---|
| 「创建技能」「新建 skill」「做一个 skill」 | 走完整 SOP（诊断→架构→起草→校验→打包） |
| 「重构 skill」「审计 skill」「这个 skill 有问题」 | 跳过诊断，从审计入口进（`references/sop.md` 第 4 节） |
| 「修 description」「改 typo」 | 跳过诊断，直接改 + 跑校验 |

## 标准流程（精简索引，详节见 sop.md）

1. **诊断访谈**（Inversion 模式开场）：问 3-6 个关键问题（触发/不确定性/输入输出/失败兜底/门槛），一次一个
2. **模式选择**（`diagnose.py` 辅助）：输出推荐模式 + 理由，多模式命中时组合
3. **架构设计**：根据模式决定 references/assets/scripts 布局
4. **起草**：`init_skill.py` 生成骨架 → 先写 references/assets/scripts → 再写 SKILL.md → 删示例文件
5. **自检清单**：人工对照 11 项设计列表 + 7 项自检（sop.md 步骤 5）
6. **自动校验**（`validate.py` 硬钳）：FAIL 即拒出包
7. **打包**：`package_skill.py`
8. **dogfood 测试**：触发率 ≥90% + 多模型（Haiku/Sonnet/Opus）+ 反触发 ≤5%
9. **落地安装**：用户级 `~/.workbuddy/skills/` 或项目级
10. **迭代**：真实任务跑 → 改 SKILL.md/references → 重跑校验+dogfood

## 5种模式快速决策表（核心）

> **不要从目录出发，从要控制的不确定性出发。**

| 你最担心的失控 | 大白话 | 推荐模式 | 关键结构 |
|---|---|---|---|
| Agent 不懂某个库/团队规范 | 怕它不懂规矩 | **Tool Wrapper** | `SKILL.md` + `references/` |
| 输出结构每次漂移 | 怕它写得没格式 | **Generator** | `SKILL.md` + `assets/template` |
| 审查结果靠感觉，不可复现 | 怕它审得没标准 | **Reviewer** | `SKILL.md` + `references/checklist` |
| 用户没说清，Agent 脑补 | 怕它没问清楚就开干 | **Inversion** | `SKILL.md`（分阶段访谈） |
| 任务必须按顺序，中间不能跳 | 怕它跳过过程直接交作业 | **Pipeline** | `SKILL.md`（带门槛步骤）+ `scripts/` |

**典型生产流程**：Inversion（问清上下文）→ Tool Wrapper（加载规范）→ Generator（生成产物）→ Reviewer（按标准审查）→ Pipeline Gate（用户确认后进下一步）。

**组合才是生产形态**，纯模式罕见。

## 铁律（15 条，详证据见 sop.md 第 1 节）

| # | 铁律 |
|---|---|
| 1 | **自举**：skill-studio 自己必须符合它教别人的所有规范 |
| 2 | **强制力靠脚本不靠词汇**：`validate.py` 真校验，不靠 "MUST reject" 措辞 |
| 3 | **description ≤ 80 字**（比官方 200 字更严）+ 动词开头 + 关键词 |
| 4 | **SKILL.md ≤ 500 行**，详节挪 `references/` |
| 5 | **设计哲学不进 SKILL.md**：挪 `references/architecture.md` |
| 6 | **铁律条目化**：1 行结论 + 1 行证据 |
| 7 | **5种模式知识外置**：每种独立 `references/pattern-*.md` |
| 8 | **真实素材优先**：反例用自己踩过的坑，不编造 |
| 9 | **专注**：一个 Skill 只解决一个特定可重复工作流 |
| 10 | **善用示例 > 抽象解释** |
| 11 | **术语全文一致** |
| 12 | **面向 Claude 写作**：祈使句、第三人称、不解释为什么、不寒暄 |
| 13 | **脚本强健**：错误处理 + 关键数值注释 |
| 14 | **给予恰当自由度**：开放任务高自由度/关键流程低自由度 |
| 15 | **dependencies 声明 Python 依赖**（如需） |

## 熔断机制（4 道，sop.md 第 6 步详）

| # | 熔断 | 触发 | 动作 |
|---|---|---|---|
| 1 | SKILL.md 行数红线 | >500 行警告 / >600 行 | 强制拆 `references/` |
| 2 | description 强制公式 | 缺"当用户提及[关键词]或[场景]时使用" | 校验不通过 |
| 3 | Pipeline Gate 硬编码 | Pipeline 步骤缺 `if not user_confirmed: stop` | 无法打包 |
| 4 | Inversion 防骚扰上限 | 连续提问 >6 个无假设出口 | 强制生成假设让用户确认 |

## 资源索引（references/，按需加载）

| 文件 | 内容 | 状态 |
|---|---|---|
| `references/sop.md` | 完整 SOP（10 步工作流 + 11 项设计列表 + 反模式 11 项 + 验收门槛 + 实现路线 + Roadmap） | ✅ 已落地 |
| `references/architecture.md` | 哲学层（Skill 本质/Tool 辨析/配置三要素/运行机制/渐进式披露） | ✅ 已落地 |
| `references/pattern-tool-wrapper.md` | Tool Wrapper 索引+执行协议 + 三好处 + 骨架 | ✅ 已落地 |
| `references/pattern-generator.md` | Generator 6 步输出契约 + 风格/结构分离 | ✅ 已落地 |
| `references/pattern-reviewer.md` | Reviewer 证据 4 要素（位置/严重度/原因/修复） | ✅ 已落地 |
| `references/pattern-inversion.md` | Inversion 阶段化访谈 + 防骚扰 | ✅ 已落地 |
| `references/pattern-pipeline.md` | Pipeline 8 要素公式 + Gate 硬编码 | ✅ 已落地 |
| `references/anti-patterns.md` | 反模式 11 项实证清单 + 已知误报说明 | ✅ 已落地 |

## 脚本索引（scripts/，确定性执行）

| 脚本 | 作用 | 状态 |
|---|---|---|
| `scripts/init_skill.py` | 生成骨架（按 pattern 选建目录 + references 骨架文件 + 下一步提示动态化） | ✅ 已完成 |
| `scripts/diagnose.py` | 模式决策树（输入任务→输出推荐模式 + required/optional dirs 区分） | ✅ 已完成 |
| `scripts/validate.py` | 硬钳校验（name/description/行数/保留词/dependencies/占位符） | ✅ 已完成 |
| `scripts/audit.py` | 已有 skill 病灶诊断（11+ 项检查，不拒出包只报告） | ✅ 已完成 |
| `scripts/package_skill.py` | 打包（自动跑 validate 后生成 zip；`--target` 一键装到 claude/copilot/codex/openclaw/cursor/gemini/hermes/coze/workbuddy） | ✅ 已完成 |

## 与 marketplace 版 skill-creator 衔接

marketplace 版（`~/.workbuddy/plugins/cache/workbuddy-builtin/skill-skill-creator/0.1.0/`）提供 `init_skill.py` + `package_skill.py`，本元技能保留并增量加 `validate.py` / `diagnose.py` / `audit.py` + `architecture.md` + `anti-patterns.md` + 5 份 pattern references。

**关键差异**：marketplace 版强制力靠 prompt 措辞（"MUST reject"），本元技能强制力靠 `validate.py` 真校验。

## 自举声明

本 SKILL.md 严格遵守它教别人的所有规范：description ≤80 字 + 动词开头 + 关键词；正文 <200 行；详节全挪 `references/`；铁律条目化；5种模式知识外置。
