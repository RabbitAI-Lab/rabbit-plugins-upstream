---
name: pixverse
description: Create, edit, transition, and extend PixVerse V6 videos through RunAPI. Use when the user asks an agent to create video from text, images, references, transitions, or a completed PixVerse task. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/pixverse.md
provider_page: https://runapi.ai/providers/pixverse.md
catalog: https://runapi.ai/models.md
metadata:
  author: runapi
  version: "0.1.0"
  openclaw:
    homepage: https://runapi.ai/models/pixverse
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
      description: Optional RunAPI API key; agents should prefer environment auth or saved CLI config. Browser login is interactive only.
---

# PixVerse on RunAPI

Create, edit, transition, and extend PixVerse V6 videos through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the SDK integration path for the target language.
- One-off generation, editing, transformation, manual smoke tests, debugging, or user-requested CLI runs use the CLI path with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating PixVerse into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/pixverse`
- Python: `runapi-pixverse`
- Ruby: `runapi-pixverse`
- Go: `github.com/runapi-ai/pixverse-sdk/go`
- Java: `ai.runapi:runapi-pixverse`
- PHP: `runapi-ai/pixverse`

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi pixverse --help
runapi pixverse text-to-video --help
runapi pixverse image-to-video --help
runapi pixverse edit-video --help
runapi pixverse transition-video --help
runapi pixverse extend-video --help
```

Run a one-off task:

```shell
runapi pixverse text-to-video --input-file request.json
runapi pixverse image-to-video --input-file request.json
runapi pixverse edit-video --input-file request.json
runapi pixverse transition-video --input-file request.json
runapi pixverse extend-video --input-file request.json
```

Submit asynchronously and poll separately:

```shell
runapi pixverse text-to-video --async --input-file request.json
runapi wait <task-id> --service pixverse --action text-to-video
```

Available commands: `text-to-video`, `image-to-video`, `edit-video`, `transition-video`, `extend-video`.

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated videos in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Continuation rules

- `extend-video` requires an account-owned completed RunAPI `source_task_id` from a PixVerse video task.
- Never substitute a caller-owned video URL for `source_task_id`.
- The continuation remains bound to the source task's execution path.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/pixverse.md
- PixVerse V6 model details: https://runapi.ai/models/pixverse/pixverse-v6.md
- Provider comparison: https://runapi.ai/providers/pixverse.md
- Full model catalog: https://runapi.ai/models.md
