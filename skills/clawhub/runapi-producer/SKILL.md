---
name: producer
description: Generate FUZZ music from exact lyrics or instrumental briefs with Producer through RunAPI. Use the RunAPI CLI for one-off work and the language SDKs for application integration.
documentation: https://runapi.ai/models/producer.md
provider_page: https://runapi.ai/providers/producer.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/producer
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
      description: Optional RunAPI API key; prefer environment auth or saved CLI config.
---

# Producer On RunAPI

Use the RunAPI CLI for one-off requests and manual verification. Use the target language SDK for applications, workers, libraries, and production integrations; never shell out to the CLI as an application runtime.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Producer into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: @runapi.ai/producer
- Python: runapi-producer
- Ruby: runapi-producer
- Go: github.com/runapi-ai/producer-sdk/go
- Java: ai.runapi:runapi-producer
- PHP: runapi-ai/producer

## Music modes

- exact_lyrics: provide lyrics and a prompt describing the music style and production.
- instrumental: provide a prompt and omit lyrics.

Both modes support `fuzz-2.0`, `fuzz-2.0-pro`, `fuzz-2.0-raw`, `fuzz-1.1-pro`, `fuzz-1.0-pro`, `fuzz-1.0`, `fuzz-1.1`, and `fuzz-0.8`.

## Variants

- [FUZZ 2.0](https://runapi.ai/models/producer/fuzz-2.0.md)
- [FUZZ 2.0 Pro](https://runapi.ai/models/producer/fuzz-2.0-pro.md)
- [FUZZ 2.0 Raw](https://runapi.ai/models/producer/fuzz-2.0-raw.md)
- [FUZZ 1.1 Pro](https://runapi.ai/models/producer/fuzz-1.1-pro.md)
- [FUZZ 1.0 Pro](https://runapi.ai/models/producer/fuzz-1.0-pro.md)
- [FUZZ 1.0](https://runapi.ai/models/producer/fuzz-1.0.md)
- [FUZZ 1.1](https://runapi.ai/models/producer/fuzz-1.1.md)
- [FUZZ 0.8](https://runapi.ai/models/producer/fuzz-0.8.md)

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. Prefer `RUNAPI_API_KEY` or import a token with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use browser login only when the user explicitly requests an interactive login.

Inspect current fields before creating a request:

~~~shell
runapi producer --help
runapi producer text-to-music --help
~~~

text-to-music is asynchronous. Run it directly to create and poll, or add --async and wait separately.

~~~shell
runapi producer text-to-music --input-file text-to-music.json
runapi producer text-to-music --async --input-file text-to-music.json
runapi wait <task-id> --service producer --action text-to-music
~~~

## Result Handling

Completed tasks return an audios array. Each result may include an audio URL, cover image URL, title, duration, lyrics, and the public model name. Generated media URLs are temporary; download and store them in durable storage.

## References

- Model overview: https://runapi.ai/models/producer.md
- Producer model details and pricing: https://runapi.ai/models/producer/fuzz-2.0.md
- Provider page: https://runapi.ai/providers/producer.md
- Full catalog: https://runapi.ai/models.md
