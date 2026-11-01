@echo off
REM release.bat - Windows版本的自动化发布脚本
REM 用法: release.bat <版本号> [功能分支列表]
REM 示例: release.bat 1.2.0 feature/A feature/C

setlocal enabledelayedexpansion

REM 颜色代码
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "NC=[0m"

REM 函数：打印带颜色的消息
call :print_info "PMS-PC项目自动化发布脚本"
call :print_info "========================================"

REM 检查参数
if "%~1"=="" (
    call :show_help
    exit /b 1
)

set "VERSION=%~1"
shift

REM 解析参数
set "COMMAND="
set "FEATURE_BRANCHES="

:parse_args
if "%~1"=="" goto :end_parse_args
if "%~1"=="publish" (
    set "COMMAND=publish"
) else if "%~1"=="publish-with-tag" (
    set "COMMAND=publish-with-tag"
) else (
    if defined FEATURE_BRANCHES (
        set "FEATURE_BRANCHES=!FEATURE_BRANCHES! %~1"
    ) else (
        set "FEATURE_BRANCHES=%~1"
    )
)
shift
goto :parse_args

:end_parse_args

REM 检查git状态
call :check_git_status

REM 根据命令执行不同操作
if "%COMMAND%"=="publish" (
    call :print_info "执行发布命令..."
    call :publish_to_main "%VERSION%" "false"
) else if "%COMMAND%"=="publish-with-tag" (
    call :print_info "执行带标签的发布命令..."
    call :publish_to_main "%VERSION%" "true"
) else (
    call :print_info "创建发布分支并合并功能分支..."
    call :create_release_branch "%VERSION%"
    if defined FEATURE_BRANCHES (
        call :merge_feature_branches "%FEATURE_BRANCHES%"
    ) else (
        call :print_info "未指定功能分支"
        call :list_feature_branches
        call :print_info "请手动合并需要的功能分支，或重新运行脚本并指定功能分支"
    )
    call :print_success "发布分支准备完成！"
    call :show_status "%VERSION%"
)

exit /b 0

REM ==================== 函数定义 ====================

:show_help
call :print_info "用法: %~nx0 <版本号> [功能分支列表] [命令]"
call :print_info ""
call :print_info "参数:"
call :print_info "  版本号          发布版本号，例如: 1.2.0"
call :print_info "  功能分支列表    要合并的功能分支（可选）"
call :print_info "  命令            特殊命令（可选）:"
call :print_info "                  - publish: 合并到main分支"
call :print_info "                  - publish-with-tag: 合并到main并创建标签"
call :print_info ""
call :print_info "示例:"
call :print_info "  %~nx0 1.2.0                          # 创建发布分支"
call :print_info "  %~nx0 1.2.0 feature/A feature/C      # 合并指定功能"
call :print_info "  %~nx0 1.2.0 publish                  # 合并到main"
call :print_info "  %~nx0 1.2.0 publish-with-tag         # 合并并创建标签"
goto :eof

:check_git_status
REM 检查是否在git仓库中
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    call :print_error "当前目录不是git仓库"
    exit /b 1
)

REM 检查是否有未提交的更改
for /f "tokens=*" %%i in ('git status --porcelain') do (
    call :print_error "有未提交的更改，请先提交或暂存"
    exit /b 1
)

REM 检查是否在正确的分支上
for /f "tokens=*" %%i in ('git branch --show-current') do set "CURRENT_BRANCH=%%i"
if not "%CURRENT_BRANCH%"=="main" if not "%CURRENT_BRANCH%"=="dev" (
    call :print_warning "当前不在main或dev分支上，当前分支: %CURRENT_BRANCH%"
    set /p "CONTINUE=是否继续? (y/N): "
    if /i not "!CONTINUE!"=="y" (
        call :print_info "操作已取消"
        exit /b 0
    )
)
goto :eof

:list_feature_branches
call :print_info "dev分支上的功能分支："
echo ----------------------------------------
for /f "tokens=*" %%i in ('git branch --merged dev ^| findstr "feature/"') do (
    echo   %%i
)
echo ----------------------------------------
goto :eof

