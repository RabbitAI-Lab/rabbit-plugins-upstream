# Kleap OpenClaw skill

An [OpenClaw](https://docs.openclaw.ai) skill that lets any OpenClaw agent
**ship a live website or web app** — hosting, database, auth, forms, TLS and
a real domain included — driven entirely through the [`kleap`
CLI](https://github.com/Kleap-co/kleap) (`npx -y @eliottd/kleap@latest`, no
install required).

> **Status: not published.** This folder is a complete, ready-to-publish
> skill package. Per project policy, nothing gets pushed to ClawHub without
> explicit founder sign-off — see [`PUBLISHING.md`](./PUBLISHING.md) for the
> exact, one-time publish steps once that's given.

## What's in here

```
kleap-openclaw-skill/
├── SKILL.md                     the skill itself (frontmatter + instructions)
├── references/
│   ├── recipes.md                longer worked examples, loaded on demand
│   └── troubleshooting.md        exact error strings + recovery, loaded on demand
├── README.md                     this file
└── PUBLISHING.md                 step-by-step ClawHub publish notice
```

This matches the [OpenClaw skill format](https://docs.openclaw.ai/clawhub/skill-format):
a folder with a required `SKILL.md` (YAML frontmatter + Markdown body) and
optional supporting text files. `SKILL.md` stays short — only what's needed
to decide *when* and *how* to act. The longer walkthroughs and the exact
error-message reference live in `references/`, loaded by the agent only when
needed (the pattern OpenClaw's own `skill-creator` skill recommends).

## Why a *skill* on top of the CLI

The `kleap` npm package (WP2) already ships an OpenClaw-*shaped* CLI:
compact 1-3 line output, `--json` everywhere, clean exit codes, `npx -y` with
no install. But a bare CLI still leaves an agent guessing:

- which flags to use for a **non-blocking** build,
- how to recover when `publish` is **refused by the quality/design gate**
  (read the message → `edit` with a fix → retry, not loop `publish` blindly),
- when it's safe to say "it's live" versus when it's premature,
- what `<app>` accepts (id / slug / URL / connected domain — no lookup step).

The skill encodes those decisions once so every agent that installs it gets
them right immediately, instead of learning them the hard way from the CLI's
own error messages on a live user's site.

## Local install / test (before publishing)

Point OpenClaw at this folder directly — no ClawHub round-trip needed to try
it:

```bash
mkdir -p ~/.agents/skills
cp -r kleap-openclaw-skill ~/.agents/skills/kleap
openclaw skills list --eligible     # should list "kleap"
openclaw agent --message "Build me a one-page site for my bakery and put it online."
```

(Requires the target machine to have already run `npx -y @eliottd/kleap@latest
auth login` once, or `KLEAP_API_KEY` set — see `SKILL.md` → Setup.)

## Once published

```bash
clawhub install kleap
```

adds it to any OpenClaw install. See `PUBLISHING.md` for how that command
comes to exist.

## Relationship to the existing Claude skill

`Kleap-co/kleap`'s own `skill/SKILL.md` (already shipped, `Kleap-co/skills`)
targets **Claude** and is written against the **MCP tool names**
(`create_app(...)`, `check_task(...)`, ...) — correct for an MCP-native
client. OpenClaw agents drive tools through a shell/`exec` tool, not
JSON-RPC MCP calls, so this skill is written against the **CLI command
line** (`npx -y @eliottd/kleap create "..."`) instead, plus the
`metadata.openclaw` block (`requires.bins`, `envVars`, `emoji`, `homepage`)
that only OpenClaw/ClawHub read. They're deliberately two different files
for two different runtimes — not a duplicate to reconcile.

## License

ClawHub requires `MIT-0` for everything it hosts (no attribution required).
This package carries no separate license file for that reason — consistent
with `Kleap-co/kleap`, which is MIT.
