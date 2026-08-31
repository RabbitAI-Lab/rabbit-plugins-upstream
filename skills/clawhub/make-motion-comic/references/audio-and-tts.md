# Audio and Edge TTS

## Default voice route

Use Edge TTS for zero-cost online Mandarin Neural speech when its service is available. It is an unofficial client and requires internet access. Run:

```bash
edge-tts --list-voices | rg '^zh-CN'
```

Do not silently fall back to macOS `say`; it is suitable for drafts and accessibility, not emotional drama.

If Edge TTS is unavailable after bounded retries, report the failure and offer a quality-preserving alternative such as an authenticated Neural TTS provider or a local expressive model.

## Cast voices

Keep voice identity stable across episodes. Recommended starting points:

| Role | Voice | Treatment |
|---|---|---|
| Warm narrator | `zh-CN-XiaoxiaoNeural` | rate −6% to +2%, pitch −3 to 0 Hz |
| Adult woman | `zh-CN-XiaoyiNeural` | rate −12% to 0%, pitch −5 to 0 Hz |
| Controlled man | `zh-CN-YunyangNeural` | rate −14% to −4%, pitch −10 to −4 Hz |
| Younger urgent man | `zh-CN-YunxiNeural` | rate 0% to +8%, pitch −4 to 0 Hz |
| Child | `zh-CN-XiaoyiNeural` | rate −12% to −4%, pitch +8 to +16 Hz |

Treat these as starting points. Generate a short audition when a new recurring cast is created.

## Acting through text

- Use full stops for conviction.
- Use a comma for a short breath.
- Use one ellipsis only for meaningful hesitation.
- Avoid repeated ellipses; Edge TTS may create long dead air.
- Split long exposition into separate line assets.
- Give urgent lines a faster rate instead of using exclamation marks everywhere.

## Manifest

Use `assets/templates/tts-script.json` and save one audio file per line. This enables:

- individual voice replacement;
- exact subtitle timing;
- per-line gain and pacing;
- resumable online synthesis.

Run:

```bash
python3 scripts/synthesize_edge_tts.py \
  --manifest tts-script.json \
  --out audio/lines \
  --speed 1.00
```

Use a small, pitch-preserving `--speed` adjustment only after hearing the generated pacing. Prefer 0.96–1.10. Do not accelerate poor acting into acceptable duration.

## Mix

- Normalize and lightly compress each voice asset.
- Keep ambience 12–20 dB beneath voice.
- Place SFX relative to measured line/shot times.
- Use sidechain ducking or keyframed bed volume under speech.
- Measure the finished program, not only the voice bus.

Target approximately −16 LUFS integrated and ≤−1.5 dBTP.

