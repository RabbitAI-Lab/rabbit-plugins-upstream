#!/bin/bash
# pre-task-check.sh — 任务前技能自动触发
# 从 stdin 读取 JSON 事件数据，匹配技能触发规则，输出触发的技能列表

set -euo pipefail

# 读取 stdin 事件数据
EVENT_DATA=$(cat)

# 提取字段（兼容 jq 和纯 bash）
if command -v jq &>/dev/null; then
    TASK_TYPE=$(echo "$EVENT_DATA" | jq -r '.task_type // ""')
    FILES=$(echo "$EVENT_DATA" | jq -r '.files // [] | .[]' 2>/dev/null || echo "")
    KEYWORDS=$(echo "$EVENT_DATA" | jq -r '.keywords // [] | .[]' 2>/dev/null || echo "")
else
    TASK_TYPE=$(echo "$EVENT_DATA" | grep -o '"task_type"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*: *"//;s/"$//')
    FILES=$(echo "$EVENT_DATA" | grep -o '"files"[[:space:]]*:[[:space:]]*\[[^]]*\]' | sed 's/.*\[//;s/\]//;s/"//g;s/,/ /g')
    KEYWORDS=$(echo "$EVENT_DATA" | grep -o '"keywords"[[:space:]]*:[[:space:]]*\[[^]]*\]' | sed 's/.*\[//;s/\]//;s/"//g;s/,/ /g')
fi

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date +"%Y-%m-%dT%H:%M:%SZ")
RULES_DIR="$(dirname "$0")/../rules"
TRIGGERED_SKILLS=()

# 加载并评估 skill-triggers.md 中的规则
if [[ -f "$RULES_DIR/skill-triggers.md" ]]; then
    IN_FRONTMATTER=false
    CURRENT_NAME=""
    CURRENT_ENABLED=""
    CURRENT_TASK_TYPE=""
    CURRENT_FILES_PATTERN=""
    CURRENT_KEYWORDS_PATTERN=""
    CURRENT_SKILL=""
    
    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if $IN_FRONTMATTER; then
                # 结束一个 frontmatter 块，评估规则
                if [[ "$CURRENT_ENABLED" != "false" && -n "$CURRENT_SKILL" ]]; then
                    MATCHED=false
                    
                    # 匹配 task_type
                    if [[ -n "$CURRENT_TASK_TYPE" && "$TASK_TYPE" =~ $CURRENT_TASK_TYPE ]]; then
                        MATCHED=true
                    fi
                    
                    # 匹配 files
                    if [[ -n "$CURRENT_FILES_PATTERN" ]]; then
                        for file in $FILES; do
                            if echo "$file" | grep -qE "$CURRENT_FILES_PATTERN"; then
                                MATCHED=true
                                break
                            fi
                        done
                    fi
                    
                    # 匹配 keywords
                    if [[ -n "$CURRENT_KEYWORDS_PATTERN" ]]; then
                        for keyword in $KEYWORDS; do
                            if echo "$keyword" | grep -qE "$CURRENT_KEYWORDS_PATTERN"; then
                                MATCHED=true
                                break
                            fi
                        done
                    fi
                    
                    if $MATCHED; then
                        TRIGGERED_SKILLS+=("$CURRENT_SKILL")
                    fi
                fi
                IN_FRONTMATTER=false
                CURRENT_NAME=""
                CURRENT_ENABLED=""
                CURRENT_TASK_TYPE=""
                CURRENT_FILES_PATTERN=""
                CURRENT_KEYWORDS_PATTERN=""
                CURRENT_SKILL=""
            else
                IN_FRONTMATTER=true
            fi
            continue
        fi
        if $IN_FRONTMATTER; then
            case "$line" in
                name:*) CURRENT_NAME=$(echo "$line" | sed 's/name:[[:space:]]*//;s/"//g') ;;
                enabled:*) CURRENT_ENABLED=$(echo "$line" | sed 's/enabled:[[:space:]]*//') ;;
                task_type:*) CURRENT_TASK_TYPE=$(echo "$line" | sed 's/task_type:[[:space:]]*//;s/"//g') ;;
                files_pattern:*) CURRENT_FILES_PATTERN=$(echo "$line" | sed 's/files_pattern:[[:space:]]*//;s/"//g') ;;
                keywords_pattern:*) CURRENT_KEYWORDS_PATTERN=$(echo "$line" | sed 's/keywords_pattern:[[:space:]]*//;s/"//g') ;;
                skill:*) CURRENT_SKILL=$(echo "$line" | sed 's/skill:[[:space:]]*//;s/"//g') ;;
            esac
        fi
    done < "$RULES_DIR/skill-triggers.md"
fi

# 去重
UNIQUE_SKILLS=()
for skill in "${TRIGGERED_SKILLS[@]}"; do
    if [[ ! " ${UNIQUE_SKILLS[*]} " =~ " ${skill} " ]]; then
        UNIQUE_SKILLS+=("$skill")
    fi
done

# 构建 JSON 输出
SKILLS_JSON="["
for i in "${!UNIQUE_SKILLS[@]}"; do
    if [[ $i -gt 0 ]]; then SKILLS_JSON+=","; fi
    SKILLS_JSON+="\"${UNIQUE_SKILLS[$i]}\""
done
SKILLS_JSON+="]"

if [[ ${#UNIQUE_SKILLS[@]} -gt 0 ]]; then
    CONTEXT_INJECTION="已加载 ${#UNIQUE_SKILLS[@]} 个技能上下文: ${UNIQUE_SKILLS[*]}"
else
    CONTEXT_INJECTION="无匹配技能"
fi

cat <<EOF
{
  "decision": "allow",
  "triggered_skills": $SKILLS_JSON,
  "context_injection": "$CONTEXT_INJECTION",
  "task_type": "$TASK_TYPE",
  "timestamp": "$TIMESTAMP"
}
EOF
