---
name: remote-macos-computer-use
description: Set up and use cua-driver (an MCP server) so an AI agent running on a remote/cloud host can drive a macOS desktop, with a persistent background daemon + reverse-SSH-tunnel wiring that survives reboots and stays in the background. Use when you want an agent on server A to click/type/capture on a Mac on another network, or to onboard a remote desktop onto any MCP-capable agent (Hermes, Claude Code, Codex, Cursor, OpenCode). Covers install, macOS TCC grants, remote login, reverse tunnel, per-agent MCP config, health checks, and safety (bounded mode).
---

# Remote macOS Computer Use via cua-driver MCP

Connect an agent running on a **remote/cloud host** to the **desktop of a Mac** on another network, so the agent can operate real macOS apps (open apps, click, type, screenshot) while the agent's memory/skills/schedules stay on the remote host.

## What this is (and is not)

- **Tool source = cua-driver** (an existing MCP server, `cua-driver mcp`). You are **not** writing a new MCP server.
- **This skill = the wiring/onboarding** to reach that MCP across a network and keep it running in the background.
- Tools exposed by the MCP look like `mcp__<server>__<tool>` in the agent, e.g. `mcp__mac_computer__list_apps`, `mcp__mac_computer__click`, `mcp__mac_computer__type_text`.

## Topology

```
[ AI Agent on server ] --( mcp_servers: <server> )--> /usr/bin/ssh -T -p <revport> --( reverse tunnel )--> Mac sshd :22
                                                                                                     |
                                                                                    cua-driver mcp --> CuaDriver.app daemon (TCC)
```

- The **agent core** runs on the server. The **cua-driver daemon** runs on the Mac (it must, because the desktop is there).
- Reachability uses a **reverse SSH tunnel** (Mac -> server) so the server can reach the Mac even when the Mac is behind NAT. No public port or Tailscale needed.

## Prerequisites

- A Mac that stays **logged in, awake, unlocked** (see "Background persistence").
- macOS Accessibility + Screen Recording grants for `CuaDriver.app`.
- SSH access **from the server to the Mac** (Remote Login enabled + the server's public key in the Mac's `~/.ssh/authorized_keys`).
- cua-driver installed on the Mac (`/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"`).

> **Privacy note:** replace every `<...>` placeholder with your own values. None of the scripts contain a real username or server address by default; you supply them via environment variables. The default `REMOTE_USER=ubuntu` is just the common cloud-image user and is not tied to anyone.

## Steps

### 1. On the Mac: install cua-driver + grants (guided)
```bash
/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"
cua-driver doctor                # verify install + permissions layout
cua-driver permissions grant     # opens macOS prompt; grant Accessibility + Screen Recording
```
The grant must be for `/Applications/CuaDriver.app` (the app identity), **not** a terminal.

### 2. On the Mac: enable Remote Login (needs admin, human step)
```bash
sudo launchctl enable system/com.openssh.sshd
sudo launchctl kickstart -k system/com.openssh.sshd
# or: System Settings -> General -> Sharing -> Remote Login -> ON
```
> macOS recently tightened `systemsetup -setremotelogin on` to require Full Disk Access. The `launchctl enable`/`kickstart` path avoids that. If sshd won't start, check `/etc/ssh/sshd_config` for stray **client** options (e.g. `ServerAliveInterval`, `ServerAliveCountMax`) — they are invalid there and make sshd exit immediately.

### 3. On the server: set up key auth to the Mac
On the server, generate a keypair, then add its public key to the Mac's `~/.ssh/authorized_keys`:
```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_mac
ssh-copy-id -i ~/.ssh/id_ed25519_mac.pub -p <revport> <mac_user>@127.0.0.1   # only after tunnel is up
```
Or copy the public key manually into `/Users/<mac_user>/.ssh/authorized_keys`.

