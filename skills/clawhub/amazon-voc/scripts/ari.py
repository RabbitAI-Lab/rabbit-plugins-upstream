#!/usr/bin/env python3
"""ARI CLI for the amazon-review-intelligence-extractor Skill.

Uses only Python's standard library. Paid collection and AI analysis commands
require an explicit --confirm flag after a free preview/quote.
"""

import argparse
import getpass
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


PROD_BASE = "https://ari.funewa.com"
TIMEOUT_SEC = 120
SITES = ("amz_us", "amz_uk", "amz_de", "amz_jp", "amz_ca", "amz_fr", "amz_es", "amz_it")
ANALYSIS_TYPES = ("voc", "insight", "trend", "variant", "compare")
_exit_code = 0

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def base_url():
    return (os.environ.get("ARI_BASE_URL") or PROD_BASE).strip().rstrip("/")


def links():
    root = (os.environ.get("ARI_WEB_URL") or PROD_BASE).strip().rstrip("/")
    return {
        "apiKeys": root + "/zh/account?ui=d47626f#api-keys",
        "billing": root + "/zh/billing",
        "products": root + "/zh/products",
        "reports": root + "/zh/reports",
    }


def config_path():
    return os.path.expanduser("~/.ari/config.json")


def resolve_key():
    key = os.environ.get("ARI_API_KEY", "").strip()
    if key:
        return key
    candidates = [
        config_path(),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.json"),
    ]
    for path in candidates:
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                key = (json.load(fh).get("api_key") or "").strip()
            if key:
                return key
        except (OSError, json.JSONDecodeError):
            pass
    return None


def require_key():
    key = resolve_key()
    if key:
        return key
    emit(error_obj(
        "ARI_API_KEY_MISSING", 0,
        "未找到 ARI API Key",
        "运行 python ari.py configure，或设置 ARI_API_KEY；在用户中心申请 Key。",
    ))
    raise SystemExit(2)


def error_obj(code, status, message, hint="", query=None, partial=None):
    out = {
        "success": False,
        "error": {"code": code, "status": status, "message": message, "hint": hint},
        "links": links(),
    }
    if query is not None:
        out["_query"] = query
    if partial:
        out["partial"] = partial
    return out


def emit(obj, compact=False):
    global _exit_code
    if isinstance(obj, dict) and obj.get("success") is False:
        _exit_code = 1
    print(json.dumps(
        obj, ensure_ascii=False,
        separators=((",", ":") if compact else (", ", ": ")),
        indent=(None if compact else 2),
    ))


def parse_http_error(exc, query):
    try:
        detail = json.loads(exc.read().decode("utf-8", errors="replace"))
    except Exception:
        detail = {}
    if isinstance(detail, dict) and detail:
        detail["_httpStatus"] = exc.code
        detail["_query"] = query
        detail["links"] = links()
        return detail
    return error_obj("HTTP_ERROR", exc.code, "HTTP %d" % exc.code, query=query)


def request_json(method, path, payload=None, params=None):
    query = {
        "method": method,
        "path": path,
        "params": {k: v for k, v in (params or {}).items() if v not in (None, "")},
        "payload": payload,
    }
    url = base_url() + path
    if query["params"]:
        url += "?" + urllib.parse.urlencode(query["params"], doseq=True)
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": "Bearer " + require_key(),
        "Accept": "application/json",
        "User-Agent": "ARI-Review-Skill/1.0",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    try:
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            raw = resp.read().decode("utf-8")
            out = json.loads(raw) if raw else {"success": True, "data": None}
            if isinstance(out, dict):
                out["_query"] = query
            return out
    except urllib.error.HTTPError as exc:
        return parse_http_error(exc, query)
    except Exception as exc:
        return error_obj("NETWORK_ERROR", 0, str(exc), "检查网络或 ARI_BASE_URL", query)


