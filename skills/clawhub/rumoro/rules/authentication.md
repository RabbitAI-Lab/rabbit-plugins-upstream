# Authentication

Every request sends `Authorization: Bearer $RUMORO_API_KEY`. A key belongs to one workspace, so every call acts on that workspace and nothing else.

## The key

- Keys start with `ref_`. The full key is shown once, when it is created; Rumoro stores only its hash.
- A key has a `scope`: `write` runs the whole skill, `read` covers searching, analytics and people but changes nothing. A write with a read key answers `403 read_only_key`.
- A key can carry `expiresAt`, after which it stops working (useful for a contractor or a one-off script).
- `GET /v1/whoami` names the workspace and says whether the credential can write. Call it once when in doubt.

## Where keys come from

- The API keys page of the Rumoro dashboard (https://app.rumoro.dev). This is what to send the user to.
- `POST /v1/api-keys` with `name`, `scope` and an optional `expiresAt` creates one from an existing write key. Don't create keys unless the user asks, and hand a new key over once without storing it.
- `DELETE /v1/api-keys/{id}` revokes one. The API refuses it right away; cached checks catch up within a few minutes.

## The same key elsewhere

The CLI and both SDKs read the same key: `RUMORO_API_KEY` in the environment, or `rumoro auth:login`, which signs in through the browser and stores a key for the CLI in `~/.rumoro/config.json` (rules/cli.md). MCP clients can sign in with OAuth instead of a key; this skill uses the key.

## Care

Never print the key back, write it into a file the user did not ask for, or send it anywhere but `api.rumoro.dev`. If a request answers `401`, stop and tell the user to check `RUMORO_API_KEY` (SKILL.md, Setup) instead of retrying.
