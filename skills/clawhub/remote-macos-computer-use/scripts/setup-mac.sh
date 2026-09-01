#!/usr/bin/env bash
# Idempotent Mac-side setup for 'remote-macos-computer-use'.
# Creates LaunchAgents for: cua-driver daemon, reverse SSH tunnel, keep-awake.
# Prints the human-only steps (Remote Login, TCC grant, auto-login/lock).
#
# REQUIRED env:  REMOTE_HOST   (server address, e.g. your cloud host)
# OPTIONAL env:  REMOTE_USER   (server ssh user; default 'ubuntu' - the usual cloud image user)
#                REMOTE_PORT   (default 22)   REVERSE_PORT (default 2299)
#                CUA_BIN       (default /Applications/CuaDriver.app/Contents/MacOS/cua-driver)
#                LA_DIR        (default $HOME/Library/LaunchAgents)
#                BRIDGE_DIR    (default $HOME/hermes-mac-bridge)
set -euo pipefail

REMOTE_HOST="${REMOTE_HOST:-}"
REMOTE_USER="${REMOTE_USER:-ubuntu}"
REMOTE_PORT="${REMOTE_PORT:-22}"
REVERSE_PORT="${REVERSE_PORT:-2299}"
CUA_BIN="${CUA_BIN:-/Applications/CuaDriver.app/Contents/MacOS/cua-driver}"
LA_DIR="${LA_DIR:-$HOME/Library/LaunchAgents}"
BRIDGE_DIR="${BRIDGE_DIR:-$HOME/hermes-mac-bridge}"

if [ -z "$REMOTE_HOST" ]; then
  echo "ERROR: set REMOTE_HOST to your server address, e.g.:  REMOTE_HOST=203.0.113.10 bash ./setup-mac.sh" >&2
  exit 1
fi

echo "==> cua-driver present?"
if ! command -v cua-driver >/dev/null 2>&1; then
  echo "    not installed. Install with:"
  echo "    /bin/bash -c \"\$(curl -fsSL https://cua.ai/driver/install.sh)\""
fi
"$CUA_BIN" --version 2>/dev/null || true

echo "==> daemon LaunchAgent (com.trycua.driver)"
mkdir -p "$LA_DIR"
cat > "$LA_DIR/com.trycua.driver.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.trycua.driver</string>
  <key>ProgramArguments</key>
  <array>
    <string>$CUA_BIN</string>
    <string>serve</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$HOME/.cua-driver/serve.out.log</string>
  <key>StandardErrorPath</key><string>$HOME/.cua-driver/serve.err.log</string>
</dict>
</plist>
PLIST

echo "==> tunnel wrapper"
mkdir -p "$BRIDGE_DIR"
cat > "$BRIDGE_DIR/tunnel.sh" <<TUN
#!/usr/bin/env bash
S="$REMOTE_USER@$REMOTE_HOST"
LOG="$BRIDGE_DIR/tunnel.log"
while true; do
  echo "[$(date '+%F %T')] starting tunnel -> \$S" >> "\$LOG"
  ssh -N \
    -o ExitOnForwardFailure=yes \
    -o ServerAliveInterval=30 \
    -o ServerAliveCountMax=3 \
    -o ConnectTimeout=15 \
    -o StrictHostKeyChecking=accept-new \
    -o BatchMode=yes \
    -R $REVERSE_PORT:127.0.0.1:22 \
    "\$S" >>"\$LOG" 2>&1
  echo "[$(date '+%F %T')] tunnel exited (rc=\$?), retry in 5s" >> "\$LOG"
  sleep 5
done
TUN
chmod +x "$BRIDGE_DIR/tunnel.sh"

echo "==> tunnel LaunchAgent (com.remote-macos.tunnel)"
cat > "$LA_DIR/com.remote-macos.tunnel.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.remote-macos.tunnel</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$BRIDGE_DIR/tunnel.sh</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>5</integer>
</dict>
</plist>
PLIST

echo "==> keep-awake LaunchAgent (com.remote-macos.keep-awake)"
cat > "$LA_DIR/com.remote-macos.keep-awake.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.remote-macos.keep-awake</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/caffeinate</string>
    <string>-dimsu</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
</dict>
</plist>
PLIST

echo "==> (re)load LaunchAgents"
for p in com.trycua.driver com.remote-macos.tunnel com.remote-macos.keep-awake; do
  launchctl unload "$LA_DIR/$p.plist" 2>/dev/null || true
  launchctl load "$LA_DIR/$p.plist" && echo "    loaded $p"
done

echo
echo "==> human-only steps (cannot be automated):"
echo "  1. Grant CuaDriver permissions:  cua-driver permissions grant"
echo "  2. Enable Remote Login:          sudo launchctl enable system/com.openssh.sshd && sudo launchctl kickstart -k system/com.openssh.sshd"
echo "  3. Auto-login + no lock (System Settings -> Users & Groups -> Login Options; Screen Saver -> Never)"
echo "  4. Add the server's SSH public key to ~/.ssh/authorized_keys"
echo
echo "Verify later with: bash ./scripts/doctor-mac.sh"
