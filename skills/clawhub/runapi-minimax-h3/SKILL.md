---
name: minimax-h3
description: Generate video from text, reference media, or first and last frames with MiniMax H3 through RunAPI. Use the RunAPI CLI for one-off generation and an SDK for application integration.
documentation: https://runapi.ai/models/minimax-h3.md
provider_page: https://runapi.ai/providers/minimax.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/minimax-h3
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
      description: Optional RunAPI API key; prefer environment auth or saved CLI config. Browser login is interactive fallback only.
---

# MiniMax H3 on RunAPI

Generate video with MiniMax H3 through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating MiniMax H3 into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/minimax-h3`
- Python: `runapi-minimax-h3`
- Ruby: `runapi-minimax-h3`
- Go: `github.com/runapi-ai/minimax-h3-sdk/go`
- Java: `ai.runapi:runapi-minimax-h3`
- PHP: `runapi-ai/minimax-h3`

The SDK resources are `textToVideo` / `text_to_video` and `imageToVideo` / `image_to_video`. Use `create`, `get`, and `run` for the asynchronous task lifecycle.

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Check authentication and inspect the live request contract:

```shell
runapi auth status
runapi minimax-h3 --help
runapi minimax-h3 text-to-video --help
runapi minimax-h3 image-to-video --help
```

Run and wait for completion:

```shell
runapi minimax-h3 text-to-video --input-file request.json
```

Submit asynchronously and poll later:

```shell
runapi minimax-h3 image-to-video --async --input-file request.json
runapi wait <task-id> --service minimax-h3 --action image-to-video
```

For prompt-only generation, `aspect_ratio` must be a fixed ratio. `adaptive` is available when `reference_image_urls` or `reference_video_urls` is present. `reference_audio_urls` cannot be used without reference images or videos. Image-to-video requests require `first_frame_image_url`, `last_frame_image_url`, or both.

## Generated file storage

Returned file URLs are temporary. Download generated files into durable storage within the retention window. Keep API keys in `RUNAPI_API_KEY` or RunAPI CLI config and never commit secrets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/minimax-h3.md
- Provider comparison: https://runapi.ai/providers/minimax.md
- Full catalog: https://runapi.ai/models.md
