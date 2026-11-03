# 分支合并指南

## 目标
指导用户如何正确合并Git分支，确保代码集成质量和团队协作效率。

## 合并类型

### 1. 功能分支合并到dev
**时机**：功能开发完成，测试通过
**目的**：集成新功能到开发环境

### 2. 功能分支合并到发布分支
**时机**：确定功能要上线
**目的**：准备发布内容

### 3. 发布分支合并到main
**时机**：发布分支测试通过
**目的**：正式发布到生产环境

### 4. 热修复分支合并到main和dev
**时机**：热修复测试通过
**目的**：紧急修复线上问题

## 分支合并流程

### 1. 功能分支合并到dev ⚠️ REQUIRED
**时机**：功能开发完成，本地测试通过
**目的**：集成到开发环境，进行集成测试

```bash
# 1. 切换到dev分支
git checkout dev
git pull origin dev

# 2. 合并功能分支
git merge --no-ff feature/user-management

# 3. 推送到远程
git push origin dev

# 4. 删除功能分支（可选）
git branch -d feature/user-management
git push origin --delete feature/user-management
```

### 2. 功能分支合并到发布分支 ⚠️ REQUIRED
**时机**：dev环境测试通过，确定功能要上线
**目的**：准备发布内容，进行发布测试

```bash
# 1. 切换到发布分支
git checkout release/2026-08-06

# 2. 合并功能分支
git merge --no-ff feature/user-management

# 3. 推送到远程
git push origin release/2026-08-06

# 4. 删除功能分支（可选）
git branch -d feature/user-management
```

### 3. 发布分支合并到main ⚠️ REQUIRED
**时机**：release环境测试通过
**目的**：正式发布到生产环境

```bash
# 1. 切换到main分支
git checkout main
git pull origin main

# 2. 合并发布分支
git merge --no-ff release/2026-08-06

# 3. 创建版本标签
git tag -a v1.2.0 -m "发布版本 1.2.0"

# 4. 推送到远程
git push origin main
git push origin v1.2.0

# 5. 合并回dev分支（同步）
git checkout dev
git merge --no-ff release/2026-08-06
git push origin dev

# 6. 删除发布分支
git branch -d release/2026-08-06
git push origin --delete release/2026-08-06
```

### 4. 热修复分支合并到main和dev ⚠️ REQUIRED
**时机**：热修复测试通过
**目的**：紧急修复线上问题

```bash
# 1. 切换到main分支
git checkout main
git pull origin main

# 2. 合并热修复分支
git merge --no-ff hotfix/login-crash-fix

# 3. 创建热修复标签
git tag -a v1.2.1 -m "热修复版本 1.2.1"

# 4. 推送到远程
git push origin main
git push origin v1.2.1

# 5. 合并到dev分支（同步修复）
git checkout dev
git merge --no-ff hotfix/login-crash-fix
git push origin dev

# 6. 删除热修复分支
git branch -d hotfix/login-crash-fix
git push origin --delete hotfix/login-crash-fix
```

## 合并策略

### 分层合并流程 ⚠️ REQUIRED
**必须按照以下顺序合并，确保代码质量：**

```
功能分支 → dev分支（集成测试）
功能分支 → release分支（发布测试）
release分支 → main分支（正式发布）

热修复分支 → main分支（紧急修复）
热修复分支 → dev分支（同步修复）
```

**为什么需要分层合并？**
1. **代码隔离**：开发、测试、发布环境分离
2. **质量保证**：多层测试确保质量
3. **灵活控制**：精确控制上线内容
4. **回滚容易**：问题时可快速回滚

### 1. --no-ff（非快进合并）
**优点**：
- 保留完整的分支历史
- 清晰的合并记录
- 便于回滚和追踪

**使用场景**：
- 功能分支合并
- 发布分支合并
- 热修复分支合并

### 2. --squash（压缩合并）
**优点**：
- 简化提交历史
- 保持主分支整洁
- 便于代码审查

**使用场景**：
- 小功能合并
- 修复合并
- 文档更新合并

### 3. --rebase（变基合并）
**优点**：
- 线性提交历史
- 避免不必要的合并提交
- 保持历史清晰

