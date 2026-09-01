# Git分支策略详解

## 目录
1. [分支类型](#分支类型)
2. [分支命名规范](#分支命名规范)
3. [分支工作流程](#分支工作流程)
4. [分支保护规则](#分支保护规则)
5. [常见问题处理](#常见问题处理)

## 分支类型

### 1. 主分支
- **main**：线上稳定版本，只包含已发布、经过充分测试的代码
- **dev**：开发测试环境，包含所有正在开发和测试的功能

### 2. 辅助分支
- **feature/xxx**：功能分支，从dev创建，开发完合回dev
- **release/xxx**：发布分支，从main创建，只包含确定要上线的功能
- **hotfix/xxx**：热修复分支，从main创建，用于紧急修复线上问题

## 分支命名规范

### 功能分支
```
feature/[功能名]
```
**示例：**
- `feature/user-management`
- `feature/login-optimization`
- `feature/dashboard-chart`

### 热修复分支
```
hotfix/[问题描述]
```
**示例：**
- `hotfix/login-crash-fix`
- `hotfix/payment-timeout`
- `hotfix/data-sync-error`

### 发布分支
```
release/[YYYY-MM-DD] 或 release/[版本号]
```
**示例：**
- `release/2026-08-06`
- `release/1.2.0`
- `release/v2.1.0`

## 分支工作流程

### 1. 功能开发流程
```bash
# 1. 从dev创建功能分支
git checkout dev
git pull origin dev
git checkout -b feature/user-management

# 2. 开发功能
# ... 编写代码 ...

# 3. 提交代码
git add .
git commit -m "feat: 实现用户管理功能"

# 4. 合并回dev
git checkout dev
git merge --no-ff feature/user-management
git push origin dev

# 5. 删除功能分支
git branch -d feature/user-management
```

### 2. 发布流程
```bash
# 1. 创建发布分支
git checkout main
git pull origin main
git checkout -b release/2026-08-06

# 2. 合并确定要上线的功能
git merge --no-ff feature/user-management
git merge --no-ff feature/login-optimization

# 3. 测试发布分支
git checkout release/2026-08-06
pnpm test
pnpm build

# 4. 发布到main
git checkout main
git merge --no-ff release/2026-08-06
git tag -a v1.2.0 -m "发布版本1.2.0"
git push origin main
git push origin v1.2.0

# 5. 合并回dev
git checkout dev
git merge --no-ff release/2026-08-06
git push origin dev
```

### 3. 热修复流程
```bash
# 1. 从main创建热修复分支
git checkout main
git pull origin main
git checkout -b hotfix/login-crash-fix

# 2. 修复bug
# ... 修改代码 ...

# 3. 提交修复
git add .
git commit -m "fix: 修复登录崩溃问题"

# 4. 合并到main
git checkout main
git merge --no-ff hotfix/login-crash-fix
git tag -a v1.2.1 -m "热修复版本1.2.1"
git push origin main
git push origin v1.2.1

# 5. 合并到dev
git checkout dev
git merge --no-ff hotfix/login-crash-fix
git push origin dev

# 6. 删除热修复分支
git branch -d hotfix/login-crash-fix
```

## 分支保护规则

### GitHub分支保护
```yaml
# .github/settings.yml
branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 2
      restrictions:
        teams: []
      enforce_admins: false
```

### GitLab分支保护
```yaml
# .gitlab-ci.yml
protect_branches:
  main:
    push_access_level: 0
    merge_access_level: 30
    unprotect_access_level: 30
```

## 常见问题处理

### 1. 合并冲突
```bash
# 查看冲突文件
git status

# 解决冲突后提交
git add .
git commit -m "resolve: 解决合并冲突"
```

### 2. 分支误删恢复
```bash
# 查看删除的分支
git reflog

# 恢复分支
git checkout -b [分支名] [commit-hash]
```

### 3. 提交历史混乱
```bash
# 使用rebase整理提交历史
git checkout feature/xxx
git rebase -i HEAD~5

# 选择要保留的提交
pick abc1234 feat: 新功能1
squash def5678 feat: 新功能2
```

### 4. 版本回滚
```bash
# 回滚到指定版本
git checkout main
git reset --hard v1.1.0
git push origin main --force

# 同时回滚dev
git checkout dev
git reset --hard v1.1.0
git push origin dev --force
```