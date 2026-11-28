"""薇芯聊天记录导出小程序（交互式终端版）。

仅用于本人设备、本人账号的数据，本地学习研究；导出内容含他人隐私，请勿外传。全程无网络。

运行：  python wechat_export.py
依赖：  pycryptodome, psutil, frida, zstandard
"""
from __future__ import annotations

import os
import shutil
import stat
import sys
from datetime import datetime
from pathlib import Path

import wxread
import exporter
import capture_keys

HERE = Path(__file__).resolve().parent
KEYS_DIR = HERE / "keys"
STATE_DIR = HERE / "state"
EXPORT_DIR = HERE / "export"


def _force_unlink(p: Path) -> None:
    """删除文件；遇只读属性先清掉再删（Windows 复制来的媒体常是只读）。"""
    try:
        p.unlink()
    except PermissionError:
        os.chmod(p, stat.S_IWRITE)
        p.unlink()


def _force_rmtree(p: Path) -> None:
    def _onerr(func, path, _exc):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception:
            pass
    try:
        shutil.rmtree(p, onexc=_onerr)          # Python 3.12+
    except TypeError:
        shutil.rmtree(p, onerror=lambda f, pth, ei: _onerr(f, pth, None))

# 导出所必需的库（扫描/导出至少要这几把密钥）
ESSENTIAL = ["contact/contact.db", "session/session.db"]


