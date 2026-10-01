#!/usr/bin/env python3
"""管理 AstraFlow 纯桌面沙箱。

操作：
  create    创建一个桌面沙箱，自带时区对齐、防息屏看门狗、
            带随机认证的 noVNC Web 图形界面，可选在 Chrome 中打开指定网址。
  list      列出跨地域的活动沙箱。
  kill      在严格安全确认下销毁指定或全部活动沙箱。
"""

import argparse
import base64
import os
import secrets
import string
import sys
from urllib.parse import urlparse

REMOTE_PROBE = "/home/user/wb-probe.sh"
REMOTE_REPAIR = "/home/user/wb-repair.sh"

PROBE = r"""#!/bin/bash
set -u
echo "=== 进程状态 ==="
for p in xfce4-screensaver Xvfb xfce4-session xfwm4 xfdesktop x11vnc websockify; do
  if pgrep -x "$p" >/dev/null 2>&1 || pgrep -f "$p" >/dev/null 2>&1; then
    echo "$p RUNNING"
  else
    echo "$p GONE"
  fi
done
echo "=== 端口监听 ==="
ss -tlnp 2>/dev/null | grep -E ':(5900|6080)\b' || echo "5900/6080 端口无监听"
"""

REPAIR_TEMPLATE = r"""#!/bin/bash
set -Eeuo pipefail
export DISPLAY=:99
LOG="/tmp"

echo "[1/7] 禁用息屏与锁屏..."
xfconf-query -c xfce4-screensaver -p /saver/enabled -n -t bool -s false >/dev/null 2>&1 || true
xfconf-query -c xfce4-screensaver -p /lock/enabled -n -t bool -s false >/dev/null 2>&1 || true

mkdir -p "$HOME/.config/autostart"
for f in xfce4-screensaver light-locker xscreensaver; do
  printf '%s\n' '[Desktop Entry]' 'Type=Application' "Name=$f" 'X-GNOME-Autostart-enabled=false' 'Hidden=true' > "$HOME/.config/autostart/$f.desktop"
done

pkill -f xfce4-screensaver >/dev/null 2>&1 || true
pkill -f light-locker >/dev/null 2>&1 || true
xset s off -dpms s noblank >/dev/null 2>&1 || true

WATCH="$HOME/.config/kill-screensaver.sh"
cat > "$WATCH" <<'WATCHER'
#!/bin/bash
export DISPLAY=:99
for _ in $(seq 1 720); do
  pkill -f xfce4-screensaver >/dev/null 2>&1 || true
  sleep 5
done
WATCHER
chmod +x "$WATCH"
setsid nohup "$WATCH" >/dev/null 2>&1 </dev/null &

echo "[2/7] 检查 noVNC 与 websockify..."
if ! command -v websockify >/dev/null 2>&1 || [ ! -f /usr/share/novnc/vnc.html ]; then
  DEBIAN_FRONTEND=noninteractive sudo apt-get update -qq
  DEBIAN_FRONTEND=noninteractive sudo apt-get install -y -qq novnc websockify
fi

echo "[3/7] 启动 Xvfb 显示 :99..."
if ! pgrep -x Xvfb >/dev/null 2>&1; then
  setsid nohup Xvfb :99 -screen 0 1920x1080x24 >"$LOG/xvfb.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[4/7] 启动 XFCE 桌面会话与窗口管理器..."
if ! pgrep -x xfce4-session >/dev/null 2>&1 && ! pgrep -f startxfce4 >/dev/null 2>&1; then
  setsid nohup startxfce4 >"$LOG/xfce.log" 2>&1 </dev/null &
  sleep 4
fi

if ! pgrep -x xfwm4 >/dev/null 2>&1; then
  setsid nohup xfwm4 --replace >"$LOG/xfwm4.log" 2>&1 </dev/null &
  sleep 2
fi

if ! pgrep -x xfdesktop >/dev/null 2>&1; then
  setsid nohup xfdesktop >"$LOG/xfdesktop.log" 2>&1 </dev/null &
  sleep 1
fi

echo "[5/7] 启动 x11vnc 并严格绑定到 localhost:5900，强制密码认证..."
mkdir -p "$HOME/.vnc"
PASS_FILE="$HOME/.vnc/passwd"
x11vnc -storepasswd "__VNC_PASSWORD__" "$PASS_FILE"
chmod 600 "$PASS_FILE"

if ! pgrep -x x11vnc >/dev/null 2>&1; then
  setsid nohup x11vnc -display :99 -listen 127.0.0.1 -forever -shared -rfbauth "$PASS_FILE" -rfbport 5900 -noxdamage >"$LOG/x11vnc.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[6/7] 启动 websockify 桥接..."
if ! pgrep -f websockify >/dev/null 2>&1; then
  setsid nohup websockify --web=/usr/share/novnc 6080 127.0.0.1:5900 >"$LOG/websockify.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[7/7] 验证网络监听状态..."
if ! ss -tln | grep -q ":6080\b"; then
  echo "[ERROR] 6080 端口未监听。" >&2
  exit 1
fi
if ! ss -tln | grep -q "127.0.0.1:5900\b"; then
  echo "[ERROR] VNC 5900 端口未在 127.0.0.1 监听。" >&2
  exit 1
fi

TARGET_URL="__TARGET_URL__"
if [ "${START_APPS:-0}" = "1" ] && [ -n "$TARGET_URL" ]; then
  echo "正在启动 Chrome 打开目标网址..."
  pkill -x chrome >/dev/null 2>&1 || true
  sleep 1
  nohup google-chrome --no-first-run --no-default-browser-check --disable-gpu --disable-dev-shm-usage --start-maximized "$TARGET_URL" >/tmp/chrome.log 2>&1 &
  sleep 2
fi

echo "ALL_SERVICES_OK"
"""


