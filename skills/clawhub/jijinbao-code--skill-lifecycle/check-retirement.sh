#!/bin/bash
# 技能退休检查脚本
# 检查所有技能的使用情况，标记低频和退休技能
# 用法: bash check-retirement.sh

SKILLS_DIR="${SKILLS_DIR:-$HOME/.openclaw/workspace/skills}"
SKILL_LIFECYCLE_DIR="${SKILL_LIFECYCLE_DIR:-$SKILLS_DIR/skill-lifecycle}"
LATEST_FILE="$SKILL_LIFECYCLE_DIR/latest-usage.json"
REPORT_FILE="$SKILL_LIFECYCLE_DIR/retirement-report.md"
ARCHIVE_DIR="${SKILLS_ARCHIVE_DIR:-$HOME/.openclaw/workspace/skills-archive}"
NOW=$(date +%s)
THRESHOLD_LOW=8640000    # 100天
THRESHOLD_RETIRE=25920000 # 300天

mkdir -p "$ARCHIVE_DIR" "$SKILL_LIFECYCLE_DIR"
[ ! -f "$LATEST_FILE" ] && echo "{}" > "$LATEST_FILE"

TOTAL=0; ACTIVE=0; LOW_FREQ=0; RETIRE=0; NO_RECORD=0

echo "# 技能退休检查报告 — $(date '+%Y-%m-%d %H:%M')" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "## 退休候选技能" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| 技能名称 | 最后使用 | 天数 | 状态 |" >> "$REPORT_FILE"
echo "|---------|---------|------|------|" >> "$REPORT_FILE"

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    [ "$skill_name" = "skill-lifecycle" ] && continue
    [ ! -f "$skill_dir/SKILL.md" ] && continue
    TOTAL=$((TOTAL + 1))
    
    last_used=$(python3 -c "
import json
try:
    with open('$LATEST_FILE') as f: data = json.load(f)
    print(data.get('$skill_name', ''))
except: print('')
" 2>/dev/null)
    
    if [ -z "$last_used" ]; then
        last_modified=$(stat -c %Y "$skill_dir/SKILL.md" 2>/dev/null || echo "0")
        days_since=$(( (NOW - last_modified) / 86400 ))
        status="无记录"
        NO_RECORD=$((NO_RECORD + 1))
    else
        last_used_ts=$(date -d "$last_used" +%s 2>/dev/null || echo "0")
        days_since=$(( (NOW - last_used_ts) / 86400 ))
        if [ $days_since -ge 300 ]; then status="退休"; RETIRE=$((RETIRE+1))
        elif [ $days_since -ge 100 ]; then status="低频"; LOW_FREQ=$((LOW_FREQ+1))
        else status="活跃"; ACTIVE=$((ACTIVE+1)); continue; fi
    fi
    
    [ "$status" != "活跃" ] && echo "| $skill_name | ${last_used:-未知} | $days_since | $status |" >> "$REPORT_FILE"
done

sed -i "s/## 退休候选技能/## 统计摘要\n\n- 总技能: $TOTAL\n- 活跃: $ACTIVE\n- 低频(>100天): $LOW_FREQ\n- 退休(>300天): $RETIRE\n- 无记录: $NO_RECORD\n\n## 退休候选技能/" "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"
echo "_由 check-retirement.sh 自动生成_" >> "$REPORT_FILE"

echo "统计: 总计=$TOTAL 活跃=$ACTIVE 低频=$LOW_FREQ 退休=$RETIRE 无记录=$NO_RECORD"
echo "报告: $REPORT_FILE"
