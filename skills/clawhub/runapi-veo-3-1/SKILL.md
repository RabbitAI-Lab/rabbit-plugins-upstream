---
name: veo-3.1
description: Generate and edit video with Veo 3 through RunAPI. Use when the user asks an agent to create, edit, or transform video with Veo 3. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/veo-3.1.md
provider_page: https://runapi.ai/providers/google.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/veo-3.1
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

# Veo 3 on RunAPI

Generate and edit video with Veo 3 through RunAPI. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, editing, transformation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Veo 3 into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/veo-3.1`
- Ruby: `runapi-veo-3.1`
- Go: `github.com/runapi-ai/veo-3.1-sdk/go`

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi veo-3-1 --help
runapi veo-3-1 text-to-video --help
```

Run a one-off task (synchronous — polls until the task completes):

```shell
runapi veo-3-1 text-to-video --input-file request.json
```

Submit asynchronously and poll separately:

```shell
runapi veo-3-1 text-to-video --async --input-file request.json
runapi wait <task-id> --service veo-3-1 --action text-to-video
```

Available commands: `text-to-video`, `extend-video`, `upscale-video`.

For `text-to-video`, request JSON may include `duration_seconds` with `4`, `6`, or `8` seconds. Omit it to use the default.

Use `veo-3.1-lite` for high-volume 720p generation. Lite supports text, first/last frame, and reference requests, but does not accept `seeds` or `auto`; reference requests must use `16:9` and 8 seconds. Extend only completed `veo-3.1` Quality or `veo-3.1-fast` source tasks. The source task determines the continuation tier automatically, and Lite sources cannot be extended.

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/veo-3.1.md
- Provider comparison: https://runapi.ai/providers/google.md
- Full model catalog: https://runapi.ai/models.md

## Variants

- [Veo 3.1](https://runapi.ai/models/veo-3.1/veo-3.1.md)
- [Veo 3 fast](https://runapi.ai/models/veo-3.1/fast.md)
- [Veo 3 Lite](https://runapi.ai/models/veo-3.1/lite.md)
