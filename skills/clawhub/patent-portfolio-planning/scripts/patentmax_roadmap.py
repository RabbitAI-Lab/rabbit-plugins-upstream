#!/usr/bin/env python3
"""PatentMax 技术路线分析客户端。

给 AI 用的命令行工具，每个子命令往 stdout 吐一份 JSON，出错时 JSON 里带
error 和中文提示，不抛栈。

跟企业情报分析同源（都走 POST /api/v1/reports），差别在 roadmap_context：
那十个字段是业务约束——你什么时候发布、有多少预算、能申请几件、哪些东西
不能公开——布局建议只有贴着这些约束才有用，否则就是"建议全面布局"这种废话。

三件事在这里处理掉：

1. **Idempotency-Key 必填**。默认按请求内容算稳定指纹，同样输入重试天然幂等，
   不会重复建任务、重复扣费。

2. **轮询退避**。这类报告跑几十分钟，间隔从 10 秒退到 60 秒。
   超时不代表失败，任务还在服务端跑。

3. **roadmap_context 从文件读**。十个字段写在命令行里没法看，
   支持用 --context-file 给一个 JSON。

4. **必填只有 --subject（技术主题）**。素材、分析目标、业务约束都可不填；
   素材和目标不填时按网页端的写法补一句，新旧版本的服务端都接受。

依赖：只用标准库，不需要 pip install。
"""

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_URL = os.environ.get("PATENTMAX_BASE_URL", "https://api.ip930.com").rstrip("/")
API_KEY = os.environ.get("PATENTMAX_API_KEY", "").strip()
TIMEOUT = 60


# ─────────────────────── 免费试用密钥 ───────────────────────
#
# 没设 PATENTMAX_API_KEY 时，第一次调用自动领一把免费试用密钥（不用注册），
# 存在 ~/.patentmax/ 下，之后接着用。规则由服务端定：每把累计 ¥40、30 天有效、
# 只开通这个 Skill 用到的功能。用完或过期后，注册 PatentMax 换正式密钥即可。
# 设了 PATENTMAX_API_KEY 就一律用它，不会去领试用。
TRIAL_SOURCE = "patent-portfolio-planning"
TRIAL_GROUP = "roadmap"
TRIAL_REGISTER_URL = "https://api.ip930.com/features/api-platform"
KEY_FROM_TRIAL = False


def _trial_key_path():
    root = os.environ.get("PATENTMAX_CACHE_DIR") or os.path.join(os.path.expanduser("~"), ".patentmax")
    return os.path.join(root, f"trial-key-{TRIAL_GROUP}.json")


def _load_trial_key():
    try:
        with open(_trial_key_path(), encoding="utf-8") as fh:
            saved = json.load(fh)
    except (OSError, ValueError):
        return None
    if not isinstance(saved, dict) or saved.get("base_url") != BASE_URL:
        return None
    expires = str(saved.get("expires_at") or "")
    # ISO 时间同为 UTC，可直接按字符串比
    if expires and expires <= time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()):
        return None
    return saved.get("api_key") or None


def _server_message(detail):
    try:
        body = json.loads(detail)
    except ValueError:
        return ""
    error = body.get("error") if isinstance(body, dict) else None
    return str(error.get("message") or "") if isinstance(error, dict) else ""


