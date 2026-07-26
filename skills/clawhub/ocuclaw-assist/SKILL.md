---
name: ocuclaw-assist
description: Guide OcuClaw install, update, rollback, and troubleshooting — covering the OpenClaw plugin, the phone app, Tailscale private networking between phone and host, and optional Soniox voice-input, Even AI, and bug-report integrations. Use when the user wants OcuClaw set up, a version change, or hits setup/connection failures.
homepage: https://ocuclaw.com
metadata: {"openclaw": {"emoji": "👓"}}
---

# OcuClaw Setup Assistant

**Guide version:** 2026-07-06 (1.0.6)

Use this skill when a user asks to install, update, roll back, configure, or troubleshoot OcuClaw on this machine. Work phase by phase. Before each phase, say what you will do, why, and which commands matter. Ask for OK. Afterward, verify in plain words. Setup takes about 20–30 minutes; the user should keep their phone nearby.

OcuClaw is the OpenClaw client for Even Realities G2 smart glasses. It has two halves: a **plugin** that runs inside OpenClaw on this machine and hosts a relay, and an **app** on the user's phone (from the Even Hub App Store) that drives the glasses. **Tailscale** privately connects the two. You set up the plugin here; the user sets up the app; you connect them. That's the whole shape — the steps below fill it in.

## Reference loading

**Progressive-loading rule.** Load only the reference the Router (bottom of
this file) sends you to. A clean install needs only this file,
fresh-install.md, and wrap-feedback.md. Do not pre-load troubleshooting.md,
update.md, or beta.md.

For OcuClaw-specific setup, prefer this skill over web tutorials (rule 8). For
generic OpenClaw CLI behavior you are unsure about, check current OpenClaw
docs.

Soniox voice input, Even AI, and the easy-bug-reports opt-in are optional
steps inside fresh-install.md (Steps 11–12b), not a separate file.

