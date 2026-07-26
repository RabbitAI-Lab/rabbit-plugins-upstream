---
name: volcengine-lip-sync
description: Generate lip-sync video with Volcengine Lip Sync through RunAPI. Use when the user asks an agent to sync mouth movement in a source video to an audio track. Default to the RunAPI CLI for one-off generation; use SDKs only when integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/volcengine-lip-sync.md
provider_page: https://runapi.ai/providers/bytedance.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/volcengine-lip-sync
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
      description: Optional RunAPI API key; agents should prefer environment auth or saved CLI config. Browser login is interactive fallback only.
---

# Volcengine Lip Sync on RunAPI

Generate lip-sync video with Volcengine Lip Sync through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Volcengine Lip Sync into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/volcengine-lip-sync`
- Python: `runapi-volcengine-lip-sync`
- PHP: `runapi-ai/volcengine-lip-sync`
- Java: `ai.runapi:runapi-volcengine-lip-sync`
- Ruby: `runapi-volcengine-lip-sync`
- Go: `github.com/runapi-ai/volcengine-lip-sync-sdk/go`

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi volcengine-lip-sync --help
runapi volcengine-lip-sync lip-sync-video --help
```

Run a one-off task (synchronous - polls until the task completes):

```shell
runapi volcengine-lip-sync lip-sync-video --input-file request.json
```

Submit asynchronously and poll separately:

```shell
runapi volcengine-lip-sync lip-sync-video --async --input-file request.json
runapi wait <task-id> --service volcengine-lip-sync --action lip-sync-video
```

Available commands: `lip-sync-video`.

## Required request shape

Use public RunAPI field names:

```json
{
  "model": "volcengine-lip-sync",
  "mode": "lite",
  "source_video_url": "https://cdn.runapi.ai/public/samples/volcengine-lip-sync-source.mp4",
  "source_audio_url": "https://cdn.runapi.ai/public/samples/volcengine-lip-sync-voice-adam.mp3"
}
```

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/volcengine-lip-sync.md
- Provider comparison: https://runapi.ai/providers/bytedance.md
- Full model catalog: https://runapi.ai/models.md
