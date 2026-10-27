# Lightweight Git Workflow Assistant Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有全流程 Git 管理 skill 收敛为只负责 README 规则同步、feature 分支安全创建、工作流状态检查和开发完成检查的轻量助手。

**Architecture:** `SKILL.md` 是唯一运行时路由和安全规则入口，`templates/readme-git-workflow.md` 是写入项目 README 的唯一工作流文本来源。skill 只允许在用户明确授权后写 README 托管区块或创建本地 feature 分支，其余检查保持只读，并禁止合并、推送、发布、历史重写和分支删除。

**Tech Stack:** Markdown skill、Git CLI、Windows PowerShell、Codex/Agent 文件编辑工具

---

## 实施说明

- 设计依据：`docs/superpowers/specs/2026-08-11-lightweight-git-workflow-assistant-design.md`
- 目标目录当前不是 Git 仓库，因此本计划不包含 `git commit` 步骤。实施完成后只报告文件变化；除非用户把目录纳入仓库并明确要求提交，否则不创建提交。
- 本次不删除或改写现有 `README.md`、`workflows/`、`guides/`、`references/`、`scripts/` 和 `docs/RELEASE_SCRIPT_USAGE.md`。
- 旧文件不再被 `SKILL.md` 引用，因此不再参与运行时决策。
- 所有文件修改使用 `apply_patch`；验证命令只读，冒烟测试仅在明确的临时目录中创建测试仓库。

## 文件结构

### 修改

- `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`
  - 负责激活门禁、禁止边界、README 同步流程、feature 创建流程、状态检查、完成检查和异常处理。

### 新增

- `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`
  - 保存完整托管标记和面向项目协作者的工作流说明，是 README 工作流文本的唯一模板来源。

### 保留但不再引用

- `C:/Users/wangyikan/.agents/skills/git-workflow/README.md`
- `C:/Users/wangyikan/.agents/skills/git-workflow/workflows/`
- `C:/Users/wangyikan/.agents/skills/git-workflow/guides/`
- `C:/Users/wangyikan/.agents/skills/git-workflow/references/`
- `C:/Users/wangyikan/.agents/skills/git-workflow/scripts/`

---

### Task 1: 建立唯一 README 工作流模板

**Files:**
- Create: `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`

- [ ] **Step 1: 验证模板尚不存在**

Run:

```powershell
$template = 'C:\Users\wangyikan\.agents\skills\git-workflow\templates\readme-git-workflow.md'
Test-Path -LiteralPath $template
```

Expected: 输出 `False`。如果已存在，先读取内容并与本任务要求比较，不覆盖未知用户修改。

- [ ] **Step 2: 创建模板目录**

Run:

```powershell
New-Item -ItemType Directory -Force -Path 'C:\Users\wangyikan\.agents\skills\git-workflow\templates'
```

Expected: 返回 `templates` 目录，且不修改其他目录。

- [ ] **Step 3: 使用 apply_patch 创建完整模板**

创建文件，内容必须精确覆盖以下协作信息：

````markdown
<!-- GIT_WORKFLOW_START -->
## Git 工作流

本项目使用 `main`、`dev`、`feature/*`、`release/*` 和 `hotfix/*` 管理开发、测试与发布。

### 分支职责

| 分支 | 用途 | 生命周期 |
| --- | --- | --- |
| `main` | 生产基准，始终保持可发布 | 常驻 |
| `dev` | 集中集成已完成的 feature，供开发环境测试 | 常驻，可按团队流程重建 |
| `feature/*` | 单个需求或功能的独立开发 | 短期 |
| `release/*` | 从 `main` 创建，选择性纳入本次发布内容并完成回归验证 | 短期 |
| `hotfix/*` | 从 `main` 创建，处理生产紧急问题 | 短期 |

### 分支流向

```text
开发：main -> feature/* -> dev
发布准备：main -> release/* <- feature/*
正式发布：release/* -> main
热修复：main -> hotfix/* -> main，并将修复同步到 dev
```

### 关键约束

