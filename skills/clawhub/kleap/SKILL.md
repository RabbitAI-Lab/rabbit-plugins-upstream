---
name: kleap
description: "Ship a live website or web app end-to-end — hosting, database, auth, forms, custom domain — driven from this agent via the kleap CLI (npx, no install)."
version: 1.0.1
metadata:
  openclaw:
    requires:
      bins:
        - npx
    primaryEnv: KLEAP_API_KEY
    envVars:
      - name: KLEAP_API_KEY
        required: false
        description: "kleap_live_sk_... API key for headless/CI use. Not needed if `kleap auth login` already ran once (token cached in ~/.kleap/config.json)."
    emoji: "🌐"
    homepage: "https://kleap.co/mcp"
---

# Kleap — ship a live business from this agent

Kleap turns a prompt into a **live, hosted site** — not code the user still has
to deploy. Hosting, database, auth, forms and TLS are all included; every
publish is **verified-live** (Kleap only reports a URL once it has confirmed
the new version is actually serving — never a dead link).

Everything runs through `npx -y @eliottd/kleap@latest <command>` — no global
install required, nothing to compile.

## Setup (one-time per machine/account)

Pick one:

- **Interactive** — `npx -y @eliottd/kleap@latest auth login` opens a browser,
  no key to copy or paste. The token is cached in `~/.kleap/config.json`; every
  later `npx` call on this machine reuses it automatically.
- **Headless / CI** — set `KLEAP_API_KEY=kleap_live_sk_...` in the environment,
  or run `npx -y @eliottd/kleap@latest auth key <KEY>` once. Get a key at
  kleap.co → Settings → API key → MCP / API access.

Verify: `npx -y @eliottd/kleap@latest auth status` — exits `0` and prints one
line naming the active auth method (env key, browser login, or stored key; it
does not print the account), or exits `1` with
`✗ not signed in — run 'kleap auth login' or 'kleap auth key <KEY>'`. Do this
first if unsure — every other command fails fast with that same message
otherwise.

## Core workflow — ship a site

1. **Create**: `npx -y @eliottd/kleap@latest create "<detailed prompt>"`.
   Describe the business in one rich sentence — who it's for, tone, the
   sections it needs (e.g. "services + pricing + contact form"). This single
   call builds **and deploys**: it blocks (typically 1-5 min, up to ~15 for
   complex sites) and, on success, prints exactly:
   `✓ created app 4821 — https://warm-bakery-fold.kleap.io`
   That URL is already confirmed live — there is no separate publish step
   after a successful `create`.
2. Doing other work while it builds? Add `--no-wait --json` → returns
   `{ app_id, task_id, ... }` immediately; check back later with `status`.
3. Always capture the `app_id` (or slug/URL) from the output — every later
   command on this site needs it.

## Edit a site that already exists

`npx -y @eliottd/kleap@latest edit <app> "<specific change>"`. `<app>` accepts
a numeric id, a `slug.kleap.io` URL, a bare slug, or a connected custom
domain — resolved server-side, no lookup needed first. Be concrete ("change
the headline to 'Roasted slow' and make the CTA button orange"), not vague
("make it better"). Blocks until redeployed and prints the same
`✓ edited app ... — <url>` confirmation. Prefer editing over recreating — it
keeps everything that already works and is far cheaper.

## Connect a domain the user already owns

1. `npx -y @eliottd/kleap@latest domains search "<name>" [--tlds .com,.io]` —
   list available names. Kleap does not buy domains on the user's behalf —
   if they want a brand-new one, tell them to buy it elsewhere (or just keep
   the free `slug.kleap.io` `create` already gave them).
2. `npx -y @eliottd/kleap@latest domains connect <domain> <app>` — connects a
   domain the user **already owns**. The app must already be live (a
   completed `create`/`edit` already counts — no extra `publish` needed
   first). Prints the exact A record to set at their registrar. TLS
   auto-issues after DNS propagates — say "a few minutes to a few hours",
   never "instant".

## Check status anytime

`npx -y @eliottd/kleap@latest status <app>` → one line: name, id, and either
the live URL or "not published". Use this to confirm before telling a user
something is live, and to poll after a `--no-wait` create/edit.

`npx -y @eliottd/kleap@latest publish <app>` forces a redeploy without
changing content — rarely needed since `create`/`edit` already deploy; use it
if a user asks to "push it live again" with no new instruction.

## When a publish is refused or a build fails

`create` / `edit` / `publish` exit `1` with one line: `✗ <reason>` on stderr
(or `{"error":{"code":...,"message":...}}` on stdout with `--json` — every
error path honors `--json` as of CLI v1.2.1). Two families, same recovery:

- **A build/generation error** — the message names what broke. Run
  `edit <app> "fix: <describe the broken thing>"`, then check `status <app>`.
- **A publish refusal (quality/design gate)** — Kleap blocks publishing
  something visibly broken (blank hero, unstyled page) and keeps the
  previous working version live instead of overwriting it. The message
  describes what looked wrong. Fix it with
  `edit <app> "<describe the fix, referencing what the error said>"` — this
  redeploys through the same gate. Do not re-run `publish` unchanged; it will
  refuse again for the same reason.

**Retry budget: fix-and-retry at most twice.** If it still fails, stop and
tell the user exactly what the error said — never claim a site is live that
isn't.

## Conventions

- Every command accepts `--json` for machine-parseable output; without it,
  output is 1-3 human-readable lines by design (built for an agent reading
  its own tool output, not a terminal).
- Exit code `0` = success, `1` = failure — safe to gate on directly, no prose
  parsing needed for the happy path.
- `kleap list [--limit N] [--q text]` — the user's existing apps, one
  tab-separated row each (`id  name  url`), if you need to find one by name.
- `kleap screenshot <app>` — capture a preview screenshot URL, useful to show
  the result without the user opening a browser.

## The golden rule

Never tell the user a site is live until a command has actually confirmed it
— the `✓ ... — <url>` line from `create`/`edit`/`publish`, or `status <app>`
showing a live URL. A build *starting* is not a site being *online*.

## What good looks like

> User: "Make me a landing page for my dog-walking business in Austin and put
> it online."
> You run: `npx -y @eliottd/kleap@latest create "landing page for a
> dog-walking business in Austin, warm and friendly tone, services + pricing
> + contact form"`
> Output: `✓ created app 5310 — https://sunny-paws-walk.kleap.io`
> You reply: "It's live: https://sunny-paws-walk.kleap.io" — said only after
> that `✓` line confirmed it.

See `references/recipes.md` for the full create → domain → edit walkthrough,
non-blocking flows and JSON parsing; `references/troubleshooting.md` for
exact error codes and recovery.
