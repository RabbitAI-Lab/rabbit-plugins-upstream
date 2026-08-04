#!/usr/bin/env python3
"""深知晓调用脚本。

固定调用统一接口 credibleChat 能力；不提供 credibleRecall 路径。
"""

import argparse
import configparser
import json
import os
import re
import socket
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.ini"


def _as_bool(value: Optional[str], default: bool = False) -> bool:
    if value is None:
        return default
    value = value.strip()
    if not value:
        return default
    return value.lower() in {"1", "true", "yes", "y", "on"}


def _read_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.read(path, encoding="utf-8")
    return cfg


def _cfg(cfg: configparser.ConfigParser, section: str, key: str, default: str = "") -> str:
    if not cfg.has_section(section):
        return default
    return cfg.get(section, key, fallback=default).strip()


def _pick(*values: Optional[str]) -> str:
    for value in values:
        if value:
            return value.strip()
    return ""


def _build_payload(args: argparse.Namespace, cfg: configparser.ConfigParser) -> Dict[str, Any]:
    defaults = "defaults"
    material = args.material or _as_bool(_cfg(cfg, defaults, "material"), True)
    if args.no_material:
        material = False
    payload: Dict[str, Any] = {
        "input": args.input,
        "safeAnswerType": args.safe_answer_type or _cfg(cfg, defaults, "safe_answer_type", "active"),
        "safeAnswerScope": args.safe_answer_scope or _cfg(cfg, defaults, "safe_answer_scope", "all"),
        "knowledgeServiceType": "credibleChat",
        "credibleChatScope": args.credible_chat_scope or _cfg(cfg, defaults, "credible_chat_scope", "all"),
        "searchMechanism": args.search_mechanism or _cfg(cfg, defaults, "search_mechanism", "autoSearch"),
        "interpretationModel": args.interpretation_model or _cfg(cfg, defaults, "interpretation_model", "autoModel"),
        "material": material,
        "recommendedQuestions": args.recommended_questions or _as_bool(_cfg(cfg, defaults, "recommended_questions"), False),
        "item": False if args.no_item else args.item or _as_bool(_cfg(cfg, defaults, "item"), True),
        "policy": False if args.no_policy else args.policy or _as_bool(_cfg(cfg, defaults, "policy"), True),
        "traceurl": args.traceurl or _as_bool(_cfg(cfg, defaults, "traceurl"), True),
        "stream": args.stream or (not args.no_stream and _as_bool(_cfg(cfg, defaults, "stream"), True)),
    }

    if args.show_reasoning:
        payload["interpretationModel"] = "deepModel"

    request_id = args.request_id or _cfg(cfg, defaults, "request_id")
    if args.auto_request_id and not request_id:
        request_id = uuid.uuid4().hex + uuid.uuid4().hex[:8]

    optional = {
        "area": args.area or _cfg(cfg, defaults, "area"),
        "requestId": request_id,
        "sessionId": args.session_id or _cfg(cfg, defaults, "session_id"),
        "szUserId": args.sz_user_id or _pick(
            os.environ.get("DKNOWC_KNOW_SZ_USER_ID"),
            os.environ.get("DKNOWC_GOV_ZHICHA_SZ_USER_ID"),
            _cfg(cfg, "api", "sz_user_id"),
        ),
    }
    for key, value in optional.items():
        if value:
            payload[key] = value

    return payload


def _read_sse_response(resp: Any) -> str:
    chunks = []
    while True:
        raw_line = resp.readline()
        if not raw_line:
            break
        line = raw_line.decode("utf-8", errors="replace")
        chunks.append(line)
        if line.strip() in {"data: [DONE]", "[DONE]"}:
            break
    return "".join(chunks).replace("\x00", "")


