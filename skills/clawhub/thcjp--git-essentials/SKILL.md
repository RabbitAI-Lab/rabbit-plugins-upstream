---
name: git-essentials
slug: git-essentials
displayName: "Git Essentials"
version: "1.0.1"
summary: "版本控制/分支/协作的Git必备命令与工作流"
description: "Git版本控制必备命令与团队协作工作流技能，系统覆盖本地初始化配置、暂存提交、分支管理与切换、合并冲突解决、远程仓库同步、历史日志检索、提交回退撤销、标签发布、变基整理、储藏恢复、子模块与清理等核心场景，深度适配Gitee与GitCode等国内代码托管平台，提供从ERR-001到ERR-008的结构化错误码表与常见问题FAQ解答，适用于日常提交、特性分支协作、紧急修复与历史整理等多种任务。"
license: "MIT"
tools:
  - read
---

# Git Essentials

Git 版本控制必备命令与团队协作工作流技能。本技能将说明文字中文化，保留英文 git 命令原貌，并适配 Gitee、GitCode 等国内代码托管平台，提供结构化错误码与常见问题解答，帮助开发者高效完成日常提交、分支管理与冲突处理。

## 触发条件

当用户表达以下意图时，本技能应被触发：

| 触发类别 | 触发词示例 |
|:---------|:-----------|
| 版本控制基础 | "git命令"、"git"、"版本控制"、"提交代码"、"commit" |
| 分支管理 | "分支管理"、"新建分支"、"切换分支"、"branch"、"merge" |
| 合并冲突 | "合并冲突"、"解决冲突"、"冲突解决"、"merge conflict" |
| 远程同步 | "推送代码"、"拉取代码"、"push"、"pull"、"远程仓库" |
| 历史回溯 | "查看历史"、"回退提交"、"撤销提交"、"git log"、"revert" |
| 标签发布 | "打标签"、"发布版本"、"tag"、"release" |
| 变基整理 | "变基"、"整理提交"、"rebase"、"压缩提交" |

说明：当用户提及上述任一关键词，或请求执行 git 操作、解释 git 命令、排查 git 报错时，应激活本技能并依据后续章节给出的命令与流程响应。

## 能力边界

### 覆盖范围

- 日常 git 命令操作：初始化、配置、暂存、提交、查看变更
- 分支与合并：创建、切换、删除、合并、冲突标记查询
- 远程协作：远程仓库管理、推送、拉取、抓取、同步 fork
- 历史与回溯：日志查询、blame、二分查找、提交回退与撤销
- 高级操作：变基、挑选提交、子模块、清理、标签、储藏
- 国内平台适配：Gitee、GitCode 等代码托管平台的远程操作示例

### 不支持的内容

| 不支持项 | 原因 | 建议替代 |
|:---------|:-----|:---------|
| Git LFS 大文件存储 | 需独立扩展与平台账户配置 | 参考 Gitee/GitCode 官方 LFS 文档 |
| CI/CD 流水线配置 | 属于持续集成领域，超出 git 命令范畴 | 使用平台内置 CI 或独立 DevOps 技能 |
| 仓库托管平台账号注册 | 涉及平台账户体系与安全验证 | 前往 Gitee/GitCode 官网注册 |
| 图形化客户端操作 | 本技能聚焦命令行 | 使用 Sourcetree、IDE 内置 Git |
| 钩子（hook）脚本开发 | 属于脚本编程范畴 | 参考 git-scm.com 钩子文档 |
| 仓库数据迁移工具 | 涉及专用迁移方案 | 使用平台官方导入功能 |

## 初始配置

