#!/usr/bin/env python3
"""
Open-Meteo 天气查询 CLI（无 key、无第三方依赖、纯标准库）

数据源（全部免费端点，已在本机实测）：
  geocoding-api.open-meteo.com/v1/search       地名/POI → 经纬度（zh、countryCode 过滤）
  api.open-meteo.com/v1/forecast               预报（current/hourly/daily/minutely_15、models、批量坐标、单位切换）
  api.open-meteo.com/v1/elevation              海拔（支持批量）
  archive-api.open-meteo.com/v1/archive        历史存档（1940 起）
  historical-forecast-api.open-meteo.com       近期存档（预报模型保存储存，约最近1个月）
  air-quality-api.open-meteo.com/v1/air-quality 空气质量（US AQI/欧洲AQI/全污染物/UV/沙尘）
  marine-api.open-meteo.com/v1/marine          海浪（current/daily）
  flood-api.open-meteo.com/v1/flood            河流流量（近一年日值）
  alerts-api.open-meteo.com/v1/alerts          官方天气预警（CAP；部分网络 DNS 不可达→自动降级）

时区纪律：所有"现在/当前小时"一律取 API 返回的 utc_offset_seconds 换算，绝不读本机时钟。
退出码：0 成功 / 1 网络失败(重试后) / 2 地名未找到。可选端点故障降级不拖垮全局。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WX_URL = "https://api.open-meteo.com/v1/forecast"
ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
PRES_URL = "https://historical-forecast-api.open-meteo.com/v1/forecast"
AQ_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
MARINE_URL = "https://marine-api.open-meteo.com/v1/marine"
FLOOD_URL = "https://flood-api.open-meteo.com/v1/flood"
ALERTS_URL = "https://alerts-api.open-meteo.com/v1/alerts"
ELEV_URL = "https://api.open-meteo.com/v1/elevation"
NOWCAST_URL = "https://nowcast-api.open-meteo.com/v1/nowcast"
CLIMATE_URL = "https://climate-api.open-meteo.com/v1/climate"
ENSEMBLE_URL = "https://ensemble-api.open-meteo.com/v1/ensemble"

UA = "openmeteo-weather-skill/2.0 (personal CLI)"
TIMEOUT = 12.0
RETRIES = 3
CACHE_DIR = os.environ.get("WEATHER_CACHE_DIR", os.path.expanduser("~/.cache/openmeteo-weather"))
CACHE_TTL = int(os.environ.get("WEATHER_CACHE_TTL", "600"))
_BAD_HOST = os.environ.get("WX_FORCE_BAD_HOST")  # 测试注入：把一切请求指向不可达 host
_BAD_OPTIONAL = os.environ.get("WX_FORCE_BAD_OPTIONAL")  # 仅注入可选端点(air/alerts)路径


def _opt_url(url: str) -> str:
    return _BAD_OPTIONAL or url if _BAD_OPTIONAL else url

WMO = {
    0: "晴", 1: "大致晴", 2: "局部多云", 3: "阴",
    45: "雾", 48: "雾凇雾",
    51: "轻毛毛雨", 53: "中毛毛雨", 55: "浓毛毛雨",
    56: "冻毛毛雨", 57: "强冻毛毛雨",
    61: "小雨", 63: "中雨", 65: "大雨",
    66: "小冻雨", 67: "大冻雨",
    71: "小雪", 73: "中雪", 75: "大雪", 77: "米雪",
    80: "小阵雨", 81: "中阵雨", 82: "强阵雨",
    85: "小阵雪", 86: "大阵雪",
    95: "雷暴", 96: "雷暴伴小冰雹", 99: "雷暴伴强冰雹",
}

AQI_BANDS = [
    (50, "优"), (100, "良"), (150, "轻度污染"),
    (200, "中度污染"), (300, "重度污染"), (10**9, "严重污染"),
]

RAIN_CODES = {51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82, 95, 96, 99}
SNOW_CODES = {71, 73, 75, 77, 85, 86}
THUNDER_CODES = {95, 96, 99}

ADVICE_THRESHOLDS = {
    "cold_max": 5, "cool_max": 15, "hot_min": 30, "extreme_min": 37,
    "feels_gap": 4, "dipswind_gap": 12, "dry_humidity": 20,
    "rain_prob": 50, "uv": 6, "wind_kmh": 40, "aqi_sensitive": 100, "aqi_bad": 150,
}

UNIT_SYSTEMS = {
    "metric": {},
    "imperial": {"temperature_unit": "fahrenheit", "wind_speed_unit": "mph", "precipitation_unit": "inch"},
    "ms": {"wind_speed_unit": "ms"},
}
UNIT_LABEL = {
    "metric": {"temp": "°C", "wind": "km/h", "precip": "mm"},
    "imperial": {"temp": "°F", "wind": "mph", "precip": "inch"},
    "ms": {"temp": "°C", "wind": "m/s", "precip": "mm"},
}


def ulabel(system, kind):
    return UNIT_LABEL.get(system or "metric", UNIT_LABEL["metric"])[kind]


# ---------------------------------------------------------------- HTTP + 缓存
def http_json(url: str, params: dict, ttl: int | None = None):
    """带缓存与重试的 GET JSON。缓存键含完整参数；坏缓存自动重抓；ttl=0 强制刷新。"""
    if ttl is None:
        ttl = CACHE_TTL
    if _BAD_HOST:
        url = _BAD_HOST
    qs = urllib.parse.urlencode(params)
    full = f"{url}?{qs}"
    key = hashlib.sha1(full.encode("utf-8")).hexdigest()
    path = os.path.join(CACHE_DIR, key)
    now = time.time()

    if ttl > 0 and os.path.exists(path):
        try:
            if now - os.path.getmtime(path) < ttl:
                with open(path, "r", encoding="utf-8") as fh:
                    return json.load(fh)
        except (OSError, json.JSONDecodeError):
            pass  # 坏缓存 → 当作未命中

    last_err: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(full, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            os.makedirs(CACHE_DIR, exist_ok=True)
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(data, fh)
            os.replace(tmp, path)
            return data
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError) as exc:
            last_err = exc
            if isinstance(exc, urllib.error.HTTPError) and 400 <= exc.code < 500:
                body = ""
                try:
                    body = json.loads(exc.read().decode()).get("reason", "")[:200]
                except Exception:
                    pass
                raise SystemExit(f"[error] 请求参数错误 HTTP {exc.code}：{url}\n  {body or exc.reason}")
            if attempt < RETRIES:
                time.sleep(0.6 * attempt)
    raise SystemExit(f"[error] 请求失败（重试{RETRIES}次后）：{url}\n  {last_err}")


def soft_http_json(url: str, params: dict, ttl: int | None = None, label: str = ""):
    """可选端点：失败返回 None，不拖垮主流程（alerts/air 降级）。"""
    try:
        return http_json(url, params, ttl)
    except SystemExit as exc:
        print(f"[warn] 可选数据 {label or url} 不可用：{str(exc).splitlines()[-1][:80]}", file=sys.stderr)
        return None


def geocode(name: str, count: int = 1, country: str | None = None):
    params = {"name": name, "count": max(1, count), "language": "zh", "format": "json"}
    if country:
        params["countryCode"] = country
    data = http_json(GEO_URL, params, ttl=86400)
    results = data.get("results") or []
    if not results:
        print(f"[error] 找不到地名：{name}" + ("（提示：区级/街道级细地址常搜不到，改用 --lat/--lon）" if len(name) > 2 else ""), file=sys.stderr)
        sys.exit(2)
    return results[0]


def resolve(city: str | None, lat, lon, country: str | None = None) -> dict:
    if lat is not None and lon is not None:
        return {"name": city or f"{lat:.3f},{lon:.3f}", "latitude": float(lat), "longitude": float(lon),
                "timezone": "auto", "country_code": "", "elevation": None}
    if not city:
        raise SystemExit("[error] 需要城市名或 --lat/--lon")
    g = geocode(city, country=country)
    return {"name": g["name"], "latitude": g["latitude"], "longitude": g["longitude"],
            "timezone": g.get("timezone", "auto"), "country_code": g.get("country_code", ""),
            "elevation": g.get("elevation")}


def wmo(code) -> str:
    try:
        return WMO.get(int(code), f"未知(code={code})")
    except (TypeError, ValueError):
        return f"未知(code={code})"


def aqi_band(v):
    if v is None:
        return "—"
    for lim, label in AQI_BANDS:
        if v <= lim:
            return label
    return "严重污染"


# ---------------------------------------------------------------- 时区纪律
def target_now(utc_offset_seconds: int, ref_utc: datetime | None = None) -> datetime:
    """API 返回的 utc_offset_seconds → 目标城市当地"现在"。ref_utc 仅供测试注入。"""
    base = (ref_utc or datetime.now(timezone.utc)).replace(tzinfo=None)
    return base + timedelta(seconds=utc_offset_seconds)


def cut_window(times: list[str], series: list, ref_now: datetime, count: int, granularity: str = "hour"):
    """从 ISO 时间串数组里截取 >= ref_now 所在时段起点的 count 条。纯函数，可单测。"""
    idx = _window_idx(times, ref_now, count, granularity)
    if not idx:
        return []
    if series:
        return [tuple(s[i] for s in series) for i in idx]
    return [times[i] for i in idx]


def _window_idx(times, ref_now, count, granularity="hour"):
    cutoff = {"hour": ref_now.strftime("%Y-%m-%dT%H"),
              "day": ref_now.strftime("%Y-%m-%d"),
              "minute15": ref_now.strftime("%Y-%m-%dT%H:")[:14] + f"{(ref_now.minute // 15) * 15:02d}"}[granularity]
    length = {"hour": 13, "day": 10, "minute15": 16}[granularity]
    return [i for i, t in enumerate(times) if t[:length] >= cutoff][: max(1, count)]


# ---------------------------------------------------------------- 查询
CURRENT_FIELDS = ("temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,"
                  "wind_speed_10m,wind_gusts_10m,precipitation,rain,showers,snowfall,"
                  "cloud_cover,is_day,dew_point_2m,surface_pressure,pressure_msl,"
                  "visibility,cape,snow_depth")
DAILY_FIELDS = ("weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,"
                "apparent_temperature_max,apparent_temperature_min,"
                "precipitation_sum,rain_sum,showers_sum,snowfall_sum,"
                "precipitation_hours,precipitation_probability_max,"
                "sunrise,sunset,daylight_duration,sunshine_duration,"
                "uv_index_max,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant")
HOURLY_FIELDS = ("temperature_2m,apparent_temperature,relative_humidity_2m,dew_point_2m,"
                 "weather_code,precipitation_probability,precipitation,rain,showers,snowfall,"
                 "snow_depth,wind_speed_10m,wind_gusts_10m,wind_direction_10m,pressure_msl,"
                 "surface_pressure,cloud_cover,visibility,uv_index,cape,is_day")
MINUTELY_FIELDS = "temperature_2m,relative_humidity_2m,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m"
AIR_VARS = ("us_aqi,european_aqi,pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,"
            "ozone,aerosol_optical_depth,dust,uv_index")
POLLEN_VARS = "alder_pollen,birch_pollen,grass_pollen,mugwort_pollen,olive_pollen,ragweed_pollen"


def _unitparams(args) -> dict:
    u = UNIT_SYSTEMS.get(getattr(args, "units", "metric") or "metric", {})
    return dict(u)


def fetch_forecast(pos: dict, args, *, current=True, hourly=False, daily=False, minutely=False,
                   past_days=0, url=WX_URL, label=""):
    params = {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "timezone": pos["timezone"] or "auto",
    }
    params.update(_unitparams(args))
    if getattr(args, "models", None):
        params["models"] = args.models
    if current:
        params["current"] = CURRENT_FIELDS
    if hourly:
        params["hourly"] = HOURLY_FIELDS
    if daily:
        params["daily"] = DAILY_FIELDS
    if minutely:
        params["minutely_15"] = MINUTELY_FIELDS
    if past_days:
        params["past_days"] = past_days
    if (daily or hourly or minutely) and not (args.start and args.end) and url != ARCHIVE_URL:
        need = 1
        if daily and args.days:
            need = max(need, min(args.days, 16))
        if minutely:
            need = max(need, 1)
        if hourly and args.hours:
            need = max(need, 1 + (-(-args.hours // 24)) - 1)  # ceil
            need = max(need, min(1 + args.hours // 24 + (1 if args.hours % 24 else 0), 16))
        # full 场景：窗口取各需求最大值，API 一窗满足后由 pack_* 裁剪
        params["forecast_days"] = need
    if getattr(args, "start", None):
        params["start_date"] = args.start
    if getattr(args, "end", None):
        params["end_date"] = args.end
    return http_json(url, params)


def cur_pack(pos: dict, data: dict, args) -> dict:
    c = data.get("current") or {}
    sys_ = getattr(args, "units", "metric") or "metric"
    return {
        "place": pos["name"], "lat": data.get("latitude"), "lon": data.get("longitude"),
        "resolved": {"country_code": pos.get("country_code"), "requested": pos["name"]},
        "timezone": data.get("timezone"), "utc_offset_seconds": data.get("utc_offset_seconds"),
        "elevation_m": data.get("elevation"), "obs_time": c.get("time"),
        "temp": c.get("temperature_2m"), "temp_unit": ulabel(sys_, "temp"),
        "feels": c.get("apparent_temperature"),
        "humidity_pct": c.get("relative_humidity_2m"), "dew_point": c.get("dew_point_2m"),
        "code": c.get("weather_code"), "sky": wmo(c.get("weather_code")),
        "wind_kmh": c.get("wind_speed_10m"), "wind_unit": ulabel(sys_, "wind"),
        "gusts": c.get("wind_gusts_10m"),
        "precip": c.get("precipitation"), "rain": c.get("rain"), "snow": c.get("snowfall"),
        "precip_unit": ulabel(sys_, "precip"),
        "cloud_pct": c.get("cloud_cover"), "is_day": c.get("is_day"),
        "pressure_hpa": c.get("surface_pressure"), "visibility_m": c.get("visibility"),
        "snow_depth_m": c.get("snow_depth"), "cape_jkg": c.get("cape"),
    }


_HOURLY_KEYS = ("temperature_2m", "apparent_temperature", "weather_code",
                "precipitation_probability", "precipitation", "wind_speed_10m",
                "uv_index", "visibility", "is_day")
_HOURLY_NAMES = ("temp", "feels", "code", "precip_prob", "precip", "wind", "uv_index", "visibility_m", "is_day")


def pack_hourly(pos, data, args, count):
    h = data.get("hourly") or {}
    times = h.get("time") or []
    off = int(data.get("utc_offset_seconds") or 0)
    cols = [h.get(k) or [None] * len(times) for k in _HOURLY_KEYS]
    idx = _window_idx(times, target_now(off), max(1, min(count, 168)))
    return [{"time": times[j], "sky": wmo(cols[2][j]),
             **dict(zip(_HOURLY_NAMES, [c[j] for c in cols]))} for j in idx]


def pack_minutely(pos, data, args, count):
    m = data.get("minutely_15") or {}
    times = m.get("time") or []
    off = int(data.get("utc_offset_seconds") or 0)
    idx = _window_idx(times, target_now(off), max(1, min(count, 96)), "minute15")
    keys = ("temp", "humidity_pct", "precip", "weather_code", "wind")
    srcs = [m.get(k) or [None] * len(times) for k in
            ("temperature_2m", "relative_humidity_2m", "precipitation", "weather_code", "wind_speed_10m")]
    return [{"time": times[j], "every": "15min", "sky": wmo(srcs[3][j]),
             **dict(zip(keys, [s[j] for s in srcs]))} for j in idx]


def pack_daily(pos, data, args):
    d = data.get("daily") or {}
    times = d.get("time") or []
    def col(k):
        return d.get(k) or [None] * len(times)
    return [{"time": t, "date": t,
             "code": col("weather_code")[i], "sky": wmo(col("weather_code")[i]),
             "tmax": col("temperature_2m_max")[i], "tmin": col("temperature_2m_min")[i],
             "tmean": col("temperature_2m_mean")[i] if "temperature_2m_mean" in d else None,
             "feels_max": col("apparent_temperature_max")[i], "feels_min": col("apparent_temperature_min")[i],
             "precip": col("precipitation_sum")[i], "rain": col("rain_sum")[i],
             "snow_cm": col("snowfall_sum")[i], "precip_hours": col("precipitation_hours")[i],
             "precip_prob": col("precipitation_probability_max")[i],
             "sunrise": col("sunrise")[i], "sunset": col("sunset")[i],
             "daylight_s": col("daylight_duration")[i], "sunshine_s": col("sunshine_duration")[i],
             "uv_max": col("uv_index_max")[i],
             "wind_max": col("wind_speed_10m_max")[i], "gusts_max": col("wind_gusts_10m_max")[i],
             "wind_dir_deg": col("wind_direction_10m_dominant")[i]}
            for i, t in enumerate(times)]


def fetch_multi(positions: list, args):
    """多坐标一次HTTP：latitude/longitude 逗号列表 → API 返回数组。"""
    params = {
        "latitude": ",".join(str(q["latitude"]) for q in positions),
        "longitude": ",".join(str(q["longitude"]) for q in positions),
        "current": CURRENT_FIELDS,
        "timezone": "auto",
    }
    params.update(_unitparams(args))
    if getattr(args, "models", None):
        params["models"] = args.models
    data = http_json(WX_URL, params)
    items = data if isinstance(data, list) else [data]
    return [cur_pack(q, d, args) for q, d in zip(positions, items)]


def fetch_air_multi(positions: list, args):
    params = {
        "latitude": ",".join(str(q["latitude"]) for q in positions),
        "longitude": ",".join(str(q["longitude"]) for q in positions),
        "current": AIR_VARS, "timezone": "auto"}
    data = soft_http_json(_opt_url(AQ_URL), params, label="air-batch")
    if data is None:
        return [None] * len(positions)
    items = data if isinstance(data, list) else [data]
    out = []
    for d in items:
        c = d.get("current") or {}
        out.append({"obs_time": c.get("time"), "us_aqi": c.get("us_aqi"),
                    "us_aqi_band": aqi_band(c.get("us_aqi")), "european_aqi": c.get("european_aqi"),
                    "pm25": c.get("pm2_5"), "pm10": c.get("pm10"), "ozone": c.get("ozone"),
                    "uv_index": c.get("uv_index")})
    return out


def fetch_air(pos: dict, args):
    data = http_json(_opt_url(AQ_URL), {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "current": AIR_VARS, "timezone": pos["timezone"] or "auto"})
    c = data.get("current") or {}
    pol = soft_http_json(_opt_url(AQ_URL), {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "current": POLLEN_VARS, "timezone": pos["timezone"] or "auto"}, label="pollen")
    pollen = ({k.replace("_pollen", ""): v for k, v in (pol.get("current") or {}).items()
               if k.endswith("_pollen")} if pol else None)
    return {"place": pos["name"], "obs_time": c.get("time"),
            "us_aqi": c.get("us_aqi"), "us_aqi_band": aqi_band(c.get("us_aqi")),
            "european_aqi": c.get("european_aqi"),
            "pm25": c.get("pm2_5"), "pm10": c.get("pm10"), "ozone": c.get("ozone"),
            "no2": c.get("nitrogen_dioxide"), "so2": c.get("sulphur_dioxide"),
            "co": c.get("carbon_monoxide"), "dust": c.get("dust"),
            "uv_index": c.get("uv_index"), "aod": c.get("aerosol_optical_depth"),
            "pollen": pollen,
            "note": "US AQI 为美国标尺，非中国 AQI 指数"}


def fetch_nowcast(pos: dict, args):
    """ECAD 临近预报（过去+未来30分钟级）；域名部分网络不可达→降级。"""
    off_hint = {"timezone": pos["timezone"] or "auto"}
    data = soft_http_json(_opt_url(NOWCAST_URL), {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "minutely_15": "precipitation,temperature_2m,weather_code",
        "past_minutely_15": 30, "forecast_minutely_15": 30,
        "domains": "ecad", **off_hint}, label="nowcast")
    if data is None:
        return {"place": pos["name"], "nowcast": None,
                "error": "unreachable（nowcast 域名在部分网络 DNS 无法解析，已自动降级）"}
    m = data.get("minutely_15") or {}
    times = m.get("time") or []
    return {"place": pos["name"], "domains": "ecad",
            "points": [{"time": t, "precip_mm": (m.get("precipitation") or [None] * len(times))[i],
                        "temp_c": (m.get("temperature_2m") or [None] * len(times))[i],
                        "sky": wmo((m.get("weather_code") or [None] * len(times))[i])}
                       for i, t in enumerate(times)]}


def fetch_elevation(pos):
    data = http_json(ELEV_URL, {"latitude": pos["latitude"], "longitude": pos["longitude"]})
    e = (data.get("elevation") or [None])[0]
    return {"place": pos["name"], "lat": pos["latitude"], "lon": pos["longitude"], "elevation": e}


def fetch_marine(pos: dict, args):
    data = http_json(MARINE_URL, {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "current": "wave_height,wave_period,wave_direction",
        "hourly": "wave_height,wave_period,wave_direction",
        "daily": "wave_height_max,wave_period_max,wave_direction_dominant",
        "timezone": pos["timezone"] or "auto", "forecast_days": 2})
    c = data.get("current") or {}
    pol = soft_http_json(_opt_url(AQ_URL), {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "current": POLLEN_VARS, "timezone": pos["timezone"] or "auto"}, label="pollen")
    pollen = ({k.replace("_pollen", ""): v for k, v in (pol.get("current") or {}).items()
               if k.endswith("_pollen")} if pol else None)
    h = data.get("hourly") or {}
    ht = h.get("time") or []
    off = int(data.get("utc_offset_seconds") or 0)
    idx = _window_idx(ht, target_now(off), max(1, min(args.hours or 12, 48)))
    hourly = [{"time": ht[j], "wave_height_m": (h.get("wave_height") or [None]*len(ht))[j],
               "wave_period_s": (h.get("wave_period") or [None]*len(ht))[j],
               "wave_dir_deg": (h.get("wave_direction") or [None]*len(ht))[j]} for j in idx]
    return {"place": pos["name"], "obs_time": c.get("time"),
            "current": {"wave_height_m": c.get("wave_height"), "wave_period_s": c.get("wave_period"),
                        "wave_dir_deg": c.get("wave_direction")},
            "hourly": hourly,
            "daily": _pack_marine_daily(data)}


def _pack_marine_daily(data):
    d = data.get("daily") or {}
    times = d.get("time") or []
    def col(k):
        return d.get(k) or [None] * len(times)
    return [{"date": t, "wave_height_max_m": col("wave_height_max")[i],
             "wave_period_max_s": col("wave_period_max")[i],
             "wave_dir_deg": col("wave_direction_dominant")[i]} for i, t in enumerate(times)]


def fetch_flood(pos: dict, args):
    params = {"latitude": pos["latitude"], "longitude": pos["longitude"],
              "daily": "river_discharge,river_discharge_mean",
              "timezone": pos["timezone"] or "auto", "past_days": 92, "forecast_days": 7}
    data = http_json(FLOOD_URL, params)
    d = data.get("daily") or {}
    times = d.get("time") or []
    def col(k):
        return d.get(k) or [None] * len(times)
    return {"place": pos["name"], "daily": [{"date": t, "river_discharge_m3s": col("river_discharge")[i],
                       "mean_m3s": col("river_discharge_mean")[i]} for i, t in enumerate(times)]}


def fetch_alerts(pos: dict, args):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    data = soft_http_json(_opt_url(ALERTS_URL), {
        "latitude": pos["latitude"], "longitude": pos["longitude"],
        "start_date": today, "end_date": today}, label="alerts")
    if data is None:
        return {"place": pos["name"], "alerts": None, "error": "unreachable（该域名在部分网络 DNS 无法解析，已自动降级）"}
    out = []
    for ev in data.get("alerts") or []:
        d = ev.get("event") or {}
        out.append({"event": d.get("eventName") or ev.get("event"),
                    "headline": d.get("headline"), "area": d.get("areaDesc"),
                    "severity": d.get("severity"), "onset": d.get("onset"), "ends": d.get("ends")})
    return {"place": pos["name"], "alerts": out}


# ---------------------------------------------------------------- 建议
def advice(cur: dict, daily: list, air: dict | None) -> list[str]:
    T = ADVICE_THRESHOLDS
    tips: list[str] = []
    t, feels = cur.get("temp"), cur.get("feels")
    if t is not None:
        if t <= T["cold_max"]:
            tips.append("寒冷：厚外套/保暖层，注意保暖")
        elif t <= T["cool_max"]:
            tips.append("凉爽：长袖或薄外套")
        elif t >= T["extreme_min"]:
            tips.append(f"极端高温 {t}：避免午后长时间户外，谨防中暑")
        elif t >= T["hot_min"]:
            tips.append("炎热：防晒、多补水")
    if feels is not None and t is not None and abs(feels - t) >= T["feels_gap"]:
        tips.append(f"体感与气温差 {feels - t:+.1f}°，按体感穿衣")
    code = cur.get("code")
    if code in RAIN_CODES:
        tips.append("当前有降水：带伞")
    if code in SNOW_CODES:
        tips.append("当前有降雪：防滑、注意出行")
    if code in THUNDER_CODES:
        tips.append("雷暴：尽快进入室内，远离空旷处")
    hum = cur.get("humidity_pct")
    if hum is not None and hum <= T["dry_humidity"]:
        tips.append(f"空气干燥（湿度 {hum}%）：保湿补水")
    wind = cur.get("wind_kmh")
    if wind is not None and wind >= T["wind_kmh"]:
        tips.append(f"大风 {wind}：注意高空坠物，骑行/打伞困难")
    if daily:
        rain_days = [r["date"] for r in daily if (r.get("precip_prob") or 0) >= T["rain_prob"]]
        if rain_days:
            tips.append("未来降水概率≥50%：" + ", ".join(rain_days[:4]) + "，出门带伞")
        gaps = [(r["date"], r.get("tmax"), r.get("tmin")) for r in daily
                if r.get("tmax") is not None and r.get("tmin") is not None
                and r["tmax"] - r["tmin"] >= T["dipswind_gap"]]
        if gaps:
            tips.append("昼夜温差≥12°：" + ", ".join(f"{d}({lo}~{hi}°)" for d, hi, lo in gaps[:2]))
        uv = max((r.get("uv_max") or 0) for r in daily)
        if uv >= T["uv"]:
            tips.append(f"紫外线强（UV 最高 {uv}）：防晒")
    if air and air.get("us_aqi") is not None:
        band = air.get("us_aqi_band") or aqi_band(air["us_aqi"])
        if air["us_aqi"] > T["aqi_bad"]:
            tips.append(f"AQI(US标尺) {air['us_aqi']}（{band}）：减少户外运动，戴口罩")
        elif air["us_aqi"] > T["aqi_sensitive"]:
            tips.append(f"AQI(US标尺) {air['us_aqi']}（{band}）：敏感人群减少长时间户外")
    return tips or ["常规天气，无特别提示"]


# ---------------------------------------------------------------- 输出
def one_line(r: dict) -> str:
    return (f"{r['place']} {r['obs_time']} · {r['sky']} · {r['temp']}{r['temp_unit']}"
            f"（体感 {r['feels']}{r['temp_unit']}）· 湿度 {r['humidity_pct']}% · "
            f"风 {r['wind_kmh']}{r['wind_unit']}（阵风 {r.get('gusts')}）· "
            f"降水 {r['precip']}{r['precip_unit']} · 云量 {r['cloud_pct']}%"
            f" · 气压 {r.get('pressure_hpa')}hPa" + ("" if r.get("is_day") is None else (" · 白天" if r['is_day'] else " · 夜间")))


def table_daily(rows: list) -> str:
    out = [f"{'日期':<12}{'天气':<12}{'最低':>7}{'最高':>7}{'降水概率':>9}{'降水量':>8}{'UV':>5}{'日出':>7}{'日落':>7}"]
    for r in rows:
        sun_r = (r.get("sunrise") or "—")[-5:]
        sun_s = (r.get("sunset") or "—")[-5:]
        out.append(f"{r['date']:<12}{r['sky']:<12}{str(r['tmin']):>6}°"
                   f"{str(r['tmax']):>6}°"
                   f"{(str(r['precip_prob'])+'%') if r['precip_prob'] is not None else '—':>9}"
                   f"{(str(r['precip'])+'mm') if r['precip'] is not None else '—':>8}"
                   f"{r['uv_max'] if r['uv_max'] is not None else '—':>5}"
                   f"{sun_r:>7}{sun_s:>7}")
    return "\n".join(out)


def table_hourly(rows: list) -> str:
    out = [f"{'时间':<18}{'天气':<12}{'温度':>7}{'降水概率':>9}{'降水量':>8}{'风':>8}"]
    for r in rows:
        out.append(f"{r['time']:<18}{r['sky']:<12}{str(r['temp']):>6}°"
                   f"{(str(r['precip_prob'])+'%') if r['precip_prob'] is not None else '—':>9}"
                   f"{(str(r['precip'])+'mm') if r['precip'] is not None else '—':>8}"
                   f"{(str(r['wind'])+'km/h') if r['wind'] is not None else '—':>8}")
    return "\n".join(out)


# ---------------------------------------------------------------- CLI



def main() -> int:
    p = argparse.ArgumentParser(description="Open-Meteo 天气查询（无 key，全免费端点）",
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["now", "daily", "hourly", "minutely", "air", "marine", "flood",
                                   "alerts", "elevation", "history", "past", "archive", "climate",
                                   "ensemble", "full", "compare", "batch", "nowcast"])
    p.add_argument("city", nargs="?", help="城市/POI 名（中文或英文）；batch 用逗号分隔；compare 用 'A..B' 或两个参数")
    p.add_argument("city2", nargs="?", help="compare 的第二个城市")
    p.add_argument("--lat", type=float); p.add_argument("--lon", type=float)
    p.add_argument("--days", type=int, default=7)
    p.add_argument("--hours", type=int, default=12)
    p.add_argument("--count", type=int, default=24, help="minutely 返回条数(≤96)")
    p.add_argument("--start"); p.add_argument("--end", help="archive 日期区间 YYYY-MM-DD")
    p.add_argument("--units", choices=["metric", "imperial", "ms"], default="metric")
    p.add_argument("--models", help="预报模型，逗号分隔，如 ecmwf_ifs025,gfs_seamless")
    p.add_argument("--country", help="地名消歧：两位国家码，如 CN / GB")
    p.add_argument("--json", action="store_true")
    p.add_argument("--trend", type=int, help="air: 未来N小时AQI序列(≤48)")
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--no-air", action="store_true")
    p.add_argument("--no-alerts", action="store_true")
    args = p.parse_args()

    global CACHE_TTL
    if args.no_cache:
        CACHE_TTL = 0
    cmd = args.cmd
    if args.start and cmd not in ("archive", "climate"):
        raise SystemExit(f"[error] --start/--end 仅用于 archive/climate，当前命令 {cmd} 不支持")
    pos_list = []
    if cmd in ("batch", "compare"):
        names = []
        if args.cmd == "compare":
            if args.city2:
                names = [args.city, args.city2]
            else:
                names = [s.strip() for s in (args.city or "").split("..") if s.strip()]
        else:
            names = [s.strip() for s in (args.city or "").split(",") if s.strip()]
        if len(names) < 2:
            raise SystemExit(f"[error] {cmd} 需要至少两个地点（'A..B'、两个参数或逗号分隔）")
        pos_list = [resolve(n, None, None, args.country) for n in names]
    else:
        if not args.city and not (args.lat is not None and args.lon is not None):
            raise SystemExit("[error] 需要城市名或 --lat/--lon")
        pos_list = [resolve(args.city, args.lat, args.lon, args.country)]

    def emit(payload, human):
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(human)
        return 0

    pos = pos_list[0]

    if cmd == "now":
        data = fetch_forecast(pos, args)
        cur = cur_pack(pos, data, args)
        return emit(cur, one_line(cur))

    if cmd == "hourly":
        data = fetch_forecast(pos, args, current=False, hourly=True)
        rows = pack_hourly(pos, data, args, args.hours)
        return emit({"place": pos["name"], "timezone": data.get("timezone"), "hourly": rows},
                    f"{pos['name']} 未来 {len(rows)} 小时\n" + table_hourly(rows))

    if cmd == "minutely":
        data = fetch_forecast(pos, args, current=False, minutely=True)
        rows = pack_minutely(pos, data, args, args.count)
        return emit({"place": pos["name"], "timezone": data.get("timezone"), "minutely": rows},
                    f"{pos['name']} 未来 {len(rows)} 个15分钟段\n" +
                    "\n".join(f"{r['time']} {r['sky']} {r['temp']}° 降水{r['precip']}" for r in rows))

    if cmd == "daily":
        data = fetch_forecast(pos, args, current=False, daily=True)
        rows = pack_daily(pos, data, args)
        return emit({"place": pos["name"], "timezone": data.get("timezone"), "daily": rows},
                    f"{pos['name']} 未来 {len(rows)} 天\n" + table_daily(rows))

    if cmd == "past":
        data = fetch_forecast(pos, args, current=False, daily=True, past_days=args.days)
        off = int(data.get("utc_offset_seconds") or 0)
        upto = target_now(off).strftime("%Y-%m-%d")
        rows = [r for r in pack_daily(pos, data, args) if r["date"] <= upto]
        return emit({"place": pos["name"], "daily": rows}, f"{pos['name']} 近 {len(rows)} 天实况\n" + table_daily(rows))

    if cmd == "history":
        import datetime as _dt
        off0 = 28800 if not pos.get("timezone") else 0
        end = (target_now(0, ref_utc=_dt.datetime.now(_dt.timezone.utc)) - _dt.timedelta(days=1)).strftime("%Y-%m-%d")
        start = (_dt.datetime.strptime(end, "%Y-%m-%d") - _dt.timedelta(days=max(1, min(args.days, 31)) - 1)).strftime("%Y-%m-%d")
        class _A: pass
        ha = _A(); ha.start, ha.end, ha.days, ha.hours, ha.models, ha.units = start, end, None, None, args.models, args.units
        data = fetch_forecast(pos, ha, current=False, daily=True, url=PRES_URL)
        src_used = "historical-forecast(保存储)"
        if not data.get("daily"):
            data = fetch_forecast(pos, ha, current=False, daily=True, url=ARCHIVE_URL)
            src_used = "archive(回落)"
        rows = pack_daily(pos, data, ha)
        return emit({"place": pos["name"], "source": src_used, "start": start, "end": end, "daily": rows},
                    f"{pos['name']} 近期历史 {start}~{end}\n" + table_daily(rows))

    if cmd == "archive":
        if not (args.start and args.end):
            raise SystemExit("[error] archive 需要 --start 与 --end (YYYY-MM-DD)")
        data = fetch_forecast(pos, args, current=False, daily=True, url=ARCHIVE_URL)
        rows = pack_daily(pos, data, args)
        return emit({"place": pos["name"], "source": "archive(1940起)", "daily": rows},
                    f"{pos['name']} 存档 {args.start}~{args.end}\n" + table_daily(rows))

    if cmd == "air":
        a = fetch_air(pos, args)
        if getattr(args, "trend", None):
            th = http_json(_opt_url(AQ_URL), {
                "latitude": pos["latitude"], "longitude": pos["longitude"],
                "hourly": "us_aqi,pm2_5,ozone", "timezone": pos["timezone"] or "auto",
                "past_days": 1, "forecast_days": 2})
            ht = (th.get("hourly") or {}).get("time") or []
            hu = th.get("hourly") or {}
            idx = _window_idx(ht, target_now(int(th.get("utc_offset_seconds") or 0)), max(1, min(args.trend, 48)))
            a["trend"] = [{"time": ht[j], "us_aqi": (hu.get("us_aqi") or [None]*len(ht))[j],
                           "pm25": (hu.get("pm2_5") or [None]*len(ht))[j],
                           "ozone": (hu.get("ozone") or [None]*len(ht))[j]} for j in idx]
        human = _air_human(a)
        if a.get("trend"):
            human += "\n逐时: " + "  ".join(
                f"{x['time'][-5:]} AQI{x['us_aqi']}" for x in a["trend"])
        return emit(a, human)

    if cmd == "marine":
        m = fetch_marine(pos, args)
        cw = m["current"]
        dash = lambda v, u: (f"{v}{u}" if v is not None else "—")
        return emit(m, f"{m['place']} 浪高 {dash(cw['wave_height_m'], 'm')} "
                       f"周期 {dash(cw['wave_period_s'], 's')} 方向 {dash(cw['wave_dir_deg'], '°')}"
                       + ("（内陆无海浪数据，请用海岸坐标）" if cw["wave_height_m"] is None else ""))

    if cmd == "flood":
        f = fetch_flood(pos, args)
        return emit(f, f"{f['place']} 流量近92天+预报7天，共 {len(f['daily'])} 天（见 --json）")

    if cmd == "alerts":
        a = fetch_alerts(pos, args)
        if a.get("alerts"):
            return emit(a, f"{a['place']} 当前预警 {len(a['alerts'])} 条：" +
                        "; ".join((x['headline'] or x['event'] or '?') for x in a['alerts'][:3]))
        if a.get("alerts") == []:
            return emit(a, f"{a['place']} 当前无官方预警")
        return emit(a, f"{a['place']} 预警服务不可达（已降级，其余数据不受影响）")

    if cmd == "nowcast":
        nc = fetch_nowcast(pos, args)
        if nc.get("nowcast") is None and nc.get("error"):
            return emit(nc, f"{nc['place']} 临近预报不可达（已降级）")
        pts = nc["points"]
        return emit(nc, f"{nc['place']} ECAD 临近预报 {len(pts)} 个15分钟段（±30min窗口）\n" +
                    "\n".join(f"{x['time']} {x['sky']} {x['precip_mm']}mm" for x in pts[:12]))

    if cmd == "climate":
        if not (args.start and args.end):
            raise SystemExit("[error] climate 需要 --start 与 --end（气候情景区间）")
        params = {"latitude": pos["latitude"], "longitude": pos["longitude"],
                  "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
                  "timezone": pos["timezone"] or "auto",
                  "start_date": args.start, "end_date": args.end}
        if args.models:
            params["climate_models"] = args.models
        data = http_json(CLIMATE_URL, params)
        rows = pack_daily(pos, data, args)
        return emit({"place": pos["name"], "source": "climate(CMIP6情景)", "daily": rows},
                    f"{pos['name']} 气候情景 {args.start}~{args.end}（CMIP6 模式平均）\n" + table_daily(rows))

    if cmd == "ensemble":
        if not args.models:
            raise SystemExit("[error] ensemble 必须 --models 指定单一模型（如 gfs_seamless；best_match 不支持）")
        data = http_json(ENSEMBLE_URL, {
            "latitude": pos["latitude"], "longitude": pos["longitude"],
            "hourly": "temperature_2m", "models": args.models,
            "forecast_days": min(max(1, args.days or 1), 3), "timezone": pos["timezone"] or "auto"})
        h = data.get("hourly") or {}
        ht = h.get("time") or []
        members = {k: v for k, v in h.items() if k.startswith("temperature_2m_member")}
        base = h.get("temperature_2m") or []
        spread = []
        for j in range(len(ht)):
            vals = [m[j] for m in members.values() if m[j] is not None]
            spread.append(round(max(vals) - min(vals), 2) if vals else None)
        idx = _window_idx(ht, target_now(int(data.get("utc_offset_seconds") or 0)), args.hours or 12)
        return emit({"place": pos["name"], "models": args.models,
                     "members": {k: [v[j] for j in idx] for k, v in members.items()},
                     "spread": {"temp": [spread[j] for j in idx], "times": [ht[j] for j in idx]}},
                    f"{pos['name']} 集合预报 {args.models}：{len(members)} 成员，"
                    f"未来 {len(idx)} 小时成员间温差(扩散度)见 --json")

    if cmd == "elevation":
        e = fetch_elevation(pos)
        return emit(e, f"{e['place']} 海拔 {e['elevation']} m")

    if cmd in ("batch", "compare"):
        curs = fetch_multi(pos_list, args)
        airs = [None] * len(pos_list) if args.no_air else fetch_air_multi(pos_list, args)
        rows = [{"place": q["name"], "current": c, "air": a} for q, c, a in zip(pos_list, curs, airs)]
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=2))
        else:
            for r in rows:
                print(one_line(r["current"]))
                if r["air"] and r["air"].get("us_aqi") is not None:
                    print(f"  AQI(US) {r['air']['us_aqi']}（{r['air']['us_aqi_band']}）· PM2.5 {r['air']['pm25']}")
        return 0

    # full：当前+逐日+逐时+逐15分+空气+预警+建议
    data = fetch_forecast(pos, args, hourly=True, daily=True, minutely=True)
    cur = cur_pack(pos, data, args)
    daily = pack_daily(pos, data, args)
    hourly = pack_hourly(pos, data, args, args.hours)
    minutely = pack_minutely(pos, data, args, 8)
    air = None if args.no_air else _soft_air(pos, args)
    alerts = None if args.no_alerts else fetch_alerts(pos, args)
    tips = advice(cur, daily, air)
    payload = {"place": pos["name"], "lat": cur["lat"], "lon": cur["lon"], "timezone": cur["timezone"],
               "current": cur, "daily": daily, "hourly": hourly, "minutely": minutely,
               "air": air, "alerts": alerts, "advice": tips}
    human = one_line(cur)
    if air:
        human += "\n" + _air_human(air)
    if alerts and alerts.get("alerts"):
        human += "\n预警：" + "; ".join(x["headline"] or x["event"] or "?" for x in alerts["alerts"][:3])
    human += "\n" + table_daily(daily) + "\n建议：" + "；".join(tips)
    return emit(payload, human)


def _soft_air(pos, args):
    try:
        return fetch_air(pos, args)
    except SystemExit:
        return None


def _air_human(air: dict) -> str:
    if not air:
        return "空气质量：不可用（已降级）"
    return (f"{air['place']} {air['obs_time']} · US AQI {air['us_aqi']}（{air['us_aqi_band']}）"
            f" · 欧洲AQI {air['european_aqi']} · PM2.5 {air['pm25']} · PM10 {air['pm10']} · "
            f"O₃ {air['ozone']} · UV {air['uv_index']}（US标尺非中国指数）")


if __name__ == "__main__":
    sys.exit(main())
