# 新功能开发工作流

## 目标
规范新功能开发的完整流程，确保代码质量和团队协作。

## 工作流步骤

### 阶段0：发布规划 ⚠️ REQUIRED
**时间**：开始开发前
**行动**：
1. 确定功能是否要上线
2. 选择分支策略
3. 创建相应分支

**分支策略选择**：
```
1. 创建发布分支 + 功能分支（确定上线）
   - 适合：明确要上线的功能
   - 流程：创建发布分支 → 创建功能分支 → 开发 → 合并到dev → 测试 → 合并到release → 发布

2. 只创建功能分支（不确定上线）
   - 适合：实验性功能或不确定是否上线
   - 流程：创建功能分支 → 开发 → 合并到dev → 测试 → 下次发布时决定
```

**检查点**：
- [ ] 发布计划已确定
- [ ] 分支策略已选择
- [ ] 相应分支已创建

### 阶段1：功能开发 ⚠️ REQUIRED
**时间**：分支创建后
**行动**：
1. 按照技术方案实现功能
2. 编写单元测试
3. 定期提交代码
4. 定期同步dev分支

**开发规范**：
```bash
# 1. 定期提交（每天至少一次）
git add .
git commit -m "feat: 实现xxx功能"

# 2. 定期同步（每周至少两次）
git checkout dev
git pull origin dev
git checkout feature/xxx
git rebase dev

# 3. 提交规范
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式
refactor: 重构
test: 测试
chore: 构建/工具
```

**检查点**：
- [ ] 功能按计划实现
- [ ] 单元测试已编写
- [ ] 代码已定期提交
- [ ] 分支已定期同步

### 阶段2：集成测试（合并到dev）⚠️ REQUIRED
**时间**：功能开发完成后
**行动**：
1. 合并功能分支到dev分支
2. 在dev环境进行集成测试
3. 修复发现的问题
4. 确认测试通过

**合并命令**：
```bash
# 合并功能分支到dev
git checkout dev
git merge --no-ff feature/xxx
git push origin dev
```

**测试清单**：
```markdown
## 集成测试清单
- [ ] 功能集成正常
- [ ] 与其他功能兼容
- [ ] 性能测试通过
- [ ] 安全测试通过
- [ ] 用户体验正常
```

**检查点**：
- [ ] 功能已合并到dev
- [ ] 集成测试通过
- [ ] 问题已修复
- [ ] 测试报告已记录

### 阶段3：发布测试（合并到release）⚠️ REQUIRED
**时间**：dev环境测试通过后
**行动**：
1. 合并功能分支到发布分支
2. 在release环境进行发布测试
3. 修复发现的问题
4. 确认测试通过

**合并命令**：
```bash
# 合并功能分支到发布分支
git checkout release/xxx
git merge --no-ff feature/xxx
git push origin release/xxx
```

**测试清单**：
```markdown
## 发布测试清单
- [ ] 功能在release环境正常
- [ ] 与已发布功能兼容
- [ ] 性能测试通过
- [ ] 安全测试通过
- [ ] 用户体验正常
- [ ] 回滚测试通过
```

**检查点**：
- [ ] 功能已合并到release
- [ ] 发布测试通过
- [ ] 问题已修复
- [ ] 测试报告已记录

### 阶段4：代码审查
**时间**：开发完成后
**行动**：
1. 按照技术方案实现功能
2. 编写单元测试
3. 定期提交代码
4. 定期同步dev分支

**开发规范**：
```bash
# 1. 定期提交（每天至少一次）
git add .
git commit -m "feat: 实现xxx功能"

# 2. 定期同步（每周至少两次）
git checkout dev
git pull origin dev
git checkout feature/xxx
git rebase dev

# 3. 提交规范
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式
refactor: 重构
test: 测试
chore: 构建/工具
```

**检查点**：
- [ ] 功能按计划实现
- [ ] 单元测试已编写
- [ ] 代码已定期提交
- [ ] 分支已定期同步

### 阶段4：代码审查
**时间**：开发完成后
**行动**：
1. 创建Pull Request
2. 邀请团队成员审查
3. 根据反馈修改代码
4. 通过审查

**Pull Request规范**：
```markdown
## 描述
简要描述这个PR的内容

## 变更类型
- [ ] 新功能
- [ ] Bug修复
- [ ] 重构
- [ ] 文档更新

## 测试情况
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 手动测试通过

## 截图（如适用）
如果有UI变更，请提供截图
```

**检查点**：
- [ ] Pull Request已创建
- [ ] 审查者已邀请
- [ ] 反馈已处理
- [ ] 审查已通过

### 阶段4：测试验证（在dev环境）⚠️ REQUIRED
**时间**：集成测试通过后
**行动**：
1. 在dev环境进行全面测试
2. 验证功能是否符合需求
3. 修复发现的问题
4. 确认测试通过

