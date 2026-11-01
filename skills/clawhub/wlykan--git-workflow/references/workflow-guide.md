# Git工作流程指南

## 目录
1. [日常工作流程](#日常工作流程)
2. [新功能开发流程](#新功能开发流程)
3. [Bug修复流程](#bug修复流程)
4. [紧急修复流程](#紧急修复流程)
5. [发布流程](#发布流程)

## 日常工作流程

### 1. 开始工作前
```bash
# 1. 更新本地仓库
git fetch origin

# 2. 切换到dev分支
git checkout dev
git pull origin dev

# 3. 创建功能分支（如果需要）
git checkout -b feature/[功能名]
```

### 2. 开发过程中
```bash
# 1. 定期提交代码
git add .
git commit -m "feat: 实现xxx功能"

# 2. 定期同步dev分支
git checkout dev
git pull origin dev
git checkout feature/[功能名]
git rebase dev
```

### 3. 完成工作后
```bash
# 1. 合并到dev分支
git checkout dev
git merge --no-ff feature/[功能名]
git push origin dev

# 2. 删除功能分支
git branch -d feature/[功能名]
```

## 新功能开发流程

### 阶段1：需求分析
1. 明确功能需求和验收标准
2. 确定技术方案和实现路径
3. 评估开发时间和风险

### 阶段2：分支创建
```bash
# 1. 确定分支策略
# 选项1：创建发布分支 + 功能分支（确定上线）
# 选项2：只创建功能分支（实验性功能）
# 选项3：在dev分支上开发（小修改）

# 2. 创建分支
git checkout dev
git pull origin dev
git checkout -b feature/[功能名]
```

### 阶段3：功能开发
1. 按照技术方案实现功能
2. 编写单元测试
3. 定期提交代码

### 阶段4：代码审查
1. 创建Pull Request
2. 邀请团队成员审查
3. 根据反馈修改代码

### 阶段5：测试验证
1. 在dev环境测试
2. 验证功能是否符合需求
3. 修复发现的问题

### 阶段6：合并发布
```bash
# 1. 合并到dev分支
git checkout dev
git merge --no-ff feature/[功能名]
git push origin dev

# 2. 如果确定上线，创建发布分支
git checkout main
git checkout -b release/[日期]
git merge --no-ff feature/[功能名]
```

## Bug修复流程

### 1. Bug分类
- **紧急Bug**：影响线上功能，需要立即修复
- **一般Bug**：影响用户体验，需要尽快修复
- **轻微Bug**：不影响主要功能，可以计划修复

### 2. 修复流程
```bash
# 1. 根据Bug类型选择分支策略
# 紧急Bug：创建热修复分支
# 一般Bug：在dev分支上修复
# 轻微Bug：在功能分支上修复

# 2. 创建修复分支
git checkout main  # 或 dev
git checkout -b hotfix/[问题描述]  # 或 feature/[修复名]

# 3. 修复Bug
# ... 修改代码 ...

# 4. 测试验证
# ... 测试修复效果 ...

# 5. 合并分支
git checkout main  # 或 dev
git merge --no-ff hotfix/[问题描述]
```

## 紧急修复流程

### 1. 紧急程度评估
- **P0级**：系统完全不可用，需要立即处理
- **P1级**：核心功能受损，需要尽快处理
- **P2级**：次要功能问题，可以计划处理

### 2. 紧急修复步骤
```bash
# 1. 立即创建热修复分支
git checkout main
git pull origin main
git checkout -b hotfix/[问题描述]

# 2. 快速修复问题
# ... 最小化修改 ...

# 3. 紧急测试
# ... 验证修复效果 ...

# 4. 立即发布
git checkout main
git merge --no-ff hotfix/[问题描述]
git tag -a v[版本号] -m "紧急修复"
git push origin main
git push origin [标签]

# 5. 后续处理
# - 通知相关人员
- 记录修复过程
- 安排后续优化
```

## 发布流程

### 1. 发布准备
```bash
# 1. 创建发布分支
git checkout main
git checkout -b release/[日期]

# 2. 合并确定上线的功能
git merge --no-ff feature/[功能1]
git merge --no-ff feature/[功能2]

# 3. 版本号更新
# 更新package.json中的版本号
```

### 2. 测试验证
```bash
# 1. 切换到发布分支
git checkout release/[日期]

# 2. 运行测试
pnpm test
pnpm lint
pnpm build

# 3. 修复问题
# ... 如果发现bug，修复后重新测试 ...
```

### 3. 正式发布
```bash
# 1. 合并到main分支
git checkout main
git merge --no-ff release/[日期]

# 2. 创建版本标签
git tag -a v[版本号] -m "发布版本[版本号]"

# 3. 推送到远程
git push origin main
git push origin v[版本号]

# 4. 合并回dev分支
git checkout dev
git merge --no-ff release/[日期]
git push origin dev

# 5. 删除发布分支
git branch -d release/[日期]
git push origin --delete release/[日期]
```

### 4. 发布后检查
1. 监控系统性能指标
2. 检查错误日志
3. 收集用户反馈
4. 记录发布过程