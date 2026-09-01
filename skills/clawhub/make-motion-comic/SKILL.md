---
name: make-motion-comic
description: Create or revise low-cost motion-comic videos from a story or script using consistent AI-generated keyframes, multi-character Chinese Edge TTS, captions, synthesized or licensed audio, and FFmpeg assembly. Use for 动态漫画、漫剧、条漫视频、animated manga/comic, narrated image-story shorts, vertical story videos, or when Codex must turn generated still images into a polished video without a generative video model; also use to diagnose or fix character drift, robotic TTS, subtitle timing, micro-jitter, shaky zoompan motion, audio balance, covers, and reusable episode production assets.
---

# Make Motion Comic

Produce a complete motion-comic episode from a script while keeping image identity, voice quality, motion smoothness, and source assets independently editable.

## Required route

1. Use the built-in Image Generator through the available `imagegen` skill for character sheets, keyframes, image corrections, and covers. Follow that skill's reference-image and save-path rules.
2. Use Edge TTS for Chinese production voice by default. Do not use macOS `say` for a final deliverable unless the user explicitly chooses its offline quality tradeoff.
3. Use FFmpeg for deterministic motion, audio mixing, captions, encoding, and inspection. A user may explicitly choose another video framework.
4. Run `scripts/preflight.sh` before producing media. Report missing required dependencies before continuing.

Edge TTS uses an unofficial client for Microsoft's online speech endpoint. It is free in normal use but needs network access and has no service guarantee. Retry transient failures; do not silently substitute a worse voice.

## Default production brief

Use these defaults when the user says “开始”“直接做” or otherwise authorizes an autonomous first pass:

- Format: 9:16, 1080×1920, 30 fps, H.264/AAC.
- Length: 45–90 seconds.
- Visuals: 6–12 keyframes; use a new image when story state changes, not at arbitrary time intervals.
- Structure: hook in 0–3 seconds, rule or dilemma, escalation, emotional reversal, final serial cliffhanger.
- Captions: render in post; never ask the image model to typeset dialogue.
- Audio: multi-character Neural voices, light ambience/SFX, no unverified copyrighted BGM.
- Review: inspect the character sheet, raw keyframe contact sheet, and final-video snapshots.

Read [references/story-and-shots.md](references/story-and-shots.md) before writing a new episode. Read [references/image-consistency.md](references/image-consistency.md) before generating images.

## Workflow

### 1. Establish the production package

Create a project-local working folder and a user-facing output folder. Preserve:

- script and shot table;
- character/world visual bible;
- one prompt per keyframe;
- raw keyframes;
- TTS manifest and voice-only mix;
- subtitle file and timed timeline;
- final mix, cover, contact sheet, and final video.

Keep temporary render fragments outside the user-facing output folder.

### 2. Write for motion comics

Write narration and dialogue before generating images. Assign every spoken line to a shot. Prefer two or three recurring characters and a small number of reusable locations. Use visual reveals, poses, props, lighting changes, and cuts rather than animation-dependent action.

Use the structure and duration guidance in [references/story-and-shots.md](references/story-and-shots.md).

### 3. Lock identity before keyframes

Generate one production visual bible with neutral full-body views, face closeups, signature clothing/accessories, and a world inset. Treat it as the identity source of truth.

For every keyframe:

- reference the original visual bible;
- optionally reference the previous shot only for pose or continuity;
- explicitly preserve face, hair, clothing, proportions, and signature props;
- label every reference image's role in the prompt;
- request no generated captions, speech bubbles, logos, or watermarks.

Do not build a pure A→B→C reference chain. It accumulates identity drift. Follow [references/image-consistency.md](references/image-consistency.md).

### 4. Generate and inspect keyframes

Generate each distinct shot with a separate built-in image call. Save final selected images into the project. Inspect full-size images and a contact sheet for:

