# 发布脚本使用示例

## 示例1：基础发布流程

### 场景
有三个功能分支：feature/A、feature/B、feature/C
临时决定B功能不上线

### 步骤

#### 1. 创建发布分支并合并A和C
```bash
./scripts/release.sh 1.0.0 feature/A feature/C
```

#### 2. 切换到发布分支进行测试
```bash
git checkout release/1.0.0

# 运行测试
pnpm test

# 构建验证
pnpm build
```

#### 3. 测试通过后发布
```bash
# 回到main分支
git checkout main

# 发布并创建标签
./scripts/release.sh 1.0.0 publish-with-tag
```

#### 4. 验证发布结果
```bash
# 查看main分支的提交历史
git log --oneline main

# 查看标签
git tag -l

# 查看发布分支（如果未删除）
git branch | grep release
```

## 示例2：紧急修复流程

### 场景
线上发现紧急bug，需要立即修复

### 步骤

#### 1. 从main创建热修复分支
```bash
git checkout main
git checkout -b hotfix/修复紧急bug
```

#### 2. 修复bug
```bash
# 编辑文件
vim src/utils/fix.js

# 提交修复
git add .
git commit -m "fix: 修复紧急bug"
```

#### 3. 合并到main和dev
```bash
# 合并到main
git checkout main
git merge --no-ff hotfix/修复紧急bug
git tag -a v1.0.1 -m "热修复版本"
git push origin main
git push origin v1.0.1

# 合并到dev
git checkout dev
git merge --no-ff hotfix/修复紧急bug
git push origin dev

# 删除热修复分支
git branch -d hotfix/修复紧急bug
```

## 示例3：功能分支管理

### 场景
开发多个功能，需要合理管理分支

### 步骤

#### 1. 创建功能分支
```bash
# 从dev创建功能分支
git checkout dev
git checkout -b feature/用户管理
git checkout -b feature/权限管理
git checkout -b feature/报表统计
```

#### 2. 开发完成后合并到dev
```bash
# 合并用户管理功能
git checkout dev
git merge --no-ff feature/用户管理
git push origin dev

# 合并权限管理功能
git merge --no-ff feature/权限管理
git push origin dev
```

#### 3. 删除已合并的功能分支
```bash
git branch -d feature/用户管理
git branch -d feature/权限管理
```

## 示例4：版本回滚

### 场景
新版本发布后发现严重问题，需要回滚

### 步骤

#### 1. 回滚main分支
```bash
# 查看所有标签
git tag -l

# 回滚到指定版本
git checkout main
git reset --hard v1.0.0
git push origin main --force
```

#### 2. 回滚dev分支
```bash
git checkout dev
git reset --hard v1.0.0
git push origin dev --force
```

#### 3. 通知团队
```bash
# 发送回滚通知
echo "已回滚到v1.0.0版本，请检查相关功能"
```

## 示例5：使用配置文件

### 场景
需要自定义发布脚本的行为

### 步骤

#### 1. 编辑配置文件
```bash
vim scripts/release.config.sh
```

#### 2. 修改配置项
```bash
# 修改分支名称
MAIN_BRANCH="master"
DEV_BRANCH="develop"

# 修改标签前缀
TAG_PREFIX="release-"

# 禁用自动创建标签
AUTO_CREATE_TAG=false
```

#### 3. 使用配置文件
```bash
# 脚本会自动加载配置文件
./scripts/release.sh 1.0.0 feature/A
```

## 示例6：测试环境验证

### 场景
在发布前验证脚本功能

### 步骤

#### 1. 创建测试环境
```bash
./scripts/test-release.sh
```

#### 2. 在测试环境中验证
```bash
# 进入测试目录
cd /tmp/pms-pc-test-*

# 测试创建发布分支
./scripts/release.sh 1.0.0 feature/A feature/C

# 测试发布
./scripts/release.sh 1.0.0 publish-with-tag
```