1. 禁止将 `dev` 合并到 `main`。
2. `main` 只接受经过验证的 `release/*` 同步，`hotfix/*` 除外。
3. 禁止对 `main`、`dev`、`release/*` 等公共分支执行 rebase 或 force push。
4. feature 合入 `dev` 前、release 或 hotfix 合入 `main` 前必须经过 PR/MR 审查。
5. feature 需要通过单元测试，dev 需要通过集成测试，release 需要通过回归测试。

### 分支命名

- 功能分支：`feature/<kebab-case-description>`
- 带需求编号的功能分支：`feature/<issue-id>-<kebab-case-description>`
- 发布分支：`release/<version>` 或 `release/<yyyy-mm-dd>`
- 热修复分支：`hotfix/<kebab-case-description>`
- 描述统一使用小写 kebab-case，不使用中文、空格或下划线。

### 使用轻量助手

- “开始开发用户权限功能”：生成候选 feature 分支名，确认分支名和基线后创建本地分支。
- “查看 Git 工作流状态”：只读检查当前分支、工作区、基线差异和 upstream。
- “检查当前 feature 的完成状态”：只读汇总阻断项、警告项和待人工确认事项。
- “同步 Git 工作流到 README”：仅更新本托管区块，其他 README 内容保持不变。

轻量助手不会自动执行 commit、stash、rebase、merge、push、tag、发布、分支删除或历史重写。
<!-- GIT_WORKFLOW_END -->
````

- [ ] **Step 4: 验证托管标记唯一且内容完整**

Run:

```powershell
$template = 'C:\Users\wangyikan\.agents\skills\git-workflow\templates\readme-git-workflow.md'
$startCount = (Select-String -LiteralPath $template -SimpleMatch '<!-- GIT_WORKFLOW_START -->').Count
$endCount = (Select-String -LiteralPath $template -SimpleMatch '<!-- GIT_WORKFLOW_END -->').Count
"start=$startCount end=$endCount"
rg -n --no-heading 'main|dev|feature/\*|release/\*|hotfix/\*|PR/MR|单元测试|集成测试|回归测试' $template
```

Expected:

- 第一行输出 `start=1 end=1`。
- `rg` 能找到五类分支、审查要求和三类测试要求。

- [ ] **Step 5: 验证模板不包含可直接执行的高风险 Git 命令**

Run:

```powershell
$template = 'C:\Users\wangyikan\.agents\skills\git-workflow\templates\readme-git-workflow.md'
rg -n --no-heading 'git (merge|push|rebase|reset|branch -[dD]|tag)' $template
```

Expected: 无输出，退出码为 1；模板只描述策略，不提供绕过 PR/MR 的执行命令。

---

### Task 2: 将 SKILL.md 重写为轻量助手

**Files:**
- Modify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`
- Reference: `C:/Users/wangyikan/.agents/skills/git-workflow/docs/superpowers/specs/2026-08-11-lightweight-git-workflow-assistant-design.md`
- Reference: `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`

- [ ] **Step 1: 保存只读基线证据**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
(Get-FileHash -LiteralPath $skill -Algorithm SHA256).Hash
rg -n --no-heading '^### [1-6]\.|发布上线|紧急修复|部分发布|git push|git merge --squash|git reset --hard' $skill
```

Expected: 输出当前文件哈希，并能找到旧版 dev、release、hotfix、cherry-pick、push 或历史重写流程。该结果用于证明后续确实移除了执行型工作流。

- [ ] **Step 2: 用 apply_patch 将 SKILL.md 替换为有效基础骨架**

新文件必须采用以下 frontmatter：

```yaml
---
name: git-workflow
description: 项目定制的轻量 Git 工作流助手。仅在用户明确要求写入或同步 README 工作流、创建 feature 分支、查看工作流状态、检查 feature 完成状态时激活。只允许更新 README 托管区块和经确认后创建本地 feature 分支；不执行 commit、stash、rebase、merge、push、tag、发布、分支删除或历史重写。
---
```

frontmatter 后先写入完整、可独立生效的基础骨架，不保留旧版发布、hotfix、cherry-pick、dev 重建和 README 内嵌模板：

