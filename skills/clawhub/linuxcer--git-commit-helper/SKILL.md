---
name: git-commit-helper
description: 自动分析代码变更并生成符合规范的 Git Commit
---

# Git Commit 自动提交 Skill

> 自动分析代码变更，生成符合规范的 Commit Message 并执行提交

---

## When to Use(触发条件)

触发关键词:
- "帮我提交代码"
- "提交 git commit"
- "git 提交"
- "自动提交"
- 用户提供了 git 仓库路径

---

## 核心行为

**智能提交模式**:自动判断暂存区状态,生成 Commit Message 并执行提交

### 两种提交方式

1. **暂存区有内容**(`git diff --cached --stat` 有输出)
   - 直接分析已暂存的文件,生成 commit message 并提交

2. **暂存区为空**(`git diff --cached --stat` 无输出)
   - 先执行 `git add .` 添加所有变更
   - 再分析变更内容,生成 commit message 并提交

### 默认路径

- 如果用户提供了仓库路径,切换到该路径
- **如果未提供路径,默认使用当前工作目录**
- 如果当前目录不是 Git 管理的仓库,**立即报错并退出**

所有操作都会:
1. 确认工作目录是 Git 仓库(非 Git 目录直接报错退出)
2. 检查暂存区状态(有内容→直接提交;无内容→先 git add .)
3. 分析代码变更
4. 生成符合规范的 commit message
5. 直接执行 `git commit -m "<message>"`(不需要用户确认)
6. 显示提交结果

---

## Commit 规范

### 基本格式

```
<type>(module): <description>
```

**格式说明**:
- `type`: 必填,提交类型(feat/fix/test/docs/refactor/chore/revert)
- `(module)`: 必填,模块名,必须用圆括号包裹
- `description`: 必填,提交描述,英文、动词开头、小写

### Type 快速参考

| Type | 用途 | 示例 |
|------|------|------|
| `feat` | 新功能/需求 | `feat(auth): add login module` |
| `fix` | 修复缺陷 | `fix(parser): resolve memory leak` |
| `test` | 测试改动 | `test(auth): add unit tests` |
| `docs` | 文档修改 | `docs(api): update documentation` |
| `refactor` | 代码重构 | `refactor(utils): extract helpers` |
| `revert` | 回滚提交 | `revert(auth): revert changes` |
| `chore` | 其他修改 | `chore(deps): update packages` |

详细格式说明见 [references/commit-format.md](references/commit-format.md)

---

## 工作流程

```
确认工作目录 → 安全检查 → 处理暂存区 → 分析变更
    → 识别 type 和模块 → 生成描述 → 组装 message → 执行提交 → 显示结果
```

### Type 识别逻辑

```
分析代码变更
  ↓
根据文件变更判断
  ├─ 新增文件 → feat
  ├─ 修改 bug → fix
  ├─ 测试文件 → test
  ├─ 文档文件 → docs
  └─ 其他 → chore
```

### 模块名提取逻辑

```
分析变更的文件路径
  ↓
单一模块?
  ├─ 是 → 提取模块名
  │      └─ src/auth/* → (auth)
  │      ├─ skills/k8s-troubleshoot/* → (skills)
  │      └─ docs/api.md → (docs)
  └─ 否 → 多个模块
         ├─ 使用主要模块名
         └─ 或使用通用名称 (如 core, common)
```

完整工作流程、决策树和示例见 [references/workflow-examples.md](references/workflow-examples.md)

---

## 安全检查

执行提交前自动检查:
1. 确认在 Git 仓库中(非 Git 目录直接报错退出)
2. 检查是否有冲突文件
3. 检查暂存区状态(为空则自动 `git add .`)

详细检查脚本和错误处理见 [references/safety-errors.md](references/safety-errors.md)

---

## 实际示例

### 示例 1: 新增 Skill

**输入**:
```
路径: /Users/chengfei/.openclaw

git status:
  new file: skills/k8s-troubleshoot/README.md
  new file: skills/k8s-troubleshoot/SKILL.md
```

**生成**:
```
feat(skills): add k8s troubleshoot skill
```

**执行**:
```bash
git commit -m "feat(skills): add k8s troubleshoot skill"
```

### 示例 2: 修复 Bug

**输入**:
```
git diff:
  - if (user == null)
  + if (user === null)
```

**生成**:
```
fix(auth): resolve null pointer exception
```

---

## 命令参考

```bash
# 基本格式
git commit -m "type(module): description"

# 查看相关
git log -1                          # 查看最近提交
git show HEAD                       # 查看提交详情
git status                          # 查看状态
git diff --cached --stat            # 查看变更统计
```

更多最佳实践、Type 选择指南、规范对照和提交后操作见 [references/best-practices.md](references/best-practices.md)