def request_sse(path, payload):
    query = {"method": "POST", "path": path, "params": {}, "payload": payload}
    url = base_url() + path
    headers = {
        "Authorization": "Bearer " + require_key(),
        "Accept": "text/event-stream",
        "Content-Type": "application/json",
        "User-Agent": "ARI-Review-Skill/1.0",
    }
    try:
        req = urllib.request.Request(
            url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "text/event-stream" not in content_type:
                raw = resp.read().decode("utf-8")
                out = json.loads(raw) if raw else {"success": True, "data": None}
                out["_query"] = query
                return out

            result = {"meta": None, "content": "", "result": None,
                      "reportId": 0, "creditsUsed": 0}
            for raw_line in resp:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line.startswith("data: "):
                    continue
                raw = line[6:].strip()
                if not raw or raw == "[DONE]":
                    continue
                try:
                    event = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                kind = event.get("type")
                if kind == "meta":
                    result["meta"] = {k: v for k, v in event.items() if k != "type"}
                elif kind == "content":
                    result["content"] += event.get("content") or ""
                elif kind == "result":
                    result["result"] = event.get("data")
                    result["reportId"] = event.get("reportId") or 0
                elif kind == "done":
                    result["creditsUsed"] = event.get("creditsUsed") or 0
                elif kind == "error":
                    return error_obj(
                        event.get("code") or "ARI_ANALYSIS_ERROR", 200,
                        event.get("message") or "analysis failed",
                        "已生成的部分内容保留在 partial 中", query, result)
            return {"success": True, "data": result, "_query": query, "links": links()}
    except urllib.error.HTTPError as exc:
        return parse_http_error(exc, query)
    except Exception as exc:
        return error_obj("NETWORK_ERROR", 0, str(exc), "检查网络后重试", query)


def data_of(out):
    return out.get("data") if isinstance(out, dict) else None


def ok(out):
    return isinstance(out, dict) and out.get("success") is True


def cmd_configure(args):
    key = getpass.getpass("ARI API Key (ari_live_*): ").strip()
    if not key.startswith("ari_live_"):
        emit(error_obj("ARI_API_KEY_INVALID_FORMAT", 0, "Key 必须以 ari_live_ 开头"), args.compact)
        raise SystemExit(2)
    path = config_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"api_key": key}, fh)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    emit({"success": True, "data": {"configured": True, "path": path}}, args.compact)


def cmd_check(args):
    me = request_json("GET", "/api/v1/user/me")
    if not ok(me):
        emit(me, args.compact)
        return
    balance = request_json("GET", "/api/v1/credits/balance")
    if not ok(balance):
        emit(balance, args.compact)
        return
    emit({"success": True, "data": {"user": data_of(me), "balance": data_of(balance)},
          "links": links()}, args.compact)


def cmd_products(args):
    emit(request_json("GET", "/api/v1/asins"), args.compact)


def wait_task(task_id, interval, timeout):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        last = request_json("GET", "/api/v1/collection/status/" + urllib.parse.quote(task_id))
        if not ok(last):
            return last
        status = str((data_of(last) or {}).get("status") or "").lower()
        if status in ("done", "completed", "succeeded", "failed", "cancelled"):
            return last
        time.sleep(interval)
    return error_obj("WAIT_TIMEOUT", 0, "等待采集超时，任务仍可能在后台运行",
                     "稍后使用 status --task %s 查询" % task_id,
                     partial=data_of(last) if last else None)


def cmd_collect(args):
    pricing = request_json("GET", "/api/v1/billing/pricing")
    if not ok(pricing):
        emit(pricing, args.compact)
        return
    price = int((data_of(pricing) or {}).get("collectPerPage") or 5)
    estimate = args.pages * price
    payload = {
        "asin": args.asin.upper(), "site": args.site, "pageCount": args.pages,
        "filterByStar": args.star, "sortBy": args.sort, "alias": args.alias,
    }
    if not args.confirm:
        emit({
            "success": True,
            "data": {
                "confirmationRequired": True,
                "estimatedCredits": estimate,
                "estimatedReviews": args.pages * int((data_of(pricing) or {}).get("reviewsPerPage") or 10),
                "message": "确认后用同一命令追加 --confirm；需要等待完成再追加 --wait。",
                "request": payload,
            },
            "links": links(),
        }, args.compact)
        return
    out = request_json("POST", "/api/v1/collection/submit", payload)
    if args.wait and ok(out):
        task_id = (data_of(out) or {}).get("taskId")
        if task_id:
            submitted = data_of(out)
            final = wait_task(task_id, args.interval, args.timeout)
            if ok(final):
                out = {"success": True, "data": {"submitted": submitted,
                                                   "final": data_of(final)},
                       "links": links()}
            else:
                final["submitted"] = submitted
                out = final
    emit(out, args.compact)


