# 轻量 Git 工作流助手设计

- 日期：2026-08-11
- 状态：已批准，待实施计划
- 目标 skill：`git-workflow`

## 背景

当前项目已经采用定制分支模型，但现有 skill 同时承担工作流说明、分支操作、合并、发布和异常恢复等职责，范围过大。skill 目录内的 `SKILL.md`、`README.md`、workflows、guides 和 scripts 还存在规则不一致，例如普通 merge 与 squash merge 并存。

本次改造把 skill 收敛为轻量助手，只负责让规则可见、安全创建 feature 分支，以及提供只读状态与完成度检查。远程协作和高风险 Git 操作继续由协作者、PR/MR 和仓库保护规则控制。

## 目标

1. 将项目 Git 工作流以受控区块写入 README，使协作者能直接了解规则。
2. 根据自然语言需求生成规范的 feature 分支名称。
3. 默认基于最新 `origin/main` 创建 feature 分支，并在创建前确认分支名和基线。
4. 提供只读工作流状态检查。
5. 提供 feature 开发完成检查，但不替用户执行交付操作。
6. 在异常场景下停止并解释，不自动清理、覆盖或恢复 Git 状态。

## 非目标

skill 不执行以下操作：

- commit、stash、rebase 或 merge；
- push、tag、发布或创建 PR/MR；
- 删除、重命名或强制更新分支；
- reset 或 checkout 丢弃修改；
- 修改 README 托管区块以外的内容；
- 代替 GitHub/GitLab 分支保护、代码审查或 CI 检查。

## 功能入口

### 写入或同步工作流

触发示例：

- “把 Git 工作流写入 README”
- “同步 Git 工作流文档”

行为：

1. 读取标准 README 工作流模板。
2. 检查 README 和托管标记状态。
3. 展示首次插入内容或更新差异。
4. 获得明确确认后写入。
5. 只修改托管区块，不修改其他内容。

托管标记固定为：

```markdown
<!-- GIT_WORKFLOW_START -->
## Git 工作流

本区块由 git-workflow skill 根据标准模板维护。
<!-- GIT_WORKFLOW_END -->
```

同步规则：

- 不存在托管区块：展示插入内容，确认后写入。
- 存在一个完整托管区块：比较模板，仅替换区块内部。
- 只有开始或结束标记：停止并报告标记损坏。
- 存在多个托管区块：停止并展示标记位置。
- 已有非托管的“Git 工作流”章节：提示可能重复，由用户决定是否迁移。
- README 不存在：展示完整新文件内容，确认后创建。
- 重复同步相同模板时不产生文件变化。

### 创建 feature 分支

触发示例：

- “开始开发用户权限功能”
- “创建用户权限 feature 分支”

默认流程：

```text
检查仓库和工作区状态
  -> fetch origin/main
  -> 根据需求生成候选分支名
  -> 验证 Git ref 和同名分支
  -> 展示需求、分支名、基线提交和状态
  -> 用户确认或修改分支名/基线
  -> 从确认后的基线创建本地 feature 分支
```

默认创建命令语义为：

```bash
git switch --no-track -c feature/<slug> origin/main
```

显式使用 `--no-track`，避免把新 feature 分支的 upstream 错误设置为 `origin/main`。skill 不自动 push 或设置远程 upstream。

分支命名规则：

- 固定使用 `feature/` 前缀。
- 描述使用小写 kebab-case。
- 中文需求转换为简短英文语义名称。
- 有需求编号时保留编号并转为小写。
- 自动生成的名称只作为建议，确认时允许编辑。
- 最终名称必须通过 `git check-ref-format --branch` 检查。

示例：

```text
开发用户权限功能
  -> feature/user-permission

PROJ-123 登录超时处理
  -> feature/proj-123-login-timeout
```

创建确认应至少展示：

```text
需求：PROJ-123 登录超时处理
分支：feature/proj-123-login-timeout
基线：origin/main
基线提交：a1b2c3d fix(auth): 修复登录状态刷新
工作区：干净
同名分支：本地无、远程无
```

### 查看工作流状态

触发示例：

- “查看 Git 工作流状态”
- “检查当前分支状态”

状态检查完全只读，不自动 fetch。输出必须注明远程引用来自本地缓存，可能不是远程最新状态。

输出内容：

- 当前分支或 detached HEAD 状态；
- 工作区和暂存区是否干净；
- 当前 HEAD 和 `origin/main` 的短提交信息；
- 相对 `origin/main` 领先和落后的提交数；
- upstream 配置；
- 分支名称规范检查；
- 正在进行的 merge、rebase 或 cherry-pick；
- 本地及缓存远程引用中的同名分支。

