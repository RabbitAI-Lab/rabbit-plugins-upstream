# Git-workflow Skill 完整实现

## 概述
这是一个完整的Git工作流引导skill，覆盖了从开发到发布的所有环节，确保团队遵循标准的Git Flow工作流。

## 核心特性

### 1. **分层合并流程** ⚠️ 核心原则
```
功能分支 → dev分支（集成测试）
功能分支 → release分支（发布测试）
release分支 → main分支（正式发布）

热修复分支 → main分支（紧急修复）
热修复分支 → dev分支（同步修复）
```

### 2. **完整工作流覆盖**
- ✅ **发布规划**：确定发布计划和分支策略
- ✅ **功能开发**：开发规范和最佳实践
- ✅ **集成测试**：合并到dev进行集成测试
- ✅ **发布测试**：合并到release进行发布测试
- ✅ **正式发布**：合并到main进行正式发布
- ✅ **问题处理**：常见问题解决方案

### 3. **智能引导**
- ✅ **上下文感知**：根据当前状态提供建议
- ✅ **场景识别**：自动识别新功能、Bug修复、发布等场景
- ✅ **最佳实践**：提供行业最佳实践和规范

## Skill 结构

```
~/.agents/skills/git-workflow/
├── SKILL.md                    # 核心skill文档
├── README.md                   # 本说明文档
├── workflows/                  # 工作流模板
│   ├── new-feature.md         # 新功能工作流
│   ├── bug-fix.md             # Bug修复工作流
│   ├── release.md             # 发布工作流
│   └── hotfix.md              # 热修复工作流
├── guides/                     # 操作指南
│   ├── branch-creation.md     # 分支创建指南
│   └── branch-merge.md        # 分支合并指南
├── references/                 # 参考资料
│   ├── branch-strategy.md     # 分支策略详解
│   ├── workflow-guide.md      # 工作流程指南
│   └── troubleshooting.md     # 常见问题处理
├── scripts/                    # 脚本目录（自包含）
│   ├── release.sh             # 发布脚本（Linux/macOS）
│   ├── release.bat            # 发布脚本（Windows）
│   ├── release.config.sh      # 发布配置文件
│   ├── test-release.sh        # 测试环境脚本
│   ├── create-feature-branch.sh  # 功能分支创建
│   ├── create-hotfix-branch.sh   # 热修复分支创建
│   ├── README.md              # 脚本使用说明
│   └── EXAMPLES.md            # 使用示例
└── docs/                       # 文档目录（自包含）
    └── RELEASE_SCRIPT_USAGE.md  # 发布脚本使用指南
```

## 使用场景

### 场景1：新功能开发
```
用户：我要开发用户管理功能
Skill：检测到您要开发新功能，请先确定发布计划：
1. 创建发布分支 + 功能分支（推荐）
2. 只创建功能分支
请选择（1/2）：1
Skill：请提供发布版本信息：
用户：1.2.0
Skill：正在创建分支...
- 创建发布分支：release/1.2.0
- 创建功能分支：feature/user-management
```

### 场景2：Bug修复
```
用户：修复登录页面崩溃的bug
Skill：检测到您要修复bug，请先确定发布计划：
1. 创建热修复分支（推荐）
2. 在dev分支上修复
请选择（1/2）：1
Skill：正在创建热修复分支...
- 创建热修复分支：hotfix/login-crash-fix
```

### 场景3：合并分支
```
用户：我要合并功能分支到dev
Skill：检测到您要合并分支，请选择合并类型：
1. 合并功能分支到dev（开发完成）
2. 合并功能分支到发布分支（准备发布）
3. 合并发布分支到main（正式发布）
4. 合并热修复分支到main（紧急修复）
请选择（1/2/3/4）：1
```

## 分层合并流程详解

### 1. 功能分支 → dev分支
**时机**：功能开发完成，本地测试通过
**目的**：集成到开发环境，进行集成测试
**命令**：
```bash
git checkout dev
git merge --no-ff feature/xxx
git push origin dev
```

### 2. 功能分支 → release分支
**时机**：dev环境测试通过，确定功能要上线
**目的**：准备发布内容，进行发布测试
**命令**：
```bash
git checkout release/xxx
git merge --no-ff feature/xxx
git push origin release/xxx
```

### 3. release分支 → main分支
**时机**：release环境测试通过
**目的**：正式发布到生产环境
**命令**：
```bash
git checkout main
git merge --no-ff release/xxx
git tag -a v1.2.0 -m "发布版本"
git push origin main
git push origin v1.2.0
```

## 优势对比

| 方面 | 传统方式 | 使用skill |
|------|----------|-----------|
| **流程规范** | 依赖个人自觉 | 自动引导 |
| **错误率** | 容易出错 | 几乎不会出错 |
| **效率** | 需要记忆流程 | 一键引导 |
| **一致性** | 团队不统一 | 完全统一 |
| **教育性** | 无 | 帮助理解流程 |

## 质量指标

### 流程质量
- 分支命名规范率 > 95%
- 合并流程执行率 100%
- 测试覆盖率 > 90%

### 效率质量
- 分支创建时间 < 1分钟
- 合并时间 < 10分钟
- 发布时间 < 2小时

### 协作质量
- 团队流程一致性 > 95%
- 问题响应时间 < 1小时
- 知识共享率 > 90%

## 常见问题

### Q1：为什么需要分层合并？
A1：分层合并确保：
1. 代码质量：多层测试保证
2. 发布可控：精确控制上线内容
3. 回滚容易：问题时可快速回滚
4. 团队协作：统一工作流程

### Q2：如何处理紧急修复？
A2：紧急修复流程：
1. 创建热修复分支
2. 修复问题
3. 合并到main（紧急修复）
4. 合并到dev（同步修复）
5. 删除热修复分支

### Q3：如何处理不确定是否上线的功能？
A3：可以：
1. 只创建功能分支
2. 合并到dev进行测试
3. 等待下次发布时再决定是否包含

## 工具和脚本

### 发布脚本（自包含）
```bash
# 创建发布分支并合并功能
./scripts/release.sh [版本号] [功能分支1] [功能分支2]

# 发布到main并创建标签
./scripts/release.sh [版本号] publish-with-tag

# 创建发布分支并创建功能分支
./scripts/release.sh [版本号] --create [功能分支1] [功能分支2]
```

### 分支创建脚本（自包含）
```bash
# 创建功能分支
./scripts/create-feature-branch.sh [功能名]

# 创建热修复分支
./scripts/create-hotfix-branch.sh [问题描述]
```

### 测试环境脚本（自包含）
```bash
# 创建测试环境
./scripts/test-release.sh
```

### 配置文件（自包含）
```bash
# 编辑发布配置
vim scripts/release.config.sh
```

## 更新日志

### v1.0.0 (2026-08-06)
- ✅ 实现完整工作流引导
- ✅ 实现分层合并流程
- ✅ 实现智能推荐
- ✅ 实现问题处理
- ✅ 创建完整文档

## 团队推广

### 推广步骤
1. **培训**：组织团队培训，讲解skill使用
2. **试点**：在小范围试点，收集反馈
3. **推广**：全面推广，确保团队使用
4. **优化**：根据反馈持续优化

### 成功标准
- 团队成员100%使用skill
- 分支命名规范率 > 95%
- 合并流程执行率 100%
- 发布成功率 > 99%