def cmd_status(args):
    emit(request_json("GET", "/api/v1/collection/status/" + urllib.parse.quote(args.task)), args.compact)


def cmd_reviews(args):
    params = {"asin": args.asin.upper(), "site": args.site, "star": args.star,
              "q": args.query, "page": args.page}
    emit(request_json("GET", "/api/v1/reviews", params=params), args.compact)


def chart_bundle(asin, site, days):
    params = {"asin": asin.upper(), "site": site, "days": days}
    return {
        name: request_json("GET", "/api/v1/charts/" + name, params=params)
        for name in ("stars", "trend", "keywords", "flow")
    }


def cmd_charts(args):
    emit({"success": True, "data": chart_bundle(args.asin, args.site, args.days),
          "links": links()}, args.compact)


def quote_payload(kind, asin, site, competitor, competitor_site):
    return {
        "type": kind, "asin": (asin or "").upper(), "site": site,
        "competitorAsin": (competitor or "").upper(),
        "competitorSite": competitor_site or site,
    }


def run_analysis(kind, asin, site, competitor, competitor_site, language, confirm):
    q_payload = quote_payload(kind, asin, site, competitor, competitor_site)
    quote = request_json("POST", "/api/v1/analysis/quote", q_payload)
    if not ok(quote):
        return quote
    q_data = data_of(quote) or {}
    if not confirm:
        return {"success": True, "data": {"confirmationRequired": True, "quote": q_data,
                                             "message": "用户确认后追加 --confirm 才会生成并扣点。"},
                "links": links()}
    if not q_data.get("sufficient", False):
        return error_obj("ARI_INSUFFICIENT_CREDITS", 402, "积点不足",
                         "需要 %s 点，当前余额 %s；请充值后重试。" %
                         (q_data.get("price"), q_data.get("balance")))

    payload = {"asin": (asin or "").upper(), "site": site, "outputLanguage": language}
    if kind == "compare":
        payload.update({"competitorAsin": (competitor or "").upper(),
                        "competitorSite": competitor_site or site})
    path = "/api/v1/analysis/" + kind
    if kind in ("voc", "insight", "compare"):
        return request_sse(path, payload)
    return request_json("POST", path, payload)


def cmd_quote(args):
    emit(request_json("POST", "/api/v1/analysis/quote",
                      quote_payload(args.type, args.asin, args.site,
                                    args.competitor, args.competitor_site)), args.compact)


def cmd_analyze(args):
    emit(run_analysis(args.type, args.asin, args.site, args.competitor,
                      args.competitor_site, args.language, args.confirm), args.compact)


def cmd_reports(args):
    params = {"asin": args.asin, "type": args.type, "starred": "1" if args.starred else "",
              "q": args.query, "limit": args.limit}
    emit(request_json("GET", "/api/v1/reports", params=params), args.compact)


def cmd_report(args):
    emit(request_json("GET", "/api/v1/reports/%d" % args.id), args.compact)


def cmd_deepdive(args):
    products = request_json("GET", "/api/v1/asins")
    if not ok(products):
        emit(products, args.compact)
        return
    items = (data_of(products) or {}).get("asins") or []
    target = next((x for x in items if str(x.get("asin", "")).upper() == args.asin.upper()
                   and x.get("site") == args.site), None)
    if not target:
        emit(error_obj(
            "ARI_ASIN_NOT_SUBSCRIBED", 403,
            "%s / %s 尚未订阅" % (args.asin.upper(), args.site),
            "先运行 collect --asin %s --site %s 获取采集报价。" % (args.asin.upper(), args.site),
        ), args.compact)
        return
    bundle = {
        "product": target,
        "charts": chart_bundle(args.asin, args.site, args.days),
        "reviews": request_json("GET", "/api/v1/reviews",
                                params={"asin": args.asin.upper(), "site": args.site, "page": 1}),
        "reports": request_json("GET", "/api/v1/reports",
                                params={"asin": args.asin.upper(), "limit": args.report_limit}),
        "analysis": run_analysis("voc", args.asin, args.site, None, None,
                                 args.language, args.confirm),
    }
    emit({"success": True, "data": bundle, "links": links()}, args.compact)