### 开发完成检查

触发示例：

- “检查这个 feature 是否可以交付”
- “检查当前 feature 的完成状态”

开发完成检查与状态检查一样保持只读，不自动 fetch；涉及 `origin/main` 的结论必须注明使用的是本地缓存远程引用。

检查结果分为三类：

#### 阻断项

- 工作区或暂存区不干净；
- 当前处于 detached HEAD；
- 正在进行 merge、rebase 或 cherry-pick；
- 无法找到或计算基线；
- 当前不是 feature 分支。

#### 警告项

- 当前 feature 落后 `origin/main`；
- feature 相对基线没有新增提交；
- 分支名称不符合规范；
- 没有设置 upstream；
- feature 范围内的提交信息不符合项目规范。

#### 待人工确认

- 需求是否完整实现；
- 测试是否通过；
- 是否完成代码审查；
- 是否允许推送或创建 PR/MR。

skill 无法验证的事项必须显示为“未验证”，不能直接宣称 feature 已经可以发布。

## 文件结构与规则来源

目标结构：

```text
git-workflow/
├── SKILL.md
└── templates/
    └── readme-git-workflow.md
```

- `SKILL.md` 保存激活规则、安全边界、检查流程和 feature 创建流程。
- `templates/readme-git-workflow.md` 保存写入项目 README 的标准内容，是 README 工作流文本的唯一模板来源。
- 现有 README、workflows、guides、references 和 scripts 不再作为运行时工作流规则来源。
- 是否删除旧文件不属于本次默认范围；实施时先解除引用，后续如需删除必须单独确认。

README 模板必须包含以下协作信息：

1. `main`、`dev`、`feature/*`、`release/*` 和 `hotfix/*` 的职责。
2. 常规开发流向：`main -> feature/* -> dev`，发布时从 `main` 创建 `release/*` 并选择性纳入 feature，验证后同步到 `main`。
3. 紧急修复流向：`main -> hotfix/* -> main`，随后同步修复到 `dev`。
4. 关键约束：禁止 `dev -> main`；`main` 只接受 release 同步，hotfix 除外；公共分支禁止 rebase 和 force push。
5. feature、release 和 hotfix 的分支命名规范。
6. feature 单元测试、dev 集成测试、release 回归测试，以及进入 dev/main 前的 PR/MR 审查要求。
7. 使用轻量助手创建 feature、查看状态和执行开发完成检查的触发示例。

模板不包含本地 merge、push、tag、删分支或发布脚本，避免 README 引导协作者绕过 PR/MR 和仓库保护规则。

## 安全与错误处理

所有异常都遵循“停止、报告、建议”的原则，不自动修复：

- 不在 Git 仓库中：停止并要求用户切换到目标仓库。
- 工作区不干净：停止创建分支，提示用户自行提交或 stash。
- 本地同名分支存在：提示切换或更换名称，不删除或覆盖。
- 缓存远程同名分支存在：提示可能已有协作者使用，停止创建。
- `origin/main` 不存在：展示可用远程和默认分支，请用户选择基线。
- fetch 失败：保持当前分支不变并报告原始错误。
- 分支名称非法：展示校验错误并要求修改。
- README 标记损坏或重复：展示标记位置，不猜测替换范围。
- 分支创建失败：报告 Git 原始错误，不尝试 reset 或清理。

## 平台要求

- 工作流必须能在 Windows PowerShell 环境执行。
- 不依赖 `/dev/null`、Bash `for ...; do` 或仅限 Bash 的条件表达式。
- Git 检查命令优先使用跨平台参数。
- 文档中的命令按单条 Git 命令展示，避免依赖 shell 链式语法。

## 验收标准

1. README 首次写入和重复同步均保持幂等。
2. README 在插入或替换范围之外的既有内容保持不变。
3. 中文、英文和带需求编号的需求能够生成合法候选分支名。
4. 创建前能够修改候选分支名和基线。
5. 工作区不干净、分支重名或基线缺失时不会创建分支。
6. 正常创建基于 fetch 后的最新 `origin/main`。
7. 新分支不会把 upstream 设置为 `origin/main`。
8. 状态中的领先和落后数量与 Git 实际结果一致。
9. 状态与完成检查不执行任何远程或历史修改操作。
10. 所有被禁止的 Git 操作都只能作为人工建议出现，不能由本 skill 执行。
11. Windows PowerShell 环境可以按文档完成所有受支持流程。

## 实施边界

本设计批准后，下一阶段先制定实施计划，再修改 `SKILL.md` 和新增 README 模板。旧文件的删除、Git 提交、远程推送和项目 README 实际同步均不在默认实施范围内，需要用户分别明确授权。
