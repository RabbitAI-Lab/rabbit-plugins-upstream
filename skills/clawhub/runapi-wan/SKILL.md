---
name: wan
description: Generate and edit video with Wan through RunAPI. Use when the user asks an agent to create, edit, or transform video with Wan. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/wan.md
provider_page: https://runapi.ai/providers/alibaba.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/wan
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

# Wan on RunAPI

Generate and edit video with Wan through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, editing, transformation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Wan into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/wan`
- PHP: `runapi-ai/wan`
- Ruby: `runapi-wan`
- Go: `github.com/runapi-ai/wan-sdk/go`

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi wan --help
runapi wan text-to-video --help
```

Run a one-off task (synchronous — polls until the task completes):

```shell
runapi wan text-to-video --input-file request.json
```

Submit asynchronously and poll separately:

```shell
runapi wan text-to-video --async --input-file request.json
runapi wait <task-id> --service wan --action text-to-video
```

Available commands: `text-to-video`, `image-to-video`, `speech-to-video`, `animate`, `text-to-image`, `edit-video`.

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/wan.md
- Provider comparison: https://runapi.ai/providers/alibaba.md
- Full model catalog: https://runapi.ai/models.md

## Variants

- [2.2 A14B text to video turbo](https://runapi.ai/models/wan/2.2-a14b-text-to-video-turbo.md)
- [2.2 A14B image to video turbo](https://runapi.ai/models/wan/2.2-a14b-image-to-video-turbo.md)
- [2.2 A14B speech to video turbo](https://runapi.ai/models/wan/2.2-a14b-speech-to-video-turbo.md)
- [2.2 animate move](https://runapi.ai/models/wan/2.2-animate-move.md)
- [2.2 animate replace](https://runapi.ai/models/wan/2.2-animate-replace.md)
- [2.5 text to video](https://runapi.ai/models/wan/2.5-text-to-video.md)
- [2.5 image to video](https://runapi.ai/models/wan/2.5-image-to-video.md)
- [2.6 text to video](https://runapi.ai/models/wan/2.6-text-to-video.md)
- [2.6 image to video](https://runapi.ai/models/wan/2.6-image-to-video.md)
- [2.6 edit video](https://runapi.ai/models/wan/2.6-edit-video.md)
- [2.6 flash image to video](https://runapi.ai/models/wan/2.6-flash-image-to-video.md)
- [2.6 flash edit video](https://runapi.ai/models/wan/2.6-flash-edit-video.md)
- [2.7 text to video](https://runapi.ai/models/wan/2.7-text-to-video.md)
- [2.7 image to video](https://runapi.ai/models/wan/2.7-image-to-video.md)
- [2.7 image](https://runapi.ai/models/wan/2.7-image.md)
- [2.7 image pro](https://runapi.ai/models/wan/2.7-image-pro.md)
- [2.7 R2V text to video](https://runapi.ai/models/wan/2.7-r2v.md)
- [2.7 video edit](https://runapi.ai/models/wan/2.7-edit-video.md)
