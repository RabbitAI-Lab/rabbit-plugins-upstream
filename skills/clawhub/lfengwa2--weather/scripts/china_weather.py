#!/usr/bin/env python3
"""Query current conditions and forecasts for locations in China."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
USER_AGENT = "china-weather-skill/1.0 (+https://clawhub.ai/)"
CHINA_CODES = {"CN", "HK", "MO", "TW"}

WMO_ZH = {
    0: "晴",
    1: "大部晴朗",
    2: "多云",
    3: "阴",
    45: "雾",
    48: "雾凇",
    51: "小毛毛雨",
    53: "中等毛毛雨",
    55: "强毛毛雨",
    56: "小冻毛毛雨",
    57: "强冻毛毛雨",
    61: "小雨",
    63: "中雨",
    65: "大雨",
    66: "小冻雨",
    67: "强冻雨",
    71: "小雪",
    73: "中雪",
    75: "大雪",
    77: "米雪",
    80: "小阵雨",
    81: "中等阵雨",
    82: "强阵雨",
    85: "小阵雪",
    86: "强阵雪",
    95: "雷暴",
    96: "雷暴伴小冰雹",
    99: "雷暴伴大冰雹",
}

WEEKDAY_ZH = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


class WeatherError(RuntimeError):
    """Expected user-facing failure."""


def request_json(url: str, params: dict[str, Any]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params, doseq=True)
    request = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as exc:
        try:
            detail = json.loads(exc.read().decode("utf-8")).get("reason")
        except (ValueError, UnicodeDecodeError, AttributeError):
            detail = None
        raise WeatherError(f"天气服务返回 HTTP {exc.code}" + (f"：{detail}" if detail else "")) from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise WeatherError(f"无法连接天气服务：{exc.reason if hasattr(exc, 'reason') else exc}") from exc
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise WeatherError("天气服务返回了无效数据") from exc

    if not isinstance(payload, dict):
        raise WeatherError("天气服务返回了意外的数据格式")
    if payload.get("error"):
        raise WeatherError(f"天气服务报错：{payload.get('reason', '未知错误')}")
    return payload


def resolve_location(name: str) -> dict[str, Any]:
    payload = request_json(
        GEOCODING_URL,
        {"name": name.strip(), "count": 20, "language": "zh", "format": "json"},
    )
    results = payload.get("results") or []
    chinese = [item for item in results if item.get("country_code") in CHINA_CODES]
    if not chinese:
        raise WeatherError(f"未找到中国境内与“{name}”匹配的地点，请补充省、市或区县。")

    needle = name.strip().casefold()

    def rank(item: dict[str, Any]) -> tuple[int, int, int]:
        exact = int(str(item.get("name", "")).casefold() == needle)
        mainland = int(item.get("country_code") == "CN")
        population = int(item.get("population") or 0)
        return exact, mainland, population

    return max(chinese, key=rank)


def location_label(location: dict[str, Any]) -> str:
    values = [location.get("country"), location.get("admin1"), location.get("admin2"), location.get("name")]
    parts: list[str] = []
    for value in values:
        if value and value not in parts:
            parts.append(str(value))
    return " ".join(parts)


def fetch_forecast(latitude: float, longitude: float, days: int) -> dict[str, Any]:
    return request_json(
        FORECAST_URL,
        {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": "auto",
            "forecast_days": days,
            "current": ",".join(
                [
                    "temperature_2m",
                    "apparent_temperature",
                    "relative_humidity_2m",
                    "precipitation",
                    "weather_code",
                    "wind_speed_10m",
                    "wind_direction_10m",
                ]
            ),
            "daily": ",".join(
                [
                    "weather_code",
                    "temperature_2m_max",
                    "temperature_2m_min",
                    "apparent_temperature_max",
                    "apparent_temperature_min",
                    "precipitation_sum",
                    "precipitation_probability_max",
                    "wind_speed_10m_max",
                    "wind_gusts_10m_max",
                    "uv_index_max",
                    "sunrise",
                    "sunset",
                ]
            ),
        },
    )


def at(values: dict[str, Any], key: str, index: int) -> Any:
    series = values.get(key) or []
    return series[index] if index < len(series) else None


def fmt_number(value: Any, digits: int = 0) -> str:
    if value is None:
        return "--"
    return f"{float(value):.{digits}f}"


def weather_text(code: Any) -> str:
    try:
        numeric = int(code)
    except (TypeError, ValueError):
        return "未知"
    return WMO_ZH.get(numeric, f"未知（WMO {numeric}）")


def wind_direction(degrees: Any) -> str:
    if degrees is None:
        return "--"
    directions = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    return directions[round(float(degrees) / 45) % 8]


def normalize_result(label: str, latitude: float, longitude: float, forecast: dict[str, Any]) -> dict[str, Any]:
    return {
        "location": label,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": forecast.get("timezone"),
        "timezone_abbreviation": forecast.get("timezone_abbreviation"),
        "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "Open-Meteo",
        "source_url": "https://open-meteo.com/",
        "current": forecast.get("current") or {},
        "current_units": forecast.get("current_units") or {},
        "daily": forecast.get("daily") or {},
        "daily_units": forecast.get("daily_units") or {},
    }


def render_text(result: dict[str, Any]) -> str:
    current = result["current"]
    current_units = result["current_units"]
    daily = result["daily"]
    daily_units = result["daily_units"]
    lines = [
        f"地点：{result['location']} ({result['latitude']:.4f}, {result['longitude']:.4f})",
        f"时区：{result.get('timezone') or '--'}",
    ]

    if current:
        lines.extend(
            [
                "",
                f"当前（{current.get('time', '--')}）：{weather_text(current.get('weather_code'))}",
                f"温度 {fmt_number(current.get('temperature_2m'), 1)}{current_units.get('temperature_2m', '°C')}，"
                f"体感 {fmt_number(current.get('apparent_temperature'), 1)}{current_units.get('apparent_temperature', '°C')}，"
                f"湿度 {fmt_number(current.get('relative_humidity_2m'))}{current_units.get('relative_humidity_2m', '%')}",
                f"降水 {fmt_number(current.get('precipitation'), 1)}{current_units.get('precipitation', 'mm')}，"
                f"{wind_direction(current.get('wind_direction_10m'))}风 {fmt_number(current.get('wind_speed_10m'), 1)}{current_units.get('wind_speed_10m', 'km/h')}",
            ]
        )

    times = daily.get("time") or []
    if times:
        lines.extend(["", "逐日预报："])
    for index, date_text in enumerate(times):
        try:
            weekday = WEEKDAY_ZH[datetime.strptime(date_text, "%Y-%m-%d").weekday()]
        except ValueError:
            weekday = ""
        lines.append(
            f"- {date_text} {weekday} {weather_text(at(daily, 'weather_code', index))}；"
            f"{fmt_number(at(daily, 'temperature_2m_min', index), 1)}~{fmt_number(at(daily, 'temperature_2m_max', index), 1)}"
            f"{daily_units.get('temperature_2m_max', '°C')}；"
            f"降水概率 {fmt_number(at(daily, 'precipitation_probability_max', index))}{daily_units.get('precipitation_probability_max', '%')}，"
            f"降水量 {fmt_number(at(daily, 'precipitation_sum', index), 1)}{daily_units.get('precipitation_sum', 'mm')}；"
            f"最大风速 {fmt_number(at(daily, 'wind_speed_10m_max', index), 1)}{daily_units.get('wind_speed_10m_max', 'km/h')}，"
            f"阵风 {fmt_number(at(daily, 'wind_gusts_10m_max', index), 1)}{daily_units.get('wind_gusts_10m_max', 'km/h')}；"
            f"UV {fmt_number(at(daily, 'uv_index_max', index), 1)}；"
            f"日出 {str(at(daily, 'sunrise', index) or '--')[-5:]}，日落 {str(at(daily, 'sunset', index) or '--')[-5:]}"
        )

    lines.extend(
        [
            "",
            f"数据源：{result['source']} ({result['source_url']})",
            f"获取时间：{result['retrieved_at']} UTC",
            "提示：模型预报不等同于官方预警，灾害性天气请同时查看中国气象局及当地部门信息。",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="查询中国地区实时天气和未来 1-10 天预报")
    parser.add_argument("location", nargs="?", help="城市、区县或地名，例如：杭州、深圳南山区")
    parser.add_argument("--latitude", type=float, help="纬度（需与 --longitude 一起使用）")
    parser.add_argument("--longitude", type=float, help="经度（需与 --latitude 一起使用）")
    parser.add_argument("--days", type=int, default=7, choices=range(1, 11), metavar="1-10", help="预报天数（默认 7）")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="输出格式")
    args = parser.parse_args()
    has_lat = args.latitude is not None
    has_lon = args.longitude is not None
    if has_lat != has_lon:
        parser.error("--latitude 和 --longitude 必须同时提供")
    if not args.location and not (has_lat and has_lon):
        parser.error("请提供地名，或同时提供 --latitude 和 --longitude")
    if has_lat and not -90 <= args.latitude <= 90:
        parser.error("纬度必须在 -90 到 90 之间")
    if has_lon and not -180 <= args.longitude <= 180:
        parser.error("经度必须在 -180 到 180 之间")
    return args


def main() -> int:
    args = parse_args()
    try:
        if args.latitude is not None:
            latitude = args.latitude
            longitude = args.longitude
            label = args.location or "用户指定坐标"
        else:
            location = resolve_location(args.location)
            latitude = float(location["latitude"])
            longitude = float(location["longitude"])
            label = location_label(location)
        forecast = fetch_forecast(latitude, longitude, args.days)
        result = normalize_result(label, latitude, longitude, forecast)
    except WeatherError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
