#!/bin/bash
# 油价查询技能安装脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "========================================"
echo "  中国油价查询技能安装程序"
echo "========================================"
echo ""

# 检查是否已安装
if [ -f "$SCRIPT_DIR/oil_price.sh" ]; then
    echo "✅ 技能已安装"
    echo ""
    echo "📚 使用说明："
    echo "  实时油价查询：oil_price.sh 北京"
    echo "  历史油价查询：oil_history.sh 广东"
    echo "  全国油价概览：oil_all.sh"
    echo ""
    echo "💡 提示："
    echo "  - 支持省份全称或简称（如：北京/京、广东/粤）"
    echo "  - 可一次性查询多个省份：oil_price.sh 北京 上海 广州"
    echo ""
    echo "📁 已安装文件："
    ls -la "$SCRIPT_DIR"
    echo ""
    exit 0
fi

# 创建技能目录
echo "⚠️  创建技能目录..."
mkdir -p "$SCRIPT_DIR"

# 创建 oil_price.sh
cat > "$SCRIPT_DIR/oil_price.sh" << 'OILPRICE'
#!/bin/bash
# 中国油价查询 - 实时油价查询脚本

# 省份名称到编码的映射（完整中国省份列表）
PROVINCE_MAP=(
    ["北京"]:110000
    ["京"]:110000
    ["天津"]:120000
    ["津"]:120000
    ["河北"]:130000
    ["冀"]:130000
    ["山西"]:140000
    ["晋"]:140000
    ["内蒙古"]:150000
    ["蒙"]:150000
    ["辽宁"]:210000
    ["辽"]:210000
    ["吉林"]:220000
    ["吉"]:220000
    ["黑龙江"]:230000
    ["黑"]:230000
    ["上海"]:310000
    ["沪"]:310000
    ["江苏"]:320000
    ["苏"]:320000
    ["浙江"]:330000
    ["浙"]:330000
    ["安徽"]:340000
    ["皖"]:340000
    ["福建"]:350000
    ["闽"]:350000
    ["江西"]:360000
    ["赣"]:360000
    ["山东"]:370000
    ["鲁"]:370000
    ["河南"]:410000
    ["豫"]:410000
    ["湖北"]:420000
    ["鄂"]:420000
    ["湖南"]:430000
    ["湘"]:430000
    ["广东"]:440000
    ["粤"]:440000
    ["广西"]:450000
    ["桂"]:450000
    ["海南"]:460000
    ["琼"]:460000
    ["重庆"]:500000
    ["渝"]:500000
    ["四川"]:510000
    ["川"]:510000
    ["贵州"]:520000
    ["黔"]:520000
    ["云南"]:530000
    ["云"]:530000
    ["西藏"]:540000
    ["藏"]:540000
    ["陕西"]:610000
    ["陕"]:610000
    ["甘肃"]:620000
    ["甘"]:620000
    ["青海"]:630000
    ["青"]:630000
    ["宁夏"]:640000
    ["宁"]:640000
    ["新疆"]:650000
    ["新"]:650000
)

# 函数：查找省份编码
find_province_code() {
    local province_name="$1"
    local province_code=""
    
    # 首先检查映射表
    if [ -n "${PROVINCE_MAP[$province_name]}" ]; then
        province_code="${PROVINCE_MAP[$province_name]}"
    else
        echo "⚠️  未找到省份名称：$province_name"
        return 1
    fi
    
    echo "$province_code"
    return 0
}

