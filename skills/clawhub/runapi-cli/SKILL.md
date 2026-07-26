---
name: runapi-cli
description: Install and use the RunAPI CLI as the universal execution layer for RunAPI models. Use when the user asks to run any RunAPI model from an agent, inspect auth, install RunAPI on a local machine/server/CI, pass JSON request bodies, wait for tasks, or automate RunAPI workflows from the terminal.
documentation: https://runapi.ai/models.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models
    primaryEnv: RUNAPI_API_KEY
    requires:
      bins:
      - runapi
    install:
    - kind: brew
      formula: runapi-ai/tap/runapi
      bins:
      - runapi
    envVars:
    - name: RUNAPI_API_KEY
      required: false
      description: Optional RunAPI API key; agents should prefer environment auth or saved shared config for headless use. Browser login can be completed with `runapi login` or the MCP `login` tool.
---

# RunAPI CLI

The `runapi` CLI is the universal execution layer for every RunAPI model that
ships a CLI service. Use it whenever an agent needs to run a one-off model task,
pass a JSON request body, wait for an async task, or script RunAPI from a
terminal, server, or CI job.

## Install

| Target | Command |
|---|---|
| macOS / Linux (interactive) | `brew install runapi-ai/tap/runapi` |
| Server / CI (headless) | `curl -fsSL https://runapi.ai/cli/install.sh \| sh` |
| Pin a specific version | `curl -fsSL https://runapi.ai/cli/install.sh \| sh -s -- --version v0.1.0` |

The installer detects OS and architecture (Linux and macOS, amd64 and arm64), verifies a SHA-256 checksum from `https://runapi.ai/cli/latest.json`, and refuses to write the binary if verification fails.

## Authentication

Check the current state first:

```shell
runapi auth status
```

| Source | How |
|---|---|
| Environment (agent/headless default) | Read `RUNAPI_API_KEY` from the environment |
| Saved config (agent/server/CI) | `printf '%s' "$RUNAPI_API_KEY" \| runapi auth import-token --token -` (writes `~/.config/runapi/config.json` with mode 0600) |
| Browser login (interactive fallback) | `runapi login` in a terminal, or the MCP `login` tool from an MCP host |

`RUNAPI_BASE_URL` overrides the default base URL.

The RunAPI MCP Server reads the same `~/.config/runapi/config.json` as the CLI. After `runapi login` or the MCP `login` tool completes, authenticated MCP tools can use the saved credentials after the host reloads config if needed.

Avoid `runapi auth import-token --token "$KEY"` directly — the value would be visible in `ps -ef` on shared hosts. Use stdin (`--token -`) or `RUNAPI_API_KEY` in the environment.

## Discover services, commands, and fields

The CLI is JSON-first: every service exposes typed commands, and each command
documents its request fields through `--help`. Always inspect before composing a
request instead of guessing flags.

```shell
runapi --help
runapi suno --help
runapi suno text-to-music --help
```

## Run a model

Pass the request body as JSON through `--input-file` (or `--input` for inline
JSON, or `-` for stdin). The default flow is synchronous and polls until the
task completes.

```shell
# Synchronous: submit and poll until done
runapi suno text-to-music --input-file request.json

# Asynchronous: submit and return immediately, then poll separately
runapi suno text-to-music --async --input-file request.json
runapi wait <task-id> --service suno --action text-to-music

# Inspect a task without waiting
runapi get <task-id> --service suno --action text-to-music
```

JSON responses go to stdout; progress lines go to stderr. Pipe to `jq` for downstream parsing.

## Account

```shell
runapi account info
runapi account balance
```

## Local callback listeners

Listener access requires the credential issued by `runapi login`; an ordinary imported API key cannot list callback candidates, read a Listen Signing Secret, or open a listener. This restriction applies only to listener operations: ordinary API keys can still create and query tasks.

Before running a listener from an agent, check the saved auth and list the current member's key metadata:

```shell
runapi auth status
runapi api-keys list --json
```

If the API returns `cli_listen_required`, explain that the imported key keeps its existing API access but cannot list or select listener keys. Ask the user to remove any `--api-key` or `RUNAPI_API_KEY` override, then complete `runapi login` in their terminal (or the MCP `login` tool) and retry `runapi listen`. Do not retry with an imported API key or a management key.

Each candidate contains `id`, `name`, `masked_token`, and `enabled`. Select an enabled stable `id`; names and masks are display context only, so renaming a key does not invalidate a stored selection. When more than one enabled key is available and the project does not identify one, present the candidates to the user instead of choosing one silently.

Selection precedence is:

1. `--callback-api-key-id <id>` for this invocation. It does not rewrite project config.
2. `callback_api_key_id` from `.runapi.toml` at the git root, or from the current directory outside a git repository.
3. The TTY selector. It writes the selected ID only after the server validates the listener session.

