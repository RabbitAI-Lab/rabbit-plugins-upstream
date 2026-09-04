#!/usr/bin/env python3
"""Small adapter for the existing public paper-check web APIs.

This is deliberately a thin client: it only selects a configured user-site
lane, follows the same presign/upload/order calls as the web UI, and returns
browser handoff URLs.  It does not add a backend, MCP server, login flow or
payment automation.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import mimetypes
import os
import secrets
import sys
import time
import urllib.parse
import urllib.error
import urllib.request
import uuid
from email.utils import formatdate
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / "config.json"
LANES = ("character-count", "vip", "wanfang", "cnki", "aigc", "reduction", "report-verify", "guidance")
FILE_LANES = {"character-count", "vip", "wanfang", "cnki", "aigc", "reduction"}
VERIFY_BRANDS = ("vip", "wanfang", "cnki")
UPLOAD_KEYS = {"uploadurl", "uploadobjectkey", "objectkey", "accesskeyid", "accesskeysecret", "securitytoken", "token", "timespan", "authorization", "headers", "uploadheaders", "endpoint", "bucketname", "region"}


class ClientError(RuntimeError):
    pass


def load_config() -> tuple[dict[str, Any], str, dict[str, Any]]:
    try:
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ClientError(f"无法读取 Skill 配置: {exc}") from exc
    environment = os.environ.get("PAPER_CHECK_ENV", config.get("default_environment", "cqccjy"))
    if environment not in config.get("environments", []):
        raise ClientError(f"不支持的部署环境: {environment}")
    domain_file = ROOT / "domains" / f"{environment}.json"
    try:
        domain = json.loads(domain_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ClientError(f"无法读取 {environment} 域名配置: {exc}") from exc
    if domain.get("environment") != environment:
        raise ClientError("域名配置与运行环境不匹配")
    return config, environment, domain


def lane_route(domain: dict[str, Any], lane: str) -> dict[str, Any]:
    if lane not in LANES:
        raise ClientError(f"不支持的产品类型: {lane}")
    route = (domain.get("lanes") or {}).get(lane)
    if not isinstance(route, dict) or not isinstance(route.get("site"), str):
        raise ClientError(f"当前环境没有配置 {lane}")
    if not route["site"].startswith("https://"):
        raise ClientError(f"{lane} 只允许 HTTPS 用户端")
    route = dict(route)
    route["owner_user_id"] = domain.get("owner_user_id")
    return route


def verification_route(route: dict[str, Any], brand: str | None) -> dict[str, Any]:
    """Keep the CQCCJY funnel as the browser handoff, with an optional fallback map."""
    if brand is None:
        return route
    pages = route.get("pages") or {}
    entry = pages.get("entry")
    if not isinstance(entry, str) or not entry.startswith("https://"):
        raise ClientError("当前环境没有配置统一报告验真入口")
    url = pages.get(brand)
    if not isinstance(url, str) or not url.startswith("https://"):
        raise ClientError(f"当前环境没有配置 {brand} 报告验真入口")
    selected = dict(route)
    selected["pages"] = {"entry": entry, brand: url}
    return selected


def api_url(route: dict[str, Any], name: str, **values: Any) -> str:
    path = (route.get("api") or {}).get(name)
    if not isinstance(path, str) or not path.startswith("/"):
        raise ClientError(f"{name} 接口未配置")
    try:
        path = path.format(**values)
    except KeyError as exc:
        raise ClientError(f"接口路径缺少参数: {exc.args[0]}") from exc
    return route["site"].rstrip("/") + path


def unwrap(payload: Any) -> Any:
    if not isinstance(payload, dict):
        return payload
    code = payload.get("code")
    if code not in (None, 0, "0", 200, "200"):
        raise ClientError(f"服务端错误（{code}）: {payload.get('msg') or payload.get('message') or '请求失败'}")
    return payload.get("data", payload)


class Rest:
    def __init__(self, dry_run: bool, timeout: int):
        self.dry_run = dry_run
        self.timeout = timeout

    def request(self, method: str, url: str, *, payload: Any = None, query: dict[str, Any] | None = None,
                headers: dict[str, str] | None = None, raw: bool = False) -> Any:
        if not url.startswith("https://"):
            raise ClientError("只允许 HTTPS 请求")
        if query:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode({k: v for k, v in query.items() if v is not None})
        body = None
        request_headers = {"Accept": "application/json", "User-Agent": "paper-check-skill/3.0"}
        if headers:
            request_headers.update(headers)
        if payload is not None:
            body = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode("utf-8")
            request_headers.setdefault("Content-Type", "application/json")
        if self.dry_run:
            return {"dry_run": True, "method": method, "url": url, "body_bytes": len(body or b"")}
        request = urllib.request.Request(url, data=body, headers=request_headers, method=method.upper())
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = response.read(3 * 1024 * 1024 + 1)
                if len(data) > 3 * 1024 * 1024:
                    raise ClientError("服务端响应超过 3MB")
                if raw:
                    return data
                if not data:
                    return None
                try:
                    return unwrap(json.loads(data.decode("utf-8")))
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    raise ClientError("服务端返回的不是 UTF-8 JSON") from exc
        except urllib.error.HTTPError as exc:
            detail = exc.read(1000).decode("utf-8", errors="replace")
            raise ClientError(f"HTTP {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ClientError(f"网络请求失败: {exc}") from exc


def ensure_file(path_value: str, config: dict[str, Any]) -> tuple[Path, bytes, str]:
    path = Path(path_value).expanduser()
    if not path.is_file():
        raise ClientError(f"文件不存在: {path}")
    limit = int(config.get("limits", {}).get("max_file_bytes", 50 * 1024 * 1024))
    if path.stat().st_size > limit:
        raise ClientError(f"文件超过 {limit} 字节限制")
    suffix = path.suffix.lower()
    allowed = {str(item).lower() for item in config.get("limits", {}).get("supported_extensions", [])}
    if allowed and suffix not in allowed:
        raise ClientError(f"不支持的文件格式 {suffix}；支持 {', '.join(sorted(allowed))}")
    try:
        content = path.read_bytes()
    except OSError as exc:
        raise ClientError(f"无法读取文件: {exc}") from exc
    return path, content, mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def multipart(fields: dict[str, Any], file_field: str, filename: str, content_type: str, content: bytes) -> tuple[bytes, str]:
    boundary = "----paper-check-" + secrets.token_hex(12)
    chunks: list[bytes] = []
    for key, value in fields.items():
        if value is None:
            continue
        chunks += [f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\n".encode(), str(value).encode("utf-8"), b"\r\n"]
    safe_name = filename.replace("\r", "").replace("\n", "").replace('"', "'")
    chunks += [f"--{boundary}\r\nContent-Disposition: form-data; name=\"{file_field}\"; filename=\"{safe_name}\"\r\nContent-Type: {content_type}\r\n\r\n".encode(), content, b"\r\n", f"--{boundary}--\r\n".encode()]
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def put_upload(rest: Rest, presign: dict[str, Any], content: bytes, content_type: str) -> str:
    """Use the exact upload ticket returned by the public UI API."""
    upload_url = presign.get("uploadUrl") or presign.get("upload_url")
    headers = {str(k): str(v) for k, v in (presign.get("headers") or {}).items()}
    headers.setdefault("Content-Type", content_type)
    if upload_url:
        rest.request("PUT", upload_url, payload=content, headers=headers, raw=True)
        return str(presign.get("objectKey") or presign.get("object_key") or "")
    # VIP uses temporary Aliyun OSS STS fields instead of a signed URL.
    endpoint = str(presign.get("endpoint") or "")
    bucket = str(presign.get("bucketName") or "")
    object_key = str(presign.get("uploadObjectKey") or "")
    access_id = str(presign.get("accessKeyId") or "")
    access_secret = str(presign.get("accessKeySecret") or "")
    security_token = str(presign.get("securityToken") or "")
    if not all((endpoint, bucket, object_key, access_id, access_secret)):
        raise ClientError("上传票据缺少 uploadUrl 或 OSS 临时字段")
    endpoint = endpoint if endpoint.startswith("https://") else "https://" + endpoint
    parsed = urllib.parse.urlsplit(endpoint)
    path = "/" + urllib.parse.quote(object_key.lstrip("/"), safe="/%:@")
    # ali-oss uses virtual-host addressing by default: bucket.endpoint/object.
    # Sending the same STS signature to endpoint/object omits the bucket routing
    # information and OSS rejects the otherwise valid request with HTTP 403.
    upload_url = urllib.parse.urlunsplit((
        parsed.scheme,
        f"{bucket}.{parsed.netloc}",
        parsed.path.rstrip("/") + path,
        "",
        "",
    ))
    date = formatdate(usegmt=True)
    headers.setdefault("Content-Type", content_type)
    headers["Date"] = date
    if security_token:
        headers["x-oss-security-token"] = security_token
    canonical = {k.lower(): " ".join(str(v).strip().split()) for k, v in headers.items() if k.lower().startswith("x-oss-")}
    canonical_headers = "".join(f"{k}:{canonical[k]}\n" for k in sorted(canonical))
    string_to_sign = "PUT\n\n" + headers["Content-Type"] + "\n" + date + "\n" + canonical_headers + f"/{bucket}{path}"
    signature = base64.b64encode(hmac.new(access_secret.encode(), string_to_sign.encode(), hashlib.sha1).digest()).decode()
    headers["Authorization"] = f"OSS {access_id}:{signature}"
    upload_request = urllib.request.Request(upload_url, data=content, headers=headers, method="PUT")
    if rest.dry_run:
        return str(presign.get("objectKey") or presign.get("object_key") or "")
    try:
        with urllib.request.urlopen(upload_request, timeout=rest.timeout) as response:
            if response.status not in (200, 201):
                raise ClientError(f"OSS 上传失败: HTTP {response.status}")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        raise ClientError(f"OSS 上传失败: {exc}") from exc
    return str(presign.get("objectKey") or presign.get("object_key") or "")


def get_value(data: Any, *keys: str) -> Any:
    if isinstance(data, dict):
        for key in keys:
            if key in data and data[key] not in (None, ""):
                return data[key]
        for item in data.values():
            found = get_value(item, *keys)
            if found not in (None, ""):
                return found
    if isinstance(data, list):
        for item in data:
            found = get_value(item, *keys)
            if found not in (None, ""):
                return found
    return None


def redact(data: Any) -> Any:
    if isinstance(data, dict):
        out = {}
        for key, value in data.items():
            normalized = "".join(ch.lower() for ch in str(key) if ch.isalnum())
            out[key] = "[execution-only]" if normalized in UPLOAD_KEYS else redact(value)
        return out
    if isinstance(data, list):
        return [redact(item) for item in data]
    return data


def envelope(lane: str, environment: str, route: dict[str, Any], action: str, data: Any, *, order_no: Any = None) -> dict[str, Any]:
    order_no = str(order_no or get_value(data, "orderNo", "order_no", "bizNo") or "") or None
    pages = {}
    for name, template in (route.get("pages") or {}).items():
        if isinstance(template, str) and order_no:
            pages[name] = template.replace("{order_no}", urllib.parse.quote(order_no, safe=""))
        elif isinstance(template, str) and (name == "entry" or action == "verify"):
            pages[name] = template
    status = get_value(data, "status", "payStatus")
    report_url = data if isinstance(data, str) and data.startswith("https://") else get_value(data, "reportUrl", "report_url", "resultDownloadUrl", "downloadUrl")
    if isinstance(report_url, str) and report_url.startswith("https://"):
        pages.setdefault("report_download", report_url)
    terminal = str(status or "").upper() in {"SUCCEEDED", "SUCCESS", "COMPLETED", "COMPLETE", "DONE"}
    selected = (pages.get("report") if action == "report" or terminal else None) or pages.get("payment") or pages.get("progress") or pages.get("entry")
    next_action = "打开页面查看当前订单；未支付时由用户在页面完成支付" if order_no else "打开用户端页面查看产品和提交入口"
    if action == "report":
        next_action = "打开报告下载地址；若接口尚未返回地址，请等待订单完成后再次查询"
    if action == "verify":
        next_action = "打开官方验真入口，按页面要求提交报告和验证码；Skill 不绕过验证码、不替你判假"
    return {"lane": lane, "environment": environment, "owner_user_id": route.get("owner_user_id"), "action": action, "status": status, "order_no": order_no, "word_count": get_value(data, "wordCount", "word_count", "actualWordCount"), "report_download_url": pages.get("report_download"), "browser_url": selected, "browser_urls": pages, "browser_action": "OPEN_BROWSER", "next_action": next_action, "data": redact(data)}


def request_id() -> str:
    return "pc-" + uuid.uuid4().hex


def dry_flow(lane: str, env: str, route: dict[str, Any], action: str, steps: list[str], file_name: str | None = None) -> dict[str, Any]:
    data: dict[str, Any] = {"dry_run": True, "steps": steps}
    if file_name:
        data["file_name"] = file_name
    return envelope(lane, env, route, action, data)


def metadata(args: argparse.Namespace, path: Path, *, default_product: str | None = None) -> dict[str, Any]:
    product = args.product_type or args.product_code or default_product
    return {"productType": product, "productCode": product, "title": args.title or path.stem, "author": args.author or "用户", "visitorKey": os.environ.get("PAPER_CHECK_VISITOR_KEY", "pc-" + secrets.token_hex(16)), "clientRequestId": args.client_request_id or request_id(), "acceptTime": args.accept_time, "checkDbs": args.check_dbs}


def vip_submit(rest: Rest, config: dict[str, Any], env: str, route: dict[str, Any], args: argparse.Namespace, *, count_only: bool) -> dict[str, Any]:
    path, content, content_type = ensure_file(args.file, config)
    if not count_only and (not args.title or not args.author):
        raise ClientError("维普查重提交需要 --title 和 --author；只算字符数可使用 character-count")
    meta = metadata(args, path, default_product="dxs" if count_only else None)
    if not meta["productType"] or not meta["title"] or not meta["author"]:
        raise ClientError("维普提交需要 product-type、title、author")
    if rest.dry_run:
        return dry_flow("character-count" if count_only else "vip", env, route, "count" if count_only else "submit", ["POST draft", "POST presign", "PUT OSS ticket", "POST complete", "GET order"], path.name)
    draft = rest.request("POST", api_url(route, "draft"), payload={"productType": meta["productType"], "detectMode": "AUTO", "title": meta["title"], "author": meta["author"], "publishDate": meta.get("acceptTime"), "visitorKey": meta["visitorKey"]})
    order_no = get_value(draft, "orderNo", "order_no")
    if not order_no:
        raise ClientError("维普草稿接口没有返回订单号")
    presign = rest.request("POST", api_url(route, "presign"), payload={"orderNo": order_no, "fileName": path.name})
    object_key = put_upload(rest, presign if isinstance(presign, dict) else {}, content, content_type)
    completed = rest.request("POST", api_url(route, "complete"), payload={"orderNo": order_no, "productType": meta["productType"], "title": meta["title"], "author": meta["author"], "objectKey": object_key, "fileName": path.name, "contentType": content_type, "fileSize": len(content)})
    order = rest.request("GET", api_url(route, "order", order_no=order_no))
    return envelope("character-count" if count_only else "vip", env, route, "count" if count_only else "submit", order or completed, order_no=order_no)


def wanfang_or_cnki(rest: Rest, config: dict[str, Any], env: str, lane: str, route: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    path, content, content_type = ensure_file(args.file, config)
    product = args.product_code
    if not product:
        raise ClientError(f"{lane} 提交需要 --product-code；先执行 products 获取实时代码")
    if not args.title or not args.author:
        raise ClientError(f"{lane} 提交需要 --title 和 --author")
    if rest.dry_run:
        return dry_flow(lane, env, route, "submit", ["POST presign", "PUT signed OSS ticket", "POST order/create", "GET order"], path.name)
    presign = rest.request("POST", api_url(route, "presign"), payload={"fileName": path.name, "productCode": product})
    object_key = put_upload(rest, presign if isinstance(presign, dict) else {}, content, content_type)
    order = rest.request("POST", api_url(route, "create"), payload={"title": args.title, "author": args.author, "productCode": product, "fileName": path.name, "objectKey": object_key, "contentType": content_type, "fileSize": len(content), "acceptTime": args.accept_time, "checkDbs": args.check_dbs})
    return envelope(lane, env, route, "submit", order)


def reduction_submit(rest: Rest, config: dict[str, Any], env: str, route: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    path, content, content_type = ensure_file(args.file, config)
    product = args.product_type or "smart_reduction"
    title = args.title or path.stem
    if rest.dry_run:
        steps = ["POST order/create-draft", "POST source/presign", "PUT source OSS ticket"]
        if args.report_file:
            steps += ["POST report/presign", "PUT report OSS ticket"]
        steps += ["POST order/{orderNo}/count/file", "GET order"]
        return dry_flow("reduction", env, route, "submit", steps, path.name)
    draft = rest.request("POST", api_url(route, "draft"), payload={"productType": product, "title": title, "author": args.author, "visitorKey": os.environ.get("PAPER_CHECK_VISITOR_KEY", "pc-" + secrets.token_hex(16))})
    order_no = get_value(draft, "orderNo", "order_no")
    if not order_no:
        raise ClientError("降重草稿接口没有返回订单号")
    source_ticket = rest.request("POST", api_url(route, "presign_source"), payload={"orderNo": order_no, "fileName": path.name})
    source_key = put_upload(rest, source_ticket if isinstance(source_ticket, dict) else {}, content, content_type)
    report_key = None
    report_meta: dict[str, Any] = {}
    if args.report_file:
        report_path, report_content, report_type = ensure_file(args.report_file, config)
        report_ticket = rest.request("POST", api_url(route, "presign_report"), payload={"orderNo": order_no, "fileName": report_path.name})
        report_key = put_upload(rest, report_ticket if isinstance(report_ticket, dict) else {}, report_content, report_type)
        report_meta = {"reportObjectKey": report_key, "reportFileName": report_path.name, "reportContentType": report_type, "reportFileSize": len(report_content)}
    count = rest.request("POST", api_url(route, "count_file", order_no=order_no), payload={"title": title, "author": args.author, "sourceObjectKey": source_key, "sourceFileName": path.name, "sourceContentType": content_type, "sourceFileSize": len(content), **report_meta, "reportType": args.report_type})
    return envelope("reduction", env, route, "submit", count, order_no=order_no)


def aigc_draft(rest: Rest, env: str, route: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    if rest.dry_run:
        return dry_flow("aigc", env, route, "draft", ["POST order/pay/draft"])
    draft = rest.request("POST", api_url(route, "pay_draft"), payload={"scene": "PAGE", "quantity": 1, "clientBatchId": args.client_request_id or request_id()})
    return envelope("aigc", env, route, "draft", draft)


def aigc_submit(rest: Rest, config: dict[str, Any], env: str, route: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    if not args.order_no:
        raise ClientError("AIGC 提交需要先用 aigc-draft 获取订单号并在页面完成支付，再传 --order-no")
    path, content, content_type = ensure_file(args.file, config)
    if rest.dry_run:
        return dry_flow("aigc", env, route, "submit", ["POST prepare-submit", "PUT source OSS ticket", "POST complete-source-archive", "POST mark-upload-attempted", "POST supplier multipart (if shouldUpload)", "POST complete-direct-submit", "GET order"], path.name)
    fields = {"orderNo": args.order_no, "title": args.title or path.stem, "author": args.author or "用户", "uploadType": 1, "uploadContent": "FILE", "sourceFileName": path.name, "sourceContentType": content_type, "sourceFileSize": len(content)}
    prepared = rest.request("POST", api_url(route, "prepare"), payload=fields)
    source = (prepared or {}).get("sourceUpload") if isinstance(prepared, dict) else None
    if not isinstance(source, dict):
        return envelope("aigc", env, route, "submit", prepared, order_no=args.order_no)
    put_upload(rest, source, content, content_type)
    rest.request("POST", api_url(route, "source_complete"), payload={"orderNo": args.order_no, "supplierUniqueCode": ((prepared.get("uploadTicket") or {}).get("uniqueCode")), "sourceObjectKey": source.get("objectKey")})
    claim = rest.request("POST", api_url(route, "upload_claim"), payload={**fields, "supplierUniqueCode": ((prepared.get("uploadTicket") or {}).get("uniqueCode"))})
    ticket = (prepared.get("uploadTicket") or {}) if isinstance(prepared, dict) else {}
    if isinstance(claim, dict) and claim.get("shouldUpload") and ticket.get("uploadUrl"):
        body, content_header = multipart({"title": fields["title"], "author": fields["author"], "uniqueCode": ticket.get("uniqueCode")}, "file", path.name, content_type, content)
        rest.request("POST", str(ticket["uploadUrl"]), payload=body, headers={"Content-Type": content_header, "token": str(ticket.get("token", "")), "timespan": str(ticket.get("timespan", ""))})
    order = rest.request("POST", api_url(route, "submit_complete"), payload={**fields, "supplierUniqueCode": ticket.get("uniqueCode")})
    return envelope("aigc", env, route, "submit", order, order_no=args.order_no)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="论文检测用户端的轻量 REST 适配层")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=30)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("products", help="读取实时产品/配置"); p.add_argument("--lane", required=True, choices=LANES)
    s = sub.add_parser("submit", help="按用户端流程创建订单、上传文件并返回页面地址"); s.add_argument("--lane", required=True, choices=sorted(FILE_LANES)); s.add_argument("--file", required=True); s.add_argument("--product-type"); s.add_argument("--product-code"); s.add_argument("--title"); s.add_argument("--author"); s.add_argument("--accept-time"); s.add_argument("--check-dbs"); s.add_argument("--report-file"); s.add_argument("--report-type"); s.add_argument("--order-no"); s.add_argument("--client-request-id")
    a = sub.add_parser("aigc-draft", help="创建 AIGC 页面支付草稿，不自动支付"); a.add_argument("--client-request-id")
    for name in ("status", "report"):
        q = sub.add_parser(name); q.add_argument("--lane", required=True, choices=LANES); q.add_argument("--order-no", required=True)
    v = sub.add_parser("verify", help="打开固定的报告验真入口"); v.add_argument("--lane", default="report-verify", choices=["report-verify"]); v.add_argument("--brand", choices=VERIFY_BRANDS)
    ans = sub.add_parser("answer", help="输出稳定的答疑口径并读取实时配置"); ans.add_argument("--question", required=True)
    args = parser.parse_args(argv)
    try:
        config, env, domain = load_config()
        rest = Rest(args.dry_run, max(1, args.timeout))
        if args.command == "products":
            route = lane_route(domain, args.lane); data = rest.request("GET", api_url(route, "config")); print(json.dumps(envelope(args.lane, env, route, "products", data), ensure_ascii=False, indent=2)); return 0
        if args.command == "verify":
            route = verification_route(lane_route(domain, "report-verify"), args.brand)
            result = envelope("report-verify", env, route, "verify", None)
            result["verification_brand"] = args.brand
            print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
        if args.command == "answer":
            route = lane_route(domain, "guidance"); data = rest.request("GET", api_url(route, "config")); result = envelope("guidance", env, route, "answer", data); result["answer"] = "价格、格式和时效以实时产品配置为准；字符数口径为维普解析的字符数（不计空格）；检测提交后订单异步处理，请用订单号查询。"; result["question"] = args.question; print(json.dumps(result, ensure_ascii=False, indent=2)); return 0
        route = lane_route(domain, getattr(args, "lane", "aigc"))
        if args.command == "aigc-draft": result = aigc_draft(rest, env, route, args)
        elif args.command == "submit" and args.lane == "character-count": result = vip_submit(rest, config, env, route, args, count_only=True)
        elif args.command == "submit" and args.lane == "vip": result = vip_submit(rest, config, env, route, args, count_only=False)
        elif args.command == "submit" and args.lane in {"wanfang", "cnki"}: result = wanfang_or_cnki(rest, config, env, args.lane, route, args)
        elif args.command == "submit" and args.lane == "reduction": result = reduction_submit(rest, config, env, route, args)
        elif args.command == "submit" and args.lane == "aigc": result = aigc_submit(rest, config, env, route, args)
        elif args.command in {"status", "report"}:
            key = "order" if args.command == "status" else ("report" if args.lane not in {"reduction", "aigc"} else ("result" if args.lane == "reduction" else None))
            data = rest.request("GET", api_url(route, key, order_no=args.order_no)) if key else None
            result = envelope(args.lane, env, route, args.command, data, order_no=args.order_no)
        else: raise ClientError("未知命令")
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str)); return 0
    except ClientError as exc:
        print(f"ERROR: {exc}", file=sys.stderr); return 2


if __name__ == "__main__":
    raise SystemExit(main())