def get_sdk():
    """延迟导入 SDK：即使 SDK 未安装，--help 仍可用。"""
    try:
        from ucloud_sandbox import Sandbox
        from ucloud_sandbox.sandbox.commands.command_handle import CommandExitException
        return Sandbox, CommandExitException
    except ImportError:
        print("\n[ERROR] 缺少必需的 Python 包 'ucloud-sandbox'。")
        print("请使用以下命令安装 SDK：")
        print("    pip install \"ucloud-sandbox>=1.5.0\"\n")
        sys.exit(1)


def generate_secure_password(length: int = 16) -> str:
    """为 VNC 会话生成密码学安全的随机密码。"""
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def validate_target_url(raw_url: str) -> str:
    """校验用户传入的 URL，拒绝不安全的协议与敏感的本地目标地址。"""
    if not raw_url:
        return ""
    parsed = urlparse(raw_url.strip())
    if parsed.scheme.lower() not in ("http", "https"):
        raise ValueError(f"无效的 URL 协议 '{parsed.scheme}'，仅允许 'http://' 与 'https://'。")
    hostname = (parsed.hostname or "").lower()
    unsafe_hosts = ("localhost", "127.0.0.1", "0.0.0.0", "169.254.169.254")
    if hostname in unsafe_hosts or hostname.startswith("192.168.") or hostname.startswith("10."):
        raise ValueError(f"禁止指向回环、私网子网或云元数据端点（{hostname}）。")
    return raw_url.strip()


def execute_script(sb, CommandExitException, script_body, remote_path, env_prefix=""):
    b64 = base64.b64encode(script_body.encode("utf-8")).decode("ascii")
    cmd = f"printf %s '{b64}' | base64 -d > {remote_path}; {env_prefix}bash {remote_path} 2>&1"
    try:
        res = sb.commands.run(cmd, timeout=600)
        return (getattr(res, "stdout", "") or "") + (getattr(res, "stderr", "") or "")
    except CommandExitException as exc:
        return (getattr(exc, "stdout", "") or "") + (getattr(exc, "stderr", "") or "")


