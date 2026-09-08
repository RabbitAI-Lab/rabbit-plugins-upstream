#!/usr/bin/env python3
"""Call one AIDSO GEO submit or query endpoint without polling or saving tokens."""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://openapi.aidso.com"
TIMEOUT_SECONDS = 60
PLATFORM_MODES = {
    "DB": {0, 1},
    "DOUBA": {0, 1},
    "DP": {0, 1},
    "DPA": {0, 1},
    "TXYB": {0, 1},
    "TXYBA": {0, 1},
    "TYQW": {0, 1},
    "TYQWA": {0, 1},
    "BDAI": {0},
    "WXYY": {0, 1},
    "KIMI": {0, 1},
    "DYAI": {0, 1},
    "XHSA": {0},
}


class AidsoApiError(ValueError):
    """Represent a safe, non-secret API or transport failure."""


def validate_base_url(value: str) -> str:
    candidate = value.rstrip("/")
    parsed = urlsplit(candidate)
    hostname = (parsed.hostname or "").lower()
    official = parsed.scheme == "https" and hostname == "openapi.aidso.com"
    local_test = parsed.scheme == "http" and hostname in {"127.0.0.1", "localhost"}
    if not (official or local_test) or parsed.username or parsed.password:
        raise AidsoApiError("API 地址必须是官方 HTTPS 地址")
    return candidate


def read_token(*, token_stdin: bool) -> str:
    if token_stdin:
        token = sys.stdin.readline().strip()
    else:
        token = os.environ.get("AIDSO_TOKEN", "").strip()
    if not token:
        raise AidsoApiError("未绑定 API 密钥；请通过当前会话输入或 AIDSO_TOKEN 安全注入")
    if any(character in token for character in "\r\n"):
        raise AidsoApiError("API 密钥格式无效")
    return token


def request_json(request: Request) -> dict[str, Any]:
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read()
    except HTTPError as exc:
        raise AidsoApiError(f"HTTP 请求失败：{exc.code}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise AidsoApiError("网络请求失败或结果不明确；不得自动重试付费提交") from exc
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AidsoApiError("API 返回的不是有效 UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise AidsoApiError("API 返回结构无效")
    code = payload.get("code")
    if code != 200:
        meanings = {
            400: "reqId 未提交",
            401: "API 密钥未授权或已失效",
            405: "请求参数错误",
            406: "积分不足",
            429: "请求频繁",
            500: "服务异常",
        }
        meaning = meanings.get(code, "未知 API 错误")
        raise AidsoApiError(f"爱搜 API 返回 {code}：{meaning}")
    return payload


def submit_conversation(
    token: str,
    prompt: str,
    platform: str,
    thinking_enabled: int,
    *,
    base_url: str = DEFAULT_BASE_URL,
) -> dict[str, Any]:
    prompt = prompt.strip()
    code = platform.strip().upper()
    if not prompt:
        raise AidsoApiError("prompt 不得为空")
    if code not in PLATFORM_MODES:
        raise AidsoApiError(f"不支持的平台编码：{code}")
    if thinking_enabled not in PLATFORM_MODES[code]:
        raise AidsoApiError(f"{code} 不支持 thinking_enabled={thinking_enabled}")
    body = json.dumps(
        {"prompt": prompt, "name": code, "thinking_enabled": thinking_enabled},
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    request = Request(
        validate_base_url(base_url) + "/geo_api/task_commit",
        data=body,
        headers={
            "aidso-token": token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    payload = request_json(request)
    request_id = str(payload.get("data") or "").strip()
    if not request_id:
        raise AidsoApiError("提交成功响应缺少 reqId；结果状态不明确，不得自动重试")
    return {
        "request_id": request_id,
        "platform": code,
        "thinking_enabled": thinking_enabled,
        "api_code": 200,
    }


def query_result(
    token: str,
    req_id: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
) -> dict[str, Any]:
    req_id = req_id.strip()
    if not req_id:
        raise AidsoApiError("reqId 不得为空")
    query = urlencode({"reqId": req_id})
    request = Request(
        validate_base_url(base_url) + "/geo_api/get_result?" + query,
        headers={"aidso-token": token, "Accept": "application/json"},
        method="GET",
    )
    payload = request_json(request)
    data = payload.get("data")
    if not isinstance(data, dict):
        raise AidsoApiError("查询成功响应缺少 data 对象")
    status = str(data.get("status") or "UNKNOWN").upper()
    return {
        "request_id": req_id,
        "status": status,
        "complete": status == "SUCCESS",
        "data": data,
        "api_code": 200,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument(
        "--token-stdin",
        action="store_true",
        help="从标准输入第一行读取当前会话密钥；否则读取 AIDSO_TOKEN",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    submit = subparsers.add_parser("submit")
    submit.add_argument("--prompt", required=True)
    submit.add_argument("--platform", required=True)
    submit.add_argument("--thinking-enabled", required=True, type=int, choices=(0, 1))

    query = subparsers.add_parser("query")
    query.add_argument("--req-id", required=True)

    args = parser.parse_args()
    try:
        token = read_token(token_stdin=args.token_stdin)
        if args.command == "submit":
            result = submit_conversation(
                token,
                args.prompt,
                args.platform,
                args.thinking_enabled,
                base_url=args.base_url,
            )
        else:
            result = query_result(token, args.req_id, base_url=args.base_url)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except AidsoApiError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
