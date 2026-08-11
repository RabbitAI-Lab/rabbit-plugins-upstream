---
name: git-workflow
description: Git 工作流管理 skill。仅在用户发出明确指令（如"创建feature分支"、"合并到dev"、"发布上线"）时激活，不响应日常讨论。所有远程推送、main/release 合并、分支删除、历史重写操作必须显式确认。遵循线性 Git 历史规范：rebase 替代 merge，squash 合并碎提交。
allowed-tools: Bash, Read, Edit, Glob, Grep
---

# Git 工作流 Skill

## 前置配置（环境要求）

在使用本 skill 的任何工作流之前，确保已配置：

```bash
# 让 git pull 默认执行 rebase，避免产生无意义的 merge commit
git config --global pull.rebase true
```

如未配置，skill 会自动检测并提示用户执行。

## 激活规则（门禁）

**本 skill 仅在用户发出明确的工作流指令时激活。日常对话、方案讨论、需求描述不构成激活条件。**

### 明确的激活指令

| 用户说 | 动作 |
|--------|------|
| "创建 feature 分支 xxx" | 创建 feature/xxx |
| "合并 feature/A feature/B 到 dev" | 重建 dev 并合并 |
| "发布 feature/A" | 创建 release，选择性合并 |
| "hotfix 登录崩溃" | 创建 hotfix/login-crash |
| "查看工作流状态" | 显示分支、更改、同步状态 |
| "同步工作流到 README" | 更新项目文档（需确认） |

### 不应激活的场景

- "我们讨论一下新功能的实现方案" — 讨论，不是指令
- "测试一下这个 API" — 开发测试，不是分支操作
- "准备上线了" — 需要明确说"发布 feature/X"
- "release 环境有问题" — 讨论，除非明确说"创建 hotfix 分支"

### 上下文提示（被动，不触发操作）

当 skill 已激活时，可根据上下文**被动提示**（不自动执行）：
- 提交信息含 `feat:` → 提示"可考虑合并到 dev 测试"
- 当前在 `feature/*` 分支 → 提示开发流程相关选项
- 当前在 `dev` 分支 → 提示测试流程相关选项
- 当前在 `release` 分支 → 提示发布流程相关选项
- 当前在 `main` 分支 → 提示"保护分支，禁止直接提交"

**这些提示不构成激活条件，仅在 skill 已通过明确指令激活后作为辅助信息。**

## 分支模型

核心哲学：**主干永远保持随时可发布状态，所有新需求都通过短生命周期的特性分支完成。用 Rebase 替代 Merge，用 Squash 合并碎提交，保持 Git 历史线性干净。**

```
main ────────────────────────────────────────────── (随时可发布，禁止直接提交)
  │
  ├── feature/A  ── 从 main 拉取，独立开发
  ├── feature/B  ── 从 main 拉取，独立开发
  ├── feature/C  ── 从 main 拉取，独立开发
  │
  ├── dev  ── 开发测试分支，合并需测试的 feature，定期清理重建
  │     │
  │     └── 合并 feature/A + feature/B → 集中测试
  │
  ├── release  ── 发布分支，从 main 创建，选择性合并 feature
  │     │
  │     └── staging 验证 → squash 合并回 main → 打 tag → 推送 main+tag → 删除
  │
  └── hotfix/*  ── 紧急修复，从 main 创建，修复后合并到 main 和 dev
```

### 分支职责

| 分支 | 拉取来源 | 职责 | 是否可直接提交 | 生命周期 |
|------|----------|------|----------------|----------|
| `main` | - | 生产基准，随时可发布 | 禁止（只接受 release 同步） | 常驻 |
| `dev` | `main` | 开发测试，集中验证 | 允许（修测试问题） | 常驻，定期清理重建 |
| `feature/*` | `main` | 功能开发，独立隔离 | 允许 | 短期，完成后删除 |
| `release` | `main` | 发布通道，选择性合并 feature | 允许（修发布问题） | 短期，发布后删除 |
| `hotfix/*` | `main` | 紧急修复 | 允许 | 短期，修复后删除 |

