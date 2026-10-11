#!/usr/bin/env python3
"""
resilience.py — 拼多多会话层取数的「对平台友好·失败即止」健壮层。

设计目标：接口改版/异常时**少打、慢打、早停**，绝不重试成风暴触发风控。

四条机制：
  1. 失败分型（classify）：区分可重试的临时抖动 vs 不该重试的结构性问题。
       transient  超时/网络/5xx        → 退避重试（最多 MAX_ATTEMPTS-1 次）
       frequency  平台频率信号(54001)   → 不重试，直接长冷却（平台在喊慢一点，就真慢）
       auth       登录过期/鉴权失败      → 不重试，停并提示用户重新登录
       drift      响应结构不符期望       → 不重试（重试一万次也没用），停并上报“疑似接口改版”
  2. 指数退避 + jitter：base * 2^attempt + 随机抖动，封顶 BACKOFF_CAP。
  3. 熔断器（持久化到 ~/.pdd-data/health.json）：
       某端点连续失败≥TRIP_AFTER → 进入冷却期（cooldown_until），期间 should_skip() 直接跳过不打。
  4. 漂移告警：drift/auth 记录 endpoint+期望+实际，供集中修复（技能作者改一次，而非每客户瞎试）。

用法（Python 侧，包住每个逻辑端点调用）：
    import resilience as R
    ok, data, err = R.run("goods_list", do_once, validate=R.v_nonempty_list("goods_list"))
其中 do_once() 返回原始响应 dict（或抛异常）；validate(resp) 返回 True/False。
"""
import os, json, time, random, datetime, re as _re, hashlib
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

HEALTH = os.path.expanduser(os.environ.get("PDD_HEALTH_PATH", "~/.pdd-data/health.json"))

MAX_ATTEMPTS = 2          # 总尝试次数（含首次）；即最多重试 1 次
BACKOFF_BASE = 1.5        # 秒
BACKOFF_CAP = 8.0         # 秒
TRIP_AFTER = 3            # 连续失败多少次后熔断
COOLDOWN = {              # 不同失败类型的冷却时长（秒）
    "transient": 300,     # 5 分钟
    "frequency": 1800,    # 30 分钟（平台喊慢，就慢久一点）
    "auth": 3600,         # 1 小时（等用户重新登录）
    "drift": 86400,       # 24 小时（等作者修技能）
}


# ---------------- 失败分型 ----------------

def classify(resp, exc=None):
    """返回 ('ok'|'transient'|'frequency'|'auth'|'drift', 说明)"""
    if exc is not None:
        msg = str(exc).lower()
        if any(k in msg for k in ("timeout", "timed out", "econn", "network", "reset", "refused")):
            return "transient", f"网络异常: {str(exc)[:80]}"
        return "transient", f"调用异常: {str(exc)[:80]}"
    if not isinstance(resp, dict):
        return "drift", "响应不是对象（结构异常）"
    ec = resp.get("error_code") or resp.get("errorCode")
    em = (resp.get("error_msg") or resp.get("errorMsg") or "")
    if ec in (54001,) or "频繁" in em or "太频繁" in str(em):
        return "frequency", f"平台频率限制: {em or ec}"
    if ec in (40001, 43001, 10001) or "登录" in str(em) or "鉴权" in str(em) or "未登录" in str(em):
        return "auth", f"登录/鉴权失效: {em or ec}"
    if "权限" in str(em):
        return "auth", f"权限不足: {em}"
    if resp.get("success") is False:
        return "transient", f"业务失败: {em or ec}"
    return "ok", ""


def backoff(attempt):
    return min(BACKOFF_CAP, BACKOFF_BASE * (2 ** attempt)) + random.uniform(0, 0.8)


# ---------------- 熔断器状态 ----------------

_MEM = {}  # 磁盘不可写（沙箱拦截）时的进程内降级缓存——熔断状态丢失好过采集崩溃

def _load():
    try:
        return {**json.load(open(HEALTH)), **_MEM}
    except Exception:
        return dict(_MEM)