def cmd_create(args):
    Sandbox, CommandExitException = get_sdk()

    # 校验目标 URL（如有）
    target_url = ""
    if args.url:
        try:
            target_url = validate_target_url(args.url)
        except ValueError as err:
            print(f"[ERROR] URL 校验失败：{err}")
            sys.exit(1)

    region = args.region
    os.environ["UCLOUD_SANDBOX_REGION"] = region
    timeout = args.timeout or 7200
    if timeout < 60 or timeout > 86400:
        print("[ERROR] 超时时长须在 60 至 86400 秒之间（最长 24 小时）。")
        sys.exit(1)

    print("============================================================")
    print("⚠️  星图 AstraFlow 沙箱计费与资源提示：")
    print(f"  - 目标地域 : {region}")
    print(f"  - 生命周期 : {timeout} 秒（{timeout // 3600} 小时 {(timeout % 3600) // 60} 分）")
    print("  - 计费规则 : 资源在运行期间持续计费，使用完毕请立即用 'kill' 销毁。")
    print("============================================================")

    vnc_password = generate_secure_password(16)
    sb = None

    try:
        print(f"正在 [{region}] 开通桌面沙箱...")
        sb = Sandbox.create(template="desktop", timeout=timeout)
        sid = sb.sandbox_id
        print(f"沙箱创建成功：{sid}")

        # 对齐时区
        tz = "America/Los_Angeles" if region == "us-ca" else "Asia/Shanghai"
        print(f"正在对齐系统时区至 {tz}...")
        sb.commands.run(
            f"sudo ln -sf /usr/share/zoneinfo/{tz} /etc/localtime; echo '{tz}' | sudo tee /etc/timezone >/dev/null",
            timeout=30,
        )

        # 注入 VNC 密码与目标 URL 到修复脚本
        repair_script = REPAIR_TEMPLATE.replace("__VNC_PASSWORD__", vnc_password)
        repair_script = repair_script.replace("__TARGET_URL__", target_url)

        print("正在执行启动前系统状态探测...")
        probe_output = execute_script(sb, CommandExitException, PROBE, REMOTE_PROBE)
        print("探测摘要：\n" + probe_output.strip())

        print("正在初始化 XFCE 桌面、安全 VNC 与防息屏看门狗（超时=600 秒）...")
        repair_output = execute_script(sb, CommandExitException, repair_script, REMOTE_REPAIR, env_prefix="START_APPS=1 ")
        if "ALL_SERVICES_OK" not in repair_output:
            print("\n[ERROR] 远程桌面初始化未报告成功完成。")
            print(f"日志追踪：\n{repair_output}")
            raise RuntimeError("沙箱服务自检失败。")

        raw_url = sb.get_url(6080).rstrip("/")
        # 在 URL 中嵌入随机 token，便于一键浏览器打开，同时保留密码认证
        authenticated_url = f"{raw_url}/vnc.html?autoconnect=true&resize=scale&password={vnc_password}"

        print("\n" + "=" * 64)
        print("🎉 沙箱桌面已就绪！")
        print(f"沙箱 ID     : {sid}")
        print(f"地  域      : {region}")
        print(f"Chrome 网址 : {target_url or '（空白新标签页）'}")
        print("\n🔐 安全凭据：")
        print(f"  VNC 密码   : {vnc_password}")
        print("  访问层级   : 容器内绑定 127.0.0.1，强制认证。")
        print("\n🖥️  Web VNC 访问网址（一键认证直连）：")
        print(f"  {authenticated_url}")
        print("=" * 64)

    except Exception as exc:
        print(f"\n[FATAL] 沙箱初始化过程发生错误：{exc}")
        if sb is not None:
            print(f"正在清理未完成的沙箱 {sb.sandbox_id} 以防止遗留计费...")
            try:
                sb.kill()
                print("遗留沙箱已成功销毁。")
            except Exception as kill_err:
                print(f"[ALERT] 自动清理失败：{kill_err}。请手动销毁沙箱 ID：{sb.sandbox_id}")
        sys.exit(1)


def cmd_list(args):
    Sandbox, _ = get_sdk()
    regions = [args.region] if args.region else ["us-ca", "cn-wlcb", "cn-sh"]
    total = 0
    for reg in regions:
        os.environ["UCLOUD_SANDBOX_REGION"] = reg
        try:
            paginator = Sandbox.list()
            items = []
            while paginator.has_next:
                items.extend(paginator.next_items())
            print(f"[{reg}] 活动实例数：{len(items)}")
            for s in items:
                total += 1
                print(f"  - ID：{s.sandbox_id} | 模板：{s.template_id} | 状态：{s.state}")
        except Exception as e:
            print(f"[{reg}] 获取实例列表失败：{e}")
    return total


