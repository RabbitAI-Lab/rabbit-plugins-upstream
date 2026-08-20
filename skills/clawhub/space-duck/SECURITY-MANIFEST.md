# space-duck — Security Manifest (byte-grounded)

Version: 0.8.6 (aligned with the space-duck family) · Generated 2026-08-11, updated 2026-08-17.
Rule: every claim cites file:line. No claim rests on an LLM "reading".
Scope note: this skill is large (~13k LOC of Python across ~40 scripts). This
manifest is a **complete disclosure of security-relevant surfaces** (egress,
credential custody, command execution, persistence) verified by deterministic
enumeration (`grep` across all scripts), not a line-by-line audit of every
function.

## Package hygiene
- Compiled `scripts/__pycache__/*.pyc` removed before this publish — source-only package.
- `_meta.json` carries no infra paths / tokens / HOME overrides (only ownerId, slug, version).

## Outbound hosts (complete egress allowlist)
Enumerated across every `.py`/`.sh` (all http(s) literals). Every host below is
part of the documented Space Duck / BYOB / MCP feature set:
- `https://beak.spaceduckling.com` — Space Duck API (`API_BASE`, pair.py:62). Identity, pecks, connections, workspace/action-log.
- `https://spaceduckling.com` — site + hosted assets.
- `https://api.telegram.org` — Telegram BYOB listener/send (opt-in).
- `https://clawhub.ai` — skill update checks.
- MCP preset endpoints (0.8.x MCP-client wave): `mcp.sentry.dev`, `docs.mcp.cloudflare.com`, `hooks.slack.com`, `discord.com` — only contacted when the user configures that MCP client.
- `docs.claude.com`, `github.com`, `nodejs.org` — documentation / version-check references.
- `http://fake-beak.local` — test fixture only (test_*.py), never a runtime host.
No egress to any host outside this list. Nothing is sent to a non-Spaceduckling
third party except the MCP client the user explicitly wires.

## Credential custody
- All local state under `~/.space-duck/` (config.json, sign_key.hex, inbox/, tg-inbox/, caches).
- `config.json` holds the beak key, written `chmod 0o600` (sign_key.py:60); dir `~/.space-duck`.
- Ed25519 signing key at `~/.space-duck/sign_key.hex` (sign_key.py:42), local-only; supports rotate-with-attestation (sign_key.py:34).
- Reads (does not transmit) host creds for wiring: `~/.claude.json`, `~/.openclaw/credentials/clawhub-gateway.json`.
- Beak key sent only as `X-Beak-Key` header to the Space Duck API (sign_key.py:15).
- **0.8.3 host-pin on peck-supplied fetch URLs [TT3]:** `_fetch_shared_mds_for_peck` (peck_listener.py) reads `fetch_url` from the (unauthenticated) inbound peck body. Before attaching the beak key, the URL host is now gated through `_apiguard.is_allowed_fetch_host` (_apiguard.py) — official `spaceduckling.com`/subdomain only, custom hosts require the explicit `allow_custom_api` opt-out (with stderr warning). Fail-closed: an attacker-supplied `fetch_url` never receives the beak key.

## Handoff target gating (0.8.3 [SDI-2])
- `peck_responder._send_handoff` fires a fresh peck at a duck named in the model's reply text (`HANDOFF_RE`). As of 0.8.3 the handoff target is gated client-side through `_check_permissions(cfg, my_sd, handoff_to)` (peck_responder.py) before sending — fail-closed if there is no permitted/active connection to that target. Owner is notified on block.

## Critic runs with no tools (0.8.4 [CRB-1])
- `peck_critic.py` reviews a draft reply (text in, JSON verdict out) using the local `claude` CLI. Its input embeds attacker-influenced inbound peck content.
- As of 0.8.4 it invokes `claude --print --tools "" --model <MODEL>` (peck_critic.py:93) — the **entire toolset is disabled**, replacing the earlier `--permission-mode bypassPermissions`. A prompt-injected critic cannot reach any tool; `--print` still runs non-interactively (nothing to approve).

## Command execution (disclosed — owner-in-the-loop)
- `telegram_listener.py:457` runs bash via `subprocess.run(..., shell=True, executable='/bin/bash')` in `_exec_pending()`.
- **Gate:** reachable only through `_handle_owner_approval_callback()` (telegram_listener.py:661) — an inline Telegram `callback_query` from the **owner** with data `sda:a:` (approve-run) or `sda:r:` (approve + 24h remember). A remote peck cannot reach this path directly.
- **Residual (disclosed):** `sda:r:` ("Run all") records the `action_kind` in `~/.space-duck/auto-approved.json` for 24h (telegram_listener.py:437-441); during that window same-kind actions run without a fresh tap. Owner-initiated, time-boxed, per-kind, 0600 file. Read-only kinds (show_beak_key, show_tunnel) auto-approve.
- No `os.system`, no `eval()`/`exec()` of remote input. The two `__import__('re')` uses (peck_responder.py:57,595) are lazy stdlib imports, not dynamic code execution.
- Other `subprocess` use is literal-arg process management (systemctl/launchctl/git/openclaw), not shell-interpolated remote input.

## Root-context file ownership (0.8.6 [F5])
- `peck_listener._align_inbox_ownership` (peck_listener.py:~100): when the listener runs as root AND the inbox dir (`~/.space-duck/inbox`) is owned by a non-root uid, newly written inbox files are `os.chown`ed to the dir owner and always `chmod 0o600`. Scope: own inbox files only, no path outside `INBOX`, wrapped in try/except (warn on failure). Purpose: a non-root responder must be able to read chain history the root listener wrote.

## Reply chain bounds (0.8.6 [RESP-A/B])
- Model reply is extracted from `<peck_reply>` tags (peck_responder.py) so CLI scaffolding text never ships as a peck; `<peck_done/>`/handoff/critic markers found in raw output are re-appended so gating (SDI-2 above) still fires. Missing tag → raw output fallback (logged).
- Sessions without an explicit `max_rounds` cap at `SPACEDUCK_MAX_ROUNDS` (default 6); short non-question farewell inbounds terminate the chain without a reply (owner notified) — bounds resource use and peer-driven chatter loops.

## Persistence
- `install_service.py` / `setup_listeners_supervised.sh` install user-level systemd/launchd units for the peck/telegram listeners — opt-in, with teardown scripts (`teardown_byob_bridge.sh`, uninstall paths).

## Not covered by this manifest
- Per-function audit of all ~40 scripts (this is a surface disclosure, not a full audit).
- Runtime behavior of remote endpoints (Space Duck API, Telegram, MCP targets) — out of package scope.
- Signing / GitHub provenance: ClawHub v0.9.0 exposes no signing command — registry-feature gap, not a code defect.
