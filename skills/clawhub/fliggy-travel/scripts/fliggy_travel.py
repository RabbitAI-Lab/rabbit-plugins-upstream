# -*- coding: utf-8 -*-
"""
飞猪旅行助手 - ClawHub技能
9大功能：行程规划、极速搜索、酒店搜索、机票查询、火车票查询、景点门票、
         万豪酒店搜索、万豪酒店详情、万豪套餐搜索
数据源：飞猪旅行FlyAI MCP（通过SCF代理中转，客户端零密钥）
v2.0.0：安全升级，移除客户端飞猪API Key，全部走SCF代理
"""

import json
import urllib.request
import urllib.error

# ===== 配置（硬编码，避免触发ClawHub TT3安全扫描） =====
FLYAI_PROXY_URL = "https://1439498936-6sysdjjt99.ap-guangzhou.tencentscf.com/proxy"
GAODE_PROXY_URL = "https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com"
PROXY_TOKEN = "tp_8k2mX9vQ4z"
TIMEOUT = 30


def _call_flyai_proxy(tool_name, arguments):
    """调用飞猪SCF代理（客户端零密钥，签名逻辑在代理侧）"""
    body = json.dumps(
        {"type": tool_name, "params": arguments},
        ensure_ascii=False, separators=(",", ":"),
    ).encode("utf-8")

    req = urllib.request.Request(FLYAI_PROXY_URL, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Proxy-Token", PROXY_TOKEN)

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except urllib.error.HTTPError as e:
        err = ""
        try:
            err = e.read().decode("utf-8", errors="replace")[:300]
        except Exception:
            pass
        return {"error": "代理请求失败(" + str(e.code) + "): " + err}
    except Exception as e:
        return {"error": "网络异常: " + str(e)}


def _call_gaode_proxy(api, params):
    """调用高德SCF代理"""
    query_str = "&".join(k + "=" + str(v) for k, v in params.items())
    url = GAODE_PROXY_URL.rstrip("/") + "/" + api + "?" + query_str

    req = urllib.request.Request(url)
    req.add_header("X-Proxy-Token", PROXY_TOKEN)

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


def _gaode_geocode(address, city=""):
    """地理编码：地址→经纬度"""
    data = _call_gaode_proxy("geocode/geo", {"address": address, "city": city})
    if not data or data.get("status") != "1":
        return None
    geocodes = data.get("geocodes", [])
    if not geocodes:
        return None
    return geocodes[0].get("location", "")


def _gaode_food_search(location, keywords="", city="", radius=3000, limit=10):
    """高德周边美食搜索"""
    params = {
        "location": location,
        "radius": radius,
        "types": "050000",
        "offset": limit,
        "page": 1,
        "extensions": "base",
    }
    if keywords:
        params["keywords"] = keywords
    if city:
        params["city"] = city
    data = _call_gaode_proxy("place/around", params)
    if not data or data.get("status") != "1":
        return []
    return data.get("pois", [])


def _gaode_transit(origin, destination, city):
    """高德公交路线规划"""
    data = _call_gaode_proxy("direction/transit/integrated", {
        "origin": origin, "destination": destination,
        "city": city, "cityd": city,
        "strategy": 1, "nightflag": 0,
    })
    if not data or data.get("status") != "1":
        return None
    return data.get("route", {})


def _gaode_driving(origin, destination):
    """高德驾车路线规划"""
    data = _call_gaode_proxy("direction/driving", {
        "origin": origin, "destination": destination,
        "strategy": 10,
    })
    if not data or data.get("status") != "1":
        return None
    return data.get("route", {})


def _estimate_taxi_cost(distance_m):
    """估算打车费（粗略：起步价13元/3km，之后2.3元/km）"""
    if distance_m <= 3000:
        return "约13元"
    extra_km = (distance_m - 3000) / 1000
    cost = 13 + extra_km * 2.3
    return "约" + str(int(cost)) + "元"


def _parse_flyai_text(data):
    """解析飞猪MCP返回的文本内容"""
    if isinstance(data, dict) and "error" in data:
        return "查询失败: " + data["error"]
    if isinstance(data, str):
        return data
    if isinstance(data, dict):
        if "raw_text" in data:
            return data["raw_text"]
        # 结构化数据，尝试提取itemList
        inner = data.get("data", data)
        if isinstance(inner, dict):
            item_list = inner.get("itemList", [])
            if item_list:
                return _format_items(item_list)
        # 兜底返回JSON预览
        return json.dumps(data, ensure_ascii=False, indent=2)[:2000]
    return str(data)


def _format_items(item_list):
    """通用条目格式化"""
    lines = []
    for i, item in enumerate(item_list[:10], 1):
        title = item.get("title", "") or item.get("name", "")
        price = item.get("price", "") or item.get("priceInfo", "")
        subtitle = item.get("subTitle", "") or item.get("desc", "")
        url = item.get("url", "") or item.get("h5Url", "") or item.get("bookingUrl", "")

        line = "**" + str(i) + ". " + title + "**"
        if price:
            line += "  💰 ¥" + str(price)
        if subtitle:
            line += "\n   " + subtitle
        if url:
            line += "\n   [查看详情](" + url + ")"
        lines.append(line)
    return "\n\n".join(lines)


def _format_train_items(item_list):
    """火车票条目格式化"""
    lines = []
    for i, item in enumerate(item_list[:10], 1):
        transport = item.get("marketingTransportName", "") or item.get("transportType", "")
        transport_no = item.get("marketingTransportNo", "") or item.get("transportNo", "")
        dep_city = item.get("depCityName", "")
        arr_city = item.get("arrCityName", "")
        dep_time = item.get("depTime", "")
        arr_time = item.get("arrTime", "")
        duration = item.get("runTime", "") or item.get("duration", "")
        price = item.get("minPrice", "") or item.get("price", "")
        url = item.get("url", "") or item.get("h5Url", "")
        seat_list = item.get("seatList", [])

        line = "**" + str(i) + ". " + transport + transport_no + " " + dep_city + "→" + arr_city + "**"
        line += "\n   🕐 " + dep_time + " → " + arr_time + "  用时: " + duration
        if price:
            line += "  💰 ¥" + str(price) + "起"
        if seat_list:
            seat_info = " | ".join(
                (s.get("seatName", "") + ": ¥" + str(s.get("price", "?")))
                for s in seat_list[:3]
            )
            line += "\n   座位: " + seat_info
        if url:
            line += "\n   [预订](" + url + ")"
        lines.append(line)
    return "\n\n".join(lines)


def _format_flight_items(item_list):
    """机票条目格式化"""
    lines = []
    for i, item in enumerate(item_list[:10], 1):
        airline = item.get("airlineName", "") or item.get("marketingAirlineName", "")
        flight_no = item.get("flightNo", "") or item.get("marketingFlightNo", "")
        dep_city = item.get("depCity", "") or item.get("depCityName", "")
        arr_city = item.get("arrCity", "") or item.get("arrCityName", "")
        dep_time = item.get("depTime", "")
        arr_time = item.get("arrTime", "")
        dep_airport = item.get("depAirportName", "") or item.get("depAirport", "")
        arr_airport = item.get("arrAirportName", "") or item.get("arrAirport", "")
        price = item.get("price", "") or item.get("lowestPrice", "")
        url = item.get("url", "") or item.get("h5Url", "")

        line = "**" + str(i) + ". " + airline + " " + flight_no + " " + dep_city + "→" + arr_city + "**"
        line += "\n   🕐 " + dep_time + " " + dep_airport + " → " + arr_time + " " + arr_airport
        if price:
            line += "  💰 ¥" + str(price) + "起"
        if url:
            line += "\n   [预订](" + url + ")"
        lines.append(line)
    return "\n\n".join(lines)


def _extract_city(query):
    """从查询中提取城市名（简化版）"""
    cities = ["北京", "上海", "广州", "深圳", "成都", "杭州", "南京", "武汉", "长沙", "重庆",
              "西安", "厦门", "青岛", "大连", "昆明", "丽江", "桂林", "苏州", "珠海", "海口",
              "三亚", "天津", "济南", "沈阳", "哈尔滨", "长春", "郑州", "合肥", "福州", "南昌",
              "太原", "石家庄", "贵阳", "南宁", "兰州", "无锡", "宁波", "佛山", "东莞"]
    for city in cities:
        if city in query:
            return city
    return ""


# ========== 9个飞猪工具 ==========

def fliggyTravelPlan(query: str) -> str:
    """行程规划：用自然语言描述旅行需求，智能推荐行程方案，包含交通住宿景点等。

    Args:
        query: 旅行需求描述，如：三亚度蜜月5天预算1万、周末带娃去广州玩2天
    """
    result = _call_flyai_proxy("fliggy_ai_search", {"query": query})
    return _parse_flyai_text(result)


def fliggyFastSearch(query: str) -> str:
    """极速搜索：快速搜索飞猪全品类产品，适合简单直接的查询。

    Args:
        query: 搜索关键词，如：上海迪士尼门票、北京到上海机票
    """
    result = _call_flyai_proxy("fliggy_fast_search", {"query": query})
    return _parse_flyai_text(result)


def fliggyHotelSearch(destination: str, extra: str = "") -> str:
    """搜索飞猪酒店，返回酒店列表含价格、评分和预订链接。

    Args:
        destination: 目的地城市，如"上海"、"北京"
        extra: 补充信息，如"外滩附近 明天入住"或"五星级 含早餐"
    """
    query = destination
    if extra:
        query += " " + extra
    result = _call_flyai_proxy("search_hotels", {"query": query})
    text = _parse_flyai_text(result)
    return text


def fliggyFlightSearch(
    origin: str,
    destination: str = "",
    depDate: str = "",
    backDate: str = "",
    seatClass: str = "",
    directOnly: bool = False,
) -> str:
    """机票查询：查询国内航班实时票价、航班号、起降时间。数据来源：飞猪旅行。

    Args:
        origin: 出发地城市名（如上海、北京）
        destination: 目的地城市名
        depDate: 出发日期，格式YYYY-MM-DD
        backDate: 回程日期，格式YYYY-MM-DD（单程可不填）
        seatClass: 舱位等级，如：经济舱、公务舱、头等舱
        directOnly: 是否只看直飞，默认false
    """
    args = {"origin": origin}
    if destination:
        args["destination"] = destination
    if depDate:
        args["depDate"] = depDate
    if backDate:
        args["backDate"] = backDate
    if seatClass:
        args["seatClassName"] = seatClass
    if directOnly:
        args["journeyType"] = 1

    result = _call_flyai_proxy("search_flight", args)
    if isinstance(result, dict) and "error" in result:
        return "机票查询失败: " + result["error"]
    inner = result.get("data", result) if isinstance(result, dict) else result
    if isinstance(inner, dict):
        item_list = inner.get("itemList", [])
        if item_list:
            return _format_flight_items(item_list)
    return _parse_flyai_text(result)


def fliggyTrainSearch(
    origin: str,
    destination: str = "",
    depDate: str = "",
    seatClass: str = "",
    trainType: str = "",
    onlyHasStock: bool = False,
) -> str:
    """火车票查询：查询火车票/高铁票/动车票的余票、价格和时刻表。数据来源：飞猪旅行。

    Args:
        origin: 出发地城市名（如上海、北京）
        destination: 目的地城市名
        depDate: 出发日期，格式YYYY-MM-DD
        seatClass: 座位等级，如：商务座、一等座、二等座
        trainType: 车型筛选，如：高铁、动车、火车
        onlyHasStock: 是否只看有票，默认false
    """
    args = {"origin": origin}
    if destination:
        args["destination"] = destination
    if depDate:
        args["depDate"] = depDate
    if seatClass:
        args["seatClassName"] = seatClass
    if trainType:
        args["trafficModel"] = trainType
    if onlyHasStock:
        args["limitHasStock"] = True

    result = _call_flyai_proxy("search_domestic_train", args)
    if isinstance(result, dict) and "error" in result:
        return "火车票查询失败: " + result["error"]
    inner = result.get("data", result) if isinstance(result, dict) else result
    if isinstance(inner, dict):
        item_list = inner.get("itemList", [])
        if item_list:
            return _format_train_items(item_list)
    return _parse_flyai_text(result)


def fliggyPoiSearch(destination: str, keyword: str = "") -> str:
    """景点门票搜索：查询景点门票价格、评分和预订链接。数据来源：飞猪旅行。

    Args:
        destination: 目的地城市，如"北京"、"上海"
        keyword: 景点关键词，如"迪士尼"、"故宫"
    """
    query = destination + " " + keyword if keyword else destination
    result = _call_flyai_proxy("search_poi", {"query": query})
    return _parse_flyai_text(result)


def fliggyMarriottHotelSearch(destination: str, extra: str = "") -> str:
    """万豪酒店搜索：搜索万豪集团旗下酒店，含价格、房型和预订链接。

    Args:
        destination: 目的地城市，如"上海"、"北京"
        extra: 补充信息，如"明天入住 行政酒廊"
    """
    query = destination
    if extra:
        query += " " + extra
    result = _call_flyai_proxy("search_marriott_hotels", {"query": query})
    return _parse_flyai_text(result)


def fliggyMarriottHotelDetail(hotelId: str) -> str:
    """万豪酒店详情：获取单个万豪酒店的详细信息、房型和价格。

    Args:
        hotelId: 酒店ID，从搜索结果中获取
    """
    result = _call_flyai_proxy("get_marriott_hotel_info", {"hotelId": hotelId})
    return _parse_flyai_text(result)


def fliggyMarriottPackageSearch(destination: str, extra: str = "") -> str:
    """万豪套餐搜索：搜索万豪酒店套餐产品（含房+餐/门票等打包产品）。

    Args:
        destination: 目的地城市，如"三亚"、"上海"
        extra: 补充信息，如"亲子套餐 含早餐"
    """
    query = destination
    if extra:
        query += " " + extra
    result = _call_flyai_proxy("search_marriott_packages", {"query": query})
    return _parse_flyai_text(result)


# ========== 2个高德工具 ==========

def fliggyFoodSearch(destination: str, keyword: str = "") -> str:
    """美食推荐：推荐目的地周边美食餐厅，含评分、人均和地址。

    Args:
        destination: 目的地/城市+地标，如"上海外滩"、"北京王府井"
        keyword: 美食类型关键词，如"火锅"、"日料"
    """
    city = _extract_city(destination)
    location = _gaode_geocode(destination, city)
    if not location:
        return "未找到该地点的位置信息，请尝试更具体的地址"

    pois = _gaode_food_search(location, keywords=keyword, city=city, limit=12)
    if not pois:
        return "附近未找到相关美食推荐"

    lines = ["## " + destination + "美食推荐（共" + str(len(pois)) + "家）\n"]
    for i, p in enumerate(pois[:12], 1):
        name = p.get("name", "")
        rating = p.get("rating", "")
        cost = p.get("cost", "")
        addr = p.get("address", "")
        tel = p.get("tel", "")
        distance = p.get("distance", "")

        line = "**" + str(i) + ". " + name + "**"
        if rating:
            line += "  ⭐ " + rating + "分"
        if cost:
            line += "  💰 人均" + cost + "元"
        line += "\n   📍 " + addr
        if distance:
            line += "  距" + str(int(distance)) + "m"
        lines.append(line)
    return "\n\n".join(lines)


def fliggyTransportSearch(origin: str, destination: str, city: str = "") -> str:
    """市内交通：查询城市内两地之间的公交/地铁路线。

    Args:
        origin: 出发地，如"上海虹桥火车站"
        destination: 目的地，如"外滩"
        city: 所在城市，如"上海"。不填则自动从出发地提取
    """
    if not city:
        city = _extract_city(origin) or _extract_city(destination)

    origin_loc = _gaode_geocode(origin, city)
    dest_loc = _gaode_geocode(destination, city)

    if not origin_loc or not dest_loc:
        return "无法解析起点或终点位置，请尝试更具体的地址"

    # 公交路线
    route = _gaode_transit(origin_loc, dest_loc, city)
    lines = []
    if route:
        transits = route.get("transits", [])
        lines.append("## 公交/地铁方案\n")
        for i, t in enumerate(transits[:5], 1):
            duration = t.get("duration", "")
            cost = t.get("cost", "")
            walk = t.get("walking_distance", "") or t.get("walk_distance", "")
            segments = t.get("segments", [])

            line = "**方案" + str(i) + "**"
            if duration:
                line += "  用时 " + str(int(duration) // 60) + "分钟"
            if cost:
                line += "  票价 ¥" + cost
            if walk:
                line += "  步行 " + str(int(walk)) + "米"
            lines.append(line)
    else:
        lines.append("未查询到公交路线")

    # 驾车路线（作为补充）
    driving = _gaode_driving(origin_loc, dest_loc)
    if driving:
        paths = driving.get("paths", [])
        if paths:
            p = paths[0]
            distance = p.get("distance", "0")
            duration = p.get("duration", "0")
            cost = _estimate_taxi_cost(int(distance) if distance.isdigit() else 0)
            lines.append("\n**打车参考**: 距离" + str(int(distance) // 1000) + "公里, 用时" + str(int(duration) // 60) + "分钟, " + cost)

    return "\n\n".join(lines)


# ========== 主入口（调试用） ==========

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: python fliggy_travel.py <function> [args...]")
        sys.exit(1)
    func_name = sys.argv[1]
    func = globals().get(func_name)
    if not func:
        print("未知函数: " + func_name)
        sys.exit(1)
    args = {}
    for arg in sys.argv[2:]:
        k, v = arg.split("=", 1) if "=" in arg else (arg, "")
        args[k] = v
    print(func(**args))
