#!/usr/bin/env python3
"""ARI CLI for the amazon-product-description-writer Skill.

Uses only Python's standard library. Paid collection and AI analysis commands
require an explicit --confirm flag after a free preview/quote.
"""

import argparse
import getpass
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from concurrent.futures import ThreadPoolExecutor


# VERSION 必须与 _meta.json 的 version 一致：它进 User-Agent，服务端据此统计版本分布
# 并判定最低支持版本。发版时两处一起改。
VERSION = "1.4.11"
# CHANNEL 标记分发渠道（不同市场 listing），由打包脚本按变体烙入；官方母版为空串。
# 非空时 User-Agent 追加 " ch/<渠道>"，服务端据此统计各渠道的注册与用量。
CHANNEL = "description-writer"
PROD_BASE = "https://ari.funewa.com"
TIMEOUT_SEC = 120
# SSE 分析在 meta 事件之后、LLM 首 token 之前可能长时间静默（推理模型可达数分钟）。
# urlopen 的 timeout 是「单次 read 拿不到数据」的上限，若沿用 120s，会在服务端已经
# 扣点并归档之后把一次成功的分析误报成网络错误，进而诱导重试 → 二次扣点。
SSE_TIMEOUT_SEC = 600
SITES = ("amz_us", "amz_uk", "amz_de", "amz_jp", "amz_ca", "amz_fr", "amz_es", "amz_it")
# 轮询时值得重试的错误：瞬时故障不应中止一次已经冻结积点的采集等待。
RETRYABLE_CODES = ("NETWORK_ERROR", "HTTP_ERROR", "ARI_RATE_LIMITED",
                   "ARI_INTERNAL_ERROR", "ARI_UPSTREAM_ERROR")
_exit_code = 0
# 服务端在每个 API Key 响应上广播最新版本，任意一条命令都能顺带发现有新版，
# 不必等用户想起来跑 check。
_release = {"latest": "", "url": ""}

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


class EndpointBlocked(ValueError):
    """Local security failure; never include an untrusted URL or credentials."""

    code = "ARI_ENDPOINT_BLOCKED"


class RedirectBlocked(EndpointBlocked):
    code = "ARI_REDIRECT_BLOCKED"


def validate_official_url(url):
    """Exact HTTPS origin, including authority syntax; TLS verifies the hostname."""
    if not isinstance(url, str) or any(ord(c) <= 32 or ord(c) == 127 for c in url) or "\\" in url:
        raise EndpointBlocked()
    try:
        parsed = urllib.parse.urlsplit(url)
        if (parsed.scheme != "https" or
                parsed.netloc.lower() not in ("ari.funewa.com", "ari.funewa.com:443") or
                parsed.hostname != "ari.funewa.com" or parsed.port not in (None, 443) or
                parsed.username is not None or parsed.password is not None or parsed.fragment):
            raise EndpointBlocked()
    except ValueError:
        raise EndpointBlocked() from None
    return parsed


def base_url():
    """Production builds do not support custom endpoints, even with the old opt-in."""
    override = os.environ.get("ARI_BASE_URL")
    if override:
        parsed = validate_official_url(override)
        if parsed.path not in ("", "/") or parsed.query or "?" in override or "#" in override:
            raise EndpointBlocked()
    return PROD_BASE


def web_root():
    """Account, billing and report links always use the official website."""
    return PROD_BASE


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        # Reject before parsing Location, copying headers, or issuing another request.
        fp.close()
        raise RedirectBlocked()

    http_error_301 = http_error_303 = http_error_307 = http_error_308 = http_error_302


def api_request(method, path, payload=None, params=None, accept="application/json", authenticated=True):
    """Validate the final destination before reading any API key."""
    if not isinstance(path, str) or not path.startswith("/api/v1/") or "?" in path or "#" in path:
        raise EndpointBlocked()
    url = base_url() + path
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    validate_official_url(url)
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": accept, "User-Agent": user_agent()}
    if data is not None:
        headers["Content-Type"] = "application/json"
    if authenticated:
        headers["Authorization"] = "Bearer " + require_key()
    return urllib.request.Request(url, data=data, headers=headers, method=method)


def open_api(req, timeout):
    validate_official_url(req.full_url)
    # A private opener avoids globally installed redirect handlers. Default HTTPS
    # certificate/hostname verification is retained; do not install an insecure context.
    return urllib.request.build_opener(NoRedirect()).open(req, timeout=timeout)


def endpoint_error(exc):
    return error_obj(exc.code, 0, "安全策略已阻止非官方地址或重定向",
                     "仅支持 https://ari.funewa.com。清除自定义 ARI_BASE_URL；"
                     "ARI_ALLOW_CUSTOM_BASE 不再生效。若官方请求发生跳转，请联系 ARI 支持。")


