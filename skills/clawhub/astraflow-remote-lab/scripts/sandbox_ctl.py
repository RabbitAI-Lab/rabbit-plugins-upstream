#!/usr/bin/env python3
"""Manage AstraFlow Pure Desktop Sandboxes.

Operations:
  create    Create a desktop sandbox with aligned timezone, anti-screensaver watchdog,
            noVNC Web GUI with randomized authentication, and optional URL opening in Chrome.
  list      List active sandboxes across regions.
  kill      Terminate specific or all active sandboxes with strict safety confirmation.
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
ss -tlnp 2>/dev/null | grep -E ':(5900|6080)\b' || echo "no listener on 5900/6080"
"""

REPAIR_TEMPLATE = r"""#!/bin/bash
set -Eeuo pipefail
export DISPLAY=:99
LOG="/tmp"

echo "[1/7] Disabling screensaver and lockups..."
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

echo "[2/7] Checking noVNC & websockify..."
if ! command -v websockify >/dev/null 2>&1 || [ ! -f /usr/share/novnc/vnc.html ]; then
  DEBIAN_FRONTEND=noninteractive sudo apt-get update -qq
  DEBIAN_FRONTEND=noninteractive sudo apt-get install -y -qq novnc websockify
fi

echo "[3/7] Starting Xvfb display :99..."
if ! pgrep -x Xvfb >/dev/null 2>&1; then
  setsid nohup Xvfb :99 -screen 0 1920x1080x24 >"$LOG/xvfb.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[4/7] Starting XFCE desktop session & window managers..."
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

echo "[5/7] Starting x11vnc bound strictly to localhost:5900 with password authentication..."
# 确保 VNC 服务仅绑定至 127.0.0.1，并强制使用动态生成的随机访问密码
mkdir -p "$HOME/.vnc"
PASS_FILE="$HOME/.vnc/passwd"
x11vnc -storepasswd "__VNC_PASSWORD__" "$PASS_FILE"
chmod 600 "$PASS_FILE"

if ! pgrep -x x11vnc >/dev/null 2>&1; then
  setsid nohup x11vnc -display :99 -listen 127.0.0.1 -forever -shared -rfbauth "$PASS_FILE" -rfbport 5900 -noxdamage >"$LOG/x11vnc.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[6/7] Starting websockify bridge..."
if ! pgrep -f websockify >/dev/null 2>&1; then
  setsid nohup websockify --web=/usr/share/novnc 6080 127.0.0.1:5900 >"$LOG/websockify.log" 2>&1 </dev/null &
  sleep 2
fi

echo "[7/7] Verifying network listening status..."
if ! ss -tln | grep -q ":6080\b"; then
  echo "[ERROR] Port 6080 is not listening." >&2
  exit 1
fi
if ! ss -tln | grep -q "127.0.0.1:5900\b"; then
  echo "[ERROR] VNC port 5900 is not listening on 127.0.0.1." >&2
  exit 1
fi

TARGET_URL="__TARGET_URL__"
if [ "${START_APPS:-0}" = "1" ] && [ -n "$TARGET_URL" ]; then
  echo "Launching Chrome with target URL..."
  pkill -x chrome >/dev/null 2>&1 || true
  sleep 1
  nohup google-chrome --no-first-run --no-default-browser-check --disable-gpu --disable-dev-shm-usage --start-maximized "$TARGET_URL" >/tmp/chrome.log 2>&1 &
  sleep 2
fi

echo "ALL_SERVICES_OK"
"""


def get_sdk():
    """Deferred SDK importer: keeps --help functional even when SDK is not installed."""
    try:
        from ucloud_sandbox import Sandbox
        from ucloud_sandbox.sandbox.commands.command_handle import CommandExitException
        return Sandbox, CommandExitException
    except ImportError:
        print("\n[ERROR] Missing required Python package 'ucloud-sandbox'.")
        print("Please install the SDK using:")
        print("    pip install \"ucloud-sandbox>=1.5.0\"\n")
        sys.exit(1)