:create_release_branch
set "VERSION=%~1"
set "RELEASE_BRANCH=release/%VERSION%"

call :print_info "开始创建发布分支..."

REM 切换到main分支并更新
call :print_info "切换到main分支并更新..."
git checkout main
git pull origin main

REM 检查发布分支是否已存在
git rev-parse --verify %RELEASE_BRANCH% >nul 2>&1
if not errorlevel 1 (
    call :print_error "发布分支 %RELEASE_BRANCH% 已存在"
    exit /b 1
)

REM 创建发布分支
call :print_info "创建发布分支: %RELEASE_BRANCH%"
git checkout -b %RELEASE_BRANCH%

call :print_success "发布分支创建完成: %RELEASE_BRANCH%"
goto :eof

:merge_feature_branches
set "FEATURE_BRANCHES=%~1"

call :print_info "合并功能分支: %FEATURE_BRANCHES%"
for %%i in (%FEATURE_BRANCHES%) do (
    git rev-parse --verify %%i >nul 2>&1
    if errorlevel 1 (
        call :print_error "分支 %%i 不存在"
        exit /b 1
    )
    call :print_info "合并分支: %%i"
    git merge --no-ff %%i -m "合并功能分支: %%i"
)

call :print_success "功能分支合并完成"
goto :eof

:publish_to_main
set "VERSION=%~1"
set "CREATE_TAG=%~2"
set "RELEASE_BRANCH=release/%VERSION%"

call :print_info "开始发布到main分支..."

REM 检查发布分支是否存在
git rev-parse --verify %RELEASE_BRANCH% >nul 2>&1
if errorlevel 1 (
    call :print_error "发布分支 %RELEASE_BRANCH% 不存在"
    exit /b 1
)

REM 切换到main分支
call :print_info "切换到main分支..."
git checkout main
git pull origin main

REM 合并发布分支
call :print_info "合并发布分支到main..."
git merge --no-ff %RELEASE_BRANCH% -m "发布版本: %VERSION%"

REM 创建标签（如果指定）
if "%CREATE_TAG%"=="true" (
    call :print_info "创建版本标签: v%VERSION%"
    git tag -a "v%VERSION%" -m "发布版本: %VERSION%"
    git push origin "v%VERSION%"
)

REM 推送到main
call :print_info "推送到main分支..."
git push origin main

REM 合并回dev分支
call :print_info "合并回dev分支..."
git checkout dev
git pull origin dev
git merge --no-ff %RELEASE_BRANCH% -m "同步发布版本: %VERSION%"
git push origin dev

call :print_success "发布完成！"

REM 询问是否删除发布分支
set /p "DELETE_BRANCH=是否删除发布分支 %RELEASE_BRANCH%? (y/N): "
if /i "%DELETE_BRANCH%"=="y" (
    git branch -d %RELEASE_BRANCH%
    git push origin --delete %RELEASE_BRANCH%
    call :print_info "已删除发布分支: %RELEASE_BRANCH%"
)
goto :eof

:show_status
set "VERSION=%~1"
set "RELEASE_BRANCH=release/%VERSION%"

call :print_info "当前状态："
echo ----------------------------------------
echo 当前分支: %CURRENT_BRANCH%
echo 版本号: %VERSION%
echo 发布分支: %RELEASE_BRANCH%
echo.

REM 检查发布分支是否存在
git rev-parse --verify %RELEASE_BRANCH% >nul 2>&1
if not errorlevel 1 (
    echo 发布分支状态: 已存在
    echo 发布分支上的提交：
    git log --oneline main..%RELEASE_BRANCH%
) else (
    echo 发布分支状态: 不存在
)
echo ----------------------------------------
goto :eof

:print_info
echo %BLUE%[INFO]%NC% %~1
goto :eof

:print_success
echo %GREEN%[SUCCESS]%NC% %~1
goto :eof

:print_warning
echo %YELLOW%[WARNING]%NC% %~1
goto :eof

:print_error
echo %RED%[ERROR]%NC% %~1
goto :eof