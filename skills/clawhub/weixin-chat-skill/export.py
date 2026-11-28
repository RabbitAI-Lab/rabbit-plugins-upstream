"""非交互 CLI（脚本化用）。交互式小程序请运行 wechat_export.py。

    python export.py --list                 列出会话
    python export.py --once [--targets a,b]  导出一次（默认全部会话；targets 为显示名/wxid 子串）
    python export.py [--targets a,b]         导出后进入实时监听
    python export.py --account <wxid>        指定账号（默认自动选第一个）
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import wxread
import exporter

HERE = Path(__file__).resolve().parent


def _arg(name, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return default


def pick_account(wxid: str | None):
    accts = wxread.find_accounts()
    if not accts:
        sys.exit("找不到薇芯账号，请先启动并登录薇芯。")
    if wxid:
        for a in accts:
            if a["wxid"] == wxid:
                return a
        sys.exit(f"未找到账号 {wxid}")
    return accts[0]


def main():
    acct = pick_account(_arg("--account"))
    keys_file = HERE / "keys" / f"{acct['wxid']}.json"
    keys = wxread.load_keys(keys_file)
    if not keys:
        sys.exit(f"账号 {acct['wxid']} 无密钥（{keys_file}）。请先运行 capture_keys.py 或 wechat_export.py 抓取。")
    tmp = wxread.make_tmp_dir()
    contacts = wxread.build_contacts(acct["db_dir"], keys, tmp)
    me = acct["wxid"]
    convs = wxread.scan_conversations(acct["db_dir"], keys, contacts, tmp)

    if "--list" in sys.argv:
        pw = wxread.pad_width
        for i, c in enumerate(convs, 1):
            last = datetime.fromtimestamp(c["last_time"]).strftime("%Y-%m-%d %H:%M") if c["last_time"] else "-"
            print(f"{pw(str(i), 3, 'right')}. {pw(c['display'], 24)} {pw(c['kind'], 12)} "
                  f"{pw(str(c['count']), 6, 'right')}条 {pw(last, 16)} {c['username']}")
        return

    targets = _arg("--targets")
    if targets:
        subs = [t.strip().lower() for t in targets.replace("，", ",").split(",") if t.strip()]
        selected = {
            c["username"] for c in convs
            if any(s in f"{c['username']}\n{c['display']}".lower() for s in subs)
        }
    else:
        selected = {c["username"] for c in convs}
    if not selected:
        sys.exit("没有匹配的会话。")

    out_dir = HERE / "export" / acct["wxid"]
    state_file = HERE / "state" / f"{acct['wxid']}.json"

    if "--once" in sys.argv:
        state = exporter.load_state(state_file)
        n = exporter.export_once(acct["db_dir"], keys, out_dir, selected, contacts, me, state, tmp,
                                 on_conv=lambda d, k, p: print(f"  {d}: +{k} -> {p.name}"))
        exporter.save_state(state_file, state)
        print(f"新增 {n} 条 -> {out_dir}")
    else:
        exporter.monitor(acct["db_dir"], keys, out_dir, selected, contacts, me, state_file, tmp,
                         interval=int(_arg("--interval", "5")))


if __name__ == "__main__":
    main()
