#!/usr/bin/env bash

# Team Memory v2.6.0 - 初始化脚本
# 用法: bash scripts/init.sh [--data-dir <path>]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="${TEAM_MEMORY_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
DATA_DIR="$SKILL_DIR/data"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --data-dir)
      DATA_DIR="$2"
      shift 2
      ;;
    --skill-dir)
      SKILL_DIR="$2"
      shift 2
      ;;
    *)
      echo "未知参数: $1" >&2
      exit 1
      ;;
  esac
done

if [[ "$DATA_DIR" != /* ]]; then
  DATA_DIR="$SKILL_DIR/$DATA_DIR"
fi

echo "Team Memory v2.6.0 初始化"
echo "目录: $SKILL_DIR"
echo "主数据目录: $DATA_DIR"

mkdir -p "$DATA_DIR/members"
mkdir -p "$DATA_DIR/stakeholders"
mkdir -p "$DATA_DIR/upward"
mkdir -p "$DATA_DIR/company"
mkdir -p "$DATA_DIR/insights"
mkdir -p "$DATA_DIR/templates"
mkdir -p "$DATA_DIR/tasks/reviews"
mkdir -p "$DATA_DIR/archive"
mkdir -p "$DATA_DIR/import/incoming"
mkdir -p "$DATA_DIR/import/reports"
mkdir -p "$DATA_DIR/.backup"

touch "$DATA_DIR/members/.gitkeep"
touch "$DATA_DIR/stakeholders/.gitkeep"
touch "$DATA_DIR/upward/.gitkeep"
touch "$DATA_DIR/company/.gitkeep"
touch "$DATA_DIR/insights/.gitkeep"
touch "$DATA_DIR/templates/.gitkeep"
touch "$DATA_DIR/tasks/.gitkeep"
touch "$DATA_DIR/tasks/reviews/.gitkeep"
touch "$DATA_DIR/archive/.gitkeep"
touch "$DATA_DIR/import/incoming/.gitkeep"
touch "$DATA_DIR/import/reports/.gitkeep"

if [ ! -f "$SKILL_DIR/skill-config.yaml" ]; then
  if [ -f "$SKILL_DIR/skill-config.example.yaml" ]; then
    cp "$SKILL_DIR/skill-config.example.yaml" "$SKILL_DIR/skill-config.yaml"
    echo "已从 skill-config.example.yaml 创建 skill-config.yaml"
  else
    echo "未找到 skill-config.yaml。请复制 skill-config.example.yaml 后配置成员。"
  fi
fi

if [ ! -f "$DATA_DIR/upward/expectations.md" ]; then
  cat > "$DATA_DIR/upward/expectations.md" <<'EOF'
# 上级期望与向上管理

## 当前期望

### 本季度
- [ ] 

## 向上沟通记录

### YYYY-MM-DD
**议题**: 
**上级反馈**: 
**我的行动**: 
**关联成员**: 
EOF
fi

if [ ! -f "$DATA_DIR/company/strategy.md" ]; then
  cat > "$DATA_DIR/company/strategy.md" <<'EOF'
# 公司战略与业务方向

## 年度战略

### YYYY
**战略主题**: 

## 业务变化

### YYYY-MM
**变化**: 
**影响**: 
**团队应对**: 
EOF
fi

python3 "$SCRIPT_DIR/adopt-data.py" --skill-dir "$SKILL_DIR" --data-dir "$DATA_DIR" --init-empty

echo "初始化完成。下一步：编辑 skill-config.yaml，或运行 scripts/new-member.sh 创建成员。"
