#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WorkBuddy 每日签到领积分 —— 幂等、零依赖（仅 Python 标准库）。

1.6.0 合并版：
  * 安全骨架来自 SkillHub 1.5.3：域名硬白名单、强制 HTTPS/443、禁止重定向、
    校验响应 host、JWT 脱敏、守卫路径加固。
  * 本机凭据自动读取（继承自 1.4.1）+ buildkey_direct.js 免 GUI 提 key
    （来自另一位作者 1.2.0）：客户端**没打开也能签到**，定时任务不中断。
  * 显式凭据优先：设置 WB_ACCESS_TOKEN / WB_TOKEN_FILE 时只用用户给的 token，
    不碰本机文件；WB_NO_LOCAL_AUTH=1 可完全关闭本机回退。

凭据优先级：
  1. WB_ACCESS_TOKEN / WB_TOKEN_FILE（显式，用户主动提供）
  2. 本机客户端会话文件（需 WB_NO_LOCAL_AUTH 未开启；at-rest 信封自动解密）

用法:
  python wb-checkin.py                 正常签到（幂等：今日已领则跳过）
  python wb-checkin.py --status        只查询状态，不领取
  python wb-checkin.py --json          以 JSON 输出状态（含 _meta / _gaps_7d）
  python wb-checkin.py --report        签到周报（本周 / 近 30 天 / 漏签日）
  python wb-checkin.py --accounts      列出凭据目录里的账号 uid（不显示 token）
  python wb-checkin.py --uid <uid>     指定签到账号（等价 WB_UID）
  python wb-checkin.py --force         强制调用领取接口（调试用）
  python wb-checkin.py --no-refresh    禁止自动续期（排障用）

退出码:
  0  成功领取 / 今日已领 / 活动未开启 / 仅查询
  1  失败（凭据缺失、鉴权失效、接口异常）
