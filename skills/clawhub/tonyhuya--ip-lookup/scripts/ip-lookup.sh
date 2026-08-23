#!/usr/bin/env bash
# ip-lookup: IP 地址归属地查询（数据源: ip.sb，免费无 Key）
# 用法:
#   ip-lookup                    # 查询本机公网 IP
#   ip-lookup 114.114.114.114    # 查询指定 IP
#   ip-lookup 8.8.8.8 --json     # 输出原始 JSON
set -euo pipefail

IP=""
JSON=0
for arg in "$@"; do
  case "$arg" in
    --json) JSON=1 ;;
    --help|-h) sed -n '2,6p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) IP="$arg" ;;
  esac
done

if [ -z "$IP" ]; then
  # 获取本机公网 IP
  IP=$(curl -fsSL --max-time 15 "https://api.ip.sb/geoip" 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin).get('ip',''))" 2>/dev/null) || true
  [ -z "$IP" ] && { echo "获取本机 IP 失败，请检查网络，或直接指定: ip-lookup 8.8.8.8" >&2; exit 1; }
  LABEL="本机公网 IP"
else
  LABEL="IP $IP"
fi

DATA=$(curl -fsSL --max-time 15 "https://api.ip.sb/geoip/$IP" 2>/dev/null) || DATA=$(curl -fsSL --max-time 15 "https://ipwho.is/$IP" 2>/dev/null) || { echo "查询失败，请检查网络" >&2; exit 1; }

if [ "$JSON" = 1 ]; then
  echo "$DATA"
  exit 0
fi

echo "$DATA" | python3 -c '
import json, sys
d = json.load(sys.stdin)
ip = d.get("ip", "?")
country = d.get("country", "?")
region = d.get("region", "?")
city = d.get("city", "?")
isp = d.get("isp", d.get("organization", "?"))
asn = d.get("asn", d.get("asn_organization", "?"))
tz = d.get("timezone", "?")
lat = d.get("latitude", "?")
lon = d.get("longitude", "?")
print(f"📍 {ip}")
print(f"🌍 国家/地区: {country}")
if region and region != "?": print(f"🗺️ 省份: {region}")
if city and city != "?": print(f"🏙️ 城市: {city}")
if isp and isp != "?": print(f"🏢 运营商: {isp}")
if asn and asn != "?": print(f"🔢 ASN: {asn}")
if tz and tz != "?":
    if isinstance(tz, dict):
        tz = tz.get("id", "?")
    print(f"🕐 时区: {tz}")
if lat != "?" and lon != "?": print(f"📍 坐标: {lat}, {lon}")
'
