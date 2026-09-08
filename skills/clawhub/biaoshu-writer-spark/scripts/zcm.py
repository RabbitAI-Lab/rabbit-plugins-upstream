#!/usr/bin/env python3
"""百炼®标书开放 API 轻客户端（thin client）。

封装「提交 → 轮询 → 取结果」异步模型，零第三方依赖（仅标准库）。
凭证通过本地凭证文件 config.json 传入；可选环境变量仅覆盖本地输出路径：
  ZCM_OUTPUT_DIR  成品标书 .docx 存放目录；未设时默认 skill 同级的 biaoshu-bailian-files/

Api Key 只从 skill 内 config.json 读取。
凭证文件权限 600。config.json 含真实 Key，**勿上传发布包**（发布包不含配置文件）。
Api Key 仅能在官网自助注册获取（本 skill 不代注册）。
用 login 显式保存凭证、logout 清除。
成品存放目录优先级：generate -o 显式路径 > ZCM_OUTPUT_DIR > 凭证文件的 output_dir > 默认 biaoshu-bailian-files。

子命令：
  login      --app-key ..  保存凭证到 skill 内 config.json（输一次，下次免输）
  logout                   删除已保存的凭证
  me                                查连通性与可用字数
  interpret  <file>                 智能解读招标文件 → 打印完整解读结果（含 8 维度+控标洞察）
  packages   <project_id>           抽取分包 → 打印 packages JSON（供用户挑选）
  generate   <project_id> [opts]    生成成品标书 → 默认输出短时下载链接（-o 时下载 .docx）
  compliance <project_id> <f...>    合规审查投标文件 → 打印完整合规结果
  duplicate  <f...>                 标书查重：2-3 份投标文件雷同/相似风险检查
  report     --job <id> | --in f    把解读/合规/查重结果渲染成 HTML/Word 报告
  knowledge-base [category]         按类别查询知识库（排除历史标书库 / 标书模板库）

interpret / compliance / duplicate 可加 --report html|docx|both 在取结果后直接出报告。
  job        <job_id>               查单个任务状态（不轮询）
  download-url <job_id>             获取成品标书短时下载链接
  result     <job_id> [-o file]     取任务结果 / -o 下载成品
  cancel     <job_id>               取消任务

提交类子命令（interpret/packages/generate/compliance/duplicate）默认自动轮询到终态，
加 --no-wait 只提交并打印 job_id。
Locale scope: zh-CN (Simplified Chinese) by design for mainland-China bidding workflows. User-facing help text, platform menu names, risk labels, and generated report prompts default to Chinese because they mirror procurement terminology used by the underlying platform and report artifacts. Assistants may explain those terms in the user's language when needed, but in-product labels remain zh-CN.
"""
import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

DEFAULT_BASE = "https://biaoshu.zhiliaobiaoxun.com/api/open/v1"

# skill 版本（单一事实来源）。适配的后端 API 版本与契约快照见 references/api.md 顶部。
SKILL_VERSION = "2.2.3"
API_TARGET = "/api/open/v1"
CONTRACT_SNAPSHOT = "2026-08-10"

# 渠道码：单发布包注入；ClawHub 使用 c666。
# 非空时官网链接追加 ?ch=。
CHANNEL = "c666"
SIGNUP_URL = "https://biaoshu.zhiliaobiaoxun.com/" + (f"?ch={CHANNEL}" if CHANNEL else "")

# Locale scope: zh-CN labels are intentional for mainland-China bidding workflows;
# assistants may translate explanations externally, but in-product menu names and prompts remain Chinese.
# 文档第 6 节错误码 → 友好提示
ERROR_HINTS = {
    "missing_credentials": "缺少鉴权头：请在本 skill 目录下的 config.json 写入 app_key（或用 login 保存）。",
    "invalid_credentials": "Api Key 不正确：核对凭证，或到官网 https://biaoshu.zhiliaobiaoxun.com/ 左侧菜单『Skill 接入 → 获取 Api Key』重置 Key（重置后旧 Key 立即失效）。",
    "account_disabled": "凭证或用户已被停用，请联系百炼®标书管理员。",
    "insufficient_points": "可用字数不足：本次不扣费也不产出，请到官网购买会员或字数包后重试。",
    "insufficient_balance": "可用字数不足：请先购买会员或字数包后重试。",
    "not_found": "404：多为开放 API 总开关未开（整层 404），请联系超级管理员在『系统设置』开启；或句柄不存在。",
    "job_not_found": "任务句柄不存在或非本人，请核对 job_id。",
    "project_not_found": "project 不存在或非本人，请核对 project_id（由智能解读产出）。",
    "result_expired": "结果已过期（默认约 7 天 TTL），需重新生成。",
    "invalid_job_state": "任务状态不允许此操作：任务未成功就取结果 / 未解读就生成 / 未抽包就 generate。",
    "validation_error": "入参校验失败：文件缺失或类型不支持 / 缺 package_ids 等。",
    "rate_limited": "触发限流（60 req/min）：稍后退避重试（参考 Retry-After）。",
    "too_many_concurrent_jobs": "并发任务超限（≤3）：等已有任务结束再提交。",
    "internal_error": "服务端异常：稍后重试或反馈百炼®标书。",
}