def user_agent():
    """版本号后随渠道尾巴（若有）。服务端按第一个空格截断取版本。"""
    ua = "ARI-Review-Skill/" + VERSION
    return ua + " ch/" + CHANNEL if CHANNEL else ua


def links():
    root = web_root()
    return {
        "apiKeys": root + "/zh/account?ui=d47626f#api-keys",
        "billing": root + "/zh/billing",
        "products": root + "/zh/products",
        "reports": root + "/zh/reports",
        "dashboard": root + "/zh/dashboard",
        "notify": root + "/zh/account#notify",
    }




def report_url(rid):
    """单份报告的网页深链（图表版 / 导出入口）。from=skill 供网页侧归因。"""
    try:
        rid = int(rid)
    except (TypeError, ValueError):
        return None
    if rid <= 0:
        return None
    return "%s/zh/reports/%d?from=skill" % (web_root(), rid)




def config_path():
    return os.path.expanduser("~/.ari/config.json")


def resolve_key():
    """Key 只从 ARI_API_KEY 或用户配置目录读取。

    刻意不回退到 Skill 包目录：那个位置会随 Skill 一起被打包、复制或提交，
    与「Key 只保存在本机用户配置中」的承诺相悖。
    """
    key = os.environ.get("ARI_API_KEY", "").strip()
    if not key:
        path = config_path()
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    key = (json.load(fh).get("api_key") or "").strip()
            except (OSError, json.JSONDecodeError):
                key = ""
    # configure/setup 写入前都校验过前缀，这里再拦一道：环境变量或手工编辑过的
    # 配置文件里放了残缺 Key 时，与其让每个请求 401，不如本地直接说清楚。
    if key and not key.startswith("ari_live_"):
        emit(error_obj(
            "ARI_API_KEY_INVALID_FORMAT", 0,
            "已配置的 Key 不是 ari_live_ 开头，可能残缺或被改动过",
            "运行 python ari.py setup 重新授权，或 configure 重新粘贴完整 Key。"))
        raise SystemExit(2)
    return key or None


