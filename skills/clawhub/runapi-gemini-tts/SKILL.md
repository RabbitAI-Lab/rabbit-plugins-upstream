---
name: gemini-tts
description: Generate multi-speaker speech with Gemini TTS through RunAPI. Use when the user asks an agent to synthesize dialogue or integrate Gemini TTS. Use the RunAPI CLI for one-off generation and the language SDK for application integration.
documentation: https://runapi.ai/models/gemini-tts.md
provider_page: https://runapi.ai/providers/google.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/gemini-tts
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

# Gemini TTS on RunAPI

Generate ordered multi-speaker dialogue with configurable voices, accents, styles, pacing, scene context, and sampling temperature.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, manual smoke tests, debugging, and user-requested command runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Gemini TTS into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

SDK packages:

- JavaScript / TypeScript: `@runapi.ai/gemini-tts`
- Python: `runapi-gemini-tts`
- Ruby: `runapi-gemini-tts`
- Go: `github.com/runapi-ai/gemini-tts-sdk/go`
- Java: `ai.runapi:runapi-gemini-tts`
- PHP: `runapi-ai/gemini-tts`

## Variants

- Gemini 2.5 Pro TTS: use `gemini-2.5-pro-tts`.
- Gemini 3.1 Flash TTS: use `gemini-3.1-flash-tts`.

Both variants accept the same speaker and dialogue request structure.

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Check authentication and inspect the current request schema:

```shell
runapi auth status
runapi gemini-tts text-to-speech --help
```

Run from a JSON request file:

```shell
runapi gemini-tts text-to-speech --input-file request.json
```

Submit without waiting and poll separately:

```shell
runapi gemini-tts text-to-speech --async --input-file request.json
runapi wait <task-id> --service gemini-tts --action text-to-speech
```

Each `dialogue_turns[].speaker_id` must match a configured `speakers[].speaker_id` in `Speaker N` format. Keep secrets in `RUNAPI_API_KEY` or saved CLI config.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/gemini-tts.md
- Provider comparison: https://runapi.ai/providers/google.md
- Full model catalog: https://runapi.ai/models.md
