# 分支创建指南

## 目标
指导用户如何正确创建和管理Git分支，确保分支命名规范和结构清晰。

## 分支类型

### 1. 主分支
- **main**：线上稳定版本
- **dev**：开发测试环境

### 2. 辅助分支
- **feature/xxx**：功能分支
- **release/xxx**：发布分支
- **hotfix/xxx**：热修复分支

## 分支命名规范

### 功能分支
```
feature/[功能名]
```
**示例**：
- `feature/user-management`
- `feature/login-optimization`
- `feature/dashboard-chart`

**规范**：
- 使用小写字母
- 使用连字符连接单词
- 名称简洁明了
- 长度不超过50个字符

### 热修复分支
```
hotfix/[问题描述]
```
**示例**：
- `hotfix/login-crash-fix`
- `hotfix/payment-timeout`
- `hotfix/data-sync-error`

**规范**：
- 使用小写字母
- 使用连字符连接单词
- 描述问题本质
- 长度不超过50个字符

### 发布分支
```
release/[YYYY-MM-DD] 或 release/[版本号]
```
**示例**：
- `release/2026-08-06`
- `release/1.2.0`
- `release/v2.1.0`

**规范**：
- 使用日期格式：YYYY-MM-DD
- 或使用版本号格式：主版本.次版本.修订号
- 长度不超过50个字符

## 分支创建流程

### 1. 功能分支创建
```bash
# 1. 确保在正确的基础分支上
git checkout dev
git pull origin dev

# 2. 创建功能分支
git checkout -b feature/user-management

# 3. 推送到远程（可选）
git push origin feature/user-management
```

### 2. 热修复分支创建
```bash
# 1. 从main分支创建
git checkout main
git pull origin main

# 2. 创建热修复分支
git checkout -b hotfix/login-crash-fix

# 3. 推送到远程（可选）
git push origin hotfix/login-crash-fix
```

### 3. 发布分支创建
```bash
# 1. 从main分支创建
git checkout main
git pull origin main

# 2. 创建发布分支
git checkout -b release/2026-08-06

# 3. 合并确定上线的功能
git merge --no-ff feature/user-management
git merge --no-ff feature/login-optimization

# 4. 推送到远程
git push origin release/2026-08-06
```

## 分支验证

### 命名验证
```bash
# 验证分支名是否符合规范
validate_branch_name() {
    local branch_name=$1
    
    # 检查分支名是否为空
    if [ -z "$branch_name" ]; then
        echo "❌ 分支名不能为空"
        return 1
    fi
    
    # 检查分支名格式
    if [[ ! $branch_name =~ ^(feature/|hotfix/|release/) ]]; then
        echo "❌ 分支名必须以 feature/、hotfix/ 或 release/ 开头"
        return 1
    fi
    
    # 检查分支名长度
    if [ ${#branch_name} -gt 50 ]; then
        echo "❌ 分支名长度不能超过50个字符"
        return 1
    fi
    
    echo "✅ 分支名符合规范: $branch_name"
    return 0
}
```

### 状态验证
```bash
# 验证分支创建状态
verify_branch_creation() {
    local branch_name=$1
    
    # 检查分支是否存在
    if git rev-parse --verify $branch_name > /dev/null 2>&1; then
        echo "✅ 分支创建成功: $branch_name"
        echo "当前分支: $(git branch --show-current)"
        return 0
    else
        echo "❌ 分支创建失败: $branch_name"
        return 1
    fi
}
```

## 常见问题

### 1. 分支已存在
**问题**：`fatal: A branch named 'xxx' already exists`

**解决方案**：
```bash
# 查看所有分支
git branch

# 删除本地分支
git branch -d [分支名]

# 强制删除分支（如果分支未合并）
git branch -D [分支名]

# 重新创建分支
git checkout -b [分支名]
```

### 2. 分支创建失败
**问题**：`fatal: Cannot lock ref 'xxx': unable to resolve reference`

**解决方案**：
```bash
# 清理无效引用
git gc

# 重新创建分支
git checkout -b [分支名]
```

### 3. 远程分支已存在
**问题**：`! [remote rejected] xxx -> xxx (refuse to create)`

**解决方案**：
```bash
# 删除远程分支
git push origin --delete [分支名]

# 重新创建并推送
git checkout -b [分支名]
git push origin [分支名]
```

## 最佳实践

### 1. 分支策略选择
- **确定上线**：创建发布分支 + 功能分支
- **实验性功能**：只创建功能分支
- **小修改**：在dev分支上开发

### 2. 分支命名规范
- 使用有意义的名称
- 遵循命名约定
- 保持名称简洁

### 3. 分支管理
- 定期清理已合并分支
- 及时删除废弃分支
- 保持分支结构清晰

### 4. 团队协作
- 通知团队分支创建
- 共享分支策略
- 统一命名规范

## 工具和脚本

### 功能分支创建脚本
```bash
# 创建功能分支
./scripts/create-feature-branch.sh [功能名]

# 从main创建功能分支
./scripts/create-feature-branch.sh [功能名] --from-main

# 模拟创建
./scripts/create-feature-branch.sh [功能名] --dry-run
```

### 热修复分支创建脚本
```bash
# 创建热修复分支
./scripts/create-hotfix-branch.sh [问题描述]

# 从最新release分支创建
./scripts/create-hotfix-branch.sh [问题描述] --from-release

# 模拟创建
./scripts/create-hotfix-branch.sh [问题描述] --dry-run
```

### 分支检查脚本
```bash
# 检查分支命名规范
./scripts/check-branch-standards.sh

# 清理已合并分支
./scripts/cleanup-branches.sh
```

## 质量指标

### 规范性
- 分支命名规范率 > 95%
- 分支结构清晰度 > 90%
- 分支管理规范率 > 95%

### 效率
- 分支创建时间 < 1分钟
- 分支切换时间 < 10秒
- 分支清理时间 < 5分钟

### 协作
- 团队分支策略一致性 > 90%
- 分支通知及时率 > 95%
- 分支冲突解决率 > 98%