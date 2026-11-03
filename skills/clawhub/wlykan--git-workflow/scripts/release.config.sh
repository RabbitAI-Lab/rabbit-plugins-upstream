#!/bin/bash
# release.config.sh - 发布脚本配置文件
# 在此文件中配置发布脚本的行为

# ==================== 基础配置 ====================

# 主分支名称（线上稳定版本）
MAIN_BRANCH="main"

# 开发分支名称（开发测试环境）
DEV_BRANCH="dev"

# 功能分支前缀（例如：feature/xxx）
FEATURE_BRANCH_PREFIX="feature/"

# 发布分支前缀（例如：release/xxx）
RELEASE_BRANCH_PREFIX="release/"

# 热修复分支前缀（例如：hotfix/xxx）
HOTFIX_BRANCH_PREFIX="hotfix/"

# ==================== 版本号配置 ====================

# 版本号格式（semantic versioning）
# major.minor.patch
# 例如：1.2.3
VERSION_FORMAT="MAJOR.MINOR.PATCH"

# 是否自动递增版本号
AUTO_INCREMENT_VERSION=false

# ==================== 合并策略 ====================

# 合并功能分支时是否使用 --no-ff（创建合并提交）
USE_NO_FF_MERGE=true

# 合并提交信息模板
# 可用变量：$VERSION, $BRANCH_NAME, $DATE
MERGE_COMMIT_TEMPLATE="合并功能分支: \$BRANCH_NAME"

# 发布提交信息模板
RELEASE_COMMIT_TEMPLATE="发布版本: \$VERSION"

# ==================== 标签配置 ====================

# 标签前缀
TAG_PREFIX="v"

# 是否自动创建标签
AUTO_CREATE_TAG=true

# 标签信息模板
# 可用变量：$VERSION, $DATE
TAG_MESSAGE_TEMPLATE="发布版本: \$VERSION"

# ==================== 分支清理配置 ====================

# 发布后是否自动删除发布分支
AUTO_DELETE_RELEASE_BRANCH=false

# 是否询问用户确认删除
ASK_BEFORE_DELETE=true

# ==================== 远程仓库配置 ====================

# 是否自动推送分支到远程
AUTO_PUSH=true

# 是否自动推送标签
AUTO_PUSH_TAGS=true

# ==================== 测试配置 ====================

# 合并前是否运行测试
RUN_TESTS_BEFORE_MERGE=false

# 测试命令
TEST_COMMAND="pnpm test"

# 构建命令（用于验证构建是否成功）
BUILD_COMMAND="pnpm build"

# ==================== 通知配置 ====================

# 是否在发布完成后发送通知
SEND_NOTIFICATION=false

# 通知方式（可选：email, slack, dingtalk）
NOTIFICATION_METHOD="email"

# 通知接收人
NOTIFICATION_RECIPIENTS=""

# ==================== 回滚配置 ====================

# 是否支持回滚操作
ENABLE_ROLLBACK=true

# 回滚时是否保留备份
KEEP_BACKUP_ON_ROLLBACK=true

# ==================== 日志配置 ====================

# 日志级别（可选：DEBUG, INFO, WARNING, ERROR）
LOG_LEVEL="INFO"

# 是否将日志输出到文件
LOG_TO_FILE=true

# 日志文件路径
LOG_FILE="release.log"

# ==================== 安全配置 ====================

# 是否强制要求干净的git工作区
REQUIRE_CLEAN_WORKSPACE=true

# 是否检查分支是否已经合并
CHECK_BRANCH_MERGED=true

# 是否允许在非main/dev分支上操作
ALLOW_OTHER_BRANCHES=false

# ==================== 自定义钩子 ====================

# 前置钩子脚本（在创建发布分支之前执行）
PRE_RELEASE_HOOK=""

# 后置钩子脚本（在发布完成之后执行）
POST_RELEASE_HOOK=""

# 合并前钩子脚本（在合并功能分支之前执行）
PRE_MERGE_HOOK=""

# 合并后钩子脚本（在合并功能分支之后执行）
POST_MERGE_HOOK=""