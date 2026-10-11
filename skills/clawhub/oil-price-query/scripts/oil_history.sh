#!/bin/bash
# 查询中国各省历史油价
# 用法：oil_history.sh [省份名称/简称]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$(dirname "$SCRIPT_DIR")"
PROVINCES_FILE="$DATA_DIR/data/provinces.json"

# 检查省份编码文件是否存在
if [ ! -f "$PROVINCES_FILE" ]; then
    echo "错误：找不到省份编码文件"
    echo "请确保省份编码文件存在：$PROVINCES_FILE"
    exit 1
fi

# 获取省份代码
get_province_code() {
    local province_name="$1"
    local code=$(python3 -c "
import json
with open('$PROVINCES_FILE', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
for name, code in data.get('省份编码', {}).items():
    if province_name in name or name in province_name:
        print(code)
        break
    for short, c in data.get('省份简称', {}).items():
        if province_name in name and short in province_name:
            print(c)
            break
" 2>/dev/null)
    
    if [ -z "$code" ]; then
        echo "未知省份：$province_name" >&2
        return 1
    fi
    
    echo "$code"
}

# 查询历史油价
query_oil_history() {
    local cityid="$1"
    local url="https://map.360.cn/app/qcms?req=oil_history&cityid=${cityid}"
    
    echo "正在获取历史油价数据..."
    
    # 使用 curl 获取数据
    local response=$(curl -s "${url}" 2>/dev/null)
    
    if [ -z "$response" ]; then
        echo "无法获取历史油价数据"
        return 1
    fi
    
    # 解析并格式化输出
    python3 << PYEOF
import json
import sys
from datetime import datetime

try:
    data = json.loads('''${response}''')
except json.JSONDecodeError:
    print("无法解析数据")
    sys.exit(1)

# 获取省份名称
province_name = data.get('city', '未知地区')
province_name = province_name.encode().decode('unicode_escape')

print("\\n" + "="*60)
print(f"  {province_name} 历史油价记录")
print("="*60 + "\\n")

# 遍历历史数据
if 'data' in data:
    records = data['data']
    # 按日期倒序排列
    records.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    for record in records:
        date_str = record.get('date', '').replace('\\u200b', '')
        date_str = date_str.encode().decode('unicode_escape')
        
        try:
            date_obj = datetime.strptime(date_str, '%Y/%m/%d')
            date_display = date_obj.strftime('%Y-%m-%d')
        except:
            date_display = date_str
        
        record_type = record.get('type', '').encode().decode('unicode_escape')
        type_emoji = "🔺" if record_type == "上调" else "🔻" if record_type == "下调" else "〰"
        
        print(f"┌{'─'*50}┐")
        print(f"│  {date_display:15}  {record_type:4}  调整")
        print(f"├{'─'*50}┤")
        
        if 'data' in record:
            for fuel in record['data']:
                fuel_name = fuel.get('name', '未知')
                price = fuel.get('price', '-')
                updown = fuel.get('updown', '')
                
                fuel_name = fuel_name.encode().decode('unicode_escape')
                updown = updown.encode().decode('unicode_escape')
                
                if price != '-':
                    try:
                        price_float = float(price)
                        updown_float = float(updown) if updown and updown != '-' else 0
                        direction = "↑" if updown_float > 0 else "↓" if updown_float < 0 else "→"
                        print(f"│  {fuel_name:8}: {price:7} 元/L  {direction} {abs(updown_float):.2f}")
                    except ValueError:
                        print(f"│  {fuel_name:8}: {price:7} 元/L  {updown if updown else '-'}")
                else:
                    print(f"│  {fuel_name:8}: -")
        
        print(f"└{'─'*50}┘")
        print()

print("\\n共查询到", len(records), "条历史记录")
print("\\n查询完成！")
PYEOF
}

# 主程序
main() {
    if [ $# -eq 0 ]; then
        echo "用法：$0 [省份名称/简称]"
        echo ""
        echo "示例："
        echo "  $0 北京"
        echo "  $0 广东"
        exit 0
    fi
    
    province_name="$1"
    code=$(get_province_code "$province_name")
    
    if [ $? -ne 0 ]; then
        exit 1
    fi
    
    query_oil_history "$code"
}

main "$@"