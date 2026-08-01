# -*- coding: utf-8 -*-
"""
patch_lnk.py — 给千问浏览器的快捷方式注入 CDP 调试端口（9666）

用途：让千问每次从桌面/任务栏/开始菜单启动时默认带 --remote-debugging-port=9666，
      小虾（qw.cjs）就能直接连上驱动，不必每次杀进程重拉。

依赖：pywin32（pip install pywin32），仅 Windows 可用。

说明：
  - 脚本会自动定位当前用户的环境变量（USERPROFILE / APPDATA / LOCALAPPDATA），
    不硬编码用户名，换机器也能跑。
  - 只修改 TargetPath 含 "qianwen" 的快捷方式（安全检查，避免误改）。
  - 同时在桌面新建一个「千问(调试).lnk」快捷方式。
"""
import os

try:
    import win32com.client
except ImportError:
    raise SystemExit("需要 pywin32：pip install pywin32")

USER = os.environ.get("USERPROFILE", "C:\\Users\\SZTSY")
APPDATA = os.environ.get("APPDATA", os.path.join(USER, "AppData", "Roaming"))
LOCAL = os.environ.get("LOCALAPPDATA", os.path.join(USER, "AppData", "Local"))

ws = win32com.client.Dispatch("WScript.Shell")
PORT_ARG = "--remote-debugging-port=9666"
PORT_FLAG = "--remote-debugging-port"

# 已有千问快捷方式（任务栏 + 开始菜单 + 常用软件）
existing = {
    "开始菜单": os.path.join(APPDATA, "Microsoft\\Windows\\Start Menu\\Programs\\千问.lnk"),
    "任务栏":   os.path.join(APPDATA, "Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar\\千问.lnk"),
    "常用软件": os.path.join(USER, "Desktop", "常用软件", "千问.lnk"),
}

real_exe = None
print("=" * 60)
print("【第一步】读取并修改已有快捷方式")
for name, path in existing.items():
    print("-" * 50)
    print(f"{name}: {path}")
    if not os.path.exists(path):
        print("  -> 不存在，跳过")
        continue
    sc = ws.CreateShortcut(path)
    tp = sc.TargetPath or ""
    args = sc.Arguments or ""
    print(f"  TargetPath: {tp!r}")
    print(f"  原参数    : {args!r}")
    if "qianwen" not in tp.lower():
        print("  !! TargetPath 不含 qianwen，疑似不是千问，跳过修改（保险）")
        continue
    if PORT_FLAG in args:
        print("  -> 已含端口参数，无需修改")
    else:
        new_args = (args + " " + PORT_ARG).strip()
        sc.Arguments = new_args
        sc.Save()
        print(f"  -> 已追加端口 -> {new_args!r}")
    if not real_exe and os.path.exists(tp):
        real_exe = tp

if not real_exe:
    real_exe = os.path.join(LOCAL, "Programs", "QianwenApp", "qianwen.exe")
    print(f"  未从已有 lnk 取得真实 exe，使用默认: {real_exe}")

# 桌面新建带端口快捷方式
print("=" * 60)
print("【第二步】桌面新建带端口快捷方式")
desktop = os.path.join(USER, "Desktop")
new_path = os.path.join(desktop, "千问(调试).lnk")
sc = ws.CreateShortcut(new_path)
sc.TargetPath = real_exe
sc.Arguments = PORT_ARG
sc.WorkingDirectory = os.path.dirname(real_exe)
sc.Description = "千问浏览器（自动开启 CDP 调试端口 9666，供自动化驱动）"
sc.IconLocation = real_exe + ",0"
sc.Save()
print(f"  已创建: {new_path}")
print(f"  TargetPath: {real_exe}")
print(f"  参数      : {PORT_ARG}")
print(f"  工作目录  : {os.path.dirname(real_exe)}")

# 顺手提示：开机自启项（注册表 Run）也可以注入端口，覆盖「开机自动启动」的千问
print("=" * 60)
print("【提示】若要覆盖「开机自启」的千问，还需在注册表添加端口：")
print(rf'  HKCU\Software\Microsoft\Windows\CurrentVersion\Run\qianwen')
print(rf'  把值改为："{real_exe}" --launch-from=loginitem {PORT_ARG}')
print("=" * 60)
print("完成。")
