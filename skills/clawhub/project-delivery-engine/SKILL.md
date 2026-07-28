---
name: project-delivery-engine
description: "让 AI 做几周或几个月的项目也不断档：持续保留进度、整理资料、支持多 AI 并行、独立复审和交接。用于项目立项或修复五件套、接续或继续项目、整理资料与状态、整理交接文件、项目内协作、派兵、并行、spawn agent（派子智能体）、worktree（隔离工作树）、独立复审、换新对话、生成启动语和项目收尾。仅在任务依赖当前项目状态或用户明确要求管理当前项目时使用；普通临时请求不使用。"
---

# 项目交付引擎 | Project Delivery Engine

让 AI 干几个月的事，仍然知道自己在干什么。

项目做得越久，AI 越容易忘记进度、弄乱文件，甚至把没做完的事说成做完了。项目交付引擎负责把项目状态持续管住。

- **很轻**：入口只有约 4KB，规则按需读取。
- **很狠**：关键成果可以交给另一个 AI 独立复审，专挑假完成。
- **很稳**：只要项目文件仍在，换窗口、换 AI、几个月后再回来，仍能从已保存状态继续。

**使用方法：** 选中本 Skill，然后输入：`项目立项`、`接续项目`、`整理交接文件`、`独立复审`、`并行（spawn agent，派子智能体）` 等。

**项目主页：** [GitHub｜项目交付引擎](https://github.com/haoyun18881-beep/project-delivery-engine)（作者 GitHub 主页）。

## 它会替用户管住什么

- 保存当前进度、下一步、风险和交接入口，换窗口不用重新解释。
- 把规则、当前状态、历史证据和真实物料分开，文件越多也不会越乱。
- 给子任务划定范围、验收要求和停止条件，多 AI 并行也不会各干各的。
- 让重要成果接受独立复审，不让做事的 AI 自己给自己判卷。
- 阶段结束时整理交接，新窗口、新 AI 或几个月后都能继续。

## 处理顺序

`SKILL.md` 只保留项目交付引擎的路由和硬边界，细则按需读取 references。

1. 以用户最新指令和当前项目文件确定任务边界；仅任务依赖当前项目状态或用户明确要求管理当前项目时套用本 Skill，普通临时请求和不依赖项目状态的一次性并行任务不得建档。
2. 任务依赖项目状态时，按 [references/project-state.md](references/project-state.md) 检查项目根、五件套和必要索引。新建或修复文件时再读 [references/project-file-templates.md](references/project-file-templates.md)。
3. 简单主线程任务直接执行。需要协作、并行、worktree（隔离工作树）或确认时，按 [references/collaboration.md](references/collaboration.md) 选择路线；真实分工再读 [references/taskcard-evidencebundle.md](references/taskcard-evidencebundle.md)。
4. 任务结束时按 [references/project-state.md](references/project-state.md) 判断是否需要沉淀。

机械检查、编号、启动语和治理文件受控写入见 [references/project-gov-cli.md](references/project-gov-cli.md)。

第一次使用、用户询问具体用法或 `project-gov` 报错时，再读 [references/quickstart-faq.md](references/quickstart-faq.md)。

## 硬边界

- 主线程负责最终采纳；协作线程、脚本和证据包不能代替主线程宣布完成或合并结果。
- 项目 `AGENTS.md` 只写项目身份、专有事实、授权和边界，不复制本 Skill 的通用规则。
- 对治理范围进行建档、checkpoint（检查点）或交接写入时，必须使用 `project-gov propose（预演）→ apply（执行）`；工具无法表达时必须停止并说明，不得绕过。
- 只选择当前任务需要的引用文件；选中后必须完整读取。
