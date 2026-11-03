---
name: commit
description: |
  在 Git 仓库中分析当前变更，生成符合项目规范的 commit message，自动判断单次提交还是按功能拆分多次提交，全部提交成功后自动推送当前分支到远端；正常情况全自动不询问，命中异常规则（不能或无须提交的文件等）才请用户确认。
  TRIGGER（中文）："提交一下代码""帮我 commit""这次改动提交了吧""生成 commit message 并提交""/commit""按 fix 提交"
  "先看看变更别提交""改一下上次的 commit"。
  DO NOT TRIGGER：用户只想看变更且未表达提交意图（直接执行 git status/diff 即可）；
  单独的 push、pull、rebase 等远端或历史操作（无提交意图，按普通指令处理并单独确认）；非 Git 仓库环境。
metadata:
  version: 1.3.1
  created: 2026-09-25
  updated: 2026-10-28
---

# Commit：Git 提交工作流

一条指令完成：检查变更 → 生成 commit message → 自动判断单次或按功能拆分提交 → 推送当前分支 → 回报 hash。正常情况全自动，只有命中异常规则才请用户确认。message 必须来自真实 diff，不许推测需求背景。全流程按「工作流」的轮次预算执行，正常 2~4 次工具调用内完成。

## 核心原则

1. **正常自动，异常确认。** 未命中异常规则的提交直接执行，不询问；命中任一异常规则必须停下展示并等用户决定，不许默默提交。拿不准的普通内容按正常提交处理，并在回报中说明判断依据；涉及密钥/凭证/大规模删除而拿不准时，一律按异常停下先问。
2. **message 只写 diff 里真实存在的改动。** 不虚构背景、不夸大范围、不凑格式写空 body。
3. **最小写入。** 分析阶段只读（status/diff/log/读文件），写入仅限 git add、git commit（含 /commit amend 的 --amend）与按「推送规则」推送当前分支。
4. **项目规范优先。** 项目 AGENTS.md/CLAUDE.md 或 git log 已有 commit 风格时从之，本 skill 的格式只是无规范时的兜底。
5. **拆分只到文件级。** 多主题拆分按文件分组；同一文件内混多个主题时不做 hunk 级拆分，归入主要主题所在组，回报时说明。
6. **最小轮次。** 执行慢的根源是工具调用往返次数：收集类只读命令必须合并为一次调用；`git add`、`git commit`、`git push` 用 `&&` 链式合并；分析在内部一次完成，不为已定案的步骤增加往返。

## 工作流（轮次预算：收集 1 轮 → 分析 0 轮 → 提交推送 1~2 轮 → 回报 1 轮）

1. **收集（必须一次调用跑完，禁止拆成多条命令逐个执行）**：

   ```bash
   git -c core.quotepath=false status -sb; echo '===DIFF==='; { git -c core.quotepath=false diff HEAD -U2 2>/dev/null || git -c core.quotepath=false diff --cached -U2 2>/dev/null; } | head -c 24000; echo; echo '===STAT==='; { git -c core.quotepath=false diff HEAD --stat 2>/dev/null || git -c core.quotepath=false diff --cached --stat 2>/dev/null; }; echo '===LOG==='; git log --format='%s' -10 2>/dev/null; echo '===REMOTE==='; git remote -v; git rev-parse --abbrev-ref '@{u}' 2>/dev/null || echo '(无上游)'
   ```

   各段用 `;` 分隔，单段失败（如空仓库无 log）静默跳过，不中断后续段。status 首行 `##` 为当前分支、上游与领先/落后（behind 可预判推送会被拒），其余行首列字母区分暂存状态。diff 与 STAT 段在无 HEAD（空仓库首次提交）时自动回退 `--cached`，暂存内容同样可见。有 HEAD 时 `git diff HEAD` 已含暂存与未暂存改动；diff 超出 24000 字符被截断时，按同轮 STAT 段定位大文件，仅对关键文件补看，不追加调用、不整段重读。未跟踪新文件（`??`）diff 不可见，全部用一条命令补看要点：`head -150 <文件1> <文件2> ...`（`??` 为目录时先展开内部文件列表，如 `find <目录> -type f` 拼入同一条命令），不逐文件调用、不全文读取；明显二进制后缀（图片 / 字体 / 压缩包等）跳过补看，按文件名归组即可；文件超量（如整目录几十个）先列文件清单，再挑关键文件补看。`-c core.quotepath=false` 使中文文件名直接可读、不被八进制转义。LOG 段学习项目 message 风格，无输出即视为无历史、跳过。
