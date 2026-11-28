"""星盘大师开放API客户端（独立版）。

Skill 核心调用库。无需安装为包，直接导入使用。

Usage:
    from astro_client import AstroClient
    client = AstroClient(api_key="zs_xxx...")
    result = client.calculate_chart(date="1990-05-15", time="14:30", timezone="+08:00", lat=39.9, lon=116.4)
"""

import json
import logging
import os
import time
from typing import Any, Optional

import requests

logger = logging.getLogger("astro_client")


# ── 异常定义 ──────────────────────────────────────────────

class AstroApiError(Exception):
    """API通用错误。"""
    def __init__(self, message: str, code: int = -1, status_code: int = 0):
        super().__init__(message)
        self.code = code
        self.status_code = status_code


class AuthenticationError(AstroApiError):
    """认证失败（密钥无效或过期）。"""
    pass


class RateLimitError(AstroApiError):
    """限流/额度用尽。"""
    pass


class ServiceUnavailableError(AstroApiError):
    """服务不可用。"""
    def __init__(self, api_key_prefix: str = "", username: str = ""):
        msg = f"当前账号{username}({api_key_prefix}...)算力接口不可用，请联系管理员"
        super().__init__(msg, status_code=503)


# ── 城市结果本地优先重排（客户端侧兜底，不改服务端排序）──────

# 语言前缀 → 优先国家（匹配结果中的 country_cn / country）
_LOCALE_PREF_COUNTRY = {
    "zh": {"中国", "CN", "China"},
}


def _reorder_cities_by_locale(result: Any, lang: str) -> Any:
    """按用户 locale 优先重排城市搜索结果（稳定排序，仅客户端兜底）。

    例如 lang=zh 时把「中国」结果提到前面，避免同名城市（如检索「北京」误取美国伊利诺伊州坐标）。
    不修改服务端返回结构与排序，只做本地二次排序，组内保持服务端原顺序。
    """
    if not isinstance(result, list) or not result:
        return result
    pref = _LOCALE_PREF_COUNTRY.get((lang or "").split("-")[0].lower())
    if not pref:
        return result

    def _rank(city: dict) -> int:
        if not isinstance(city, dict):
            return 1
        country = (city.get("country_cn") or city.get("country") or "").strip()
        return 0 if country in pref else 1

    return sorted(result, key=_rank)  # 稳定排序


# ── 错误体解析（兼容 str / list / dict / 嵌套 detail 四形态）───

def _parse_error_detail(payload: Any) -> str:
    """从 4xx 响应体提取可读错误文本（仅用于日志，不直接透给用户）。

    兼容四种形态：
      - {"detail": "..."}                       ← 后端 400（值转换失败）常见
      - {"detail": [ {...}, ... ]}              ← 标准 FastAPI 422
      - {"detail": {"detail": [...] }}          ← 本服务端实际嵌套 422
      - {"detail": {"detail": "..." }}          ← 嵌套 400
    """
    if not isinstance(payload, dict):
        return ""
    detail = payload.get("detail")
    for _ in range(3):                       # 防御性解嵌套
        if isinstance(detail, dict) and isinstance(detail.get("detail"), (dict, list, str)):
            detail = detail["detail"]
        else:
            break
    if isinstance(detail, dict):
        return str(detail.get("message") or detail)
    if isinstance(detail, list):
        parts = []
        for item in detail:
            if isinstance(item, dict):
                loc = ".".join(str(x) for x in item.get("loc", []) if x != "body")
                parts.append(f"{loc}: {item.get('msg', '')}".strip(": "))
            else:
                parts.append(str(item))
        return "；".join(p for p in parts if p)
    return detail if isinstance(detail, str) else ""


def _parse_validation_error(payload: Any) -> str:
    """从 422 响应体提取可读校验错误信息（兼容单层 / 嵌套 detail 结构）。"""
    msg = _parse_error_detail(payload)
    return f"参数校验失败: {msg}" if msg else "参数校验失败"