### 分支流向

```
开发阶段：  main → feature/* → dev（集中测试）
发布阶段：  main → release ← feature/*（选择性合并 squash）→ staging 验证 → squash 合并回 main → 打 tag → 推送 main+tag → 删除 release
紧急修复：  main → hotfix/xxx → squash 合并回 main + 同步 dev
加急修复：  main → hotfix/xxx → squash 合并回 main（跳过 dev，需额外确认）
```

### 代码审查

| 阶段 | 审查要求 |
|------|----------|
| 合并到 dev 前 | 必须经过代码审查（PR/MR） |
| 合并到 main 前 | 必须经过最终审查（PR/MR） |

使用 Pull Request / Merge Request 进行代码审查，禁止跳过。

### 测试要求

| 分支 | 测试类型 | 要求 |
|------|----------|------|
| feature/* | 单元测试 | 必须通过 |
| dev | 集成测试 | 必须通过 |
| release | 回归测试 | 必须通过 |

### 铁律

1. **永远不能把 dev 合并到 main**
2. **main 只接受 release 的同步（squash merge）**，hotfix 除外（hotfix 可直接合并到 main）
3. **禁止对公共分支（main、dev、release）执行 rebase**

## 提交规范（Conventional Commits）

所有提交信息**必须**遵循 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

### 常用 type

| type | 含义 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat(auth): 添加 JWT 登录` |
| `fix` | Bug 修复 | `fix(api): 修复分页偏移量` |
| `chore` | 构建/工具/依赖 | `chore(deps): 升级 axios` |
| `docs` | 文档 | `docs(readme): 更新部署说明` |
| `refactor` | 重构（不改功能） | `refactor(user): 抽取验证逻辑` |
| `test` | 测试 | `test(auth): 补充登录边界用例` |
| `style` | 格式（不影响逻辑） | `style: 运行 prettier` |
| `perf` | 性能优化 | `perf(query): 添加索引` |

### 规范要求

- `description` 用中文或英文均可，但同一项目保持一致
- `scope` 可选，建议填写受影响的模块名
- 不符合规范的提交 → 提示用户修正，不自动阻断

## 分支命名规范

| 类型 | 格式 | 示例 | 说明 |
|------|------|------|------|
| 功能分支 | `feature/<描述>` | `feature/user-auth` | 简单场景 |
| 功能分支 | `feature/<issue号>-<描述>` | `feature/PROJ-123-login` | 有 ticket 跟踪时 |
| 发布分支 | `release/YYYY-MM-DD` 或 `release/<版本号>` | `release/2026-08-06` 或 `release/v1.2.0` | 按日期或版本号 |
| 热修复 | `hotfix/<问题描述>` | `hotfix/login-crash` | 紧急修复 |

### 命名规则

- 使用 **kebab-case**（小写 + 连字符）
- **禁止**中文、空格、下划线
- 描述部分不超过 5 个词
- 注意：此处 `<描述>` 或 `<issue号>` 是分支标识，与 Conventional Commits 的 `type`（feat/fix/chore）无关

## 破坏性操作铁律

**只对破坏性操作要求确认。根据上下文智能推断用户意图，减少不必要的交互。**

以下操作**必须在执行前获得用户显式确认**：

| 操作 | 风险等级 | 确认时必须展示 |
|------|----------|---------------|
| 合并到 `main`（包括 release 同步） | 高 | 影响生产基准代码 |
| 推送到远程（任何分支） | 高 | 目标分支、是否触发 CI/CD |
| `git reset --hard`（任何变体） | 极高 | **不可逆**：永久丢弃工作区和暂存区更改 |
| `git push --force-with-lease` | 高 | **风险**：可能覆盖远程提交，仅限个人 feature 分支 |
| 删除分支（本地或远程） | 高 | **不可逆**：协作者和 CI 可能依赖该分支 |
| 重建 `dev` 或 `release` 分支 | 中 | 会丢失该分支上未同步的本地提交 |
| 编辑项目文档（README.md 等） | 中 | 展示 diff 预览 |

**确认时必须展示**：即将执行的命令、影响范围、不可逆风险说明。

## 保持 Git 线性（核心规范）

**目标**：Git 提交历史呈线性干净，无交叉线、无立交桥。

### 1. 拉代码：全局 rebase

```bash
# 前置配置（只需执行一次）
git config --global pull.rebase true

# 之后 git pull 默认等同于 git pull --rebase
git pull
```

### 2. 提交前：Rebase 主干

开发完成、准备合并前，先将本地分支基于最新主干变基：

```bash
# 1. 切换到主分支并拉取最新代码
git checkout main
git pull

# 2. 切换回自己的特性分支
git checkout feature/your-feature

# 3. 将本地提交"变基"到最新主干之上
git rebase main

# 4. 如果遇到冲突，解决冲突后执行：
git add .
git rebase --continue
```

### 3. 清理碎提交：交互式 Rebase

开发过程中产生了很多临时 Commit（如 `fix bug`, `wip`），合并前使用交互式变基清理：

```bash
git rebase -i HEAD~N
```

将不需要独立展示的 Commit 标记为 `squash` 或 `fixup`，压缩为一个干净的提交。

### 4. 推送：仅限个人 feature 分支

Rebase 后推送到远端特性分支：

```bash
# ⚠️ REQUIRES_CONFIRMATION: 仅限个人 feature 分支
git push --force-with-lease origin feature/xxx
```

**禁止**对 `main`、`dev`、`release` 等公共分支执行 force push 或 rebase。

### 5. 合并：Squash and Merge

PR/MR 合并时，**必须使用 Squash and Merge**，禁止普通 Create a merge commit。

> **平台设置建议**：在 GitHub / GitLab 的仓库设置中，仅勾选 Squash merging，关闭普通 merge commit 功能。

## 合并策略

| 场景 | 策略 | 命令 | 原因 |
|------|------|------|------|
| feature → dev | squash | `git merge --squash feature/X` | dev 是临时测试分支，保持干净历史 |
| feature → release | squash | `git merge --squash feature/X` | 发布历史清晰，一个 feature 一个提交 |
| release → main | squash | `git merge --squash release` | 线性历史，release 发布后删除 |
| feature rebase main | rebase | `git rebase origin/main` | 保持 feature 线性，减少冲突 |

**squash merge 注意事项**：
- squash merge 会创建一个**全新提交**在目标分支上，原 feature 分支的 commit 不变
- git **不会**标记 feature 分支为"已合并"（因为没有 merge commit），`git branch -d` 可能拒绝删除
- 删除已 squash 的 feature 分支需用 `git branch -D`，确认该分支的所有提交已包含在 squash 中

### feature 依赖处理

当 feature/B 依赖 feature/A 的代码时：
1. 先将 feature/A 合并到 dev
2. 在 feature/B 上 rebase dev：`git rebase dev`
3. 或 feature/B 直接从 feature/A 拉取：`git checkout -b feature/B feature/A`

## 工作流

### 1. 新功能开发

**激活指令**：用户明确说"创建 feature 分支 xxx"、"开始开发 xxx 功能"

```bash
git fetch --all --prune
git checkout -b feature/[issue号]-[功能名] origin/main
```

自动提示：
```markdown
检测到新功能开发指令，正在创建分支：
- 分支名：feature/PROJ-123-user-management
- 基础分支：main（确保基于稳定代码）

✅ 已创建：feature/PROJ-123-user-management
```

**提交规范**：
- 所有提交必须遵循 Conventional Commits 格式
- 不符合规范的提交会提示修正

**开发过程提醒**（自动，不确认）：
- feature 分支超过 N 天未同步 main → 建议 rebase（N 默认为 3，可根据团队节奏调整）
- 有未提交的更改 → 建议提交或 stash 后再切换分支
- 开发完成 → 提示：先 rebase main、清理碎提交，然后合并到 dev 进行测试

**开发完成检查清单**（合并前）：
1. 交互式 rebase 清理碎提交：`git rebase -i HEAD~N`
2. Rebase 最新 main：`git fetch origin && git rebase origin/main`
3. 推送到远端：`git push --force-with-lease origin feature/xxx`
4. 合并到 dev 测试

### 2. 集中开发测试

**激活指令**：用户明确说"合并 xxx 到 dev"、"测试 feature/A feature/B"

```bash
git fetch --all --prune
# ⚠️ REQUIRES_CONFIRMATION: 删除并重建 dev 分支
git checkout main
git log main..dev --oneline 2>/dev/null  # 检查未同步提交
```

确认提示（必须确认）：
```markdown
⚠️ 即将删除并重建 dev 分支

检查结果：
- dev 上未同步到 main 的提交：X 个（如有）
- 请确认是否有 dev-only 的调试代码或配置需要保留

操作步骤：
1. 从 main 重建 dev 分支
2. Squash merge：feature/A, feature/B

确认重建？(y/n)
```

```bash
git branch -d dev 2>/dev/null || git branch -D dev
git checkout -b dev main

# squash merge（冲突时进入冲突解决流程，见下方）
git merge --squash feature/A
# 有冲突 → 解决后 git add . && git commit -m "chore(dev): 合并 feature/A"
# 无冲突 → git commit -m "chore(dev): 合并 feature/A"
# 无变更（Already up to date）→ 跳过，说明该 feature 已在 main 中

git merge --squash feature/B
git commit -m "chore(dev): 合并 feature/B"
```

**squash merge 冲突处理**：
```markdown
squash merge 冲突：
- 冲突文件：xxx
- 处理步骤：
  1. 解决冲突文件中的冲突标记
  2. git add <已解决的文件>
  3. git commit -m "chore(dev): 合并 feature/X（解决冲突）"
  4. 如冲突过多无法解决：git merge --abort 放弃，报告给用户
```

**dev 分支管理规则**：
- dev 是常驻的开发测试分支，但定期清理重建以保持干净
- 测试发现的 bug 直接在对应 feature 分支上修复，修复后重新合并到 dev
- dev 分支不直接发布
- **永远不能把 dev 合并到 main**

### 3. 发布上线

**激活指令**：用户明确说"发布 feature/A feature/B"、"上线 xxx"

```bash
git fetch --all --prune
# ⚠️ REQUIRES_CONFIRMATION: 创建 release 分支
git checkout main
```

确认提示（必须确认）：
```markdown
⚠️ 检测到发布操作，即将创建 release 分支：

确认信息：
- 基础分支：main
- 本次发布功能（将 squash merge）：
  - feature/A（用户管理）
  - feature/B（权限模块）
- 未发布功能：
  - feature/C（消息通知）

确认创建 release 分支并合并？(y/n)
```

```bash
git checkout -b release main

# 同步检查：确保 feature 分支已基于最新 main，避免合并时冲突
git fetch origin
for feature in feature/A feature/B; do
  if ! git merge-base --is-ancestor origin/main "$feature" 2>/dev/null; then
    echo "⚠️ $feature 未包含最新 main，请先在该分支上 rebase origin/main"
  fi
done

git merge --squash feature/A && git commit -m "release: 合并 feature/A"
# 如果有冲突 → 解决后 git add . && git commit -m "release: 合并 feature/A（解决冲突）"
git merge --squash feature/B && git commit -m "release: 合并 feature/B"
```

**版本号规范**：遵循 [Semantic Versioning](https://semver.org/)（MAJOR.MINOR.PATCH）
- MAJOR：不兼容的 API 变更 | MINOR：向后兼容的功能新增 | PATCH：向后兼容的 Bug 修复
- 版本号由发布者根据本次变更内容决定

**发布完成后：推送到 staging → 验证 → squash 合并到 main → 打 tag → 推送 main+tag → 清理分支**（必须确认）：

```bash
# ⚠️ REQUIRES_CONFIRMATION: 推送 release（触发 staging CI/CD 验证）
git push origin release

# （等待 staging 环境验证通过）

# ⚠️ REQUIRES_CONFIRMATION: squash 合并到 main
git checkout main
git pull origin main                          # 拉取最新 main，提前暴露冲突
git merge --squash release
git commit -m "release: v1.x.x 包含 feature/A, feature/B"

# ⚠️ REQUIRES_CONFIRMATION: 在 main 上创建版本 tag 并推送
git tag -a v1.x.x -m "release: v1.x.x 包含 feature/A, feature/B"
git push origin main v1.x.x                  # 同时推送 main 和 tag，触发 production 部署

# ⚠️ REQUIRES_CONFIRMATION: 删除已发布分支（本地+远程）
git branch -D release && git push origin --delete release
git branch -D feature/A && git push origin --delete feature/A
git branch -D feature/B && git push origin --delete feature/B
```

确认提示（必须确认）：
```markdown
⚠️ 即将执行发布流程

确认信息：
- 包含功能：feature/A, feature/B
- 版本号：v1.x.x
- 操作序列：
  1. 推送 release → 远程（触发 staging CI/CD 验证）
  2. 等待 staging 验证通过
  3. 拉取最新 main，检查冲突
  4. Squash 合并 release → main
  5. 在 main 上打 tag v1.x.x
  6. 推送 main + tag（触发 production 部署）
  7. 删除 release 和已发布 feature 分支

确认发布？(y/n)
```

**CI/CD 集成提示**：
- 推送 release 后 → 提示确认 staging 环境 CI/CD 状态
- 推送 main + tag 后 → 提示确认 production 部署状态

### 4. 紧急修复（Hotfix）

**激活指令**：用户明确说"hotfix xxx"、"紧急修复 xxx"

**hotfix 分支从 main 创建，修复后直接合并到 main 和 dev，不走 release 通道。**

#### 标准流程

```bash
git fetch --all --prune
git checkout -b hotfix/[问题描述] main
# ... 修复代码 ...
```

修复完成后，合并到 main 和 dev（必须确认）：

```bash
# ⚠️ REQUIRES_CONFIRMATION: hotfix 合并到 main 和 dev

# 合并到 main，打 tag
git checkout main
git merge --squash hotfix/[问题描述]
git commit -m "hotfix: [问题描述]"
git tag -a v1.x.x -m "hotfix: [问题描述]"
git push origin main
git push origin v1.x.x

# 同步到 dev
git checkout dev
git merge --squash hotfix/[问题描述]
git commit -m "hotfix: 同步 [问题描述] 到 dev"

# 清理分支
git branch -D hotfix/[问题描述] && git push origin --delete hotfix/[问题描述]
```

确认提示（必须确认）：
```markdown
⚠️ 紧急修复：即将合并到 main 和 dev

确认信息：
- 修复内容：[描述]
- 影响范围：[文件/模块]
- 版本号：v1.x.x
- 操作序列：
  1. Squash 合并到 main + 打 tag
  2. 同步到 dev
  3. 删除 hotfix 分支

确认执行？(y/n)
```

#### 加急通道（跳过 dev，需额外确认）

**适用场景**：线上 P0/P1 事故，需立即上线，跳过 dev 测试直接合并到 main。

```bash
# ⚠️ REQUIRES_CONFIRMATION: 加急通道 — 跳过 dev
git fetch --all --prune
git checkout -b hotfix/[问题描述] main
# ... 修复代码 ...
```

确认提示（必须确认）：
```markdown
⚠️⚠️ 加急修复通道 — 跳过测试直接发布

风险警告：此修复未经 dev 验证，直接发布到生产。

确认信息：
- 修复内容：[描述]
- 影响范围：[文件/模块]

后续要求：发布后 24h 内补充完整测试。

确认使用加急通道？(y/n)
```

加急通道执行：
```bash
git checkout main
git merge --squash hotfix/[问题描述]
git commit -m "hotfix: [问题描述]"
git tag -a v1.x.x -m "hotfix: [问题描述]"
git push origin main
git push origin v1.x.x

# 清理分支（后续补充同步到 dev）
git branch -D hotfix/[问题描述] && git push origin --delete hotfix/[问题描述]
```

### 5. 部分发布（Cherry-pick）

**激活指令**：用户明确说"从 feature/X 挑选部分提交发布"

**适用场景**：feature 未全部完成，但部分提交需要先发布。

```bash
git fetch --all --prune
# 确保 release 分支存在
git checkout release 2>/dev/null || git checkout -b release main

# 查看 feature 分支的提交列表（对比 release 已有内容）
git log --oneline feature/X
git log --oneline release  # 检查哪些提交已包含在 release 中

# ⚠️ REQUIRES_CONFIRMATION: cherry-pick 特定提交到 release
git cherry-pick <commit-sha-1> <commit-sha-2>
```

确认提示（必须确认）：
```markdown
⚠️ 部分发布：从 feature/X 中挑选提交

即将 cherry-pick：
- abc1234 feat(auth): 添加登录接口
- def5678 fix(auth): 修复 token 过期问题

未包含：
- ghi9012 feat(auth): 添加 OAuth（未完成）

注意：cherry-pick 后 feature/X 仍保留所有提交，
后续完整发布时需确认不会重复合并。

确认 cherry-pick？(y/n)
```

**后续处理**：
- feature 分支继续开发未完成的部分
- 完整发布时，feature 分支 squash merge 到 release 前，用 `git log` 检查是否与已 cherry-pick 的提交重复
- git squash merge 时会自动处理重复变更，但 commit message 需手动调整避免混淆

### 6. 查看工作流状态

**激活指令**：用户明确说"查看工作流状态"、"当前分支状态"

输出内容：
```markdown
工作流状态

当前分支：feature/PROJ-123-user-management
基础分支：main（落后 main 2 个提交）
HEAD 状态：正常（如为 detached HEAD 会警告）

未提交更改：
- 修改：src/auth.ts, src/user.ts
- 新增：src/login.vue

活跃 feature 分支：
- feature/PROJ-123-user-management（当前，3 天未同步 main）
- feature/PROJ-456-payment（2 天未同步 main）

Stash：2 个未处理的 stash（建议检查 git stash list）

最近发布：v1.2.0（3 天前，包含 feature/A, feature/B）
```

## 异常处理

### 错误速查

| 错误 | 处理方式 |
|------|----------|
| **分支已存在** | 提供选项：切换 / 重命名后重建 / 使用其他名称。不自动删除。 |
| **有未提交更改** | 提供选项：`git stash` / 提交 / 查看后再决定。不自动丢弃。 |
| **推送被拒绝** | 先 pull --rebase 再 push；如是分支保护则走 PR；不用 force 推共享分支。 |
| **feature 与 main 差异过大** | rebase origin/main；冲突过多则重建分支 + cherry-pick。 |
| **合并冲突（rebase）** | 解决冲突文件 → `git add .` → `git rebase --continue`；放弃则 `git rebase --abort`。 |
| **合并冲突（squash merge）** | 解决冲突 → `git add .` → `git commit`；冲突过多则 `git merge --abort`。 |
| **需要撤销已合并功能** | 使用 revert（见下方），不用 reset --hard + push --force。 |
| **Stash 泄漏** | `git stash list` 检查并处理，避免长期积累丢失代码。 |
| **误操作丢失提交** | `git reflog` 查看所有操作历史，用 `git reset --hard <sha>` 恢复到任意历史状态。 |
| **feature 依赖其他 feature** | 见"合并策略 > feature 依赖处理"。 |

### 回滚已发布的合并（revert-based）

使用 `git revert`，不用 `git reset --hard` + `git push --force`。

```bash
# ⚠️ REQUIRES_CONFIRMATION: 回滚已发布功能
git fetch --all --prune
git log --oneline main  # 找到 release squash merge 的 commit
git checkout main
git revert <commit-sha>
git push origin main
```

确认提示：
```markdown
⚠️ 即将回滚已发布功能

操作：git revert <commit>
影响：撤销该提交引入的所有更改，保留历史记录
可恢复性：revert 本身可被 revert，安全可逆

确认回滚？(y/n)
```

**revert 后的后续操作**：
1. **重新发布**：从 revert 后的 main 重新拉 feature 分支，修复后走正常流程
2. **不再需要**：删除对应 feature 分支
3. **恢复回滚**：`git revert <revert-commit-sha>`（revert the revert）

### 分支回滚（仅限个人 feature 分支）

仅在个人 feature 分支、确认无其他人工作时：

```bash
# ⚠️ REQUIRES_CONFIRMATION: 历史重写，仅限个人 feature 分支
git reset --hard HEAD~N
git push --force-with-lease origin feature/xxx  # 比 --force 更安全
```

确认提示：
```markdown
⚠️ 历史重写：feature/xxx

操作：reset --hard HEAD~N + push --force-with-lease
风险：本地未提交更改将永久丢失
禁止：此操作禁止用于 main/dev/release 等共享分支

确认执行？(y/n)
```

## README 工作流文档同步

**触发条件**：仅在用户明确要求时执行（如"同步工作流到 README"）。

**不会自动执行**：避免意外修改项目文档。

**执行步骤**：
1. 用 Grep 检查 README.md 是否已包含 `Git 工作流` 或 `分支策略`
2. 如缺失 → 按下方「写入内容」生成精简版，用 Edit 追加（**必须确认，展示 diff 预览**）
3. 如已存在 → 展示现有内容，询问是否需要更新

**写入内容**（精简版，面向使用者的核心信息）：

1. **分支简介**：一句话说明 main / feature / dev / release / hotfix 各自用途，不展开职责表格细节
2. **关键约束**：铁律规则必须写入——禁止 dev→main、main 只接受 release 同步（hotfix 除外）、公共分支禁止 rebase
3. **操作流程**：
   - 常规：`创建 feature → 合并到 dev 测试 → 发布到 release → squash 合并回 main`
   - 紧急：`创建 hotfix → squash 合并到 main + 同步 dev`
4. **分支命名**：一句话说明 kebab-case 规则（禁止中文/空格/下划线，描述不超 5 个词）
5. **使用方式**：激活指令表（**剔除「同步工作流到 README」条目**，避免自引用）
6. **代码审查与测试**：合并到 dev / main 前必须 PR/MR；各阶段测试要求（feature 单测、dev 集测、release 回归）

**不写入 README 的内容**（属于 skill 内部规范，不暴露给使用者）：
- Conventional Commits 格式（由 `git-commit` skill 独立管理）
- 合并策略细节（squash 命令、squash 注意事项、feature 依赖处理）
- hotfix 加急通道、cherry-pick 部分发布
- 破坏性操作确认表、异常处理速查表
- 分支职责表格、分支流向图等细节图表

## 注意事项

1. **main 分支保护**：禁止直接提交代码，只接受 release 的 squash 同步
2. **dev 分支隔离**：永远不能把 dev 合并到 main，dev 仅用于开发测试
3. **feature 隔离**：每个 feature 独立开发，避免相互依赖
4. **release 临时性**：发布后删除；**dev 常驻但定期清理重建**，保持干净历史
5. **同步及时性**：发布完成后立即 squash 合并回 main 并清理分支
6. **squash 后删除分支**：squash merge 后 git 不标记 feature 为已合并，需用 `-D` 删除（确认提交已包含在 squash 中）
7. **保持线性**：提交前 rebase 主干，清理碎提交，用 squash merge，禁止普通 merge commit
8. **禁止对公共分支 rebase**：main、dev、release 已推送的提交严禁 rebase
9. **不搞大长腿分支**：feature 分支生命周期要短，存在时间越长 rebase 冲突成本越高