#### 3. 清理测试环境
```bash
rm -rf /tmp/pms-pc-test-*
```

## 示例7：Windows环境使用

### 场景
在Windows环境下使用发布脚本

### 步骤

#### 1. 使用批处理脚本
```cmd
# 查看帮助
scripts\release.bat --help

# 创建发布分支
scripts\release.bat 1.0.0 feature/A feature/C

# 发布
scripts\release.bat 1.0.0 publish-with-tag
```

#### 2. 或者使用Git Bash
```bash
# 在Git Bash中使用bash脚本
./scripts/release.sh 1.0.0 feature/A feature/C
```

## 示例8：团队协作流程

### 场景
多人协作开发，统一发布流程

### 步骤

#### 1. 开发人员工作流
```bash
# 从dev创建功能分支
git checkout dev
git checkout -b feature/新功能

# 开发完成后
git add .
git commit -m "feat: 实现新功能"

# 合并到dev
git checkout dev
git merge --no-ff feature/新功能
git push origin dev

# 删除功能分支
git branch -d feature/新功能
```

#### 2. 测试人员工作流
```bash
# 在dev环境测试
git checkout dev
pnpm dev

# 测试完成后通知开发团队
```

#### 3. 发布负责人工作流
```bash
# 创建发布分支
./scripts/release.sh 1.0.0 feature/功能1 feature/功能2

# 测试发布分支
git checkout release/1.0.0
pnpm test
pnpm build

# 发布
./scripts/release.sh 1.0.0 publish-with-tag
```

## 示例9：处理合并冲突

### 场景
功能分支与main分支有冲突

### 步骤

#### 1. 检查冲突
```bash
# 尝试合并
git merge feature/有冲突的功能

# 查看冲突文件
git status
```

#### 2. 解决冲突
```bash
# 编辑冲突文件
vim src/components/冲突文件.vue

# 解决冲突后提交
git add .
git commit -m "resolve: 解决合并冲突"
```

#### 3. 继续发布流程
```bash
# 完成发布
./scripts/release.sh 1.0.0 publish-with-tag
```

## 示例10：查看发布历史

### 场景
需要查看项目发布历史

### 步骤

#### 1. 查看所有标签
```bash
git tag -l
```

#### 2. 查看特定版本的提交
```bash
# 查看v1.0.0到v1.1.0之间的提交
git log v1.0.0..v1.1.0 --oneline
```

#### 3. 查看发布分支的提交
```bash
# 查看release/1.0.0分支相对于main的提交
git log main..release/1.0.0 --oneline
```

#### 4. 查看发布说明
```bash
# 查看标签的详细信息
git show v1.0.0
```

## 示例11：自动化脚本集成

### 场景
将发布脚本集成到CI/CD流程

### 步骤

#### 1. 创建CI配置文件
```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        run: pnpm build
      - name: Test
        run: pnpm test
      - name: Deploy
        run: ./scripts/deploy.sh
```

#### 2. 使用发布脚本触发CI
```bash
# 发布时会自动触发CI流程
./scripts/release.sh 1.0.0 publish-with-tag
```

## 示例12：多环境发布

### 场景
需要发布到多个环境（开发、测试、生产）

### 步骤

#### 1. 发布到开发环境
```bash
# 从dev创建发布分支
./scripts/release.sh 1.0.0 feature/A feature/B

# 合并到dev分支（自动）
```

#### 2. 发布到测试环境
```bash
# 在发布分支上测试
git checkout release/1.0.0
pnpm test

# 合并到测试分支
git checkout test
git merge --no-ff release/1.0.0
git push origin test
```

#### 3. 发布到生产环境
```bash
# 测试通过后发布到main
./scripts/release.sh 1.0.0 publish-with-tag
```

## 总结

这些示例展示了发布脚本的各种使用场景，从基础发布到高级用法，涵盖了团队协作的各个方面。根据实际需求选择合适的示例进行使用。