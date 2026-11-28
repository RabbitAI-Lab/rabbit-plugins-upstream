#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""配置读写与请求工具。

安全约定（本文件所有代码都遵守）：
  * 只向 WorkBuddy 官方服务地址发送请求，不做任何第三方转发、不做跨域重试
  * 只使用用户本人主动粘贴的凭据，不扫描、不读取、不解密本机任何登录数据
  * 凭据只保存在本技能目录内，文件权限 0600，随时可一键清除
  * 不支持多账号、不支持批量，只服务当前用户自己的账号
  * 不打印凭据内容，任何输出都不含凭据片段
"""

import json
import os
import stat
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
TIMEOUT = 20
CN_TZ = timezone(timedelta(hours=8))

# 官方服务地址
HOST = "https://copilot.tencent.com"
PATH_STATUS = "/v2/billing/meter/checkin-activity-status"
PATH_CLAIM = "/v2/billing/meter/daily-checkin"
PATH_RENEW = "/v2/plugin/auth/token/refresh"
SITE_DOMAIN = "www.codebuddy.cn"

# 凭据唯一位置：本技能目录
CONF = SKILL_DIR / "config.json"
STATE = HERE / "last_checkin.json"

TOKEN_FIELDS = ("access_token",)
UID_FIELDS = ("uid",)


def now_cn():
    return datetime.now(CN_TZ)


def log(msg):
    print("[%s] %s" % (now_cn().strftime("%Y-%m-%d %H:%M:%S"), msg), flush=True)


def is_set(v):
    v = (v or "").strip() if isinstance(v, str) else ""
    if not v:
        return False
    return not any(m in v.upper() for m in ("PASTE_", "YOUR_", "CHANGEME"))


def norm_exp(v):
    """秒或毫秒时间戳统一为毫秒。"""
    try:
        v = int(v)
    except Exception:
        return 0
    if not v:
        return 0
    return v * 1000 if 0 < v < 1e12 else v


def exp_text(ms):
    ms = norm_exp(ms)
    if not ms:
        return "未知"
    dt = datetime.fromtimestamp(ms / 1000)
    return "%s（剩 %d 天）" % (dt.strftime("%Y-%m-%d %H:%M"), (dt - datetime.now()).days)


def exp_days_left(ms):
    ms = norm_exp(ms)
    if not ms:
        return None
    return (datetime.fromtimestamp(ms / 1000) - datetime.now()).days


# ---------------------------------------------------------------- 配置文件

def read_conf(path=None):
    p = Path(path) if path else CONF
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def write_conf(updates):
    """合并写入，权限 0600。

    只写本技能目录下的 config.json 这一个位置。
    返回 (是否成功, 路径或错误说明)。
    """
    try:
        CONF.parent.mkdir(parents=True, exist_ok=True)
        merged = read_conf()
        for k, v in updates.items():
            if v not in (None, ""):
                merged[k] = v
        tmp = CONF.with_name(CONF.name + ".tmp")
        tmp.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, CONF)
        try:
            os.chmod(CONF, stat.S_IRUSR | stat.S_IWUSR)
        except Exception:
            pass
        return True, str(CONF)
    except Exception as e:
        return False, "%s: %s" % (CONF, e)


def remove_conf():
    try:
        if CONF.exists():
            CONF.unlink()
            return True, "已删除 %s" % CONF
    except Exception as e:
        return False, "删除失败: %s" % e
    return True, "本技能目录下没有配置，无需清除"


def load_state():
    try:
        with open(STATE, "r", encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def save_state(d):
    try:
        STATE.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass


# ---------------------------------------------------------------- 请求

def post(path, body=None, token=None, uid=None, domain=None):
    """向官方地址发一次 POST，返回 (status_code, 解析后的 dict)。

    只接受相对路径，防止被改造成任意地址请求。
    不重试、不换域名、不收发凭据到其他地方。
    """
    import urllib.error
    import urllib.request

    if not path.startswith("/"):
        raise ValueError("仅支持站内相对路径")

    url = HOST + path
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Domain": domain or SITE_DOMAIN,
        "User-Agent": "wb-checkin/3.0",
    }
    if token:
        headers["Authorization"] = "Bearer %s" % token
    if uid:
        headers["X-User-Id"] = uid

    data = json.dumps(body or {}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read().decode("utf-8", "ignore")
            code = resp.status
    except urllib.error.HTTPError as e:
        raw = ""
        try:
            raw = e.read().decode("utf-8", "ignore")
        except Exception:
            pass
        code = e.code
    try:
        return code, json.loads(raw) if raw else {}
    except Exception:
        return code, {}


def dig(obj, *names):
    """在响应对象的两层固定结构里取一个字段值（不递归、不遍历未知结构）。"""
    if not isinstance(obj, dict):
        return None
    want = {n.lower() for n in names}
    layers = [obj]
    for sub in ("data", "result", "payload"):
        v = obj.get(sub)
        if isinstance(v, dict):
            layers.append(v)
    for layer in layers:
        for k, v in layer.items():
            if k.lower() in want and v not in (None, ""):
                return v
    return None


def dig_int(obj, *names):
    v = dig(obj, *names)
    try:
        return int(v)
    except Exception:
        return None


def ok_code(resp):
    return resp.get("code") in (0, 200, "0", "200") if isinstance(resp, dict) else False


def renew_session(conf, domain=None):
    """用手里的续期凭据，向官方地址换一组新的访问凭据。

    仅在用户主动录入过续期凭据（renew_key）时调用。
    单次请求，不重试、不换地址、不做多份凭据轮替。

    返回 (需要写回配置的字段 dict 或 None, 说明)。
    """
    import urllib.error
    import urllib.request

    key = (conf.get("renew_key") or "").strip()
    if not is_set(key):
        return None, "没有续期凭据"

    req = urllib.request.Request(
        HOST + PATH_RENEW,
        data=b"{}",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Refresh-Token": key,
            "X-Auth-Refresh-Source": "plugin",
            "X-Domain": domain or conf.get("domain") or SITE_DOMAIN,
            "User-Agent": "wb-checkin/3.2",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", "ignore")[:100]
        except Exception:
            pass
        return None, "HTTP %s %s" % (e.code, body)
    except Exception as e:
        return None, "网络异常: %s" % e

    try:
        obj = json.loads(raw) if raw else {}
    except Exception:
        return None, "响应无法解析"

    if not ok_code(obj):
        return None, "code=%s" % (obj.get("code") if isinstance(obj, dict) else "?")

    at = dig(obj, "accessToken", "access_token", "token")
    if not is_set(at):
        return None, "响应缺少访问凭据"

    out = {"access_token": at}
    nk = dig(obj, "refreshToken", "refresh_token")
    if is_set(nk):
        out["renew_key"] = nk
    exp = dig(obj, "expiresAt", "expires_at", "expireAt")
    if exp:
        out["expires_at"] = norm_exp(exp)
    got_uid = dig(obj, "uid", "userId", "user_id")
    if is_set(got_uid) and not is_set(conf.get("uid")):
        out["uid"] = str(got_uid)
    out["renewed_at"] = now_cn().isoformat(timespec="seconds")
    return out, "已延长有效期"
