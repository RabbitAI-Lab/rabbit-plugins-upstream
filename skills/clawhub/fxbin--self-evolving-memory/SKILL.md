---
name: self-evolving-memory
archetype: mentor
description: 为 AI Agent 部署分层自进化记忆系统的 mentor skill。核心状态保存在本地文件；语义检索和定时触发是可选 Host 能力。覆盖三层存储（即时 ≤20KB / 近中期 / 长期检索）、事务化巩固与回滚、多因子晋升、事件因果图谱、主题索引、回忆规划器和证据账本。当用户要初始化或修复 Agent 记忆、轻量记录、跑巩固、评估晋升、回滚校验、建索引或规划检索时触发。
---

# 自进化记忆系统

为 AI Agent 部署分层自进化记忆系统：三层存储 + 事务化巩固守卫 + 完整写集回滚 + 多因子晋升 + 两大索引 + 回忆侧双引擎（回忆规划器 + 证据账本），共 13 大模块。核心状态以本地文件为真相源；定时触发和语义检索按 Host 能力启用，并有手动调度与本地检索降级。产品定位见 [docs/positioning.md](docs/positioning.md)，完整版本历史见 [CHANGELOG.md](CHANGELOG.md)。

**版本**：v7.3.3 · 13大模块 · 2026-07-23

## Core role

- 覆盖领域：AI Agent 的分层记忆管理——从即时层工作记忆到长期语义检索的完整闭环。
- 质量标准：每次干预后，记忆系统应通过快照回滚校验、晋升评分闭环、检索充分性校验三道关卡。
- 不做什么：不替代具体业务逻辑，不把 Host 可选能力冒充为本地实现，不在上下文文件中存明文凭证，不由巩固流程修改核心身份定义（SOUL.md）。

## Trigger cues

- 用户要"初始化记忆系统""部署记忆""给 Agent 装记忆"（模块一）
- 用户要"记忆巩固""跑一次巩固""沉淀记忆""安全守卫"（模块三 + 模块九）
- 用户要"评估晋升""这条记忆该不该升级"（模块四）
- 用户要"回滚记忆""安全校验""快照恢复"（模块三）
- 用户要"自我认知""身份演化""关系理解""Agent 反思自己"（模块二）
- 用户要"技能建议冷却""Agent 反复提建议""驳回建议"（模块五）
- 用户要"检索校验""回忆规划""证据账本"（模块八 + 模块十二 + 模块十三）
- 用户要"因果图谱""主题索引""事件关联"（模块六 + 模块七）
- 用户要"主动探索""认知拉伸""盲区发现"（模块十）
- 用户要"DPM 动态分层""Trace Forest""角色切片""微巩固"（模块十一）
- 用户只说"记一下""记住这条"（包括"赶紧记一下"）时进入 `lightweight_record`，只做一次安全归属与写入，不启动巩固/微巩固/晋升工作流（模块一）

## 快速上手

第一次使用？按 [快速上手指南](references/quick-start-guide.md) 走四步：初始化 → 写入第一条记忆 → 触发巩固 → 体验回忆。fresh init 必须从 [assets/](assets/) 使用 5 个即时层模板（USER / MEMORY / SOUL / TOOLS / SECRET）、3 个核心自我指涉模板（growth-journal / user-profile / relationship）和仅在索引不存在时使用的 index 模板；Calendar 与语义检索均为可选 Host 能力。

## Workflow

1. **诊断**：确认用户的记忆系统当前状态——是否已有即时层文件？是否已有近中期层索引？巩固流程是否在运行？识别用户处于初始化阶段还是优化阶段。
2. **路由**：根据需求选择模块——初始化走部署指南，巩固走执行手册，晋升走评分协议，检索走回忆规划器+证据账本，探索走主动探索模块。只加载需要的参考文档。
3. **执行**：按对应模块的分步流程执行操作，每步完成后立即校验（文件容量、格式规范、快照完整性）。
4. **校验**：执行后跑安全校验——即时层 ≤20KB、SOUL.md 字节不变、SECRET.md 只含 handle/locator 与脱敏元数据、格式规范正确。巩固与微巩固的任何失败都按模块三恢复状态机回滚完整 write-set。

## Output template

1. `Diagnosis`：用户记忆系统当前处于什么阶段，缺少什么，最该做什么
2. `Priority moves`：按模块路由的最高优先级操作（初始化 / 巩固 / 晋升 / 检索 / 回滚）
3. `Why this works`：基于的设计原则（分层是注意力管理、巩固是提炼、安全是底线）
4. `Watchouts`：常见坑——即时层超容、SOUL.md 被改写、巩固跳过快照、检索只搜一次就放弃