- character identity and clothing;
- hand anatomy and person count;
- prop continuity;
- color and lighting continuity;
- focal area and subtitle-safe space;
- accidental text or watermarks.

Regenerate a failed shot with one targeted correction. Never continue from a visibly drifted reference.

### 5. Produce voices before final timing

Create a JSON TTS manifest from `assets/templates/tts-script.json`. Give recurring characters stable voices and stable rate/pitch settings. Use `scripts/synthesize_edge_tts.py` to generate one file per line with retries and resumability.

For Mandarin, start with:

- `zh-CN-XiaoxiaoNeural`: warm narrator;
- `zh-CN-XiaoyiNeural`: adult woman or a lightly raised-pitch child;
- `zh-CN-YunyangNeural`: controlled or authoritative man;
- `zh-CN-YunxiNeural`: younger, urgent man.

Punctuation controls acting. Use commas and ellipses sparingly; excessive ellipses make an episode drag. Read [references/audio-and-tts.md](references/audio-and-tts.md) before casting voices or mixing.

### 6. Build the real timeline

Measure generated voice files with `ffprobe`; voice duration overrides estimates. Build subtitle and shot timing from those durations plus deliberate pauses. Retiming must update all of:

- shot boundaries;
- subtitle in/out times;
- SFX placement;
- final card timing.

Never hardcode subtitle timing from the draft script.

Use `scripts/build_timeline.py` to create `voice.wav`, `subtitles.srt`, and `timeline.json` from the same TTS manifest:

```bash
python3 scripts/build_timeline.py \
  --manifest tts-script.json \
  --audio-dir audio/lines \
  --out timeline
```

### 7. Render deliberate, non-jittery motion

Use motion only when it supports attention or emotion:

- push in for realization or threat;
- pull out for isolation or consequence;
- pan to reveal information;
- hold still for shock, grief, or the final reveal.

Do not add camera shake as a generic “dynamic” effect. Do not run low-resolution `zoompan` directly at delivery size.

Render still-image motion with `scripts/render_still_clip.sh`. It uses an oversized working canvas, eased movement, Lanczos downsampling, and 30 fps defaults to prevent integer-coordinate stepping and line-art shimmer. Read [references/motion-and-qc.md](references/motion-and-qc.md) before implementing motion or diagnosing jitter.

### 8. Mix captions and audio

Keep captions separate from generated art. Use a stable bottom safe area, high contrast, and at most two short lines. Do not cover faces or required props.

Mix voice first, then ambience, transitions, and music. Duck beds under dialogue. Target approximately:

- integrated loudness: −16 LUFS for social video;
- true peak: no higher than −1.5 dBTP;
- clear dialogue at phone-speaker volume.

Use synthesized ambience/SFX or media with explicit reusable licensing. Record provenance for downloaded audio.

### 9. Verify before handoff

Run all applicable checks:

```bash
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate,sample_rate,channels -of json final.mp4
ffmpeg -v error -i final.mp4 -f null -
ffmpeg -hide_banner -i final.mp4 -vf blackdetect=d=0.3:pix_th=0.05 -an -f null -
ffmpeg -hide_banner -i final.mp4 -af loudnorm=I=-16:LRA=9:TP=-1.5:print_format=summary -f null -
```

Extract and inspect snapshots from the hook, each major reversal, the last spoken line, and the final card. Confirm the last subtitle does not overlap the final card.

Deliver the final video plus cover, script/shot list, subtitles, character bible, prompt set, keyframes/contact sheet, and reusable audio mix.

## Quality gates

Do not call the episode complete when any of these remain:

- system-quality or novelty TTS in a production track;
- character identity drift across keyframes;
- generated Chinese dialogue inside images;
- arbitrary camera motion on every frame;
- visible one-pixel stepping, shimmer, or unintended shake;
- subtitle/face overlap or subtitle/final-card overlap;
- clipped audio, unverified copyrighted music, missing codec/audio stream, or black gaps.
