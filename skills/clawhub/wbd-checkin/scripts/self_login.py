#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本人账号自助登录：手机端无需电脑即可取得凭据。

设计约束（这个文件的关键在于约束，而不是功能）：
  * 号码必须先用 --bind 绑一次，绑定后所有请求只认这一个号码，脚本没有 --phone 入参
  * 本地限频：两次发送间隔 >= 120 秒，每天最多 3 次
  * 只请求平台自己的登录接口，无转发、无备用域、无多账号、无批量
  * 不打印号码全量与凭据内容

用法：
    python3 scripts/self_login.py --bind 13xxxxxxxxx   # 一次性绑定本人号码
    python3 scripts/self_login.py --send               # 向已绑定号码请求验证码
    python3 scripts/self_login.py --code 123456        # 用验证码换凭据并写入 config.json
    python3 scripts/self_login.py --status             # 查看绑定与限频状态
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wbcfg as wb  # noqa: E402

WEB_HOST = "https://www.workbuddy.cn"
PATH_SEND = "/v2/plugin/login/send-sms"
PATH_TOKEN = "/v2/plugin/login/token"

SEND_GAP_SEC = 120          # 两次发送最小间隔
SEND_DAILY_MAX = 3          # 每日上限
STATE_KEY = "self_login"


def mask_phone(p):
    p = (p or "").strip()
    return "%s****%s" % (p[:3], p[-4:]) if len(p) == 11 else "未绑定"


def post_json(url, body):
    req = urllib.request.Request(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "wb-checkin/3.3",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=wb.TIMEOUT) as resp:
            raw = resp.read().decode("utf-8", "ignore")
            code = resp.status
    except urllib.error.HTTPError as e:
        raw = ""
        try:
            raw = e.read().decode("utf-8", "ignore")[:200]
        except Exception:
            pass
        return e.code, {"_raw": raw}
    except Exception as e:
        return 0, {"_err": str(e)}
    try:
        return code, json.loads(raw) if raw else {}
    except Exception:
        return code, {"_raw": raw[:200]}


def bounded_phone():
    """取出已绑定号码；没绑就返回 None。这是唯一的号码来源。"""
    p = (wb.read_conf().get("owner_phone") or "").strip()
    return p if (p.isdigit() and len(p) == 11) else None


def quota_check():
    """返回 (可否发送, 说明)。"""
    st = wb.load_state().get(STATE_KEY) or {}
    now = time.time()
    last = float(st.get("last_send_ts") or 0)
    today = wb.now_cn().strftime("%Y-%m-%d")
    used = int(st.get("day_count") or 0) if st.get("day") == today else 0

    if now - last < SEND_GAP_SEC:
        return False, "发送太频繁，请等 %d 秒后再试" % int(SEND_GAP_SEC - (now - last))
    if used >= SEND_DAILY_MAX:
        return False, "今日已达 %d 次上限，明天再试" % SEND_DAILY_MAX
    return True, "今日已用 %d/%d 次" % (used, SEND_DAILY_MAX)


def quota_mark():
    st = wb.load_state()
    cur = st.get(STATE_KEY) or {}
    today = wb.now_cn().strftime("%Y-%m-%d")
    used = int(cur.get("day_count") or 0) if cur.get("day") == today else 0
    st[STATE_KEY] = {"last_send_ts": time.time(), "day": today, "day_count": used + 1}
    wb.save_state(st)


def cmd_bind(phone):
    phone = (phone or "").strip()
    if not (phone.isdigit() and len(phone) == 11):
        print("号码格式不对，应为 11 位手机号")
        return 1
    old = bounded_phone()
    if old and old != phone:
        print("已绑定 %s。换号请先执行 --unbind" % mask_phone(old))
        return 1
    ok, info = wb.write_conf({"owner_phone": phone})
    if not ok:
        print("写入失败：%s" % info)
        return 1
    print("已绑定 %s。之后所有请求只发给这个号码，脚本不接受其他号码。" % mask_phone(phone))
    print("注意：请只绑定你本人的号码。")
    return 0


def cmd_unbind():
    ok, info = wb.remove_conf()
    print("已解除绑定并清除凭据" if ok else "清除失败：%s" % info)
    return 0 if ok else 1


