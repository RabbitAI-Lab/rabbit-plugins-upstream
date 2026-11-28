#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""录入或清除签到凭据。

凭据来自用户本人从 WorkBuddy 网页端复制的 token，脚本只负责保存到本技能目录，
不读取、不扫描、不解密本机任何登录数据。

安全约定：
  * 不打印凭据内容，任何输出都不含凭据片段
  * 只写入本技能目录下的 config.json，权限 0600
  * 可通过 --purge 一次性彻底删除

用法：
    python3 setup.py                                   # 交互式粘贴录入
    python3 setup.py --token '凭据'             # 直接录入
    python3 setup.py --token '凭据' --uid <uid>           # 同时指定用户标识
    python3 setup.py --token '凭据' --expires-at <ts>     # 指定到期时间（秒或毫秒）
    python3 setup.py --check                           # 查看当前状态
    python3 setup.py --guide                           # 查看各设备如何取得凭据
    python3 setup.py --purge                           # 清除凭据
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wbcfg as cfgmod

# 用户复制粘贴时可能带上的前后缀，逐层剥掉
LEAD_STRINGS = (
    "authorization:",
    "authorization=",
    "bearer ",
    "access_token=",
    "accesstoken=",
    "token=",
    "\u0000",
)
TRIM_CHARS = " \t\r\n\"'`;,&"


def _strip_prefix(s):
    """逐层剥掉头/前缀/引号，直到不再变化。"""
    changed = True
    while changed:
        changed = False
        s = s.strip(TRIM_CHARS)
        low = s.lower()
        for pre in LEAD_STRINGS:
            if low.startswith(pre):
                s = s[len(pre):].strip(TRIM_CHARS)
                changed = True
                break
    return s.strip(TRIM_CHARS)


def parse_token(raw):
    """把用户粘贴的内容整理成纯 token。

    手机上复制粘贴很难做到精确，这里容忍常见格式：
    带 Bearer 前缀、带 Authorization 头、被引号包裹、多行、末尾带 shell 符号。
    """
    if not raw:
        return ""
    # 多行粘贴时，优先取最像凭据的那一行；都不像则取第一段有实质内容的行
    lines = [x for x in raw.replace("\r", "\n").split("\n") if x.strip(TRIM_CHARS)]
    if not lines:
        return ""
    pick = ""
    for part in lines:
        if looks_like_token(_strip_prefix(part)):
            pick = part
            break
    if not pick:
        pick = lines[0]
    got = _strip_prefix(pick)

    # 用户可能连整条命令一起复制（curl -H '...'），此时从原文里按形态定位
    if not looks_like_token(got):
        shaped = _longest_token_shape(raw)
        if shaped:
            return shaped
    return got


def looks_like_token(t):
    """形态粗检：真实凭据是两段点号分隔的长串，只由字母数字与点号连字符组成。

    含空格、引号、冒号、花括号的一律不算——那说明整条命令被一起复制了。
    不做强校验，只用于挑选与提醒。
    """
    if not t or len(t) < 40 or t.count(".") < 2:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyz"
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  "0123456789_-.")
    return all(c in allowed for c in t)


def _longest_token_shape(text):
    """在一行文本里找出最长的「三段点号分隔长串」，用于用户连命令一起复制时定位。

    只做字符形态匹配，不解析内容。
    """
    import re
    pat = re.compile(r"[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{4,}")
    found = pat.findall(text or "")
    return max(found, key=len) if found else ""


def ask_guide():
    print("""取得凭据的步骤（只需做一次）

── 在电脑上 ──────────────────────────────
1. 浏览器打开 WorkBuddy 网页版并登录
2. 打开浏览器的开发者工具，切到「网络」面板
3. 在页面上随便点一下（比如刷新或打开签到页），让面板里出现请求
4. 找到发往 WorkBuddy 服务地址的请求，查看它的请求头
5. 复制 Authorization 这一行的值（形如 Bearer eyJhbGciOi...）

── 传到手机 ──────────────────────────────
把刚才复制的内容通过任意方式发给自己：微信文件传输助手、备忘录、隔空投送都行。

── 在手机上录入 ──────────────────────────────
把内容粘贴给助手，说「这是我的凭据」，助手会调用本脚本录入。
或自己执行：

    python3 scripts/setup.py --token '粘贴内容'

粘贴内容不用清洗：带 Bearer 前缀、带引号、带换行都能识别。

──────────────────────────────────────────
下面这一步是可选的，但强烈建议做

只录上面那一串的话，约 28 天后会失效，你得重取一次。
再多录一个「续期凭据」，之后每次运行都会自动延长有效期，
只要不连续一个月不签，就再也不需要重新录入。

1. 仍在网络面板里，找一条发往 .../auth/token/refresh 的请求
   （在页面上停留一会儿、或切到下个页面，这条请求就会出现）
2. 看它的请求头，复制 X-Refresh-Token 这一行的值
3. 录入时一并提供：

    python3 scripts/setup.py --token '凭据' --renew-key '续期凭据'

续期凭据同样只存在本技能目录的 config.json 里，可以随时用 --purge 清除。

── 验证 ──────────────────────────────
    python3 scripts/checkin.py --dry-run     # 只看状态，不领取
    python3 scripts/checkin.py               # 正式签到

注意：手机端无法自行取得这些内容，必须先在电脑上取一次。这不是本技能的限制，
而是它们只存在于浏览器的登录会话中，手机浏览器没有查看它们的入口。""")