def _claim_trial_key():
    url = f"{BASE_URL}/api/v1/trial-keys"
    data = json.dumps({"source": TRIAL_SOURCE}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        message = _server_message(exc.read().decode("utf-8", "replace"))
        die(message or f"领取免费试用密钥失败（HTTP {exc.code}）。也可以注册 PatentMax 创建正式密钥：{TRIAL_REGISTER_URL}",
            free_trial=True, register_url=TRIAL_REGISTER_URL)
    except (urllib.error.URLError, TimeoutError, ConnectionError, ValueError) as exc:
        die(f"领取免费试用密钥失败：{getattr(exc, 'reason', exc)}", free_trial=True)
    data = payload.get("data") if isinstance(payload, dict) else None
    key = data.get("api_key") if isinstance(data, dict) else None
    if not key:
        die("领取免费试用密钥失败：服务端没有返回密钥。", free_trial=True)
    path = _trial_key_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({
                "api_key": key,
                "expires_at": data.get("expires_at"),
                "spending_limit_yuan": data.get("spending_limit_yuan"),
                "source": TRIAL_SOURCE,
                "base_url": BASE_URL,
            }, fh, ensure_ascii=False, indent=2)
        os.chmod(path, 0o600)
    except OSError:
        pass  # 存不下就只用这一次，下次再领
    # 走 stderr，不混进 stdout 的 JSON；请把这句话转告用户。Windows 控制台默认 GBK，¥ 会变成转义
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    print(f"[PatentMax] 已自动领取免费试用：{data.get('note') or ''}", file=sys.stderr)
    return key


def ensure_api_key():
    """有 PATENTMAX_API_KEY 用它；没有就用本地存的试用密钥，再没有就领一把。"""
    global API_KEY, KEY_FROM_TRIAL
    if API_KEY:
        return API_KEY
    API_KEY = _load_trial_key() or _claim_trial_key()
    KEY_FROM_TRIAL = True
    return API_KEY


def explain_trial_error(code, detail, url):
    """试用密钥碰到额度用完、功能没开通时，原样给出服务端的话（里面有下一步怎么办）。"""
    if not KEY_FROM_TRIAL:
        return
    if code == 401:
        # 过期或被停用：清掉本地缓存，下次运行自动领新的
        try:
            os.remove(_trial_key_path())
        except OSError:
            pass
        die("免费试用密钥已过期或失效，本地缓存已清除。重跑同一条命令会自动领取新的试用密钥；"
            f"也可以注册 PatentMax 换正式密钥：{TRIAL_REGISTER_URL}",
            free_trial=True, url=url.split("?")[0])
    # 只接管试用特有的错误（额度用完、功能没开通），其余照常走通用提示
    message = _server_message(detail)
    if "免费试用" in message:
        die(f"HTTP {code}：{message}", free_trial=True, register_url=TRIAL_REGISTER_URL, url=url.split("?")[0])
REPORT_TYPE = "roadmap_layout"

#: roadmap_context 的十个可选字段。每项都能留空，填了布局建议才贴合实际约束。
CONTEXT_FIELDS = {
    "future_plan": "未来规划：接下来一到三年打算做什么",
    "existing_assets": "现有资产：已有的专利、产线、技术积累",
    "own_advantages": "自身优势：相对竞争对手强在哪",
    "known_risks": "已知风险：担心撞上谁、哪些方向有雷",
    "evidence_data": "证据数据：实验数据、参数、验证结果",
    "disclosure_timing": "公开时点：什么时候要发布、参展、投标",
    "filing_preference": "申请偏好：发明为主还是实用新型、国内还是 PCT",
    "budget_and_volume": "预算与数量：今年打算申请几件、预算多少",
    "confidentiality_limits": "保密边界：哪些内容不能写进公开文件",
    "excluded_directions": "排除方向：明确不做的领域",
}

QUALITY_HINT = {
    "qualified": "报告通过质量校验，可作为布局决策依据。",
    "qualified_degraded": "报告已生成但存在数据短板，布局建议要保守使用，交付时须说明限制。",
    "review_required": "报告需要人工复核，不要直接当作布局方案交给决策层。",
}


def die(message, **extra):
    payload = {"error": True, "message": message}
    payload.update(extra)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    sys.exit(1)


def request(path, method="GET", body=None, headers=None, raw=False):
    ensure_api_key()

    url = path if path.startswith("http") else f"{BASE_URL}{path}"
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Accept", "application/json")
    if data:
        req.add_header("Content-Type", "application/json")
    for key, value in (headers or {}).items():
        req.add_header(key, value)

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            payload = response.read()
            return payload if raw else json.loads(payload.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:600]
        explain_trial_error(exc.code, detail, url)
        hint = {
            400: "参数不正确，detail 里逐项写了缺什么、怎么填。必填只有 --subject（技术主题，至少 3 字）；"
                 "roadmap_context 每项最长 2000 字（公开时点/申请偏好/预算/保密边界为 500 字）。",
            401: "密钥无效或已撤销。",
            402: "余额不足，到 https://api.ip930.com/features/api-platform 充值。",
            403: "该密钥没有此接口的权限。",
            404: "任务或报告不存在。确认 id 抄全了。",
            409: "任务冲突：报告还没跑完就来取结果，或同一个 Idempotency-Key 正在处理中。",
            429: "触发限流或已有同类任务在排队，稍后再试。",
        }.get(exc.code, "")
        die(f"HTTP {exc.code}：{hint}", detail=detail, url=url.split("?")[0])
    except urllib.error.URLError as exc:
        die(f"网络请求失败：{exc.reason}")
    except json.JSONDecodeError:
        die("响应不是合法 JSON，可能上游异常。")


def unwrap(payload):
    if isinstance(payload, dict) and "data" in payload:
        return payload["data"]
    return payload


def fingerprint(body):
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
    return "pmr-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def read_text(direct, path, label):
    if path:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                text = handle.read().strip()
        except OSError as exc:
            die(f"读不到{label}文件：{exc}")
        if not text:
            die(f"{label}文件是空的：{path}")
        return text
    return (direct or "").strip()


def build_context(args):
    """roadmap_context 支持两种给法：--context-file 给 JSON，或逐个命令行参数。"""
    context = {}
    if args.context_file:
        try:
            with open(args.context_file, "r", encoding="utf-8") as handle:
                loaded = json.load(handle)
        except OSError as exc:
            die(f"读不到 context 文件：{exc}")
        except json.JSONDecodeError as exc:
            die(f"context 文件不是合法 JSON：{exc}")
        if not isinstance(loaded, dict):
            die("context 文件必须是一个 JSON 对象。")
        unknown = [k for k in loaded if k not in CONTEXT_FIELDS]
        if unknown:
            die(f"context 里有未知字段：{', '.join(unknown)}",
                allowed={k: v for k, v in CONTEXT_FIELDS.items()})
        context.update({k: str(v).strip() for k, v in loaded.items() if str(v).strip()})

    for key in CONTEXT_FIELDS:
        value = getattr(args, key, None)
        if value and value.strip():
            context[key] = value.strip()
    return context


def do_create(args):
    if not args.yes:
        die("技术路线分析是付费任务，确认要跑请加 --yes。",
            hint="跑之前先跟用户确认技术主题：只写技术名称，例如「钠离子电池正极材料」。")

    subject = args.subject.strip()
    materials = read_text(args.materials, args.materials_file, "素材") or f"技术主题：{subject}"
    objective = (args.objective or "").strip() or "生成技术路线分析正式报告"
    context = build_context(args)

    body = {
        "report_type": REPORT_TYPE,
        "input": {
            "subject": subject,
            "materials": materials,
            "objective": objective,
            "target_markets": [x.strip() for x in args.markets.split(",") if x.strip()] if args.markets else [],
            "competitors": [x.strip() for x in args.competitors.split(",") if x.strip()] if args.competitors else [],
        },
    }
    if context:
        body["input"]["roadmap_context"] = context

    key = args.idempotency_key or fingerprint(body)
    created = unwrap(request("/api/v1/reports", method="POST", body=body,
                             headers={"Idempotency-Key": key}))

    operation = created.get("operation_id")
    if not operation:
        return {"created": created, "_warning": "响应里没有 operation_id，原样返回。"}

    result = {
        "operation_id": operation,
        "report_id": created.get("report_id"),
        "title": created.get("title"),
        "status": created.get("status"),
        "price_yuan": created.get("price_yuan"),
        "simulated": created.get("simulated"),
        "context_filled": sorted(context.keys()),
        "idempotency_key": key,
    }
    if not args.wait:
        result["_next"] = f"轮询：python {os.path.basename(__file__)} status --operation-id {operation}"
        return result
    return {**result, **poll(operation, args.timeout, args.quiet)}


def poll(operation, timeout, quiet=False):
    started = time.time()
    interval = 10
    last_stage = None

    while time.time() - started < timeout:
        data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(operation)}"))
        status = (data.get("status") or "").lower()
        stage = data.get("stage")

        if not quiet and stage and stage != last_stage:
            print(f"  [{data.get('progress', 0)}%] {stage}", file=sys.stderr)
            last_stage = stage

        if status in ("succeeded", "success", "completed", "done"):
            report_id = data.get("report_id")
            out = {
                "status": status,
                "report_id": report_id,
                "quality_status": data.get("quality_status"),
                "quality_hint": QUALITY_HINT.get(data.get("quality_status"), ""),
                "quality_details": data.get("quality_details"),
                "amount_charged_yuan": data.get("amount_charged_yuan"),
                "links": data.get("links"),
            }
            if report_id:
                out["result"] = unwrap(request(f"/api/v1/reports/{urllib.parse.quote(report_id)}"))
                out["_docx"] = f"python {os.path.basename(__file__)} download --report-id {report_id}"
            return out

        if status in ("failed", "error", "cancelled", "canceled"):
            return {"status": status, "error": data.get("error"), "detail": data}

        time.sleep(interval)
        interval = min(interval * 1.4, 60)

    return {
        "status": "timeout",
        "message": f"等了 {timeout} 秒还没完成。任务仍在服务端运行，不要重新提交。",
        "_next": f"python {os.path.basename(__file__)} status --operation-id {operation}",
    }