```markdown
# 轻量 Git 工作流助手

## 职责

本 skill 只负责：

1. 将标准工作流模板写入或同步到项目根目录 `README.md` 的托管区块。
2. 根据新需求生成候选 feature 分支名，确认分支名和基线后创建本地分支。
3. 只读查看当前 Git 工作流状态。
4. 只读检查当前 feature 的开发完成状态。

## 绝对边界

本 skill 不执行 commit、stash、rebase、merge、push、tag、发布、PR/MR 创建、分支删除、分支重命名、force push、reset 或丢弃工作区修改。

除以下两种动作外，所有流程必须保持只读：

- 用户明确要求同步工作流且确认 diff 后，更新 README 托管区块。
- 用户明确要求创建 feature 且确认分支名和基线后，创建本地 feature 分支。

遇到异常时只停止、报告和建议，不自动清理或恢复。
```

继续写入下列“激活门禁”表：

```markdown
## 激活门禁

| 明确指令 | 允许动作 |
| --- | --- |
| “把 Git 工作流写入 README” | 预览并确认后写入托管区块 |
| “同步 Git 工作流文档” | 比较模板，预览并确认后更新托管区块 |
| “开始开发用户权限功能” | 生成候选分支并进入创建确认流程 |
| “创建用户权限 feature 分支” | 生成候选分支并进入创建确认流程 |
| “查看 Git 工作流状态” | 执行完全只读的状态检查 |
| “检查当前 feature 的完成状态” | 执行完全只读的完成检查 |

以下表达只做讨论或解释，不修改文件或 Git 状态：“分析工作流”“看看分支策略”“为什么这样设计”“给个方案”“准备开发”“准备上线”。

## 唯一规则源

- README 工作流的唯一模板是相对本文件的 `templates/readme-git-workflow.md`。
- 必须完整读取模板后再生成预览或更新项目 README。
- 现有 `README.md`、workflows、guides、references 和 scripts 不参与运行时判断。
- 不得从旧文件复制 merge、push、release、hotfix 或历史重写命令。
```

此时文件已经形成保守可用的轻量 skill：能正确激活并拒绝越界操作，但功能流程将在后续任务中逐章追加。

- [ ] **Step 3: 验证旧执行型章节已移除**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
rg -n --no-heading '^### [1-6]\.|集中开发测试|发布上线|紧急修复|部分发布|回滚已发布|README 工作流文档同步' $skill
```

Expected: 无输出，退出码为 1。

- [ ] **Step 4: 验证新入口和边界存在**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
rg -n --no-heading '^## (职责|绝对边界|激活门禁|唯一规则源)$' $skill
```

Expected: 精确找到 4 个基础二级标题。

---

### Task 3: 落实 README 托管区块同步流程

**Files:**
- Modify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`
- Reference: `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`

- [ ] **Step 1: 验证“唯一规则源”已经固定模板路径和旧文件边界**

确认 Task 2 已精确写入：

```markdown
- README 工作流的唯一模板是相对本文件的 `templates/readme-git-workflow.md`。
- 必须完整读取模板后再生成预览或更新 README。
- 现有 `README.md`、workflows、guides、references 和 scripts 不参与运行时判断。
- 不得从旧文件复制 merge、push、release、hotfix 或历史重写命令。
```

- [ ] **Step 2: 写入托管标记检查算法**

流程必须逐项规定：

```text
1. 定位目标 Git 仓库根目录和根目录 README.md。
2. 读取 README 原文；不存在时记录为“待创建”，不立即写入。
3. 统计 GIT_WORKFLOW_START 和 GIT_WORKFLOW_END。
4. 0/0：首次插入；先展示完整模板和插入位置。
5. 1/1：确认开始标记位于结束标记之前；只比较这一段。
6. 1/0、0/1、多个开始或多个结束：停止并展示标记行号。
7. 托管区块外存在“Git 工作流”标题：停止并提示可能重复。
8. 展示 diff；没有差异时报告“已是最新”，不写文件。
9. 有差异时再次获得用户明确确认。
10. 使用文件编辑工具只插入或替换托管范围。
11. 写入后重新统计标记，并确认区块外既有内容未变化。
```

- [ ] **Step 3: 写入 README 安全约束**

必须明确：

- 不使用模糊标题匹配直接替换章节。
- 不修复残缺或重复标记。
- 不在没有 diff 预览和用户确认时写入。
- 不执行格式化整个 README 的命令。
- README 不存在时必须展示将创建的完整文件并确认。

- [ ] **Step 4: 静态验证模板引用唯一**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
$templateRefs = (Select-String -LiteralPath $skill -SimpleMatch 'templates/readme-git-workflow.md').Count
"templateRefs=$templateRefs"
rg -n --no-heading 'workflows/|guides/|references/|scripts/' $skill
```

