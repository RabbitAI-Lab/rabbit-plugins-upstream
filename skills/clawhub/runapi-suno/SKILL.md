---
name: suno
description: Generate and transform music or compose lyrics with Suno through RunAPI. Use when the user asks an agent to create, extend, transform music/audio, generate or blend lyrics, prepare voice validation phrases, or create reusable custom voices with Suno. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.
documentation: https://runapi.ai/models/suno.md
provider_page: https://runapi.ai/providers/suno.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/suno
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

# Suno on RunAPI

Generate and transform music or compose lyrics with Suno through RunAPI, including lyric blending, voice validation phrase, and custom voice workflows. The default path for one-off agent tasks is the `runapi` CLI; SDKs are for application integration.

## Critical: Integration Runtime

- Integration work (app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production codebase) uses the **SDK integration path** for the target language.
- One-off generation, editing, transformation, manual smoke tests, debugging, or user-requested CLI runs use the **CLI path** with the `runapi` binary. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill.
- Never shell out to the `runapi` CLI as the production runtime integration layer.

## SDK integration path

When integrating Suno into an app, backend, worker, library, Rails service, Node service, Go service, webhook pipeline, or production workflow, start by checking the current SDK package and official usage. Confirm install commands, client methods (`create`, `get`, `run`), request fields, response shape, and error classes before using CLI help or raw HTTP examples. Use a RunAPI SDK package:

- JavaScript / TypeScript: `@runapi.ai/suno`
- PHP: `runapi-ai/suno`
- Ruby: `runapi-suno`
- Go: `github.com/runapi-ai/suno-sdk/go`

## CLI path

The `runapi` binary is the one-off and manual testing runtime dependency. For full CLI-specific agent guidance, see https://github.com/runapi-ai/cli-skill. Run `runapi auth status` first. For agents and headless runs, prefer `RUNAPI_API_KEY` or import it into saved config with `printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -`. Use `runapi login` only when the user explicitly wants interactive browser auth.

Inspect the available commands and request fields with CLI help:

```shell
runapi suno --help
runapi suno text-to-music --help
runapi suno blend-lyrics --help
runapi suno separate-audio-stems --help
runapi suno voice-to-validation-phrase --help
runapi suno regenerate-validation-phrase --help
runapi suno generate-voice --help
runapi suno check-voice --help
```

Run a one-off task (synchronous — polls until the task completes):

```shell
runapi suno text-to-music --input-file request.json
runapi suno blend-lyrics --input-file lyrics.json
runapi suno voice-to-validation-phrase --input-file voice-phrase.json
runapi suno generate-voice --input-file generate-voice.json
runapi suno check-voice --input-file check-voice.json
```

For advanced stem separation, set `type` to `split_stem_advanced` and include a target `stem_name`. The result contains the extracted stem and the remaining audio under `separated_audios.pairs`.

Submit asynchronously and poll separately:

```shell
runapi suno text-to-music --async --input-file request.json
runapi wait <task-id> --service suno --action text-to-music
```

Available commands: `text-to-music`, `extend-music`, `generate-artwork`, `cover-audio`, `add-instrumental`, `add-vocals`, `separate-audio-stems`, `generate-midi`, `convert-audio`, `visualize-music`, `generate-lyrics`, `blend-lyrics`, `get-timestamped-lyrics`, `replace-section`, `create-mashup`, `text-to-sound`, `voice-to-validation-phrase`, `regenerate-validation-phrase`, `generate-voice`, `check-voice`, `generate-persona`, `boost-style`.

For custom voice workflows: generate or regenerate a validation phrase, create a custom voice with `generate-voice`, then use the completed `voice_id` as `persona_id` with `persona_type: "voice"` on supported Suno v5 music generation endpoints. Use `check-voice` to confirm availability before depending on that voice in a generation request.

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/suno.md
- Provider comparison: https://runapi.ai/providers/suno.md
- Full model catalog: https://runapi.ai/models.md

## Variants

- [v4](https://runapi.ai/models/suno/v4.md)
- [v4.5](https://runapi.ai/models/suno/v4.5.md)
- [v4.5 all](https://runapi.ai/models/suno/v4.5-all.md)
- [v4.5 plus](https://runapi.ai/models/suno/v4.5-plus.md)
- [v5](https://runapi.ai/models/suno/v5.md)
- [v5.5](https://runapi.ai/models/suno/v5.5.md)
