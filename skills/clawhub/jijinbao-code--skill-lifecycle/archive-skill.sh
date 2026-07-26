#!/bin/bash
# 技能归档脚本
# 用法: bash archive-skill.sh <skill-name>

SKILL_NAME="$1"
SKILLS_DIR="${SKILLS_DIR:-$HOME/.openclaw/workspace/skills}"
ARCHIVE_DIR="${SKILLS_ARCHIVE_DIR:-$HOME/.openclaw/workspace/skills-archive}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

[ -z "$SKILL_NAME" ] && echo "Usage: $0 <skill-name>" && exit 1

SKILL_PATH="$SKILLS_DIR/$SKILL_NAME"
ARCHIVE_PATH="$ARCHIVE_DIR/${SKILL_NAME}_${TIMESTAMP}"

[ ! -d "$SKILL_PATH" ] && echo "❌ 技能不存在: $SKILL_PATH" && exit 1

mv "$SKILL_PATH" "$ARCHIVE_PATH" && {
    echo "✅ 已归档: $SKILL_NAME -> $ARCHIVE_PATH"
    cat > "$ARCHIVE_PATH/_archive_meta.json" << EOF
{
    "original_name": "$SKILL_NAME",
    "archived_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
    "reason": "retirement_threshold_exceeded",
    "restore_command": "bash restore-skill.sh $SKILL_NAME"
}
EOF
} || echo "❌ 归档失败"