# 面向用户的 4xx 友好文案（脱敏：不回传 invalid literal / could not convert 等内部字样）
_4XX_ZH = {
    400: "请求参数无法解析，请检查日期/时间格式与经纬度数值后重试",
    403: "无权访问该接口",
    404: "接口不存在",
    405: "请求方法不被允许",
}


def _friendly_4xx_message(status: int) -> str:
    return _4XX_ZH.get(status, f"请求失败 (HTTP {status})")


# ── 客户端主类 ────────────────────────────────────────────

class AstroClient:
    """星盘大师开放API客户端，支持14项占星能力。"""

    DEFAULT_BASE_URL = "https://api.astro.jiuchongju.com"

    def __init__(self, api_key: str, base_url: Optional[str] = None, timeout: int = 10, username: str = ""):
        if not api_key:
            raise ValueError("api_key 不能为空")
        self.api_key = api_key
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.username = username
        self._session = requests.Session()
        self._session.headers.update({
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "AstroMaster-Python-Client/2.0.0",
        })

    # ── 功能1: 地理编码 ──

    def search_city(self, keyword: str, limit: int = 5, country: Optional[str] = None, lang: str = "zh") -> list:
        """搜索城市获取经纬度坐标。结果按用户 locale 优先重排（客户端侧兜底）。"""
        params = {"keyword": keyword, "limit": str(limit), "lang": lang}
        if country:
            params["country"] = country
        result = self._request("GET", "/api/v1/open/cities/search", params=params)
        return _reorder_cities_by_locale(result, lang)

    # ── 功能3: 本命排盘 ──

    def calculate_chart(self, date: str, time: str, timezone: str, lat: float, lon: float, hsys: str = "P", gender: str = "male") -> dict:
        """本命排盘计算（基础版：行星+宫位+相位）。lat/lon 服务端要求字符串，组装时转换。"""
        payload = {"date": date, "time": time, "timezone": timezone, "lat": str(lat), "lon": str(lon), "hsys": hsys, "gender": gender}
        return self._request("POST", "/api/v1/open/chart/calculate", json=payload)

    def calculate_full_chart(self, date: str, time: str, timezone: str, lat: float, lon: float, hsys: str = "P", gender: str = "male") -> dict:
        """全量排盘分析（含尊贵度+阿拉伯点+气质+行为+动力学+本命解读）。lat/lon 服务端要求字符串，组装时转换。"""
        payload = {"date": date, "time": time, "timezone": timezone, "lat": str(lat), "lon": str(lon), "hsys": hsys, "gender": gender}
        return self._request("POST", "/api/v1/open/chart/full-analysis", json=payload)

    def generate_pdf_report(self, date: str, time: str, timezone: str, lat: float, lon: float, hsys: str = "P", gender: str = "male", name: str = "", locale: str = "zh-CN") -> dict:
        """生成本命盘 PDF 报告，返回下载链接（有效期48小时，无需鉴权即可下载）。lat/lon 服务端要求字符串，组装时转换。"""
        payload = {"date": date, "time": time, "timezone": timezone, "lat": str(lat), "lon": str(lon), "hsys": hsys, "gender": gender, "name": name, "locale": locale}
        return self._request("POST", "/api/v1/open/chart/pdf-report", json=payload)

    # ── 功能15: 过运盘 ──

    def calculate_transit(self, birth_date: str, latitude: float, longitude: float, birth_time: str = "12:00", timezone: str = "+08:00", target_date: str = "", period_days: int = 30) -> dict:
        """过运盘计算：过运行星位置、过运-本命相位（含精确成相日期/状态）、期间行星事件。

        注意：/chart/transit 的 latitude/longitude 后端契约要求数值型（与 /chart/calculate 等要求字符串相反），
        故此处保持 float，不做字符串化。target_date 为空时不传该字段，避免触发额外校验分支。
        """
        payload = {
            "birth_date": birth_date, "birth_time": birth_time,
            "latitude": float(latitude), "longitude": float(longitude),
            "timezone": timezone, "period_days": period_days,
        }
        if target_date:
            payload["target_date"] = target_date
        return self._request("POST", "/api/v1/open/chart/transit", json=payload)

    # ── 功能4: 个人每日运势 ──

    def get_personal_daily_horoscope(self, birth_date: str) -> dict:
        """获取个人每日运势（根据出生日期推导太阳星座）。"""
        return self._request("GET", "/api/v1/open/horoscope/daily/personal", params={"birth_date": birth_date})

    # ── 功能5-7: 个人期间运势 ──

    def get_personal_horoscope(self, period: str, birth_date: str, birth_time: str, lat: float, lon: float, timezone: str = "+08:00") -> dict:
        """获取个人周/月/年运势。period: weekly/monthly/yearly"""
        params = {"birth_date": birth_date, "birth_time": birth_time, "latitude": str(lat), "longitude": str(lon), "timezone": timezone}
        return self._request("GET", f"/api/v1/open/horoscope/{period}/basic", params=params)

    # ── 功能8: 十二星座每日运势 ──

    def get_daily_horoscope(self, date: Optional[str] = None) -> dict:
        """获取12星座每日运势概况。"""
        params = {"date": date} if date else {}
        return self._request("GET", "/api/v1/open/horoscope/daily", params=params)

    # ── 功能9: 指定星座每日运势 ──

    def get_daily_horoscope_by_sign(self, sign: str, date: Optional[str] = None) -> dict:
        """获取指定星座每日运势详情。"""
        params = {"date": date} if date else {}
        return self._request("GET", f"/api/v1/open/horoscope/daily/{sign}", params=params)

    # ── 功能10-12: 指定星座期间运势 ──

    def get_sign_period_horoscope(self, period: str, sign: str) -> dict:
        """获取指定星座的周/月/年运势。period: weekly/monthly/yearly"""
        return self._request("GET", f"/api/v1/open/horoscope/{period}/public/{sign}")

    # ── 功能13: 调用记录 ──

    def get_call_logs(self, limit: int = 10) -> list:
        """查询当前API-KEY最近调用记录。"""
        result = self._request("GET", "/api/v1/open/call-logs", params={"limit": str(limit)})
        return result.get("items", []) if isinstance(result, dict) else result

    # ── 内部方法 ──

    def _request(self, method: str, path: str, params: Optional[dict] = None, json: Optional[dict] = None) -> Any:
        url = f"{self.base_url}{path}"
        key_prefix = self.api_key[:12] if len(self.api_key) >= 12 else self.api_key
        logger.info("→ %s %s", method, path)
        start = time.time()
        try:
            resp = self._session.request(method, url, params=params, json=json, timeout=self.timeout)
        except (requests.ConnectionError, requests.Timeout, requests.RequestException) as exc:
            elapsed = int((time.time() - start) * 1000)
            logger.error("✗ %s %s 连接失败 (%dms): %s", method, path, elapsed, exc)
            raise ServiceUnavailableError(api_key_prefix=key_prefix, username=self.username)

        elapsed = int((time.time() - start) * 1000)

        if resp.status_code == 401:
            logger.error("✗ %s %s 认证失败 (%dms) HTTP 401", method, path, elapsed)
            raise AuthenticationError("API密钥无效或已过期，请到 https://astro.jiuchongju.com 重新申请获取")
        if resp.status_code == 422:
            # 参数校验错误：兼容单层与嵌套 detail，输出可读信息（内部字样仅落日志，不向用户暴露）
            try:
                msg = _parse_validation_error(resp.json())
            except Exception:
                msg = f"参数校验失败 (HTTP 422): {resp.text[:200]}"
            logger.error("✗ %s %s 参数校验失败 (%dms): %s", method, path, elapsed, msg)
            raise AstroApiError(msg, code=422, status_code=422)
        if resp.status_code == 429:
            # 透传后端可配置超限文案（含官网链接与申请指引），解析失败回退通用提示
            fallback = f"当前账号{self.username}({key_prefix}...)每日调用额度已用尽，请前往 https://astro.jiuchongju.com 申请提升额度或联系管理员"
            try:
                detail = resp.json().get("detail")
                m = detail.get("message") if isinstance(detail, dict) else detail
                m = m or fallback
            except Exception:
                m = fallback
            logger.error("✗ %s %s 限流 (%dms) HTTP 429: %s", method, path, elapsed, m)
            raise RateLimitError(m, code=429, status_code=429)
        if resp.status_code >= 500:
            logger.error("✗ %s %s 服务异常 (%dms) HTTP %d", method, path, elapsed, resp.status_code)
            raise ServiceUnavailableError(api_key_prefix=key_prefix, username=self.username)

        # 非 2xx 兜底：401/422/429/>=500 已在上方显式处理，这里覆盖其余 4xx（400/403/404/405…）。
        # 关键：无信封兼容分支必须只作用于 2xx，否则 400 错误体（恰好无 code 字段）会被当成功数据返回。
        if not (200 <= resp.status_code < 300):
            try:
                payload = resp.json()
            except ValueError:
                payload = None
            raw = _parse_error_detail(payload)
            logger.error("✗ %s %s HTTP %d (%dms): %s", method, path, resp.status_code, elapsed, raw)
            raise AstroApiError(
                _friendly_4xx_message(resp.status_code),
                code=resp.status_code,
                status_code=resp.status_code,
            )

        try:
            data = resp.json()
        except ValueError:
            logger.error("✗ %s %s 响应解析失败 (%dms) HTTP %d", method, path, elapsed, resp.status_code)
            raise AstroApiError(f"响应解析失败: HTTP {resp.status_code}", status_code=resp.status_code)

        # 无统一信封兼容：HTTP 200 且顶层不是 {code, ...} 信封结构（如 /chart/transit 直接返回对象/数组）
        # → 视作成功，直接返回原始数据。该判断通用，覆盖同类无信封接口。分支仅记录在日志，不暴露给用户。
        if isinstance(data, list):
            logger.debug("无信封响应(list): %s", path)
            return data
        if isinstance(data, dict) and "code" not in data:
            logger.debug("无信封响应(dict): %s", path)
            return data

        code = data.get("code", -1)
        if code != 0 and code != 200:
            detail = data.get("detail")
            if detail and isinstance(detail, dict):
                msg = detail.get("message", str(detail))
                code = detail.get("code", code)
            elif detail and isinstance(detail, str):
                msg = detail
            else:
                msg = data.get("message", f"未知错误 (HTTP {resp.status_code}, code={code})")
            logger.warning("✗ %s %s 业务错误 (%dms) code=%s: %s", method, path, elapsed, code, msg)
            raise AstroApiError(msg, code=code, status_code=resp.status_code)

        logger.info("✓ %s %s (%dms)", method, path, elapsed)
        return data.get("data", {})

    def __repr__(self) -> str:
        prefix = self.api_key[:12] if len(self.api_key) >= 12 else "***"
        return f"AstroClient(base_url='{self.base_url}', key='{prefix}...')"


# ── 便捷加载 ──────────────────────────────────────────────

def _is_placeholder_key(key: str) -> bool:
    """判断密钥是否为未替换的 BYOK 占位符（形如 ${ASTRO_API_KEY}）。"""
    return bool(key) and key.startswith("${") and key.endswith("}")


def load_client_from_config() -> AstroClient:
    """从同目录 config.json 或环境变量加载配置创建客户端。"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    api_key = os.environ.get("ASTRO_API_KEY", config.get("api_key", ""))
    base_url = os.environ.get("ASTRO_BASE_URL", config.get("base_url", "https://api.astro.jiuchongju.com"))
    username = config.get("username", "")
    if _is_placeholder_key(api_key):
        raise ValueError(
            "未配置 API 密钥：当前值 ${ASTRO_API_KEY} 为占位符。"
            "请设置环境变量 ASTRO_API_KEY，或将 config.json 的 api_key 改为你的真实密钥。"
        )
    return AstroClient(api_key=api_key, base_url=base_url, username=username)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s %(message)s")
    client = load_client_from_config()
    print(f"客户端: {client}")
    print("正在获取今日运势...")
    result = client.get_daily_horoscope()
    print(json.dumps(result, ensure_ascii=False, indent=2)[:500])