def do_status(args):
    data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(args.operation_id)}"))
    status = (data.get("status") or "").lower()
    out = {
        "operation_id": args.operation_id,
        "report_id": data.get("report_id"),
        "status": status,
        "progress": data.get("progress"),
        "stage": data.get("stage"),
        "quality_status": data.get("quality_status"),
        "quality_hint": QUALITY_HINT.get(data.get("quality_status"), ""),
        "amount_charged_yuan": data.get("amount_charged_yuan"),
        "links": data.get("links"),
    }
    if status in ("succeeded", "success", "completed", "done") and data.get("report_id"):
        out["result"] = unwrap(request(f"/api/v1/reports/{urllib.parse.quote(data['report_id'])}"))
    return out


def do_download(args):
    payload = request(f"/api/v1/reports/{urllib.parse.quote(args.report_id)}/files/report.docx", raw=True)
    with open(args.out, "wb") as handle:
        handle.write(payload)
    return {"saved": args.out, "bytes": len(payload)}


def do_cancel(args):
    data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(args.operation_id)}/cancel", method="POST"))
    return {"operation_id": args.operation_id, "status": data.get("status"), "detail": data}


def do_fields(args):
    """把 roadmap_context 的十个字段打出来，方便照着填。"""
    return {"roadmap_context_fields": CONTEXT_FIELDS,
            "_note": "写进一个 JSON 文件用 --context-file 传，或用同名命令行参数逐个给。全部可选，但填得越全建议越贴合实际。"}