class App:
    def __init__(self):
        self.account: dict | None = None
        self.keys: dict = {}
        self.contacts: dict = {}
        self.me: str = ""
        self.tmp = wxread.make_tmp_dir()
        self.conversations: list[dict] = []
        self.selected: set[str] = set()
        self.out_dir = EXPORT_DIR
        self.interval = 5

    # ----------------------------------------------------------- 路径 ----
    @property
    def keys_file(self) -> Path:
        return KEYS_DIR / f"{self.account['wxid']}.json"

    @property
    def state_file(self) -> Path:
        return STATE_DIR / f"{self.account['wxid']}.json"

    @property
    def acct_out_dir(self) -> Path:
        return self.out_dir / self.account["wxid"]

    # --------------------------------------------------------- 工具 ------
    def reload_keys(self):
        self.keys = wxread.load_keys(self.keys_file)
        self.contacts = wxread.build_contacts(self.account["db_dir"], self.keys, self.tmp)
        self.me = self.account["wxid"]

    def need_account(self) -> bool:
        if not self.account:
            print("！请先用菜单 1 选择薇芯账号。")
            return False
        return True

    def message_key_ready(self) -> bool:
        rels = wxread.message_db_rels(self.account["db_dir"])
        return any(self.keys.get(r) for r in rels)

    # ========================================================= 菜单项 ====
    def menu_accounts(self):
        print("\n正在检测薇芯账号…")
        accts = wxread.find_accounts()
        if not accts:
            print("未发现薇芯账号。请确认薇芯已启动并登录后重试（抓密钥也需要薇芯在运行）。")
            return
        print("发现以下账号：")
        for i, a in enumerate(accts, 1):
            flag = "运行中" if a.get("running") else "未运行"
            print(f"  {i}. {a['wxid']}  [{flag}]  {a['db_dir']}")
        sel = input("选择账号序号（回车选 1）：").strip() or "1"
        try:
            self.account = accts[int(sel) - 1]
        except (ValueError, IndexError):
            print("输入无效。")
            return
        self.reload_keys()
        self.selected.clear()
        self.conversations = []
        print(f"已选账号：{self.account['wxid']}")
        if not self.message_key_ready():
            print("提示：该账号尚无消息库密钥，请用菜单 2 抓取。")

    def menu_keys(self):
        if not self.need_account():
            return
        db_dir = self.account["db_dir"]
        all_dbs = capture_keys.load_encrypted_dbs(db_dir)
        print(f"\n加密库共 {len(all_dbs)} 个；已有密钥 {len(self.keys)} 把。关键库状态：")
        for rel in ESSENTIAL + wxread.message_db_rels(db_dir):
            mark = "✓" if self.keys.get(rel) else "✗"
            print(f"  [{mark}] {rel}")
        if input("\n是否现在抓取密钥？(y/N) ").strip().lower() != "y":
            return
        secs = input("抓取时长秒数（回车 90）：").strip() or "90"
        try:
            secs = int(secs)
        except ValueError:
            secs = 90
        print("\n★ 操作指引：脚本已 hook 薇芯。请在接下来的时间里到薇芯窗口中：")
        print("   · 多点开不同会话，并上翻历史消息")
        print("   · 用搜索框搜索聊天内容（会打开全文搜索库）")
        print("   · 打开 收藏 / 朋友圈 / 公众号 等")
        print("   每个数据库的连接首次打开时才会暴露它的密钥。\n")
        try:
            def prog(done, total, rel):
                print(f"   抓到 {rel}  （{done}/{total}）")
            capture_keys.capture(db_dir, self.keys_file, secs, on_progress=prog)
        except Exception as e:
            print(f"抓取失败：{e}")
            return
        self.reload_keys()
        print(f"完成，当前 {len(self.keys)} 把密钥已保存到 {self.keys_file}")

    def menu_scan(self):
        if not self.need_account():
            return
        if not self.message_key_ready():
            print("！尚无消息库密钥，请先用菜单 2 抓取。")
            return
        print("\n正在扫描会话（解密读取中，稍候）…")
        self.conversations = wxread.scan_conversations(
            self.account["db_dir"], self.keys, self.contacts, self.tmp
        )
        if not self.conversations:
            print("未扫描到会话。可能消息库密钥还没抓到，或该账号暂无聊天记录。")
            return
        self._print_conversations()

    def _print_conversations(self):
        pw = wxread.pad_width
        print(f"\n可导出的会话（共 {len(self.conversations)} 个）：")
        header = (f"  {pw('#', 3, 'right')}  {pw('显示名', 24)} {pw('类型', 12)} "
                  f"{pw('消息数', 7, 'right')}  {pw('最近', 16)} wxid")
        print(header)
        print("  " + "-" * (len(header) - 2))
        for i, c in enumerate(self.conversations, 1):
            last = datetime.fromtimestamp(c["last_time"]).strftime("%Y-%m-%d %H:%M") if c["last_time"] else "-"
            mark = "●" if c["username"] in self.selected else " "
            print(f"{mark} {pw(str(i), 3, 'right')}  {pw(c['display'], 24)} {pw(c['kind'], 12)} "
                  f"{pw(str(c['count']), 7, 'right')}  {pw(last, 16)} {c['username']}")

    def menu_select(self):
        if not self.conversations:
            print("！请先用菜单 3 扫描会话。")
            return
        self._print_conversations()
        print("\n输入要导出的序号：如 1,3,5 或 2-6，或 all 全选，或 none 清空。")
        raw = input("选择：").strip().lower()
        if raw == "none":
            self.selected.clear()
            print("已清空。")
            return
        if raw == "all":
            self.selected = {c["username"] for c in self.conversations}
        else:
            picked = set()
            for part in raw.replace("，", ",").split(","):
                part = part.strip()
                if "-" in part:
                    try:
                        a, b = part.split("-")
                        for n in range(int(a), int(b) + 1):
                            picked.add(n)
                    except ValueError:
                        pass
                elif part.isdigit():
                    picked.add(int(part))
            self.selected = {
                self.conversations[n - 1]["username"]
                for n in picked if 1 <= n <= len(self.conversations)
            }
        names = [wxread.display_of(self.contacts, u) or u for u in self.selected]
        print(f"已选 {len(self.selected)} 个：{', '.join(names) if names else '(无)'}")

    def _ensure_ready_for_export(self) -> bool:
        if not self.need_account():
            return False
        if not self.selected:
            print("！请先用菜单 3 扫描、菜单 4 选择要导出的会话。")
            return False
        return True

    def menu_export_once(self):
        if not self._ensure_ready_for_export():
            return
        state = exporter.load_state(self.state_file)
        print(f"\n导出到 {self.acct_out_dir} …（已存在的文件会追加新消息）")

        def on_conv(display, n, path):
            print(f"  {display}: +{n} 条 -> {path.name}")

        n = exporter.export_once(
            self.account["db_dir"], self.keys, self.acct_out_dir,
            self.selected, self.contacts, self.me, state, self.tmp, on_conv=on_conv
        )
        exporter.save_state(self.state_file, state)
        print(f"完成，本次新增 {n} 条。")

    def menu_monitor(self):
        if not self._ensure_ready_for_export():
            return
        print(f"\n实时监听导出到 {self.acct_out_dir}，每 {self.interval}s 检查一次。")
        print("（注：DB 方式为准实时，最新消息可能有几秒延迟；Ctrl+C 停止）")
        exporter.monitor(
            self.account["db_dir"], self.keys, self.acct_out_dir,
            self.selected, self.contacts, self.me, self.state_file, self.tmp,
            interval=self.interval,
        )

    def menu_settings(self):
        print(f"\n当前输出目录：{self.out_dir}")
        new = input("新的输出目录（回车不改）：").strip()
        if new:
            self.out_dir = Path(new)
        print(f"当前轮询间隔：{self.interval}s")
        iv = input("新的轮询间隔秒数（回车不改）：").strip()
        if iv.isdigit() and int(iv) >= 1:
            self.interval = int(iv)
        print(f"已设置：输出目录={self.out_dir}  轮询间隔={self.interval}s")

    def menu_reset(self):
        """清理所有生成物（密钥 / 导出 / 状态 / 缓存），还原到初始状态。"""
        targets: list[Path] = []
        for d in (KEYS_DIR, STATE_DIR, EXPORT_DIR, HERE / "__pycache__"):
            if d.is_dir():
                targets.append(d)
        for name in ("keys.json", "captured_key.json", "imgkey.txt", "export_state.json"):
            p = HERE / name
            if p.exists():
                targets.append(p)
        # 安全：只允许删除项目目录内的东西
        targets = [t for t in targets if HERE in t.resolve().parents or t.resolve().parent == HERE]
        if not targets:
            print("\n已是初始状态，无需清理。")
            return
        print("\n将删除以下生成物（仅项目目录内，不影响薇芯本身的数据）：")
        for t in targets:
            print("  -", t.relative_to(HERE))
        if input("确认清理？此操作不可撤销 (y/N) ").strip().lower() != "y":
            print("已取消。")
            return
        for t in targets:
            try:
                if t.is_dir():
                    _force_rmtree(t)
                else:
                    _force_unlink(t)
            except OSError as e:
                print(f"  删除失败 {t.name}: {e}")
        # 清空内存中的状态
        self.keys = {}
        self.contacts = {}
        self.conversations = []
        self.selected.clear()
        print("已还原到初始状态。若要再次导出，请重新用菜单 2 抓取密钥。")

    # ========================================================= 主循环 ====
    def run(self):
        print("=" * 60)
        print(" 薇芯聊天记录导出小程序（仅限本人数据 / 本地学习研究）")
        print(" 步骤：1 选账号 → 2 抓密钥 → 3 扫描 → 4 选会话 → 5 导出 / 6 实时监听")
        print("=" * 60)
        actions = {
            "1": self.menu_accounts,
            "2": self.menu_keys,
            "3": self.menu_scan,
            "4": self.menu_select,
            "5": self.menu_export_once,
            "6": self.menu_monitor,
            "7": self.menu_settings,
            "8": self.menu_reset,
        }
        while True:
            acct = self.account["wxid"] if self.account else "未选择"
            print("\n" + "-" * 60)
            print(f"当前账号：{acct}    已选会话：{len(self.selected)}    输出：{self.out_dir}")
            print(" 1.检测/选择账号  2.密钥状态/抓取  3.扫描会话  4.选择会话")
            print(" 5.立即导出所选   6.实时监听导出  7.设置  8.清理/还原  0.退出")
            choice = input("请选择：").strip()
            if choice == "0":
                print("再见。")
                return
            fn = actions.get(choice)
            if not fn:
                print("无效选项。")
                continue
            try:
                fn()
            except KeyboardInterrupt:
                print("\n（已中断当前操作）")
            except Exception as e:
                print(f"出错：{e}")


if __name__ == "__main__":
    try:
        App().run()
    except KeyboardInterrupt:
        sys.exit(0)
