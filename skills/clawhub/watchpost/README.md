# `[` Watchpost skill — the safety net for your agent's spending

A distribution artifact for the "ungoverned" open-agent path: an
[Agent Skills](https://agentskills.io/specification) skill that teaches an agent
(OpenClaw, Hermes, or any agentskills-compatible runtime) to run every purchase
past Watchpost before paying, and to honor the verdict.

It's a plain `SKILL.md` (frontmatter + instructions) plus one helper,
`scripts/check-purchase.mjs`, that calls `POST /v1/verify` with the user's
connection token and returns the verdict via its exit code (0 approve, 2 review,
1 block/error).

## Try it locally

The script targets the official hosted API (`https://api.watchpost.systems`) —
the endpoint is hardcoded, not env-configurable, so the token can only ever go
there. To test against a local API instead, temporarily change the `base`
constant in `scripts/check-purchase.mjs`.

```bash
# WATCHPOST_TOKEN: a real connection token from the Watchpost app → Connections.
WATCHPOST_TOKEN=wp_your_connection_token \
node scripts/check-purchase.mjs '{"merchant":"too-good-deals.io","title":"Premium subscription","amountMinor":19900,"currency":"USD"}'
# → prints a "block" verdict and exits 1
```

## Publish

Same `SKILL.md` works for both registries (both follow the Agent Skills spec):

- **Install from ClawHub:** `openclaw skills install @lelis92/watchpost`.
- **Publish an update:** `npm i -g clawhub`, then `clawhub login`, then
	`clawhub skill publish ./ --slug watchpost --name "Watchpost" --version 0.1.7`
	(needs a GitHub account old enough to pass ClawHub's upload gate; skills are MIT-0).
- **agentskills.io / Hermes:** host the folder and list it in your
  `/.well-known/agent-skills/index.json`, or submit to the registry per its docs.

Publishing is an outward-facing step — do it from an account you control. The API
endpoint is hardcoded to `https://api.watchpost.systems` in the script and is not
env-configurable, so there's nothing to change before publishing: the user's
token can only ever reach the official Watchpost API.
