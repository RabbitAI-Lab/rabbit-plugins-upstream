#!/usr/bin/env bash

# Team Memory v2.8.1 - 初始化脚本
# 用法: bash scripts/init.sh [--data-dir <path>]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="${TEAM_MEMORY_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
REQUESTED_DATA_DIR=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --data-dir)
      REQUESTED_DATA_DIR="$2"
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

# Resolve and validate the existing root before creating any directory. In
# particular --skill-dir must not leave DATA_DIR pointing at the script's root.
DATA_DIR="$(python3 - "$SCRIPT_DIR" "$SKILL_DIR" "$REQUESTED_DATA_DIR" <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from team_memory_paths import (TeamMemoryPathError, read_config_data_path, read_root_lock,
                               resolve_data_path, same_path, validate_config_data_path)
skill = Path(sys.argv[2]).expanduser().resolve()
requested = sys.argv[3]
lock = read_root_lock(skill)
try:
    if lock:
        if not lock.get("data-dir"):
            raise TeamMemoryPathError("主库锁定文件缺少 data-dir。")
        data = resolve_data_path(str(lock["data-dir"]), skill)
        if requested and not same_path(data, resolve_data_path(requested, skill)):
            raise TeamMemoryPathError("初始化目录与已锁定主库冲突；请先检查，不创建另一套数据。")
    else:
        configured = read_config_data_path(skill / "skill-config.yaml")
        data = resolve_data_path(requested or configured or "data", skill)
    validate_config_data_path(skill / "skill-config.yaml", skill, data)
except TeamMemoryPathError as exc:
    print(f"ERROR: {exc}", file=sys.stderr)
    raise SystemExit(1)
print(data)
PY
)"

echo "Team Memory v2.8.1 初始化"
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

python3 - "$SCRIPT_DIR" "$SKILL_DIR" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
from memory_events import ensure_management_layout
from team_memory_paths import TeamMemoryWriteLock, resolve_paths
paths = resolve_paths(sys.argv[2])
with TeamMemoryWriteLock(paths.data_dir):
    ensure_management_layout(paths.data_dir)
PY

echo "初始化完成。下一步：编辑 skill-config.yaml，或运行 scripts/new-member.sh 创建成员。"
