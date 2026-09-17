#!/usr/bin/env python3
"""PatentMax 专利查新客户端。

给 AI 用的命令行工具，每个子命令往 stdout 吐一份 JSON，出错时 JSON 里带
error 和中文提示，不抛栈。

走 POST /api/v1/reports 的 report_type=novelty。老的 /api/v1/novelty/tasks
仍然可用且共用同一个余额，但新接入官方建议走统一报告接口，所以这里用后者。

三件事在这里处理掉：

1. **Idempotency-Key 必填**。默认按请求内容算稳定指纹——同样的技术方案重试
   不会重复建任务、重复扣费。查新是这四个任务里最容易被手滑重复提交的，
   因为等待时间长、用户容易以为没跑起来。

2. **技术方案长度护栏**。这个任务的结果质量几乎完全由 technical_solution 决定，
   一句"一种新型电池"查不出任何有用的东西，却照样扣费。

3. **轮询退避**。间隔从 10 秒退到 60 秒。超时不代表失败，任务还在服务端跑。

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
REPORT_TYPE = "novelty"

PURPOSES = {
    "novelty": "新颖性——判断是否已被公开",
    "inventiveness": "创造性——比新颖性更严，看是否显而易见",
    "pre_filing": "申请前查新——马上要递交申请",
    "project_screening": "立项筛查——看方向有没有被占",
    "competitor_scan": "竞品扫描——看对手做到哪一步",
}

DEPTHS = {
    "quick": "快速——摸底用，不构成正式结论",
    "standard": "标准——默认，适合多数场景",
    "deep": "深度——正式申请决策用，最全但最慢",
}

QUALITY_HINT = {
    "qualified": "报告通过质量校验，可作为查新依据。",
    "qualified_degraded": "报告已生成但存在数据短板，结论要保守使用，交付时须说明限制。",
    "review_required": "报告需要人工复核，不要直接当作查新结论交付。",
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
            400: "参数不正确。technical_solution 必填；purpose / depth / legal_status 只接受枚举值。",
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
    return "pmn-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def read_solution(args):
    if args.solution_file:
        try:
            with open(args.solution_file, "r", encoding="utf-8") as handle:
                text = handle.read().strip()
        except OSError as exc:
            die(f"读不到技术方案文件：{exc}")
        if not text:
            die(f"技术方案文件是空的：{args.solution_file}")
        return text
    if args.solution:
        return args.solution.strip()
    die("必须提供技术方案：用 --solution 给文本，或 --solution-file 指定文件。",
        hint="方案描述的质量直接决定查新结果。见 references/solution-guide.md。")


def do_create(args):
    if not args.yes:
        die("专利查新是付费任务，确认要跑请加 --yes。",
            hint="跑之前先确认技术方案写够细——描述太笼统等于白花钱。"
                 "只是想看看有没有类似的，用检索加相似专利就够了，便宜得多。")

    solution = read_solution(args)
    if len(solution) < 80 and not args.force:
        die(f"技术方案只有 {len(solution)} 字，太短了，查出来不会有参考价值。",
            hint="至少讲清三件事：解决什么问题、用什么手段（具体的结构/材料/步骤/参数）、"
                 "达到什么效果。见 references/solution-guide.md。确实只有这些就加 --force。")

    body = {
        "report_type": REPORT_TYPE,
        "input": {
            "technical_solution": solution,
            "purpose": args.purpose,
            "depth": args.depth,
            "regions": [x.strip() for x in args.regions.split(",") if x.strip()],
            "legal_status": args.legal_status,
            "source_scope": {
                "patents": True,
                "papers": not args.patents_only,
                "web": not args.patents_only,
            },
        },
    }
    if args.title:
        body["input"]["title"] = args.title
    if args.date_range:
        body["input"]["date_range"] = {"type": args.date_range}

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
        "purpose": args.purpose,
        "depth": args.depth,
        "price_yuan": created.get("price_yuan"),
        "simulated": created.get("simulated"),
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


def do_options(args):
    return {"purpose": PURPOSES, "depth": DEPTHS,
            "legal_status": {"all": "全部", "active": "有效", "pending": "审中", "inactive": "失效"},
            "regions": "global 或 CN,US,EP,JP,KR,WO 逗号分隔",
            "_note": "正式申请决策用 depth=standard 或 deep；立项摸底可以用 quick。"}


def main():
    parser = argparse.ArgumentParser(description="PatentMax 专利查新")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("create", help="创建查新任务")
    p.add_argument("--solution", default=None, help="技术方案描述：解决什么问题、用什么手段、达到什么效果")
    p.add_argument("--solution-file", dest="solution_file", default=None, help="技术方案文件路径（UTF-8）")
    p.add_argument("--title", default=None, help="方案名称，可选")
    p.add_argument("--purpose", default="novelty", choices=list(PURPOSES), help="查新目的，见 options 子命令")
    p.add_argument("--depth", default="standard", choices=list(DEPTHS), help="检索深度")
    p.add_argument("--regions", default="global", help="地域：global，或 CN,US,EP,JP,KR,WO 逗号分隔")
    p.add_argument("--legal-status", dest="legal_status", default="all",
                   choices=["all", "active", "pending", "inactive"], help="法律状态筛选")
    p.add_argument("--date-range", dest="date_range", default=None, help="日期范围类型，留空为全部")
    p.add_argument("--patents-only", action="store_true",
                   help="只查专利，不查论文和网页。一般别加——论文和公开产品资料同样能破坏新颖性")
    p.add_argument("--idempotency-key", dest="idempotency_key", default=None, help="幂等键，默认按请求内容自动生成")
    p.add_argument("--wait", action="store_true", help="等到出结果")
    p.add_argument("--timeout", type=int, default=5400, help="等待上限（秒），默认 90 分钟")
    p.add_argument("--quiet", action="store_true", help="不打印进度")
    p.add_argument("--force", action="store_true", help="方案过短时强制执行")
    p.add_argument("--yes", action="store_true", help="确认扣费")
    p.set_defaults(func=do_create)

    p = sub.add_parser("options", help="列出 purpose / depth 等可选值")
    p.set_defaults(func=do_options)

    p = sub.add_parser("status", help="查询任务状态")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_status)

    p = sub.add_parser("download", help="下载 DOCX 报告")
    p.add_argument("--report-id", dest="report_id", required=True)
    p.add_argument("--out", default="专利查新报告.docx")
    p.set_defaults(func=do_download)

    p = sub.add_parser("cancel", help="取消任务")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_cancel)

    args = parser.parse_args()
    print(json.dumps(args.func(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
