#!/usr/bin/env python3
"""深知政务智查调用脚本。

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
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


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
    material = args.material or _as_bool(_cfg(cfg, defaults, "material"), False)
    if args.no_material:
        material = False
    payload: Dict[str, Any] = {
        "input": args.input,
        "safeAnswerType": args.safe_answer_type or _cfg(cfg, defaults, "safe_answer_type", "active"),
        "safeAnswerScope": args.safe_answer_scope or _cfg(cfg, defaults, "safe_answer_scope", "all"),
        "knowledgeServiceType": "credibleChat",
        "credibleChatScope": args.credible_chat_scope or _cfg(cfg, defaults, "credible_chat_scope", "onlyNorms"),
        "searchMechanism": args.search_mechanism or _cfg(cfg, defaults, "search_mechanism", "autoSearch"),
        "interpretationModel": args.interpretation_model or _cfg(cfg, defaults, "interpretation_model", "autoModel"),
        "material": material,
        "recommendedQuestions": args.recommended_questions or _as_bool(_cfg(cfg, defaults, "recommended_questions"), False),
        "item": False if args.no_item else args.item or _as_bool(_cfg(cfg, defaults, "item"), False),
        "policy": False if args.no_policy else args.policy or _as_bool(_cfg(cfg, defaults, "policy"), False),
        "stream": not args.no_stream and _as_bool(_cfg(cfg, defaults, "stream"), True),
    }

    request_id = args.request_id or _cfg(cfg, defaults, "request_id")
    if args.auto_request_id and not request_id:
        request_id = uuid.uuid4().hex + uuid.uuid4().hex[:8]

    optional = {
        "area": args.area or _cfg(cfg, defaults, "area"),
        "requestId": request_id,
        "sessionId": args.session_id or _cfg(cfg, defaults, "session_id"),
        "szUserId": args.sz_user_id or _pick(
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
        for key in ("requestId", "sessionId", "safeType", "knowledgeScope", "created", "area"):
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


def _format_units(value: Any) -> str:
    if isinstance(value, list):
        return "、".join(str(item) for item in value if item)
    if value:
        return str(value)
    return ""


def _shorten(text: str, limit: int = 220) -> str:
    compact = " ".join(str(text).split())
    if len(compact) <= limit:
        return compact
    return compact[:limit].rstrip() + "..."


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def _extract_citation_ids(text: str) -> Iterable[int]:
    seen = set()
    for match in re.finditer(r"\[\^?(\d+)\^?\]", text):
        value = int(match.group(1))
        if value not in seen:
            seen.add(value)
            yield value


def _format_answer_content(text: str) -> str:
    cleaned = _strip_html(text)
    return re.sub(r"\[\^?\d+\^?\]", "", cleaned)


def _build_source_index(items: Iterable[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    index: Dict[int, Dict[str, Any]] = {}
    for item in items:
        content = item.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict) or "id" not in block:
                continue
            try:
                cid = int(block["id"])
            except (TypeError, ValueError):
                continue
            index[cid] = {
                "title": item.get("title", "无标题"),
                "writtenText": item.get("writtenText") or item.get("documentNo") or "",
                "unit": _format_units(item.get("unit")),
                "createDate": item.get("createDate", ""),
                "createDateReliability": item.get("createDateReliability", ""),
                "sourceUrl": item.get("sourceUrl", ""),
                "text": block.get("text", ""),
            }
    return index


def _print_material_source(index: int, source: Dict[str, Any]) -> None:
    title = source.get("title") or "无标题"
    print(f"{index}. 《{title}》")
    print(f"   - 发文字号：{source.get('writtenText') or '接口未返回'}")
    print(f"   - 发布单位：{source.get('unit') or '接口未返回'}")
    print(f"   - 发布日期：{source.get('createDate') or '接口未返回'}")
    print(f"   - 发布日期可信度：{source.get('createDateReliability') or '接口未返回'}")
    if source.get("sourceUrl"):
        print(f"   - 链接：{source['sourceUrl']}")
    else:
        print("   - 链接：接口未返回源链接")
    if source.get("text"):
        related = _shorten(_strip_html(source["text"]))
    else:
        related = "接口未返回"
    print(f"   - 相关内容：{related}")
    print()


def _iter_material_sources(items: Iterable[Dict[str, Any]]) -> Iterable[Dict[str, Any]]:
    for item in items:
        content = item.get("content", [])
        text = ""
        if isinstance(content, list) and content:
            first = content[0]
            if isinstance(first, dict):
                text = first.get("text", "")
        yield {
            "title": item.get("title", "无标题"),
            "writtenText": item.get("writtenText") or item.get("documentNo") or "",
            "unit": _format_units(item.get("unit")),
            "createDate": item.get("createDate", ""),
            "createDateReliability": item.get("createDateReliability", ""),
            "sourceUrl": item.get("sourceUrl", ""),
            "text": text,
        }


def _print_cited_sources(content: str, items: Iterable[Dict[str, Any]]) -> None:
    material_items = list(items)
    cited_ids = list(_extract_citation_ids(content))
    if not cited_ids:
        if material_items:
            print("\n参考依据")
            print("说明：正文未返回可对应的引用角标，以下列出接口返回的前 5 条参考材料。")
            for index, source in enumerate(_iter_material_sources(material_items), 1):
                if index > 5:
                    break
                _print_material_source(index, source)
        return

    source_index = _build_source_index(material_items)
    if not source_index:
        print("\n参考依据：本次回答包含引用信息，但接口未返回可展示的参考材料。")
        return

    print("\n参考依据")
    shown = 0
    for index, cid in enumerate(cited_ids, 1):
        source = source_index.get(cid)
        if not source:
            print(f"{index}. 接口未返回该条参考依据对应的材料。")
            continue
        shown += 1
        _print_material_source(index, source)
    if shown:
        print("\n说明：这里只列出本次回复实际使用的参考依据。")


def _print_recommendation_items(items: Iterable[Dict[str, Any]]) -> None:
    rows = list(items)
    if not rows:
        return
    print(f"\n--- 办理事项（{len(rows)} 项）---")
    for i, item in enumerate(rows, 1):
        print(f"[{i}] {item.get('title', '无标题')}")
        if item.get("unit"):
            print(f"    实施单位：{item['unit']}")
        if item.get("itemCategory"):
            print(f"    服务对象：{item['itemCategory']}")
        urls = item.get("onlineProcessUrls")
        if isinstance(urls, list) and urls:
            for url in urls:
                print(f"    网上办理：{url}")
        elif item.get("sourceUrl"):
            print(f"    详情：{item['sourceUrl']}")
        else:
            print("    办理链接：接口未返回")


def _print_policy_files(items: Iterable[Dict[str, Any]]) -> None:
    rows = list(items)
    if not rows:
        return
    print(f"\n--- 政策文件（{len(rows)} 篇）---")
    for i, item in enumerate(rows, 1):
        print(f"[{i}] {item.get('title', '无标题')}")
        document_no = item.get("writtenText") or item.get("documentNo")
        if document_no:
            print(f"    文号：{document_no}")
        if item.get("sourceUrl"):
            print(f"    来源：{item['sourceUrl']}")
        if item.get("createDate"):
            print(f"    发布日期：{item['createDate']}")
        if item.get("createDateReliability"):
            print(f"    发布日期可信度：{item['createDateReliability']}")


def _print_summary(result: Dict[str, Any], show_reasoning: bool) -> None:
    print("=== 深知政务智查 ===")

    safe_labels = {
        "Safe": "安全",
        "Unsafe": "不安全",
        "ConditionallySafe": "有条件安全",
        "Focus": "重点关注",
    }
    scope_labels = {
        "Norms": "规范性知识",
        "Mix": "混合知识",
        "ChitChat": "闲聊",
        "Other": "其他",
    }

    if result.get("safeType"):
        value = result["safeType"]
        print(f"安全状态：{safe_labels.get(value, value)}")
    if result.get("knowledgeScope"):
        value = result["knowledgeScope"]
        print(f"知识范围：{scope_labels.get(value, value)}")
    if result.get("area"):
        print(f"地域：{result['area']}")

    resp = result.get("resp", {})
    if isinstance(resp, dict):
        if resp.get("waitText"):
            print(f"\n等待提示：{resp['waitText']}")
        if resp.get("areaTip"):
            print(f"地域提示：{resp['areaTip']}")

        content = resp.get("content")
        if content:
            print(f"\n回复内容：\n{_format_answer_content(content)}")

        reasoning = resp.get("reasoning_content")
        if show_reasoning and reasoning:
            print(f"\n模型思考过程：\n{reasoning}")
    elif resp:
        print(f"\n回复内容：\n{resp}")

    cited_content = content if isinstance(resp, dict) and isinstance(content, str) else ""
    _print_cited_sources(cited_content, result.get("referenceMaterials", []))
    _print_recommendation_items(result.get("recommendationItems", []))
    _print_policy_files(result.get("policyFiles", []))


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
    parser = argparse.ArgumentParser(description="深知政务智查 credibleChat 调用脚本")
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
    parser.add_argument("--no-stream", action="store_true", help="关闭流式")
    parser.add_argument("--show-payload", action="store_true", help="打印请求参数")
    parser.add_argument("--dry-run", action="store_true", help="只打印请求参数，不发起请求")
    parser.add_argument("--raw", action="store_true", help="打印原始响应")
    parser.add_argument("--json-only", action="store_true", help="仅输出聚合后的 JSON")
    parser.add_argument("--show-reasoning", action="store_true", help="摘要中显示 deepModel 思考过程")
    parser.add_argument("--timeout", type=int, default=90, help="请求超时秒数")
    args = parser.parse_args()

    cfg = _read_config(Path(args.config))
    endpoint = _pick(args.endpoint, os.environ.get("DKNOWC_GOV_ZHICHA_ENDPOINT"), _cfg(cfg, "api", "endpoint"))
    api_key = _pick(args.api_key, os.environ.get("DKNOWC_GOV_ZHICHA_API_KEY"), _cfg(cfg, "api", "api_key"))

    payload = _build_payload(args, cfg)
    if args.show_payload:
        safe_payload = dict(payload)
        print("=== 请求参数 ===")
        print(json.dumps(safe_payload, ensure_ascii=False, indent=2))
        print()
    if args.dry_run:
        return

    if not endpoint:
        print("错误：缺少 endpoint，请在 config.ini 的 [api] 中配置。", file=sys.stderr)
        sys.exit(2)
    if not api_key:
        print(
            "错误：缺少 api_key。ClawHub 版请先运行 scripts/register.mjs，"
            "用手机号和验证码注册可信统一接口账号并自动写入 config.ini；"
            "或使用 --api-key 临时传入。",
            file=sys.stderr,
        )
        sys.exit(2)

    text = _post(endpoint, api_key, payload, args.timeout)
    _print_result(text, args.raw, args.json_only, args.show_reasoning)


if __name__ == "__main__":
    main()
