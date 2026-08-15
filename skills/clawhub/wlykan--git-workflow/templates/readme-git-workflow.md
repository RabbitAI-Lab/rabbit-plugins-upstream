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
