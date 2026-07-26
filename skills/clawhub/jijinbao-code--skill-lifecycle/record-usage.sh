#!/bin/bash
# 技能使用记录脚本
# 记录每次技能被加载/使用的时间戳
# 用法: bash record-usage.sh <skill-name> [action]

SKILL_NAME="$1"
ACTION="${2:-loaded}"
SKILL_LIFECYCLE_DIR="${SKILL_LIFECYCLE_DIR:-$HOME/.openclaw/workspace/skills/skill-lifecycle}"
USAGE_FILE="$SKILL_LIFECYCLE_DIR/usage.jsonl"
LATEST_FILE="$SKILL_LIFECYCLE_DIR/latest-usage.json"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
DATE=$(date +"%Y-%m-%d")

if [ -z "$SKILL_NAME" ]; then
    echo "Usage: $0 <skill-name> [action]"
    echo "Actions: loaded, used, searched, installed, updated, restored"
    exit 1
fi

# 确保目录存在
mkdir -p "$SKILL_LIFECYCLE_DIR"
touch "$USAGE_FILE"

# 记录使用
echo "{\"skill\":\"$SKILL_NAME\",\"action\":\"$ACTION\",\"timestamp\":\"$TIMESTAMP\",\"date\":\"$DATE\"}" >> "$USAGE_FILE"

# 更新最新使用时间
if [ -f "$LATEST_FILE" ]; then
    python3 -c "
import json
with open('$LATEST_FILE', 'r') as f:
    data = json.load(f)
data['$SKILL_NAME'] = '$TIMESTAMP'
with open('$LATEST_FILE', 'w') as f:
    json.dump(data, f, indent=2)
" 2>/dev/null || echo "{\"$SKILL_NAME\":\"$TIMESTAMP\"}" > "$LATEST_FILE"
else
    echo "{\"$SKILL_NAME\":\"$TIMESTAMP\"}" > "$LATEST_FILE"
fi

echo "✅ Recorded: $SKILL_NAME ($ACTION) at $TIMESTAMP"