def generate_secure_password(length: int = 16) -> str:
    """Generate a cryptographically secure password for VNC session."""
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def validate_target_url(raw_url: str) -> str:
    """Validate user-supplied URL to reject unsafe protocols and sensitive local destinations."""
    if not raw_url:
        return ""
    parsed = urlparse(raw_url.strip())
    if parsed.scheme.lower() not in ("http", "https"):
        raise ValueError(f"Invalid URL scheme '{parsed.scheme}'. Only 'http://' and 'https://' are permitted.")
    hostname = (parsed.hostname or "").lower()
    unsafe_hosts = ("localhost", "127.0.0.1", "0.0.0.0", "169.254.169.254")
    if hostname in unsafe_hosts or hostname.startswith("192.168.") or hostname.startswith("10."):
        raise ValueError(f"Targeting loopback, private subnet, or cloud metadata endpoints ({hostname}) is forbidden.")
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

    # Validate target URL if provided
    target_url = ""
    if args.url:
        try:
            target_url = validate_target_url(args.url)
        except ValueError as err:
            print(f"[ERROR] URL validation failed: {err}")
            sys.exit(1)

    region = args.region
    os.environ["UCLOUD_SANDBOX_REGION"] = region
    timeout = args.timeout or 7200
    if timeout < 60 or timeout > 86400:
        print("[ERROR] Timeout must be between 60 and 86400 seconds (24h max).")
        sys.exit(1)

    print("============================================================")
    print("⚠️  AstraFlow Sandbox Billing & Resource Notice:")
    print(f"  - Target Region : {region}")
    print(f"  - Lifespan      : {timeout} seconds ({timeout // 3600}h {(timeout % 3600) // 60}m)")
    print("  - Lifecycle     : Resources accrue usage while active. Terminate promptly via 'kill' when finished.")
    print("============================================================")

    vnc_password = generate_secure_password(16)
    sb = None

    try:
        print(f"Provisioning desktop sandbox in [{region}]...")
        sb = Sandbox.create(template="desktop", timeout=timeout)
        sid = sb.sandbox_id
        print(f"Sandbox created successfully: {sid}")

        # Align timezone
        tz = "America/Los_Angeles" if region == "us-ca" else "Asia/Shanghai"
        print(f"Aligning system timezone to {tz}...")
        sb.commands.run(
            f"sudo ln -sf /usr/share/zoneinfo/{tz} /etc/localtime; echo '{tz}' | sudo tee /etc/timezone >/dev/null",
            timeout=30,
        )

        # Prepare repair script with secure VNC password & target URL
        repair_script = REPAIR_TEMPLATE.replace("__VNC_PASSWORD__", vnc_password)
        repair_script = repair_script.replace("__TARGET_URL__", target_url)

        print("Executing pre-launch system state probe...")
        probe_output = execute_script(sb, CommandExitException, PROBE, REMOTE_PROBE)
        print("Probe summary:\n" + probe_output.strip())

        print("Initializing XFCE desktop, secure VNC, and anti-screensaver watchdog (timeout=600s)...")
        repair_output = execute_script(sb, CommandExitException, repair_script, REMOTE_REPAIR, env_prefix="START_APPS=1 ")
        if "ALL_SERVICES_OK" not in repair_output:
            print("\n[ERROR] Remote desktop initialization did not report successful completion.")
            print(f"Log trace:\n{repair_output}")
            raise RuntimeError("Sandbox service verification failed.")

        raw_url = sb.get_url(6080).rstrip("/")
        # Embed randomized token in URL for one-click browser convenience while keeping password active
        authenticated_url = f"{raw_url}/vnc.html?autoconnect=true&resize=scale&password={vnc_password}"

        print("\n" + "=" * 64)
        print("🎉 Sandbox Desktop is READY!")
        print(f"Sandbox ID   : {sid}")
        print(f"Region       : {region}")
        print(f"Chrome URL   : {target_url or '(empty new tab)'}")
        print("\n🔐 Security Credentials:")
        print(f"  VNC Password : {vnc_password}")
        print("  Access Level : Bound to 127.0.0.1 inside container with mandatory auth.")
        print("\n🖥️  Web VNC Access URL (Single-Click Authenticated):")
        print(f"  {authenticated_url}")
        print("=" * 64)

    except Exception as exc:
        print(f"\n[FATAL] Error occurred during sandbox setup: {exc}")
        if sb is not None:
            print(f"Cleaning up uninitialized sandbox {sb.sandbox_id} to prevent orphan billing...")
            try:
                sb.kill()
                print("Orphan sandbox killed successfully.")
            except Exception as kill_err:
                print(f"[ALERT] Automatic cleanup failed: {kill_err}. Please manually terminate sandbox ID: {sb.sandbox_id}")
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
            print(f"[{reg}] Active instances: {len(items)}")
            for s in items:
                total += 1
                print(f"  - ID: {s.sandbox_id} | Template: {s.template_id} | State: {s.state}")
        except Exception as e:
            print(f"[{reg}] Failed to retrieve instance list: {e}")
    return total


