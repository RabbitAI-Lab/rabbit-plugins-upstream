#!/bin/bash
# 查询中国各省实时油价
# 用法：oil_price.sh [省份名称/简称] [省份名称/简称] ...

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
    
# 尝试通过名称匹配
for name, code in data.get('省份编码', {}).items():
    if province_name in name or name in province_name:
        print(code)
        break
    # 尝试通过简称匹配
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

# 主查询函数
query_oil_price() {
    local cityid="$1"
    local url="https://map.360.cn/app/qcms?req=oil_price&cityid=${cityid}"
    
    # 使用 curl 获取数据，处理 JSONP
    local response=$(curl -s "${url}" 2>/dev/null | sed 's/.*callback([^{]*)({).*/\1/g' | sed 's/}$//')
    
    if [ -z "$response" ] || [ "$response" == "null" ]; then
        echo "无法获取油价数据"
        return 1
    fi
    
    # 解析 JSON 并格式化输出
    python3 << PYEOF
import json
import sys

try:
    data = json.loads('''${response}''')
except json.JSONDecodeError:
    print("无法解析数据")
    sys.exit(1)

# 获取日期
if 'date' in data:
    date = data['date'].replace('\\u200b', '')
    # 解码 unicode
    date = date.encode().decode('unicode_escape')
else:
    date = "未知"

print("\\n" + "="*60)
print(f"  油价查询结果 ({date})")
print("="*60 + "\\n")

# 遍历城市数据
if 'cities' in data:
    for city in data['cities']:
        city_name = city.get('city', '未知地区')
        adcode = city.get('adcode', '')
        
        print(f"┌{'─'*48}┐")
        print(f"│  {city_name:18}  油价信息")
        print(f"├{'─'*48}┤")
        
        # 处理各油品数据
        if 'data' in city:
            for fuel in city['data']:
                fuel_name = fuel.get('name', '未知')
                price = fuel.get('price', '-')
                last_price = fuel.get('last', '-')
                
                # 解码 unicode
                fuel_name = fuel_name.encode().decode('unicode_escape')
                if last_price and last_price != '-':
                    last_price = last_price.encode().decode('unicode_escape')
                
                # 计算涨跌
                if price != '-' and last_price != '-':
                    try:
                        price_float = float(price)
                        last_float = float(last_price)
                        diff = price_float - last_float
                        if diff > 0:
                            trend = "📈"
                            trend_text = f"+{diff:.2f}"
                        elif diff < 0:
                            trend = "📉"
                            trend_text = f"{diff:.2f}"
                        else:
                            trend = "➡"
                            trend_text = "0.00"
                    except ValueError:
                        trend = "-"
                        trend_text = "-"
                else:
                    trend = "-"
                    trend_text = "-"
                
                # 根据油品类型添加 emoji
                if '89' in fuel_name:
                    emoji = "⛽"
                elif '92' in fuel_name:
                    emoji = "⛽"
                elif '95' in fuel_name:
                    emoji = "⛽+"
                elif '98' in fuel_name:
                    emoji = "⛽++"
                elif '0#' in fuel_name or '柴油' in fuel_name:
                    emoji = "⛽"
                else:
                    emoji = "⛽"
                
                print(f"│  {emoji} {fuel_name:12}: {price:7} 元/L  (上次：{last_price if last_price != '-' else 'N/A':7})  {trend} {trend_text}")
        
        print(f"└{'─'*48}┘")
        print()

print("\\n查询完成！")
PYEOF
}

# 主程序
main() {
    if [ $# -eq 0 ]; then
        echo "用法：$0 [省份名称/简称] [省份名称/简称] ..."
        echo ""
        echo "示例："
        echo "  $0 北京"
        echo "  $0 北京 上海 广州"
        echo "  $0 京 沪 粤"
        exit 0
    fi
    
    echo "正在查询油价数据..."
    
    for province in "$@"; do
        code=$(get_province_code "$province")
        if [ $? -eq 0 ]; then
            query_oil_price "$code"
        fi
    done
}

main "$@"