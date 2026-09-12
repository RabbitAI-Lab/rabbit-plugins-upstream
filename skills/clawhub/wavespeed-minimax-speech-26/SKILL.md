---
name: wavespeed-minimax-speech-26
description: Convert text to speech using MiniMax Speech 2.6 Turbo via WaveSpeed AI. Features ultra-human voice cloning, sub-250ms latency, 40+ languages, emotion control, and 200+ voice presets. Use when the user wants to generate speech audio from text.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI MiniMax Speech 2.6 Turbo

Convert text to speech using MiniMax Speech 2.6 Turbo via the WaveSpeed AI platform. Features ultra-human voice cloning, sub-250ms latency, 40+ language support, and emotion control.

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

Prefer MCP tools over shell commands? The same platform is exposed by [`@wavespeed/mcp`](https://github.com/WaveSpeedAI/mcp-server) (`npx -y @wavespeed/mcp`; tools `search_models`, `get_model_schema`, `get_price`, `upload_file`, `run_model`, `get_prediction`). It shares the CLI's stored login. Every example below maps one-to-one onto `run_model` with the same model id and input fields.

## Quick Start

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.6-turbo \
  -i text="Hello, welcome to WaveSpeed AI!" \
  -i voice_id="English_CalmWoman" \
  --json | jq -r '.outputs[0]')
```

## API Endpoint

**Model ID:** `minimax/speech-2.6-turbo`

Convert text to speech with configurable voice, emotion, speed, pitch, and audio format.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | string | Yes | -- | Text to convert to speech. Max 10,000 characters. Use `<#x#>` between words to insert pauses (0.01-99.99 seconds). |
| `voice_id` | string | Yes | -- | Voice preset ID. See [Voice IDs](#voice-ids) below. |
| `speed` | number | No | `1` | Speech speed. Range: 0.50-2.00 |
| `volume` | number | No | `1` | Speech volume. Range: 0.10-10.00 |
| `pitch` | number | No | `0` | Speech pitch. Range: -12 to 12 |
| `emotion` | string | No | `happy` | Emotional tone. One of: `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`, `neutral` |
| `english_normalization` | boolean | No | `false` | Improve English number reading normalization |
| `sample_rate` | integer | No | -- | Sample rate in Hz. One of: `8000`, `16000`, `22050`, `24000`, `32000`, `44100` |
| `bitrate` | integer | No | -- | Bitrate in bps. One of: `32000`, `64000`, `128000`, `256000` |
| `channel` | string | No | -- | Audio channels. `1` (mono) or `2` (stereo) |
| `format` | string | No | -- | Output format. One of: `mp3`, `wav`, `pcm`, `flac` |
| `language_boost` | string | No | -- | Enhance recognition for a specific language. See [Supported Languages](#supported-languages). |

### Example

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.6-turbo \
  -i text="The quick brown fox jumps over the lazy dog." \
  -i voice_id="English_expressive_narrator" \
  -i speed=1.0 \
  -i pitch=0 \
  -i emotion="neutral" \
  -i format="mp3" \
  -i sample_rate=24000 \
  -i bitrate=128000 \
  --json | jq -r '.outputs[0]')
```

### Pause Control

Insert pauses in speech using `<#x#>` syntax where `x` is seconds (0.01-99.99):

```bash
OUTPUT_URL=$(wavespeed run minimax/speech-2.6-turbo \
  -i text="And the winner is <#2.0#> WaveSpeed AI!" \
  -i voice_id="English_CaptivatingStoryteller" \
  --json | jq -r '.outputs[0]')
```


## Voice IDs

### English Voices (Popular)

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
| `English_PlayfulGirl` | Playful girl voice |
| `English_ManWithDeepVoice` | Deep male voice |
| `English_ConfidentWoman` | Confident female voice |
| `English_Comedian` | Comedic voice |
| `English_SereneWoman` | Serene female voice |
| `English_WiseScholar` | Scholarly voice |
| `English_Cute_Girl` | Cute girl voice |
| `English_Sharp_Commentator` | Sharp commentator |
| `English_Lucky_Robot` | Robot voice |

### General Voices

`Wise_Woman`, `Friendly_Person`, `Inspirational_girl`, `Deep_Voice_Man`, `Calm_Woman`, `Casual_Guy`, `Lively_Girl`, `Patient_Man`, `Young_Knight`, `Determined_Man`, `Lovely_Girl`, `Decent_Boy`, `Imposing_Manner`, `Elegant_Man`, `Abbess`, `Sweet_Girl_2`, `Exuberant_Girl`

### Special Voices

`whisper_man`, `whisper_woman_1`, `angry_pirate_1`, `massive_kind_troll`, `movie_trailer_deep`, `peace_and_ease`

### Other Languages

Voices are available for: Chinese (Mandarin), Cantonese, Arabic, Russian, Spanish, French, Portuguese, German, Turkish, Dutch, Ukrainian, Vietnamese, Indonesian, Japanese, Italian, Korean, Thai, Polish, Romanian, Greek, Czech, Finnish, Hindi, Bulgarian, Danish, Hebrew, Malay, Persian, Slovak, Swedish, Croatian, Filipino, Hungarian, Norwegian, Slovenian, Catalan, Nynorsk, Tamil, Afrikaans.

Voice IDs follow the pattern `{Language}_{VoiceName}` (e.g., `Japanese_KindLady`, `Korean_SweetGirl`, `French_CasualMan`).

## Supported Languages

For `language_boost`: `Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`, `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`, `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`, `Italian`, `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`, `Czech`, `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`, `Malay`, `Persian`, `Slovak`, `Swedish`, `Croatian`, `Filipino`, `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`, `Nynorsk`, `Tamil`, `Afrikaans`

## Pricing

$0.06 per 1,000 characters.

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run minimax/speech-2.6-turbo -h

# Quote the price first
wavespeed price minimax/speech-2.6-turbo -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run minimax/speech-2.6-turbo -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run minimax/speech-2.6-turbo -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
