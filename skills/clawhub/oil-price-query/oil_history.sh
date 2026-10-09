#!/bin/bash
# 中国油价查询 - 历史油价查询脚本
# 用法：./oil_history.sh <省份或城市名称> <起始日期> [结束日期]
# 示例：./oil_history.sh 北京 2026-01-01 2026-12-31

# 不要使用 set -e，因为 find_province_code 对于日期参数会返回非零值

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 嵌入省份映射
declare -A PROVINCE_MAP=(
    ['北京']='110000' ['京']='110000' ['天津']='120000' ['津']='120000' ['河北']='130000' ['冀']='130000' ['山西']='140000' ['晋']='140000' ['内蒙古']='150000' ['蒙']='150000' ['辽宁']='210000' ['辽']='210000' ['吉林']='220000' ['吉']='220000' ['黑龙江']='230000' ['黑']='230000' ['上海']='310000' ['沪']='310000' ['江苏']='320000' ['苏']='320000' ['浙江']='330000' ['浙']='330000' ['安徽']='340000' ['皖']='340000' ['福建']='350000' ['闽']='350000' ['江西']='360000' ['赣']='360000' ['山东']='370000' ['鲁']='370000' ['河南']='410000' ['豫']='410000' ['湖北']='420000' ['鄂']='420000' ['湖南']='430000' ['湘']='430000' ['广东']='440000' ['粤']='440000' ['广西']='450000' ['桂']='450000' ['海南']='460000' ['琼']='460000' ['重庆']='500000' ['渝']='500000' ['四川']='510000' ['川']='510000' ['贵州']='520000' ['黔']='520000' ['云南']='530000' ['云']='530000' ['西藏']='540000' ['藏']='540000' ['陕西']='610000' ['陕']='610000' ['甘肃']='620000' ['甘']='620000' ['青海']='630000' ['青']='630000' ['宁夏']='640000' ['宁']='640000' ['新疆']='650000' ['新']='650000'
)

# 嵌入城市到省份映射（只映射到省份名称）
declare -A CITY_PROVINCE_MAP=(
    ['南京']='江苏' ['杭州']='浙江' ['武汉']='湖北' ['长沙']='湖南' ['广州']='广东' ['深圳']='广东' ['成都']='四川' ['重庆']='重庆' ['西安']='陕西' ['昆明']='云南' ['拉萨']='西藏' ['长春']='吉林' ['沈阳']='辽宁' ['大连']='辽宁' ['郑州']='河南' ['济南']='山东' ['青岛']='山东' ['福州']='福建' ['厦门']='福建' ['南宁']='广西' ['海口']='海南' ['贵阳']='贵州' ['哈尔滨']='黑龙江' ['石家庄']='河北' ['太原']='山西' ['合肥']='安徽'
)

# 燃油名称映射（用于历史油价）
declare -A FUEL_NAMES_HTML=(
    ['88#汽油']='88 号汽油' ['89#汽油']='89 号汽油' ['91#汽油']='91 号汽油' ['92#汽油']='92 号汽油' ['94#汽油']='94 号汽油' ['95#汽油']='95 号汽油' ['1#柴油']='1 号柴油' ['0#柴油']='0 号柴油'
)

# 查找省份编码函数
find_province_code() {
    local input_name="$1"
    local province_code=""
    
    # 首先检查省份映射
    if [ -n "${PROVINCE_MAP[$input_name]+x}" ]; then
        province_code="${PROVINCE_MAP[$input_name]}"
        echo "$province_code"
        return 0
    fi
    
    # 然后检查城市映射
    if [ -n "${CITY_PROVINCE_MAP[$input_name]+x}" ]; then
        local mapped_value="${CITY_PROVINCE_MAP[$input_name]}"
        # 如果映射值是省份名称，则查找对应的省份编码
        if [ -n "${PROVINCE_MAP[$mapped_value]+x}" ]; then
            province_code="${PROVINCE_MAP[$mapped_value]}"
        else
            # 映射值已经是编码
            province_code="$mapped_value"
        fi
        echo "$province_code"
        return 0
    fi
    
    echo ""
    return 1
}

# 检查参数
if [ $# -lt 2 ]; then
    echo "用法：./oil_history.sh <省份或城市名称> <起始日期> [结束日期]" >&2
    echo "示例：./oil_history.sh 北京 2026-01-01 2026-12-31" >&2
    exit 1
fi

LOCATION="$1"
START_DATE="$2"
END_DATE="${3:-$(date +%Y-%m-%d)}"

# 获取省份编码
# 注意：如果 LOCATION 是日期，find_province_code 会返回错误
# 我们需要检查 LOCATION 是否是有效的位置
PROVINCE_CODE=$(find_province_code "$LOCATION" || echo "")

if [ -z "$PROVINCE_CODE" ]; then
    echo "❌ 未找到省份/城市：$LOCATION" >&2
    exit 1
fi

# 注意：历史油价 API 只返回固定城市（上海）的数据
# 如果查询的城市不是上海，API 会返回上海的数据
echo "⚠️  提示：历史油价 API 目前只支持查询上海，不支持按城市查询历史油价。" >&2
if [ "$LOCATION" != "上海" ] && [ "$LOCATION" != "沪" ]; then
    echo "⚠️  将显示上海的历史油价数据（而非您查询的 $LOCATION）。" >&2
fi

echo "正在查询历史油价数据..."
echo "" >&2

# 获取上海的城市编码（因为历史油价 API 只返回上海的数据）
SHANGHAI_CODE="310000"

# 查询历史油价数据
# 注意：历史油价 API 可能只返回固定城市（上海）的数据
HISTORY_RESPONSE=$(curl -s "https://map.360.cn/app/qcms?req=oil_history&cityid=${SHANGHAI_CODE}&date=${START_DATE}")

if [ -z "$HISTORY_RESPONSE" ]; then
    echo "❌ 无法获取历史油价数据" >&2
    exit 1
fi

# 获取 API 返回的城市编码（固定为上海）
API_ADCode="${SHANGHAI_CODE}"

# 保存到临时文件
TMPFILE=$(mktemp)
echo "$HISTORY_RESPONSE" > "$TMPFILE"

# 调用 Python 脚本解析历史数据
python3 "${SCRIPT_DIR}/oil_history.py" "$TMPFILE" "$API_ADCode" "$START_DATE" "$END_DATE" 2>&1 | tee /tmp/oil_history_debug.log

# 清理临时文件
rm -f "$TMPFILE"

# 检查是否有错误
if [ $? -ne 0 ]; then
    echo "" >&2
    echo "❌ 解析失败，请查看 /tmp/oil_history_debug.log 了解详情" >&2
    exit 1
fi

echo "" >&2
echo "查询完成。" >&2
