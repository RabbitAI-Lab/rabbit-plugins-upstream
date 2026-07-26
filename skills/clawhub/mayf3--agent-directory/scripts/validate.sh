#!/bin/bash
# validate.sh — 校验所有 Agent 档案 JSON 格式
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# scripts/ → skill/ → skills/ → workspace/
WS_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
PROFILES_DIR="$WS_DIR/docs/agent-profiles"
ERRORS=0
WARNINGS=0
VALID=0

VALID_LAYERS=("main" "exploration" "life" "infra" "cross-cutting")
VALID_PIPELINES=("content-production" "ai-evangelist" "open-source" "parenting" "investment" "family-health" "smart-home" "planning" "infra-dev" "life-services" "community")
REQUIRED_FIELDS=("systemName" "displayName" "role" "layer" "pipelines" "mainlineDirection" "status" "createdAt" "updatedAt")

# Collect all systemNames for uniqueness check (use file instead of associative array for sh compat)
NAMES_FILE="/tmp/agent-dir-names-$$"
> "$NAMES_FILE"
trap "rm -f $NAMES_FILE" EXIT

echo "🔍 校验 Agent 档案..."
echo "   目录: $PROFILES_DIR"
echo ""

for f in "$PROFILES_DIR"/*.json; do
  [ -f "$f" ] || continue
  fname=$(basename "$f")
  
  # Check if valid JSON
  if ! python3 -c "import json; json.load(open('$f'))" 2>/dev/null; then
    echo "❌ $fname: 不是有效 JSON"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  VALID=$((VALID + 1))
  ISSUES=""

  # Validate fields
  ISSUES=$(python3 -c "
import json, sys

with open('$f') as fh:
    d = json.load(fh)

errors = []
warnings = []

# Required fields
required = $([ "${REQUIRED_FIELDS[*]}" ] && echo "['systemName','displayName','role','layer','pipelines','mainlineDirection','status','createdAt','updatedAt']")
for r in required:
    if r not in d or not d[r]:
        errors.append(f'缺少必填字段: {r}')

# layer validation
valid_layers = ['main','exploration','life','infra','cross-cutting']
if d.get('layer') not in valid_layers:
    errors.append(f'layer 值非法: {d.get(\"layer\")} (合法: {valid_layers})')

# status validation
valid_status = ['active','inactive','pending-setup']
if d.get('status') not in valid_status:
    errors.append(f'status 值非法: {d.get(\"status\")}')

# pipelines validation
valid_pipelines = ['content-production','ai-evangelist','open-source','parenting','investment','family-health','smart-home','planning','infra-dev','life-services','community']
pipelines = d.get('pipelines', [])
if not isinstance(pipelines, list) or len(pipelines) == 0:
    errors.append('pipelines 必须是非空数组')
else:
    for p in pipelines:
        if p not in valid_pipelines:
            errors.append(f'pipeline ID 非法: {p}')

# currentTodos should be array of numbers
todos = d.get('currentTodos', [])
if not isinstance(todos, list):
    warnings.append('currentTodos 应为数组')

# systemName should match filename
import os
expected_name = os.path.splitext(os.path.basename('$f'))[0]
if d.get('systemName') != expected_name:
    warnings.append(f'systemName({d.get(\"systemName\")}) 与文件名({expected_name})不匹配')

if errors:
    print('ERRORS:' + '; '.join(errors))
if warnings:
    print('WARNINGS:' + '; '.join(warnings))
" 2>&1)

  if [ -n "$ISSUES" ]; then
    echo "$ISSUES" | while IFS= read -r line; do
      if echo "$line" | grep -q "^ERRORS:"; then
        echo "❌ $fname: $(echo "$line" | sed 's/^ERRORS://')"
        ERRORS=$((ERRORS + 1))
      elif echo "$line" | grep -q "^WARNINGS:"; then
        echo "⚠️  $fname: $(echo "$line" | sed 's/^WARNINGS://')"
        WARNINGS=$((WARNINGS + 1))
      fi
    done
  else
    echo "✅ $fname"
  fi

  # Uniqueness check
  sname=$(python3 -c "import json; print(json.load(open('$f')).get('systemName',''))" 2>/dev/null || echo "")
  if [ -n "$sname" ]; then
    existing=$(grep "^${sname}|" "$NAMES_FILE" 2>/dev/null || true)
    if [ -n "$existing" ]; then
      prev_file=$(echo "$existing" | cut -d'|' -f2)
      echo "❌ systemName 重复: $sname (在 $fname 和 $prev_file 中)"
      ERRORS=$((ERRORS + 1))
    else
      echo "${sname}|${fname}" >> "$NAMES_FILE"
    fi
  fi
done

echo ""
echo "📊 结果: ✅${VALID}个有效 ❌${ERRORS}个错误 ⚠️${WARNINGS}个警告"

if [ "$ERRORS" -gt 0 ]; then
  exit 1
fi