"""
import os
import re
import sys
import json
import glob
import time
import base64
import datetime
import platform
import argparse
import unicodedata
import urllib.parse
import urllib.request
import urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# at_rest.py / token_provider.py 与本脚本同目录
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import token_provider  # noqa: E402

DEFAULT_ENDPOINT = "https://copilot.tencent.com"
STATUS_PATH = "/v2/billing/meter/checkin-activity-status"
CLAIM_PATH = "/v2/billing/meter/daily-checkin"
REFRESH_PATH = "/v2/plugin/auth/token/refresh"

# 仅允许 WorkBuddy 官方域名；硬约束，无环境变量可放行到其它主机。
ALLOWED_HOSTS = frozenset({"copilot.tencent.com", "www.workbuddy.cn"})

# 客户端共享数据目录名（源码常量 EXTENSION_DATA_DIR_NAME）
DATA_DIR_NAME = "CodeBuddyExtension"
AUTH_SUBPATH = os.path.join(DATA_DIR_NAME, "Data", "Public", "auth")
BACKUP_RE = re.compile(r"\.\d{4}-\d{2}-\d{2}T[\d-]+Z\.info$", re.IGNORECASE)
_JWT_IN_TEXT = re.compile(
    r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")


def log(*a):
    print(*a, flush=True)


def redact(text):
    """日志/错误信息脱敏：绝不把完整 JWT 打到终端。"""
    return _JWT_IN_TEXT.sub("***REDACTED***", str(text))


# ---------------------------------------------------------------- 出口安全
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """禁止自动重定向：请求头带 Bearer token，302 到别的域名等于把 token 交出去。"""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(
            req.full_url, code,
            "redirect blocked: token must not follow cross-origin redirects",
            headers, fp)


_OPENER = urllib.request.build_opener(_NoRedirect)


def resolve_endpoint():
    """把 endpoint 收敛成 https://白名单主机。"""
    raw = (os.environ.get("WB_ENDPOINT") or DEFAULT_ENDPOINT).strip()
    if "://" not in raw:
        raw = "https://" + raw
    p = urllib.parse.urlparse(raw)
    if p.scheme != "https":
        raise ValueError("endpoint 必须是 https，拒绝明文传输 token")
    if p.username or p.password:
        raise ValueError("endpoint 不允许内嵌用户名/密码")
    if p.path not in ("", "/") or p.query or p.fragment:
        raise ValueError("endpoint 只允许纯主机，不允许路径/查询/片段")
    host = (p.hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise ValueError("endpoint 主机 %r 不在白名单 %s 内；白名单为硬约束"
                         % (host, sorted(ALLOWED_HOSTS)))
    if p.port not in (None, 443):
        raise ValueError("endpoint 只允许默认的 443 端口")
    return "https://" + host


def _post(url, headers, expected_host):
    """固定 https + 白名单 host + 禁重定向 + 校验最终响应 host。"""
    if urllib.parse.urlparse(url).scheme != "https":
        return 0, {"raw": "refused: non-https url"}
    req = urllib.request.Request(url, data=b"{}", method="POST")
    for key, val in headers.items():
        req.add_header(key, str(val))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        with _OPENER.open(req, timeout=20) as r:
            final_host = (urllib.parse.urlparse(r.geturl()).hostname or "").lower()
            if final_host != expected_host:
                return 0, {"raw": "refused: response from unexpected host %s" % final_host}
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": redact(raw[:400])}
    except urllib.error.URLError as e:
        return 0, {"raw": "网络不可达: %s" % redact(e.reason)}


def call(path, cred, endpoint):
    headers = {"Authorization": "Bearer " + cred["token"]}
    if cred.get("uid"):
        headers["X-User-Id"] = str(cred["uid"])
    if cred.get("domain"):
        headers["X-Domain"] = str(cred["domain"])
    host = urllib.parse.urlparse(endpoint).hostname
    return _post(endpoint + path, headers, host)


# ---------------------------------------------------------------- 本机凭据
def auth_dir_candidates():
    override = os.environ.get("WB_AUTH_DIR")
    if override:
        return [override]
    out = []
    system = platform.system()
    home = os.path.expanduser("~")
    if system == "Windows":
        local = os.environ.get("LOCALAPPDATA") or os.path.join(home, "AppData", "Local")
        out.append(os.path.join(local, AUTH_SUBPATH))
    elif system == "Darwin":
        out.append(os.path.join(home, "Library", "Application Support", AUTH_SUBPATH))
        out.append(os.path.join(home, ".local", "share", AUTH_SUBPATH))
    else:
        xdg = os.environ.get("XDG_DATA_HOME") or os.path.join(home, ".local", "share")
        out.append(os.path.join(xdg, AUTH_SUBPATH))
    out.append(os.path.join(home, AUTH_SUBPATH))
    return out


def _load_at_rest():
    try:
        import at_rest
        return at_rest
    except Exception:
        return None


def _read_info(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return None


def _uid_of(data):
    return ((data.get("account") or {}).get("uid")
            or (data.get("auth") or {}).get("uid"))


def list_accounts():
    """列出凭据目录里的账号 uid 与文件情况（绝不输出 token）。"""
    found = {}
    tried = []
    for d in auth_dir_candidates():
        tried.append(d)
        if not os.path.isdir(d):
            continue
        for f in glob.glob(os.path.join(d, "*.info")):
            data = _read_info(f)
            if not data:
                continue
            uid = _uid_of(data) or "(unknown)"
            rec = found.setdefault(uid, {"count": 0, "mtime": 0})
            rec["count"] += 1
            rec["mtime"] = max(rec["mtime"], os.path.getmtime(f))
        if found:
            break
    return found, tried


def _scan_cred(uid=None):
    """扫凭据目录，返回 dict(cred, rejected, tried, envelope_blocked, uids)。

    uid 非空时**只认这个账号**——这是修「定时任务签到签给别人」的关键：
    旧版按「最新文件的 uid」猜目标账号，客户端一切换账号就串号。
    """
    at_rest = _load_at_rest()
    tried, rejected, uids = [], [], set()
    envelope_blocked = False

    for d in auth_dir_candidates():
        tried.append(d)
        if not os.path.isdir(d):
            continue
        files = glob.glob(os.path.join(d, "*.info"))
        if not files:
            continue
        parsed = []
        for f in files:
            data = _read_info(f)
            if data:
                parsed.append((f, data))
                if _uid_of(data):
                    uids.add(str(_uid_of(data)))
        if not parsed:
            continue

        parsed.sort(key=lambda x: os.path.getmtime(x[0]), reverse=True)
        target_uid = uid or next(
            (str(_uid_of(data)) for _f, data in parsed if _uid_of(data)), None)

        def rank(item):
            f, data = item
            auth = data.get("auth") or {}
            cur_uid = _uid_of(data)
            exp = (auth.get("expiresAt") or 0) / 1000
            return (
                0 if str(cur_uid) == str(target_uid) else 1,
                0 if exp > time.time() else 1,
                0 if not BACKUP_RE.search(os.path.basename(f)) else 1,
                -os.path.getmtime(f),
            )

        for f, data in sorted(parsed, key=rank):
            if uid and str(_uid_of(data)) != str(uid):
                continue
            auth = data.get("auth") or {}
            acct = data.get("account") or {}
            raw = auth.get("accessToken")
            if not raw:
                continue
            try:
                if isinstance(raw, str):
                    token = raw
                else:
                    envelope_blocked = True
                    if at_rest is None:
                        raise RuntimeError("at_rest 模块不可用，无法解密信封")
                    token = at_rest.unwrap(raw)
            except Exception as e:
                rejected.append("%s: %s" % (os.path.basename(f)[:48], e))
                continue
            if not isinstance(token, str) or token.count(".") < 2:
                rejected.append("%s: 解出的不是 JWT" % os.path.basename(f)[:48])
                continue

            refresh = None
            raw_refresh = auth.get("refreshToken")
            if raw_refresh:
                try:
                    refresh = at_rest.unwrap(raw_refresh) if at_rest else (
                        raw_refresh if isinstance(raw_refresh, str) else None)
                except Exception:
                    refresh = None

            return {
                "cred": {
                    "file": f,
                    "token": token,
                    "refresh": refresh,
                    "uid": _uid_of(data),
                    "domain": auth.get("domain"),
                    "data": data,
                },
                "rejected": rejected,
                "tried": tried,
                "envelope_blocked": envelope_blocked,
                "uids": uids,
            }

    return {"cred": None, "rejected": rejected, "tried": tried,
            "envelope_blocked": envelope_blocked, "uids": uids}


def _bootstrap_build_key():
    try:
        import buildkey_bootstrap
    except Exception as e:
        return False, {"reason": "bootstrap_module_unavailable: %s" % e}
    try:
        return buildkey_bootstrap.bootstrap(verbose=False)
    except Exception as e:
        return False, {"reason": "bootstrap_error: %s" % e}


def load_cred(uid=None, allow_bootstrap=True):
    """挑一个能用的本机凭据。解密失败时自愈提 build key 后重试一次。"""
    res = _scan_cred(uid=uid)
    if res["cred"]:
        return res["cred"]

    if allow_bootstrap and res["envelope_blocked"]:
        log("[INFO] 本地凭据是加密信封，但没有可用的 build key；尝试自动提取…")
        ok, info = _bootstrap_build_key()
        if ok:
            log("[INFO] 已提取 build key（%s），重试解密…" % info.get("method"))
            res2 = _scan_cred(uid=uid)
            if res2["cred"]:
                return res2["cred"]
            res["rejected"] = res2["rejected"] or res["rejected"]
        else:
            reason = info.get("reason")
            log("[WARN] 自动提取 build key 失败：%s（direct=%s）"
                % (reason, info.get("direct")))
            if info.get("hint"):
                log("       %s" % info["hint"])

    msg = ("未找到可用的凭据文件。已尝试以下目录：\n  " + "\n  ".join(res["tried"]))
    if uid:
        msg += "\n指定 uid=%s 在该目录下没有可用凭据。可用 uid：\n  %s" % (
            uid, "\n  ".join(sorted(res["uids"])) or "(无)")
    else:
        msg += "\n本机可用 uid：\n  %s" % ("\n  ".join(sorted(res["uids"])) or "(无)")
    msg += "\n也可显式提供凭据：WB_ACCESS_TOKEN / WB_TOKEN_FILE，或用 WB_AUTH_DIR 指定目录。"
    if res["rejected"]:
        msg += "\n\n已跳过（解密/格式不合格）：\n  " + "\n  ".join(res["rejected"][:8])
    raise FileNotFoundError(msg)


def resolve_cred(uid=None):
    """统一凭据入口，返回 (cred, mode)。mode = explicit | local。"""
    explicit = token_provider.resolve_optional()
    if explicit:
        return explicit, "explicit"
    if os.environ.get("WB_NO_LOCAL_AUTH") == "1":
        raise FileNotFoundError(
            "已禁用本机凭据回退（WB_NO_LOCAL_AUTH=1）。请设置 WB_ACCESS_TOKEN "
            "或 WB_TOKEN_FILE 提供 accessToken。")
    return load_cred(uid=uid), "local"


# ---------------------------------------------------------------- 登录态续期
def client_running():
    try:
        import buildkey_bootstrap
        return bool(buildkey_bootstrap.candidate_pids())
    except Exception:
        return False


def _claim_lock(lock_path, stale_seconds=120):
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return True
    except FileExistsError:
        try:
            if time.time() - os.path.getmtime(lock_path) > stale_seconds:
                os.unlink(lock_path)
                fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                return True
        except Exception:
            pass
        return False


def _release_lock(lock_path):
    try:
        os.unlink(lock_path)
    except Exception:
        pass


def _now_ms():
    return int(time.time() * 1000)


def refresh_session(cred, endpoint):
    if not cred.get("refresh"):
        return False, {"reason": "no_refresh_token"}
    headers = {"X-Refresh-Token": cred["refresh"],
               "X-Auth-Refresh-Source": "plugin"}
    if cred.get("uid"):
        headers["X-User-Id"] = str(cred["uid"])
    if cred.get("domain"):
        headers["X-Domain"] = str(cred["domain"])
    host = urllib.parse.urlparse(endpoint).hostname
    status, payload = _post(endpoint + REFRESH_PATH, headers, host)
    if status != 200:
        return False, {"reason": "http_%s" % status, "payload": payload}
    if not isinstance(payload, dict) or payload.get("code") not in (0, None):
        return False, {"reason": "api_code_%s" % (payload or {}).get("code")}
    data = (payload.get("data") or {})
    if not isinstance(data, dict) or not data.get("accessToken"):
        return False, {"reason": "empty_token"}
    return True, {"data": data}


def _seal_like(original_value, plaintext):
    if isinstance(original_value, str):
        return plaintext
    import at_rest
    return at_rest.seal(plaintext)


def persist_auth(cred, new_auth):
    """新 token 写回本机凭据（仅 local 模式）。原子替换 + 备份 + 排他锁。"""
    path, data = cred.get("file"), cred.get("data")
    if not path or not isinstance(data, dict):
        return False, "非本机凭据模式，不写盘"
    auth = data.get("auth")
    if not isinstance(auth, dict):
        return False, "凭据文件缺少 auth 段"
    try:
        import at_rest  # noqa: F401
    except Exception as e:
        return False, "at_rest 不可用: %s" % e

    lock_path = path + ".wb-lock"
    if not _claim_lock(lock_path):
        return False, "凭据文件被占用（另一实例正在写），本次跳过写回"
    tmp_path, bak_path = path + ".wb-tmp", path + ".wb-bak"
    try:
        try:
            with open(path, encoding="utf-8") as fh:
                latest = json.load(fh)
            if (latest.get("auth") or {}).get("accessToken") != auth.get("accessToken"):
                return False, "凭据已被客户端更新，跳过写回"
        except Exception:
            pass
        try:
            with open(path, "rb") as src, open(bak_path, "wb") as dst:
                dst.write(src.read())
        except Exception:
            pass

        auth["accessToken"] = _seal_like(auth.get("accessToken"), new_auth["accessToken"])
        if new_auth.get("refreshToken"):
            auth["refreshToken"] = _seal_like(auth.get("refreshToken"), new_auth["refreshToken"])
        for k in ("expiresIn", "refreshExpiresIn", "tokenType", "domain", "sessionState"):
            if new_auth.get(k) is not None:
                auth[k] = new_auth[k]

        now = _now_ms()
        auth["lastRefreshTime"] = now
        if new_auth.get("expiresAt"):
            auth["expiresAt"] = int(new_auth["expiresAt"])
        elif new_auth.get("expiresIn"):
            auth["expiresAt"] = now + int(new_auth["expiresIn"]) * 1000
        if new_auth.get("refreshExpiresAt"):
            auth["refreshExpiresAt"] = int(new_auth["refreshExpiresAt"])
        elif new_auth.get("refreshExpiresIn"):
            auth["refreshExpiresAt"] = now + int(new_auth["refreshExpiresIn"]) * 1000

        with open(tmp_path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, path)
        return True, "已写回 %s" % os.path.basename(path)
    except Exception as e:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        return False, "写回失败: %s" % e
    finally:
        _release_lock(lock_path)


def ensure_fresh_cred(cred, endpoint, allow_refresh=True):
    """token 邻近/已过期时续期一次。explicit 模式的新 token 不落盘。"""
    exp = 0
    try:
        payload_b64 = cred["token"].split(".")[1]
        payload_b64 += "=" * (-len(payload_b64) % 4)
        exp = json.loads(base64.urlsafe_b64decode(payload_b64)).get("exp") or 0
    except Exception:
        exp = 0
    remaining = exp - time.time() if exp else None
    if remaining is None or remaining > 1800:
        return cred, None
    if not allow_refresh:
        return cred, "token 已过期但已禁用续期（--no-refresh）"
    if not cred.get("refresh"):
        return cred, "token 已过期且没有 refreshToken，只能重新登录客户端"
    ok, info = refresh_session(cred, endpoint)
    if not ok:
        return cred, "自动续期失败（%s）" % info.get("reason")
    new_auth = info["data"]
    cred2 = dict(cred)
    cred2["token"] = new_auth["accessToken"]
    if new_auth.get("refreshToken"):
        cred2["refresh"] = new_auth["refreshToken"]
    if not cred.get("file"):
        return cred2, "已自动续期（显式凭据模式，新 token 仅本次运行生效）"
    if client_running():
        return cred2, "已自动续期（客户端在运行，本次不写回凭据文件）"
    wrote, msg = persist_auth(cred, new_auth)
    if wrote:
        return cred2, "已自动续期并写回凭据文件"
    return cred2, "已自动续期（写回失败：%s，仅在本次运行生效）" % msg


def ok(status, payload):
    return status == 200 and (not isinstance(payload, dict) or payload.get("code") in (0, None))


def auth_failed(status):
    return status in (401, 403)


def call_with_refresh(path, cred, endpoint, allow_refresh=True):
    status, payload = call(path, cred, endpoint)
    if not auth_failed(status):
        return cred, status, payload, None
    cred2, note = ensure_fresh_cred(cred, endpoint, allow_refresh=allow_refresh)
    if cred2.get("token") == cred.get("token"):
        return cred, status, payload, note
    status2, payload2 = call(path, cred2, endpoint)
    return cred2, status2, payload2, note


# ---------------------------------------------------------------- 输出
def fmt_progress(wp):
    if not isinstance(wp, list):
        return ""
    return "".join("\u25cf" if x else "\u25cb" for x in wp)


def disp_width(s):
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
               for ch in str(s))


def pad(s, width):
    return str(s) + " " * max(0, width - disp_width(s))


def _dates(d):
    return sorted({str(x)[:10] for x in (d.get("checkin_dates") or [])})


def gaps(d, days=7):
    """近 days 天（不含今天）里没签到的日期，且只统计活动开始之后。"""
    have = set(_dates(d))
    start = str(d.get("start_time") or "")[:10]
    today = datetime.date.today()
    out = []
    for i in range(1, days + 1):
        s = (today - datetime.timedelta(days=i)).isoformat()
        if s not in have and (not start or s >= start):
            out.append(s)
    return sorted(out)


def recent_bar(d, days=7):
    """最近 days 天的签到情况，最左为最早一天。"""
    have = set(_dates(d))
    today = datetime.date.today()
    return "".join(
        "\u25cf" if (today - datetime.timedelta(days=days - 1 - i)).isoformat() in have
        else "\u25cb" for i in range(days))


def render(d):
    """人类可读状态。保持原有的「累计积分 / 今日积分」行，守卫依赖它们解析。"""
    name = d.get("activity_name") or d.get("theme_name") or "未知活动"
    theme = d.get("theme_name")
    title = name if not theme or theme == name else "%s（%s）" % (name, theme)

    bonus = ""
    if d.get("streak_bonus_credit"):
        bonus = "+%s 积分（连签 %s 天）" % (
            d.get("streak_bonus_credit"), d.get("streak_bonus_days") or "-")
    elif d.get("is_streak_day"):
        bonus = "今日为连签奖励日"
    elif d.get("next_streak_day"):
        bonus = "再签 %s 天可得连签奖励" % d.get("next_streak_day")

    rows = [
        ("活动", title),
        ("期数", "第 %s 期" % d.get("season") if d.get("season") is not None else None),
        ("时间范围", "%s ~ %s" % (d.get("start_time"), d.get("end_time"))
            if d.get("start_time") else None),
        ("已签到天数", "%s（本周 %s 天）" % (d.get("streak_days"), d.get("week_checkin_days"))),
        ("累计积分", d.get("total_credits")),
        ("今日积分", d.get("today_credit")),
        ("本周进度", fmt_progress(d.get("week_progress")) or None),
        ("连签奖励", bonus or None),
        ("最近 7 天", recent_bar(d) if _dates(d) else None),
    ]
    for k, v in rows:
        if v not in (None, ""):
            log("%s: %s" % (pad(k, 12), v))


def render_report(d, days=30):
    """周报：本周进度、近 N 天签到/漏签、连签与积分。"""
    have = set(_dates(d))
    start = str(d.get("start_time") or "")[:10]
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    week = [(monday + datetime.timedelta(days=i)).isoformat() for i in range(7)]
    week_done = [s for s in week if s in have]
    window = [(today - datetime.timedelta(days=i)).isoformat()
              for i in range(days - 1, -1, -1)]
    window = [s for s in window if not start or s >= start]
    done = [s for s in window if s in have]
    missed = [s for s in window if s not in have]
    log("%s: %s ~ %s" % (pad("本周", 12), week[0], week[-1]))
    log("%s: %s/%s 天  %s" % (pad("本周已签", 12), len(week_done), 7,
                              fmt_progress([s in have for s in week])))
    log("%s: 已签 %s 天，未签 %s 天（%s%%）" % (
        pad("近 %s 天" % len(window), 12), len(done), len(missed),
        round(100.0 * len(done) / len(window)) if window else 0))
    if missed:
        log("%s: %s" % (pad("未签日期", 12), ", ".join(missed)))
    log("%s: %s" % (pad("连续签到", 12), d.get("streak_days")))
    log("%s: %s" % (pad("累计积分", 12), d.get("total_credits")))
    g = gaps(d, 7)
    if g:
        log("[WARN] 近 7 天有 %s 天未签到：%s" % (len(g), ", ".join(g)))


def warn_gaps(d):
    g = gaps(d, 7)
    if g:
        log("[WARN] 近 7 天有 %s 天未签到：%s（可用 --report 看完整周报）"
            % (len(g), ", ".join(g)))


# ---------------------------------------------------------------- 主流程
def main():
    ap = argparse.ArgumentParser(description="WorkBuddy 每日签到领积分")
    ap.add_argument("--status", action="store_true", help="只查询状态，不领取")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出状态")
    ap.add_argument("--report", action="store_true", help="签到周报（含漏签日）")
    ap.add_argument("--accounts", action="store_true", help="列出本机可用账号 uid")
    ap.add_argument("--uid", help="指定签到账号 uid（等价 WB_UID）")
    ap.add_argument("--force", action="store_true", help="强制调用领取接口（调试）")
    ap.add_argument("--no-refresh", action="store_true", help="禁止自动续期")
    args = ap.parse_args()

    if args.accounts:
        found, tried = list_accounts()
        log("[INFO] 本机凭据目录中的账号（不显示任何 token）：")
        for uid, rec in sorted(found.items(), key=lambda x: -x[1]["mtime"]):
            ts = datetime.datetime.fromtimestamp(rec["mtime"]).strftime("%Y-%m-%d %H:%M")
            log("  %s  文件 %s 个，最近 %s" % (uid, rec["count"], ts))
        if not found:
            log("  (未找到凭据文件；已尝试：%s)" % "; ".join(tried))
        log("  用 --uid <uid> 或 WB_UID 固定账号，避免客户端切换账号后签错人。")
        return 0

    try:
        endpoint = resolve_endpoint()
    except ValueError as e:
        log("[FAIL] endpoint 校验失败：%s" % redact(e))
        return 1

    uid = args.uid or os.environ.get("WB_UID")
    try:
        cred, mode = resolve_cred(uid=uid)
    except Exception as e:
        log("[FAIL] 凭据加载失败：%s" % redact(e))
        return 1

    allow_refresh = not args.no_refresh
    cred, status, payload, note = call_with_refresh(
        STATUS_PATH, cred, endpoint, allow_refresh=allow_refresh)
    if note:
        log("[INFO] %s" % note)

    if not ok(status, payload):
        if auth_failed(status):
            log("[FAIL] 鉴权失败（HTTP %s），accessToken 已过期且无法自动续期。" % status)
            log("       请打开一次 WorkBuddy 客户端刷新登录态，或重新提供有效凭据。")
            return 1
        log("[FAIL] 查询状态失败 HTTP %s：%s" % (status, redact(str(payload)[:300])))
        return 1

    data = (payload or {}).get("data") or {}

    if args.json:
        out = dict(data)
        out["_meta"] = {
            "uid": cred.get("uid"), "mode": mode, "endpoint": endpoint,
            "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        }
        out["_gaps_7d"] = gaps(data, 7)
        out["_recent_7d"] = recent_bar(data)
        log(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    if args.report:
        render_report(data)
        log("[INFO] 周报模式，未执行领取。")
        return 0

    active = data.get("active", True)
    checked = data.get("today_checked_in", False)

    if args.status:
        render(data)
        warn_gaps(data)
        log("[INFO] 仅查询模式，未执行领取。")
        return 0

    if checked and not args.force:
        render(data)
        warn_gaps(data)
        log("[SKIP] 今天已经领过了，无需重复领取（今日 +%s 积分）" % data.get("today_credit"))
        return 0

    if not active and not args.force:
        render(data)
        log("[SKIP] 当前没有进行中的签到活动。")
        return 0

    cred, status2, payload2, note2 = call_with_refresh(
        CLAIM_PATH, cred, endpoint, allow_refresh=allow_refresh)
    if note2 and note2 != note:
        log("[INFO] %s" % note2)
    if not ok(status2, payload2):
        if auth_failed(status2):
            log("[FAIL] 领取失败，鉴权失效（HTTP %s）。请重新提供有效凭据。" % status2)
            return 1
        log("[FAIL] 领取接口异常 HTTP %s：%s" % (status2, redact(str(payload2)[:300])))
        return 1

    # 复查，用服务端权威状态汇报
    status3, payload3 = call(STATUS_PATH, cred, endpoint)
    if ok(status3, payload3):
        data = (payload3 or {}).get("data") or data

    render(data)
    if data.get("today_checked_in"):
        log("[OK] 领取成功！本次 +%s 积分，累计 %s。"
            % (data.get("today_credit"), data.get("total_credits")))
        return 0

    log("[FAIL] 接口返回成功但状态仍为未签到，请检查活动规则或稍后重试。")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
