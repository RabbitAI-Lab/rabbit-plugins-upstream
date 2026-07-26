# 安全检查与错误处理

## 安全检查

执行提交前的自动检查:

```bash
# 1. 确认在 Git 仓库中(非 Git 目录直接报错退出)
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "❌ 错误:当前目录不是 Git 仓库"
  exit 1
fi

# 2. 检查是否有冲突文件
if git ls-files -u | grep -q .; then
  echo "❌ 错误:存在未解决的冲突文件"
  exit 1
fi

# 3. 检查暂存区状态
if [ -z "$(git diff --cached --name-only)" ]; then
  echo "i️  暂存区为空,自动执行 git add ."
  git add .
fi
```

---

## 错误处理

### 情形 1: 暂存区为空,自动添加

```
i️  暂存区为空,自动执行 git add .

当前状态:
Changes not staged for commit:
  modified:   src/app.js

→ 执行: git add .
→ 继续生成 commit message 并提交
```

### 错误 1: 非 Git 目录

```
❌ 错误:当前目录不是 Git 仓库!

当前路径: /Users/chengfei/Downloads

💡 解决方案:
1. 请指定 Git 仓库路径
2. 或切换到 Git 仓库目录后再试
```

### 错误 2: 无法识别模块

```
⚠️  警告:无法自动识别模块名

变更的文件:
  src/utils/helper.js
  src/auth/login.js
  docs/api.md

💡 将使用通用模块名: core
或者请手动指定模块名
```