Expected:

- `templateRefs` 至少为 1。
- 第二条命令只允许命中“旧目录不参与运行时判断”的负面说明，不允许出现读取或执行旧文件的步骤。

---

### Task 4: 落实 feature 分支生成与确认流程

**Files:**
- Modify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`

- [ ] **Step 1: 写入候选名称生成规则**

规则必须完整包含：

```text
- 固定 feature/ 前缀。
- 中文需求转换为简短英文语义名称。
- 英文描述转为小写 kebab-case。
- 需求编号保留并转为小写，例如 PROJ-123 -> proj-123。
- 删除空格、下划线和非 Git ref 合法字符。
- 名称只是候选值，创建前允许用户编辑。
- 使用 git check-ref-format --branch 验证最终名称。
```

示例必须包含：

```text
开发用户权限功能 -> feature/user-permission
PROJ-123 登录超时处理 -> feature/proj-123-login-timeout
```

- [ ] **Step 2: 写入创建前检查命令**

使用可在 PowerShell 单独运行的命令，不使用 Bash 循环或 `/dev/null`：

```powershell
git rev-parse --show-toplevel
git status --porcelain=v2 --branch
git fetch origin main
git rev-parse --verify 'origin/main^{commit}'
git log -1 --format='%h %s' origin/main
git check-ref-format --branch $branchName
git show-ref --verify --quiet "refs/heads/$branchName"
git ls-remote --exit-code --heads origin "refs/heads/$branchName"
```

命令语义必须说明：

- `git status --porcelain=v2 --branch` 检测到工作区或暂存区变化时停止。
- fetch 只在用户明确要求创建 feature 后执行。
- 本地或远程同名分支存在时停止，不覆盖、不删除、不自动切换。
- `git ls-remote` 只读取远程，不创建或更新远程分支。
- `git ls-remote --exit-code` 返回 0 表示远程同名分支存在，返回 2 表示没有匹配分支；其他退出码按远程访问失败处理。
- 默认基线是 fetch 后的 `origin/main`。

- [ ] **Step 3: 写入进行中 Git 操作检查**

先运行：

```powershell
$mergeHead = git rev-parse --git-path MERGE_HEAD
$cherryPickHead = git rev-parse --git-path CHERRY_PICK_HEAD
$rebaseMerge = git rev-parse --git-path rebase-merge
$rebaseApply = git rev-parse --git-path rebase-apply
Test-Path -LiteralPath $mergeHead
Test-Path -LiteralPath $cherryPickHead
Test-Path -LiteralPath $rebaseMerge
Test-Path -LiteralPath $rebaseApply
```

任一结果为 `True` 时停止分支创建，并报告具体进行中的操作；不得自动 abort。

- [ ] **Step 4: 写入创建确认格式**

确认信息必须使用以下字段：

```text
需求：PROJ-123 登录超时处理
候选分支：feature/proj-123-login-timeout
基线：origin/main
基线提交：a1b2c3d fix(auth): 修复登录状态刷新
工作区：干净
进行中的 Git 操作：无
同名分支：本地无、远程无
```

用户可以修改候选分支名或基线。修改后必须重新执行 ref 校验、基线解析和同名检查；不能复用旧检查结果。

- [ ] **Step 5: 写入唯一允许的创建命令**

默认基线确认后执行：

```powershell
git switch --no-track -c $branchName origin/main
```

若用户修改基线，使用已经重新验证并展示 SHA 的 `$baseRef`：

```powershell
git switch --no-track -c $branchName $baseRef
```

成功后只报告当前分支、基线 SHA 和“尚未设置 upstream”；不执行 push 或 upstream 设置。

- [ ] **Step 6: 验证 skill 中只有允许的 Git 状态变更命令**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
rg -n --no-heading 'git (switch|checkout|commit|stash|rebase|merge|push|tag|reset|branch -[dDmM])' $skill
```

Expected:

