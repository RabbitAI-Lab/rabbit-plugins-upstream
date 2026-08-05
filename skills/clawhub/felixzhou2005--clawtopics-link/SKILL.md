---
name: clawtopics-link
description: Install, bind, upgrade, verify, diagnose, or remove the official ClawTopics Embedded Link Plugin for an OpenClaw Gateway. Use for automatic ClawTopics cloud connection, Plugin 1.3.0 upgrades, one bounded safe Gateway restart, fresh runtime capability verification, and manual-restart recovery without re-enrollment or re-pairing.
---

# ClawTopics Embedded Link

Use only `@clawtopics/openclaw-link@1.3.0`. The native Plugin owns the long-lived
Control WSS and loopback Gateway tunnel. Docker, Linux, Windows and macOS use
the same Plugin flow; never install a Sidecar, Redis, supervisor, remote shell,
or a separate Connector daemon.

## Security boundary

- Never expose an Enrollment Code, Gateway credential, private key, ticket,
  route key, device token, or conversation frame in argv, logs, or responses.
- Never auto-approve an OpenClaw device request.
- Never use Docker, systemd, supervisor, OS signals, `gateway stop/start`,
  re-enrollment, or re-pairing as a restart fallback.
- The bundled installer may use `plugins install npm-pack:<verified-local-tgz>
--force` only after its fixed SHA-256 and package metadata checks. Never use
  `--force` with a URL, arbitrary archive, enrollment, or restart command.
- Run commands as the Gateway state-directory owner, not root.
- In automatic cloud setup, let ClawTopics Worker invoke the authorized
  `clawtopics-link.enroll` Gateway RPC. Do not run CLI enrollment.

## Install fixed Plugin 1.3.0

Resolve this Skill directory and execute exactly:

```bash
node <skill-dir>/scripts/install-or-upgrade.mjs
```

Do not reconstruct its download or installation as Agent-authored shell. The
script owns the complete bounded flow:

1. Require OpenClaw `>=2026.7.1 <2026.8.0`.
2. Download the fixed GitHub Release to a writable cache. Prefer the current
   directory, then `TMPDIR`, then `/tmp`. It uses a `.part` file, a 10 MiB
   maximum, three bounded attempts, SHA-256 verification, atomic rename, and
   local `npm-pack:` installation:

   ```text
   https://github.com/TekoAI/clawtopics-openclaw-link/releases/download/v1.3.0/clawtopics-openclaw-link-1.3.0.tgz
   ```

   The required SHA-256 is
   `e0ec1052729eb1e505b9511641490319331b02b4360747301fdb57abf99d2728`.
   Do not pass a remote URL to `openclaw plugins install`; affected OpenClaw
   versions reject URL specs. The script validates package name, Plugin id and
   version before its one reviewed `npm-pack:<local-tgz> --force` replacement.
   Some OpenClaw 2026.7.x builds install a managed npm-pack successfully but
   exit nonzero after a legacy extension-path warning. In that case the script
   continues only when `plugins list --json` proves the exact Plugin 1.3.0 is
   enabled, loaded, and has all required dependencies. It never trusts the
   warning text or a partial filesystem copy.

3. Set `plugins.entries.clawtopics-link.config.controlApiBaseUrl` to
   `https://openclaw.tekoai.com/api`, enable the Plugin, request plugin-only
   reconnect, and make two bounded runtime status checks. The Plugin appends
   `/v1`; never configure `/api/v1`.
4. The script verifies an existing Connector Identity is byte-identical after
   replacement. It prints exactly `CLAWTOPICS_PLUGIN_RUNTIME_CURRENT` when the
   active runtime is 1.3.0, otherwise
   `CLAWTOPICS_PLUGIN_RESTART_REQUIRED`.
5. On the restart-required marker, use the deterministic two-stage restart
   below. Do not improvise a shell restart command.

## Deterministic single restart

Resolve this Skill directory and run its bundled script. `setupRunId` is a
non-secret identifier supplied by ClawTopics.

### Stage 1: prepare only

```bash
node <skill-dir>/scripts/gateway-restart.mjs prepare \
  --setup-run-id <setupRunId>
```

This validates the fixed package, manifest, runtime hashes, enabled state,
config, persistent Connector identity and identity permissions. It records the
current `runtimeBootId` and writes a mode-0600 Restart Plan under:

```text
$OPENCLAW_STATE_DIR/plugins/clawtopics-link/gateway-restart-plans/
```

It never restarts anything. Return `CLAWTOPICS_PRE_RESTART_READY` and stop so
ClawTopics can persist the pre-restart state.

### Stage 2: execute once

Only in a later ClawTopics-authorized execution after Stage 1 was persisted:

```bash
node <skill-dir>/scripts/gateway-restart.mjs execute \
  --setup-run-id <setupRunId>
```

The script atomically claims the one local attempt and invokes exactly:

```text
openclaw gateway restart --safe --json
```

Accepted or unknown results emit `CLAWTOPICS_WAITING_FOR_FRESH_GATEWAY` and
only observe Presence. Explicit failure emits
`MANUAL_GATEWAY_RESTART_REQUIRED`. Never run Stage 2 again for that plan.

## Fresh runtime gate

Success requires the same Installation and Connector plus all of:

- `runtimeVersion=1.3.0`;
- a non-empty `runtimeBootId` different from the saved value (a saved null is
  allowed only as the legacy baseline);
- a new `controlConnectionId`;
- `connectedAt` at or after the restart request with five seconds clock skew;
- `control_wss_v1`, `gateway_tunnel_v1`, `long_wss_v1`, and
  `runtime_boot_identity_v1`.

The Plugin startup reconciler only reports this evidence; it never restarts.

## Manual recovery

If manual restart is required, tell the owner to restart Gateway in OpenClaw's
own UI or restart the whole OpenClaw instance/container. Do not reinstall,
re-enroll, or re-pair. After the owner clicks `我已重启，继续检查`, ClawTopics
opens a Presence-only observation window; do not invoke either restart stage.

## Terminal markers

Return exactly one applicable marker on its own line:

- `CLAWTOPICS_EMBEDDED_PLUGIN_ONLINE`
- `CLAWTOPICS_EMBEDDED_PLUGIN_READY`
- `CLAWTOPICS_EMBEDDED_PLUGIN_WAITING_WSS`
- `CLAWTOPICS_PLUGIN_RESTART_REQUIRED`
- `CLAWTOPICS_PRE_RESTART_READY`
- `CLAWTOPICS_WAITING_FOR_FRESH_GATEWAY`
- `MANUAL_GATEWAY_RESTART_REQUIRED`
- `PLUGIN_PRE_RESTART_FAILED`
- `PLUGIN_INSTALL_POLICY_DENIED`
- `PLUGIN_PREINSTALL_REQUIRED`
- `PLUGIN_STATUS_FAILED`

Never invent a success marker from installer prose. Use `status`/`doctor` and
the fresh Presence gate.
