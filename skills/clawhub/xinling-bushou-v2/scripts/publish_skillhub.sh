#!/bin/bash
#
# 发布到 SkillHub 的打包脚本
# SkillHub 服务端不允许无扩展名文件，需把 scripts/xinling 复制为 scripts/xinling.py
# 用法: ./scripts/publish_skillhub.sh [--dry-run]
#
set -euo pipefail

PROJ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAGE="$(mktemp -d)"
DRY=""
[ "${1:-}" = "--dry-run" ] && DRY="--dry-run"

trap 'rm -rf "$STAGE"' EXIT

echo "[1/3] 构建 SkillHub 合规目录..."
# 复制源码（排除 .git / __pycache__ / 运行时产物）
rsync -a --exclude '.git' --exclude '__pycache__' --exclude 'logs' --exclude 'sessions' \
  "$PROJ/" "$STAGE/" 2>/dev/null || cp -r "$PROJ/." "$STAGE/"

# 把无扩展名 CLI 复制为 .py 版本（SkillHub 白名单认可），并移除无扩展名原文件
if [ -f "$STAGE/scripts/xinling" ]; then
  cp "$STAGE/scripts/xinling" "$STAGE/scripts/xinling.py"
  rm "$STAGE/scripts/xinling"
  echo "   ✅ scripts/xinling.py 已生成，无扩展名原文件已移除"
else
  echo "   ⚠️ scripts/xinling 不存在，跳过"
fi

echo "[2/3] 运行 SkillHub 预检..."
skillhub publish "$STAGE" --version 3.5.0 \
  --changelog "V3.5.0: 修复人格切换崩溃(结构归一化器,此前5/6人格会KeyError); 友好错误提示+xinling check健康检查; 6人格补齐能力边界; heixiang玄学降级兜底; 新增FAQ+ANTIPATTERNS" \
  $DRY

echo "[3/3] 完成 (临时目录: $STAGE)"