## 系统架构

**三层记忆存储 + 两大索引体系 + 自我指涉子系统 + 回忆侧双引擎 + 四个协议模块**

```
┌─────────────────────────────────────────────────┐
│              回忆侧双引擎（检索前+检索后）         │
│  回忆规划器（Recall Planner）→ 证据账本（Evidence Ledger）
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│              三层记忆架构                          │
│  即时层（USER/MEMORY/SOUL/TOOLS 自动加载）≤20KB │
│  SECRET 仅存 handle/locator，0600，按需读取       │
│  近中期层（recent_memory/index + 分类文件）       │
│  长期层（可选 memory_search / 本地白名单检索）     │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  两大索引：事件因果图谱 + 主题实体索引              │
│  四个协议：巩固守卫 / 晋升评估 / 技能冷却 / 检索手册 │
│  自我指涉子系统：growth-journal / user / relationship / diaries
└─────────────────────────────────────────────────┘
```

## 模块索引

| # | 模块 | 一句话说明 | 详细文档 |
|---|------|-----------|---------|
| 1 | 分层存储 | 即时/近中期/长期三层架构，容量驱动的筛选机制 | [references/01-layered-storage.md](references/01-layered-storage.md) |
| 2 | 自我指涉 | Agent对自身、用户、关系的认知与反思 | [references/02-self-reference.md](references/02-self-reference.md) |
| 3 | 记忆巩固守卫 | 防止巩固过程中自我改写失控的安全闸 | [references/03-consolidation-guard.md](references/03-consolidation-guard.md) |
| 4 | 多因子晋升评估 | 10分制评估记忆是否应该晋升层级 | [references/04-promotion-protocol.md](references/04-promotion-protocol.md) |
| 5 | 技能建议冷却 | 管理技能建议的生命周期，避免反复折腾 | [references/05-skill-suggestion-cooldown.md](references/05-skill-suggestion-cooldown.md) |
| 6 | 事件因果图谱 | 按时间线+因果链组织记忆节点 | [references/06-event-causality-graph.md](references/06-event-causality-graph.md) |
| 7 | 主题实体索引 | 按主题聚合跨层级记忆指针 | [references/07-topic-entity-index.md](references/07-topic-entity-index.md) |
| 8 | 检索校验回路 | 四级检索+结果校验+自我进化 | [references/08-retrieval-verification.md](references/08-retrieval-verification.md) |
| 9 | 记忆巩固执行手册 | 巩固操作的分步执行指南 | [references/09-consolidation-manual.md](references/09-consolidation-manual.md) |
| 10 | 主动探索与认知拉伸 | 主动发现盲区，扩展认知边界 | [references/10-active-exploration.md](references/10-active-exploration.md) |
| 11 | DPM 动态分层增强（全称：DPM 启发的动态分层记忆增强） | DeepTutor 启发的动态记忆分层 | [references/11-dpm-enhancement.md](references/11-dpm-enhancement.md) |
| 12 | 证据账本 | HMS启发的检索后证据结构化输出 | [references/12-evidence-ledger.md](references/12-evidence-ledger.md) |
| 13 | 回忆规划器 | 检索前的问题拆解与策略匹配 | [references/13-recall-planner.md](references/13-recall-planner.md) |

**其他参考文档：**
- [快速上手指南](references/quick-start-guide.md) — 30分钟四步跑通记忆系统
- [部署指南](references/deployment-guide.md) — 初始化新Agent记忆系统、容量管理、自检清单
- [设计原则与技术约束](references/design-principles.md) — 设计理念与边界
- [版本历史](CHANGELOG.md) — v1到v7的完整迭代记录
- [操作手册笔记](references/playbook-notes.md) — 核心启发式规则与反模式

## 快速部署检查清单

- [ ] 5 个即时文件和 3 个核心自我指涉文件均从模板 create-only 初始化；已有文件未覆盖
- [ ] 仅 USER/MEMORY/SOUL/TOOLS 自动加载；SECRET 为 0600，可信本地 scanner 返回 locator-only/clean 且不暴露匹配内容
- [ ] MEMORY.md 有两个分区：长期行为规则 + 核心状态锚点
- [ ] TOOLS.md 按索引格式维护，详情放 recent_memory/tools/
- [ ] recent_memory/index.json 索引存在
- [ ] Host 有 Calendar/调度器时才设置定时任务；否则已保存手动巩固清单
- [ ] Host 有 memory_search 时验证授权语义检索；否则已验证排除 SECRET/事务文件的本地白名单检索

完整部署指南见 [references/deployment-guide.md](references/deployment-guide.md)。
