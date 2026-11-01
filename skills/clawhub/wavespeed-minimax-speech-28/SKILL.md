---
name: wavespeed-minimax-speech-28
description: Convert text to speech using MiniMax Speech 2.8 via WaveSpeed AI, in two versions with the same inputs - HD (minimax/speech-2.8-hd) and Turbo (minimax/speech-2.8-turbo, lower price). Supports up to 10,000 characters per request, hundreds of system voices across 40 languages plus trained voice-clone IDs, emotion, speed, volume and pitch control, pause markers, interjections such as (laughs), a pronunciation dictionary, and mp3 / wav / pcm / flac output. Use when the user wants to generate speech audio or a voiceover from text with MiniMax Speech 2.8.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI MiniMax Speech 2.8

Convert text to speech using MiniMax Speech 2.8 via the WaveSpeed AI platform: a high-definition text-to-speech model with natural pronunciation and clear articulation. Two versions share the same inputs:

- **HD**: `minimax/speech-2.8-hd`
- **Turbo**: `minimax/speech-2.8-turbo` (lower price per character)

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

The same platform is exposed as an MCP server: hosted at `https://api.wavespeed.ai/mcp` (browser sign-in) or locally with `npx -y @wavespeed/mcp@latest`; every example below maps onto `run_model` with the same model id and input fields.

## Quick Start

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.8-hd \
  -i text="Hello, welcome to WaveSpeed AI!" \
  -i voice_id="English_CalmWoman" \
  --json | jq -r '.outputs[0]')
```

For the Turbo version, use `minimax/speech-2.8-turbo` with the same inputs.

## API Endpoints

**Model IDs:** `minimax/speech-2.8-hd`, `minimax/speech-2.8-turbo`

Convert text to speech with configurable voice, emotion, speed, volume, pitch and audio format. Both endpoints take the same parameters.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | string | Yes | -- | Text to convert to speech. Max 10,000 characters. Use `<#x#>` between words to insert a pause of `x` seconds (0.01-99.99). Supports interjections, see [Interjections](#interjections). |
| `voice_id` | string | Yes | -- | A system voice ID (see [Voice IDs](#voice-ids)) or a voice ID you trained with [MiniMax voice clone](https://wavespeed.ai/models/minimax/voice-clone). |
| `speed` | number | No | `1` | Speech speed. Range: 0.5-2.0 |
| `volume` | number | No | `1` | Speech volume. Range: 0.1-10.0 |
| `pitch` | number | No | `0` | Speech pitch. Range: -12 to 12 |
| `emotion` | string | No | `happy` | One of: `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`, `neutral` |
| `english_normalization` | boolean | No | `false` | English text normalization; improves number reading |
| `pronunciation_dict` | string[] | No | -- | Custom pronunciations as `Alias/Pronunciation` entries, e.g. `Omg/Oh my god` (max 100) |
| `sample_rate` | integer | No | -- | One of: `8000`, `16000`, `22050`, `24000`, `32000`, `44100` |
| `bitrate` | integer | No | -- | One of: `32000`, `64000`, `128000`, `256000` |
| `channel` | string | No | -- | `1` (mono) or `2` (stereo) |
| `format` | string | No | -- | One of: `mp3`, `wav`, `pcm`, `flac` |
| `language_boost` | string | No | -- | Improve recognition of a language or dialect. See [Supported Languages](#supported-languages). |

### Example

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.8-turbo \
  -i text="The quick brown fox jumps over the lazy dog." \
  -i voice_id="English_expressive_narrator" \
  -i speed=1.0 \
  -i emotion="neutral" \
  -i format="mp3" \
  -i sample_rate=24000 \
  -i bitrate=128000 \
  -i language_boost="English" \
  --json | jq -r '.outputs[0]')
```

### Pause Control

Insert pauses using `<#x#>` where `x` is seconds (0.01-99.99):

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.8-hd \
  -i text="And the winner is <#2.0#> WaveSpeed AI!" \
  -i voice_id="English_CaptivatingStoryteller" \
  --json | jq -r '.outputs[0]')
```

### Interjections

Write these tags inline in `text`: `(laughs)`, `(chuckle)`, `(coughs)`, `(clear-throat)`, `(groans)`, `(breath)`, `(pant)`, `(inhale)`, `(exhale)`, `(gasps)`, `(sniffs)`, `(sighs)`, `(snorts)`, `(burps)`, `(lip-smacking)`, `(humming)`, `(hissing)`, `(emm)`, `(whistles)`, `(sneezes)`, `(crying)`, `(applause)`.

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.8-hd \
  -i text="I really did not expect that (laughs). Okay, let's start again." \
  -i voice_id="English_Comedian" \
  --json | jq -r '.outputs[0]')
```

### Pronunciation Dictionary

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.8-hd \
  -i text="Omg, the results are in!" \
  -i voice_id="English_Upbeat_Woman" \
  -i pronunciation_dict='["Omg/Oh my god"]' \
  --json | jq -r '.outputs[0]')
