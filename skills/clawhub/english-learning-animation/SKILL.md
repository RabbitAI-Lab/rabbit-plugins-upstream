---
name: english-learning-animation
description: Create or revise short, character-led English-learning animation videos with an English-only hook/cover, original editorial-cartoon visuals, distinct Qwen3-TTS VoiceDesign characters, and audio-driven scene timing. Use when the user asks for animated English lessons, dialogue-based language-learning shorts, cartoon ESL videos, or to improve their character voices, subtitles, cover, motion, or audiovisual synchronization.
---

# English Learning Animation

Create a coherent, original short-form English lesson. Prioritize a watchable scene over a slide deck with narration.

## Workflow

1. Define one communicative outcome and write an English-only script with 3–5 usable phrases, a natural dialogue, and a brief repeat-after-me close. Do not choose a target runtime first. Let the generated speech, necessary pauses, cover, and recap determine the final duration. Many lessons will naturally land near 25–45 seconds, but this is not a quota.
2. Build a shot list before generating visuals. Add a `semantic_contract` to `script.json`: topic, setting, visual brief, required scene tags, and stale terms that must never appear. Every scene needs `semantic_tags`. Give every voice segment a stable semantic owner such as `customer`, `barista`, or `narrator`; do not use gender as the long-term character identity.
3. Use Qwen3-TTS VoiceDesign when no reference audio exists. Create a short audition for every recurring role first; do not reuse one voice for multiple characters. Lock each approved role's `voice_profile` and add line-specific `performance` direction.
4. Generate an empty background plate and separate transparent character/prop cutouts that visibly match the current setting. A hotel lobby cannot stand in for a subway station, restaurant, or attraction. Use a layered animation system such as `paper-collage-remotion`; never animate a single flattened illustration as the whole video.
5. Place audio using actual generated durations, then make visual changes at segment starts, phrase beats, and turn changes. Never add dead air or extend scenes merely to reach a round-number runtime. During dialogue, keep the speaker visually primary; during narration, use an English phrase card or semantic graphic rather than pretending a character is speaking.
6. Render only after passing the quality gates below.

## Production Starter

Initialize a new project from the approved layered-animation baseline:

```bash
python <skill>/scripts/init_project.py <new-or-empty-project-directory>
```

Add the empty background plates and transparent cutouts at the asset paths declared in `script.json`; do not copy generated user content into the skill. Each speaking cutout should declare a `speaker` field matching the narration role id.

Generate role-separated audio with the bundled script:

```bash
python <skill>/scripts/generate_qwen3_voices.py voice-manifest.json \
  --model <local-qwen3-tts-voicedesign-checkpoint>
```

Use `voice-manifest.json` as the editable voice contract. Every row needs a semantic role id, English line, stable `voice_profile`, and line-specific `performance` instruction. The generator remains compatible with the older combined `voice_instruction` field.
Keep the manifest's generation seed for reproducible auditions. Device selection is automatic (`CUDA` → `MPS` → `CPU`); override it only when necessary.

If the Qwen3 path is unknown, discover it first:

```bash
python <skill>/scripts/find_qwen3_voicedesign.py
```

The model finder respects `HF_HOME`; pass `--cache-dir` for a nonstandard cache.

## Visual and Language Rules

- Start with a 2–3 second cover that says the learning promise in English. Default to a topic or benefit subtitle such as `Travel English · Speak Naturally`; do not put the total runtime on the cover unless the user explicitly requests it. Any runtime claim must come from the final measured render.
- Keep on-video language English-only for immersion. Put Chinese explanations in post copy or a separate study sheet only if requested.
- Keep all character layers opaque. Do not use opacity to de-emphasize a non-speaker; use mild saturation/scale contrast instead.
- Use low-frequency micro-motion only: roughly 1 px vertical travel and <= 1% scale change. Never use rapid sinusoidal shaking as a speaking cue.
- Treat subtitle/phrase-card timing as audio-driven. Show whole dialogue lines for comprehension; use short phrase progression only for deliberate practice beats.
- Keep phrase cards in `script.json` under `phrase_cards`, keyed by narrator segment id. The renderer must read this data; never leave topic-specific cards hard-coded in `video.tsx`.
- Preserve a repeatable visual system: original characters, no copied logos/layouts/assets, warm editorial illustration, strong hierarchy, readable English type.

## Quality Gates

Before delivery, verify the current render against `references/quality-gates.md`.

Run all pre-render gates with one command:

```bash
python <skill>/scripts/validate_project.py <project-directory>
```

This preflight also rejects missing topic/scene tags, stale prohibited terms, and hard-coded phrase-card logic. After rendering, inspect the generated cover and one review frame per segment against the `semantic_contract`; mechanical validation cannot decide whether an illustration truly depicts the requested setting.

After rendering, run the same acceptance pipeline with the final video. This also extracts the cover and one representative frame per spoken segment:

```bash
python <skill>/scripts/validate_project.py <project-directory> \
  --video <final.mp4> \
  --review-dir <review-frame-directory>
```

Use the individual gates below when diagnosing a failure.

Validate the lesson and voice contract:

```bash
python <skill>/scripts/validate_lesson.py voice-manifest.json
python <skill>/scripts/validate_contract.py voice-manifest.json script.json
```

Before rendering, validate that every declared character asset is a real opaque cutout rather than a flattened or ghosted plate:

```bash
python <skill>/scripts/validate_layers.py script.json public
```

After generating audio, check actual durations, declared scene windows, overlap, English-only captions, and speaker-to-layer ownership:

```bash
python <skill>/scripts/validate_timeline.py script.json public
```

After rendering, validate the stream and extract the cover plus one representative frame per spoken segment. Inspect all review frames before delivery:

```bash
python <skill>/scripts/validate_render.py out/final.mp4 --cover-frame work/cover-check.png
python <skill>/scripts/extract_review_frames.py \
  out/final.mp4 script.json work/review-frames
```

## Tool Routing

- Read and use `paper-collage-remotion` for cutout-layer animation and Remotion rendering.
- Use `imagegen` to create new bitmap background plates or cutouts.
- Use local Qwen3-TTS VoiceDesign for no-reference character voice generation. Keep its model path, role instructions, and audio assets local to the project.
- Use `ffprobe` to read actual audio/video duration and validate the final file.