2. **异常检查 + 分组 + 生成 message（纯内部推理，不产生工具调用，不输出中间过程）**：对照「异常清单」对全部变更统一检查；命中任一项 → 展示发现 + 处理建议 + 建议 message，等用户指示，不执行任何 add/commit。全部未命中 → 直接定稿分组与 message：变更主题单一 → 一个 commit；多个不相关主题 → 按功能拆分，一个功能/一个修复一组，每组独立 message；暂存区原有内容与工作区变更统一分析分组，预暂存文件必须划入第一组（见步骤 3 的暂存区纪律），划不进（如横跨多主题）按异常确认；同一文件的暂存与未暂存改动分属不同主题时同理（文件级拆分无法分离同一文件的两种状态）。message：项目已有风格按项目风格；无风格兜底 `type: 中文描述`（type 英文、描述中文，50 字内说清改了什么）；改动跨多个模块时补 body 分点说明。
3. **提交并推送（能用 `&&` 连接的写进同一条命令）**：

   暂存区纪律：每次 `commit` 时暂存区须恰好等于当前组的文件——首组提交时预暂存集天然已在索引中（首组无预暂存文件则与普通情形相同），此后各组先 `add` 后 `commit` 即满足。不要用 `git commit -- <路径>` 部分提交绕开分组限制：与改写文件的 pre-commit 钩子（如 lint-staged）组合会留下索引与 HEAD 不一致的残留（已实测）。

   单组一条命令完成提交与推送：

   ```bash
   git add <该组文件> && git commit -m "$(cat <<'EOF'
   type: 中文描述
   EOF
   )" && git push
   ```

   多组：全部组串成一条命令一次执行，组再多也不拆成多次调用：

   ```bash
   git add <组1文件> && git commit -m "$(cat <<'EOF'
   type: 描述一
   EOF
   )" && git add <组2文件> && git commit -m "$(cat <<'EOF'
   type: 描述二
   EOF
   )" && git push
   ```

   链尾 push 形态按「推送规则」：有上游 `git push`，无上游 `git push -u origin HEAD`（HEAD 自动解析当前分支名，无须先查分支；单组同理；/commit local 链尾不接 push）。`&&` 链保证任一组 commit 失败（含 pre-commit hook 拒绝）即中断，后续组不执行、不会推送，已成功的 commit 保留在本地；重跑时从失败的那组继续，只补做剩余组的 add/commit/push，已成功的组不重复提交。
4. **回报**：每个 commit 的 message + 文件统计 + 短 hash；多个 commit 逐条列出；推送结果一并回报（成功注明远端分支，失败注明原因）；有值得注意的判断（如拆分依据、同文件混主题归组）附一句说明。

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

判据：完整且有价值的独立改动走拆分（工作流步骤 2）；噪声与残留才进本清单。

**其他异常**：
- 依赖变更：package.json / lock 文件增删依赖（需用户知情）
- 大规模删除或重写（如单文件内容删过半）
- 变更完全无法归纳出合理主题
- 仓库处于合并/变基中（存在 UU 等未解决冲突路径）：不代提 merge commit，等用户处理

命中时展示：具体异常 + 处理建议（剔除/保留/拆分）+ 建议 message，等用户指示后继续。

## 推送规则（用户 2026-10-09 授权默认推送）

- **范围**：只推当前分支。有上游 → `git push`；无上游但有远端 → `git push -u origin HEAD` 建立跟踪（HEAD 自动解析为当前分支名）。
- **时机**：push 以 `&&` 接在最后一组 commit 之后，链条本身保证全部 commit 成功才推。任一组被 pre-commit hook 拒绝或 commit 失败 → 停止推送，如实报告等用户处理（已成功的 commit 保留在本地）；/commit local、/commit status 不推；无远端仓库跳过推送并说明。
- **失败即停**：推送被拒（远端有新提交）、无权限、网络失败 → 如实报告原因，已完成的 commit 照常回报，不自动 pull / rebase / force。
- **amend 后默认不推**：改写已推送历史需 force push（默认禁止），仅用户明确要求时执行。

## 子命令

| 用法 | 行为 |
|---|---|
| /commit | 完整流程，类型自动判断，提交后自动推送 |
| /commit feat | 强制类型（fix / refactor / perf / docs / chore / test 同理），跳过类型判断，其余流程不变 |
| /commit local | 只提交不推送：流程与 /commit 完全一致，跳过推送步骤 |
| /commit status | 干跑：展示变更分析 + 建议 message + 拆分建议，不执行任何 add/commit/push |
| /commit amend | 修改上一次 commit：无新变更时只改 message；有变更时并入当前变更（工作区与暂存区，先走异常检查）后重新生成 message。一律先展示（原 hash + 原 message → 新 message）等确认；amend 后默认不推送；该 commit 已 push 时提示改写需 force push 同步远端（默认禁止），用户明确要求才继续 |

自然语言等价说法（"这次按 fix 提交""先看看变更别提交""改下刚才的 commit""只提交别推"）同样路由到对应子命令。

## 默认禁止（用户明确要求除外）

git reset / clean / checkout / restore / rebase / cherry-pick / stash / pull / 任何 --force / 任何 --no-verify；修改代码、删除文件、移动文件。amend 仅在 /commit amend 显式调用时执行。push 仅限「推送规则」场景：提交后的当前分支常规推送；amend 后的 push 与 force push 一律默认禁止。

## 边界情况

- **非 Git 仓库**：告知当前目录不是 Git 仓库，不做任何操作。
- **工作区为空**：直接告知无可提交内容，不做任何操作。
- **同文件混多主题**：按核心原则 5 归入主要主题组，回报时说明，不阻塞、不询问。
- **提交后用户对 message 不满**：未 push 的 commit 用 /commit amend 修正；已 push 的默认不动（force push 须用户明确要求），不擅自改历史。
- **pre-commit hook 拒绝提交**：如实报告失败原因，停止推送，等用户处理；禁止 --no-verify 绕过，不自行改代码消警。
- **push 失败或无远端**：如实报告或说明，commit 结果照常回报，不自动 pull，等用户处理后再推。
