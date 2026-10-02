#!/usr/bin/env python3
"""PatentMax 技术交底书客户端。

给 AI 用的命令行工具，每个子命令往 stdout 吐一份 JSON，出错时 JSON 里带
error 和中文提示，不抛栈。

走 POST /api/v1/reports 的两种报告：

    idea_upgrade          只有一个想法时，先出几个可申请的升级方向
    technical_disclosure  材料够了，直接出交底书 Word（外加一份核对说明）

四件事在这里处理掉：

1. **Idempotency-Key 必填**。默认按请求内容算稳定指纹——同样的材料重试
   不会重复建任务、重复扣费。

2. **材料护栏**。交底书在服务端是无人值守跑的：材料缺什么，流水线就按推荐值
   自己补。材料越薄，要推断的越多，交底书里需要人确认的条目就越多。
   太短的材料直接拦下来，别花钱买一份全是推断的交底书。

3. **多文件拼装**。--file 可以给多次，.md / .txt 直接读，.docx 用标准库解压取正文，
   拼成一段带出处标记的纯文本交给服务端。

4. **方向接力**。--from-ideas 直接取上一步创新升级的某个方向当材料，
   不用手动复制。

依赖：只用标准库，不需要 pip install。
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_URL = os.environ.get("PATENTMAX_BASE_URL", "https://api.ip930.com").rstrip("/")
API_KEY = os.environ.get("PATENTMAX_API_KEY", "").strip()
TIMEOUT = 60

MAX_CHARS = 100_000
# 交底书低于这个长度，服务端会发起提问，而 API 模式下没人回答，全部按推荐值继续
RICH_CHARS = 800
MIN_DISCLOSURE_CHARS = 200
MIN_IDEA_CHARS = 40

QUALITY_HINT = {
    "qualified": "已生成并通过校验。",
    "qualified_degraded": "已生成但存在短板，交付时须说明限制。",
    "review_required": "需要人工复核，不要直接交付。",
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
            400: "参数不正确。材料至少 20 字、不超过 10 万字；方向数只能是 1-5。",
            401: "密钥无效或已撤销。",
            402: "余额不足，到 https://api.ip930.com/features/api-platform 充值。",
            403: "该密钥没有此接口的权限。",
            404: "任务或文件不存在。确认 id 抄全了；创新升级没有 Word，结果用 status 取。",
            409: "任务还没跑完就来取结果，或同一个 Idempotency-Key 正在处理中。",
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
    return "pmd-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


# ─────────────────────────── 材料 ───────────────────────────

def read_docx(path):
    """标准库取 .docx 正文：它就是个 zip，正文在 word/document.xml。

    表格按行拼成「单元格 | 单元格」，段落之间空行。图片、公式取不到，
    这一点要在 SKILL.md 里交代：附图内容得用文字补。
    """
    try:
        with zipfile.ZipFile(path) as archive:
            xml = archive.read("word/document.xml").decode("utf-8", "replace")
    except (zipfile.BadZipFile, KeyError, OSError) as exc:
        die(f"读不了这个 Word 文件：{path}（{exc}）。只支持 .docx，老的 .doc 请先另存为 .docx。")
    xml = re.sub(r"</w:tc>", " | ", xml)
    xml = re.sub(r"</w:p>|</w:tr>", "\n", xml)
    xml = re.sub(r"<w:tab/>", "\t", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    for entity, char in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'"), ("&amp;", "&")):
        text = text.replace(entity, char)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def read_file(path):
    if not os.path.isfile(path):
        die(f"找不到文件：{path}")
    if path.lower().endswith(".docx"):
        return read_docx(path)
    if path.lower().endswith((".pdf", ".doc", ".ppt", ".pptx", ".xls", ".xlsx")):
        die(f"不支持直接读 {os.path.splitext(path)[1]}：{path}",
            hint="先把正文转成 .md / .txt / .docx，或者由你读完后把要点写进 --supplement。")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except UnicodeDecodeError:
        die(f"{path} 不是 UTF-8 文本。只支持 .md / .txt / .docx。")


def collect_materials(files, text):
    """把多份材料拼成一段。每份前面标出处，服务端检查材料冲突时要靠它指认来源。"""
    parts = []
    for path in files or []:
        body = read_file(path)
        if body:
            parts.append(f"【材料：{os.path.basename(path)}】\n{body}")
    if text and text.strip():
        parts.append(f"【补充说明】\n{text.strip()}" if parts else text.strip())
    return "\n\n".join(parts)


def direction_to_material(direction, idea_text=None):
    """把创新升级的一个方向转成交底书材料。字段为空就跳过，不写「无」占位。"""
    lines = []
    if idea_text:
        lines.append(f"【原始想法】\n{idea_text.strip()}")
    head = direction.get("title") or direction.get("direction_label") or "选定方向"
    lines.append(f"【选定方向】{head}")
    for key, label in (
        ("plain_summary", "方向概述"),
        ("technical_field", "技术领域"),
        ("background", "背景技术"),
        ("triz_contradiction", "要解决的技术矛盾"),
        ("core_idea", "核心技术方案"),
        ("existing_tech_description", "与现有技术的关系"),
    ):
        value = direction.get(key)
        if value:
            lines.append(f"【{label}】\n{value}")
    points = [p for p in direction.get("innovation_points") or [] if p]
    if points:
        lines.append("【创新点】\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(points, 1)))
    return "\n\n".join(lines)


# ─────────────────────────── 轮询 ───────────────────────────

def fetch_result(report_id):
    return unwrap(request(f"/api/v1/reports/{urllib.parse.quote(report_id)}"))


def poll(operation, timeout, quiet=False):
    started = time.time()
    interval = 10
    last = None

    while time.time() - started < timeout:
        data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(operation)}"))
        status = (data.get("status") or "").lower()
        marker = (data.get("progress"), data.get("stage"))
        if not quiet and marker != last:
            waited = int(time.time() - started)
            print(f"  [{data.get('progress', 0)}%] {data.get('stage') or status}（已等 {waited} 秒）", file=sys.stderr)
            last = marker

        if status == "succeeded":
            return finished(data)
        if status in ("failed", "cancelled"):
            return {"status": status, "error": data.get("error"),
                    "_note": "失败和取消都会全额退回预扣的钱。"}

        time.sleep(interval)
        interval = min(interval * 1.4, 60)

    return {
        "status": "timeout",
        "message": f"等了 {timeout} 秒还没完成。任务仍在服务端运行，不要重新提交。",
        "_next": f"python {os.path.basename(__file__)} status --operation-id {operation}",
    }


def finished(data):
    report_id = data.get("report_id")
    out = {
        "status": "succeeded",
        "report_type": data.get("report_type"),
        "report_id": report_id,
        "quality_status": data.get("quality_status"),
        "quality_hint": QUALITY_HINT.get(data.get("quality_status"), ""),
        "amount_charged_yuan": data.get("amount_charged_yuan"),
    }
    if report_id:
        out["result"] = (fetch_result(report_id) or {}).get("result")
    me = os.path.basename(__file__)
    if data.get("report_type") == "idea_upgrade":
        out["_next"] = (f"挑一个方向写交底书：python {me} create --from-ideas {report_id} "
                        "--direction <序号> --yes")
    else:
        out["_next"] = [
            f"python {me} download --report-id {report_id} --out 技术交底书.docx",
            f"python {me} download --report-id {report_id} --kind notes --out 核对说明.docx",
        ]
    return out


# ─────────────────────────── 子命令 ───────────────────────────

def submit(body, args):
    key = args.idempotency_key or fingerprint(body)
    created = unwrap(request("/api/v1/reports", method="POST", body=body,
                             headers={"Idempotency-Key": key}))
    operation = created.get("operation_id")
    if not operation:
        return {"created": created, "_warning": "响应里没有 operation_id，原样返回。"}

    result = {
        "operation_id": operation,
        "report_id": created.get("report_id"),
        "report_type": body["report_type"],
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


def do_ideas(args):
    if not args.yes:
        die("创新升级是付费任务，确认要跑请加 --yes。",
            hint="只有一个想法、还没想清楚往哪个方向写时才用它；方案已经定了就直接 create。")
    idea = collect_materials(args.file, args.idea)
    if not idea:
        die("必须提供想法：--idea 给文本，或 --file 给文件。")
    if len(idea) < MIN_IDEA_CHARS and not args.force:
        die(f"想法只有 {len(idea)} 字，太短了。",
            hint="至少说清：想解决什么问题、现在打算怎么做。确实只有这些就加 --force。")
    if len(idea) > MAX_CHARS:
        die(f"材料 {len(idea)} 字，超过上限 {MAX_CHARS}。删掉与方案无关的部分再试。")

    body = {"report_type": "idea_upgrade",
            "input": {"idea_text": idea, "direction_count": args.count}}
    if args.title:
        body["input"]["title_hint"] = args.title
    return submit(body, args)


def do_create(args):
    if not args.yes:
        die("技术交底书是付费任务，确认要跑请加 --yes。",
            hint="跑之前先确认材料够全：问题、方案、实施细节、效果。"
                 "材料越全，交底书里要人确认的推断就越少。")

    if args.from_ideas:
        report = fetch_result(args.from_ideas)
        directions = ((report or {}).get("result") or {}).get("directions") or []
        if not directions:
            die(f"报告 {args.from_ideas} 里没有方向清单。确认它是创新升级的 report_id，且已经跑完。")
        if args.direction is None:
            die("用 --from-ideas 时必须用 --direction 指定选第几个方向。",
                directions=[{"direction": d.get("direction_index"), "title": d.get("title"),
                             "overall": (d.get("scores") or {}).get("overall")} for d in directions])
        picked = next((d for d in directions if d.get("direction_index") == args.direction), None)
        if not picked:
            die(f"没有第 {args.direction} 个方向。可选：" +
                "、".join(str(d.get("direction_index")) for d in directions))
        extra = collect_materials(args.file, args.supplement)
        supplement = direction_to_material(picked, args.idea)
        if extra:
            supplement += "\n\n" + extra
        title = args.title or picked.get("title")
    else:
        supplement = collect_materials(args.file, args.supplement)
        title = args.title
        if not supplement:
            die("必须提供材料：--supplement 给文本，--file 给文件（可多次），"
                "或 --from-ideas 接上一步的方向。")

    length = len(supplement)
    if length < MIN_DISCLOSURE_CHARS and not args.force:
        die(f"材料只有 {length} 字，写出来的交底书会几乎全是推断。",
            hint="至少讲清：解决什么问题、具体怎么做（结构/步骤/参数）、达到什么效果。"
                 "只有一个模糊想法的话，先用 ideas 子命令出方向。确实只有这些就加 --force。")
    if length > MAX_CHARS:
        die(f"材料 {length} 字，超过上限 {MAX_CHARS}。删掉与方案无关的部分再试。")

    body = {"report_type": "technical_disclosure", "input": {"supplement": supplement}}
    if title:
        body["input"]["title_hint"] = title[:255]
    result = submit(body, args)
    result["material_chars"] = length
    if length < RICH_CHARS:
        result["_warning"] = (f"材料 {length} 字，偏薄。缺的信息会按推荐值自动补，"
                              "交付前务必让用户看核对说明里的待确认条目。")
    return result


def do_status(args):
    data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(args.operation_id)}"))
    status = (data.get("status") or "").lower()
    if status == "succeeded":
        return {"operation_id": args.operation_id, **finished(data)}
    return {
        "operation_id": args.operation_id,
        "report_id": data.get("report_id"),
        "report_type": data.get("report_type"),
        "status": status,
        "progress": data.get("progress"),
        "stage": data.get("stage"),
        "error": data.get("error"),
    }


def do_download(args):
    path = f"/api/v1/reports/{urllib.parse.quote(args.report_id)}/files/report.docx"
    if args.kind == "notes":
        path += "?kind=notes"
    out = args.out or ("核对说明.docx" if args.kind == "notes" else "技术交底书.docx")
    payload = request(path, raw=True)
    with open(out, "wb") as handle:
        handle.write(payload)
    return {"saved": out, "bytes": len(payload), "kind": args.kind}


def do_cancel(args):
    data = unwrap(request(f"/api/v1/operations/{urllib.parse.quote(args.operation_id)}/cancel",
                          method="POST"))
    return {"operation_id": args.operation_id, "status": data.get("status"),
            "_note": "取消后预扣的钱全额退回。"}


def do_preview(args):
    """不花钱：看看拼好的材料长什么样、多少字，确认无误再 create。"""
    text = collect_materials(args.file, args.supplement)
    if not text:
        die("没有材料可预览。")
    return {"chars": len(text),
            "level": "充分" if len(text) >= RICH_CHARS else ("偏薄" if len(text) >= MIN_DISCLOSURE_CHARS else "太短"),
            "head": text[:1500],
            "tail": text[-500:] if len(text) > 2000 else None}


def main():
    parser = argparse.ArgumentParser(description="PatentMax 技术交底书")
    sub = parser.add_subparsers(dest="command", required=True)

    def common(p):
        p.add_argument("--title", default=None, help="案件名称，可选")
        p.add_argument("--file", action="append", default=[], help="材料文件，可多次：.md / .txt / .docx")
        p.add_argument("--idempotency-key", dest="idempotency_key", default=None,
                       help="幂等键，默认按请求内容自动生成")
        p.add_argument("--wait", action="store_true", help="等到出结果")
        p.add_argument("--timeout", type=int, default=5400, help="等待上限（秒），默认 90 分钟")
        p.add_argument("--quiet", action="store_true", help="不打印进度")
        p.add_argument("--force", action="store_true", help="材料过短时强制执行")
        p.add_argument("--yes", action="store_true", help="确认扣费")

    p = sub.add_parser("ideas", help="创新升级：一个想法 → 几个可申请的方向")
    p.add_argument("--idea", default=None, help="想法描述")
    p.add_argument("--count", type=int, default=3, choices=range(1, 6), metavar="1-5",
                   help="要几个方向，默认 3")
    common(p)
    p.set_defaults(func=do_ideas)

    p = sub.add_parser("create", help="生成技术交底书")
    p.add_argument("--supplement", default=None, help="材料正文或补充说明")
    p.add_argument("--from-ideas", dest="from_ideas", default=None, help="创新升级的 report_id")
    p.add_argument("--direction", type=int, default=None, help="选第几个方向（配合 --from-ideas）")
    p.add_argument("--idea", default=None, help="配合 --from-ideas：把原始想法也带上")
    common(p)
    p.set_defaults(func=do_create)

    p = sub.add_parser("preview", help="不花钱：预览拼好的材料和字数")
    p.add_argument("--supplement", default=None)
    p.add_argument("--file", action="append", default=[])
    p.set_defaults(func=do_preview)

    p = sub.add_parser("status", help="查询任务状态，完成后带结果")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_status)

    p = sub.add_parser("download", help="下载 Word")
    p.add_argument("--report-id", dest="report_id", required=True)
    p.add_argument("--kind", default="disclosure", choices=["disclosure", "notes"],
                   help="disclosure = 交底书正文；notes = 核对说明")
    p.add_argument("--out", default=None)
    p.set_defaults(func=do_download)

    p = sub.add_parser("cancel", help="取消任务")
    p.add_argument("--operation-id", dest="operation_id", required=True)
    p.set_defaults(func=do_cancel)

    args = parser.parse_args()
    print(json.dumps(args.func(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