def _save(s):
    """就地截断写（非 原子替换）。

    刻意不用"写 .tmp + os.replace"：replace 在文件系统层 = unlink 旧文件，
    Agent 沙箱（WorkBuddy/CodeBuddy 等）的文件监控会把它误判成"删除文件"弹权限，
    用户拒绝后采集被中断。health.json 是可再生缓存（熔断/健康状态，坏了从零累计），
    不值得为原子性冒权限弹窗的险。写失败（沙箱只读）→ 降级内存态，绝不阻塞采集。
    """
    try:
        os.makedirs(os.path.dirname(HEALTH), exist_ok=True)
        with open(HEALTH, "w") as f:
            json.dump(s, f, ensure_ascii=False, indent=1)
            f.flush()
            os.fsync(f.fileno())
        _MEM.clear()
    except OSError:
        _MEM.clear()
        _MEM.update(s)

def _now():
    return int(time.time())


def should_skip(endpoint):
    """熔断冷却中 → (True, 冷却剩余秒, 原因)；否则 (False, 0, '')"""
    st = _load().get(endpoint, {})
    until = st.get("cooldown_until", 0)
    if until > _now():
        return True, until - _now(), st.get("last_error", "")
    return False, 0, ""


def record(endpoint, kind, note=""):
    s = _load()
    st = s.get(endpoint, {"consecutive_fails": 0})
    now = _now()
    if kind == "ok":
        st = {"consecutive_fails": 0, "last_ok": now, "last_error": ""}
    else:
        st["consecutive_fails"] = st.get("consecutive_fails", 0) + 1
        st["last_error"] = f"{kind}: {note}"[:160]
        st["last_fail"] = now
        # frequency/auth/drift 立刻冷却；transient 到达阈值才熔断
        if kind in ("frequency", "auth", "drift") or st["consecutive_fails"] >= TRIP_AFTER:
            st["cooldown_until"] = now + COOLDOWN.get(kind, 300)
            st["tripped_as"] = kind
        if kind == "drift":
            st.setdefault("drift_reports", []).append({"at": now, "note": note[:200]})
            st["drift_reports"] = st["drift_reports"][-5:]
    s[endpoint] = st
    _save(s)
    return st


# ---------------- 校验器工厂 ----------------

def _unwrap(resp):
    """__mms.fetch.post 已解包返回 result 本身（顶层即数据）；也兼容带 {result:...} 包装。"""
    if not isinstance(resp, dict):
        return None
    r = resp.get("result")
    return r if isinstance(r, dict) else resp

def v_nonempty_list(list_key):
    def _v(resp):
        r = _unwrap(resp)
        if not isinstance(r, dict):
            return False
        return isinstance(r.get(list_key), list)   # 允许空列表，但必须是 list
    return _v

def v_has_keys(*keys):
    def _v(resp):
        r = _unwrap(resp)
        return isinstance(r, dict) and all(k in r for k in keys)
    return _v

def v_truthy(resp):
    return isinstance(resp, dict) and resp.get("success") is not False


# ---------------- 编排器 ----------------

def run(endpoint, do_once, validate=v_truthy, shop=None):
    """
    返回 (ok: bool, data: dict|None, err: dict|None)。
    err 结构（给 agent）：{endpoint, kind, note, action:{type,message}, cooldown_s}
    shop: 店铺别名（多店模式）。熔断键 = endpoint#shop，各店独立熔断互不连坐。
    """
    key = f"{endpoint}#{shop}" if shop else endpoint
    skip, left, why = should_skip(key)
    if skip:
        return False, None, {
            "endpoint": endpoint, "kind": "cooldown", "note": why,
            "cooldown_s": left,
            "action": {"type": "notify_user",
                       "message": f"{endpoint} 近期连续异常，已暂停 {left // 60} 分钟以保护账号安全，稍后自动恢复。"}}

    last = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            resp = do_once()
            kind, note = classify(resp)
            if kind == "ok":
                if validate(resp):
                    record(key, "ok")
                    return True, resp, None
                kind, note = "drift", "响应结构不符期望（校验未通过）"
        except Exception as e:  # noqa: BLE001
            kind, note = classify(None, exc=e)
            resp = None

        last = (kind, note)
        # 不可重试类型：立刻停
        if kind in ("frequency", "auth", "drift"):
            break
        # 可重试：退避后再试（若还有次数）
        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(backoff(attempt))

    kind, note = last
    st = record(key, kind, note)
    if kind == "drift":
        # 进化闭环：疑似接口改版 → 上报 Claw School（fail-silent，不影响本流程）
        # 注意：endpoint 不带 shop 维度——接口改版是平台侧问题，11 家店撞同一个改版应聚成 1 条
        report_bug(endpoint, kind, note)
    action = {
        "frequency": {"type": "notify_user", "message": "拼多多提示操作频繁，已自动暂停采集，稍后自动重试。"},
        "auth": {"type": "notify_user", "message": "拼多多登录可能已过期，请在浏览器重新登录商家后台后再试。"},
        "drift": {"type": "call_support", "message": "拼多多后台接口可能有更新，已记录并暂停。请联系 Claw School 更新技能（我们会集中修复）。"},
        "transient": {"type": "retry", "message": "网络波动导致采集未完成，稍后会自动重试。"},
    }.get(kind, {"type": "notify_user", "message": "采集暂时未完成。"})
    return False, None, {"endpoint": endpoint, "kind": kind, "note": note,
                         "cooldown_s": st.get("cooldown_until", 0) - _now()
                         if st.get("cooldown_until") else 0,
                         "action": action}