**使用场景**：
- 同步dev分支
- 准备合并前的清理
- 个人分支管理

## 合并前检查

### 1. 代码质量检查
```bash
# 运行代码检查
pnpm lint

# 运行测试
pnpm test

# 检查构建
pnpm build
```

### 2. 分支状态检查
```bash
# 查看分支状态
git status

# 查看分支差异
git diff dev..feature/user-management

# 查看提交历史
git log --oneline dev..feature/user-management
```

### 3. 冲突预防
```bash
# 同步最新代码
git checkout feature/user-management
git rebase dev

# 解决可能的冲突
# ... 解决冲突 ...

# 继续rebase
git rebase --continue
```

## 冲突解决

### 1. 冲突检测
```bash
# 查看冲突文件
git status

# 查看冲突内容
git diff [文件名]
```

### 2. 冲突解决步骤
```bash
# 1. 打开冲突文件，查找冲突标记
<<<<<<< HEAD
当前分支的代码
=======
要合并分支的代码
>>>>>>> [分支名]

# 2. 手动解决冲突，删除冲突标记

# 3. 添加解决后的文件
git add [文件名]

# 4. 完成合并
git commit -m "resolve: 解决合并冲突"
```

### 3. 放弃合并
```bash
# 放弃当前合并
git merge --abort

# 回到合并前的状态
git reset --hard HEAD
```

## 合并后验证

### 1. 功能验证
```markdown
## 功能验证清单
- [ ] 新功能正常工作
- [ ] 相关功能正常
- [ ] 边界条件测试通过
- [ ] 异常情况处理正常
```

### 2. 性能验证
```markdown
## 性能验证清单
- [ ] 响应时间正常
- [ ] 内存使用正常
- [ ] CPU使用正常
- [ ] 并发处理正常
```

### 3. 兼容性验证
```markdown
## 兼容性验证清单
- [ ] 浏览器兼容性正常
- [ ] 移动端兼容性正常
- [ ] 不同分辨率正常
- [ ] 不同操作系统正常
```

## 常见问题

### 1. 合并冲突
**问题**：`CONFLICT (content): Merge conflict in xxx`

**解决方案**：
```bash
# 1. 查看冲突文件
git status

# 2. 手动解决冲突
# ... 编辑冲突文件 ...

# 3. 添加解决后的文件
git add [文件名]

# 4. 完成合并
git commit -m "resolve: 解决合并冲突"
```

### 2. 合并后测试失败
**问题**：合并后功能异常

**解决方案**：
```bash
# 1. 回滚合并
git merge --abort

# 2. 分析问题原因
# ... 分析代码 ...

# 3. 修复问题后重新合并
# ... 修复代码 ...
```

### 3. 合并后性能下降
**问题**：合并后系统变慢

**解决方案**：
```bash
# 1. 回滚合并
git merge --abort

# 2. 性能分析
# ... 分析性能问题 ...

# 3. 优化后重新合并
# ... 优化代码 ...
```

## 最佳实践

### 1. 合并前准备
- 同步最新代码
- 运行测试验证
- 检查代码质量

### 2. 合并过程
- 使用--no-ff保留历史
- 解决冲突要彻底
- 提交信息要规范

### 3. 合并后验证
- 功能验证要全面
- 性能验证要充分
- 兼容性验证要完整

### 4. 团队协作
- 及时通知合并
- 共享合并经验
- 统一合并规范

## 工具和脚本

### 合并检查脚本
```bash
# 检查合并状态
./scripts/check-merge-status.sh [分支名]

# 检查冲突文件
./scripts/check-conflicts.sh
```

### 合并辅助脚本
```bash
# 自动合并功能分支
./scripts/auto-merge-feature.sh [功能分支名]

# 自动合并热修复分支
./scripts/auto-merge-hotfix.sh [热修复分支名]
```

## 质量指标

### 合并质量
- 合并成功率 > 99%
- 冲突解决率 > 98%
- 合并后问题率 < 2%

### 流程质量
- 合并前检查率 > 95%
- 合并后验证率 > 95%
- 文档更新率 > 90%

### 效率质量
- 合并时间 < 10分钟
- 冲突解决时间 < 30分钟
- 问题响应时间 < 1小时