def main():
    parser = argparse.ArgumentParser(description="PatentMax 技术路线分析与专利布局建议")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("create", help="创建技术路线分析任务")
    p.add_argument("--subject", required=True, help="【必填】技术主题，只写技术名称，3-255 字。例：钠离子电池正极材料")
    p.add_argument("--materials", default=None, help="可选：技术方案与背景")
    p.add_argument("--materials-file", dest="materials_file", default=None, help="可选：素材文件路径（UTF-8）")
    p.add_argument("--objective", default=None, help="可选：这份报告要支持什么决策")
    p.add_argument("--markets", default=None, help="可选：目标市场，逗号分隔。例：CN,US,EP")
    p.add_argument("--competitors", default=None, help="可选：对标企业，逗号分隔，用全称")
    p.add_argument("--context-file", dest="context_file", default=None, help="可选：业务约束 JSON 文件，字段见 fields 子命令")
    for key, desc in CONTEXT_FIELDS.items():
        p.add_argument(f"--{key.replace('_', '-')}", dest=key, default=None, help=desc)
    p.add_argument("--idempotency-key", dest="idempotency_key", default=None, help="幂等键，默认按请求内容自动生成")
    p.add_argument("--wait", action="store_true", help="等到出结果")
    p.add_argument("--timeout", type=int, default=5400, help="等待上限（秒），默认 90 分钟")
    p.add_argument("--quiet", action="store_true", help="不打印进度")
    p.add_argument("--force", action="store_true", help=argparse.SUPPRESS)  # 旧版素材/约束拦截已取消，保留以兼容
    p.add_argument("--yes", action="store_true", help="确认扣费")
    p.set_defaults(func=do_create)

    p = sub.add_parser("fields", help="列出业务约束的十个字段")
    p.set_defaults(func=do_fields)

    p = sub.add_parser("status", help="查询任务状态")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_status)

    p = sub.add_parser("download", help="下载 DOCX 报告")
    p.add_argument("--report-id", dest="report_id", required=True)
    p.add_argument("--out", default="技术路线分析报告.docx")
    p.set_defaults(func=do_download)

    p = sub.add_parser("cancel", help="取消任务")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_cancel)

    args = parser.parse_args()
    print(json.dumps(args.func(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
