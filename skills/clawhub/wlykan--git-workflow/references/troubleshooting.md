# Git常见问题处理

## 目录
1. [分支相关问题](#分支相关问题)
2. [合并冲突问题](#合并冲突问题)
3. [提交历史问题](#提交历史问题)
4. [远程仓库问题](#远程仓库问题)
5. [性能优化问题](#性能优化问题)

## 分支相关问题

### 1. 分支创建失败
**问题**：`fatal: A branch named 'xxx' already exists`

**解决方案**：
```bash
# 查看所有分支
git branch

# 删除本地分支
git branch -d [分支名]

# 强制删除分支（如果分支未合并）
git branch -D [分支名]

# 重新创建分支
git checkout -b [分支名]
```

### 2. 分支切换失败
**问题**：`error: Your local changes to the following files would be overwritten`

**解决方案**：
```bash
# 方案1：暂存更改
git stash
git checkout [分支名]
git stash pop

# 方案2：提交更改
git add .
git commit -m "chore: 暂存当前更改"
git checkout [分支名]
```

### 3. 分支删除失败
**问题**：`error: Cannot delete branch 'xxx' checked out at`

**解决方案**：
```bash
# 切换到其他分支
git checkout main

# 删除分支
git branch -d [分支名]
```

## 合并冲突问题

### 1. 合并冲突检测
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

## 提交历史问题

### 1. 修改最后一次提交
```bash
# 修改提交信息
git commit --amend -m "新的提交信息"

# 添加遗漏的文件
git add [文件名]
git commit --amend --no-edit
```

### 2. 整理提交历史
```bash
# 交互式变基，整理最近5次提交
git rebase -i HEAD~5

# 在编辑器中选择操作：
# pick = 保留提交
# squash = 合并提交
# reword = 修改提交信息
# drop = 删除提交
```

### 3. 撤销提交
```bash
# 撤销最后一次提交，保留更改
git reset --soft HEAD~1

# 撤销最后一次提交，丢弃更改
git reset --hard HEAD~1

# 撤销多次提交
git reset --hard HEAD~3
```

## 远程仓库问题

### 1. 推送失败
**问题**：`! [rejected] main -> main (non-fast-forward)`

**解决方案**：
```bash
# 方案1：强制推送（谨慎使用）
git push origin main --force

# 方案2：先拉取再推送
git pull origin main
git push origin main
```

### 2. 拉取失败
**问题**：`error: Your local changes to the following files would be overwritten`

**解决方案**：
```bash
# 方案1：暂存本地更改
git stash
git pull origin main
git stash pop

# 方案2：放弃本地更改
git reset --hard origin/main
```

### 3. 远程分支删除
```bash
# 删除远程分支
git push origin --delete [分支名]

# 清理本地对远程分支的引用
git fetch --prune
```

## 性能优化问题

### 1. 大文件处理
```bash
# 使用Git LFS管理大文件
git lfs install
git lfs track "*.psd"
git lfs track "*.zip"
git add .gitattributes
```

### 2. 仓库瘦身
```bash
# 清理无用对象
git gc

# 深度清理
git gc --aggressive --prune=now

# 查看仓库大小
git count-objects -v
```

### 3. 子模块管理
```bash
# 初始化子模块
git submodule init
git submodule update

# 更新子模块到最新
git submodule update --remote --merge

# 删除子模块
git submodule deinit [子模块路径]
git rm [子模块路径]
rm -rf .git/modules/[子模块路径]
```

## 工具和脚本

### 1. 分支检查脚本
```bash
#!/bin/bash
# scripts/check-branches.sh

echo "检查分支命名规范..."

# 检查所有本地分支
for branch in $(git branch | grep -v '^\*' | sed 's/^[ ]*//'); do
    if [[ ! $branch =~ ^(main|dev|feature/|release/|hotfix/) ]]; then
        echo "❌ 不符合规范的分支: $branch"
    fi
done
```

### 2. 清理已合并分支
```bash
#!/bin/bash
# scripts/cleanup-branches.sh

echo "清理已合并的分支..."

# 删除已合并到dev的分支
git branch --merged dev | grep -v '^\*' | grep -v 'main\|dev' | xargs git branch -d

# 删除已合并到main的分支
git branch --merged main | grep -v '^\*' | grep -v 'main\|dev' | xargs git branch -d
```

### 3. 分支状态报告
```bash
#!/bin/bash
# scripts/branch-status.sh

echo "分支状态报告"
echo "============"

echo "当前分支: $(git branch --show-current)"
echo "本地分支数量: $(git branch | wc -l)"
echo "远程分支数量: $(git branch -r | wc -l)"

echo ""
echo "最近提交:"
git log --oneline -10