REGISTER_GUIDE = f"""\
还没配置 Api Key —— 这是用百炼®标书写作助手出解读/标书/合规的唯一开关。
好消息：一个手机号就能开通，手机号注册赠 5 万字，开通后这份文件马上就能出解读。

转述给用户时按顺序完整给出，链接原样显示完整 URL：

  第 1 步 · 注册拿 Key（只需手机号）
    1) 打开官网 {SIGNUP_URL}
    2) 手机号 + 短信验证码注册登录（手机号注册赠 5 万字）
    3) 点左侧菜单『Skill 接入 → 获取 Api Key』，在面板里查看/复制 Api Key（首次打开自动生成，形如 bk_live_xxxxx）

  第 2 步 · 配置凭证（拿到 Key 后做一次，配好下次免输）
    由用户本人在本 skill 目录下创建凭证文件 config.json，写入一行：
      {{"app_key": "bk_live_xxxxx"}}
    （把 bk_live_xxxxx 换成自己的 Key。）

凭证安全：Api Key 是账户的完整凭证，全程由用户本人写入本地文件——
  不要在对话里索取、让用户粘贴或复述 Key。Key 泄露或想作废时，随时到官网
  左侧菜单『Skill 接入 → 获取 Api Key』重置，旧 Key 立即失效。
"""


def die(msg, code=1):
    print(msg, file=sys.stderr, flush=True)
    sys.exit(code)


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def _format_seconds(value):
    try:
        seconds = int(value)
    except (TypeError, ValueError):
        return None
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    remain = seconds % 60
    if minutes < 60:
        return f"{minutes}分{remain}秒" if remain else f"{minutes}分钟"
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}小时{minutes}分钟" if minutes else f"{hours}小时"


def _format_bytes(value):
    try:
        size = int(value)
    except (TypeError, ValueError):
        return "未知大小"
    units = ["B", "KB", "MB", "GB"]
    n = float(size)
    for unit in units:
        if n < 1024 or unit == units[-1]:
            return f"{n:.1f}{unit}" if unit != "B" else f"{int(n)}B"
        n /= 1024
    return f"{size}B"


def format_progress_line(prog, status=None, *, include_job_id=None):
    """把 Open API progress 快照转成 WorkBuddy/Monitor 易读的一行状态。"""
    prog = prog or {}
    status_label = {
        "queued": "排队中",
        "running": "进行中",
        "succeeded": "已完成",
        "failed": "失败",
        "canceled": "已取消",
    }.get(status, status)
    pct = prog.get("percent")
    label = prog.get("stage_label") or prog.get("stage") or "处理中"
    message = prog.get("message") or ""
    current = prog.get("current_step")
    total = prog.get("total_steps")
    unit = prog.get("unit_label") or "项"
    current_label = prog.get("current_step_label") or ""

    head = f"[{pct if pct is not None else '?'}%] {label}"
    parts = []
    if message and message != label:
        parts.append(str(message))
    if current is not None and total is not None and not message:
        parts.append(f"已完成 {current}/{total} {unit}")
    if current_label:
        parts.append(f"当前：{current_label}")
    elapsed = _format_seconds(prog.get("elapsed_seconds"))
    remaining = _format_seconds(prog.get("estimated_remaining_seconds"))
    if elapsed:
        parts.append(f"已用 {elapsed}")
    if remaining:
        parts.append(f"预计剩余 {remaining}")
    if status_label:
        parts.append(str(status_label))
    body = " · ".join(parts)
    line = f"{head} · {body}" if body else head
    if include_job_id:
        return f"[{include_job_id}] {line}"
    return line


def creds_path():
    """凭证文件：固定为 skill 内 config.json（不可由环境变量重定向）。"""
    return os.path.join(skill_dir(), "config.json")


