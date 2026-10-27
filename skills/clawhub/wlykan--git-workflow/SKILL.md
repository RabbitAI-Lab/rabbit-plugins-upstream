---
name: git-workflow
description: 项目定制的轻量 Git 工作流助手。仅在用户明确要求写入或同步 README 工作流、创建 feature 分支、查看工作流状态、检查 feature 完成状态时激活。只允许更新 README 托管区块和经确认后创建本地 feature 分支；不执行 commit、stash、rebase、merge、push、tag、发布、分支删除或历史重写。
---

# 轻量 Git 工作流助手

## 职责

本 skill 只负责：

1. 将标准工作流模板写入或同步到目标仓库根目录 `README.md` 的托管区块。
2. 根据新需求生成候选 feature 分支名，确认分支名和基线后创建本地分支。
3. 只读查看当前 Git 工作流状态。
4. 只读检查当前 feature 的开发完成状态。

## 绝对边界

本 skill 不执行 commit、stash、rebase、merge、push、tag、发布、PR/MR 创建、分支删除、分支重命名、force push、reset 或丢弃工作区修改。

除以下两种动作外，所有流程必须保持只读：

- 用户明确要求同步工作流，查看 diff 并再次确认后，更新 README 托管区块。
- 用户明确要求创建 feature，确认分支名和基线后，创建本地 feature 分支。

遇到异常时只停止、报告和建议，不自动清理、覆盖或恢复 Git 状态。

## 激活门禁

只有明确的工作流操作指令才能激活本 skill。

| 明确指令 | 允许动作 |
| --- | --- |
| “把 Git 工作流写入 README” | 预览并确认后写入托管区块 |
| “同步 Git 工作流文档” | 比较模板，预览并确认后更新托管区块 |
| “开始开发用户权限功能” | 生成候选分支并进入创建确认流程 |
| “创建用户权限 feature 分支” | 生成候选分支并进入创建确认流程 |
| “查看 Git 工作流状态” | 执行完全只读的状态检查 |
| “检查当前 feature 的完成状态” | 执行完全只读的完成检查 |

以下表达只做讨论或解释，不修改文件或 Git 状态：

- “分析工作流”
- “看看分支策略”
- “为什么这样设计”
- “给个方案”
- “准备开发”
- “准备上线”

当用户要求执行超出本 skill 边界的 Git 操作时，说明本 skill 是轻量助手，不代替其他 Git 操作流程。

## 唯一规则源

- README 工作流的唯一模板是相对本文件的 `templates/readme-git-workflow.md`。
- 使用模板前必须完整读取该文件。
- skill 目录中既有的 `README.md`、`workflows/`、`guides/`、`references/` 和 `scripts/` 不参与运行时判断。
- 不得从旧文件复制 merge、push、release、hotfix、分支删除或历史重写命令。
- 不在 `SKILL.md` 内维护第二份 README 工作流正文。

## README 同步流程

### 前置条件

只有在用户明确要求“写入”或“同步”Git 工作流时才能进入本流程。读取、比较和展示 diff 不等于获得最终写入确认。

目标文件固定为当前目标 Git 仓库根目录的 `README.md`，托管边界固定为：

```markdown
<!-- GIT_WORKFLOW_START -->
<!-- 内容来自 templates/readme-git-workflow.md -->
<!-- GIT_WORKFLOW_END -->
```

模板文件本身包含完整的开始和结束标记。写入 README 时使用完整模板，不额外嵌套第二层标记。

### 检查步骤

1. 用 `git rev-parse --show-toplevel` 定位目标仓库根目录；失败时停止。
2. 完整读取 `templates/readme-git-workflow.md`。
3. 读取仓库根目录 `README.md`；文件不存在时记录为“待创建”，不立即写入。
4. 分别统计 `GIT_WORKFLOW_START` 和 `GIT_WORKFLOW_END` 标记数量。
5. 检查 README 托管区块之外是否已经存在非托管的“Git 工作流”标题。

按以下情况处理：

| 标记状态 | 处理方式 |
| --- | --- |
| 开始 0、结束 0，且无同名非托管章节 | 计划在 README 末尾追加完整模板 |
| 开始 1、结束 1，且顺序正确 | 只比较并替换完整托管区块 |
| 开始 1、结束 0，或开始 0、结束 1 | 停止，展示残缺标记行号 |
| 任一标记超过 1 个 | 停止，展示所有标记行号 |
| 开始标记位于结束标记之后 | 停止，报告标记顺序错误 |
| 托管区块外已有“Git 工作流”标题 | 停止，提示可能产生重复章节 |

### 预览与确认

