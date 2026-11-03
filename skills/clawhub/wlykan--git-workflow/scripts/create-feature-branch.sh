#!/bin/bash
# create-feature-branch.sh - 创建功能分支脚本
# 用法: ./create-feature-branch.sh <功能名>

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
    echo "创建功能分支脚本"
    echo ""
    echo "用法: $0 <功能名> [选项]"
    echo ""
    echo "参数:"
    echo "  功能名          功能分支名称（例如: user-management）"
    echo ""
    echo "选项:"
    echo "  --from-dev      从dev分支创建（默认）"
    echo "  --from-main     从main分支创建"
    echo "  --dry-run       模拟执行，不实际创建分支"
    echo "  --help          显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 user-management              # 从dev创建功能分支"
    echo "  $0 user-management --from-main  # 从main创建功能分支"
    echo "  $0 user-management --dry-run    # 模拟创建"
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

# 函数：创建功能分支
create_feature_branch() {
    local feature_name=$1
    local base_branch=$2
    local dry_run=$3
    
    local branch_name="feature/$feature_name"
    
    print_info "创建功能分支: $branch_name"
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
    
    # 创建功能分支
    print_info "创建分支: $branch_name"
    git checkout -b $branch_name
    
    print_success "功能分支创建成功: $branch_name"
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

FEATURE_NAME=""
BASE_BRANCH="dev"
DRY_RUN="false"

# 解析参数
while [ $# -gt 0 ]; do
    case $1 in
        --from-dev)
            BASE_BRANCH="dev"
            shift
            ;;
        --from-main)
            BASE_BRANCH="main"
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
            FEATURE_NAME=$1
            shift
            ;;
    esac
done

# 检查功能名是否提供
if [ -z "$FEATURE_NAME" ]; then
    print_error "请提供功能名"
    exit 1
fi

# 验证分支名
validate_branch_name $FEATURE_NAME

# 检查git状态
check_git_status

# 创建功能分支
create_feature_branch $FEATURE_NAME $BASE_BRANCH $DRY_RUN