def health_summary():
    s = _load()
    out = {}
    for ep, st in s.items():
        if ep.startswith("_"):
            continue
        cd = st.get("cooldown_until", 0) - _now()
        out[ep] = {"fails": st.get("consecutive_fails", 0),
                   "cooldown_left_s": max(0, cd),
                   "last_error": st.get("last_error", "")}
    return out


# ---------------- Bug Report（fail-silent 进化闭环上报器） ----------------
# 技能在外场发现 drift（疑似接口改版）→ 结构化上报 claw-school.com → 学校集中修复。
# 三条纪律：
#   1. 隐私：payload 只有 技能名/版本/端点/分型/规范化指纹/脱敏说明。绝不带 cookie/店铺数据/订单。
#   2. fail-silent：上报失败不影响技能本身（3 秒超时，异常全吞）。
#   3. 防重复：同指纹本地 7 天只发一次（服务端还有 7 天去重窗口，双保险）。

REPORT_URL = os.environ.get("PDD_BUG_REPORT_URL", "https://claw-school.com/api/bug-report")
REPORT_ENABLED = os.environ.get("PDD_BUG_REPORT", "1") != "0"
REPORT_COOLDOWN = 7 * 86400
_REDACT = _re.compile(r"(cookie|session|token|passwd|password|authorization)[^\s]*", _re.I)


def _skill_identity():
    """(skill_name, version) 从 ../skill.yaml 读；读不到就退回目录名。"""
    fallback = os.path.basename(os.path.dirname(HERE))
    try:
        y = open(os.path.join(HERE, "..", "skill.yaml"), encoding="utf-8").read()
        name = _re.search(r"^name:\s*(\S+)", y, _re.M)
        ver = _re.search(r"^version:\s*(\S+)", y, _re.M)
        return (name.group(1) if name else fallback, ver.group(1) if ver else None)
    except Exception:
        return (fallback, None)


def _fingerprint(skill, endpoint, kind, note):
    """规范化（去数字/空白，消除时戳与计数差异）后哈希 → 同一故障聚成一条。"""
    norm = _re.sub(r"[\d\s]", "", f"{skill}|{endpoint}|{kind}|{note or ''}").lower()
    return hashlib.sha256(norm.encode()).hexdigest()[:32]


def report_bug(endpoint, kind, note=""):
    """把 drift 级故障上报 Claw School。任何失败都静默（返回 None 或响应摘要 dict）。"""
    if not REPORT_ENABLED:
        return None
    try:
        skill, ver = _skill_identity()
        clean_note = _REDACT.sub("<redacted>", (note or ""))[:300]
        fp = _fingerprint(skill, endpoint, kind, clean_note)

        # 本地冷却：同指纹 7 天只发一次
        s = _load()
        last = (s.get("_bug_reports", {}) or {}).get(fp, 0)
        if _now() - last < REPORT_COOLDOWN:
            return None

        payload = json.dumps({
            "skill": skill, "skill_version": ver, "endpoint": endpoint,
            "kind": kind, "fingerprint": fp, "note": clean_note, "client": "workbuddy",
        }).encode()
        req = urllib.request.Request(
            REPORT_URL, data=payload, method="POST",
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=3) as r:
            resp = json.loads(r.read().decode() or "{}")

        s = _load()
        s.setdefault("_bug_reports", {})[fp] = _now()
        s["_bug_reports"] = dict(list(s["_bug_reports"].items())[-50:])
        _save(s)
        return resp
    except Exception:
        return None  # fail-silent：上报通道再糟也不拖累技能本身