def cmd_send():
    phone = bounded_phone()
    if not phone:
        print("还没有绑定号码。先执行：python3 scripts/self_login.py --bind 你的手机号")
        return 1
    can, why = quota_check()
    if not can:
        print(why)
        return 1
    print("正在向 %s 请求验证码…" % mask_phone(phone))
    code, resp = post_json(WEB_HOST + PATH_SEND, {"phone": phone})
    if resp.get("_err"):
        print("请求失败：%s" % resp["_err"])
        return 1
    if resp.get("code") in (0, 200):
        quota_mark()
        print("已发出，5 分钟内有效（%s）" % why)
        print("收到后执行：python3 scripts/self_login.py --code 六位验证码")
        return 0
    detail = resp.get("msg") or resp.get("message") or resp.get("_raw") or ""
    print("发送失败 HTTP %s code=%s %s" % (code, resp.get("code"), str(detail)[:120]))
    return 1


def cmd_code(sms_code):
    sms_code = (sms_code or "").strip()
    phone = bounded_phone()
    if not phone:
        print("还没有绑定号码，无法登录。先 --bind")
        return 1
    if not (sms_code.isdigit() and len(sms_code) == 6):
        print("验证码应为 6 位数字")
        return 1
    status, resp = post_json(
        WEB_HOST + PATH_TOKEN,
        {"login_method": "phone", "phone": phone, "sms_code": sms_code},
    )
    if resp.get("_err"):
        print("请求失败：%s" % resp["_err"])
        return 1
    if resp.get("code") not in (0, 200):
        detail = resp.get("msg") or resp.get("message") or resp.get("_raw") or ""
        print("登录未通过 HTTP %s %s" % (status, str(detail)[:120]))
        return 2

    at = wb.dig(resp, "accessToken", "access_token", "token")
    rt = wb.dig(resp, "refreshToken", "refresh_token")
    uid = wb.dig(resp, "uid", "userId", "user_id")
    exp = wb.dig(resp, "expiresAt", "expires_at", "expireAt")
    if not wb.is_set(at):
        print("响应里没有访问凭据，未写入任何内容")
        return 1

    updates = {"access_token": at, "domain": wb.SITE_DOMAIN,
               "login_at": wb.now_cn().isoformat(timespec="seconds")}
    if wb.is_set(rt):
        updates["renew_key"] = rt
    if wb.is_set(uid):
        updates["uid"] = str(uid)
    if exp:
        updates["expires_at"] = wb.norm_exp(exp)
    ok, info = wb.write_conf(updates)
    if not ok:
        print("写入失败：%s" % info)
        return 1

    print("登录成功，凭据已写入 %s" % info)
    print("有效期：%s" % wb.exp_text(exp))
    print("自动续期：%s" % ("已具备，之后每天跑签到会自动延长" if wb.is_set(rt) else "未取得，到期需重新登录"))
    print("下一步：python3 scripts/checkin.py")
    return 0


def cmd_status():
    phone = bounded_phone()
    conf = wb.read_conf()
    print("绑定号码：%s" % mask_phone(phone or ""))
    print("访问凭据：%s" % ("已录入" if wb.is_set(conf.get("access_token")) else "未录入"))
    print("续期凭据：%s" % ("已录入" if wb.is_set(conf.get("renew_key")) else "未录入"))
    print("有效期：%s" % wb.exp_text(conf.get("expires_at")))
    can, why = quota_check()
    print("今日额度：%s" % why)
    return 0


def main():
    ap = argparse.ArgumentParser(description="本人账号自助登录（凭据取回，移动端优先）")
    ap.add_argument("--bind", metavar="PHONE", help="一次性绑定本人手机号")
    ap.add_argument("--unbind", action="store_true", help="解除绑定并清除凭据")
    ap.add_argument("--send", action="store_true", help="向已绑定号码请求验证码")
    ap.add_argument("--code", metavar="CODE", help="用验证码换凭据")
    ap.add_argument("--status", action="store_true", help="查看绑定与额度")
    a = ap.parse_args()

    if a.bind:
        return cmd_bind(a.bind)
    if a.unbind:
        return cmd_unbind()
    if a.send:
        return cmd_send()
    if a.code:
        return cmd_code(a.code)
    if a.status:
        return cmd_status()
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
