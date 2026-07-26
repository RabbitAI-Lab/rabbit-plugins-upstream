# OcuClaw fresh install — Steps 1–13

**Guide version:** 2026-07-06 (1.0.6)

Return to the skill's SKILL.md for the guardrails, lane card, checklist, and
router at any time.

## Setup steps

### Step 1 · Prerequisites

GOAL: confirm the hardware is ready and the host meets the minimum version requirement.

CHECK: Ask the user — are the G2 glasses paired in the Even Realities app, and does Even Hub open on their phone? If not, stop: finish Even Realities onboarding first.

Set expectations: setup takes about 20–30 minutes; they'll need their phone, a terminal on this machine, and will create 1–2 passwords.

```bash
openclaw --version
```

VERIFY: version is ≥ 2026.6.9.   ·   If not → `HOST-OLD`.   ·   `openclaw: command not found` → OpenClaw itself isn't installed — installing OpenClaw is outside this skill: point the user at OpenClaw's official install docs, then re-enter here once `openclaw --version` works.

---

### Step 2 · Install the plugin

GOAL: get the OcuClaw plugin onto this OpenClaw host.

**Step 2 owns all first-time installs, both channels. B1 is for updating or rolling back an already-installed plugin — not for first installs.**

Skip if: `openclaw plugins list` already shows `ocuclaw` → go to Step 3.

Ask first (routing): "Are you installing the **beta** build from the OcuClaw Discord?" Route to beta only if they confirm they're a beta-testing Discord member; otherwise install stable.

**Stable (default):**
```bash
openclaw plugins install clawhub:ocuclaw
```

The install prints a notice like `ClawHub package "ocuclaw" is community; review
source and verification before enabling.` — that is a standard advisory for
community-channel packages (the release is security-scanned and source-linked),
**not an error**; say so and continue.

**Beta (only if the user confirmed they are a beta-Discord tester — betas ship on npm, not ClawHub):**
```bash
openclaw plugins install npm:ocuclaw@beta
```

(To install a pinned beta build instead: `openclaw plugins install npm:ocuclaw@<spec>`.)

The prefix pins the install source: `clawhub:` is the stable lane (ClawHub —
scanned, source-linked releases), `npm:` carries the beta channel and serves as
the stable fallback. If the OpenClaw build rejects the `clawhub:` prefix as an
unknown package (older hosts), install stable from npm instead:
`openclaw plugins install npm:ocuclaw`.

VERIFY: `openclaw plugins list` shows `ocuclaw`.   ·   If the install fails → `HOST-OLD`; for any other failure → `ESCALATE`.

---

### Step 3 · Relay token   [REQUIRED · the user runs this, never you]

GOAL: the user creates a relay password and sets it themselves so it never passes through you. The plugin's schema requires the token before it can be enabled — set it before Step 4.

Skip if: relayToken probe = 1 **and** the user still knows their token → go to Step 4. If probe = 1 but token forgotten → they set a new one with the same command below.

🔑 USER ACTION REQUIRED — you run this, I never see it.

Run this in your own terminal, replacing ONLY the quoted value (no `read`, no pipe, no extra flags). The value must be a real, non-empty password — you will re-type it on your phone in Step 9, so make it typeable:

```
openclaw config set plugins.entries.ocuclaw.config.relayToken "<your-relay-token>"
```

Then tell me "done." I will not continue until the relayToken probe returns 1.

⚠️ If the command errors `must have required property 'relayToken'`, the value came through empty — STOP and re-run it with a visible, non-empty value. Never set it empty, never proceed.

VERIFY: relayToken probe = 1.   ·   Still failing → `TERM-HELP`.

---

### Step 4 · Enable + agent tool access

GOAL: enable the plugin and ensure the agent can call OcuClaw's glasses-display tools.

Skip if: `openclaw plugins list` shows `ocuclaw` already enabled **and** the tool-access VERIFY below already passes → go to Step 5.

**Enable the plugin:**
```bash
openclaw plugins enable ocuclaw
```

