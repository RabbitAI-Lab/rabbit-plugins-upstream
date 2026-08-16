#!/bin/bash
# create-hotfix-branch.sh - 创建热修复分支脚本
# 用法: ./create-hotfix-branch.sh <问题描述>

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 函数：打印带颜色的消息
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 函数：显示帮助信息
show_help() {
    echo "创建热修复分支脚本"
    echo ""
    echo "用法: $0 <问题描述> [选项]"
    echo ""
    echo "参数:"
    echo "  问题描述        热修复分支名称（例如: login-crash-fix）"
    echo ""
    echo "选项:"
    echo "  --from-main     从main分支创建（默认）"
    echo "  --from-release  从最新的release分支创建"
    echo "  --dry-run       模拟执行，不实际创建分支"
    echo "  --help          显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 login-crash-fix              # 从main创建热修复分支"
    echo "  $0 login-crash-fix --from-release  # 从最新release创建"
    echo "  $0 login-crash-fix --dry-run    # 模拟创建"
}

# 函数：验证分支名
validate_branch_name() {
    local branch_name=$1
    
    # 检查分支名是否为空
    if [ -z "$branch_name" ]; then
        print_error "分支名不能为空"
        exit 1
    fi
    
    # 检查分支名格式
    if [[ ! $branch_name =~ ^[a-z0-9_-]+$ ]]; then
        print_error "分支名只能包含小写字母、数字、下划线和连字符"
        exit 1
    fi
    
    # 检查分支名长度
    if [ ${#branch_name} -gt 50 ]; then
        print_error "分支名长度不能超过50个字符"
        exit 1
    fi
}

# 函数：检查git状态
check_git_status() {
    # 检查是否在git仓库中
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "当前目录不是git仓库"
        exit 1
    fi
    
    # 检查是否有未提交的更改
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "有未提交的更改"
        read -p "是否继续? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "操作已取消"
            exit 0
        fi
    fi
}

# 函数：获取最新的release分支
get_latest_release_branch() {
    local latest_release=$(git branch -r | grep "release/" | sort -r | head -n 1 | sed 's/origin\///' | sed 's/^[ ]*//')
    
    if [ -z "$latest_release" ]; then
        print_error "未找到release分支"
        exit 1
    fi
    
    echo $latest_release
}

# 函数：创建热修复分支
create_hotfix_branch() {
    local issue_name=$1
    local base_branch=$2
    local dry_run=$3
    
    local branch_name="hotfix/$issue_name"
    
    print_info "创建热修复分支: $branch_name"
    print_info "基础分支: $base_branch"
    
    if [ "$dry_run" = "true" ]; then
        print_info "[模拟] 将执行以下操作:"
        echo "  1. 切换到 $base_branch 分支"
        echo "  2. 拉取最新代码"
        echo "  3. 创建分支: $branch_name"
        echo "  4. 切换到新分支"
        return 0
    fi
    
    # 检查分支是否已存在
    if git rev-parse --verify $branch_name > /dev/null 2>&1; then
        print_error "分支 $branch_name 已存在"
        exit 1
    fi
    
    # 切换到基础分支
    print_info "切换到 $base_branch 分支..."
    git checkout $base_branch
    
    # 拉取最新代码
    if git remote -v | grep -q "origin"; then
        print_info "拉取最新代码..."
        git pull origin $base_branch
    else
        print_warning "未检测到远程仓库，跳过拉取"
    fi
    
    # 创建热修复分支
    print_info "创建分支: $branch_name"
    git checkout -b $branch_name
    
    print_success "热修复分支创建成功: $branch_name"
    print_info "当前分支: $(git branch --show-current)"
}

# 主程序开始
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# 处理帮助参数
if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    show_help
    exit 0
fi

ISSUE_NAME=""
BASE_BRANCH="main"
DRY_RUN="false"

# 解析参数
while [ $# -gt 0 ]; do
    case $1 in
        --from-main)
            BASE_BRANCH="main"
            shift
            ;;
        --from-release)
            BASE_BRANCH=$(get_latest_release_branch)
            shift
            ;;
        --dry-run)
            DRY_RUN="true"
            shift
            ;;
        -*)
            print_error "未知选项: $1"
            exit 1
            ;;
        *)
            ISSUE_NAME=$1
            shift
            ;;
    esac
done

# 检查问题描述是否提供
if [ -z "$ISSUE_NAME" ]; then
    print_error "请提供问题描述"
    exit 1
fi

# 验证分支名
validate_branch_name $ISSUE_NAME

# 检查git状态
check_git_status

# 创建热修复分支
create_hotfix_branch $ISSUE_NAME $BASE_BRANCH $DRY_RUN