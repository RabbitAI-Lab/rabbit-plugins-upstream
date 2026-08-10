#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: B站 + 贴吧 Cookie 配置向导（写入 config/cookies.json）。

用法:
    python config_cookies.py                              # 交互式向导
    python config_cookies.py --bili-cookie "SESSDATA=...; bili_jct=..." --tieba-cookie "BDUSS=..."
    python config_cookies.py --status                      # 查看当前配置与有效性
    python config_cookies.py --clear                       # 清空 cookie 配置

获取方式:
- B站: 登录 bilibili.com → F12 → Network → 刷新页面 → 点任意 api.bilibili.com 请求
       → 复制 Request Headers 里的 Cookie 整段
- 贴吧: 登录 tieba.baidu.com → 同上操作

安全提示: cookie 等同账号凭证, 文件权限尽量收紧; 勿提交到仓库。
"""
import sys
import json
import urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import common


def check_bili(cookie: str) -> dict:
    """验证 B站 cookie: nav API 返回 0 + uname 即有效。"""
    if not cookie:
        return {"ok": False, "msg": "未提供"}
    try:
        d = json.loads(common.fetch(
            "https://api.bilibili.com/x/web-interface/nav",
            cookie=cookie))
        if d.get("code") == 0 and (d.get("data") or {}).get("isLogin"):
            return {"ok": True, "msg": f"已登录: {(d['data'] or {}).get('uname')}"}
        return {"ok": False, "msg": f"登录态无效 (code={d.get('code')})，cookie 可能过期"}
    except Exception as e:
        return {"ok": False, "msg": f"请求失败: {e}"}


def check_tieba(cookie: str) -> dict:
    """验证贴吧 cookie: c.tieba frs/page 返回 error_code=0 即有效。"""
    if not cookie:
        return {"ok": False, "msg": "未提供"}
    try:
        body = common.fetch(
            "https://c.tieba.baidu.com/c/f/frs/page?kw=%E7%BD%91%E7%BB%9C%E6%A2%97&rn=5",
            referer="", cookie=cookie, mobile=True)
        d = json.loads(body)
        ec = d.get("error_code")
        if ec == 0:
            name = (d.get("forum") or {}).get("name", "")
            return {"ok": True, "msg": f"有效 (访问吧: {name})"}
        return {"ok": False, "msg": f"error_code={ec} ({d.get('error_msg')})，cookie 可能过期"}
    except Exception as e:
        return {"ok": False, "msg": f"请求失败: {e}"}


def interactive() -> None:
    print("=" * 56)
    print("Meme-Digger Cookie 配置向导")
    print("B站: 登录 bilibili.com → F12 → Network → 复制请求头 Cookie")
    print("贴吧: 登录 tieba.baidu.com → 同上")
    print("直接回车 = 跳过/保持不变")
    print("=" * 56)
    cur = common.load_cookies()
    if cur["bilibili"]:
        print(f"[当前] B站 cookie 已配置: {cur['bilibili'][:24]}...")
    if cur["tieba"]:
        print(f"[当前] 贴吧 cookie 已配置: {cur['tieba'][:24]}...")
    bili = input("粘贴 B站 Cookie (回车跳过): ").strip() or None
    tieba = input("粘贴 贴吧 Cookie (回车跳过): ").strip() or None
    bili = bili if bili else cur["bilibili"] or None
    tieba = tieba if tieba else cur["tieba"] or None
    if not bili and not tieba:
        print("!! 未提供任何 cookie，未修改配置。")
        return
    print("\n验证中...")
    if bili:
        r = check_bili(bili)
        print(f"B站 : {'✅' if r['ok'] else '❌'} {r['msg']}")
    if tieba:
        r = check_tieba(tieba)
        print(f"贴吧: {'✅' if r['ok'] else '❌'} {r['msg']}")
    common.save_cookies(bili=bili, tieba=tieba)
    print(f"\n已写入 {common.CONFIG_FILE}")


def show_status() -> None:
    cur = common.load_cookies()
    print("== 当前配置状态 ==")
    if cur["bilibili"]:
        r = check_bili(cur["bilibili"])
        print(f"B站 : {'✅' if r['ok'] else '❌'} {r['msg']}")
    else:
        print("B站 : 未配置")
    if cur["tieba"]:
        r = check_tieba(cur["tieba"])
        print(f"贴吧: {'✅' if r['ok'] else '❌'} {r['msg']}")
    else:
        print("贴吧: 未配置")
    print(f"\n配置文件: {common.CONFIG_FILE}")


def main():
    args = sys.argv[1:]
    if "--status" in args:
        show_status()
        return
    if "--clear" in args:
        common.save_cookies(bili="", tieba="")
        print("已清空 cookie 配置。")
        return
    bili = tieba = None
    i = 0
    while i < len(args):
        if args[i] == "--bili-cookie" and i + 1 < len(args):
            bili, i = args[i + 1], i + 1
        elif args[i] == "--tieba-cookie" and i + 1 < len(args):
            tieba, i = args[i + 1], i + 1
        i += 1
    if bili or tieba:
        ok_bili, ok_tieba = None, None
        print("验证中...")
        if bili:
            r = check_bili(bili)
            ok_bili = r["ok"]
            print(f"B站 : {'✅' if r['ok'] else '❌'} {r['msg']}")
        if tieba:
            r = check_tieba(tieba)
            ok_tieba = r["ok"]
            print(f"贴吧: {'✅' if r['ok'] else '❌'} {r['msg']}")
        # 仅保存验证通过的项；失败的打印提示（用户可 --force 强存）
        save_bili = bili if ok_bili else None
        save_tieba = tieba if ok_tieba else None
        if not save_bili and not save_tieba:
            print("!! 没有验证通过的 cookie，未写入配置。")
            return
        common.save_cookies(bili=save_bili, tieba=save_tieba)
        print(f"\n已写入 {common.CONFIG_FILE}（仅保存验证通过的项）")
        return
    interactive()


if __name__ == "__main__":
    main()