初始化全局身份信息与本地仓库，是使用 git 的首要步骤。

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git init
git clone https://gitee.com/user/repo.git
git clone https://gitcode.com/user/repo.git custom-name
```

## 基础工作流

### 暂存与提交

将工作区变更加入暂存区并生成提交记录。

```bash
git status
git add file.txt
git add .
git add -A  # 包含删除在内的全部变更
git commit -m "Commit message"
git commit -am "Message"
git commit --amend -m "New message"
git commit --amend --no-edit  # 保留原提交信息
```

### 查看变更

对比工作区、暂存区与历史提交之间的差异。

```bash
git diff
git diff --staged
git diff file.txt
git diff commit1 commit2
```

## 分支与合并

### 分支管理

创建、切换、删除与重命名分支，支持现代 switch 命令。

```bash
git branch
git branch -a  # 含远程分支
git branch feature-name
git checkout feature-name
git switch feature-name  # 现代替代写法
git checkout -b feature-name
git switch -c feature-name
git branch -d branch-name
git branch -D branch-name  # 强制删除
git branch -m old-name new-name
```

### 合并操作

将分支整合到当前分支，并处理合并冲突标记。

```bash
git merge feature-name
git merge --no-ff feature-name
git merge --abort
git diff --name-only --diff-filter=U
```

## 远程操作

### 远程仓库管理

管理远程地址，适配 Gitee、GitCode 等国内平台。

```bash
git remote -v
# 添加 Gitee 远程
git remote add origin https://gitee.com/user/repo.git
# 添加 GitCode 远程
git remote add gitcode https://gitcode.com/user/repo.git
# 同时配置多平台（origin 走 Gitee，mirror 走 GitCode）
git remote set-url origin https://gitee.com/user/repo.git
git remote add mirror https://gitcode.com/user/repo.git
git remote remove origin
```

### 与远程同步

抓取、拉取与推送远程分支变更。

```bash
git fetch origin
git pull
git pull --rebase
git push
git push -u origin branch-name
git push --force-with-lease
```

## 历史与日志

### 查看历史

按需检索提交历史，支持图形化展示。

```bash
git log
git log --oneline
git log --graph --oneline --all
git log -5
git log --author="Name"
git log --since="2 weeks ago"
git log --until="2024-01-01"
git log -- file.txt
```

### 搜索历史

按关键字或代码变更定位历史提交。

```bash
git log --grep="bug fix"
git log -S "function_name"
git blame file.txt
git bisect start
git bisect bad
git bisect good commit-hash
```

## 撤销变更

### 工作区

丢弃工作区未暂存的修改。

```bash
git restore file.txt
git checkout -- file.txt  # 旧写法
git restore .
```

### 暂存区

将已暂存变更退回工作区。

```bash
git restore --staged file.txt
git reset HEAD file.txt  # 旧写法
git reset
```

### 提交

回退或撤销已生成的提交。

```bash
git reset --soft HEAD~1
git reset --hard HEAD~1
git revert commit-hash
git reset --hard commit-hash
```

## 储藏工作区

临时保存未完成变更，便于切换上下文。

```bash
git stash
git stash save "Work in progress"
git stash list
git stash apply
git stash pop
git stash apply stash@{2}
git stash drop stash@{0}
git stash clear
```

## 变基

将分支提交重新整合到目标基线，便于线性历史。

```bash
git rebase main
git rebase -i HEAD~3
git rebase --continue
git rebase --skip
git rebase --abort
```

## 标签

标记发布版本节点，便于检索与发布。

```bash
git tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
git tag v1.0.0 commit-hash
git push origin v1.0.0
git push --tags
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## 高级操作

### 挑选提交

将指定提交单独应用到当前分支。

```bash
git cherry-pick commit-hash
git cherry-pick -n commit-hash
```

### 子模块

在仓库中嵌入并跟踪外部仓库。

```bash
git submodule add https://gitee.com/user/submodule.git path/
git submodule init
git submodule update
git clone --recursive https://gitcode.com/user/repo.git
```

### 清理

删除未跟踪文件与目录。

```bash
git clean -n
git clean -f
git clean -fd
git clean -fdx
```

## 常用工作流

特性分支工作流：

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
git checkout main
git pull
git branch -d feature/new-feature
```

热修复工作流：

```bash
git checkout main
git pull
git checkout -b hotfix/critical-bug
git commit -am "Fix critical bug"
git push -u origin hotfix/critical-bug
git checkout main && git pull
```

同步 fork 仓库：

```bash
git remote add upstream https://gitee.com/upstream/repo.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## 别名配置

在 `~/.gitconfig` 中配置常用别名以提升效率。

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all
    amend = commit --amend --no-edit