def do_check():
    conf = cfgmod.read_conf()
    if not conf:
        print("[状态] 未录入凭据（%s 不存在）" % cfgmod.CONF, file=sys.stderr)
        print("       录入：python3 setup.py --token '凭据'", file=sys.stderr)
        print("       指引：python3 setup.py --guide", file=sys.stderr)
        return 2
    if not cfgmod.is_set(conf.get("access_token")):
        print("[状态] 未录入有效凭据", file=sys.stderr)
        return 2

    print("[状态]   已录入凭据")
    print("[位置]   %s（权限 0600）" % cfgmod.CONF)
    print("[有效期] %s" % cfgmod.exp_text(conf.get("expires_at", 0)))
    if cfgmod.is_set(conf.get("renew_key")):
        print("[续期]   已录入，每次运行会自动延长有效期，无需手动重录")
        if conf.get("renewed_at"):
            print("[上次延长] %s" % conf.get("renewed_at"))
    else:
        print("[续期]   未录入，到期后需手动重新录入（加 --renew-key 可免这一步）")
    if cfgmod.is_set(conf.get("uid")):
        print("[账号]   已记录用户标识：%s" % conf.get("uid"))
    else:
        print("[账号]   未记录用户标识（首次签到成功后会尝试自动补记）")
    days = cfgmod.exp_days_left(conf.get("expires_at", 0))
    if days is not None and days < 3:
        print("[提醒]   凭据将在 %d 天内过期，到期后需重新录入" % max(days, 0))
    return 0


def do_purge():
    ok, msg = cfgmod.remove_conf()
    print("[清除] %s" % msg, file=sys.stdout if ok else sys.stderr)
    if ok:
        print("[提示] 如需彻底失效，请同时在 WorkBuddy 客户端退出登录。")
    return 0 if ok else 2


def read_stdin():
    """交互式录入：从标准输入读一次粘贴内容。"""
    if sys.stdin.isatty():
        print("请粘贴凭据内容后回车（输入内容不会回显在提示里）：")
    try:
        return sys.stdin.readline()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser(description="录入 WorkBuddy 签到凭据")
    ap.add_argument("--token", help="accessToken（可直接粘贴带 Bearer 前缀的整行）")
    ap.add_argument("--renew-key", dest="renew_key",
                    help="续期凭据（可选；录入后每次运行自动延长有效期）")
    ap.add_argument("--uid", help="用户标识（可选，首次签到成功会自动补记）")
    ap.add_argument("--expires-at", dest="exp", help="到期时间戳，秒或毫秒（可选）")
    ap.add_argument("--check", action="store_true", help="查看当前录入状态")
    ap.add_argument("--guide", action="store_true", help="查看各设备如何取得凭据")
    ap.add_argument("--purge", action="store_true", help="清除已保存的凭据")
    a = ap.parse_args()

    if a.guide:
        ask_guide()
        return 0
    if a.check:
        return do_check()
    if a.purge:
        return do_purge()

    raw = a.token if a.token is not None else read_stdin()
    token = parse_token(raw)

    if not cfgmod.is_set(token):
        print("[错误] 未提供有效凭据。\n"
              "       用法：python3 setup.py --token '凭据'\n"
              "       不确定怎么取：python3 setup.py --guide",
              file=sys.stderr)
        return 2

    if not looks_like_token(token):
        print("[提醒] 这段内容看起来不像完整凭据（常见为两段点号分隔的长串）。\n"
              "       仍然尝试保存；若签到报 401，请重新复制完整的一行。",
              file=sys.stderr)

    updates = {"access_token": token, "domain": cfgmod.SITE_DOMAIN}
    if cfgmod.is_set(a.renew_key):
        updates["renew_key"] = parse_token(a.renew_key)
    if cfgmod.is_set(a.uid):
        updates["uid"] = parse_token(a.uid)
    if a.exp:
        updates["expires_at"] = cfgmod.norm_exp(a.exp)

    ok, where = cfgmod.write_conf(updates)
    if not ok:
        print("[错误] 写入失败：%s" % where, file=sys.stderr)
        return 2

    print("[已写入] %s（权限 0600）" % where)
    print("[有效期] %s" % cfgmod.exp_text(cfgmod.read_conf().get("expires_at", 0)))
    if cfgmod.is_set(a.renew_key):
        print("[续期]   已录入，之后每次运行会自动延长有效期")
    else:
        print("[续期]   未录入，约 28 天后需重新录入；想免掉可加 --renew-key")
    if not cfgmod.is_set(a.uid):
        print("[账号]   未提供用户标识；若签到报 401，请用 --uid 补一个")
    print("[下一步] 执行 python3 checkin.py --dry-run 验证凭据可用")
    return 0


if __name__ == "__main__":
    sys.exit(main())
