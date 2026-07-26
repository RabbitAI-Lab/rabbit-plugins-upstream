---
name: omnihuman
description: Create OmniHuman audio-to-video tasks and helper tasks for human identification and subject-mask detection through RunAPI. Use when the user asks an agent to generate talking-head video from an image and audio file, identify human regions, or detect subject masks with OmniHuman. Default to the RunAPI CLI for one-off calls; use SDKs only when integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/omnihuman.md
provider_page: https://runapi.ai/providers/bytedance.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/omnihuman
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

# OmniHuman On RunAPI

Create OmniHuman audio-to-video tasks and helper tasks for human identification and subject-mask detection through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, editing, transformation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating OmniHuman into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/omnihuman`
- Python: `runapi-omnihuman`
- Ruby: `runapi-omnihuman`
- Go: `github.com/runapi-ai/omnihuman-sdk/go`
- Java: `ai.runapi:runapi-omnihuman`
- PHP: `runapi-ai/omnihuman`

## Variants

- Audio to video: generate talking-head video from a source image and driving audio with `runapi omnihuman audio-to-video`.
- Human identification: identify human regions in a source image with `runapi omnihuman human-identification`.
- Subject detection: detect subject masks in a source image with `runapi omnihuman subject-detection`.

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi omnihuman --help
runapi omnihuman audio-to-video --help
runapi omnihuman human-identification --help
runapi omnihuman subject-detection --help
```

Run one-off tasks:

```shell
runapi omnihuman human-identification --input-file identify-human.json
runapi omnihuman subject-detection --input-file detect-subject.json
runapi omnihuman audio-to-video --input-file audio-to-video.json
```

Submit asynchronously and poll separately:

```shell
runapi omnihuman audio-to-video --async --input-file audio-to-video.json
runapi wait <task-id> --service omnihuman --action audio-to-video
```

Use the same async pattern with `--action human-identification` or `--action subject-detection` for helper tasks.

Available commands: `audio-to-video`, `human-identification`, `subject-detection`.

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated videos, masks, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/omnihuman.md
- Audio-to-video variant: https://runapi.ai/models/omnihuman/1.5.md
- Human-identification variant: https://runapi.ai/models/omnihuman/1.5-human-identification.md
- Subject-detection variant: https://runapi.ai/models/omnihuman/1.5-subject-detection.md
- Provider comparison: https://runapi.ai/providers/bytedance.md
- Full model catalog: https://runapi.ai/models.md
