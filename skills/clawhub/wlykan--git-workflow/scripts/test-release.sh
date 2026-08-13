#!/bin/bash
# test-release.sh - 测试发布脚本的模拟环境
# 这个脚本创建一个模拟的开发环境来测试发布流程

set -e

echo "=========================================="
echo "创建测试环境来验证发布脚本"
echo "=========================================="

# 1. 创建测试目录
TEST_DIR="/tmp/pms-pc-test-$(date +%Y%m%d%H%M%S)"
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"

echo "测试目录: $TEST_DIR"

# 2. 初始化git仓库
git init
git config user.email "test@example.com"
git config user.name "Test User"

# 3. 创建初始文件
echo "# PMS-PC测试项目" > README.md
git add README.md
git commit -m "初始提交"

# 4. 创建main分支
git checkout -b main

# 5. 创建dev分支
git checkout -b dev
echo "开发环境配置" > dev-config.txt
git add dev-config.txt
git commit -m "添加开发环境配置"

# 6. 创建功能分支
git checkout -b feature/A
echo "功能A的实现" > feature-a.txt
git add feature-a.txt
git commit -m "实现功能A"

git checkout -b feature/B
echo "功能B的实现" > feature-b.txt
git add feature-b.txt
git commit -m "实现功能B"

git checkout -b feature/C
echo "功能C的实现" > feature-c.txt
git add feature-c.txt
git commit -m "实现功能C"

# 7. 合并功能分支到dev
git checkout dev
git merge --no-ff feature/A -m "合并功能A"
git merge --no-ff feature/B -m "合并功能B"
git merge --no-ff feature/C -m "合并功能C"

# 8. 切换回main
git checkout main

echo ""
echo "测试环境创建完成！"
echo "目录: $TEST_DIR"
echo ""
echo "现在可以测试发布脚本了："
echo "cd $TEST_DIR"
echo "../scripts/release.sh 1.0.0 feature/A feature/C"
echo ""
echo "或者测试其他命令："
echo "../scripts/release.sh --help"
echo "../scripts/release.sh 1.0.0"
echo "../scripts/release.sh 1.0.0 publish"
echo "../scripts/release.sh 1.0.0 publish-with-tag"