def require_key():
    key = resolve_key()
    if key:
        return key
    emit(error_obj(
        "ARI_API_KEY_MISSING", 0,
        "未找到 ARI API Key",
        "推荐运行 python ari.py setup 浏览器一键授权；也可 configure 手动粘贴或设置 ARI_API_KEY。",
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


def version_tuple(v):
    out = []
    for part in str(v or "").split("."):
        try:
            out.append(int(part.strip()))
        except ValueError:
            out.append(0)
    return tuple(out)


def version_cmp(a, b):
    """比较点分版本号，返回 -1/0/1。与服务端 compareVersions 同语义。

    段数不同时短的补 0：裸用元组比较会把 1.0 判成早于 1.0.0（前缀更短即更小），
    从而对已是最新版的用户反复弹升级提示。
    """
    at, bt = version_tuple(a), version_tuple(b)
    n = max(len(at), len(bt))
    at += (0,) * (n - len(at))
    bt += (0,) * (n - len(bt))
    return (at > bt) - (at < bt)


def note_release(headers):
    """记录服务端广播的最新版本（响应头），供 update_info 生成升级提示。"""
    try:
        latest = (headers.get("X-ARI-Skill-Latest") or "").strip()
        url = (headers.get("X-ARI-Skill-Update-Url") or "").strip()
    except Exception:
        return
    if latest:
        _release["latest"] = latest
    if url:
        _release["url"] = url


def update_info():
    """本地版本低于服务端最新版时返回升级提示，否则 None。

    只在「确实更旧」时提示：本地版本更新（开发中）不该反复告警。
    """
    latest = _release.get("latest") or ""
    if not latest or version_cmp(VERSION, latest) >= 0:
        return None
    return {
        "current": VERSION, "latest": latest,
        "url": _release.get("url") or links()["apiKeys"],
        "message": "有新版 Skill（%s → %s）。请通过原安装渠道更新后再使用；"
                   "本 CLI 不会自行下载或执行任何远端代码。" % (VERSION, latest),
    }


def emit(obj, compact=False):
    global _exit_code
    if isinstance(obj, dict) and obj.get("success") is False:
        _exit_code = 1
    if isinstance(obj, dict):
        upd = update_info()
        if upd:
            obj["update"] = upd
    print(json.dumps(
        obj, ensure_ascii=False,
        separators=((",", ":") if compact else (", ", ": ")),
        indent=(None if compact else 2),
    ))


def err_code(out):
    if not isinstance(out, dict):
        return ""
    err = out.get("error")
    if isinstance(err, dict) and err.get("code"):
        return str(err["code"])
    return str(out.get("code") or "")




def parse_http_error(exc, query):
    note_release(exc.headers)  # 426（版本过旧）等错误响应同样带广播头
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


def as_collecting(out, http_status):
    """把「采集中、暂无足够数据」的 202 转成显式错误码。

    服务端在这种情况下返回 202 + success:true，但信封里既没有报告也没有内容；
    照原样交给上层会被当成一次成功的分析。该分支未扣点，重试是免费的。
    """
    if http_status != 202 or not isinstance(out, dict):
        return None
    data = out.get("data")
    if not isinstance(data, dict) or data.get("status") != "COLLECTING":
        return None
    wait = data.get("retryAfterSeconds") or 30
    return error_obj(
        "ARI_COLLECTING", 202, "该 ASIN 正在采集中，暂无足够数据可分析",
        "本次未扣点。等待约 %s 秒后重试即可（该分支重试免费）。" % wait)


def request_json(method, path, payload=None, params=None):
    query = {
        "method": method,
        "path": path,
        "params": {k: v for k, v in (params or {}).items() if v not in (None, "")},
        "payload": payload,
    }
    try:
        req = api_request(method, path, payload, query["params"])
        with open_api(req, timeout=TIMEOUT_SEC) as resp:
            note_release(resp.headers)
            raw = resp.read().decode("utf-8")
            out = json.loads(raw) if raw else {"success": True, "data": None}
            if isinstance(out, dict):
                alt = as_collecting(out, resp.status)
                if alt is not None:
                    alt["_query"] = query
                    return alt
                out["_query"] = query
            return out
    except EndpointBlocked as exc:
        return endpoint_error(exc)
    except urllib.error.HTTPError as exc:
        return parse_http_error(exc, query)
    except Exception as exc:
        return error_obj("NETWORK_ERROR", 0, str(exc), "检查网络或 ARI 官方服务状态", query)


def request_sse(path, payload, recovery_hint=None):
    query = {"method": "POST", "path": path, "params": {}, "payload": payload}
    result = {"meta": None, "content": "", "result": None, "reportId": 0, "creditsUsed": 0}
    try:
        req = api_request("POST", path, payload, accept="text/event-stream")
        with open_api(req, timeout=SSE_TIMEOUT_SEC) as resp:
            note_release(resp.headers)
            content_type = resp.headers.get("Content-Type", "")
            if "text/event-stream" not in content_type:
                # 就绪检查等前置校验在开流之前返回普通 JSON。
                raw = resp.read().decode("utf-8")
                out = json.loads(raw) if raw else {"success": True, "data": None}
                alt = as_collecting(out, resp.status)
                if alt is not None:
                    alt["_query"] = query
                    return alt
                out["_query"] = query
                return out

            for raw_line in resp:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line.startswith("data: "):
                    continue
                raw = line[6:].strip()
                if not raw:
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
                    result["result"] = event.get("data") or {
                        k: v for k, v in event.items() if k != "type"
                    }
                    result["reportId"] = event.get("reportId") or 0
                elif kind == "done":
                    result["creditsUsed"] = event.get("creditsUsed") or 0
                    result["reportId"] = event.get("reportId") or result["reportId"]
                    for key in ("requestId", "taskId", "reportUrl"):
                        if event.get(key):
                            result[key] = event[key]
                elif kind == "error":
                    return error_obj(
                        event.get("code") or "ARI_ANALYSIS_ERROR", 200,
                        event.get("message") or "analysis failed",
                        "已生成的部分内容保留在 partial 中", query, result)
            if result.get("reportId"):
                result["reportUrl"] = report_url(result["reportId"])
            return {"success": True, "data": result, "_query": query, "links": links()}
    except EndpointBlocked as exc:
        return endpoint_error(exc)
    except urllib.error.HTTPError as exc:
        return parse_http_error(exc, query)
    except Exception as exc:
        # 流中断（socket 超时 / 连接断开）时服务端往往已经跑完、扣点并归档。
        # 这里绝不能提示「重试」——重跑 --confirm 会为同一份报告扣第二次点。
        return error_obj(
            "ARI_STREAM_INTERRUPTED", 0, "分析流中断：%s" % exc,
            recovery_hint or
            "本次分析可能已扣点并已归档。请先运行 reports --asin <ASIN> --limit 1 "
            "确认是否已生成新报告；确认没有生成后才可重试，不要直接重跑 --confirm。",
            query, result)


def fetch_release():
    """读取公开的版本发布信息（免认证，Key 缺失或失效时也能拿到升级入口）。

    失败一律静默返回 None——查不到新版说明不该影响任何正常命令。
    """
    try:
        req = api_request("GET", "/api/v1/public/config", authenticated=False)
        with open_api(req, timeout=15) as resp:
            note_release(resp.headers)
            body = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None
    rel = ((body or {}).get("data") or {}).get("skillRelease")
    if not isinstance(rel, dict):
        return None
    if rel.get("latest"):
        _release["latest"] = str(rel["latest"])
    if rel.get("url"):
        _release["url"] = str(rel["url"])
    return rel


def data_of(out):
    return out.get("data") if isinstance(out, dict) else None


def ok(out):
    return isinstance(out, dict) and out.get("success") is True






def save_key(key):
    """写本机用户配置（0600 直接创建，避免「默认权限 → chmod」之间的可读窗口）。"""
    path = config_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump({"api_key": key}, fh)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return path


def cmd_configure(args):
    key = getpass.getpass("ARI API Key (ari_live_*): ").strip()
    if not key.startswith("ari_live_"):
        emit(error_obj("ARI_API_KEY_INVALID_FORMAT", 0, "Key 必须以 ari_live_ 开头"), args.compact)
        raise SystemExit(2)
    path = save_key(key)
    emit({"success": True, "data": {
        "configured": True, "path": path,
        "note": "Windows 上 POSIX 权限位不生效，请自行确保该路径不被共享或同步到云端。",
    }}, args.compact)


def request_public(method, path, payload=None, timeout=15):
    """免认证请求（设备码授权等公开端点），错误统一转 error_obj。"""
    query = {"method": method, "path": path, "params": {}, "payload": payload}
    try:
        req = api_request(method, path, payload, authenticated=False)
        with open_api(req, timeout=timeout) as resp:
            note_release(resp.headers)
            out = json.loads(resp.read().decode("utf-8"))
            if isinstance(out, dict):
                out["_query"] = query
            return out
    except EndpointBlocked as exc:
        return endpoint_error(exc)
    except urllib.error.HTTPError as exc:
        return parse_http_error(exc, query)
    except Exception as exc:
        return error_obj("NETWORK_ERROR", 0, str(exc), "检查网络或 ARI 官方服务状态", query)


def cmd_setup(args):
    """设备码授权：浏览器点一下，Key 自动落到本机，全程无复制粘贴。

    进度提示走 stderr（用户/代理立即可见），stdout 仍只输出最终 JSON。
    刻意不在 CLI 里做注册：注册留在网页（人机验证与邮箱验证防线不动）。
    """
    start = request_public("POST", "/api/v1/auth/device/start", {})
    if not ok(start):
        emit(start, args.compact)
        return
    data = start.get("data") or {}
    code = str(data.get("code") or "")
    verify_url = str(data.get("verifyUrl") or "")
    token = str(data.get("pollToken") or "")
    interval = max(1, int(data.get("interval") or 3))
    expires = int(data.get("expiresIn") or 600)
    if not (code and verify_url and token):
        emit(error_obj("ARI_DEVICE_START_MALFORMED", 0, "服务端响应缺少必要字段"), args.compact)
        return

    try:
        validate_official_url(verify_url)
    except EndpointBlocked as exc:
        emit(endpoint_error(exc), args.compact)
        return

    print("请在浏览器打开以下链接完成授权（设备码 %s，%d 分钟内有效）：" % (code, expires // 60),
          file=sys.stderr)
    print("  " + verify_url, file=sys.stderr)
    print("未注册会先引导注册（需完成邮箱验证）；授权后本命令自动完成。", file=sys.stderr)

    deadline = time.time() + expires
    while time.time() < deadline:
        time.sleep(interval)
        poll = request_public("POST", "/api/v1/auth/device/poll", {"pollToken": token})
        if not ok(poll):
            if err_code(poll) in ("ARI_NOT_FOUND", "ARI_ENDPOINT_BLOCKED", "ARI_REDIRECT_BLOCKED"):
                emit(poll, args.compact)
                return
            continue  # 网络抖动/限流：下轮再试
        status = str((poll.get("data") or {}).get("status") or "")
        if status == "APPROVED":
            key = str((poll.get("data") or {}).get("apiKey") or "")
            if not key.startswith("ari_live_"):
                emit(error_obj("ARI_DEVICE_KEY_MALFORMED", 0, "服务端未返回有效 Key"), args.compact)
                return
            path = save_key(key)
            emit({"success": True, "data": {
                "configured": True, "path": path,
                "keyPrefix": key[:len("ari_live_") + 8],
                "note": "API Key 已保存到本机用户配置，其余命令可直接使用。",
            }}, args.compact)
            return
        if status == "CLAIMED":
            emit(error_obj(
                "ARI_DEVICE_ALREADY_CLAIMED", 0, "该会话的 Key 已被领取",
                "若非你本人操作，请到用户中心撤销该 Key 后重新运行 setup。"), args.compact)
            return
        if status == "EXPIRED":
            break
    emit(error_obj(
        "ARI_DEVICE_EXPIRED", 0, "授权未在有效期内完成",
        "重新运行 python ari.py setup 并尽快在浏览器完成授权。"), args.compact)


def cmd_check(args):
    # 先取公开发布信息：Key 无效时也能顺带告诉用户「你的版本旧了、去哪儿更新」。
    release = fetch_release()
    me = request_json("GET", "/api/v1/user/me")
    if not ok(me):
        emit(me, args.compact)
        return
    balance = request_json("GET", "/api/v1/credits/balance")
    if not ok(balance):
        emit(balance, args.compact)
        return
    # 1.4.11：不再回报账户免确认策略。它只服务于「小额付费操作直接生成」，等于把
    # 「不用先问」交给 agent，与全系列「先报价、用户明确确认才执行」的契约冲突
    # （ClawSweeper 归类为 Autonomous Decision Making）。付费门槛仍由服务端策略
    # 控制，本地不做任何隐式确认，所以 check 只回 Key、账户与余额。
    emit({"success": True, "data": {
        "skillVersion": VERSION,
        "release": release,
        "user": data_of(me),
        "balance": data_of(balance),
    }, "links": links()}, args.compact)








def usable_balance(site):
    """返回该站点实际可用于采集的积点。

    赠送积点（注册礼/Free 周期发放/任务奖励等）只能在 amz_us 消费；
    付费积点（订阅套餐周期积点、增量包）全站可用。服务端在 balance 里
    给出 nonUsCollectCredits（非美站可用额），以它为准——
    只报「总余额」会让用户在余额看似充足的情况下确认后吃 402。
    返回 (info, err)：err 非 None 时应直接把它 emit 出去。
    """
    bal = request_json("GET", "/api/v1/credits/balance")
    if not ok(bal):
        return None, bal
    d = data_of(bal) or {}
    plan = int((d.get("planCredits") or {}).get("available") or 0)
    addon = int((d.get("addonCredits") or {}).get("available") or 0)
    if site == "amz_us":
        return {"usable": plan + addon, "planCredits": plan, "addonCredits": addon,
                "note": ""}, None
    non_us = d.get("nonUsCollectCredits")
    if non_us is None:
        # 旧服务端没有该字段时保守回落：只按付费增量包算，宁可少报不误导确认。
        non_us = addon
    return {"usable": int(non_us), "planCredits": plan, "addonCredits": addon,
            "note": "非美国站采集仅可使用付费积点（订阅套餐/增量包），赠送积点不可用。"}, None


def collection_plan(asin, site, pages, star="all_stars", sort="recent", alias=""):
    pricing = request_json("GET", "/api/v1/billing/pricing")
    if not ok(pricing):
        return None, pricing
    pdata = data_of(pricing) or {}
    price = int(pdata.get("collectPerPage") or 5)
    max_pages = int(pdata.get("maxPages") or 10)
    if pages > max_pages:
        return None, error_obj(
            "ARI_COLLECT_PAGE_LIMIT", 403,
            "单次采集超过 %d 页需要月付 Professional 套餐或累计充值满 ¥99" % max_pages,
            "请改用 --pages %d，或升级套餐 / 充值后再采集更多页。" % max_pages)
    bal, err = usable_balance(site)
    if err is not None:
        return None, err
    return {
        # 采集是固定单价：credits = 单价 × 页数，不是估算区间。上游评论不够这么多页时
        # 只收实际采到的页数（网关按商品评论总数预裁），差额自动退回。
        "credits": pages * price,
        "pricePerPage": price,
        "pages": pages,
        "approxReviews": pages * int(pdata.get("reviewsPerPage") or 10),
        "balance": bal,
        "maxPages": max_pages,
        "payload": {
            "asin": asin.upper(), "site": site, "pageCount": pages,
            "filterByStar": star, "sortBy": sort, "alias": alias,
        },
    }, None


def collection_quote(plan):
    bal = plan["balance"]
    return {
        "confirmationRequired": True,
        "credits": plan["credits"],
        "pricePerPage": plan["pricePerPage"],
        "pages": plan["pages"],
        "approxReviews": plan["approxReviews"],
        "usableBalance": bal["usable"],
        "planCredits": bal["planCredits"],
        "addonCredits": bal["addonCredits"],
        "sufficient": bal["usable"] >= plan["credits"],
        "siteNote": bal["note"],
        "pricingNote": "固定 %d 积点/页 × %d 页 = %d 积点；评论不够这么多页时只收实际采到的页数，差额自动退回。"
                       % (plan["pricePerPage"], plan["pages"], plan["credits"]),
        "message": "确认后用同一命令追加 --confirm；需要等待完成再追加 --wait。",
        "request": plan["payload"],
    }


def execute_collection(plan, wait, interval, timeout):
    bal = plan["balance"]
    estimate = plan["credits"]
    site = plan["payload"]["site"]
    if bal["usable"] < estimate:
        return error_obj(
            "ARI_INSUFFICIENT_CREDITS", 402, "积点不足",
            "本次需要 %d 点（%d 积点/页 × %d 页），%s 站可用 %d 点。%s请充值后重试。"
            % (estimate, plan["pricePerPage"], plan["pages"], site, bal["usable"],
               bal["note"] and bal["note"] + " "))
    out = request_json("POST", "/api/v1/collection/submit", plan["payload"])
    if wait and ok(out):
        task_id = (data_of(out) or {}).get("taskId")
        if task_id:
            submitted = data_of(out)
            final = wait_task(task_id, interval, timeout)
            if ok(final):
                out = {"success": True, "data": {"submitted": submitted,
                                                   "final": data_of(final)},
                       "links": links()}
            else:
                final["submitted"] = submitted
                out = final
    return out


def wait_task(task_id, interval, timeout):
    """轮询到任务终态。jobs 表的状态集合是 queued/running/done/failed。

    单次瞬时错误不中止等待：此时采集积点已冻结、任务仍在后台跑，
    直接返回会让调用方误以为采集已经结束。
    """
    deadline = time.time() + timeout
    last = None
    transient = 0
    while time.time() < deadline:
        last = request_json("GET", "/api/v1/collection/status/" + urllib.parse.quote(task_id))
        if ok(last):
            transient = 0
            status = str((data_of(last) or {}).get("status") or "").lower()
            if status in ("done", "failed"):
                return last
        elif err_code(last) in RETRYABLE_CODES:
            transient += 1
            if transient >= 3:
                last["hint"] = ("连续 %d 次查询失败；采集任务仍可能在后台运行，"
                                "稍后用 status --task %s 查询。" % (transient, task_id))
                return last
        else:
            return last
        time.sleep(interval)
    return error_obj("WAIT_TIMEOUT", 0, "等待采集超时，任务仍可能在后台运行",
                     "稍后使用 status --task %s 查询" % task_id,
                     partial=data_of(last) if last else None)


def cmd_collect(args):
    plan, err = collection_plan(args.asin, args.site, args.pages,
                                args.star, args.sort, args.alias)
    if err is not None:
        emit(err, args.compact)
        return
    if not args.confirm:
        emit({"success": True, "data": collection_quote(plan), "links": links()}, args.compact)
        return
    emit(execute_collection(plan, args.wait, args.interval, args.timeout), args.compact)




























def cmd_status(args):
    emit(request_json("GET", "/api/v1/collection/status/" + urllib.parse.quote(args.task)), args.compact)
























def operation_defaults():
    """Read immutable workflow defaults generated into specialized Skills."""
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "skill-defaults.json")
    try:
        with open(path, encoding="utf-8") as fh:
            value = json.load(fh)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def allowed_commands():
    """专属包构建期写入的命令白名单；返回 None 表示不限制。

    1.4.11 起打包脚本会把文档没有承诺的命令从本文件里整段删掉。这里再读
    一次 skill-defaults.json 兜底：只删代码不留闸的话，任何人把命令加回来
    就绕过了收窄。母版与全功能马甲包没有这个字段，行为完全不变。
    """
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "skill-defaults.json")
    try:
        with open(path, encoding="utf-8") as fh:
            value = json.load(fh)
    except (OSError, ValueError):
        return None
    if not isinstance(value, dict):
        return None
    commands = value.get("allowedCommands")
    if not isinstance(commands, list):
        return None
    allowed = {item.strip() for item in commands
               if isinstance(item, str) and item.strip()}
    return allowed or None


def operation_payload(args):
    defaults = operation_defaults()
    workflow = (getattr(args, "workflow", None) or defaults.get("workflow") or "").strip()
    focus = (getattr(args, "focus", None) or defaults.get("focus") or "").strip()
    if not workflow or not focus:
        return None, error_obj(
            "ARI_VALIDATION_ERROR", 0, "运营工作流缺少 workflow/focus",
            "通用 Skill 请显式传 --workflow 和 --focus；专属 Skill 会内置固定值。")
    request_id = (getattr(args, "request_id", None) or "").strip() or str(uuid.uuid4())
    return {
        "requestId": request_id,
        "workflow": workflow,
        "focus": focus,
        "asin": args.asin.upper(),
        "site": args.site or defaults.get("defaultSite") or "amz_us",
        "competitorAsin": (getattr(args, "competitor", None) or "").upper(),
    }, None


def operation_contract(payload):
    capabilities = request_json("GET", "/api/v1/product-operations/capabilities")
    if not ok(capabilities):
        return capabilities
    data = data_of(capabilities) or {}
    if not data.get("enabled"):
        return error_obj("ARI_OPERATIONS_DISABLED", 403,
                         "当前账户尚未启用商品运营工具", "请稍后再试或联系管理员开通灰度。")
    supported = False
    for item in data.get("workflows") or []:
        if (item.get("workflow") == payload["workflow"] and
                payload["focus"] in (item.get("focuses") or [])):
            supported = True
            break
    if not supported:
        return error_obj("ARI_INVALID_OPERATIONS_WORKFLOW", 422,
                         "服务端不支持该 workflow/focus 组合",
                         "先运行 operations capabilities 查看当前白名单。")
    return None


def operation_quote(args):
    payload, err = operation_payload(args)
    if err is not None:
        return err
    contract_err = operation_contract(payload)
    if contract_err is not None:
        return contract_err
    out = request_json("POST", "/api/v1/product-operations/quote", payload)
    data = data_of(out)
    if ok(out) and isinstance(data, dict):
        data["request"] = payload
        data["confirmationRequired"] = True
        data["message"] = "确认后使用同一 requestId 运行 operations run --confirm。"
    return out


def cmd_operation_capabilities(args):
    emit(request_json("GET", "/api/v1/product-operations/capabilities"), args.compact)


def cmd_operation_profile(args):
    emit(request_json("GET", "/api/v1/product-operations/profile",
                      params={"asin": args.asin.upper(), "site": args.site}), args.compact)


def cmd_operation_quote(args):
    emit(operation_quote(args), args.compact)


def cmd_operation_run(args):
    quote = operation_quote(args)
    if not ok(quote):
        emit(quote, args.compact)
        return
    quote_data = data_of(quote) or {}
    payload = quote_data.get("request") or {}
    details = quote_data.get("quote") or {}
    if not args.confirm:
        emit(quote, args.compact)
        return
    if not details.get("reviewReady", False):
        emit(error_obj("ARI_INSUFFICIENT_REVIEWS", 422, "评论尚未达到运营分析要求",
                       "先使用现有 collect 命令采集评论；不会隐式采集或扣分析点。"), args.compact)
        return
    if details.get("missingFields"):
        emit(error_obj("ARI_PRODUCT_FIELDS_INSUFFICIENT", 422,
                       "商品详情关键字段不足", "稍后刷新商品资料后重新报价。"), args.compact)
        return
    if not details.get("sufficient", False):
        emit(error_obj("ARI_INSUFFICIENT_CREDITS", 402, "积点不足",
                       "需要 %s 点，当前余额 %s。" %
                       (details.get("price"), details.get("balance"))), args.compact)
        return
    rid = payload.get("requestId") or "<requestId>"
    hint = ("本次运营任务可能已继续执行。不要直接重跑；先运行 operations status "
            "--request-id %s 精确查询状态。" % rid)
    emit(request_sse("/api/v1/product-operations/run", payload, hint), args.compact)


def cmd_operation_status(args):
    request_id = urllib.parse.quote(args.request_id.strip(), safe="")
    emit(request_json("GET", "/api/v1/product-operations/runs/" + request_id), args.compact)






























ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")
# 文档示例里的占位 ASIN：格式合法但必然不是真实商品，单独拦截并给出明确指引。
PLACEHOLDER_ASINS = {"B0XXXXXXXX", "B0AAAAAAAA", "B0BBBBBBBB"}


def check_asin_args(args):
    """本地快速失败：格式错误的 ASIN 不值得打到服务端换一个模糊的 4xx。

    ASIN 只保证 10 位字母数字，不保证以 B 开头（书类沿用 ISBN-10，数字开头），
    所以校验不能写死 B 前缀。顺手把值归一成大写，后续命令不必再 upper()。
    """
    for attr in ("asin", "competitor"):
        value = getattr(args, attr, None)
        if value in (None, ""):
            continue
        normalized = str(value).strip().upper()
        if not ASIN_RE.match(normalized) or normalized in PLACEHOLDER_ASINS:
            emit(error_obj(
                "ARI_INVALID_ASIN", 0,
                "%s 不是有效的 ASIN（应为 10 位字母数字，如 B08N5WRWNW）" % value,
                "请从商品详情页 URL 的 /dp/ 后复制真实 ASIN；文档中的占位符示例不能直接使用。"),
                args.compact)
            raise SystemExit(2)
        setattr(args, attr, normalized)


def cmd_version(args):
    emit({"success": True, "data": {
        "skillVersion": VERSION,
        "channel": CHANNEL or "official",
        "python": sys.version.split()[0],
    }}, args.compact)




def add_operation_args(parser, confirm=False):
    parser.add_argument("--asin", required=True)
    parser.add_argument("--site", default="amz_us", choices=SITES)
    parser.add_argument("--workflow")
    parser.add_argument("--focus")
    parser.add_argument("--competitor")
    parser.add_argument("--request-id", default="")
    if confirm:
        parser.add_argument("--confirm", action="store_true",
                            help="确认按报价扣点并生成；未提供时只返回报价")




def main():
    # --compact 用 parents 挂到每个子命令上，这样放在子命令前后都能识别。
    # default=SUPPRESS 是必须的：否则子解析器会用自己的默认值覆盖掉
    # 已经在顶层解析出来的 --compact。缺省值只能在 parse_args 之后补，
    # 不能用 set_defaults——parents 共享同一个 action 对象，
    # set_defaults 会把 SUPPRESS 改掉，反而把覆盖问题带回来。
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--compact", action="store_true",
                        default=argparse.SUPPRESS, help="输出单行 JSON")

    ap = argparse.ArgumentParser(prog="ari.py", parents=[common],
                                 description="ARI Amazon 评论采集与智能分析 CLI")
    sub = ap.add_subparsers(dest="command", required=True)

    p = sub.add_parser("setup", parents=[common],
                       help="浏览器一键授权，自动获取并保存 API Key（推荐首次使用）")
    p.set_defaults(fn=cmd_setup)

    p = sub.add_parser("configure", parents=[common], help="隐藏输入并保存 ARI API Key")
    p.set_defaults(fn=cmd_configure)

    p = sub.add_parser("check", parents=[common], help="验证 Key、账户和积点余额")
    p.set_defaults(fn=cmd_check)


    p = sub.add_parser("version", parents=[common], help="显示 Skill 版本与渠道（无需 Key）")
    p.set_defaults(fn=cmd_version)


    p = sub.add_parser("collect", parents=[common], help="采集报价或提交采集任务")
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

    p = sub.add_parser("status", parents=[common], help="查询采集任务状态")
    p.add_argument("--task", required=True)
    p.set_defaults(fn=cmd_status)

















    operations_parser = sub.add_parser(
        "operations", parents=[common], help="商品运营工具：能力、资料、报价、运行与状态")
    operations_sub = operations_parser.add_subparsers(dest="operations_command", required=True)

    p = operations_sub.add_parser("capabilities", parents=[common], help="查看运营能力与套餐限制")
    p.set_defaults(fn=cmd_operation_capabilities)

    p = operations_sub.add_parser("profile", parents=[common], help="读取商品资料与字段完整度")
    p.add_argument("--asin", required=True)
    p.add_argument("--site", default="amz_us", choices=SITES)
    p.set_defaults(fn=cmd_operation_profile)

    p = operations_sub.add_parser("quote", parents=[common], help="运营分析报价（不扣点）")
    add_operation_args(p)
    p.set_defaults(fn=cmd_operation_quote)

    p = operations_sub.add_parser("run", parents=[common], help="报价或确认运行运营分析")
    add_operation_args(p, confirm=True)
    p.set_defaults(fn=cmd_operation_run)

    p = operations_sub.add_parser("status", parents=[common], help="按 requestId 精确查询运营任务")
    p.add_argument("--request-id", required=True)
    p.set_defaults(fn=cmd_operation_status)











    args = ap.parse_args()
    if not hasattr(args, "compact"):
        args.compact = False
    # 专属包的运行期兜底闸。打包脚本（scripts/build_skill_variants.py）已把
    # 未承诺的命令从本文件整段删掉，这里再按 skill-defaults.json 的
    # allowedCommands 复核一次——只删代码不留闸的话，把命令加回来就绕过了收窄。
    allowed = allowed_commands()
    if allowed is not None and getattr(args, "command", None) not in allowed:
        emit(error_obj(
            "ARI_COMMAND_NOT_ALLOWED", 0,
            "本包不提供 %s 命令" % getattr(args, "command", "?"),
            "此 Skill 只提供：%s。需要其他能力请安装对应的 ARI Skill 包。" %
            "、".join(sorted(allowed))), args.compact)
        raise SystemExit(2)
    check_asin_args(args)
    args.fn(args)
    raise SystemExit(_exit_code)


if __name__ == "__main__":
    main()
