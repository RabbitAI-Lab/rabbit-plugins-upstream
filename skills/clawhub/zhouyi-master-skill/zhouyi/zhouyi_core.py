#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zhouyi_core — 常量、错误类型与 HTTP 传输层。

开放 API 约定（与 jcjasp-backend /api/open/** 保持一致）：
  - 鉴权头：X-API-Key（官网注册获取）；来源标识头：X-Open-Source（默认 skill）
  - 统一响应：{"code":0,"message":"ok","data":{...},"render":{"html":"..."},"meta":{...}}
  - 错误码：40001 参数错误 / 40101 KEY 无效 / 40301 额度过期 /
            42901 每日额度用尽 / 50301 算力接口不可用

依赖：requests 优先，未安装时自动回退标准库 urllib。
"""

from __future__ import annotations

import json
import os
import shlex
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urlsplit, urlunsplit

try:
    import requests as _requests  # 优先使用 requests
except ImportError:  # pragma: no cover - 未安装 requests 时回退 urllib
    _requests = None
    import urllib.request
    import urllib.error

__version__ = "1.1.0"

DEFAULT_BASE_URL = "https://api.iching.jiuchongju.com"
API_KEY_ENV = "ZHOUYI_API_KEY"
DEFAULT_OPEN_SOURCE = "skill"

# 错误码说明（规格 11.3，与 OpenApiErrorCode 对齐）
ERROR_MESSAGES = {
    40001: "参数缺失或格式错误",
    40101: "API-KEY无效或已失效",
    40301: "额度有效期已过期",
    42901: "每日调用额度已用完",
    50301: "算力接口不可用",
}


class ZhouyiApiError(Exception):
    """开放平台业务/传输错误，含业务码 code、描述 message、HTTP 状态码 http_status。"""

    def __init__(self, code: int, message: str, http_status: Optional[int] = None,
                 raw: Any = None):
        super().__init__(f"[{code}] {message}" + (f" (HTTP {http_status})" if http_status else ""))
        self.code = code
        self.message = message
        self.http_status = http_status
        self.raw = raw


def load_package_config(config_path: Optional[str] = None) -> Dict[str, str]:
    """仅读取包内约定的标量字段，不搜索工作目录、不执行 YAML 标签。"""
    root = Path(__file__).resolve().parent.parent
    candidates = [Path(config_path)] if config_path is not None else [
        root / "config.yaml", root.parent / "config.yaml"]
    path = next((p for p in candidates if p.is_file()), None)
    if path is None:
        if config_path is not None:
            raise ValueError("指定的配置文件不存在")
        return {}
    config = {}
    section = ""
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.strip().split(":", 1)
        if not line[0].isspace():
            section = key if not value.strip() else ""
        field = "base_url" if section == "endpoint" and key == "base_url" else key
        if (section and section != "endpoint") or field not in {
                "api_key", "base_url", "open_source", "timeout"} or not value.strip():
            continue
        try:
            scalar = " ".join(shlex.split(value, comments=True)).strip()
        except ValueError:
            raise ValueError(f"配置字段 {field} 的引号格式错误") from None
        if scalar and not scalar.startswith(("{", "${", "!", "[", "|", ">")):
            config[field] = scalar
    return config


def normalize_base_url(url: Optional[str]) -> str:
    """服务根地址：去除 /api、/api/open 尾缀，保留反代子路径。"""
    parts = urlsplit((url or DEFAULT_BASE_URL).strip())
    if parts.scheme not in {"http", "https"} or not parts.netloc or parts.query or parts.fragment:
        raise ValueError("base_url 必须为不含查询参数或片段的 HTTP(S) 服务地址")
    path = parts.path.rstrip("/")
    while path.lower().endswith(("/api/open", "/api")):
        suffix = "/api/open" if path.lower().endswith("/api/open") else "/api"
        path = path[:-len(suffix)].rstrip("/")
    return urlunsplit((parts.scheme, parts.netloc, path, "", ""))


def _config_value(explicit, env: str, config: Dict[str, str], field: str, default=None):
    if explicit is not None:
        return explicit
    return os.environ.get(env, "").strip() or config.get(field) or default


class ZhouyiClientBase:
    """周易大师开放平台客户端基础类（传输层）。

    :param base_url: 服务地址，默认 https://api.iching.jiuchongju.com（可用环境变量
                     ZHOUYI_BASE_URL 覆盖，本地开发如 http://localhost:8090）
    :param api_key:  官网注册获取的 API-KEY（也可通过环境变量 ZHOUYI_API_KEY 提供）
    :param open_source: X-Open-Source 来源标识，默认 skill（mcp/api 等可配置）
    :param timeout: 请求超时秒数
    """

    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None,
                 open_source: Optional[str] = None, timeout: Optional[float] = None,
                 config_path: Optional[str] = None):
        config = load_package_config(config_path)
        self.base_url = normalize_base_url(_config_value(
            base_url, "ZHOUYI_BASE_URL", config, "base_url", DEFAULT_BASE_URL))
        self.api_key = _config_value(api_key, API_KEY_ENV, config, "api_key")
        self.open_source = _config_value(
            open_source, "ZHOUYI_OPEN_SOURCE", config, "open_source", DEFAULT_OPEN_SOURCE)
        self.timeout = float(_config_value(timeout, "ZHOUYI_TIMEOUT", config, "timeout", 30.0))
        if self.timeout <= 0:
            raise ValueError("timeout 必须大于 0")

    # ==================== 底层请求 ====================

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/json",
            "X-Open-Source": self.open_source,
        }
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        return headers

    def _request(self, method: str, path: str, body: Optional[Dict] = None,
                 params: Optional[Dict] = None) -> Dict:
        url = self.base_url + path
        if params:
            cleaned = {k: v for k, v in params.items() if v is not None}
            if cleaned:
                url += "?" + urlencode(cleaned)
        headers = self._headers()

        if _requests is not None:
            try:
                resp = _requests.request(
                    method, url,
                    json=body if method.upper() == "POST" else None,
                    headers=headers, timeout=self.timeout)
            except _requests.RequestException as exc:
                raise ZhouyiApiError(-1, f"网络请求失败: {exc}") from exc
            http_status = resp.status_code
            text = resp.text
        else:
            data = None
            if method.upper() == "POST":
                data = json.dumps(body if body is not None else {}, ensure_ascii=False).encode("utf-8")
                headers["Content-Type"] = "application/json; charset=utf-8"
            req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    http_status = resp.status
                    text = resp.read().decode("utf-8")
            except urllib.error.HTTPError as exc:
                http_status = exc.code
                text = exc.read().decode("utf-8", errors="replace")
            except urllib.error.URLError as exc:
                raise ZhouyiApiError(-1, f"网络请求失败: {exc.reason}") from exc

        return self._parse_response(text, http_status)

    @staticmethod
    def _parse_response(text: str, http_status: int) -> Dict:
        try:
            payload = json.loads(text)
        except (ValueError, TypeError):
            raise ZhouyiApiError(-1, f"非 JSON 响应（HTTP {http_status}）: {text[:200]}",
                                 http_status=http_status, raw=text)
        if not isinstance(payload, dict):
            raise ZhouyiApiError(-1, "响应结构异常：缺少顶层 JSON 对象",
                                 http_status=http_status, raw=payload)
        code = payload.get("code", 0)
        if code != 0:
            raise ZhouyiApiError(code, payload.get("message") or ERROR_MESSAGES.get(code, "未知错误"),
                                 http_status=http_status, raw=payload)
        if http_status >= 400:
            raise ZhouyiApiError(code or http_status,
                                 payload.get("message") or f"HTTP {http_status}",
                                 http_status=http_status, raw=payload)
        return payload

    def _post(self, path: str, body: Dict) -> Dict:
        return self._request("POST", path, body={k: v for k, v in body.items() if v is not None})

    def _get(self, path: str, params: Optional[Dict] = None) -> Dict:
        return self._request("GET", path, params=params)
