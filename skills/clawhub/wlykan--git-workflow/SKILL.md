---
name: git-workflow
description: Git 工作流管理 skill。仅在用户发出明确指令（如"创建feature分支"、"合并到test"、"发布上线"）时激活，不响应日常讨论。所有远程推送、main/release 合并、分支删除、历史重写操作必须显式确认。
allowed-tools: Bash, Read, Edit, Glob, Grep
---

# Git工作流 Skill

## 激活规则（门禁）

**本 skill 仅在用户发出明确的工作流指令时激活。日常对话、方案讨论、需求描述不构成激活条件。**

### 明确的激活指令

| 用户说 | 动作 |
|--------|------|
| "创建 feature 分支 xxx" | 创建 feature/xxx |
| "合并 feature/A feature/B 到 test" | 重建 test 并合并 |
| "发布 feature/A" | 创建 release，选择性合并 |
| "hotfix 登录崩溃" | 创建 feature/hotfix-xxx |
| "查看工作流状态" | 显示分支、更改、同步状态 |
| "同步工作流到 README" | 更新项目文档（需确认） |

### 不应激活的场景

- "我们讨论一下新功能的实现方案" — 讨论，不是指令
- "测试一下这个 API" — 开发测试，不是分支操作
- "准备上线了" — 需要明确说"发布 feature/X"
- "release 环境有问题" — 讨论，除非明确说"创建 hotfix 分支"

### 上下文提示（被动，不触发操作）

当 skill 已激活时，可根据上下文**被动提示**（不自动执行）：
- 提交信息含 `feat:` → 提示"可考虑合并到 test 测试"
- 当前在 `feature/*` 分支 → 提示开发流程相关选项
- 当前在 `test` 分支 → 提示测试流程相关选项
- 当前在 `release` 分支 → 提示发布流程相关选项
- 当前在 `main` 分支 → 提示"保护分支，禁止直接提交"

**这些提示不构成激活条件，仅在 skill 已通过明确指令激活后作为辅助信息。**

## 分支模型

```
main ────────────────────────────────────────────── (随时可发布，禁止直接提交)
  │
  ├── feature/A  ── 从 main 拉取，独立开发
  ├── feature/B  ── 从 main 拉取，独立开发
  ├── feature/C  ── 从 main 拉取，独立开发
  │
  ├── test  ── 临时测试分支，合并需测试的 feature，定期清理重建
  │     │
  │     └── 合并 feature/A + feature/B → 集中测试
  │
  └── release  ── 发布分支，只合并测试通过且本次要发布的 feature
        │
        └── 发布完成 → 打 tag → 同步回 main
```

### 分支职责

| 分支 | 拉取来源 | 职责 | 是否可直接提交 |
|------|----------|------|----------------|
| `main` | - | 生产基准，随时可发布 | 禁止（只接受 release 同步） |
| `feature/*` | `main` | 功能开发，独立隔离 | 允许 |
| `test` | `main` | 临时测试，定期清理重建 | 允许（修测试问题） |
| `release` | `main` | 发布通道，选择性合并 feature | 允许（修发布问题） |

### 分支流向

```
开发阶段：  main → feature/* → test（集中测试）
发布阶段：  main → release ← feature/*（选择性合并）→ 打 tag → 同步回 main
紧急修复：  main → feature/hotfix-xxx → test → release → 同步回 main
加急修复：  main → feature/hotfix-xxx → release（跳过 test，需额外确认）→ 同步回 main
```

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

feature 分支命名格式：

| 格式 | 示例 | 说明 |
|------|------|------|
| `feature/<描述>` | `feature/user-auth` | 简单场景 |
| `feature/<ticket>-<描述>` | `feature/PROJ-123-login` | 有 ticket 跟踪时 |
| `feature/hotfix-<描述>` | `feature/hotfix-login-crash` | 紧急修复 |

### 命名规则

- 使用 **kebab-case**（小写 + 连字符）
- **禁止**中文、空格、下划线（hotfix 前缀除外）
- 描述部分不超过 5 个词
- 注意：此处 `<描述>` 或 `<ticket>` 是分支标识，与 Conventional Commits 的 `type`（feat/fix/chore）无关

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
| 重建 `test` 或 `release` 分支 | 中 | 会丢失该分支上未同步的本地提交 |
| 编辑项目文档（README.md 等） | 中 | 展示 diff 预览 |

**确认时必须展示**：即将执行的命令、影响范围、不可逆风险说明。

## 合并策略