def add_analysis_args(parser, include_type=True):
    if include_type:
        parser.add_argument("--type", required=True, choices=ANALYSIS_TYPES)
    parser.add_argument("--asin", required=True)
    parser.add_argument("--site", default="amz_us", choices=SITES)
    parser.add_argument("--competitor")
    parser.add_argument("--competitor-site", choices=SITES)
    parser.add_argument("--language", default="zh")


def main():
    ap = argparse.ArgumentParser(prog="ari.py", description="ARI Amazon 评论采集与智能分析 CLI")
    ap.add_argument("--compact", action="store_true", help="输出单行 JSON")
    sub = ap.add_subparsers(dest="command", required=True)

    p = sub.add_parser("configure", help="隐藏输入并保存 ARI API Key")
    p.set_defaults(fn=cmd_configure)

    p = sub.add_parser("check", help="验证 Key、账户和积点余额")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("products", help="列出当前账户订阅的 ASIN")
    p.set_defaults(fn=cmd_products)

    p = sub.add_parser("collect", help="采集报价或提交采集任务")
    p.add_argument("--asin", required=True)
    p.add_argument("--site", default="amz_us", choices=SITES)
    p.add_argument("--pages", type=int, default=3, choices=range(1, 11), metavar="1..10")
    p.add_argument("--star", default="all_stars",
                   choices=("all_stars", "critical", "positive", "one_star", "two_star",
                            "three_star", "four_star", "five_star"))
    p.add_argument("--sort", default="recent", choices=("recent", "helpful"))
    p.add_argument("--alias", default="")
    p.add_argument("--confirm", action="store_true", help="确认扣点并提交")
    p.add_argument("--wait", action="store_true", help="提交后等待任务完成")
    p.add_argument("--interval", type=int, default=3)
    p.add_argument("--timeout", type=int, default=600)
    p.set_defaults(fn=cmd_collect)

    p = sub.add_parser("status", help="查询采集任务状态")
    p.add_argument("--task", required=True)
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("reviews", help="读取已采集评论")
    p.add_argument("--asin", required=True)
    p.add_argument("--site", default="amz_us", choices=SITES)
    p.add_argument("--star", type=int, choices=range(1, 6))
    p.add_argument("--query")
    p.add_argument("--page", type=int, default=1)
    p.set_defaults(fn=cmd_reviews)

    p = sub.add_parser("charts", help="读取免费星级、趋势、关键词和流向数据")
    p.add_argument("--asin", required=True)
    p.add_argument("--site", default="amz_us", choices=SITES)
    p.add_argument("--days", type=int, default=0)
    p.set_defaults(fn=cmd_charts)

    p = sub.add_parser("quote", help="查询 AI 分析报价（不扣点）")
    add_analysis_args(p)
    p.set_defaults(fn=cmd_quote)

    p = sub.add_parser("analyze", help="AI 分析报价或确认生成")
    add_analysis_args(p)
    p.add_argument("--confirm", action="store_true", help="确认按报价扣点并生成")
    p.set_defaults(fn=cmd_analyze)

    p = sub.add_parser("deepdive", help="产品、图表、评论、报告与 VOC 报价/分析")
    p.add_argument("--asin", required=True)
    p.add_argument("--site", default="amz_us", choices=SITES)
    p.add_argument("--days", type=int, default=365)
    p.add_argument("--report-limit", type=int, default=10)
    p.add_argument("--language", default="zh")
    p.add_argument("--confirm", action="store_true", help="确认 VOC 报价并生成")
    p.set_defaults(fn=cmd_deepdive)

    p = sub.add_parser("reports", help="列出归档报告")
    p.add_argument("--asin")
    p.add_argument("--type")
    p.add_argument("--starred", action="store_true")
    p.add_argument("--query")
    p.add_argument("--limit", type=int, default=20)
    p.set_defaults(fn=cmd_reports)

    p = sub.add_parser("report", help="读取单份归档报告")
    p.add_argument("--id", type=int, required=True)
    p.set_defaults(fn=cmd_report)

    args = ap.parse_args()
    args.fn(args)
    raise SystemExit(_exit_code)


if __name__ == "__main__":
    main()