Non-TTY invocations never select automatically. Without a flag or config, the `callback_api_key_required` error includes the candidate list so an agent can choose explicitly.

Project config has one allowed field and is safe to commit:

```toml
callback_api_key_id = "token_abc123"
```

Do not add credentials, key names, masks, signing secrets, forwarding URLs, or `base_url` to `.runapi.toml`; unknown fields are rejected.

Pass the selected ID explicitly from an agent. The listener receives only tasks created with that API key:

```shell
runapi listen localhost:3000/webhooks/runapi --callback-api-key-id token_abc123
```

Startup output identifies the selected key by name, ID, and mask, prints the absolute project config path, and prints that key's stable Listen Signing Secret. To inject the secret without starting a listener, keep it out of logs and project config:

```shell
RUNAPI_WEBHOOK_SECRET="$(runapi listen --print-secret --callback-api-key-id token_abc123)"
```

If the secret is exposed, rotate only the selected key's Listen Signing Secret:

```shell
RUNAPI_WEBHOOK_SECRET="$(runapi listen --rotate-secret --callback-api-key-id token_abc123)"
```

This invalidates every active listener using the selected key without rotating its business API credential. Update each local verifier with the printed secret, then restart those listeners.

Recovery rules:

- A committed ID owned by another member is not reusable. Run `runapi api-keys list --json`, select that member's key, and pass its ID explicitly. Update the one-line project config only when the project should adopt that member-specific selection.
- `callback_api_key_unusable` means the selected key was disabled, discarded, or lost membership. The listener exits without falling back; list keys and select another one explicitly.
- After upgrading from the previous listener behavior, update the CLI, run `runapi login` again, restart listeners, and replace the old local webhook secret.

## Temporary files

Model commands accept readable local file paths in top-level media URL fields, such as `source_image_url`, `source_image_urls`, `reference_image_urls`, `first_frame_image_url`, `mask_url`, `upload_url`, or `source_audio_url`. The CLI uploads each local file before submitting the request and replaces the field value with the temporary URL. Remote `http://` and `https://` values stay unchanged.

Use `runapi files create` when you need an explicit temporary URL for reuse, or when the source is Base64 encoded or already hosted at another URL.

```shell
runapi files create ./image.png --file-name image.png
runapi files create --url https://cdn.runapi.ai/public/samples/mask.png --file-name image.png
runapi files create --base64 "$BASE64_IMAGE" --file-name image.png
```

The command returns JSON with `file_name`, `url`, `size_bytes`, `mime_type`, `created_at`, and `expires_at`. The returned `url` is a one-hour temporary File Upload URL. Use it in endpoint fields that accept media URLs; check the model/action docs for the exact field name. Add `--url-only` when a script needs only the temporary URL on stdout.

## Install the skill into another agent runtime

```shell
runapi agent install-skill --target claude    # ~/.claude/skills/runapi-cli/
runapi agent install-skill --target codex     # ~/.codex/skills/runapi-cli/
runapi agent install-skill --target gemini    # ~/.gemini/skills/runapi-cli/
runapi agent install-skill --target openclaw  # ~/.openclaw/skills/runapi-cli/
runapi agent list-targets                     # JSON list with resolved paths
runapi agent install-skill --target-dir <path>  # custom location
```

## Troubleshooting CLI/skill drift

This skill is installed independently from the `runapi` binary and usually
tracks the newest CLI behavior. If a command, action, flag, or input field
described here is unavailable or behaves differently, check the installed CLI
version and update it before changing the request:

```shell
runapi version
brew upgrade runapi-ai/tap/runapi
# or reinstall
curl -fsSL https://runapi.ai/cli/install.sh | sh
```

After updating, inspect the command help again:

```shell
runapi --help
runapi <service> --help
runapi <service> <action> --help
```

## Safety notes for agents

- Never paste API keys into example commands. Reference `RUNAPI_API_KEY` or `runapi auth import-token` instead.
- Do not run interactive `runapi login` by default from an agent. In MCP hosts, guide the user through the `login` tool; in terminal/headless contexts, prefer `runapi auth status`, `RUNAPI_API_KEY`, and stdin token import unless the user explicitly wants browser auth.
- Listener operations are the exception: when they return `cli_listen_required`, an imported key cannot recover. Explain that it keeps its existing API access but cannot list or select listener keys. Ask the user to remove any `--api-key` or `RUNAPI_API_KEY` override and complete browser-backed login; never store the returned credential or Listen Signing Secret in `.runapi.toml`.
- The CLI exits non-zero on validation failures, network errors, and timeouts. Check the exit code before assuming success.
- For long-running tasks, prefer `--async` plus a `wait` loop so the agent can release the shell promptly.
- RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Browse every RunAPI model and its CLI service: https://runapi.ai/models.md