def cmd_kill(args):
    Sandbox, _ = get_sdk()

    if not args.sandbox_id and not args.all:
        print("[ERROR] Refusing ambiguous kill command.")
        print("Usage:")
        print("  - To terminate a specific sandbox: python sandbox_ctl.py kill <SANDBOX_ID>")
        print("  - To terminate ALL active sandboxes: python sandbox_ctl.py kill --all [--region <region>]")
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
            print(f"[{reg}] Query error: {e}")

    if not all_targets:
        print("No matching active sandboxes found to terminate.")
        return

    print("\nTarget sandboxes selected for termination:")
    for reg, target_id, tpl in all_targets:
        print(f"  - [{reg}] {target_id} (Template: {tpl})")

    if not args.force:
        prompt_msg = f"\n⚠️  Confirm terminating {len(all_targets)} active sandbox instance(s)? (Type 'yes' to proceed): "
        try:
            choice = input(prompt_msg).strip().lower()
            if choice not in ("y", "yes"):
                print("Operation canceled by user.")
                return
        except (KeyboardInterrupt, EOFError):
            print("\nOperation canceled.")
            return

    killed = 0
    for reg, target_id, _ in all_targets:
        os.environ["UCLOUD_SANDBOX_REGION"] = reg
        try:
            sb = Sandbox.connect(target_id)
            sb.kill()
            print(f"[{reg}] Successfully terminated: {target_id}")
            killed += 1
        except Exception as e:
            print(f"[{reg}] Failed to terminate {target_id}: {e}")

    print(f"\nCompleted: {killed}/{len(all_targets)} sandbox(es) terminated. Billing stopped.")


def main():
    parser = argparse.ArgumentParser(
        description="AstraFlow Desktop Sandbox CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    p_create = subparsers.add_parser("create", help="Create and initialize a desktop sandbox")
    p_create.add_argument("--region", default="us-ca", choices=["us-ca", "cn-wlcb", "cn-sh"], help="Target region (default: us-ca)")
    p_create.add_argument("--timeout", type=int, default=7200, help="Sandbox lifespan in seconds (default: 7200, max: 86400)")
    p_create.add_argument("--url", help="Target URL to open in Chrome on startup (http:// or https:// only)")

    p_list = subparsers.add_parser("list", help="List active sandboxes across regions")
    p_list.add_argument("--region", choices=["us-ca", "cn-wlcb", "cn-sh"], help="Filter by specific region")

    p_kill = subparsers.add_parser("kill", help="Terminate active sandboxes")
    p_kill.add_argument("sandbox_id", nargs="?", help="Specific sandbox ID to terminate")
    p_kill.add_argument("--all", action="store_true", help="Explicitly confirm terminating all sandboxes in target region(s)")
    p_kill.add_argument("--region", choices=["us-ca", "cn-wlcb", "cn-sh"], help="Limit kill operation to specific region")
    p_kill.add_argument("-f", "--force", action="store_true", help="Bypass interactive confirmation prompt")

    args = parser.parse_args()

    # --help and no-argument executions are completely independent of SDK and API Key
    if not args.command:
        parser.print_help()
        sys.exit(0)

    # API key check only occurs when executing concrete action commands
    api_key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    if not api_key:
        print("[ERROR] Environment variable UCLOUD_SANDBOX_API_KEY is not set.")
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