def _post(url: str, api_key: str, payload: Dict[str, Any], timeout: int) -> str:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("api-key", api_key)
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if payload.get("stream"):
                return _read_sse_response(resp)
            return resp.read().decode("utf-8", errors="replace").replace("\x00", "")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="ignore")
        print(f"错误：HTTP {e.code} {detail or e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"错误：网络请求失败 - {e.reason}", file=sys.stderr)
        sys.exit(1)
    except socket.timeout:
        print("错误：接口流式响应读取超时。请确认接口是否持续输出 SSE 数据，或适当增大 --timeout。", file=sys.stderr)
        sys.exit(1)


class _StreamingCleaner:
    def __init__(self) -> None:
        self._buffer = ""
        self._hold_chars = 512

    def feed(self, text: str) -> str:
        self._buffer += text
        if len(self._buffer) <= self._hold_chars:
            return ""
        cut = len(self._buffer) - self._hold_chars

        last_tag_start = self._buffer.rfind("<", 0, cut)
        if last_tag_start != -1:
            next_tag_end = self._buffer.find(">", last_tag_start)
            if next_tag_end == -1 or next_tag_end >= cut:
                cut = last_tag_start

        last_citation_start = max(
            self._buffer.rfind("[^", 0, cut),
            self._buffer.rfind("[", 0, cut),
        )
        if last_citation_start != -1:
            next_citation_end = self._buffer.find("]", last_citation_start)
            if next_citation_end == -1 or next_citation_end >= cut:
                cut = last_citation_start

        safe, self._buffer = self._buffer[:cut], self._buffer[cut:]
        return _format_answer_content(safe)

    def finish(self) -> str:
        text = _format_answer_content(self._buffer)
        self._buffer = ""
        return text


def _post_streaming_to_stdout(url: str, api_key: str, payload: Dict[str, Any], timeout: int) -> None:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("api-key", api_key)
    req.add_header("Content-Type", "application/json")

    cleaner = _StreamingCleaner()
    trace_url = ""
    wrote_content = False

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            while True:
                raw_line = resp.readline()
                if not raw_line:
                    break
                line = raw_line.decode("utf-8", errors="replace").replace("\x00", "").strip()
                if not line.startswith("data:"):
                    continue
                chunk = line[5:].strip()
                if chunk == "[DONE]":
                    break
                try:
                    obj = json.loads(chunk)
                except json.JSONDecodeError:
                    continue

                if isinstance(obj.get("traceUrl"), str):
                    trace_url = obj["traceUrl"].strip()

                piece = _extract_piece(obj)
                if not piece:
                    continue

                cleaned = cleaner.feed(piece)
                if cleaned:
                    print(cleaned, end="", flush=True)
                    wrote_content = True

        tail = cleaner.finish()
        if tail:
            print(tail, end="", flush=True)
            wrote_content = True
        if wrote_content:
            print()
        if trace_url:
            print("\n可信溯源报告")
            print(trace_url)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="ignore")
        print(f"错误：HTTP {e.code} {detail or e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"错误：网络请求失败 - {e.reason}", file=sys.stderr)
        sys.exit(1)
    except socket.timeout:
        print("错误：接口流式响应读取超时。请确认接口是否持续输出 SSE 数据，或适当增大 --timeout。", file=sys.stderr)
        sys.exit(1)


def _iter_sse_payloads(text: str) -> Iterable[Dict[str, Any]]:
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("data:"):
            continue
        chunk = line[5:].strip()
        if chunk == "[DONE]":
            break
        try:
            yield json.loads(chunk)
        except json.JSONDecodeError:
            continue


def _merge_sse_result(text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    resp: Dict[str, Any] = {}
    content_parts = []
    reasoning_parts = []

    for obj in _iter_sse_payloads(text):
        for key in ("requestId", "sessionId", "safeType", "knowledgeScope", "created", "area", "traceUrl"):
            if key in obj and key not in result:
                result[key] = obj[key]

        for key in ("referenceMaterials", "recommendationItems", "policyFiles"):
            if key in obj and key not in result:
                result[key] = obj[key]

        chunk_resp = obj.get("resp")
        if isinstance(chunk_resp, dict):
            for key in ("waitText", "areaTip"):
                if key in chunk_resp and key not in resp:
                    resp[key] = chunk_resp[key]
            content = chunk_resp.get("content")
            if isinstance(content, str):
                content_parts.append(content)
            reasoning = chunk_resp.get("reasoning_content")
            if isinstance(reasoning, str):
                reasoning_parts.append(reasoning)

        choices = obj.get("choices")
        if isinstance(choices, list) and choices:
            delta = choices[0].get("delta", {})
            if isinstance(delta, dict):
                for key in ("waitText", "areaTip"):
                    if key in delta and key not in resp:
                        resp[key] = delta[key]
                content = delta.get("content")
                if isinstance(content, str):
                    content_parts.append(content)
                reasoning = delta.get("reasoning_content")
                if isinstance(reasoning, str):
                    reasoning_parts.append(reasoning)

    if content_parts:
        resp["content"] = "".join(content_parts)
    if reasoning_parts:
        resp["reasoning_content"] = "".join(reasoning_parts)
    if resp:
        result["resp"] = resp
    return result


def _normalize_result(text: str) -> Dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        return {"resp": {"content": ""}}
    if "data:" in stripped:
        return _merge_sse_result(stripped)
    try:
        body = json.loads(stripped)
    except json.JSONDecodeError:
        return {"resp": {"content": stripped}}
    if isinstance(body, dict):
        return body
    return {"resp": {"content": body}}


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def _format_answer_content(text: str) -> str:
    cleaned = _strip_html(text)
    return re.sub(r"\[\^?\d+\^?\]", "", cleaned)


def _print_trace_report(result: Dict[str, Any]) -> None:
    trace_url = result.get("traceUrl")
    if isinstance(trace_url, str) and trace_url.strip():
        print("\n可信溯源报告")
        print(trace_url.strip())


def _print_summary(result: Dict[str, Any], show_reasoning: bool) -> None:
    resp = result.get("resp", {})
    if isinstance(resp, dict):
        if resp.get("waitText"):
            print(resp["waitText"])
        if resp.get("areaTip"):
            print(resp["areaTip"])

        content = resp.get("content")
        if content:
            print(_format_answer_content(content))

        reasoning = resp.get("reasoning_content")
        if show_reasoning and reasoning:
            print(f"\n模型思考过程：\n{reasoning}")
    elif resp:
        print(resp)

    _print_trace_report(result)


def _print_result(text: str, raw: bool, json_only: bool, show_reasoning: bool) -> None:
    result = _normalize_result(text)

    if json_only:
        print(json.dumps({"success": True, "data": result}, ensure_ascii=False, indent=2))
        return

    _print_summary(result, show_reasoning)
    if raw:
        print("\n=== RAW_RESPONSE_START ===")
        print(text.strip())
        print("=== RAW_RESPONSE_END ===")


def _extract_piece(obj: Dict[str, Any]) -> str:
    choices = obj.get("choices")
    if isinstance(choices, list) and choices:
        delta = choices[0].get("delta", {})
        if isinstance(delta, dict):
            for key in ("content", "reasoning_content", "areaTip", "waitText"):
                value = delta.get(key)
                if isinstance(value, str):
                    return value

    resp = obj.get("resp")
    if isinstance(resp, dict):
        content = resp.get("content")
        if isinstance(content, str):
            return content

    content = obj.get("content")
    if isinstance(content, str):
        return content
    return ""


def main() -> None:
    parser = argparse.ArgumentParser(description="深知晓 credibleChat 调用脚本")
    parser.add_argument("input", help="用户政务问题")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="配置文件路径")
    parser.add_argument("--endpoint", help="覆盖接口地址")
    parser.add_argument("--api-key", help="覆盖 API Key")
    parser.add_argument("--sz-user-id", help="覆盖 szUserId")
    parser.add_argument("--area", help="覆盖地域")
    parser.add_argument("--session-id", help="覆盖 sessionId")
    parser.add_argument("--request-id", help="覆盖 requestId")
    parser.add_argument("--auto-request-id", action="store_true", help="未传 requestId 时自动生成")
    parser.add_argument("--safe-answer-scope", choices=["none", "all", "risk"], help="覆盖安全代答范围")
    parser.add_argument("--safe-answer-type", choices=["active", "conservative"], help="覆盖安全代答模式")
    parser.add_argument("--credible-chat-scope", choices=["onlyNorms", "needNorms", "all"], help="覆盖可信问答范围")
    parser.add_argument("--search-mechanism", choices=["quickSearch", "autoSearch", "deepSearch"], help="覆盖搜索机制")
    parser.add_argument("--interpretation-model", choices=["autoModel", "fastModel", "deepModel"], help="覆盖解读模型")
    parser.add_argument("--material", action="store_true", help="返回参考材料")
    parser.add_argument("--no-material", action="store_true", help="不返回参考材料")
    parser.add_argument("--recommended-questions", action="store_true", help="返回推荐问题")
    parser.add_argument("--item", action="store_true", help="返回办理事项")
    parser.add_argument("--no-item", action="store_true", help="不返回办理事项")
    parser.add_argument("--policy", action="store_true", help="返回政策文件")
    parser.add_argument("--no-policy", action="store_true", help="不返回政策文件")
    parser.add_argument("--traceurl", action="store_true", help="返回可信溯源报告链接")
    parser.add_argument("--stream", action="store_true", help="开启流式返回")
    parser.add_argument("--no-stream", action="store_true", help="关闭流式")
    parser.add_argument("--show-payload", action="store_true", help="打印请求参数")
    parser.add_argument("--dry-run", action="store_true", help="只打印请求参数，不发起请求")
    parser.add_argument("--raw", action="store_true", help="打印原始响应")
    parser.add_argument("--json-only", action="store_true", help="仅输出聚合后的 JSON")
    parser.add_argument("--show-reasoning", action="store_true", help="显示 deepModel 思考过程，并自动使用 deepModel")
    parser.add_argument("--timeout", type=int, default=90, help="请求超时秒数")
    args = parser.parse_args()

    cfg = _read_config(Path(args.config))
    endpoint = _pick(
        args.endpoint,
        os.environ.get("DKNOWC_KNOW_ENDPOINT"),
        os.environ.get("DKNOWC_GOV_ZHICHA_ENDPOINT"),
        _cfg(cfg, "api", "endpoint"),
    )
    api_key = _pick(
        args.api_key,
        os.environ.get("DKNOWC_KNOW_API_KEY"),
        os.environ.get("DKNOWC_GOV_ZHICHA_API_KEY"),
        _cfg(cfg, "api", "api_key"),
    )

    if not endpoint:
        print("错误：缺少 endpoint，请在 config.ini 的 [api] 中配置。", file=sys.stderr)
        sys.exit(2)
    if not api_key:
        print("错误：缺少 api_key，请在 config.ini 的 [api] 中配置，或使用 --api-key 临时传入。", file=sys.stderr)
        sys.exit(2)

    payload = _build_payload(args, cfg)
    if args.show_payload:
        safe_payload = dict(payload)
        print("=== 请求参数 ===")
        print(json.dumps(safe_payload, ensure_ascii=False, indent=2))
        print()
    if args.dry_run:
        return

    if payload.get("stream") and not (args.raw or args.json_only or args.show_reasoning):
        _post_streaming_to_stdout(endpoint, api_key, payload, args.timeout)
        return

    text = _post(endpoint, api_key, payload, args.timeout)
    _print_result(text, args.raw, args.json_only, args.show_reasoning)


if __name__ == "__main__":
    main()
