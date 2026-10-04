---
name: commit
description: |
  在 Git 仓库中分析当前变更，生成符合项目规范的 commit message，自动判断单次提交还是按功能拆分多次提交；正常情况全自动不询问，命中异常规则（不能或无须提交的文件等）才请用户确认。
  TRIGGER（中文）："提交一下代码""帮我 commit""这次改动提交了吧""生成 commit message 并提交""/commit""按 fix 提交"
  "先看看变更别提交""改一下上次的 commit"。
  DO NOT TRIGGER：用户只想看变更且未表达提交意图（直接执行 git status/diff 即可）；
  push、rebase 等远端或历史操作（按普通指令处理并单独确认）；非 Git 仓库环境。
metadata:
  version: 1.0.0
  created: 2026-09-25
---

# Commit：Git 提交工作流

一条指令完成：检查变更 → 生成 commit message → 自动判断单次或按功能拆分提交 → 回报 hash。正常情况全自动，只有命中异常规则才请用户确认。message 必须来自真实 diff，不许推测需求背景。

## 核心原则

1. **正常自动，异常确认。** 未命中异常规则的提交直接执行，不询问；命中任一异常规则必须停下展示并等用户决定，不许默默提交。拿不准的普通内容按正常提交处理，并在回报中说明判断依据；涉及密钥/凭证/大规模删除而拿不准时，一律按异常停下先问。
2. **message 只写 diff 里真实存在的改动。** 不虚构背景、不夸大范围、不凑格式写空 body。
3. **不碰工作区。** 分析阶段只读（status/diff/log/读文件），唯一写入是 git add 与 git commit（含 /commit amend 的 --amend）。
4. **项目规范优先。** 项目 AGENTS.md/CLAUDE.md 或 git log 已有 commit 风格时从之，本 skill 的格式只是无规范时的兜底。
5. **拆分只到文件级。** 多主题拆分按文件分组；同一文件内混多个主题时不做 hunk 级拆分，归入主要主题所在组，回报时说明。

## 工作流

1. **收集**：`git status --short`、`git diff`、`git diff --cached`、`git log --oneline -10`（学习项目 message 风格，仓库无提交历史时跳过）；未跟踪的新文件 diff 不可见，直接读文件内容。
2. **检查异常**：对照下方「异常清单」，在提交前对全部变更统一检查；命中任一项 → 展示发现 + 处理建议 + 建议 message，等用户指示，不执行任何 add/commit。全部未命中 → 继续。
3. **分组**：变更主题单一 → 一个 commit；多个不相关主题 → 按功能拆分，一个功能/一个修复一组，每组独立 message，逐组提交。暂存区原有内容与工作区变更统一分析分组。
4. **生成 message**：项目已有风格按项目风格；无风格兜底 `type: 中文描述`（type 英文、描述中文，50 字内说清改了什么）；改动跨多个模块时补 body 分点说明。
5. **提交**：逐组 `git add <该组文件>` + `git commit`（message 用 heredoc 传参）。
6. **回报**：每个 commit 的 message + 文件统计 + 短 hash；多个 commit 逐条列出；有值得注意的判断（如拆分依据、同文件混主题归组）附一句说明。

## 类型判断

| type | 用于 |
|---|---|
| feat | 新功能、新页面、新接口对接 |
| fix | 缺陷修复 |
| refactor | 不改行为的结构调整 |
| perf | 性能优化 |
| docs | 纯文档 |
| chore | 依赖、配置、脚手架 |
| test | 测试相关 |

拿不准 feat 还是 fix 看动因：为已有功能补能力是 feat，为已有功能修错误是 fix。

## 异常清单（命中任一才停下确认）

**不能提交的文件**：
- 密钥与凭证：.env、*.pem、*.key、id_rsa、token 类文件
- 敏感内容：代码中新出现的硬编码密码/密钥/内网地址
- 系统与临时文件：.DS_Store、*.log、*.swp、tmp/、草稿文件
- 构建产物：dist/、build/、*.min.js（项目有提交构建产物惯例的除外）

**无须提交的文件**（明显与本任务无关的顺手混入）：
- 本地个人配置、个人脚本、调试文件
- 明显无关的独立小改动（如无关格式化）

判据：完整且有价值的独立改动走拆分（工作流步骤 3）；噪声与残留才进本清单。

**其他异常**：
- 依赖变更：package.json / lock 文件增删依赖（需用户知情）
- 大规模删除或重写（如单文件内容删过半）
- 变更完全无法归纳出合理主题
- 仓库处于合并/变基中（存在 UU 等未解决冲突路径）：不代提 merge commit，等用户处理

命中时展示：具体异常 + 处理建议（剔除/保留/拆分）+ 建议 message，等用户指示后继续。

## 子命令

| 用法 | 行为 |
|---|---|
| /commit | 完整流程，类型自动判断 |
| /commit feat | 强制类型（fix / refactor / perf / docs / chore / test 同理），跳过类型判断，其余流程不变 |
| /commit status | 干跑：展示变更分析 + 建议 message + 拆分建议，不执行任何 add/commit |
| /commit amend | 修改上一次 commit：无新变更时只改 message；有变更时并入当前变更（工作区与暂存区，先走异常检查）后重新生成 message。一律先展示（原 hash + 原 message → 新 message）等确认；该 commit 已 push 时提示改写需 force push 同步远端（默认禁止），用户明确要求才继续 |

自然语言等价说法（"这次按 fix 提交""先看看变更别提交""改下刚才的 commit"）同样路由到对应子命令。

## 默认禁止（用户明确要求除外）

git push / reset / clean / checkout / restore / rebase / cherry-pick / stash / 任何 --force / 任何 --no-verify；修改代码、删除文件、移动文件。amend 仅在 /commit amend 显式调用时执行。

## 边界情况

- **非 Git 仓库**：告知当前目录不是 Git 仓库，不做任何操作。
- **工作区为空**：直接告知无可提交内容，不做任何操作。
- **同文件混多主题**：按核心原则 5 归入主要主题组，回报时说明，不阻塞、不询问。
- **提交后用户对 message 不满**：未 push 的 commit 用 /commit amend 修正，不擅自改历史。
- **pre-commit hook 拒绝提交**：如实报告失败原因，等用户处理；禁止 --no-verify 绕过，不自行改代码消警。