| 场景 | 推荐策略 | 命令 | 原因 |
|------|----------|------|------|
| feature → test | `--squash` | `git merge --squash feature/X` | test 是临时分支，保持干净历史 |
| feature → release | `--squash` | `git merge --squash feature/X` | 发布历史清晰，一个 feature 一个提交 |
| release → main | `merge`（普通） | `git merge release` | 保留完整的合并记录 |
| feature rebase main | `rebase` | `git rebase origin/main` | 保持 feature 线性，减少冲突 |

**squash merge 注意事项**：
- squash merge 会创建一个**全新提交**在目标分支上，原 feature 分支的 commit 不变
- git **不会**标记 feature 分支为"已合并"（因为没有 merge commit），`git branch -d` 可能拒绝删除
- 删除已 squash 的 feature 分支需用 `git branch -D`，确认该分支的所有提交已包含在 squash 中

### feature 依赖处理

当 feature/B 依赖 feature/A 的代码时：
1. 先将 feature/A 合并到 test
2. 在 feature/B 上 rebase test：`git rebase test`
3. 或 feature/B 直接从 feature/A 拉取：`git checkout -b feature/B feature/A`

## 工作流

### 1. 新功能开发

**激活指令**：用户明确说"创建 feature 分支 xxx"、"开始开发 xxx 功能"

```bash
git fetch --all --prune
git checkout -b feature/[ticket]-[功能名] origin/main
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
- 开发完成 → 提示可以合并到 test 进行测试

### 2. 集中测试

**激活指令**：用户明确说"合并 xxx 到 test"、"测试 feature/A feature/B"

```bash
git fetch --all --prune
# ⚠️ REQUIRES_CONFIRMATION: 删除并重建 test 分支
git checkout main
git log main..test --oneline 2>/dev/null  # 检查未同步提交
```

确认提示（必须确认）：
```markdown
⚠️ 即将删除并重建 test 分支

检查结果：
- test 上未同步到 main 的提交：X 个（如有）
- 请确认是否有 test-only 的调试代码或配置需要保留

操作步骤：
1. 从 main 重建 test 分支
2. Squash merge：feature/A, feature/B

确认重建？(y/n)
```

```bash
git branch -d test 2>/dev/null || git branch -D test
git checkout -b test main

# squash merge（冲突时进入冲突解决流程，见下方）
git merge --squash feature/A
# 有冲突 → 解决后 git add . && git commit -m "test: 合并 feature/A"
# 无冲突 → git commit -m "test: 合并 feature/A"
# 无变更（Already up to date）→ 跳过，说明该 feature 已在 main 中

git merge --squash feature/B
git commit -m "test: 合并 feature/B"
```

**squash merge 冲突处理**：
```markdown
squash merge 冲突：
- 冲突文件：xxx
- 处理步骤：
  1. 解决冲突文件中的冲突标记
  2. git add <已解决的文件>
  3. git commit -m "test: 合并 feature/X（解决冲突）"
  4. 如冲突过多无法解决：git merge --abort 放弃，报告给用户
```

**test 分支管理规则**：
- test 是临时分支，测试完成后可以删除重建
- 测试发现的 bug 直接在对应 feature 分支上修复，修复后重新合并到 test
- test 分支不直接发布

### 3. 发布上线

**激活指令**：用户明确说"发布 feature/A feature/B"、"上线 xxx"

```bash
git fetch --all --prune
# ⚠️ REQUIRES_CONFIRMATION: 删除并重建 release 分支
git checkout main
git log main..release --oneline 2>/dev/null  # 检查未同步提交
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
git branch -d release 2>/dev/null || git branch -D release
git checkout -b release main

git merge --squash feature/A && git commit -m "release: 合并 feature/A"
# 如果有冲突 → 解决后 git add . && git commit -m "release: 合并 feature/A（解决冲突）"
git merge --squash feature/B && git commit -m "release: 合并 feature/B"
```

**版本号规范**：遵循 [Semantic Versioning](https://semver.org/)（MAJOR.MINOR.PATCH）
- MAJOR：不兼容的 API 变更 | MINOR：向后兼容的功能新增 | PATCH：向后兼容的 Bug 修复
- 版本号由发布者根据本次变更内容决定

**发布完成后：打 tag → 推送 → 同步到 main**（必须确认）：

```bash
# ⚠️ REQUIRES_CONFIRMATION: 推送 release（可能触发 CI/CD）
git push origin release

