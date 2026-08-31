# Quality Gates

## Voice

- One stable Qwen3 VoiceDesign instruction per character.
- Use semantic role ids (`customer`, `barista`) and keep gender/age inside the voice profile rather than using them as identity keys.
- Character age, role, and delivery are visibly distinct in an audition.
- Every line combines a stable `voice_profile` with a line-specific `performance` cue.
- Audio duration is read from the generated file before timeline placement.

## Sync

- Voice manifest filenames, speakers, text, cover title, and cover duration exactly match the Remotion timeline.
- Each audio segment has a visual owner and a matching start frame.
- The narration role id matches a declared layer `speaker` or a cutout filename.
- Dialogue lines foreground the speaking character; narrator lines foreground an English learning graphic.
- No audio begins before its intended picture is visible.
- Captions or phrase cards begin and end with their audio segment.
- Declared audio windows contain the full measured waveform and do not overlap.

## Motion

- Background, characters, and props are separate layers.
- All character cutouts have a real alpha channel, transparent exterior pixels, and at least 88% fully opaque visible pixels.
- Reject a cutout if more than 12% of its visible pixels are semitransparent; this is the mechanical ghosting alarm.
- Speaking motion is subtle and low frequency; no jitter, flicker, or high-frequency scale oscillation.
- At least 4 distinct visual beats for a normal dialogue lesson; add more beats when the content needs them.
- Final runtime follows the generated speech and intentional pauses. Do not pad, trim, or hold a scene merely to hit a preferred integer or range.

## Semantic continuity

- `script.json` declares a `semantic_contract` and each scene carries topic-relevant `semantic_tags`.
- Each setting receives a setting-appropriate plate and props; do not repurpose a previous location merely because its visual style matches.
- Phrase cards are data-driven from `script.json`. No card may survive from a starter or earlier episode unless it belongs to the current lesson.
- Before release, inspect the cover and every extracted speech frame for setting, character role, phrase-card, caption, and dialogue consistency.

## Publishing

- Cover is 2–3 seconds, English-only, and states the learning outcome.
- Omit runtime from the cover by default. If the user explicitly requests a runtime claim, derive it from the final render and require it to match.
- Video surface contains no Chinese unless the user explicitly requests bilingual on-video subtitles.
- Validate resolution, codec, audio stream, and total duration with `ffprobe`.
- Extract the cover and one midpoint frame for every spoken segment; inspect character solidity, speaker emphasis, subtitle correctness, and composition.