```

## Voice IDs

The live list (472 suggested IDs) is in the schema: `wavespeed schema minimax/speech-2.8-hd --json | jq -r '.properties.voice_id["x-suggestions"][]'`. A selection:

### English

| Voice ID | Description |
|----------|-------------|
| `English_CalmWoman` | Calm female voice |
| `English_Trustworth_Man` | Trustworthy male voice |
| `English_expressive_narrator` | Expressive narrator |
| `English_radiant_girl` | Radiant girl voice |
| `English_magnetic_voiced_man` | Magnetic male voice |
| `English_CaptivatingStoryteller` | Storyteller voice |
| `English_Upbeat_Woman` | Upbeat female voice |
| `English_GentleTeacher` | Gentle teacher voice |
| `English_ManWithDeepVoice` | Deep male voice |
| `English_ConfidentWoman` | Confident female voice |
| `English_Comedian` | Comedic voice |
| `English_WiseScholar` | Scholarly voice |
| `English_Aussie_Bloke` | Australian male voice |
| `English_Lucky_Robot` | Robot voice |

### General and special voices

`Wise_Woman`, `Friendly_Person`, `Inspirational_girl`, `Deep_Voice_Man`, `Calm_Woman`, `Casual_Guy`, `Lively_Girl`, `Patient_Man`, `Young_Knight`, `Determined_Man`, `Lovely_Girl`, `Decent_Boy`, `Imposing_Manner`, `Elegant_Man`, `Abbess`, `Sweet_Girl_2`, `Exuberant_Girl`, `whisper_man`, `whisper_woman_1`, `angry_pirate_1`, `massive_kind_troll`, `movie_trailer_deep`, `peace_and_ease`

### Other languages

Most IDs follow `{Language}_{VoiceName}`, for example `Japanese_DecisivePrincess`, `Korean_SweetGirl`, `French_CasualMan`, `German_FriendlyMan`, `Spanish_FriendlyNeighbor`, `Portuguese_FunnyGuy`, `Cantonese_GentleLady`, `Chinese (Mandarin)_News_Anchor`. Copy IDs exactly from the schema list: some contain spaces or full-width characters.

## Supported Languages

For `language_boost`: `Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`, `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`, `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`, `Italian`, `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`, `Czech`, `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`, `Malay`, `Persian`, `Slovak`, `Swedish`, `Croatian`, `Filipino`, `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`, `Nynorsk`, `Tamil`, `Afrikaans`, `auto`

## Pricing

Billed by text length. Estimates from `wavespeed price` (USD). Prices may change; check `wavespeed price <model-id> ...` or the model pages: [HD](https://wavespeed.ai/models/minimax/speech-2.8-hd), [Turbo](https://wavespeed.ai/models/minimax/speech-2.8-turbo).

| Model | 1,000 characters | 10,000 characters (max) |
|-------|------------------|-------------------------|
| `minimax/speech-2.8-hd` | $0.10 | $1.00 |
| `minimax/speech-2.8-turbo` | $0.06 | $0.60 |

## Tips

- Pick a `voice_id` that matches the text's language, and set `language_boost` for non-English or mixed-language text.
- Set `emotion` explicitly; the default is `happy`, so use `neutral` for narration or documentation.
- Use `<#x#>` pauses and interjections for pacing instead of extra punctuation.
- Turn on `english_normalization` when the text has many numbers, dates or amounts.
- Use Turbo for drafts and long batches, HD for final output; inputs are identical, so switching is just the model id.

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run minimax/speech-2.8-hd -h

# Estimate the cost (no generation, no charge)
wavespeed price minimax/speech-2.8-hd -i text="..." -i voice_id="English_CalmWoman"

# Save outputs to disk instead of only printing URLs
wavespeed run minimax/speech-2.8-hd -i text="..." -i voice_id="English_CalmWoman" --json --download "./out/{index}.{ext}"

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

A `run` that fails with a gateway or network error (502/503/504, connection reset, timeout) does NOT mean the task failed, and the submit request is never retried automatically, so re-running can create a duplicate paid task. Do not re-run immediately. If the error contains a task id (`task_id` / prediction id), keep checking it with `wavespeed show <id> --json` until its status is terminal (`completed`, `failed`, `cancelled`, `timeout`, `deleted`). If no id was returned, check recent predictions with `wavespeed history --json` (add `--model <id>`; default window is the last 24h) and re-run once only if none matches. A client-side wait timeout or an interrupted `run` does not mean the task failed: tasks can run for a long time, so do not give up after a fixed time.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
