---
name: produce-voiceover-teaching-video
description: Turn a supplied narration audio file plus an article, notes, screenshots, or images into a fact-checked faceless vertical teaching video, synchronized captions, cover, publish copy, hashtags, and pinned comment. Use when a user provides a cloned or recorded MP3/WAV and wants a multi-agent edit with adjustable speech rate, semantic image placement, mobile-safe text, modern transitions, final QC, and social publishing assets.
---

# Voiceover Teaching Video Factory

Act as the director of a seven-worker production line. Treat the supplied narration as sensitive source material and the prepared narration duration as the timeline authority. Do not clone a voice, upload source media, or publish the finished video unless the user explicitly requests that separate action.

## Required setup

Require `ffmpeg`, `ffprobe`, Python 3.10+, and a video renderer capable of deterministic 9:16 output. Prefer HyperFrames when installed; otherwise use the existing renderer in the repository or an FFmpeg composition. Use local Whisper only when no transcript or reliable timing exists.

Read these references before execution:

- `references/workflow.md` for the seven roles and wave schedule.
- `references/contracts.md` for stage artifacts and handoff fields.
- `references/performance.md` for `fast`, `balanced`, and `quality` modes.
- `references/publishing.md` before creating the cover or social copy.

## Initialize the job

Create a new job directory outside the skill folder. Never write user media into the skill directory.

```bash
python scripts/jobctl.py init \
  --job-dir <job-dir> \
  --article <article-or-notes> \
  --audio <voiceover.mp3-or-wav> \
  --images <image-1> <image-2> \
  --mode fast \
  --speech-rate 1.0
```

Use `--speech-rate 1.2` only when the user explicitly requests 1.2x. If the user gives a target duration instead, run `scripts/prepare_voiceover.py --target-minutes <min>-<max>` and reject an automatically calculated rate outside `0.85-1.35`; ask the user whether the script or duration should change.

## Run seven workers

Use subagents when the host supports them. Give each worker only the artifact paths listed in `references/workflow.md`, never the full conversation. Run independent roles in parallel; otherwise run the same roles sequentially without changing their contracts.

1. Intake and rights worker
2. Timing and captions worker
3. Editorial distillation worker
4. Teaching storyboard worker
5. Visual preparation worker
6. Composition and finishing worker
7. QC and publishing worker

Every worker must write a compact JSON report with `status: pass|needs-human|fail`. A failure returns only to the worker that owns the defective artifact. Do not rerun completed upstream roles unless their input hash changed.

## Editing contract

- Prepare the speech rate once, before transcription and alignment. Preserve pitch with FFmpeg `atempo`; never speed the final mixed video as a shortcut.
- Keep the voice understandable. Default to `1.0x`; recommend `1.1-1.2x` for concise explainers and require explicit approval above `1.25x`.
- Map every visual to the sentence it explains. Do not distribute article images evenly or use a screenshot merely because it is available.
- Default to 1080x1920, 30 fps, H.264 High, yuv420p, and AAC 48 kHz for delivery.
- Keep captions and critical labels inside conservative mobile safe bounds. Remove source-account branding, unrelated headers, and engagement prompts when the user requests it.
- Use restrained modern transitions. A card flip, vertical card exchange, or depth slide may bridge major sections; use simple cuts inside procedural steps.
- Do not invent claims. Verify names, numbers, dates, and quoted statements against the frozen local source.
- Use only licensed source images, fonts, music, sound effects, and authorized voice recordings.

## Fast production loop

1. Prepare the narration and timing artifacts.
2. Build the storyboard and visual manifest before authoring the composition.
3. Render a low-cost proxy defined by the selected mode.
4. Inspect the first frame, every configured sample interval, every transition boundary, and the last frame. Run automated overflow, black-frame, decode, and loudness checks.
5. Repair only affected scenes or render chunks. Reuse unchanged chunks by cache key.
6. Render the full-resolution final once after the proxy gate passes.
7. Create `cover.png` and `publish-copy.json`, then run `scripts/validate_delivery.py`.

Never perform a second full render for a copy-only or outro-only change when a local scene/chunk replacement is possible.

## Delivery gate

Deliver only when all of the following exist and validation passes:

- `08-delivery/final.mp4`
- `08-delivery/cover.png`
- `08-delivery/publish-copy.json`
- `07-qc/qc-report.json`

The final response must report the absolute output paths, duration, speech rate, resolution, frame rate, loudness result, mode, and any rights items that still need human confirmation.

## Bundled scripts

- `scripts/jobctl.py`: initialize jobs, hash inputs, track stages, and validate handoffs.
- `scripts/prepare_voiceover.py`: apply pitch-preserving speed changes and write audio metadata.
- `scripts/render_cover.py`: render an exact-text 9:16 technology-style cover without model-generated text.
- `scripts/validate_delivery.py`: probe the final MP4, cover, publish copy, and QC report.
- `scripts/build_public_package.py`: create an allowlisted, privacy-scanned Skill archive for registry publishing.