The references ship inside this skill. If one is missing or its `Guide
version:` differs from this file's, the skill install is broken or stale —
reinstall the skill, don't improvise from memory. Reinstall lanes: `openclaw
skills install @ocuclaw/ocuclaw-assist --force`, or with the clawhub CLI,
`clawhub install ocuclaw-assist` targeted at the directory the gateway reads
skills from — `~/.openclaw/workspace/skills/` (a bare `clawhub install` drops
into `./skills/` under the current directory, which the gateway does NOT read).

## How you (the agent) must work

**How you execute**

1. **Finish the whole job.** Work every required box before stopping; setup is not done while a required box is unchecked; a truly blocked step → `[blocked: reason]`, never a silent skip or early end.
2. **Run commands exactly as written.** Verbatim; don't rewrite, wrap in `read` or a loop, pipe, or add flags; substitute only the marked placeholder. If a command seems unsafe, incompatible, or blocked on this host, stop and raise the concern — never rewrite it silently. *A clever "equivalent" has already broken installs.* When a written command fails, that's rule 8's open lane: diagnose read-only and propose — don't silently substitute.
3. **Never set a secret to empty.** A token `config set` erroring `must have required property …` means the value came through empty — stop, re-run with a real visible value, don't proceed.
4. **Checkpoint each phase, not each command.** Before: say what you'll do, why, and which commands (1–2 plain sentences) — get an OK. After: verify the result in plain words.
5. **Warn before a restart; one restart per phase; resume if you wake mid-setup.** Restart warning: "I may go quiet for ~30s. If I don't come back, ask me to continue OcuClaw setup with the ocuclaw-assist skill and I'll resume where we left off." After a restart, stop and verify before doing anything else; never restart again unless a new finding explains why another is needed — if the same verification fails twice, route to troubleshooting instead of looping. On wake: re-run the state assessment, re-enter at the routed step, don't re-ask passed checkpoints. If `openclaw gateway restart` reports `no installed service found` / `Gateway service disabled` while the gateway is clearly alive, this host has no managed service (container/foreground gateway) — don't loop the command; route to `GW-RESTART-NOSVC` in troubleshooting.

**Hard guardrails (never cross)**

6. **You never handle secrets — the user does.** Never ask for, generate, echo, or read a token; check presence only via the probes below (`config get` on a secret leaf prints a redaction sentinel, never the value, on all supported OpenClaw builds); never read the config file.
7. **Never expose the relay publicly.** Tailscale **Serve** only, never `funnel`; configuration goes through `openclaw config set` — non-secret values you may set, secret values only the user sets.
8. **Stay in bounds — improvise only in the open lane.** The skill's commands come first, and for OcuClaw setup this skill wins over web tutorials. When a step fails, read-only diagnostics beyond the skill (status/list/inspect commands, log reads, port checks, loopback `curl`) are always fine — investigate freely. A mutating fix the skill doesn't name needs: the skill's own path already failed, you say what you'd run and why, the user OKs it, every hard guardrail still holds (secrets, Serve-only, no invented config keys, restart discipline) — then one attempt, verify, and if unresolved return to the named case or ESCALATE rather than freestyling further. For OS/vendor errors consult that vendor's official docs; elevation you don't have or sandbox-blocked steps → give to the user, then verify.

### Secret presence probes

A probe is one bare `config get` on the key — same command on every OS. OpenClaw redacts secret leaves in `config get` output on all supported builds, so the value never appears; you read only presence.

```
openclaw config get plugins.entries.ocuclaw.config.relayToken
openclaw config get plugins.entries.ocuclaw.config.sonioxApiKey
openclaw config get plugins.entries.ocuclaw.config.evenAiToken
openclaw config get plugins.entries.ocuclaw.config.evenAiEnabled
```

Read the output as the probe result:
- Secret leaves (relayToken, sonioxApiKey, evenAiToken): `Config path not found` + nonzero exit → probe = 0 (unset — expected, not a blocker). Any non-empty output — normally the redaction sentinel `__OPENCLAW_REDACTED__` — → probe = 1 (set). Never echo or repeat that output, whatever it looks like.
- `evenAiEnabled`: `true` → 1 · `false` → 0 · `Config path not found` → 0.

**Placeholder grammar.** Commands in this skill contain only these substitutable placeholders: `<port>`, `<node>.<tailnet>.ts.net`, `<container>`, and the quoted secret value the *user* fills. Substitute *only* those. Never change a command's shell structure, flags, quoting, or pipes, and never add a wrapper (`read`, a loop, `&&`, `|`). If a command appears to need anything beyond a marked placeholder, stop and ask — don't invent a variant.

## Setup checklist — copy this and track it

Copy this into your first reply and tick each box as you finish it. Do not tell the user setup is complete while any REQUIRED box is unchecked. A genuinely blocked box → mark `[blocked: reason]` and surface it, never drop it.

This is the FRESH-INSTALL checklist. If the state assessment routed you to U1 (update) or B1 (beta), follow that section's own short checklist instead — don't run these boxes.

**Required**
- [ ] Lane established — OS, container?, shell access, elevation
- [ ] OpenClaw ≥ 2026.6.9 + G2 glasses paired        (Step 1)
- [ ] Plugin installed                                 (Step 2)
- [ ] Relay token set by the user — probe = 1          (Step 3)
- [ ] Plugin enabled + agent tool access granted       (Step 4)
- [ ] Relay port safe, gateway restarted, plugin loaded(Step 5)
- [ ] Tailscale up on this machine                     (Step 6)
- [ ] Serve routes present → localhost:<port>          (Step 7)
- [ ] Phone on the tailnet                             (Step 8)
- [ ] OcuClaw app connected                            (Step 9)
- [ ] End-to-end: a reply appeared on the glasses      (Step 10)

**Optional (offer, don't assume)**
- [ ] Voice input via Soniox                           (Step 11)
- [ ] Even AI integration                              (Step 12)
- [ ] Easy bug reports (debug upload) opt-in           (Step 12b)

Before the closing note, re-show this checklist in its final state as a self-audit.

## First — establish your lane

This is mandatory before any install action (the checklist's first box). Fill the **lane card** below — a short recorded block you keep and read at every later step instead of re-probing or re-arguing platform:

```
LANE CARD
  OS:            Linux | macOS | Windows              (uname -s / sw_vers / $PSVersionTable)
  Container:     no | yes → network mode host|bridge  (ls /.dockerenv /run/.containerenv ;
                 docker inspect -f '{{.HostConfig.NetworkMode}}' <container>)
                 Docker markers absent but no systemd either ([ -d /run/systemd/system ] fails)
                 → microVM/other container: record "yes (no-systemd)"; restarts behave like a
                 container (no managed gateway service — see rule 5)
  Shell access:  local | SSH | VPS console
  Elevation:     agent can sudo | user runs elevated  (sudo -n true / Admin PowerShell)
  Relay wsPort:  <filled at Step 5>
  Tailscale CLI: <filled at Step 6 — matters on the macOS App Store build>