def load_creds_file():
    """读凭证：仅 skill 内 config.json。"""
    try:
        with open(creds_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except (FileNotFoundError, ValueError, OSError):
        pass
    return {}


def save_creds_file(data):
    """把凭证写入 skill 内 config.json（文件权限 600）。⚠️ 含真实 Key，勿上传发布包。"""
    path = creds_path()
    d = os.path.dirname(path)
    try:
        if d:
            os.makedirs(d, exist_ok=True)
    except OSError:
        pass
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def get_creds():
    """返回 Api Key。只从本地 config.json 读取；未配置时打印官网获取指引并退出（码 2）。"""
    app_key = str(load_creds_file().get("app_key", "")).strip()
    if not app_key:
        die(REGISTER_GUIDE, code=2)
    return app_key


def _site_base():
    """站点根地址（剥掉 /api/... 段），用于拼注册/绑定/充值网页链接。"""
    b = base_url()
    return b.split("/api/", 1)[0].rstrip("/") if "/api/" in b else "https://biaoshu.zhiliaobiaoxun.com"


def _guide_insufficient_balance(err=None):
    """可用字数不足引导：只给不含凭证的官网链接（凭证保护：平台 402 下发的
    recharge_url/bind_url 携带明文 bind_key，一律不转发进对话）。"""
    die(
        "可用字数不足，请用户自行登录官网购买会员或字数包后重试（Api Key 保持不变）：\n"
        f"  入口：{_site_base()}/recharge （用注册手机号登录后操作）\n"
        "（为保护凭证，不要向用户转发任何携带 Api Key / bind_key 参数的链接。）",
        code=1,
    )


def base_url():
    """ClawHub 净化线固定只访问生产开放 API，禁止任何本地覆盖。"""
    return DEFAULT_BASE


def skill_dir():
    """SKILL 包根目录（scripts/ 的上一级）。"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def default_output_dir():
    """未配置时的默认成品目录：skill 包同级的 biaoshu-bailian-files/。"""
    return os.path.join(os.path.dirname(skill_dir()), "biaoshu-bailian-files")


def output_dir():
    """解析成品标书存放目录并确保存在。优先级：env > 凭证文件 > 默认。"""
    d = os.environ.get("ZCM_OUTPUT_DIR", "").strip()
    if not d:
        d = str(load_creds_file().get("output_dir") or "").strip()
    d = os.path.expanduser(d) if d else default_output_dir()
    os.makedirs(d, exist_ok=True)
    return d


def projects_path():
    home = os.environ.get("ZCM_HOME", "").strip() or os.path.join(
        os.path.expanduser("~"), ".zcm")
    return os.path.join(home, "projects.json")


def _load_projects():
    try:
        with open(projects_path(), "r", encoding="utf-8") as f:
            d = json.load(f)
            return d if isinstance(d, dict) else {}
    except (FileNotFoundError, ValueError, OSError):
        return {}


def remember_tender(tender_filename, project_id=None, job_id=None):
    """interpret 时把招标文件名按 project_id / job_id 记到本地，供后续报告自动命名。"""
    if not tender_filename:
        return
    name = os.path.basename(str(tender_filename).rstrip("/"))
    d = _load_projects()
    by_pid = d.setdefault("by_project", {})
    by_job = d.setdefault("by_job", {})
    if project_id is not None:
        by_pid[str(project_id)] = name
    if job_id is not None:
        by_job[str(job_id)] = name
    path = projects_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def recall_tender(project_id=None, job_id=None):
    """按 job_id / project_id 回查本地记下的招标文件名；查不到返回 None。"""
    d = _load_projects()
    if job_id is not None:
        v = d.get("by_job", {}).get(str(job_id))
        if v:
            return v
    if project_id is not None:
        v = d.get("by_project", {}).get(str(project_id))
        if v:
            return v
    return None


def _headers(extra=None):
    h = {"X-App-Key": get_creds()}
    if extra:
        h.update(extra)
    return h


def _handle_http_error(e):
    """把 HTTPError 转成友好提示并退出。"""
    body = b""
    try:
        body = e.read()
    except Exception:
        pass
    code = None
    msg = ""
    err = {}
    try:
        payload = json.loads(body.decode("utf-8"))
        # 兼容嵌套 {"error": {...}} 和平铺 {"code": ...} 两种格式
        err = payload.get("error") or payload
        code = err.get("code")
        msg = err.get("message", "")
    except Exception:
        msg = body.decode("utf-8", "replace")
    # 可用字数不足：走购买引导而非直接报错退出
    if e.code == 402 or code in ("insufficient_balance", "insufficient_points"):
        _guide_insufficient_balance(err)
        return
    hint = ERROR_HINTS.get(code, "")
    retry_after = e.headers.get("Retry-After") if e.headers else None
    lines = [f"请求失败 HTTP {e.code}" + (f" [{code}]" if code else "")]
    if msg:
        lines.append(f"  message: {msg}")
    if hint:
        lines.append(f"  → {hint}")
    if retry_after:
        lines.append(f"  → Retry-After: {retry_after}s")
    die("\n".join(lines), code=1)


def request_json(method, path, *, headers=None, data=None, json_body=None):
    """发起请求并解析 JSON 响应。data 为已编码 bytes（如 multipart）。"""
    url = base_url() + path
    hdrs = _headers(headers)
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as e:
        _handle_http_error(e)
    except urllib.error.URLError as e:
        die(f"网络错误：{e.reason}\n  → 检查网络连通性与开放 API 地址（当前 {base_url()}）。", code=1)


def encode_multipart(fields, files):
    """fields: dict[str,str]; files: list[(field_name, filepath)]。返回 (body_bytes, content_type)。"""
    boundary = "----zcm" + uuid.uuid4().hex
    crlf = b"\r\n"
    buf = bytearray()
    for name, value in (fields or {}).items():
        buf += b"--" + boundary.encode() + crlf
        buf += f'Content-Disposition: form-data; name="{name}"'.encode() + crlf + crlf
        buf += str(value).encode("utf-8") + crlf
    for field_name, filepath in files:
        if not os.path.isfile(filepath):
            die(f"文件不存在：{filepath}")
        fname = os.path.basename(filepath)
        ctype = mimetypes.guess_type(fname)[0] or "application/octet-stream"
        with open(filepath, "rb") as f:
            content = f.read()
        buf += b"--" + boundary.encode() + crlf
        buf += (
            f'Content-Disposition: form-data; name="{field_name}"; filename="{fname}"'
        ).encode("utf-8") + crlf
        buf += f"Content-Type: {ctype}".encode() + crlf + crlf
        buf += content + crlf
    buf += b"--" + boundary.encode() + b"--" + crlf
    return bytes(buf), f"multipart/form-data; boundary={boundary}"


def _reject_remote(s, label):
    """本 skill 只接受本地文件；给了链接就友好拒绝（不做任何远程抓取）。"""
    if s.startswith("http://") or s.startswith("https://"):
        die(f"{label}只支持本地文件路径，不支持云端链接：请先自行把文件下载到本地，再把本地路径提供给助手。")


# 上传大小上限（百炼®标书限制）
MAX_TENDER_MB = 50      # 招标文件
MAX_BID_MB = 1024       # 投标文件
MAX_DUP_TOTAL_MB = 2048 # 查重批次总大小


def _check_size(path, max_mb, label):
    """本地文件大小上限校验，超限直接报错。"""
    try:
        sz = os.path.getsize(path)
    except OSError:
        return
    if sz > max_mb * 1024 * 1024:
        die(f"{label}超过大小上限：{sz / 1024 / 1024:.1f} MB > {max_mb} MB"
            f"（{os.path.basename(path)}）。请压缩或拆分后重试。")


def _check_total_size(paths, max_mb, label):
    """本地批量上传总大小校验；单个文件读不到大小时交给服务端兜底。"""
    total = 0
    for path in paths:
        try:
            total += os.path.getsize(path)
        except OSError:
            return
    if total > max_mb * 1024 * 1024:
        die(f"{label}总大小超过上限：{total / 1024 / 1024:.1f} MB > {max_mb} MB。请压缩或减少文件后重试。")


def poll(job_id, interval=5, timeout=3600):
    """轮询任务到终态。返回最终状态 dict。"""
    deadline = time.time() + timeout
    last = ""
    while True:
        st = request_json("GET", f"/jobs/{job_id}")
        status = st.get("status")
        prog = st.get("progress") or {}
        line = format_progress_line(prog, status=status, include_job_id=job_id)
        if line != last:
            log(line)
            last = line
        if status == "succeeded":
            return st
        if status in ("failed", "canceled"):
            err = st.get("error") or {}
            ecode = err.get("code", "")
            hint = ERROR_HINTS.get(ecode, "")
            extra = ""
            if ecode == "worker_lost":
                extra = "（服务重启导致，需重新提交）"
            die(f"任务 {status}：{ecode} {err.get('message','')} {hint}{extra}".strip(), code=1)
        if time.time() > deadline:
            die(f"轮询超时（>{timeout}s），任务仍未完成。可稍后用 `job {job_id}` 继续查看。", code=1)
        time.sleep(interval)


def idempotency_header(args):
    if getattr(args, "idempotency_key", None):
        return {"Idempotency-Key": args.idempotency_key}
    return {}


# ---------------- 子命令 ----------------

_RISK_ZH = {"high": "高风险", "review": "待复核", "tip": "提示"}
_PRIORITY_ZH = {"high": "高", "medium": "中", "low": "低"}
# 按字段名分别映射英文枚举 → 中文（仅这些键转换，其余原样）
_ENUM_ZH = {"risk_level": _RISK_ZH, "priority": _PRIORITY_ZH}


def zh_risk(obj):
    """递归把 risk_level(high/review/tip)、priority(high/medium/low) 等枚举值转中文（输出展示用）。"""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            m = _ENUM_ZH.get(k)
            if m and isinstance(v, str) and v in m:
                out[k] = m[v]
            else:
                out[k] = zh_risk(v)
        return out
    if isinstance(obj, list):
        return [zh_risk(x) for x in obj]
    return obj


def _platform_reminder():
    """输出平台查看提示，在每次输出结果文件路径时调用。"""
    log("📎 结果同步在百炼®标书平台查看：https://biaoshu.zhiliaobiaoxun.com/")


def _report_balance():
    """任务完成后播报当前可用字数；查询失败静默，绝不影响已完成的任务。"""
    try:
        data = request_json("GET", "/me")
        bal = data.get("available_words", data.get("wallet_balance"))
    except BaseException:
        return
    if bal is not None:
        log(f"💰 当前可用字数：{bal}")


def _maybe_report(result_response, fmt, label, tender_name=None):
    """interpret/compliance/duplicate 取结果后，若指定 --report 则渲染报告到成品目录。

    报告默认名 = 招标文件名_{智能解读|合规审查|标书查重}（tender_name 提供时）。
    """
    if not fmt:
        return
    import report as _report
    d = output_dir()
    try:
        outs = _report.generate(result_response, fmt=fmt, out_dir=d, tender_name=tender_name)
    except Exception as e:  # 渲染失败不应让整条命令崩
        log(f"⚠️ 报告生成失败：{e}")
        return
    for p in outs:
        log(f"已生成{label}报告：{os.path.abspath(p)}")
    log(f"报告所在目录：{os.path.abspath(d)}")
    _platform_reminder()


def cmd_report(args):
    import report as _report
    if args.in_file:
        with open(args.in_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = request_json("GET", f"/jobs/{args.job}/result")
    # 招标文件名：--name > 本地缓存（job_id / 结果里的 project_id|document_id）> 结果自动识别
    tender = args.name
    if not tender:
        res = data.get("result") if isinstance(data, dict) else {}
        res = res if isinstance(res, dict) else {}
        pid = res.get("project_id") or (res.get("compliance") or {}).get("document_id") or res.get("document_id")
        tender = recall_tender(job_id=args.job, project_id=pid)
    out_dir = args.out_dir or output_dir()
    outs = _report.generate(data, service=args.service, fmt=args.format,
                            out_dir=out_dir, basename=args.basename, tender_name=tender)
    for p in outs:
        log(f"已生成报告：{os.path.abspath(p)}")
        print(os.path.abspath(p))
    log(f"报告所在目录：{os.path.abspath(out_dir)}")
    _platform_reminder()


def cmd_login(args):
    stored = load_creds_file()
    if args.app_key:
        stored["app_key"] = args.app_key.strip()
    stored.pop("base", None)
    if args.output_dir:
        stored["output_dir"] = os.path.expanduser(args.output_dir.strip())
    if not stored.get("app_key"):
        die("login 需要 --app-key（Api Key 形如 bk_live_xxxxx）。")
    save_creds_file(stored)
    log(f"凭证已保存到 {creds_path()}（权限 600），下次免输。")
    if stored.get("output_dir"):
        log(f"成品标书默认存放目录：{stored['output_dir']}")


def cmd_logout(args):
    try:
        os.remove(creds_path())
        log(f"已删除凭证文件 {creds_path()}。")
    except FileNotFoundError:
        log("没有已保存的凭证文件。")


def cmd_me(args):
    data = request_json("GET", "/me")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    bal = data.get("available_words", data.get("wallet_balance"))
    if bal is not None:
        log(f"可用字数：{bal}")


def cmd_knowledge_base(args):
    path = "/knowledge-base"
    if getattr(args, "category", None):
        path += f"/{args.category}"
    query = []
    if getattr(args, "category", None):
        query.append(f"page={args.page}")
        query.append(f"page_size={args.page_size}")
    if query:
        path += "?" + "&".join(query)
    data = request_json("GET", path)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def _precheck_balance():
    """提交前门槛（解读/生成/合规/查重）：低于 1 直接走购买引导，不发起任务。

    平台侧同样有 402 闸门兜底；此处提前拦截，避免白传大文件。
    """
    resp = request_json("GET", "/me")
    balance = int(resp.get("available_words", resp.get("wallet_balance", 0)) or 0)
    if balance < 1:
        log(f"当前可用字数：{balance}，不足以发起操作（需 ≥ 1）。")
        _guide_insufficient_balance({"wallet_balance": balance})


def _submit_interpret(args):
    extra = idempotency_header(args)
    _reject_remote(args.source, "招标文件")
    _check_size(args.source, MAX_TENDER_MB, "招标文件")
    body, ctype = encode_multipart(None, [("file", args.source)])
    return request_json("POST", "/interpretations",
                        headers={**extra, "Content-Type": ctype}, data=body)


def cmd_interpret(args):
    _precheck_balance()
    resp = _submit_interpret(args)
    job_id = resp["job_id"]
    log(f"已提交解读任务 job_id={job_id}")
    if args.no_wait:
        print(job_id)
        return
    poll(job_id, interval=args.interval)
    result = request_json("GET", f"/jobs/{job_id}/result")
    print(json.dumps(zh_risk(result), ensure_ascii=False, indent=2))
    pid = (result.get("result") or {}).get("project_id")
    if pid is not None:
        log(f"project_id={pid}  （后续抽包/生成/合规都复用它）")
    # 招标文件名：优先 --name，否则取上传文件名（路径或 URL 末段）
    tender = args.name or os.path.basename(args.source.rstrip("/"))
    # 记到本地，供后续 report --job / compliance 自动命名（无需再传 --name）
    remember_tender(tender, project_id=pid, job_id=job_id)
    _maybe_report(result, args.report, "解读", tender_name=tender)
    _report_balance()


def cmd_packages(args):
    extra = idempotency_header(args)
    resp = request_json("POST", f"/bid-documents/{args.project_id}/packages", headers=extra)
    job_id = resp["job_id"]
    log(f"已提交抽包任务 job_id={job_id}")
    if args.no_wait:
        print(job_id)
        return
    poll(job_id, interval=args.interval)
    result = request_json("GET", f"/jobs/{job_id}/result")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_generate(args):
    _precheck_balance()
    body = {}
    if args.package_ids:
        body["package_ids"] = [int(x) for x in args.package_ids.split(",") if x.strip()]
    if args.total_pages:
        body["total_pages"] = args.total_pages
    extra = idempotency_header(args)
    resp = request_json("POST", f"/bid-documents/{args.project_id}/generate",
                        headers=extra, json_body=body)
    job_id = resp["job_id"]
    log(f"已提交生成任务 job_id={job_id}（耗时较长，请耐心轮询）")
    if args.no_wait:
        print(job_id)
        return
    poll(job_id, interval=args.interval, timeout=args.timeout)
    if args.output:
        out = args.output
        download_result(job_id, out)
        abs_out = os.path.abspath(out)
        log(f"已下载成品标书：{abs_out}")
        log(f"标书所在目录：{os.path.dirname(abs_out)}")
        print(abs_out)
    else:
        print_download_link(job_id)
    _platform_reminder()
    _report_balance()


def cmd_compliance(args):
    _precheck_balance()
    extra = idempotency_header(args)
    paths = list(args.files)
    for p in paths:
        _reject_remote(p, "投标文件")
        _check_size(p, MAX_BID_MB, "投标文件")
    fields = {
        "is_blind_bid": str(args.blind).lower(),
        "is_electronic_bid": str(args.electronic).lower(),
    }
    if args.sibling_unit_names:
        fields["sibling_unit_names"] = args.sibling_unit_names
    if args.no_semantic_review:
        fields["semantic_review"] = "false"
    body, ctype = encode_multipart(fields, [("bid_files", p) for p in paths])
    resp = request_json("POST", f"/projects/{args.project_id}/compliance-reviews",
                        headers={**extra, "Content-Type": ctype}, data=body)
    job_id = resp["job_id"]
    log(f"已提交合规审查任务 job_id={job_id}")
    if args.no_wait:
        print(job_id)
        return
    poll(job_id, interval=args.interval)
    result = request_json("GET", f"/jobs/{job_id}/result")
    print(json.dumps(zh_risk(result), ensure_ascii=False, indent=2))
    # 招标文件名：--name 优先，否则按 project_id 回查本地（interpret 时记下的）
    tender = args.name or recall_tender(project_id=args.project_id)
    _maybe_report(result, args.report, "合规", tender_name=tender)
    _report_balance()


def cmd_duplicate(args):
    """标书查重：2-3 份投标文件做雷同/相似风险检查，可选招标文件作为公共表述基线。"""
    if not args.legal_possession_attested:
        die("发起标书查重前必须确认：用户合法持有并有权处理本次上传的全部文件。请确认后加 --legal-possession-attested。", code=2)
    if not 2 <= len(args.files) <= 3:
        die("标书查重需要上传 2-3 份投标文件。")
    _precheck_balance()
    extra = idempotency_header(args)
    paths = list(args.files)
    for p in paths:
        _reject_remote(p, "投标文件")
        _check_size(p, MAX_BID_MB, "投标文件")
    tender = args.tender_file
    if tender:
        _reject_remote(tender, "招标文件")
        _check_size(tender, MAX_TENDER_MB, "招标文件")
    _check_total_size(paths + ([tender] if tender else []), MAX_DUP_TOTAL_MB, "查重文件")
    fields = {
        "legal_possession_attested": "true",
        "enable_image": str(not args.no_image).lower(),
        "enable_metadata": str(not args.no_metadata).lower(),
        "enable_semantic": str(not args.no_semantic).lower(),
        "exclude_tender_baseline": str(not args.include_tender_baseline).lower(),
    }
    files = [("bid_files", p) for p in paths]
    if tender:
        files.append(("tender_file", tender))
    body, ctype = encode_multipart(fields, files)
    resp = request_json("POST", "/bid-duplicate/runs",
                        headers={**extra, "Content-Type": ctype}, data=body)
    job_id = resp["job_id"]
    log(f"已提交标书查重任务 job_id={job_id}")
    if args.no_wait:
        print(job_id)
        return
    poll(job_id, interval=args.interval)
    result = request_json("GET", f"/jobs/{job_id}/result")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.report:
        _maybe_report(result, args.report, "查重")
    else:
        log("标书查重结果已输出；可登录百炼®标书平台查看历史报告。")
        _platform_reminder()
    _report_balance()


def cmd_job(args):
    data = request_json("GET", f"/jobs/{args.job_id}")
    print(json.dumps(data, ensure_ascii=False, indent=2))


def download_result(job_id, out_path):
    """流式下载结果（标书制作返回 .docx 二进制）。"""
    url = base_url() + f"/jobs/{job_id}/result"
    req = urllib.request.Request(url, headers=_headers(), method="GET")
    try:
        with urllib.request.urlopen(req) as resp, open(out_path, "wb") as f:
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                f.write(chunk)
    except urllib.error.HTTPError as e:
        _handle_http_error(e)
    except urllib.error.URLError as e:
        die(f"网络错误：{e.reason}", code=1)


def get_download_url(job_id):
    """获取成品标书短时下载链接；链接面向用户，不包含 Api Key。"""
    return request_json("GET", f"/jobs/{job_id}/download-url")


def print_download_link(job_id):
    data = get_download_url(job_id)
    filename = data.get("filename") or f"bid_{job_id}.docx"
    url = data.get("download_url") or ""
    expires = _format_seconds(data.get("expires_in")) or "短时间"
    size = _format_bytes(data.get("size_bytes"))
    log(f"成品标书已生成：{filename}")
    log(f"文件大小：{size}；下载链接 {expires} 内有效。")
    log("如需保存到本地，请继续执行：python3 scripts/zcm.py result "
        f"{job_id} -o <本地路径>.docx")
    print(url)


def cmd_result(args):
    if args.output:
        download_result(args.job_id, args.output)
        log(f"已保存：{args.output}")
        print(args.output)
        _platform_reminder()
    else:
        data = request_json("GET", f"/jobs/{args.job_id}/result")
        print(json.dumps(zh_risk(data), ensure_ascii=False, indent=2))


def cmd_download_url(args):
    print_download_link(args.job_id)


def cmd_cancel(args):
    data = request_json("POST", f"/jobs/{args.job_id}/cancel")
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_progress_stream(args):
    """流式进度到 stdout，每行一条状态变更，供 Monitor 工具实时订阅。
    成功退出 0，失败/取消/超时退出 1。
    """
    deadline = time.time() + args.timeout
    last = ""
    last_pct = None
    last_stage = ""
    last_emit_at = 0.0
    while True:
        try:
            st = request_json("GET", f"/jobs/{args.job_id}")
        except (Exception, SystemExit):
            # 网络抖动/连接重置/服务重启时跳过本次，不崩溃
            time.sleep(1)
            continue
        status = st.get("status")
        prog = st.get("progress") or {}
        pct = prog.get("percent")
        # stage_key 不含时间字段，避免秒级变化造成刷屏；心跳由 --heartbeat 控制。
        stage_key = "|".join(str(prog.get(k) or "") for k in (
            "stage", "stage_label", "message", "current_step", "total_steps", "current_step_label",
        )) + f"|{status}"
        stage_changed = stage_key != last_stage
        pct_stepped = (last_pct is None or pct is None or
                       abs(pct - last_pct) >= args.step or stage_changed)
        heartbeat_due = last_emit_at <= 0 or (time.time() - last_emit_at) >= args.heartbeat
        line = format_progress_line(prog, status=status)
        if line != last and (pct_stepped or heartbeat_due):
            print(line, flush=True)
            last = line
            last_stage = stage_key
            last_emit_at = time.time()
            if pct is not None:
                last_pct = pct
        if status == "succeeded":
            print("[完成]", flush=True)
            return
        if status in ("failed", "canceled"):
            err = st.get("error") or {}
            ecode = err.get("code", "")
            hint = ERROR_HINTS.get(ecode, "")
            print(f"[失败] {ecode} {err.get('message', '')} {hint}".strip(), flush=True)
            sys.exit(1)
        if time.time() > deadline:
            print(f"[超时] 任务超过 {args.timeout}s 未完成", flush=True)
            sys.exit(1)
        time.sleep(args.interval)


def build_parser():
    p = argparse.ArgumentParser(description="百炼®标书开放 API 轻客户端 / zh-CN client for mainland-China bidding workflows")
    p.add_argument("--version", action="version",
                   version=f"biaoshu-bailian {SKILL_VERSION}　·　适配 {API_TARGET}　·　契约快照 {CONTRACT_SNAPSHOT}")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_common(sp, wait=False):
        sp.add_argument("--interval", type=int, default=5, help="轮询间隔秒（默认 5）")
        if wait:
            sp.add_argument("--no-wait", action="store_true", help="只提交，打印 job_id 不轮询")
            sp.add_argument("--idempotency-key", help="幂等键 UUID，重试防重复扣费")

    sp = sub.add_parser("login", help="保存凭证到 skill 内 config.json")
    sp.add_argument("--app-key", help="Api Key，形如 bk_live_xxxxx（必填）")
    sp.add_argument("--output-dir", help="可选：成品标书 .docx 默认存放目录")
    sp.set_defaults(func=cmd_login)

    sp = sub.add_parser("logout", help="删除已保存的凭证文件")
    sp.set_defaults(func=cmd_logout)

    sp = sub.add_parser("me", help="查连通性与可用字数")
    sp.set_defaults(func=cmd_me)

    sp = sub.add_parser("knowledge-base", help="按类别查询知识库（排除历史标书库 / 标书模板库）")
    sp.add_argument("category", nargs="?", help="可选：company_profile / qualifications / performances / financial_reports")
    sp.add_argument("--page", type=int, default=1, help="分页类页码（默认 1）")
    sp.add_argument("--page-size", type=int, default=50, help="分页类每页条数（默认 50）")
    sp.set_defaults(func=cmd_knowledge_base)

    sp = sub.add_parser("interpret", help="智能解读招标文件 → 完整解读结果")
    sp.add_argument("source", help="本地文件(.pdf/.doc/.docx)")
    sp.add_argument("--report", choices=["html", "docx", "both"], help="取结果后直接生成解读报告")
    sp.add_argument("--name", help="招标文件名（报告默认命名用；不填取上传文件名）")
    add_common(sp, wait=True)
    sp.set_defaults(func=cmd_interpret)

    sp = sub.add_parser("packages", help="抽取分包供挑选")
    sp.add_argument("project_id")
    add_common(sp, wait=True)
    sp.set_defaults(func=cmd_packages)

    sp = sub.add_parser("generate", help="生成成品标书（默认输出短时下载链接，-o 时下载 .docx）")
    sp.add_argument("project_id")
    sp.add_argument("--package-ids", help="逗号分隔的选中分包 ID，如 11,12（多包必填）")
    sp.add_argument("--total-pages", type=int, help="期望总页数（可选）")
    sp.add_argument("-o", "--output", help="输出 .docx 路径（默认 招标文件名_投标文件.docx）")
    sp.add_argument("--name", help="招标文件名（成品默认命名 招标文件名_投标文件）")
    sp.add_argument("--timeout", type=int, default=3600, help="轮询超时秒（默认 3600）")
    add_common(sp, wait=True)
    sp.set_defaults(func=cmd_generate)

    sp = sub.add_parser("compliance", help="标书审查投标文件(.doc/.docx/.pdf)")
    sp.add_argument("project_id")
    sp.add_argument("files", nargs="+", help="一个或多个本地 .doc/.docx/.pdf")
    sp.add_argument("--blind", action="store_true", help="暗标")
    sp.add_argument("--electronic", action="store_true", help="电子标")
    sp.add_argument("--sibling-unit-names", help="敏感单位名称，多个用逗号或顿号分隔")
    sp.add_argument("--no-semantic-review", action="store_true", help="关闭语义审查，仅保留规则类检查")
    sp.add_argument("--report", choices=["html", "docx", "both"], help="取结果后直接生成合规报告")
    sp.add_argument("--name", help="招标文件名（合规报告默认命名 招标文件名_合规审查）")
    add_common(sp, wait=True)
    sp.set_defaults(func=cmd_compliance)

    sp = sub.add_parser("duplicate", help="标书查重：2-3 份投标文件雷同/相似风险检查")
    sp.add_argument("files", nargs="+", help="2-3 个本地 .doc/.docx/.pdf")
    sp.add_argument("--tender-file", help="可选：招标文件（本地 .doc/.docx/.pdf），用于排除招标原文共同表述")
    sp.add_argument("--legal-possession-attested", action="store_true",
                    help="确认用户合法持有并有权处理本次上传的全部文件（必需）")
    sp.add_argument("--no-image", action="store_true", help="关闭图片相似检查")
    sp.add_argument("--no-metadata", action="store_true", help="关闭文档元数据检查")
    sp.add_argument("--no-semantic", action="store_true", help="关闭语义相似检查")
    sp.add_argument("--include-tender-baseline", action="store_true",
                    help="不排除招标文件原文造成的共同表述（默认排除）")
    sp.add_argument("--report", choices=["html", "docx", "both"], help="取结果后直接生成查重报告")
    add_common(sp, wait=True)
    sp.set_defaults(func=cmd_duplicate)

    sp = sub.add_parser("report", help="把解读/合规/查重结果渲染成 HTML/Word 报告")
    g = sp.add_mutually_exclusive_group(required=True)
    g.add_argument("--job", help="任务 job_id（自动取 /result 再渲染）")
    g.add_argument("--in", dest="in_file", help="本地结果 JSON 文件（/result 响应或 result 体）")
    sp.add_argument("--service", choices=["interpretation", "compliance", "bid_duplicate"], help="不指定则自动识别")
    sp.add_argument("--format", choices=["html", "docx", "both"], default="html",
                    help="默认 html；用户明确要 Word 才用 docx 或 both")
    sp.add_argument("-o", "--out-dir", help="输出目录（默认成品目录 biaoshu-bailian-files/）")
    sp.add_argument("--name", help="招标文件名（报告默认命名 招标文件名_{智能解读|合规审查|标书查重}）")
    sp.add_argument("--basename", help="完整文件名（不含扩展名），优先级最高")
    sp.set_defaults(func=cmd_report)

    sp = sub.add_parser("job", help="查任务状态（不轮询）")
    sp.add_argument("job_id")
    sp.set_defaults(func=cmd_job)

    sp = sub.add_parser("result", help="取任务结果")
    sp.add_argument("job_id")
    sp.add_argument("-o", "--output", help="保存到本地文件（标书制作 .docx 需要本地文件时使用）")
    sp.set_defaults(func=cmd_result)

    sp = sub.add_parser("download-url", help="获取成品标书短时下载链接（不暴露 Api Key）")
    sp.add_argument("job_id")
    sp.set_defaults(func=cmd_download_url)

    sp = sub.add_parser("cancel", help="取消任务")
    sp.add_argument("job_id")
    sp.set_defaults(func=cmd_cancel)

    sp = sub.add_parser("progress-stream",
                        help="流式进度到 stdout，供 Monitor 实时订阅（配合 --no-wait 两阶段用）")
    sp.add_argument("job_id")
    sp.add_argument("--interval", type=float, default=0.015, help="轮询间隔秒（默认 0.015 即 15ms）")
    sp.add_argument("--step", type=int, default=5, help="百分比变化步进阈值，达到才输出（默认 5）")
    sp.add_argument("--heartbeat", type=float, default=30, help="无新阶段时的心跳输出间隔秒（默认 30）")
    sp.add_argument("--timeout", type=int, default=3600, help="超时秒（默认 3600）")
    sp.set_defaults(func=cmd_progress_stream)

    return p


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