**Grant lifecycle hooks** (non-secret but privacy-relevant — it allows the trusted OcuClaw plugin's lifecycle hook to access conversation state for per-session glasses display reset/cleanup; tell the user that's what it's for):
```bash
openclaw config set plugins.entries.ocuclaw.hooks.allowConversationAccess true --strict-json
```

**Grant agent tool access** — don't assume a runtime default; check the actual config. Local onboarding writes `tools.profile: "coding"` into new configs, and `coding` (or any restrictive profile, a `tools.allow` list, or a `tools.deny`) filters out plugin-owned tools — OcuClaw's `render_glasses_ui` would be invisible. Unset profile / `full` is permissive. Read the current policy first:
```bash
openclaw config get tools
```
("Config path not found" is expected when no policy is set — the command exits nonzero then; record it, it's not a blocker.)

Then, based on the output — config validation rejects `allow` and `alsoAllow` both set in the same scope, so use exactly one lane:
- `deny` contains `"ocuclaw"` or `"group:plugins"` → STOP and ask the user — deny wins over every allow, and removing a deny entry is their call.
- `allow` or `alsoAllow` already contains `"ocuclaw"` or `"group:plugins"` → nothing to do.
- `allow` exists and is non-empty → merge `"ocuclaw"` into `tools.allow`, preserving all existing entries. Do NOT add an `alsoAllow` beside it.
- Otherwise ("Config path not found", or no non-empty `allow`) →
  ```bash
  openclaw config set tools.alsoAllow '["ocuclaw"]' --strict-json
  ```
  If `tools.alsoAllow` already has entries, merge `"ocuclaw"` into them instead — never replace an existing list.

Takes effect at the Step 5 restart.

VERIFY: `openclaw plugins list` shows `ocuclaw` enabled, **and** `openclaw config get tools` admits `ocuclaw` — `"ocuclaw"` or `"group:plugins"` in `allow` or `alsoAllow` with no matching `deny` — or shows no tool policy at all / "Config path not found" (that is a pass).   ·   A rejection usually means the token didn't save → back to Step 3.

---

### Step 5 · Relay port + restart + verify

GOAL: bind the relay to a host-safe loopback port, then load the plugin.

**Step 5a — choose a safe wsPort (decide by value, not by emptiness).**

Read the current configured port (non-secret):
```bash
openclaw config get plugins.entries.ocuclaw.config.wsPort
```

Decide by value:
- **A specific non-`9000` value (e.g. `47800`)** → a deliberate choice; keep it, make no change. Go to Step 5b.
- **`9000` on an existing install** → working baseline wins: if the app connects (or connected until recently), keep `9000` and go to Step 5b. Migrate to the ladder below only if the relay is broken (bind errors), a Step 10 test proves the setup broken, or the user asks for the modern layout. (`9000` is avoided on fresh installs because it falls inside a reserved-port range on some Windows hosts.)
- **"Config path not found" (fresh default — expected; the command exits nonzero, record it), or a migration case from the row above** → pick a free port:
  - Target `47800`. Check whether it is free on this host (read-only):
    - **Linux:** `ss -ltnH "sport = :47800"` (no output = free)
    - **macOS:** `lsof -nP -iTCP:47800 -sTCP:LISTEN` (no output = free)
    - **Windows:** `netsh int ipv4 show excludedportrange protocol=tcp` (must not fall in a block) AND `netstat -ano | findstr :47800` (no line = free)
  - If `47800` is taken, walk the ladder re-checking each: `47800 → 43117 → 38271`. Use the first free one.
  - Then set it (replace `<port>` with the number you chose):
    ```bash
    openclaw config set plugins.entries.ocuclaw.config.wsPort <port> --strict-json
    ```
**Whichever branch applied — write the resulting wsPort into your lane card now** (`Relay wsPort: <port>`), including when you kept an existing value.

**Step 5b — container sub-step** (read the lane card):
- **Container: no** → skip this sub-step entirely.
- **Container: yes, network mode = host** → no changes; skip this sub-step.
- **Container: yes, network mode = bridge (or named network)**:
  - Bind (you may run this — non-secret):
    ```bash
    openclaw config set plugins.entries.ocuclaw.config.wsBind "0.0.0.0"
    ```
  - The Docker port publish (`127.0.0.1:<port>:<port>`) must be done on the host machine, not inside the container → walk **`DOCKER-RELAY-UNREACHABLE`** with the user now.

**Step 5c — restart.** Before restarting, give the restart warning (rule 5). Then, if you changed anything in **Step 4, 5a, or 5b**, or if the gateway is not already healthy with ocuclaw `Status: loaded`:
```bash
openclaw gateway restart
```
Only if you changed nothing in Steps 4–5 and the gateway was already healthy with the plugin loaded may you skip the restart.

VERIFY (always, before leaving Step 5 — never continue to Step 6 with an unloaded relay):
```bash
openclaw gateway status
openclaw plugins inspect ocuclaw
openclaw plugins inspect ocuclaw --runtime
openclaw plugins doctor
```
Pass = gateway healthy + `plugins inspect ocuclaw` shows `Status: loaded` + `plugins inspect ocuclaw --runtime` confirms runtime loading + `plugins doctor` reports no ocuclaw issues. (Unrelated warnings about other plugins don't block — only ocuclaw-specific failures do.)

Container lane adds: confirm the startup log line reads `relay service started on ws://0.0.0.0:<port>` (not `ws://127.0.0.1:…`); the warning `[ocuclaw] relay is bound to … inside a container` must be gone.

If the startup log shows a bind/port error (`EADDRINUSE`, `WSAEACCES`, "address already in use", "forbidden by its access permissions") → `RELAY-PORT-CLAIMED`. If the log shows the relayToken error verbatim → `ERR-RELAY-TOKEN`. Any other gateway failure → `GW-DOWN`.

---

### Step 6 · Tailscale on this machine

GOAL: install Tailscale — only devices on the user's tailnet can reach the relay; the phone can reach this machine from anywhere.

**Container lane:** Tailscale belongs on the HOST, not inside the container. Every `tailscale` command in Steps 6 and 7 goes to the user's host terminal.

Skip if: `tailscale status` already shows signed in → go to Step 7.

**Install (per OS):**

> **Why root:** Tailscale's daemon manages network interfaces, so install, `tailscale up`, and `tailscale serve` need elevation on Linux — standard Tailscale practice, scoped to exactly those commands. If the lane card says "user runs elevated," every `sudo` command in Steps 6–7 goes to the user.

Linux (needs root — if your lane card says "user runs elevated," hand this to the user):
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

macOS: install the **standalone package** from `tailscale.com/download` — it puts `tailscale` on PATH. If the user has the Mac **App Store** build instead, its CLI lives at `/Applications/Tailscale.app/Contents/MacOS/Tailscale`. **Write that full path into the lane card's `Tailscale CLI` row if the App Store build is used** — you'll need it in Step 7.

Windows: run the installer from `tailscale.com/download/windows`.

**Sign in (per OS):**

| OS | Sign in |
|---|---|
| Linux | `sudo tailscale up` — user opens the printed URL and logs in |
| macOS | Open the Tailscale app and sign in |
| Windows | Sign in from the tray app |

VERIFY: `tailscale ip -4` prints a `100.x.y.z` address.   ·   If not → `TS-AUTH`.

---

### Step 7 · Serve routes (two doors into the relay)

GOAL: expose the relay on the tailnet. Two routes, one purpose each:

| Port | Type | Used by |
|---|---|---|
| `:8444` | direct TCP (TLS-terminated) | the OcuClaw app (Step 9) |
| `:8443` | HTTPS proxy | Even AI's agent endpoint (Step 12) |

**Resolve `<port>`** from your lane card (`Relay wsPort`). If it is blank, re-read it now: `openclaw config get plugins.entries.ocuclaw.config.wsPort`. If that returns `9000`, apply Step 5a's decision first (a working existing `9000` setup keeps `9000` — the routes below then target it), then return here.

Skip if: `tailscale serve status` already shows both routes each proxying to `localhost:<port>` → go to Step 8. (If they proxy to a different port, re-run the commands below with the current `<port>`; if the old `tcp://…:8443` scheme appears **and the app doesn't currently connect** → `MIGRATE-8443` — if that old shape still works end-to-end, leave it: working baseline wins.)

**Run both commands for your OS** (substitute `<port>` from the lane card in both; on the macOS App Store build, use the lane card's `Tailscale CLI` path in place of `tailscale`):

Linux / macOS:
```bash
sudo tailscale serve --bg --tls-terminated-tcp=8444 tcp://localhost:<port>
sudo tailscale serve --bg --https=8443 http://localhost:<port>
```

Windows (Administrator PowerShell):
```powershell
tailscale serve --bg --tls-terminated-tcp=8444 tcp://localhost:<port>
tailscale serve --bg --https=8443 http://localhost:<port>
```

VERIFY: `tailscale serve status` shows both blocks each proxying to `localhost:<port>`:
```
|-- tcp://<node>.<tailnet>.ts.net:8444 (TLS terminated, tailnet only)
|--> tcp://localhost:<port>

https://<node>.<tailnet>.ts.net:8443 (tailnet only)
|-- / proxy http://localhost:<port>
```
If exactly one expected route is missing or still points at the wrong local backend, re-run just that route's command once more, then check `tailscale serve status` again — a route can need a second application after a port change. Still wrong after that single retry → `TS-PORT-CLAIMED` or `TS-SERVE-UNSUPPORTED` (or ESCALATE), never further blind re-runs.

Note the machine name `<node>.<tailnet>.ts.net` from that output — you'll use it in Step 9.   ·   Port already claimed → `TS-PORT-CLAIMED`; unknown command or flag → `TS-SERVE-UNSUPPORTED`.

---

### Step 8 · Phone joins the tailnet

GOAL: the user's phone becomes a trusted member of the same private tailnet as this machine.

Ask the user to: install Tailscale on their phone (App Store / Google Play), sign in with the **same account**, and leave the VPN toggle on. If their tailnet requires device approval, they approve it at `login.tailscale.com/admin/machines`.

VERIFY: `tailscale status` on this machine shows the phone, **and** the phone's Tailscale app shows "Connected." If several devices appear in `tailscale status`, ask the user which is their phone — trust the phone app's own "Connected" state as the source of truth.   ·   If not → `PHONE-NO-REACH`.

---

### Step 9 · OcuClaw app

GOAL: the user installs and connects the OcuClaw phone app to the relay on this machine.

Ask the user to: open the Even Realities app → Even Hub App Store → install and open OcuClaw → go to **Relay Server** and enter:

- **Address:** `wss://<node>.<tailnet>.ts.net:8444` (use the exact machine name from Step 7)

  ⚠️ The address must start with `wss://` (not `ws://`), and use port `:8444` — not `:8443` (that is the Even AI door), and not the relay's local `wsPort` (e.g. `47800`), which is loopback-only and the phone can never reach it.

  > **Common wrong addresses — do not mix these up:**
  > OcuClaw app relay address: `wss://<node>.<tailnet>.ts.net:8444`
  > Even AI agent URL: `https://<node>.<tailnet>.ts.net:8443/v1/chat/completions`
  > Local relay backend: `localhost:<wsPort>`

- **Token:** the relay password the user created in Step 3

Tap **Connect**.

VERIFY: the app shows "Connected" and OpenClaw Status fills in (session, model). Host-side confirmation: `openclaw logs` shows `[ocuclaw] relay client connected …` from the moment they tapped Connect.   ·   The app connects but then shows a version screen saying the **app is too old** for the installed plugin → `CLIENT-TOO-OLD` (troubleshooting).   ·   Anything else → `APP-CONNECT-FAIL`.

---

### Step 10 · End-to-end check

GOAL: confirm the full chain works — message sent, reply received, glasses display it.

Ask the user to: put on their glasses, then send "hello" from the app's Send Message box and read the reply on the glasses.

VERIFY: reply is visible on the glasses. Core setup is DONE — say so, warmly.

If not:
- App reported a send failure → `APP-CONNECT-FAIL`
- Message sent but no reply → `GW-DOWN`
- Reply visible in the app but glasses are dark → wake the glasses (double-tap), reopen OcuClaw inside Even Hub, and retry

---

### Step 11 · Voice input via Soniox   [OPTIONAL — recommended]

GOAL: let the user talk to the agent from the glasses instead of typing.

**Offer this step; let them skip to Step 12 if they prefer.**

Ask: "Would you like to set up voice input? You'll speak to me from the glasses and I'll transcribe it. It takes about 5 minutes and needs a Soniox account (free sign-up, requires a little credit for transcription). Say yes to continue or skip to move on."

If they want it:

1. Sign up at **soniox.com**, add a payment method, load a small credit balance.
2. In the Soniox dashboard, create an API key.

🔑 USER ACTION REQUIRED — you run this, I never see it.
Run this in your own terminal, replacing ONLY the quoted value (no `read`, no pipe, no extra flags):

```
openclaw config set plugins.entries.ocuclaw.config.sonioxApiKey "<your-soniox-api-key>"
```

Then tell me "done." I will not continue until the sonioxApiKey probe returns 1.

Once the probe returns 1: **if the user has already said yes to Even AI (Step 12) too**, you may skip this restart and let Step 12 Part C's single restart cover both keys — then run this step's VERIFY after that restart. Otherwise (Soniox only, or they want to prove voice before deciding on Even AI), give the restart warning (rule 5), then run:

```
openclaw gateway restart
```

VERIFY (after whichever restart applied — never test voice against a config the gateway hasn't reloaded): the user taps the microphone / listen button on their glasses and speaks a short phrase — it transcribes and appears as their message.   ·   If voice never activates or transcription fails → `ESCALATE` (note that voice input was the failing step).

---

### Step 12 · Even AI integration   [OPTIONAL — recommended]

GOAL: the Even AI wake word on the glasses gets answered by this OpenClaw session, not Even's default AI.

**Offer this step; let them skip to Step 12b if they prefer.**

Ask: "Would you like to wire up Even AI so your glasses' wake word goes to your OpenClaw? Saying yes routes all Even AI requests here. Say yes to continue or skip to move on."

If they want it:

**ORDER MATTERS: set the token first, then enable.** Config validation rejects enabling Even AI without its token already set.

**Part A — unlock Agent Configuration (Even Realities beta)**

This section is hidden until your Even Realities account is flagged for it. Sign in at `https://hub.evenrealities.com/hub` with the **same email** as your Even Realities account. Once signed in, an `Agent Configuration` section appears at the bottom of the app's Even AI settings. Propagation is not instant — if it is not there yet, wait a minute and fully force-close and reopen the Even Realities app on the phone.

**Part B — create a second password (the Even AI token)**

Create a strong password to use as the Even AI token (you will type it into the app in Part D).

🔑 USER ACTION REQUIRED — you run this, I never see it.
Run this in your own terminal, replacing ONLY the quoted value (no `read`, no pipe, no extra flags):

```
openclaw config set plugins.entries.ocuclaw.config.evenAiToken "<your-even-ai-token>"
```

Then tell me "done." I will not continue until the evenAiToken probe returns 1.

**Part C — enable Even AI (agent runs this)**

Once the probe returns 1, run:

```
openclaw config set plugins.entries.ocuclaw.config.evenAiEnabled true --strict-json
```

Then give the restart warning (rule 5), then run:

```
openclaw gateway restart
```

**Part D — configure the app (user, phone)**

Even Realities app → Settings → Even AI settings → Agent Configuration (at the bottom) → Add Agent:

- **URL:** `https://<node>.<tailnet>.ts.net:8443/v1/chat/completions`
- **Token:** the Even AI password set in Part B

⚠️ This is the OTHER door — the `https://…:8443/v1/chat/completions` URL, NOT the `wss://…:8444` relay address. Do not mix them up.

> **Common wrong addresses — do not mix these up:**
> OcuClaw app relay address: `wss://<node>.<tailnet>.ts.net:8444`
> Even AI agent URL: `https://<node>.<tailnet>.ts.net:8443/v1/chat/completions`
> Local relay backend: `localhost:<wsPort>`

VERIFY: the user triggers Even AI on the glasses (wake word or button); the reply comes from their OpenClaw session.

If not:
- `Agent Configuration` never appears in the app → the beta unlock hasn't propagated yet; re-check that hub.evenrealities.com was signed in with the correct account email, wait, force-close and reopen the Even Realities app, and try again
- Token mismatch or auth error → `ERR-EVENAI-TOKEN`
- Anything else → `ESCALATE`

---

### Step 12b · Easy bug reports   [OPTIONAL]

GOAL: pre-enable the in-app debug upload so a future problem is a two-tap bug report with real diagnostics, instead of a fresh troubleshooting session.

**Version gate first:** this lane needs plugin ≥ 1.3 — check `Version:` from `openclaw plugins inspect ocuclaw`. Below 1.3, skip this step silently (bug reports go via the Discord paste route in troubleshooting).

Ask: "One last optional thing — want me to enable easy bug reports? If OcuClaw ever misbehaves, you'd flip one switch in the app and tap **Send Bug Report**; the developer gets real diagnostics and you get a ticket number. Nothing is captured or sent until you do that. You can ask me to turn it off (or on) anytime later."

If they want it (both keys are non-secret — you run them; the upload gate requires BOTH):

```
openclaw config set plugins.entries.ocuclaw.config.externalDebugToolsEnabled true --strict-json
openclaw config set plugins.entries.ocuclaw.config.allowDebugUpload true --strict-json
```

Restart handling: if a Step 11/12 restart is still pending, let that single restart cover these keys too. Otherwise give the restart warning (rule 5), then `openclaw gateway restart`.

VERIFY: both keys read back `true` via `config get`. Nothing to test in the app now — the Send flow only matters when a problem exists.

If they decline: fine — the troubleshooting ESCALATE path enables the same thing on demand later. Note the decline and move on.

---

### Step 13 · Handoff

Return to the skill's SKILL.md, then load
`{baseDir}/references/wrap-feedback.md` only after the required checklist is
complete or the user intentionally skipped the optional steps (Soniox, Even
AI, easy bug reports).