**测试清单**：
```markdown
## 功能测试
- [ ] 所有功能测试通过
- [ ] 边界条件测试通过
- [ ] 异常情况测试通过

## 性能测试
- [ ] 响应时间达标
- [ ] 并发处理正常
- [ ] 内存使用正常

## 安全测试
- [ ] 权限控制正常
- [ ] 数据加密正常
- [ ] 输入验证正常

## 用户体验
- [ ] 界面交互正常
- [ ] 操作流程顺畅
- [ ] 错误提示友好
```

**检查点**：
- [ ] 所有测试用例通过
- [ ] 问题已修复
- [ ] 测试报告已记录

### 阶段5：发布准备（合并到release）⚠️ REQUIRED
**时间**：dev环境测试通过后
**行动**：
1. 确定功能要上线
2. 合并功能分支到发布分支
3. 在release环境进行发布测试
4. 修复发现的问题

**合并命令**：
```bash
# 合并功能分支到发布分支
git checkout release/xxx
git merge --no-ff feature/xxx
git push origin release/xxx
```

**发布测试清单**：
```markdown
## 发布测试
- [ ] 功能在release环境正常
- [ ] 与已发布功能兼容
- [ ] 性能测试通过
- [ ] 安全测试通过
- [ ] 用户体验正常

## 回滚测试
- [ ] 回滚方案可行
- [ ] 回滚操作正常
- [ ] 数据一致性正常
```

**检查点**：
- [ ] 功能已合并到release
- [ ] 发布测试通过
- [ ] 问题已修复
- [ ] 测试报告已记录

### 阶段6：正式发布（合并到main）⚠️ REQUIRED
**时间**：release环境测试通过后
**行动**：
1. 合并发布分支到main分支
2. 创建版本标签
3. 部署到生产环境
4. 验证发布结果

**发布命令**：
```bash
# 1. 合并发布分支到main
git checkout main
git merge --no-ff release/xxx

# 2. 创建版本标签
git tag -a v1.2.0 -m "发布版本 1.2.0"

# 3. 推送到远程
git push origin main
git push origin v1.2.0

# 4. 合并回dev分支
git checkout dev
git merge --no-ff release/xxx
git push origin dev

# 5. 删除发布分支
git branch -d release/xxx
git push origin --delete release/xxx
```

**发布检查清单**：
```markdown
## 发布前检查
- [ ] 所有要上线的功能已合并到release
- [ ] release环境测试通过
- [ ] 发布说明已准备
- [ ] 回滚方案已准备
- [ ] 监控已配置

## 发布过程
- [ ] 合并release分支到main
- [ ] 创建版本标签
- [ ] 推送到远程
- [ ] 部署到生产环境
- [ ] 验证发布结果

## 发布后检查
- [ ] 系统状态正常
- [ ] 用户反馈正常
- [ ] 文档已更新
- [ ] 发布分支已删除
```

**检查点**：
- [ ] 已合并到main分支
- [ ] 版本标签已创建
- [ ] 已部署到生产环境
- [ ] 发布结果已验证

## 常见问题处理

### 1. 开发过程中需要修复紧急bug
```bash
# 1. 暂存当前工作
git stash

# 2. 创建热修复分支
git checkout main
git checkout -b hotfix/xxx

# 3. 修复bug
# ... 修复代码 ...

# 4. 合并到main和dev
git checkout main
git merge --no-ff hotfix/xxx
git checkout dev
git merge --no-ff hotfix/xxx

# 5. 恢复工作
git checkout feature/xxx
git stash pop
```

### 2. 需要同时开发多个功能
```bash
# 1. 为每个功能创建独立分支
git checkout -b feature/功能1
git checkout -b feature/功能2

# 2. 分别开发，定期同步dev
git checkout feature/功能1
git rebase dev

git checkout feature/功能2
git rebase dev
```

### 3. 功能开发完成但不想立即上线
```bash
# 1. 合并到dev分支
git checkout dev
git merge --no-ff feature/xxx

# 2. 不创建发布分支
# 等待下次发布时再决定是否包含
```

## 工具和脚本

### 分支创建脚本
```bash
# 创建功能分支
./scripts/create-feature-branch.sh [功能名]

# 从main创建功能分支
./scripts/create-feature-branch.sh [功能名] --from-main
```

### 分支检查脚本
```bash
# 检查分支命名规范
./scripts/check-branch-standards.sh

# 清理已合并分支
./scripts/cleanup-branches.sh
```

## 质量指标

### 代码质量
- 单元测试覆盖率 > 80%
- 代码审查通过率 100%
- 静态代码分析无严重问题

### 流程质量
- 分支命名规范率 100%
- 提交信息规范率 100%
- 文档更新及时率 100%

### 协作质量
- Pull Request响应时间 < 24小时
- 问题解决时间 < 48小时
- 知识分享频率 > 每周1次