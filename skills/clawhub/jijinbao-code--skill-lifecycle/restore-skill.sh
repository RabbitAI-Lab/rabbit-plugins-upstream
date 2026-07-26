#!/bin/bash
# 技能恢复脚本
# 用法: bash restore-skill.sh <skill-name>

SKILL_NAME="$1"
SKILLS_DIR="${SKILLS_DIR:-$HOME/.openclaw/workspace/skills}"
ARCHIVE_DIR="${SKILLS_ARCHIVE_DIR:-$HOME/.openclaw/workspace/skills-archive}"

[ -z "$SKILL_NAME" ] && echo "Usage: $0 <skill-name>" && exit 1

ARCHIVE_PATH=$(find "$ARCHIVE_DIR" -maxdepth 1 -type d -name "${SKILL_NAME}*" | sort -r | head -1)
[ -z "$ARCHIVE_PATH" ] && echo "❌ 未找到归档: $SKILL_NAME" && exit 1

RESTORE_PATH="$SKILLS_DIR/$SKILL_NAME"
[ -d "$RESTORE_PATH" ] && echo "❌ 技能已存在: $RESTORE_PATH" && exit 1

mv "$ARCHIVE_PATH" "$RESTORE_PATH" && {
    echo "✅ 已恢复: $SKILL_NAME"
    bash "$SKILLS_DIR/skill-lifecycle/record-usage.sh" "$SKILL_NAME" "restored"
    rm -f "$RESTORE_PATH/_archive_meta.json"
} || echo "❌ 恢复失败"