- README 不存在时，展示将创建的完整文件内容。
- 首次追加时，展示插入位置和完整模板；默认在既有 README 末尾保留一个空行后追加。
- 更新既有托管区块时，只展示该区块的差异。
- 模板与托管区块一致时，报告“Git 工作流已是最新”，不写文件。
- 存在变化时，必须再次获得用户明确确认后才能写入。

### 写入约束

- 使用文件编辑工具只创建 README、追加完整模板或替换完整托管区块。
- 不使用模糊标题匹配直接替换章节。
- 不自动修复残缺、重复或乱序的标记。
- 不格式化整个 README。
- 不修改托管区块之外的既有内容。
- 写入后重新读取 README，确认开始和结束标记各 1 个、顺序正确，并确认插入或替换范围之外的既有内容保持不变。

## Feature 分支创建流程

### 激活和默认基线

只有用户明确要求开始某项新需求或创建 feature 分支时才能执行本流程。

- 默认候选基线：最新的 `origin/main`。
- 用户在最终确认时可以修改基线。
- 用户修改分支名或基线后，必须重新执行相关校验，不能复用旧结果。

### 候选分支名

生成规则：

- 固定使用 `feature/` 前缀。
- 中文需求转换为简短、明确的英文语义名称。
- 英文描述转换为小写 kebab-case。
- 需求编号保留并转换为小写，例如 `PROJ-123` 转为 `proj-123`。
- 不使用中文、空格、下划线或其他非法 Git ref 字符。
- 候选名称只是建议，创建前必须允许用户编辑。

示例：

```text
开发用户权限功能
-> feature/user-permission

PROJ-123 登录超时处理
-> feature/proj-123-login-timeout
```

最终名称必须通过以下检查，其中 `$branchName` 表示已经替换为实际候选值的 PowerShell 变量：

```powershell
git check-ref-format --branch $branchName
```

### 创建前检查

依次执行并解释结果：

```powershell
git rev-parse --show-toplevel
git status --porcelain=v2 --branch
git status --porcelain
```

- 不在 Git 仓库中时停止。
- `git status --porcelain` 有任何输出时，说明工作区、暂存区或未跟踪文件不干净，停止创建。
- 不自动 commit 或 stash。

检查是否存在进行中的 Git 操作：

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

任一路径存在时停止并报告具体操作，不自动 abort。

当基线保持为默认值时，获取并验证最新 `origin/main`：

```powershell
git fetch origin main
git rev-parse --verify 'origin/main^{commit}'
git log -1 --format='%h %s' origin/main
```

- fetch 只在用户已经明确要求创建 feature 后执行。
- `origin`、`main` 或访问权限不存在时停止并报告原始错误。
- 不使用本地 `main` 代替未验证的 `origin/main`。

如果用户改为其他远程基线，先 fetch 对应 remote 和 branch，再验证对应远程 ref；如果改为本地基线，只验证该 ref 能解析为 commit。所有基线都必须展示实际 SHA 和最近一条提交信息。

检查同名分支：

```powershell
git show-ref --verify --quiet "refs/heads/$branchName"
git ls-remote --exit-code --heads origin "refs/heads/$branchName"
```

- 本地检查退出码为 0：本地同名分支存在，停止创建。
- 远程检查退出码为 0：远程同名分支存在，停止创建。
- 远程检查退出码为 2：没有匹配的远程分支，可以继续。
- 远程检查为其他退出码：按远程访问失败处理，停止创建。
- 不自动切换、删除、覆盖或重命名同名分支。

### 创建确认

执行创建前必须展示：

```text
即将创建 feature 分支

需求：PROJ-123 登录超时处理
候选分支：feature/proj-123-login-timeout
基线：origin/main
基线提交：a1b2c3d fix(auth): 修复登录状态刷新
工作区：干净
进行中的 Git 操作：无
同名分支：本地无、远程无
```

等待用户确认，或者接受用户对候选分支名和基线的修改。修改后返回校验阶段。

### 创建分支

执行前把变量替换为已验证的实际值，不执行包含未解析占位符的命令。

默认基线：

```powershell
git switch --no-track -c $branchName origin/main
```

用户修改后的基线：

```powershell
git switch --no-track -c $branchName $baseRef
```

创建成功后只报告：

- 当前分支名；
- 基线 ref 和 SHA；
- 新分支尚未设置 upstream；
- 后续 push、commit、merge 或 PR/MR 不属于本 skill 的执行范围。

## 工作流状态检查

本流程完全只读，不自动 fetch。涉及远程分支的结论使用本地缓存 remote-tracking ref，并明确提示可能不是远程最新状态。

### 检查命令