### 4. On the Mac: run this skill's setup script (daemon + tunnel + keep-awake)
```bash
REMOTE_HOST=<server-ip> REMOTE_USER=<server_user> REVERSE_PORT=2299 \
  bash ./scripts/setup-mac.sh
```
This installs three Login Items (`~/Library/LaunchAgents`):
- `com.trycua.driver` — cua-driver daemon (RunAtLoad + KeepAlive).
- `com.remote-macos.tunnel` — reverse tunnel (keeps the server's `<revport>` -> Mac `:22`).
- `com.remote-macos.keep-awake` — `caffeinate -dimsu` so the Mac doesn't idle-sleep.

### 5. On the server: register the MCP in the agent config
Generate the exact config:
```bash
MAC_USER=<mac_user> REVERSE_PORT=2299 REMOTE_KEY=~/.ssh/id_ed25519_mac \
  SERVER_NAME=mac_computer python3 ./scripts/gen-mcp-config.py
```
For Hermes (`~/.hermes/config.yaml`) the result goes under `mcp_servers:`. For other agents, adapt `command`/`args` to that client's stdio MCP form. Then reload:
- Hermes (CLI/terminal): `/reload-mcp`, or start a **new session** (existing sessions keep their old tool set).
- Claude Code / Codex / Cursor: restart the client so it re-reads MCP config.

**Note on tool naming:** if an agent says it has no "mac_computer tool", it usually means the tools are named `mcp__mac_computer__*` and the session is stale — not that the server failed.

### 6. Verify end-to-end
```bash
bash ./scripts/doctor-mac.sh            # on the Mac: daemon, permissions, tunnel
# on the server:
hermes mcp test mac_computer            # Hermes
# raw (after the tunnel is up):
ssh -p <revport> -i ~/.ssh/id_ed25519_mac <mac_user>@127.0.0.1 cua-driver mcp   # then MCP initialize
```
Then ask the agent to run a **read-only** check:
> Use `mcp__mac_computer__list_apps` to list the macOS apps currently running. Do not use the agent's own `computer_use` (that drives the server, not the Mac).

## Background persistence ("always on, survives restart")

- The three LaunchAgents run at **login** (`RunAtLoad`) and auto-restart (`KeepAlive`), so after a Mac **reboot** they come back (if the Mac auto-logs-in).
- The tunnel wrapper loops (`sleep 5` + retry), so after the **server** reboots, the Mac reconnects within seconds.
- For true "headless, always drivable", the Mac must also:
  - **Auto-login**: System Settings -> Users & Groups -> Login Options -> automatic login.
  - **No screen lock**: set screen saver/lock to Never so the desktop session stays interactive.
  - **No sleep / lid**: keep it plugged in and lid open (or on an external display); `caffeinate -dimsu` covers idle/display/system sleep but not a closed lid on battery.

## Safety

You are giving an agent **GUI control of a machine**. Default to **`bounded`** mode (limit to a reviewed set of apps) instead of `standard` (input to every app). cua-driver does this at the daemon level:
```bash
cua-driver serve --permission-mode bounded --capability-manifest <path>   # in the daemon LaunchAgent
```
Also: require approval for destructive tools, keep the SSH key scoped to one account, and don't expose the tunnel/listener to the public internet (bind the reverse forward to `127.0.0.1` on the server, which is the default).

## Troubleshooting

- **"MCP server connected but tools not in session"** -> the session was built before the config change. Reload (`/reload-mcp`) or start a brand-new session.
- **`Connection closed` / no SSH banner on the Mac** -> sshd config has invalid client options, or the service isn't enabled. Check `/etc/ssh/sshd_config` and `sudo launchctl enable system/com.openssh.sshd`.
- **`connect_to 127.0.0.1 port 22: failed`** -> Mac sshd not up, or the tunnel was established before Remote Login was enabled; restart the tunnel.
- **Permissions lost after a macOS update** -> re-run `cua-driver permissions grant`; grants attach to the app bundle, so re-approve `CuaDriver.app`.
- **Apps without an AX tree** -> the agent falls back to pixel coordinates; use a strong vision model.

## Files

- `scripts/setup-mac.sh` — idempotent Mac-side setup (daemon, tunnel, keep-awake).
- `scripts/doctor-mac.sh` — health checks.
- `scripts/gen-mcp-config.py` — emits the `mcp_servers` fragment for the remote bridge.
- `templates/` — the exact LaunchAgent plists and tunnel wrapper this skill installs.