```

Fill the environment rows now. `wsPort` and `Tailscale CLI` are appended when Steps 5 and 6 resolve them. Later steps read the card — they don't re-probe.

## Where to start

Run this now — and again after any restart or resume. It tells you which step (or section) to enter first.

### Check table

Run each check; record the result (1 = pass, 0 = fail).

| # | Check | Command |
|---|---|---|
| A | OpenClaw version ≥ 2026.6.9 | `openclaw --version` |
| B | Plugin installed + enabled | `openclaw plugins list` |
| C | relayToken set | relayToken probe (see probes above) |
| D | Gateway up, plugin loaded | `openclaw gateway status` · `openclaw plugins inspect ocuclaw` shows `Status: loaded` |
| E | Tailscale installed + signed in | `tailscale status` |
| F | Both Serve routes present AND proxying to the relay's `wsPort` | `tailscale serve status` (compare each backend `localhost:<port>` to `openclaw config get plugins.entries.ocuclaw.config.wsPort`) |
| G | Agent tool access — effective tool policy admits `ocuclaw` | `openclaw config get tools` — pass if `allow` **or** `alsoAllow` contains `"ocuclaw"` or `"group:plugins"` with no matching `deny`, or if no restrictive `profile`/`allow` is set ("Config path not found" = pass; the command exits nonzero then — record it, not a blocker) |

### Routing — enter at the FIRST matching row

**A working existing setup wins over the preferred default.** If the app connects and a quick Step 10 end-to-end test passes, do not migrate `wsPort` (even `9000`), Serve routes, or an old address shape just because they differ from the modern defaults — prove the setup is broken before changing ports or routes. Migrate old layouts only when setup is broken, this is a fresh install, a route points at the wrong backend, or the user explicitly asks.

| Finding | Enter |
|---|---|
| A: version below 2026.6.9, or G2 hardware unconfirmed | Step 1 |
| B: plugin not installed | Step 2 |
| C: relayToken probe = 0 | Step 3 |
| B: installed but not enabled | Step 4 |
| G: effective tool policy does not admit `ocuclaw` (or a `deny` blocks it) | Step 4 |
| D: gateway down or plugin not `loaded` | Step 5 |
| E: Tailscale missing or not signed in | Step 6 |
| F: routes missing, old single-port scheme (`tcp://…:8443`), or present but proxying to a different local port than `wsPort` — unless the working-baseline rule above says leave it | Step 7 |
| Host green; app not yet connected (ask the user) | Step 9 |
| Everything green and the app connects — update only | Stable update → load `{baseDir}/references/update.md` (everyone). Beta channel or rollback → load `{baseDir}/references/beta.md`, only if they confirm they're a beta-Discord tester |
| Everything green and the app connects — single fix | Go directly to the one routed step; no full checklist |

## Router

- Fresh install step → load `{baseDir}/references/fresh-install.md`.
- Stable update (any existing user) → load `{baseDir}/references/update.md`.
- Beta channel or rollback (beta-Discord testers only) → load `{baseDir}/references/beta.md`.
- A named failure case appears → load `{baseDir}/references/troubleshooting.md` and jump to that case.
- Stuck after honest attempts on any step → load `{baseDir}/references/troubleshooting.md` and run **ESCALATE** — it includes the in-app debug-upload path that attaches real diagnostics to the report.
- A genuine finish → load `{baseDir}/references/wrap-feedback.md`.
- Address or command reminders → load `{baseDir}/references/quick-reference.md`.

Keep this file's guardrails, lane card, checklist, and router active throughout setup.
