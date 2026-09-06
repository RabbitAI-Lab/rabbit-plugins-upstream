#!/bin/bash
# release.sh - PMS-PC项目自动化发布脚本
# 用法: ./release.sh <版本号> [功能分支列表]
# 示例: ./release.sh 1.2.0 feature/A feature/C

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
    echo "PMS-PC项目自动化发布脚本"
    echo ""
    echo "用法: $0 <版本号> [选项] [功能分支列表] [命令]"
    echo ""
    echo "参数:"
    echo "  版本号          发布版本号，例如: 1.2.0 或 2026-08-06"
    echo "  功能分支列表    要合并的功能分支（可选）"
    echo "  命令            特殊命令（可选）:"
    echo "                  - publish: 合并到main分支"
    echo "                  - publish-with-tag: 合并到main并创建标签"
    echo ""
    echo "选项:"
    echo "  --create, -c    创建新的功能分支（如果不存在）"
    echo "  --help, -h      显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 1.2.0                          # 创建发布分支"
    echo "  $0 1.2.0 feature/A feature/C      # 合并已存在的功能分支"
    echo "  $0 1.2.0 --create feature/A feature/C  # 创建功能分支并合并"
    echo "  $0 2026-08-06 --create feat/row-width hotfix/row-edit  # 创建分支并合并"
    echo "  $0 1.2.0 publish                  # 合并到main"
    echo "  $0 1.2.0 publish-with-tag         # 合并并创建标签"
    echo ""
    echo "流程说明:"
    echo "  1. 创建发布分支"
    echo "  2. 合并确定要上线的功能分支"
    echo "  3. 测试发布分支"
    echo "  4. 合并到main分支并打标签"
    echo "  5. 合并回dev分支保持同步"
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
        print_error "有未提交的更改，请先提交或暂存"
        exit 1
    fi

    # 检查是否在正确的分支上（main或dev）
    current_branch=$(git branch --show-current)
    if [ "$current_branch" != "main" ] && [ "$current_branch" != "dev" ]; then
        print_warning "当前不在main或dev分支上，当前分支: $current_branch"
        read -p "是否继续? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "操作已取消"
            exit 0
        fi
    fi
}

# 函数：列出dev分支上的功能分支
list_feature_branches() {
    print_info "dev分支上的功能分支："
    echo "----------------------------------------"
    git branch --merged dev | grep "feature/" | sed 's/^[ ]*//' | while read branch; do
        echo "  $branch"
    done
    echo "----------------------------------------"
}

# 函数：创建发布分支
create_release_branch() {
    local version=$1
    local release_branch="release/$version"

    print_info "开始创建发布分支..."

    # 切换到main分支并更新
    print_info "切换到main分支并更新..."
    git checkout main
    
    # 尝试从远程更新（如果存在远程仓库）
    if git remote -v | grep -q "origin"; then
        git pull origin main
    else
        print_warning "未检测到远程仓库，跳过远程更新"
    fi

    # 检查发布分支是否已存在
    if git rev-parse --verify $release_branch > /dev/null 2>&1; then
        print_error "发布分支 $release_branch 已存在"
        exit 1
    fi

    # 创建发布分支
    print_info "创建发布分支: $release_branch"
    git checkout -b $release_branch

    print_success "发布分支创建完成: $release_branch"
}