- 允许出现两条 `git switch --no-track -c` 创建命令。
- `commit`、`stash`、`rebase`、`merge`、`push`、`tag`、`reset` 和分支删除只能出现在“禁止执行”的文字说明中，不能出现在执行步骤或命令代码块中。

---

### Task 5: 落实只读状态与完成检查

**Files:**
- Modify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`

- [ ] **Step 1: 写入状态检查命令集**

状态检查不得 fetch，使用以下只读命令：

```powershell
git rev-parse --show-toplevel
git branch --show-current
git rev-parse --short HEAD
git log -1 --format='%h %s' HEAD
git status --porcelain=v2 --branch
git show-ref --verify --quiet refs/remotes/origin/main
git rev-list --left-right --count origin/main...HEAD
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
```

`git rev-list --left-right --count origin/main...HEAD` 的第一个数字解释为当前分支落后 `origin/main` 的提交数，第二个数字解释为领先提交数。

如果缓存中没有 `origin/main` 或没有 upstream，显示“不可用/未设置”，不能把命令失败解释为仓库异常。

- [ ] **Step 2: 写入标准状态输出**

```text
Git 工作流状态

当前分支：feature/proj-123-login-timeout
HEAD：a1b2c3d fix(auth): 修复登录状态刷新
工作区：干净
基线：origin/main @ d4e5f6a
相对基线：领先 3，落后 1
Upstream：未设置
分支命名：通过
进行中的 Git 操作：无
远程引用：使用本地缓存，可能不是远程最新状态
```

detached HEAD、缺失 `origin/main`、脏工作区和进行中的 Git 操作都要改变对应字段，不能省略。

- [ ] **Step 3: 写入完成检查命令和分类**

完成检查不得 fetch，并在状态检查基础上增加：

```powershell
git log --format='%h %s' origin/main..HEAD
git diff --name-status origin/main...HEAD
git rev-list --count origin/main..HEAD
```

分类必须与设计一致：

- 阻断：脏工作区、detached HEAD、正在 merge/rebase/cherry-pick、基线不可计算、当前不是 `feature/*`。
- 警告：落后主干、没有新增提交、分支名不规范、未设置 upstream、feature 范围提交信息不规范。
- 未验证：需求完整性、测试结果、代码审查、推送和 PR/MR 权限。

最终结论只能是“存在阻断项”“无阻断项但存在警告”“本地 Git 检查无阻断项”；不得输出“可以发布”或“验证通过”。

- [ ] **Step 4: 验证只读章节没有状态变更命令**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
$content = Get-Content -LiteralPath $skill -Raw
$statusStart = $content.IndexOf('## 工作流状态检查')
$errorStart = $content.IndexOf('## 异常处理')
$readonlySections = $content.Substring($statusStart, $errorStart - $statusStart)
$readonlySections | Select-String -Pattern 'git\s+(fetch|switch|checkout|commit|stash|rebase|merge|push|tag|reset|branch\s+-[dDmM])' -AllMatches
```

Expected: 无匹配。

---

### Task 6: 完成异常处理、平台约束和静态自检

**Files:**
- Modify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`
- Verify: `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`

- [ ] **Step 1: 写入异常处理矩阵**

`## 异常处理` 必须覆盖并规定以下结果：

| 异常 | 结果 |
| --- | --- |
| 不在 Git 仓库 | 停止，要求用户切换到目标仓库 |
| 工作区或暂存区不干净 | 停止创建，只提示用户自行提交或 stash |
| detached HEAD | 状态中警告；创建 feature 时停止 |
| merge/rebase/cherry-pick 进行中 | 停止，不自动 abort |
| 本地同名分支 | 停止，建议切换或修改名称 |
| 远程同名分支 | 停止，提示可能已有协作者使用 |
| `origin/main` 不存在 | 展示可用 remote 和默认分支，请用户选择 |
| fetch 失败 | 保持当前分支不变，报告 Git 原始错误 |
| README 标记残缺或重复 | 展示标记行号，不自动修复 |
| 分支创建失败 | 报告原始错误，不 reset、不删除、不重试其他基线 |

- [ ] **Step 2: 写入 PowerShell 兼容要求**

必须明确：

- 默认按 Windows PowerShell 展示 shell 片段。
- 每条 Git 命令独立展示。
- 不使用 `/dev/null`、`for ...; do`、Bash 数组或 Bash 条件表达式。
- 不使用 `&&` 或 `||` 串联带状态修改的命令。
- 路径检查使用 `Test-Path -LiteralPath`。
- Git ref 中包含 `@{upstream}` 或 `^{commit}` 时使用单引号，避免 PowerShell 解析。

- [ ] **Step 3: 执行占位符与结构扫描**

Run:

```powershell
$root = 'C:\Users\wangyikan\.agents\skills\git-workflow'
rg -n --no-heading 'T[B]D|T[O]DO|待[定]|稍后实[现]|fill[ ]in|implement[ ]later' "$root\SKILL.md" "$root\templates\readme-git-workflow.md"
rg -n --no-heading '^## ' "$root\SKILL.md"
```

Expected:

- 占位符扫描无输出。
- 标题扫描包含且只包含计划规定的运行时章节；frontmatter 后只有一个一级标题。

- [ ] **Step 4: 执行旧流程回归扫描**

Run:

```powershell
$skill = 'C:\Users\wangyikan\.agents\skills\git-workflow\SKILL.md'
rg -n --no-heading '发布上线|集中开发测试|紧急修复（Hotfix）|部分发布（Cherry-pick）|回滚已发布|重建 dev|publish-with-tag|release\.sh' $skill
```

Expected: 无输出，退出码为 1。

- [ ] **Step 5: 执行文件范围检查**

Run:

```powershell
$root = 'C:\Users\wangyikan\.agents\skills\git-workflow'
Get-Item -LiteralPath "$root\SKILL.md", "$root\templates\readme-git-workflow.md" |
  Select-Object FullName, Length, LastWriteTime
Get-ChildItem -LiteralPath "$root\workflows", "$root\guides", "$root\references", "$root\scripts" -Recurse -File |
  Select-Object FullName, LastWriteTime
```

Expected:

- `SKILL.md` 和新模板存在。
- 旧目录文件仍存在；实施过程中没有删除它们。
- 结合实施前记录确认旧目录文件时间未被本次操作改写。

---

### Task 7: 在临时 Git 仓库中验证关键命令语义

**Files:**
- Temporary only: `C:/Users/wangyikan/Documents/Codex/2026-08-11/j/work/git-workflow-smoke/`

- [ ] **Step 1: 创建限定范围的临时远程和工作仓库**

Run:

```powershell
$smokeRoot = 'C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work\git-workflow-smoke'
$resolvedSmoke = [System.IO.Path]::GetFullPath($smokeRoot)
$allowedRoot = [System.IO.Path]::GetFullPath('C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work')
$allowedPrefix = $allowedRoot.TrimEnd('\') + '\'
if (-not $resolvedSmoke.StartsWith($allowedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
  throw "临时目录不在允许的 work 范围：$resolvedSmoke"
}
if (Test-Path -LiteralPath $resolvedSmoke) {
  throw "临时目录已存在，拒绝复用未知内容：$resolvedSmoke"
}
New-Item -ItemType Directory -Force -Path $resolvedSmoke
git init --bare "$resolvedSmoke\remote.git"
git init -b main "$resolvedSmoke\seed"
git -C "$resolvedSmoke\seed" config user.name 'Git Workflow Smoke Test'
git -C "$resolvedSmoke\seed" config user.email 'git-workflow-smoke@example.invalid'
git -C "$resolvedSmoke\seed" commit --allow-empty -m 'chore: initialize smoke repository'
git -C "$resolvedSmoke\seed" remote add origin "$resolvedSmoke\remote.git"
git -C "$resolvedSmoke\seed" push -u origin main
git -C "$resolvedSmoke\remote.git" symbolic-ref HEAD refs/heads/main
git clone "$resolvedSmoke\remote.git" "$resolvedSmoke\client"
git -C "$resolvedSmoke\client" switch main
```

Expected: bare remote、seed 和 client 创建成功，client 位于 `main`。

- [ ] **Step 2: 验证 feature 从 origin/main 创建且不误设 upstream**

Run:

```powershell
$client = 'C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work\git-workflow-smoke\client'
git -C $client fetch origin main
git -C $client switch --no-track -c feature/user-permission origin/main
git -C $client branch --show-current
git -C $client rev-parse HEAD
git -C $client rev-parse origin/main
git -C $client rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
```

Expected:

- 当前分支为 `feature/user-permission`。
- `HEAD` 与 `origin/main` SHA 相同。
- upstream 查询失败并提示未配置，而不是输出 `origin/main`。

- [ ] **Step 3: 验证领先/落后顺序**

Run:

```powershell
$client = 'C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work\git-workflow-smoke\client'
git -C $client config user.name 'Git Workflow Smoke Test'
git -C $client config user.email 'git-workflow-smoke@example.invalid'
git -C $client commit --allow-empty -m 'feat: add user permission smoke commit'
git -C $client rev-list --left-right --count origin/main...HEAD
```

Expected: 输出 `0 1`；skill 应解释为“落后 0，领先 1”。

- [ ] **Step 4: 验证同名分支检测**

Run:

```powershell
$client = 'C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work\git-workflow-smoke\client'
git -C $client show-ref --verify --quiet refs/heads/feature/user-permission
$LASTEXITCODE
```

Expected: 输出 `0`，代表本地同名分支存在；创建流程必须在执行 `git switch -c` 前停止。

- [ ] **Step 5: 清理临时测试目录**

先验证目标，再删除：

```powershell
$smokeRoot = 'C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work\git-workflow-smoke'
$resolvedSmoke = [System.IO.Path]::GetFullPath($smokeRoot)
$allowedRoot = [System.IO.Path]::GetFullPath('C:\Users\wangyikan\Documents\Codex\2026-08-11\j\work')
$allowedPrefix = $allowedRoot.TrimEnd('\') + '\'
if (-not $resolvedSmoke.StartsWith($allowedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
  throw "拒绝删除范围外目录：$resolvedSmoke"
}
Remove-Item -LiteralPath $resolvedSmoke -Recurse -Force
Test-Path -LiteralPath $resolvedSmoke
```

Expected: 输出 `False`。临时仓库不可恢复，但只包含本任务生成的测试数据。

---

### Task 8: 最终设计覆盖与交付检查

**Files:**
- Verify: `C:/Users/wangyikan/.agents/skills/git-workflow/SKILL.md`
- Verify: `C:/Users/wangyikan/.agents/skills/git-workflow/templates/readme-git-workflow.md`
- Reference: `C:/Users/wangyikan/.agents/skills/git-workflow/docs/superpowers/specs/2026-08-11-lightweight-git-workflow-assistant-design.md`

- [ ] **Step 1: 按设计逐项核对功能覆盖**

确认以下 11 项均可指向 `SKILL.md` 中的明确章节：

1. README 托管区块首次写入。
2. README 托管区块幂等同步。
3. 托管区块异常保护。
4. 自然语言到 feature 候选名称。
5. 默认 `origin/main` 及修改基线后的重新校验。
6. 创建前确认分支名、基线和状态。
7. `--no-track` 本地创建。
8. 完全只读的状态检查。
9. 阻断/警告/未验证三类完成检查。
10. Windows PowerShell 兼容。
11. 禁止远程、发布、合并、历史重写和删除操作。

Expected: 无缺项，不依赖旧版运行时文件。

- [ ] **Step 2: 最终读取 active 文件**

Run:

```powershell
$root = 'C:\Users\wangyikan\.agents\skills\git-workflow'
Get-Content -LiteralPath "$root\SKILL.md" -Raw
Get-Content -LiteralPath "$root\templates\readme-git-workflow.md" -Raw
```

Expected: 文档可完整读取、Markdown fence 配对、frontmatter 仅出现一次、无截断段落。

- [ ] **Step 3: 报告验证层级和未执行事项**

最终交付必须明确报告：

- 已修改：`SKILL.md`。
- 已新增：`templates/readme-git-workflow.md`。
- 已验证：静态结构、禁止命令扫描、模板标记、临时 Git 仓库中的 branch/upstream/ahead-behind 语义。
- 未执行：真实项目 README 同步、真实项目 feature 创建、push、merge、发布、删除、Git 提交。
- 旧文件：仍保留，但不再被 active `SKILL.md` 引用。
