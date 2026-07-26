# 最佳实践与命令参考

## Type 选择指南

### 快速决策表

| 场景 | Type | 示例 |
|------|------|------|
| 新增功能/模块 | `feat` | feat(auth): add login module |
| 修复 Bug | `fix` | fix(parser): resolve memory leak |
| 仅测试改动 | `test` | test(auth): add unit tests |
| 仅文档改动 | `docs` | docs(api): update documentation |
| 代码重构 | `refactor` | refactor(utils): extract helpers |
| 回滚提交 | `revert` | revert(auth): revert changes |
| 多次提交(任意) | `feat` | feat(auth): implement validation |
| 配置/依赖更新 | `chore` | chore(deps): update packages |

---

## 注意事项

### 两种提交方式的行为差异

| 暂存区状态 | 行为 | 说明 |
|----------|------|------|
| 有内容 | 直接生成 message 并提交 | 用户已用 `git add` 选择了文件 |
| 无内容 | 先 `git add .` 再提交 | 自动添加所有变更 |

### 默认路径规则

- 用户提供路径 → 切换到该路径
- 未提供路径 → 使用当前工作目录
- 非 Git 目录 → **立即报错并退出**

---

## 最佳实践

### DO(推荐)

1. ✅ **模块名清晰且必须用圆括号**
   - 使用项目约定的模块名
   - 必须用 `()` 包裹模块名
   - 多模块改动使用主要模块名

2. ✅ **描述简洁明确**
   - 使用英文
   - 动词开头(add, fix, update, remove)
   - 小写字母
   - 格式:`type(module): description`

3. ✅ **多次提交统一使用 feat**
   - 所有提交都用 `feat`

4. ✅ **自动检查**
   - 检查是否有敏感信息

### DON'T(避免)

1. ❌ **不要使用错误的 type**
   - Bug 必须用 `fix`
   - 新功能必须用 `feat`

2. ❌ **不要使用中文**
   - 描述必须是英文
   - ❌ feat(auth): 添加登录模块
   - ✅ feat(auth): add login module

3. ❌ **不要混合多个不相关的改动**
   - 一个 commit 应该聚焦单一目的

---

## 规范对照表

### 本规范 vs Conventional Commits

| 本规范 | Conventional Commits | 差异 |
|-------------|---------------------|------|
| `feat(auth): add login` | `feat(auth): add login` | 基本一致 |
| `fix(parser): resolve bug` | `fix(parser): resolve bug` | 基本一致 |

**关键差异**:
1. **模块名必须用圆括号**:`(skills)` 是必需的

---

## 命令参考

```bash
# === 提交相关 ===
git commit -m "type(module): description"
git log -1                          # 查看最近提交
git show HEAD                       # 查看提交详情
git log --oneline -5                # 查看最近5次提交

# === 推送相关 ===
git push origin main                # 推送到远程
git push origin main --force        # 强制推送(慎用)

# === 撤销相关 ===
git reset --soft HEAD~1             # 撤销提交,保留修改
git reset --hard HEAD~1             # 撤销提交,丢弃修改
git commit --amend -m "new message" # 修改最后一次提交

# === 查看相关 ===
git status                          # 查看状态
git diff --cached                   # 查看暂存区变更
git diff --cached --stat            # 查看变更统计
```

---

## 提交后操作

### 自动建议

```
✅ 提交成功!

🔗 建议的下一步操作:

1️⃣ 推送到远程仓库:
   git push origin main

2️⃣ 查看提交详情:
   git show HEAD

3️⃣ 如果需要修改提交信息:
   git commit --amend -m "新的 commit message"

4️⃣ 如果需要撤销本次提交:
   git reset --soft HEAD~1  # 保留修改
```

---

*最后更新:2026-06-20*
*核心变更:*
- *格式为 `type(module): description`,模块用圆括号*
- *移除 Aone ID 集成*
- *支持智能暂存区处理:暂存区有内容直接提交,为空则自动 git add .*
- *默认使用当前工作目录,非 Git 目录报错退出*
- *支持 feat/fix/test/docs/revert/refactor/chore 7种类型*