# 函数：合并功能分支
merge_feature_branches() {
    local feature_branches=("$@")

    if [ ${#feature_branches[@]} -eq 0 ]; then
        print_info "未指定功能分支"
        list_feature_branches
        echo ""
        echo "请手动合并需要的功能分支，或重新运行脚本并指定功能分支"
        echo "例如: ./release.sh $(git branch --show-current | sed 's/release\///') feature/A feature/C"
        return 1
    fi

    print_info "合并功能分支: ${feature_branches[*]}"
    for branch in "${feature_branches[@]}"; do
        if git rev-parse --verify $branch > /dev/null 2>&1; then
            print_info "合并分支: $branch"
            git merge --no-ff $branch -m "合并功能分支: $branch"
        else
            print_error "分支 $branch 不存在"
            exit 1
        fi
    done

    print_success "功能分支合并完成"
}

# 函数：创建功能分支
create_feature_branches() {
    local feature_branches=("$@")

    if [ ${#feature_branches[@]} -eq 0 ]; then
        print_info "未指定功能分支"
        return 1
    fi

    print_info "创建功能分支: ${feature_branches[*]}"
    
    # 切换到dev分支作为基础
    print_info "切换到dev分支作为功能分支基础..."
    git checkout dev
    if git remote -v | grep -q "origin"; then
        git pull origin dev
    else
        print_warning "未检测到远程仓库，跳过远程更新"
    fi
    
    for branch in "${feature_branches[@]}"; do
        if git rev-parse --verify $branch > /dev/null 2>&1; then
            print_warning "分支 $branch 已存在，跳过创建"
        else
            print_info "创建分支: $branch"
            git checkout -b $branch
            # 创建一个初始提交（可选）
            # git commit --allow-empty -m "初始化分支: $branch"
            print_success "分支 $branch 创建完成"
        fi
    done
    
    # 切换回发布分支
    local current_branch=$(git branch --show-current)
    if [[ $current_branch == release/* ]]; then
        print_info "切换回发布分支: $current_branch"
        git checkout $current_branch
    else
        print_warning "当前不在发布分支上，需要手动切换"
    fi
}

# 函数：发布到main分支
publish_to_main() {
    local version=$1
    local create_tag=$2
    local release_branch="release/$version"

    print_info "开始发布到main分支..."

    # 检查发布分支是否存在
    if ! git rev-parse --verify $release_branch > /dev/null 2>&1; then
        print_error "发布分支 $release_branch 不存在"
        exit 1
    fi

    # 切换到main分支
    print_info "切换到main分支..."
    git checkout main
    
    # 尝试从远程更新（如果存在远程仓库）
    if git remote -v | grep -q "origin"; then
        git pull origin main
    else
        print_warning "未检测到远程仓库，跳过远程更新"
    fi

    # 合并发布分支
    print_info "合并发布分支到main..."
    git merge --no-ff $release_branch -m "发布版本: $version"

    # 创建标签（如果指定）
    if [ "$create_tag" = "true" ]; then
        print_info "创建版本标签: v$version"
        git tag -a "v$version" -m "发布版本: $version"
        
        # 尝试推送标签到远程（如果存在远程仓库）
        if git remote -v | grep -q "origin"; then
            git push origin "v$version"
        else
            print_warning "未检测到远程仓库，跳过标签推送"
        fi
    fi

    # 尝试推送到main（如果存在远程仓库）
    if git remote -v | grep -q "origin"; then
        print_info "推送到main分支..."
        git push origin main
    else
        print_warning "未检测到远程仓库，跳过远程推送"
    fi

    # 合并回dev分支
    print_info "合并回dev分支..."
    git checkout dev
    
    # 尝试从远程更新（如果存在远程仓库）
    if git remote -v | grep -q "origin"; then
        git pull origin dev
    else
        print_warning "未检测到远程仓库，跳过远程更新"
    fi
    
    git merge --no-ff $release_branch -m "同步发布版本: $version"
    
    # 尝试推送到dev（如果存在远程仓库）
    if git remote -v | grep -q "origin"; then
        git push origin dev
    else
        print_warning "未检测到远程仓库，跳过远程推送"
    fi

    print_success "发布完成！"

    # 询问是否删除发布分支
    echo ""
    if [ -t 0 ]; then
        # 交互式模式
        read -p "是否删除发布分支 $release_branch? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git branch -d $release_branch
            
            # 尝试删除远程分支（如果存在远程仓库）
            if git remote -v | grep -q "origin"; then
                git push origin --delete $release_branch
            else
                print_warning "未检测到远程仓库，跳过远程分支删除"
            fi
            
            print_info "已删除发布分支: $release_branch"
        else
            print_info "保留发布分支: $release_branch"
        fi
    else
        # 非交互式模式，自动保留发布分支
        print_info "非交互式模式，保留发布分支: $release_branch"
    fi
}

# 函数：显示当前状态
show_status() {
    local version=$1
    local release_branch="release/$version"

    print_info "当前状态："
    echo "----------------------------------------"
    echo "当前分支: $(git branch --show-current)"
    echo "版本号: $version"
    echo "发布分支: $release_branch"
    echo ""

    # 检查发布分支是否存在
    if git rev-parse --verify $release_branch > /dev/null 2>&1; then
        echo "发布分支状态: 已存在"
        echo "发布分支上的提交："
        git log --oneline main..$release_branch | head -10
    else
        echo "发布分支状态: 不存在"
    fi
    echo "----------------------------------------"
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

VERSION=$1
shift
COMMAND=""
FEATURE_BRANCHES=()
CREATE_NEW_BRANCHES=false

# 解析参数
for arg in "$@"; do
    if [ "$arg" = "publish" ] || [ "$arg" = "publish-with-tag" ]; then
        COMMAND=$arg
    elif [ "$arg" = "--create" ] || [ "$arg" = "-c" ]; then
        CREATE_NEW_BRANCHES=true
    elif [[ $arg == --* ]]; then
        # 其他选项，忽略
        print_warning "未知选项: $arg"
    else
        FEATURE_BRANCHES+=("$arg")
    fi
done

# 检查git状态
check_git_status

# 根据命令执行不同操作
case "$COMMAND" in
    "publish")
        print_info "执行发布命令..."
        publish_to_main $VERSION false
        ;;
    "publish-with-tag")
        print_info "执行带标签的发布命令..."
        publish_to_main $VERSION true
        ;;
    *)
        # 默认操作：创建发布分支并合并功能分支
        print_info "创建发布分支并合并功能分支..."
        create_release_branch $VERSION
        
        # 如果指定了--create参数，则先创建功能分支
        if [ "$CREATE_NEW_BRANCHES" = "true" ]; then
            create_feature_branches "${FEATURE_BRANCHES[@]}"
        fi
        
        merge_feature_branches "${FEATURE_BRANCHES[@]}"
        print_success "发布分支准备完成！"
        echo ""
        echo "下一步操作："
        echo "1. 在发布分支上进行测试"
        echo "2. 测试通过后运行: ./release.sh $VERSION publish"
        echo "3. 或者运行: ./release.sh $VERSION publish-with-tag"
        echo ""
        show_status $VERSION
        ;;
esac
