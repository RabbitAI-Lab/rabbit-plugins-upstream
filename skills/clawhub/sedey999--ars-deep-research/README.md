# ARS Deep Research — 学术深度研究技能包

> 源自开源项目 [imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills) 的通用可移植版本，已剥离原平台专属依赖，可在任意支持「SKILL.md + references/」技能目录规范的 Agent 网关中加载运行。

## 这是什么

一个领域无关的 **13+1 人研究智能体团队**：从选题发散到 APA 7.0 完整研究报告的全流程科研助手。内置苏格拉底式引导、系统性综述（PRISMA 2020）、元分析、证据分级、魔鬼代言人质疑、伦理审查与文献监控。

## 安装

解压本压缩包，将 `ars-deep-research/` 文件夹放入你所使用平台的技能目录（通常为 skills 目录），重启会话即可被识别。文件夹内根目录只有一份 `SKILL.md` 与一个 `references/` 目录，无需任何额外配置。

## 触发方式（自然语言即可，无需命令）

| 你想做的事 | 示例输入 |
|------------|----------|
| 完整研究 | "Research the impact of AI on higher education quality assurance" / "帮我深度研究 AI 对高教质保的影响" |
| 苏格拉底引导 | "引導我的研究：少子化對私立大學的影響" / "我不确定要研究什么，帮我想想" |
| 快速简报 | "给我一个 30 分钟级别的快速研究简报" |
| 文献综述 | "帮我做 XX 主题的文献综述" |
| 系统性综述/元分析 | "做一项 PRISMA 系统性综述" |
| 事实核查 | "核查这几个论断的证据" |
| 三方对比扫描 | "用 WHY/HOW/WHAT 框架快速比较这几篇论文" |
| 审阅已有文本 | "评审一下这份研究报告" |

## 8 种运行模式

`full`（默认完整研究）｜`quick`（快速简报）｜`review`（文本评审）｜`lit-review`（文献综述）｜`three-way-scan`（WHY/HOW/WHAT 扫描）｜`fact-check`（事实核查）｜`socratic`（苏格拉底引导，不确定时优先）｜`systematic-review`（PRISMA 系统综述 + 可选元分析）

## 目录结构

```
ars-deep-research/
├─ SKILL.md               # 主控调度（模式路由、6 阶段工作流、检查点规则）
└─ references/
   ├─ *_agent.md          # 14 个子角色 prompt（RQ 架构师、文献官、魔鬼代言人等）
   ├─ guides/             # 学术规范（APA7、PRISMA、证据金字塔、API 协议等）
   ├─ templates/          # 输出模板（研究简报、PRISMA 报告、证据评估卡等）
   ├─ examples/           # 8 个示例
   └─ shared/             # 跨技能共享协议与数据契约
```

## 运行环境自适应

本技能加载后先做环境自检（子 Agent 派生、并发、会话间通信、文件读取、视觉 OCR），任一能力缺失时自动降级为单会话角色扮演模式，**不会中断任务**。所有角色文件引用均为 `./references/...` 相对路径，跨 Windows/Linux/macOS 迁移无障碍。

## 与其它 ARS 技能包的关系

可完全独立运行。研究完成后可将 RQ Brief、方法论蓝图、文献库、综合报告移交给 `ars-academic-paper`（论文写作包）继续成稿；如需调研→写作→评审全自动流水线，另装 `ars-pipeline-orchestrator`（编排器包）。

## 版本

基于 ARS Deep Research v2.12.1（2026-08-15）移植，功能模式与角色配置完整保留。

---

## 移植溯源与更新指引

**原项目**：[imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)
（ARS，开源科研工具集；本包为剥离平台专属依赖后的通用可移植版）

**源目录 → 本包目录映射**（原项目变动时按此对照同步）：

| 原项目位置 | 本包位置 |
|------------|----------|
| `deep-research/SKILL.md` | `SKILL.md`（主控，少量段落按改动原则重写） |
| `deep-research/agents/*.md` | `references/*.md`（子角色文件，原样保留 + 附加通用学术规则） |
| `deep-research/references/*.md` | `references/guides/*.md`（changelog 除外，未随包附带） |
| `deep-research/templates/*` | `references/templates/*` |
| `deep-research/examples/*` | `references/examples/*` |
| 仓库 `shared/` 中被引用的协议与数据契约 | `references/shared/`（文件名扁平化；`contracts/` 保留原子目录） |

**基本改动原则**（下次更新时遵循同样规则）：

1. **剥离平台依赖**：删除斜杠命令、工具调用前钩子、fork/spawn 专属调度、插件市场协议、运行时校验脚本引用（以文字规则与可选配置项替代），不改变任何学术流程语义；
2. **目录标准化**：重构为单 SKILL.md + references/ 结构，全部角色文件引用改为 `./references/...` 相对路径；
3. **跨技能引用**：统一改写为 `ars-xxx/...` 新包名前缀（4 包并列安装在同一技能目录时互相可解析）；
4. **保留核心价值**：智能体团队、运行模式、防幻觉约束、评审逻辑、数据契约（JSON Schema）完整保留，仅删除平台绑定层；
5. **新增通用机制**：运行环境自检与降级、子 Agent 调度必读角色文件、5 条通用学术强制规则（已同步嵌入全部角色文件）。

**同步更新方法**：原项目对应技能目录（`deep-research/`）有版本变动时，先比对其 `SKILL.md` 与 `agents/` 的差异，按上表映射位置将变动内容合入本包，再按上述 5 条原则对新增文本做同样的平台依赖清理即可。