def cmd_kill(args):
    Sandbox, _ = get_sdk()

    if not args.sandbox_id and not args.all:
        print("[ERROR] 拒绝执行语义不明的销毁命令。")
        print("用法：")
        print("  - 销毁指定沙箱：python sandbox_ctl.py kill <SANDBOX_ID>")
        print("  - 销毁全部活动沙箱：python sandbox_ctl.py kill --all [--region <地域>]")
        sys.exit(1)

    regions = [args.region] if args.region else ["us-ca", "cn-wlcb", "cn-sh"]
    all_targets = []
    for reg in regions:
        os.environ["UCLOUD_SANDBOX_REGION"] = reg
        try:
            paginator = Sandbox.list()
            while paginator.has_next:
                for s in paginator.next_items():
                    if args.sandbox_id and s.sandbox_id == args.sandbox_id:
                        all_targets.append((reg, s.sandbox_id, s.template_id))
                    elif args.all:
                        all_targets.append((reg, s.sandbox_id, s.template_id))
        except Exception as e:
            print(f"[{reg}] 查询出错：{e}")

    if not all_targets:
        print("未找到匹配的活动沙箱。")
        return

    print("\n以下沙箱将被销毁：")
    for reg, target_id, tpl in all_targets:
        print(f"  - [{reg}] {target_id}（模板：{tpl}）")

    if not args.force:
        prompt_msg = f"\n⚠️  确认销毁 {len(all_targets)} 个活动沙箱实例？（输入 'yes' 继续）："
        try:
            choice = input(prompt_msg).strip().lower()
            if choice not in ("y", "yes"):
                print("用户已取消操作。")
                return
        except (KeyboardInterrupt, EOFError):
            print("\n操作已取消。")
            return

    killed = 0
    for reg, target_id, _ in all_targets:
        os.environ["UCLOUD_SANDBOX_REGION"] = reg
        try:
            sb = Sandbox.connect(target_id)
            sb.kill()
            print(f"[{reg}] 成功销毁：{target_id}")
            killed += 1
        except Exception as e:
            print(f"[{reg}] 销毁 {target_id} 失败：{e}")

    print(f"\n完成：已销毁 {killed}/{len(all_targets)} 个沙箱，计费已停止。")


def main():
    parser = argparse.ArgumentParser(
        description="星图 AstraFlow 桌面沙箱命令行工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    p_create = subparsers.add_parser("create", help="创建并初始化一个桌面沙箱")
    p_create.add_argument("--region", default="us-ca", choices=["us-ca", "cn-wlcb", "cn-sh"], help="目标地域（默认：us-ca）")
    p_create.add_argument("--timeout", type=int, default=7200, help="沙箱生命周期秒数（默认 7200，上限 86400）")
    p_create.add_argument("--url", help="启动时在 Chrome 中打开的目标网址（仅支持 http:// 或 https://）")

    p_list = subparsers.add_parser("list", help="列出跨地域的活动沙箱")
    p_list.add_argument("--region", choices=["us-ca", "cn-wlcb", "cn-sh"], help="按指定地域过滤")

    p_kill = subparsers.add_parser("kill", help="销毁活动沙箱")
    p_kill.add_argument("sandbox_id", nargs="?", help="要销毁的指定沙箱 ID")
    p_kill.add_argument("--all", action="store_true", help="明确确认销毁目标地域下的全部活动沙箱")
    p_kill.add_argument("--region", choices=["us-ca", "cn-wlcb", "cn-sh"], help="把销毁操作限制在指定地域")
    p_kill.add_argument("-f", "--force", action="store_true", help="跳过交互式确认提示")

    args = parser.parse_args()

    # --help 与无参数执行完全独立于 SDK 与 API Key
    if not args.command:
        parser.print_help()
        sys.exit(0)

    # 仅在执行具体操作命令时才检查 API Key
    api_key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    if not api_key:
        print("[ERROR] 环境变量 UCLOUD_SANDBOX_API_KEY 未设置。")
        print("请在 AstraFlow Key Management 页面创建并复制你的专属 Key：")
        print("    🔑 https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl")
        print("")
        print("配置方式（任选其一）：")
        print("    export UCLOUD_SANDBOX_API_KEY=\"sk-xxx\"")
        print("    # 或临时传入：")
        print("    python3 scripts/sandbox_ctl.py create --api-key sk-xxx")
        sys.exit(1)

    if args.command == "create":
        cmd_create(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "kill":
        cmd_kill(args)


if __name__ == "__main__":
    main()
