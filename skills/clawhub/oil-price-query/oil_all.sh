#!/bin/bash
# 中国油价查询 - 全国油价概览脚本
# 用法：./oil_all.sh
# 示例：./oil_all.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 嵌入省份映射（只保留主要省份名称，不保留别名）
declare -A PROVINCE_MAP=(
    ['北京']='110000' ['天津']='120000' ['河北']='130000' ['山西']='140000' ['内蒙古']='150000' ['辽宁']='210000' ['吉林']='220000' ['黑龙江']='230000' ['上海']='310000' ['江苏']='320000' ['浙江']='330000' ['安徽']='340000' ['福建']='350000' ['江西']='360000' ['山东']='370000' ['河南']='410000' ['湖北']='420000' ['湖南']='430000' ['广东']='440000' ['广西']='450000' ['海南']='460000' ['重庆']='500000' ['四川']='510000' ['贵州']='520000' ['云南']='530000' ['西藏']='540000' ['陕西']='610000' ['甘肃']='620000' ['青海']='630000' ['宁夏']='640000' ['新疆']='650000'
)

# 输出全国油价概览
output_national_overview() {
    echo ""
    echo "============================================================"
    echo "  全国油价概览"
    echo "============================================================"
    echo ""
    echo "省份 | 89 号汽油 | 92 号汽油 | 95 号汽油 | 98 号汽油 | 0 号柴油"
    echo "-----|-----------|-----------|-----------|-----------|--------"
    
    # 按省份编码排序，逐个查询
    for province_name in $(for p in "${!PROVINCE_MAP[@]}"; do echo "${PROVINCE_MAP[$p]} $p"; done | sort | cut -d' ' -f2); do
        province_code="${PROVINCE_MAP[$province_name]}"
        
        echo -n "${province_name}..."
        
        # 查询实时油价数据
        REALTIME_RESPONSE=$(curl -s "https://map.360.cn/app/qcms?req=oil_price&cityid=${province_code}" 2>/dev/null)
        
        if [ -z "$REALTIME_RESPONSE" ]; then
            echo " 无数据"
            printf "%-10s | - | - | - | - | -\n" "$province_name"
            continue
        fi
        
        # 保存到临时文件
        TMPFILE=$(mktemp)
        echo "$REALTIME_RESPONSE" > "$TMPFILE"
        
        # 调用 Python 脚本解析实时数据，并直接输出到屏幕
        CURRENT_TIMESTAMP=$(date '+%Y-%m-%d')
        python3 "${SCRIPT_DIR}/oil_price.py" "$TMPFILE" "$province_code" "$CURRENT_TIMESTAMP" 2>/dev/null
        
        echo " 完成"
    done
    
    echo ""
    echo "============================================================"
    echo "  查询完成。"
    echo "============================================================"
}

# 主函数
main() {
    echo "============================================================"
    echo "  中国油价查询 - 全国油价概览"
    echo "============================================================"
    echo ""
    
    output_national_overview
}

# 执行主函数
main
