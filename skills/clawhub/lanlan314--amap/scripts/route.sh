#!/bin/bash
# 高德地图骑行路线查询脚本
# 用法: ./route.sh "出发地" "目的地" [出行方式]
# 出行方式: bicycling(骑行,默认) / driving(驾车) / walking(步行)

set -e

# 读取 API Key
API_KEY=$(cat ~/.openclaw/credentials/amap.json 2>/dev/null | python3 -c "import sys,json; print(json.load(sys.stdin).get('amap',{}).get('api_key',''))" 2>/dev/null)

if [ -z "$API_KEY" ]; then
    echo "错误: 未找到 AMAP_API_KEY，请在 ~/.openclaw/credentials/amap.json 中配置"
    exit 1
fi

FROM="$1"
TO="$2"
MODE="${3:-bicycling}"

if [ -z "$FROM" ] || [ -z "$TO" ]; then
    echo "用法: $0 \"出发地\" \"目的地\" [出行方式]"
    echo "示例: $0 \"南京\" \"景德镇\" bicycling"
    exit 1
fi

FROM_LOC=$(curl -s "https://restapi.amap.com/v3/geocode/geo?address=${FROM}&key=${API_KEY}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['geocodes'][0]['location'] if d.get('geocodes') else '')" 2>/dev/null)
TO_LOC=$(curl -s "https://restapi.amap.com/v3/geocode/geo?address=${TO}&key=${API_KEY}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['geocodes'][0]['location'] if d.get('geocodes') else '')" 2>/dev/null)

if [ -z "$FROM_LOC" ] || [ -z "$TO_LOC" ]; then
    echo "错误: 地理编码失败，请检查输入的地址是否正确"
    exit 1
fi

curl -s "https://restapi.amap.com/v3/direction/${MODE}?origin=${FROM_LOC}&destination=${TO_LOC}&key=${API_KEY}" | python3 -c "
import sys, json
d = json.load(sys.stdin)
if d.get('status') == '1':
    route = d['routes']
    print(f\"距离: {route.get('distance', 'N/A')} 米\")
    print(f\"耗时: {int(route.get('time', 0))//60} 分钟\")
    print(f\"路线点数: {len(route.get('paths', []))}\")
else:
    print('查询失败:', d.get('info', 'Unknown error'))
"
