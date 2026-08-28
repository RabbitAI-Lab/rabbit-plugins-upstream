---
name: jys-skill-suite-ai-shop-drama
description: |
  JYS AI 带货短剧工作流（WorkBuddy 版入口）。把带货短剧从选套路、剧情改造、选产品、逐段写作到最终拍摄稿，放进一套可续接、可协作、可维护数据库的 JYS 工作流。包含 jys 主控与 jys-s1～jys-s5 五个执行阶段，须一起安装。当用户说“使用 JYS / 做个带货短剧 / 继续上次 JYS 项目 / 录入剧本 / 录入产品”等时触发。
version: 2026.8.10.2
category: content-creation
triggers:
  - "JYS"
  - "带货短剧"
  - "AI带货短剧"
  - "短剧脚本"
  - "带货剧本"
  - "使用JYS"
license: MIT
author: BetterCallLu
---

# JYS AI 带货短剧（WorkBuddy 入口）

> 本文件是 **WorkBuddy** 的入口。原 Codex 版本完全保留：`jys/SKILL.md` 为主控、`jys-s1/`～`jys-s5/` 为各阶段，Codex 用户照常使用。WorkBuddy 用户以本文件为总入口，运行方式见下方「执行流程」。

## 你会得到什么

- **S1 选套路 / 数据库入库**：选择或推荐内核与变体，解析用户上传的新剧本并同步归档剧本及产品，或单独维护产品数据库（`jys-s1/SKILL.md`）
- **S2 去重替换**：拆解选定套路变体，按真实前置依赖分层批量确认人物组合、大替换、小替换或产品强绑定套路的因果链重构（`jys-s2/SKILL.md`）
- **S3 选产品**：从现有带货产品库读取并确认当前项目使用的产品（`jys-s3/SKILL.md`）
- **S4 写剧本**：把 S2 剧情骨架细化为事件级大纲，确定产品植入并逐段完成台词（`jys-s4/SKILL.md`）
- **S5 最终整理**：根据 S4 完整剧本添加场景标注，提取人物、场景和重要道具，生成 3 类 6 个标题并输出分幕拍摄模板（`jys-s5/SKILL.md`）
- 共享套路库 / 剧本库 / 产品库位于 `jys/assets/`

## 工作区约定（WorkBuddy）

- 将当前项目的实际根目录记为 `JYS_PROJECT_ROOT`：优先使用用户明确指定的目录，否则使用当前 WorkBuddy 任务的工作区根目录。
- 将 `JYS_WORKSPACE` 固定为 `JYS_PROJECT_ROOT/jys-workspace`。同一项目全程使用该目录；不要根据任务名或对话标题重新推断。
- 首次使用时，创建 `JYS_WORKSPACE`，将 `jys/assets/workspace-template.md` 复制为 `JYS_WORKSPACE/status.md` 并填写项目绑定信息。
- 详细路径、状态、默认续接与旧项目兼容以 `jys/references/workspace-contract.md` 为准。

## 调度表

| 步骤 | 阶段文件 | 前置条件 | 完成条件 |
|---|---|---|---|
| S1 选套路/数据库入库 | `jys-s1/SKILL.md` | 无 | 用户确认内核和变体并更新状态；剧本及非黑名单产品全部入库 |
| S2 去重替换 | `jys-s2/SKILL.md` | S1 完成；内核标注产品机制改变因果链时 S3 也须完成 | 用户确认定制化剧情骨架 |
| S3 选产品 | `jys-s3/SKILL.md` | 产品已在数据库 | 用户确认数据库中的产品 |
| S4 写剧本 | `jys-s4/SKILL.md` | S1–S3 完成 | 全部段落写完并逐段确认 |
| S5 最终整理 | `jys-s5/SKILL.md` | S4 完成 | 交付可复制的模板化完整文本 |

## 执行流程（WorkBuddy）

1. 初始化或恢复 `JYS_WORKSPACE`，读取 `status.md`；旧状态先按 `jys/references/workspace-contract.md` 兼容迁移。
2. 识别用户指定的步骤；未指定时读取 `status.md` 的 `next_skill`，只询问真正阻塞的信息。
3. **调度对应阶段**：直接用 WorkBuddy 的「读取文件」能力打开对应的 `jys-sN/SKILL.md`，**完整阅读后严格按其指令执行**（不要只凭本文件概括）。
4. 用户确认结果后，按该阶段要求写入规定文件，并更新 `status.md` 的 `current_skill` / `next_skill` / `next_action` / `waiting_for`。
5. 每轮结束按调度表展示「下一步默认调用」与「默认动作」尾注：
   - 普通路线：S1 → S2 → S4 → S5
   - 产品强绑定路线：S1 → S3 → S2 → S4 → S5
6. 各阶段所需的共享契约、开头钩子设计指南等见 `jys/references/`；套路 / 剧本 / 产品库见 `jys/assets/`。

## 规则要点

- 用户未明确指定子阶段时，由主控读取 `status.md` 并调用 `next_skill`；不要重复询问「是否继续」。
- 只有缺少不可替代的用户选择、事实、文件或唯一项目路径时才提问。
- 不对产品或套路做主观评判、贴标签或臆测适配关系。
- 新产品入库由 S1 负责；S3 发现产品缺失时先返回 S1，禁止自行写库。
- 仅在用户确认后标记步骤完成。
- 用户提到开头 / 开场 / 第一幕 / 前几秒 / 钩子时，先按 `status.md` 判断阶段：S2 未完成调度 S2，S2 已完成调度 S4，并完整读取 `jys/references/开头钩子设计指南.md` 后处理。
