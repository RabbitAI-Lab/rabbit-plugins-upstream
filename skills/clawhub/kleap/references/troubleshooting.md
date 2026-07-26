# Kleap troubleshooting

Exact error shapes seen from the `kleap` CLI (verified by running the
published v1.2.1 tarball locally), and the recovery for each.

Error output contract (v1.2.1): plain mode prints `✗ <message>` on stderr;
`--json` mode prints `{"error":{"code":"<code>","message":"<message>"}}` on
stdout (codes seen: `not_authenticated`, `unknown_command`, `usage`,
`login_failed`) with nothing stray on stderr. Exit code `1` either way.
(Pre-1.2.1 builds printed some errors as plain text even with `--json`;
`npx -y @eliottd/kleap@latest` always gets the fixed version, so don't code
around that.)

## Not signed in

```
✗ not signed in — run `kleap auth login` or `kleap auth key <KEY>`
```
(with `--json`:
`{"error":{"code":"not_authenticated","message":"not signed in — ..."}}`)

Exit code `1`. This is the single most common failure — suspect it whenever a
first command in a session fails and nothing else has been tried yet. Fix:
`kleap auth login` (interactive) or set `KLEAP_API_KEY` / `kleap auth key
<KEY>` (headless), then retry the original command.

## Usage errors (missing/malformed arguments)

```
✗ usage: kleap edit <app> "<prompt>" [--no-wait] [--json]
✗ usage: kleap publish <app> [--no-wait] [--json]
✗ usage: kleap domains search <query> [--tlds .com,.io] [--json]
```
Exit code `1`. Self-explanatory — fix the invocation, don't retry as-is.

## Unknown command

```
✗ unknown command: <name>

kleap v1.2.1 — CLI for AI agents to build, edit and publish real websites (Kleap)
Usage:
  ...full help text...
```
(with `--json`: `{"error":{"code":"unknown_command","message":"unknown command: <name>"}}`)

Means a command name was invented. Re-check against `SKILL.md`'s command
list before retrying — the only commands are `auth`, `create`, `edit`,
`publish`, `status`, `list`, `domains search|connect`, `screenshot`, `mcp`.

## Errors before a build starts (create / edit)

The underlying API rejects some requests immediately, before any build task
is created — the CLI surfaces these as a normal `✗ <reason>` / exit `1`:

| Cause | What it means | What to do |
|---|---|---|
| `INSUFFICIENT_CREDITS` (402) | Account is out of credits | Tell the user to top up. **Do not retry** — it will fail again identically. |
| `VALIDATION_ERROR` (400) | The prompt or a flag was rejected | Fix the input (e.g. shorten/clarify the prompt) and retry once. |
| `UNAUTHORIZED` (401) | Key expired/revoked | Re-run `auth login` or `auth key`, then retry. |
| `RATE_LIMITED` (429) | Too many calls too fast | Back off (a few seconds) and retry — don't hammer it. |
| `NOT_FOUND` (404) | `<app>` doesn't resolve to a real app | Double-check the id/slug/domain, or run `list` to find the right one. |

## A build/task fails after it starts

`create`/`edit` normally block and only return once the build has finished
(success or failure), so most agents never see an intermediate "failed"
state directly — the command itself just exits `1` with the reason. Two
transient causes are worth a retry, everything else is not:

- **Transient stall** (the message reads like a timeout/stall, not a content
  problem) — re-run the **same** `edit`/`create` command up to twice. Kleap
  resumes from partial state; it does not start over from zero.
- **Generation failed** (the message describes a real problem with the
  content/prompt) — retry **once** with a refined prompt that addresses what
  the message said. If it fails the same way again, stop and report the
  exact message to the user. Never loop silently more than twice total.
- **Never** retry `INSUFFICIENT_CREDITS` or a `VALIDATION_ERROR` unchanged —
  see the table above.

## Publish refused by the quality/design gate

Kleap will refuse to publish a change that would make the live site visibly
broken (e.g. an empty/unstyled page, a blank hero section) and leaves the
previous good version live instead of overwriting it. This surfaces exactly
like any other `publish`/`edit` failure — a `✗ <reason>` line describing
what looked wrong, exit `1`. There is no special flag or bypass; the fix is
always the same:

1. Read the message — it names the visible problem (e.g. "page has no
   visible content" / "hero section renders empty").
2. `edit <app> "<describe the fix, referencing the problem>"`.
3. `status <app>` to confirm the new version is live.
4. If it refuses again for the same reason after one retry, stop and tell
   the user what's wrong rather than trying a third time.

The site a user already had stays live and correct throughout — a refused
publish is never a broken site in production, only a blocked *change*.

## Domain connect issues

`domains connect <domain> <app>` requires the app to already be live (a
completed `create`/`edit` counts). If it fails, check `status <app>` first —
connecting a domain to an app that was never actually published will fail
with a clear reason, not silently.
