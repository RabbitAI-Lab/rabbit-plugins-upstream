# 发布脚本使用指南

## 概述

本项目提供了自动化发布脚本，帮助团队规范发布流程，减少人为错误，提高发布效率。

## 脚本文件

### 1. `scripts/release.sh` - Linux/macOS版本
### 2. `scripts/release.bat` - Windows版本
### 3. `scripts/release.config.sh` - 配置文件

## 快速开始

### 基本用法

```bash
# Linux/macOS
./scripts/release.sh <版本号> [功能分支列表] [命令]

# Windows
scripts\release.bat <版本号> [功能分支列表] [命令]
```

### 示例

#### 1. 创建发布分支（不合并功能）
```bash
# 只创建发布分支
./scripts/release.sh 1.2.0

# 或指定功能分支
./scripts/release.sh 1.2.0 feature/A feature/C
```

#### 2. 合并功能分支
```bash
# 合并指定功能分支到发布分支
./scripts/release.sh 1.2.0 feature/A feature/C
```

#### 3. 发布到main分支
```bash
# 发布到main分支（不创建标签）
./scripts/release.sh 1.2.0 publish

# 发布到main分支并创建标签
./scripts/release.sh 1.2.0 publish-with-tag
```

## 完整工作流程

### 场景：ABC三个功能，临时决定B不上线

#### 步骤1：创建发布分支并合并A和C
```bash
./scripts/release.sh 1.2.0 feature/A feature/C
```

#### 步骤2：在发布分支上进行测试
```bash
# 切换到发布分支
git checkout release/1.2.0

# 运行测试
pnpm test

# 构建验证
pnpm build
```

#### 步骤3：测试通过后发布
```bash
# 发布到main并创建标签
./scripts/release.sh 1.2.0 publish-with-tag
```

#### 步骤4：B功能继续在dev上测试
```bash
# B功能保留在dev分支继续开发
git checkout dev
# 继续开发功能B
```

## 命令详解

### 1. 创建发布分支
```bash
./scripts/release.sh <版本号>
```
- 从main分支创建发布分支
- 列出dev分支上的功能分支
- 提示手动合并需要的功能分支

### 2. 合并功能分支
```bash
./scripts/release.sh <版本号> <功能分支1> <功能分支2> ...
```
- 在发布分支上合并指定的功能分支
- 支持同时合并多个功能分支
- 只合并确定要上线的功能

### 3. 发布到main分支
```bash
./scripts/release.sh <版本号> publish
```
- 合并发布分支到main分支
- 合并回dev分支保持同步
- 询问是否删除发布分支

### 4. 发布并创建标签
```bash
./scripts/release.sh <版本号> publish-with-tag
```
- 包含publish的所有操作
- 创建语义化版本标签（如v1.2.0）
- 推送标签到远程仓库

## 配置文件

编辑 `scripts/release.config.sh` 可以自定义脚本行为：

### 主要配置项

```bash
# 分支配置
MAIN_BRANCH="main"          # 主分支名称
DEV_BRANCH="dev"            # 开发分支名称
FEATURE_BRANCH_PREFIX="feature/"  # 功能分支前缀
RELEASE_BRANCH_PREFIX="release/"  # 发布分支前缀

# 合并策略
USE_NO_FF_MERGE=true        # 使用--no-ff创建合并提交

# 标签配置
AUTO_CREATE_TAG=true        # 自动创建标签
TAG_PREFIX="v"              # 标签前缀

# 安全配置
REQUIRE_CLEAN_WORKSPACE=true  # 要求干净的git工作区
CHECK_BRANCH_MERGED=true      # 检查分支是否已合并
```

### 自定义钩子

可以在配置文件中设置钩子脚本：

```bash
# 前置钩子（创建发布分支之前执行）
PRE_RELEASE_HOOK=""

# 后置钩子（发布完成之后执行）
POST_RELEASE_HOOK=""

# 合并前钩子（合并功能分支之前执行）
PRE_MERGE_HOOK=""

# 合并后钩子（合并功能分支之后执行）
POST_MERGE_HOOK=""
```

## 常见问题

### Q1：如何回滚发布？
```bash
# 回滚到指定版本
git checkout main
git reset --hard v1.1.0  # 回滚到v1.1.0
git push origin main --force

# 同时回滚dev
git checkout dev
git reset --hard v1.1.0
git push origin dev --force
```

### Q2：如何处理紧急bug？
```bash
# 从main创建热修复分支
git checkout -b hotfix/修复紧急bug main

# 修复bug
# ... 修改代码 ...

# 合并到main和dev
git checkout main
git merge --no-ff hotfix/修复紧急bug
git tag -a v1.2.1 -m "热修复版本"

git checkout dev
git merge --no-ff hotfix/修复紧急bug

# 删除热修复分支
git branch -d hotfix/修复紧急bug
```

### Q3：如何查看发布历史？
```bash
# 查看所有标签
git tag -l

# 查看特定版本的提交
git log v1.1.0..v1.2.0

# 查看发布分支的提交
git log main..release/1.2.0
```

### Q4：如何修改已发布的版本？
```bash
# 不建议修改已发布的版本
# 如果必须修改，建议创建新的热修复版本
git checkout -b hotfix/修复问题 main
# ... 修改代码 ...
# 然后按照正常流程发布新版本
```

## 最佳实践

### 1. 版本号规范
- 使用语义化版本号：`主版本号.次版本号.修订号`
- 示例：`1.2.3`
- 主版本号：重大功能更新
- 次版本号：新功能添加
- 修订号：bug修复

### 2. 分支命名规范
- 功能分支：`feature/功能名`
- 发布分支：`release/版本号`
- 热修复分支：`hotfix/问题描述`

### 3. 提交信息规范
```
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 添加测试
chore: 构建/工具链更新
```

### 4. 发布检查清单
- [ ] 所有功能分支已合并到发布分支
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 代码审查完成
- [ ] 文档已更新
- [ ] 发布说明已准备

## 团队协作

### 职责分工
- **开发人员**：在功能分支开发，完成后合并到dev
- **测试人员**：在dev环境测试，确认功能正常
- **发布负责人**：创建发布分支，决定上线功能
- **项目经理**：协调发布计划，确认上线功能

### 沟通机制
1. 每日站会同步开发进度
2. 发布前明确功能上线状态
3. 建立发布群组，及时沟通问题
4. 发布后进行复盘总结

## 故障排除

### 问题1：脚本权限不足
```bash
# Linux/macOS
chmod +x scripts/release.sh

# Windows
# 确保有管理员权限
```

### 问题2：git操作失败
```bash
# 检查git状态
git status

# 检查远程仓库配置
git remote -v

# 检查分支状态
git branch -a
```

### 问题3：合并冲突
```bash
# 解决冲突
git merge --abort  # 中止合并
git merge feature/A  # 重新合并

# 或者手动解决冲突
# 编辑冲突文件
git add .
git commit -m "解决合并冲突"
```

## 更新日志

### v1.0.0 (2026-08-03)
- 初始版本
- 支持创建发布分支
- 支持合并功能分支
- 支持发布到main分支
- 支持创建版本标签
- 支持Windows和Linux/macOS