# ⚠️ REQUIRES_CONFIRMATION: 创建版本 tag
git tag -a v1.x.x -m "release: v1.x.x 包含 feature/A, feature/B"
git push origin v1.x.x

# ⚠️ REQUIRES_CONFIRMATION: 合并到 main
git checkout main
git merge release
git push origin main

# ⚠️ REQUIRES_CONFIRMATION: 删除已发布分支（本地+远程）
git branch -D feature/A && git push origin --delete feature/A
git branch -D feature/B && git push origin --delete feature/B
```

确认提示（必须确认）：
```markdown
⚠️ 即将执行发布流程

确认信息：
- 包含功能：feature/A, feature/B
- 操作序列：
  1. 推送 release → 远程（可能触发 CI/CD）
  2. 打 tag v1.x.x
  3. 同步 release → main
  4. 删除已发布 feature 分支

确认发布？(y/n)
```

**CI/CD 集成提示**：
- 推送 release 后 → 提示确认 staging 环境 CI/CD 状态
- 推送 main 后 → 提示确认 production 部署状态
- 打 tag 后 → 如有基于 tag 的发布流程，提示检查 release pipeline

### 4. 紧急修复（Hotfix）

**激活指令**：用户明确说"hotfix xxx"、"紧急修复 xxx"

#### 标准流程（推荐）

```bash
git fetch --all --prune
git checkout -b feature/hotfix-[问题描述] main
# 修复完成后走正常流程：test → release → tag → main
```

#### 加急通道（跳过 test，需额外确认）

**适用场景**：线上 P0/P1 事故，需立即上线。

```bash
# ⚠️ REQUIRES_CONFIRMATION: 加急通道 — 跳过 test
git fetch --all --prune
git checkout -b feature/hotfix-[问题描述] main
# ... 修复代码 ...
# 确保 release 分支存在（如不存在则从 main 创建）
git checkout release 2>/dev/null || git checkout -b release main
git merge --squash feature/hotfix-[问题描述] && git commit -m "hotfix: [问题描述]"
```

确认提示（必须确认）：
```markdown
⚠️⚠️ 加急修复通道 — 跳过测试直接发布

风险警告：此修复未经 test 验证，直接发布到生产。

确认信息：
- 修复内容：[描述]
- 影响范围：[文件/模块]

后续要求：发布后 24h 内补充完整测试。

确认使用加急通道？(y/n)
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
- feature/PROJ-123-user-management（当前，3 天未同步）
- feature/PROJ-456-payment（2 天未同步）

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
git log --oneline --merges main  # 找到 release→main 的 merge commit
# 注意：feature→release 使用 squash merge，无法通过 --merges 找到
# 如需回滚特定 feature，找到对应的 release merge commit 即可
git checkout main
git revert -m 1 <merge-commit-sha>
git push origin main
```

确认提示：
```markdown
⚠️ 即将回滚已发布功能

操作：git revert -m 1 <commit>
影响：撤销该合并引入的所有更改，保留历史记录
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
禁止：此操作禁止用于 main/release/test 等共享分支

确认执行？(y/n)
```

## README 工作流文档同步

**触发条件**：仅在用户明确要求时执行（如"同步工作流到 README"）。

**不会自动执行**：避免意外修改项目文档。

**执行步骤**：
1. 用 Grep 检查 README.md 是否已包含 `Git 工作流` 或 `分支策略`
2. 如缺失 → 生成内容（参考上方分支模型、提交规范、合并策略章节），用 Edit 追加（**必须确认，展示 diff 预览**）
3. 如已存在 → 展示现有内容，询问是否需要更新

**生成 README 内容时参考**（精简版，仅保留使用者需要的信息）：
- 分支简介：一句话说明 main / feature / test / release 各自用途，不展开细节列
- 操作流程：简述 `创建 feature → 合并到 test → 发布到 release → 同步 main` 的基本步骤
- 使用方式：使用上方"激活指令"表格

**不需要写入 README 的内容**：Conventional Commits 格式、合并策略、hotfix 加急通道、cherry-pick、异常处理等细节属于 skill 内部规范，不需要暴露到项目 README 中。

## 注意事项

1. **main 分支保护**：禁止直接提交代码，只接受 release 的同步
2. **feature 隔离**：每个 feature 独立开发，避免相互依赖
3. **test/release 临时性**：定期清理重建，不保留历史
4. **同步及时性**：发布完成后立即同步到 main
5. **squash 后删除分支**：squash merge 后 git 不标记 feature 为已合并，需用 `-D` 删除（确认提交已包含在 squash 中）
