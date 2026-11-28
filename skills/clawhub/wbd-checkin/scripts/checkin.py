#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WorkBuddy 每日签到。

流程：读取本技能目录下的配置 → 若录入过续期凭据则先延长有效期
      → 查询今日签到状态 → 未签到则领取 → 回报结果。

安全约定：
  * 只向 WorkBuddy 官方服务地址发送请求，不向任何第三方转发
  * 只使用用户本人主动粘贴的凭据，不读取本机登录数据
  * 不打印凭据内容；只保存一组凭据，不做多份备份
  * 只操作用户本人的一个账号，不支持批量

退出码：
  0  签到成功，或今日已签到（幂等跳过）
  1  网络/服务异常，可稍后重试
  2  未录入凭据，或凭据已失效 → 需要用户重新提供

用法：
    python3 checkin.py               # 签到
    python3 checkin.py --dry-run     # 只看状态，不领取
    python3 checkin.py --force       # 忽略"今日已签"强制领取
    python3 checkin.py status        # 查看最近一次结果
    python3 checkin.py --json        # 机器可读输出
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wbcfg as cfgmod


def emit(payload, as_json, human):
    if as_json:
        import json
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(human)


def renew_once(conf, domain):
    """尝试延长一次有效期。成功则把新凭据写回配置并同步到 conf。

    返回 (是否成功, 原因)。失败不影响后续用现有凭据继续尝试。
    """
    newf, why = cfgmod.renew_session(conf, domain)
    if not newf:
        return False, why
    cfgmod.write_conf(newf)
    conf.update(newf)
    return True, ""


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    dry = "--dry-run" in args
    force = "--force" in args

    if "status" in args:
        st = cfgmod.load_state()
        if not st:
            print("还没有签到记录")
            return 0
        emit(st, as_json, "最近一次：%s %s（%s）" % (
            st.get("at", "-"), st.get("result", "-"), st.get("detail", "-")))
        return 0

    conf = cfgmod.read_conf()
    token = conf.get("access_token", "")
    uid = conf.get("uid", "")
    domain = conf.get("domain", "")
    has_key = cfgmod.is_set(conf.get("renew_key"))

    if not cfgmod.is_set(token):
        msg = "未录入凭据。先执行：python3 setup.py --token '凭据'"
        emit({"ok": False, "result": "CREDENTIALS_MISSING", "detail": msg},
             as_json, "❌ " + msg)
        return 2

    # 0. 录入过续期凭据时，每次运行先延长一次有效期。
    #    每天跑一次，链条就不会断，不需要用户反复录入。
    renewed = False
    if has_key:
        renewed, why = renew_once(conf, domain)
        if renewed:
            token = conf.get("access_token", token)
            domain = conf.get("domain", domain)
            cfgmod.log("有效期已延长至 %s" % cfgmod.exp_text(conf.get("expires_at", 0)))
        else:
            cfgmod.log("延长有效期未成功（%s），改用现有凭据尝试" % why)

    exp = cfgmod.exp_days_left(conf.get("expires_at", 0))
    if exp is not None and exp < 0 and not has_key:
        msg = "凭据已过期（%s）。请重新录入：python3 setup.py --token '凭据'" % cfgmod.exp_text(conf.get("expires_at", 0))
        emit({"ok": False, "result": "CREDENTIALS_EXPIRED", "detail": msg},
             as_json, "❌ " + msg)
        return 2

    # 1. 查询今日状态
    code, resp = cfgmod.post(cfgmod.PATH_STATUS, {}, token, uid, domain)

    # 首次就 401/403，且手里有续期凭据但刚才没续成 → 再试一次续期后重查
    if code in (401, 403) and has_key and not renewed:
        if renew_once(conf, domain)[0]:
            token = conf.get("access_token", token)
            domain = conf.get("domain", domain)
            code, resp = cfgmod.post(cfgmod.PATH_STATUS, {}, token, uid, domain)

    if code in (401, 403):
        msg = "凭据已失效（HTTP %s）。请重新录入：python3 setup.py --token '凭据'" % code
        cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                           "result": "CREDENTIALS_INVALID", "detail": msg})
        emit({"ok": False, "result": "CREDENTIALS_INVALID", "detail": msg},
             as_json, "❌ " + msg)
        return 2

    if code != 200 or not isinstance(resp, dict):
        msg = "查询状态失败（HTTP %s），可稍后重试" % code
        cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                           "result": "FAIL", "detail": msg})
        emit({"ok": False, "result": "FAIL", "detail": msg}, as_json, "❌ " + msg)
        return 1

    # 接口若带回用户标识而本地尚未记录，补写一次（避免让用户手填 uid）
    if not cfgmod.is_set(uid):
        got = cfgmod.dig(resp, "uid", "userId", "user_id", "accountId")
        if got:
            uid = str(got)
            cfgmod.write_conf({"uid": uid})

    data = resp.get("data") if isinstance(resp.get("data"), dict) else resp
    already = bool(
        data.get("today_checked_in")
        or data.get("todayCheckedIn")
        or data.get("checked_in_today")
    )
    streak = cfgmod.dig_int(resp, "streak_days", "streakDays", "continuous_days",
                            "continuousDays", "streak")
    credit = cfgmod.dig_int(resp, "credit", "credits", "total_credit", "totalCredit",
                            "balance", "score")

    if already and not force:
        msg = "今日已签到%s" % ("，连续 %d 天" % streak if streak else "")
        if dry:
            msg = "[只读] " + msg
        cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                           "result": "SKIP", "detail": msg,
                           "streak_days": streak, "credit": credit})
        emit({"ok": True, "result": "SKIP", "detail": msg, "streak_days": streak,
              "credit": credit, "already": True, "renewed": renewed}, as_json, "✅ " + msg)
        return 0

    if dry:
        msg = "今日未签到%s" % ("，连续 %d 天" % streak if streak else "")
        emit({"ok": True, "result": "READY", "detail": msg, "streak_days": streak,
              "credit": credit, "renewed": renewed}, as_json,
             "ℹ️ [只读] " + msg + "（未领取）")
        return 0

    # 2. 领取今日奖励
    code2, resp2 = cfgmod.post(cfgmod.PATH_CLAIM, {}, token, uid, domain)

    if code2 in (401, 403):
        msg = "凭据已失效（HTTP %s）。请重新录入：python3 setup.py --token '凭据'" % code2
        cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                           "result": "CREDENTIALS_INVALID", "detail": msg})
        emit({"ok": False, "result": "CREDENTIALS_INVALID", "detail": msg},
             as_json, "❌ " + msg)
        return 2

    if code2 != 200:
        msg = "领取失败（HTTP %s），可稍后重试" % code2
        cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                           "result": "FAIL", "detail": msg})
        emit({"ok": False, "result": "FAIL", "detail": msg}, as_json, "❌ " + msg)
        return 1

    gained = cfgmod.dig_int(resp2, "credit", "credits", "gain", "gained", "reward",
                            "amount", "score")
    streak2 = cfgmod.dig_int(resp2, "streak_days", "streakDays", "continuous_days",
                             "continuousDays", "streak") or streak
    total = cfgmod.dig_int(resp2, "total_credit", "totalCredit", "balance", "total")

    parts = ["签到成功"]
    if gained:
        parts.append("本次 +%d" % gained)
    if streak2:
        parts.append("连续 %d 天" % streak2)
    if total:
        parts.append("累计 %d" % total)
    msg = "，".join(parts)

    cfgmod.save_state({"at": cfgmod.now_cn().isoformat(timespec="seconds"),
                       "result": "OK", "detail": msg, "streak_days": streak2,
                       "credit": total or gained})

    emit({"ok": True, "result": "OK", "detail": msg, "gained": gained,
          "streak_days": streak2, "credit": total or gained,
          "already": False, "renewed": renewed}, as_json, "✅ " + msg)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("❌ 运行异常：%s" % e, file=sys.stderr)
        sys.exit(1)