```

## 实践建议

- 频繁提交，后续再用交互式变基整理
- 撰写含义清晰的提交信息
- 使用 `.gitignore` 排除无需跟踪的文件
- 切勿对共享分支执行强制推送
- 开始工作前先拉取最新代码
- 合并前对特性分支执行变基
- 使用 `--force-with-lease` 替代 `--force`

## 错误处理

结构化错误码表，覆盖常见 git 故障场景，给出原因与处理指引。

| 错误码 | 场景 | 原因 | 处理方式 |
|:-------|:-----|:-----|:---------|
| ERR-001 | 合并冲突 | 同一行被多方修改，无法自动合并 | `git status` 定位冲突文件，手动编辑后 `git add` 再 `git commit` |
| ERR-002 | 权限拒绝 | 远程仓库认证失败或无写权限 | 检查 SSH 密钥或访问令牌，确认账号对该仓库具备写权限 |
| ERR-003 | 网络中断 | 推送或拉取时连接超时或不可达 | 检查网络后重试，国内建议优先使用 Gitee/GitCode 镜像 |
| ERR-004 | 大文件推送失败 | 单文件超出平台限制或未启用 LFS | 拆分提交或启用 Git LFS，参考平台大文件文档 |
| ERR-005 | 非快进推送被拒 | 远程已有他人新提交 | `git pull --rebase` 整合后再推送 |
| ERR-006 | 提交信息为空 | 未填写提交信息或被钩子拦截 | 补充有意义的提交信息后重新提交 |
| ERR-007 | 远程仓库不存在 | 远程地址拼写错误或已被删除 | `git remote -v` 核对地址，使用 `git remote set-url` 更正 |
| ERR-008 | 变基因脏工作区中止 | 工作区有未提交变更 | `git stash` 暂存后重试变基，完成后再 `git stash pop` |

通用错误排查流程：先 `git status` 查看状态，再 `git log` 核对历史，最后依据错误码表对应处理。

## 常见问题

### Q1: 如何解决合并冲突？

A: 执行 `git status` 列出冲突文件，打开文件查找 `<<<<<<<`、`=======`、`>>>>>>>` 标记，手动保留所需内容并删除标记，随后 `git add <文件>` 标记已解决，最后 `git commit` 完成合并。也可使用 `git merge --abort` 放弃本次合并。

### Q2: 如何回退最近一次提交？

A: 若尚未推送，使用 `git reset --soft HEAD~1` 回退但保留变更在工作区；若已推送且希望反向提交，使用 `git revert HEAD` 生成一次撤销提交，避免改写公共历史。

### Q3: 如何删除远程分支？

A: 执行 `git push origin --delete branch-name` 删除远程分支，本地分支用 `git branch -d branch-name` 清理。删除前确认无协作者依赖该分支。

### Q4: 何时使用 force-with-lease 而非 force？

A: 推荐始终使用 `git push --force-with-lease`。它会在远程有他人新提交时拒绝推送，避免覆盖他人工作；而 `--force` 会无条件覆盖，仅适合个人独占分支。

### Q5: 如何撤销已推送的提交？

A: 已推送至共享分支的提交，使用 `git revert commit-hash` 生成反向提交再推送；仅在个人独占分支才可考虑 `git reset --hard` 后强制推送。

### Q6: 如何合并多个提交为一个？

A: 执行 `git rebase -i HEAD~3` 进入交互式变基，将后续提交标记为 `squash` 或 `fixup`，保存后编辑合并信息，完成后 `git push --force-with-lease` 更新远程。

### Q7: 如何恢复误删的分支？

A: 使用 `git reflog` 查找该分支最后一次的提交哈希，再执行 `git checkout -b branch-name <commit-hash>` 重新创建分支。reflog 默认保留约 90 天。

### Q8: 如何修改历史提交的作者信息？

A: 使用 `git rebase -i <commit>^` 将目标提交标记为 `edit`，到达时执行 `git commit --amend --author="Name <email>"`，再 `git rebase --continue`。已推送的历史需强制推送。

## 文档参考

- 官方文档：https://git-scm.com/doc
- Pro Git 在线书：https://git-scm.com/book
- 可视化 Git 指南：https://marklodato.github.io/visual-git-guide/
- Gitee 帮助中心：https://gitee.com/help
- GitCode 文档：https://gitcode.com/docs

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Git 版本**: 建议 2.20 及以上，以支持 switch / restore 等现代命令

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Git 客户端 | 命令行工具 | 执行命令时必需 | 系统包管理器安装 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)
- 推送至 Gitee/GitCode 时需配置对应平台的访问令牌或 SSH 密钥

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 日常提交 | 文件变更与提交信息 | 暂存与提交命令序列 |
| 分支协作 | 分支名称与操作意图 | 分支创建、切换、删除命令 |
| 冲突处理 | 冲突文件 | 冲突解决步骤与命令 |

**不适用于**：需要人工判断的复杂决策场景、CI/CD 流水线设计、Git LFS 大文件存储配置

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 依据触发条件判断是否激活本技能
3. 对照能力边界确认任务在覆盖范围内
4. 选择对应章节命令或工作流执行
5. 遇到报错时参考错误处理章节按错误码处置
6. 疑问时查阅常见问题章节

## 已知限制

- 需要 LLM 支持，无 LLM 环境无法使用
- 不支持 Git LFS、CI/CD 配置与图形化客户端操作
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
