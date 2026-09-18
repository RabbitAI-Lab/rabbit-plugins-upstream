#!/usr/bin/env python3
"""PatentMax 企业情报分析客户端。

给 AI 用的命令行工具，每个子命令往 stdout 吐一份 JSON，出错时 JSON 里带
error 和中文提示，不抛栈。

这条链是异步的：create 拿 operation_id → 轮询 status → 完成后 result / docx。
几件事在这里处理掉：

1. **Idempotency-Key 是必填的**。没带的话服务端直接拒。网络重试时带同一个 key
   不会重复建任务、重复扣费，所以这里默认按请求内容算一个稳定指纹，
   同样的输入重试天然幂等。

2. **轮询退避**。这类报告要跑几十分钟，密集轮询没意义也没礼貌，
   间隔从 10 秒退到 60 秒。超时不代表失败，任务还在服务端跑。

3. **报告质量分档**。返回里的 quality_status 有三档，qualified_degraded 和
   review_required 意味着素材或数据有短板，不能当成完整结论直接交付，
   这里会把它翻译成给人看的提示。

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
REPORT_TYPE = "patent_intelligence"

QUALITY_HINT = {
    "qualified": "报告通过质量校验，可作为分析依据。",
    "qualified_degraded": "报告已生成但存在数据短板（来源覆盖不足或部分维度缺失），结论要保守使用，交付时须说明限制。",
    "review_required": "报告需要人工复核，不要直接当作结论交付给决策层。",
}


def die(message, **extra):
    payload = {"error": True, "message": message}
    payload.update(extra)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    sys.exit(1)


def request(path, method="GET", body=None, headers=None, raw=False):
    if not API_KEY:
        die("未设置 API 密钥。请先 export PATENTMAX_API_KEY=pm_live_xxx，"
            "密钥在 https://api.ip930.com/features/api-platform 创建。")

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
        hint = {
            400: "参数不正确。subject 至少 3 字，materials 至少 5 字，objective 至少 3 字。",
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
    """服务端统一用 {success, data} 信封包一层。"""
    if isinstance(payload, dict) and "data" in payload:
        return payload["data"]
    return payload


def fingerprint(body):
    """按请求内容算幂等键：同样的输入重试不会重复建任务、重复扣费。"""
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
    return "pmc-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def read_materials(args):
    """素材可以直接给文本，也可以给文件路径——竞品资料通常很长，命令行塞不下。"""
    if args.materials_file:
        try:
            with open(args.materials_file, "r", encoding="utf-8") as handle:
                text = handle.read().strip()
        except OSError as exc:
            die(f"读不到素材文件：{exc}")
        if not text:
            die(f"素材文件是空的：{args.materials_file}")
        return text
    if args.materials:
        return args.materials.strip()
    die("必须提供素材：用 --materials 直接给文本，或用 --materials-file 指定文件路径。",
        hint="素材质量直接决定报告质量。见 references/materials-guide.md。")


def do_create(args):
    if not args.yes:
        die("企业情报分析是付费任务，确认要跑请加 --yes。",
            hint="跑之前先确认素材写够细——素材太笼统等于白花钱。见 references/materials-guide.md。")

    materials = read_materials(args)
    if len(materials) < 200 and not args.force:
        die(f"素材只有 {len(materials)} 字，太短了，跑出来多半是泛泛而谈。",
            hint="至少补齐：这家企业做什么、你关心哪个技术方向、已知的竞争格局。"
                 "确实只有这些信息就加 --force 强制执行。")

    body = {
        "report_type": REPORT_TYPE,
        "input": {
            "subject": args.subject,
            "materials": materials,
            "objective": args.objective,
            "target_markets": [x.strip() for x in args.markets.split(",") if x.strip()] if args.markets else [],
            "competitors": [x.strip() for x in args.competitors.split(",") if x.strip()] if args.competitors else [],
            "source_types": [x.strip() for x in args.sources.split(",") if x.strip()],
            "time_range": args.time_range,
        },
    }
    if args.excluded:
        body["input"]["excluded_directions"] = args.excluded

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
        "idempotency_key": key,
    }
    if not args.wait:
        result["_next"] = f"轮询：python {os.path.basename(__file__)} status --operation-id {operation}"
        return result
    return {**result, **poll(operation, args.timeout, args.quiet)}


def poll(operation, timeout, quiet=False):
    """退避轮询。这类报告要跑几十分钟，10 秒起步退到 60 秒。"""
    started = time.time()
    interval = 10
    last_stage = None

    while time.time() - started < timeout:
        data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(operation)}"))
        status = (data.get("status") or "").lower()
        stage = data.get("stage")

        # 阶段变了就报一声，让人知道没卡死；走 stderr 不污染 stdout 的 JSON
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


def main():
    parser = argparse.ArgumentParser(description="PatentMax 企业情报分析（企业技术专利竞争分析）")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("create", help="创建企业情报分析任务")
    p.add_argument("--subject", required=True, help="分析主题，3-255 字。例：宁德时代在钠离子电池方向的专利布局")
    p.add_argument("--materials", default=None, help="素材文本。企业背景、技术方向、已知竞争格局等")
    p.add_argument("--materials-file", dest="materials_file", default=None, help="素材文件路径（UTF-8），适合长素材")
    p.add_argument("--objective", required=True, help="分析目标，3-2000 字。这份报告要支持什么决策")
    p.add_argument("--markets", default=None, help="目标市场，逗号分隔。例：CN,US,EP")
    p.add_argument("--competitors", default=None, help="竞争对手，逗号分隔，用工商全称")
    p.add_argument("--sources", default="patent,paper,web,news",
                   help="信息来源，逗号分隔，可选 patent,paper,web,news,standard,litigation")
    p.add_argument("--time-range", dest="time_range", default="all", help="时间范围，如 all、近三年、2020-2025")
    p.add_argument("--excluded", default=None, help="排除方向，不想让报告覆盖的领域")
    p.add_argument("--idempotency-key", dest="idempotency_key", default=None, help="幂等键，默认按请求内容自动生成")
    p.add_argument("--wait", action="store_true", help="等到出结果")
    p.add_argument("--timeout", type=int, default=5400, help="等待上限（秒），默认 90 分钟")
    p.add_argument("--quiet", action="store_true", help="不打印进度")
    p.add_argument("--force", action="store_true", help="素材过短时强制执行")
    p.add_argument("--yes", action="store_true", help="确认扣费")
    p.set_defaults(func=do_create)

    p = sub.add_parser("status", help="查询任务状态")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_status)

    p = sub.add_parser("download", help="下载 DOCX 报告")
    p.add_argument("--report-id", dest="report_id", required=True)
    p.add_argument("--out", default="企业情报分析报告.docx")
    p.set_defaults(func=do_download)

    p = sub.add_parser("cancel", help="取消任务")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_cancel)

    args = parser.parse_args()
    print(json.dumps(args.func(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
