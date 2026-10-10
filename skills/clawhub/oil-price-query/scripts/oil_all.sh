#!/bin/bash
# 查询全国各省实时油价概览
# 用法：oil_all.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$(dirname "$SCRIPT_DIR")"
PROVINCES_FILE="$DATA_DIR/data/provinces.json"

# 检查省份编码文件是否存在
if [ ! -f "$PROVINCES_FILE" ]; then
    echo "错误：找不到省份编码文件"
    echo "请确保省份编码文件存在：$PROVINCES_FILE"
    exit 1
fi

# 读取所有省份编码
python3 -c "
import json
with open('$PROVINCES_FILE', 'r', encoding='utf-8') as f:
    data = json.load(f)
codes = list(data.get('省份编码', {}).values())
print(' '.join(codes))
"