```powershell
git rev-parse --show-toplevel
git branch --show-current
git rev-parse --short HEAD
git log -1 --format='%h %s' HEAD
git status --porcelain=v2 --branch
git status --porcelain
git show-ref --verify --quiet refs/remotes/origin/main
git rev-list --left-right --count origin/main...HEAD
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
```

解释规则：

- `git branch --show-current` 无输出时表示 detached HEAD。
- `git status --porcelain` 无输出时表示工作区干净。
- 缓存中没有 `origin/main` 时，基线和领先/落后显示为“不可用”，不自动 fetch。
- `git rev-list --left-right --count origin/main...HEAD` 的第一个数字是当前分支落后 `origin/main` 的提交数，第二个数字是领先提交数。
- upstream 查询失败时显示“未设置”，不把它误报为仓库异常。
- 使用 Feature 创建流程中的路径检查方法识别 merge、rebase 和 cherry-pick。
- 当前分支是 feature 时，检查名称是否符合 `feature/<kebab-case-description>`，并检查缓存的 `refs/remotes/origin/<当前分支>` 是否存在。

### 输出格式

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
同名缓存远程分支：无
远程引用：使用本地缓存，可能不是远程最新状态
```

字段不可用或存在异常时保留该字段并说明原因，不静默省略。

## Feature 开发完成检查

本流程完全只读，不自动 fetch。涉及 `origin/main` 的结论必须注明使用本地缓存 remote-tracking ref。

先执行“工作流状态检查”，然后执行：

```powershell
git log --format='%h %s' origin/main..HEAD
git diff --name-status origin/main...HEAD
git rev-list --count origin/main..HEAD
```

### 阻断项

以下任一情况存在时，结论为“存在阻断项”：

- 工作区、暂存区或未跟踪文件不干净；
- 当前处于 detached HEAD；
- 正在进行 merge、rebase 或 cherry-pick；
- 缓存中没有 `origin/main`，或者无法计算共同基线；
- 当前分支不符合 `feature/*`。

### 警告项

- 当前 feature 落后缓存的 `origin/main`；
- feature 相对基线没有新增提交；
- 分支名称不符合规范；
- 没有设置 upstream；
- 仓库存在明确的提交规范，但 feature 范围内的提交信息不符合该规范。

提交规范处理规则：优先读取仓库已有的 commitlint、CONTRIBUTING 或明确文档；仓库没有明确规范时只列出提交信息，不自行发明规则或判为不合规。

### 未验证项

以下事项必须标记为“未验证”，不能根据本地 Git 状态推断完成：

- 需求是否完整实现；
- 测试是否通过；
- 是否完成代码审查；
- 是否允许推送；
- 是否允许创建或合并 PR/MR。

最终结论只能使用：

- “存在阻断项”；
- “无阻断项，但存在警告”；
- “本地 Git 检查无阻断项”。

不得输出“可以发布”“验证通过”或其他超出证据范围的结论。

## 异常处理

| 异常 | 处理方式 |
| --- | --- |
| 不在 Git 仓库 | 停止，要求用户切换到目标仓库 |
| 工作区、暂存区或未跟踪文件不干净 | 停止创建，只提示用户自行 commit 或 stash |
| detached HEAD | 状态中警告；创建 feature 时停止 |
| merge、rebase 或 cherry-pick 进行中 | 停止，不自动 abort |
| 本地同名分支存在 | 停止，建议切换或修改候选名称 |
| 远程同名分支存在 | 停止，提示可能已有协作者使用 |
| `origin/main` 不存在 | 展示可用 remote 和默认分支，请用户选择基线 |
| fetch 失败 | 保持当前分支不变，报告 Git 原始错误 |
| README 标记残缺、重复或乱序 | 展示标记行号，不自动修复 |
| README 存在同名非托管章节 | 停止，提示用户决定是否迁移 |
| 分支创建失败 | 报告 Git 原始错误，不 reset、不删除、不尝试其他基线 |

任何建议都必须与已经执行的动作分开表述，不能把建议伪装成已完成结果。

## Windows PowerShell 兼容要求

- 默认按 Windows PowerShell 展示 shell 片段。
- 每条 Git 命令独立展示和执行。
- 不使用 `/dev/null`、Bash `for ...; do`、Bash 数组或 Bash 条件表达式。
- 不使用 `&&` 或 `||` 串联带状态修改的命令。
- 路径存在性检查使用 `Test-Path -LiteralPath`。
- Git ref 中包含 `@{upstream}` 或 `^{commit}` 时使用单引号，避免 PowerShell 解析。
- 文件编辑使用精确路径和托管边界，不运行全文件格式化命令。
