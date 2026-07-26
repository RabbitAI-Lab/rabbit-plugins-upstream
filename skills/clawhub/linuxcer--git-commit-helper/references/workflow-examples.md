# 工作流程与示例

## 完整步骤

```
步骤 1: 确认工作目录
  ├─ 用户提供了路径 → cd 到该路径
  └─ 未提供路径 → 使用当前工作目录
  ↓
步骤 2: 安全检查
  ├─ 确认在 Git 仓库中(非 Git 目录 → 报错退出)
  ├─ 检查是否有冲突文件
  └─ 检查暂存区状态
  ↓
步骤 3: 处理暂存区
  ├─ git diff --cached --stat 有输出 → 直接继续
  └─ git diff --cached --stat 无输出 → 执行 git add .
  ↓
步骤 4: 分析代码变更
  ├─ git status
  ├─ git diff --cached --stat
  └─ git diff --cached
  ↓
步骤 5: 识别变更类型
  ├─ 新增文件 → feat
  ├─ Bug 修复相关 → fix
  ├─ 测试文件 → test
  ├─ 文档文件 → docs
  └─ 其他 → chore
  ↓
步骤 6: 提取模块名
  ├─ 从文件路径提取
  ├─ 例如: src/auth/login.js → auth
  └─ 例如: skills/k8s-troubleshoot/ → (skills)
  ↓
步骤 7: 生成描述
  ├─ 分析 diff 内容
  ├─ 总结主要变更
  └─ 使用英文、动词开头、小写
  ↓
步骤 8: 组装 Commit Message
  └─ <type>(module): <description>
  ↓
步骤 9: 直接执行提交
  └─ git commit -m "<message>"
  ↓
步骤 10: 显示结果
  ├─ Commit Hash
  ├─ 文件统计
  └─ 下一步建议
```

---

## 决策树

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

---

## 实际示例

### 示例 1: 新增 K8s Troubleshoot Skill

**输入**:
```
路径: /Users/chengfei/.openclaw

git status:
  new file:   skills/k8s-troubleshoot/README.md
  new file:   skills/k8s-troubleshoot/SKILL.md
```

**分析**:
- 类型: 新增文件 → `feat`
- 模块: `skills` (必须用圆括号)
- 描述: 基于文件名和 diff 内容

**生成的 Commit Message**:
```
feat(skills): add k8s troubleshoot skill
```

**执行命令**:
```bash
git commit -m "feat(skills): add k8s troubleshoot skill"
```

**输出**:
```
[main abc1234] feat(skills): add k8s troubleshoot skill
 2 files changed, 969 insertions(+)
 create mode 100644 skills/k8s-troubleshoot/README.md
 create mode 100644 skills/k8s-troubleshoot/SKILL.md
```

---

### 示例 2: 修复认证模块 Bug

**输入**:
```
路径: /Users/dev/myapp

git diff:
  - if (user == null)
  + if (user === null)
```

**生成的 Commit Message**:
```
fix(auth): resolve null pointer exception
```

---

### 示例 3: 多次提交

**第一次提交**:
```
feat(auth): implement login validation
```

**第二次提交**:
```
feat(auth): add session management
```

**第三次提交(最后)**:
```
feat(auth): complete user authentication module
```

---

### 示例 4: 文档更新

**输入**:
```
git status:
  modified: docs/api/authentication.md
```

**生成的 Commit Message**:
```
docs(api): update authentication documentation
```

---

### 示例 5: 测试改动

**输入**:
```
git status:
  new file: tests/auth/login.test.js
```

**生成的 Commit Message**:
```
test(auth): add unit tests for login module
```

---

## 用户交互流程

### 完整对话示例

```
用户: "帮我提交 /Users/chengfei/.openclaw 项目"

AI:
1️⃣ 正在检查代码变更...

$ cd /Users/chengfei/.openclaw
$ git status

Changes to be committed:
  new file:   skills/k8s-troubleshoot/README.md
  new file:   skills/k8s-troubleshoot/SKILL.md

2️⃣ 正在分析变更...

$ git diff --cached --stat
 skills/k8s-troubleshoot/README.md | 160 ++++++++
 skills/k8s-troubleshoot/SKILL.md  | 808 ++++++++++++++++++++++++++++++++++++++
 2 files changed, 968 insertions(+)

3️⃣ 识别的模块: skills

4️⃣ 直接提交...

$ git commit -m "feat(skills): add k8s troubleshoot skill"

✅ 提交成功!

[main abc1234] feat(skills): add k8s troubleshoot skill
 2 files changed, 968 insertions(+)
 create mode 100644 skills/k8s-troubleshoot/README.md
 create mode 100644 skills/k8s-troubleshoot/SKILL.md

📊 提交详情:
- Commit Hash: abc1234
- 分支: main
- 文件变更: 2 个文件,968 行新增

🔗 下一步建议:
- 推送到远程: git push origin main
- 查看提交: git show abc1234
- 查看历史: git log --oneline -5
```