# 函数：查询实时油价
query_oil_price() {
    local province_code="$1"
    local timestamp=$(date "+%Y 年 %m 月 %d 日")
    
    # 请求实时油价 API
    echo "正在查询油价数据..."
    echo ""
    
    local response
    response=$(curl -s "https://map.360.cn/app/qcms?req=oil_price&cityid=$province_code")
    
    if [ -z "$response" ]; then
        echo "❌ 无法获取数据，请检查网络连接"
        return 1
    fi
    
    # 解析 JSON 数据
    python3 << PYEOF
import json
import sys

try:
    data = json.loads('''$response''')
    province_code = "$province_code"
    
    # 查找对应的省份信息
    province_info = None
    for city in data.get('cities', []):
        if city.get('adcode') == province_code:
            province_info = city
            break
    
    if not province_info:
        print(f"❌ 未找到省份信息：{province_code}", file=sys.stderr)
        sys.exit(1)
    
    province_name = province_info.get('city', '未知')
    cities_data = province_info.get('data', [])
    
    # 查找汽油和柴油数据
    gasoline_89 = None
    gasoline_92 = None
    gasoline_95 = None
    gasoline_98 = None
    diesel_0 = None
    
    for item in cities_data:
        fuel_name = item.get('name', '')
        price = item.get('price', '')
        last_price = item.get('last', '')
        
        if fuel_name == '89 号汽油':
            gasoline_89 = {'name': fuel_name, 'price': price, 'last': last_price}
        elif fuel_name == '92 号汽油':
            gasoline_92 = {'name': fuel_name, 'price': price, 'last': last_price}
        elif fuel_name == '95 号汽油':
            gasoline_95 = {'name': fuel_name, 'price': price, 'last': last_price}
        elif fuel_name == '98 号汽油':
            gasoline_98 = {'name': fuel_name, 'price': price, 'last': last_price}
        elif fuel_name == '0 号柴油':
            diesel_0 = {'name': fuel_name, 'price': price, 'last': last_price}
    
    # 格式化输出
    print(f"\n============================================================")
    print(f"  油价查询结果 ({timestamp})")
    print("============================================================")
    print("")
    print("┌─────────────────────────────────────────────────┐")
    print(f"│  {province_name:18} 油价信息                     │")
    print("├─────────────────────────────────────────────────┤")
    
    fuels = [
        (gasoline_89, '89 号汽油', '⛽'),
        (gasoline_92, '92 号汽油', '⛽'),
        (gasoline_95, '95 号汽油', '⛽+'),
        (gasoline_98, '98 号汽油', '⛽++'),
        (diesel_0, '0 号柴油', '⛽')
    ]
    
    for fuel_info, fuel_name, prefix in fuels:
        if fuel_info:
            price = f"   {fuel_info['price']} 元/L"
            last_price = f" (上次：{fuel_info['last']})"
            
            # 判断涨跌
            if fuel_info['last']:
                old_price = float(fuel_info['last'])
                new_price = float(fuel_info['price'])
                diff = round(new_price - old_price, 2)
                
                if diff > 0:
                    trend = "📈"
                    diff_str = f"+{diff}"
                elif diff < 0:
                    trend = "📉"
                    diff_str = f"{diff}"
                else:
                    trend = "➡️"
                    diff_str = "0.00"
            else:
                trend = "➡️"
                diff_str = "无历史数据"
            
            print(f"│  {prefix} {fuel_name:11} : {price:12} {last_price:8} {trend} {diff_str}")
        else:
            print(f"│  {prefix} {fuel_name:11} :   无数据{'':12} {'':8}  ➡️  未销售")
    
    print("└─────────────────────────────────────────────────┘")
    print("")
    
except Exception as e:
    print(f"❌ 解析错误：{e}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# 检查参数
if [ $# -eq 0 ]; then
    echo "用法：$0 [省份名称]"
    echo ""
    echo "示例："
    echo "  $0 北京        # 查询北京实时油价"
    echo "  $0 北京 上海   # 查询北京和上海实时油价"
    echo "  $0 京          # 使用省份简称"
    exit 1
fi

# 处理多个省份
for province in "$@"; do
    echo ""
    code=$(find_province_code "$province")
    if [ $? -eq 0 ] && [ -n "$code" ]; then
        query_oil_price "$code"
    else
        echo ""
        echo "⚠️  无法查询省份：$province"
    fi
done

exit 0
OILPRICE

chmod +x "$SCRIPT_DIR/oil_price.sh"
echo "✅ 已安装 oil_price.sh"

# 创建 oil_history.sh
cat > "$SCRIPT_DIR/oil_history.sh" << 'OILHISTORY'
#!/bin/bash
# 中国油价查询 - 历史油价查询脚本

# 省份名称到编码的映射（完整中国省份列表）
PROVINCE_MAP=(
    ["北京"]:110000
    ["京"]:110000
    ["天津"]:120000
    ["津"]:120000
    ["河北"]:130000
    ["冀"]:130000
    ["山西"]:140000
    ["晋"]:140000
    ["内蒙古"]:150000
    ["蒙"]:150000
    ["辽宁"]:210000
    ["辽"]:210000
    ["吉林"]:220000
    ["吉"]:220000
    ["黑龙江"]:230000
    ["黑"]:230000
    ["上海"]:310000
    ["沪"]:310000
    ["江苏"]:320000
    ["苏"]:320000
    ["浙江"]:330000
    ["浙"]:330000
    ["安徽"]:340000
    ["皖"]:340000
    ["福建"]:350000
    ["闽"]:350000
    ["江西"]:360000
    ["赣"]:360000
    ["山东"]:370000
    ["鲁"]:370000
    ["河南"]:410000
    ["豫"]:410000
    ["湖北"]:420000
    ["鄂"]:420000
    ["湖南"]:430000
    ["湘"]:430000
    ["广东"]:440000
    ["粤"]:440000
    ["广西"]:450000
    ["桂"]:450000
    ["海南"]:460000
    ["琼"]:460000
    ["重庆"]:500000
    ["渝"]:500000
    ["四川"]:510000
    ["川"]:510000
    ["贵州"]:520000
    ["黔"]:520000
    ["云南"]:530000
    ["云"]:530000
    ["西藏"]:540000
    ["藏"]:540000
    ["陕西"]:610000
    ["陕"]:610000
    ["甘肃"]:620000
    ["甘"]:620000
    ["青海"]:630000
    ["青"]:630000
    ["宁夏"]:640000
    ["宁"]:640000
    ["新疆"]:650000
    ["新"]:650000
)

# 函数：查找省份编码
find_province_code() {
    local province_name="$1"
    local province_code=""
    
    # 首先检查映射表
    if [ -n "${PROVINCE_MAP[$province_name]}" ]; then
        province_code="${PROVINCE_MAP[$province_name]}"
    else
        echo "⚠️  未找到省份名称：$province_name"
        return 1
    fi
    
    echo "$province_code"
    return 0
}

# 函数：查询历史油价
query_oil_history() {
    local province_code="$1"
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    
    # 请求历史油价 API
    echo "正在获取历史油价数据..."
    echo ""
    
    local response
    response=$(curl -s "https://map.360.cn/app/qcms?req=oil_history&cityid=$province_code")
    
    if [ -z "$response" ]; then
        echo "❌ 无法获取数据，请检查网络连接"
        return 1
    fi
    
    # 解析 JSON 数据
    python3 << PYEOF
import json
import sys

try:
    data = json.loads('''$response''')
    province_code = "$province_code"
    
    # 查找对应的省份信息
    province_info = None
    for city in data.get('cities', []):
        if city.get('adcode') == province_code:
            province_info = city
            break
    
    if not province_info:
        print(f"❌ 未找到省份信息：{province_code}", file=sys.stderr)
        sys.exit(1)
    
    province_name = province_info.get('city', '未知')
    history_data = province_info.get('history', [])
    
    # 格式化输出
    print(f"\n============================================================")
    print(f"  {province_name} 历史油价记录")
    print("============================================================")
    print("")
    
    # 按日期分组显示
    adjustments = {}
    for record in history_data:
        date = record.get('date', '未知')
        if date not in adjustments:
            adjustments[date] = {'up': [], 'down': []}
        
        for item in record.get('data', []):
            fuel_name = item.get('name', '')
            price = float(item.get('price', 0))
            old_price = float(item.get('old_price', price))
            diff = price - old_price
            
            if diff > 0:
                adjustments[date]['up'].append({
                    'name': fuel_name,
                    'price': price,
                    'diff': diff
                })
            elif diff < 0:
                adjustments[date]['down'].append({
                    'name': fuel_name,
                    'price': price,
                    'diff': diff
                })
    
    # 按日期排序并输出
    for date in sorted(adjustments.keys()):
        up_items = adjustments[date]['up']
        down_items = adjustments[date]['down']
        
        print(f"┌{'─'*50}  上调   调整{'─'*50}┐")
        for item in up_items:
            print(f"│  {item['name']}: {item['price']:.2f} 元/L  ↑ {item['diff']:.2f}")
        print(f"└{'─'*50}{'':<50}{'':<50}┘")
        
        print(f"┌{'─'*50}  下调   调整{'─'*50}┐")
        for item in down_items:
            print(f"│  {item['name']}: {item['price']:.2f} 元/L  ↓ {abs(item['diff']):.2f}")
        print(f"└{'─'*50}{'':<50}{'':<50}┘")
        print("")
    
except Exception as e:
    print(f"❌ 解析错误：{e}", file=sys.stderr)
    sys.exit(1)
PYEOF
}

# 检查参数
if [ $# -eq 0 ]; then
    echo "用法：$0 [省份名称]"
    echo ""
    echo "示例："
    echo "  $0 北京        # 查询北京历史油价"
    echo "  $0 广东        # 查询广东历史油价"
    exit 1
fi

# 处理单个省份
province="$1"
code=$(find_province_code "$province")
if [ $? -eq 0 ] && [ -n "$code" ]; then
    query_oil_history "$code"
else
    echo ""
    echo "⚠️  无法查询省份：$province"
fi

exit 0
OILHISTORY

chmod +x "$SCRIPT_DIR/oil_history.sh"
echo "✅ 已安装 oil_history.sh"

# 创建 oil_all.sh
cat > "$SCRIPT_DIR/oil_all.sh" << 'OILALL'
#!/bin/bash
# 中国油价查询 - 全国油价概览脚本

# 省份名称到编码的映射（完整中国省份列表）
PROVINCE_MAP=(
    ["北京"]:110000
    ["京"]:110000
    ["天津"]:120000
    ["津"]:120000
    ["河北"]:130000
    ["冀"]:130000
    ["山西"]:140000
    ["晋"]:140000
    ["内蒙古"]:150000
    ["蒙"]:150000
    ["辽宁"]:210000
    ["辽"]:210000
    ["吉林"]:220000
    ["吉"]:220000
    ["黑龙江"]:230000
    ["黑"]:230000
    ["上海"]:310000
    ["沪"]:310000
    ["江苏"]:320000
    ["苏"]:320000
    ["浙江"]:330000
    ["浙"]:330000
    ["安徽"]:340000
    ["皖"]:340000
    ["福建"]:350000
    ["闽"]:350000
    ["江西"]:360000
    ["赣"]:360000
    ["山东"]:370000
    ["鲁"]:370000
    ["河南"]:410000
    ["豫"]:410000
    ["湖北"]:420000
    ["鄂"]:420000
    ["湖南"]:430000
    ["湘"]:430000
    ["广东"]:440000
    ["粤"]:440000
    ["广西"]:450000
    ["桂"]:450000
    ["海南"]:460000
    ["琼"]:460000
    ["重庆"]:500000
    ["渝"]:500000
    ["四川"]:510000
    ["川"]:510000
    ["贵州"]:520000
    ["黔"]:520000
    ["云南"]:530000
    ["云"]:530000
    ["西藏"]:540000
    ["藏"]:540000
    ["陕西"]:610000
    ["陕"]:610000
    ["甘肃"]:620000
    ["甘"]:620000
    ["青海"]:630000
    ["青"]:630000
    ["宁夏"]:640000
    ["宁"]:640000
    ["新疆"]:650000
    ["新"]:650000
)

# 函数：查找省份编码
find_province_code() {
    local province_name="$1"
    local province_code=""
    
    # 首先检查映射表
    if [ -n "${PROVINCE_MAP[$province_name]}" ]; then
        province_code="${PROVINCE_MAP[$province_name]}"
    else
        echo "⚠️  未找到省份名称：$province_name"
        return 1
    fi
    
    echo "$province_code"
    return 0
}

# 函数：查询实时油价
query_oil_price() {
    local province_code="$1"
    local timestamp=$(date "+%Y-%m-%d")
    
    # 请求实时油价 API
    echo "正在查询油价数据..."
    echo ""
    
    local response
    response=$(curl -s "https://map.360.cn/app/qcms?req=oil_price&cityid=$province_code")
    
    if [ -z "$response" ]; then
        echo "❌ 无法获取数据，请检查网络连接"
        return 1
    fi
    
    # 解析 JSON 数据
    python3 << PYEOF
import json

try:
    data = json.loads('''$response''')
    
    # 查找所有省份数据
    results = []
    for city in data.get('cities', []):
        city_code = city.get('adcode', '')
        province_name = city.get('city', '')
        city_name = city.get('name', '')
        cities_data = city.get('data', [])
        
        # 计算平均价格
        prices = []
        for item in cities_data:
            price = float(item.get('price', 0))
            prices.append(price)
        
        avg_price = sum(prices) / len(prices) if prices else 0
        
        results.append({
            'province': province_name,
            'city': city_name,
            'code': city_code,
            'avg_price': round(avg_price, 2)
        })
    
    # 按平均价格排序
    results.sort(key=lambda x: x['avg_price'])
    
    # 输出表格
    print(f"\n============================================================")
    print(f"  全国各省实时油价概览 ({timestamp})")
    print("============================================================")
    print("")
    print("┌──────────┬────────┬────────┬────────┬────────┬──────────┐")
    print("│  省份     │  92#汽油│  95#汽油│  98#汽油│  0#柴油 │  平均价格│")
    print("├──────────┼────────┼────────┼────────┼────────┼──────────┤")
    
    for r in results:
        print(f"│  {r['province']:<6}  │   {r['avg_price']:7.2f}  │")
    
    print("└──────────┴────────┴────────┴────────┴────────┴──────────┘")
    print("")
    
    # 显示价格区间
    if results:
        min_price = min(r['avg_price'] for r in results)
        max_price = max(r['avg_price'] for r in results)
        print(f"💡 全国平均油价范围：{min_price:.2f} ~ {max_price:.2f} 元/L")
        
except Exception as e:
    print(f"❌ 解析错误：{e}", file=sys.stderr)
PYEOF
}

# 检查参数
if [ $# -eq 0 ]; then
    echo "正在查询全国油价数据..."
    echo ""
    query_oil_price ""
else
    # 处理指定的省份
    for province in "$@"; do
        code=$(find_province_code "$province")
        if [ $? -eq 0 ] && [ -n "$code" ]; then
            query_oil_price "$code"
        fi
    done
fi

exit 0
OILALL

chmod +x "$SCRIPT_DIR/oil_all.sh"
echo "✅ 已安装 oil_all.sh"

# 提示用户
echo ""
echo "✅ 安装成功！"
echo ""
echo "📚 使用说明："
echo "  实时油价查询：oil_price.sh 北京"
echo "  历史油价查询：oil_history.sh 广东"
echo "  全国油价概览：oil_all.sh"
echo ""
echo "💡 提示："
echo "  - 支持省份全称或简称（如：北京/京、广东/粤）"
echo "  - 可一次性查询多个省份：oil_price.sh 北京 上海 广州"
echo ""

# 显示目录结构
echo "📁 目录结构："
ls -la "$SCRIPT_DIR"
echo ""

echo "安装完成！"