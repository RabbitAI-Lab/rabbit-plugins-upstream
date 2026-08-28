---
name: narrated-handdrawn-story-video
description: "Create polished Chinese story short videos from story text or ordered illustrations: story-specific multi-scene colored hand-drawn visuals, a text-led opening poster, sentence-synchronous local Qwen3-TTS narration with optional character voices, subtitles, and licensed BGM mixed beneath narration. Use for idiom stories, children's stories, history explainers, or any Chinese narrated hand-drawn short-video request where visual variety and audio-text synchronization matter."
---

# Narrated Hand-drawn Story Video

Use the installed `story-to-handdrawn-video` renderer for the picture track, then produce narration and the final mix. This is a quality-first workflow: never substitute one illustration across all story beats.

## Required outcome

- Create an opening poster (normally 3 seconds) with a legible Chinese title, category/tag, concise synopsis, and one takeaway; reserve uncluttered image space for this text. Render the complete image-and-text cover at frame 0; never fade its text in after the video begins.
- Turn the story into 8–18 narrative beats. For every beat, define setting, action, characters, emotion, and an exact subtitle/narration sentence before generating artwork.
- Generate or source a distinct scene illustration for every beat. Build multi-panel source art only as a generation convenience, then crop it into one image per beat.
- Keep character identity, era, palette, and framing consistent with the project's actual output ratio. Read `project.width` and `project.height` from the storyboard before prompting for art; the current renderer defaults to 1080×1440 (3:4), not 9:16. Use `contain` only after the source image has been normalized to the same ratio.
- Generate one local Qwen3-TTS segment per subtitle from that exact string. Use distinct voice-design instructions for narrator and named speaking characters. Derive the scene duration from the resulting audio; do not write narration separately from captions.
- Obtain BGM from a source whose license permits the intended use. Preserve the source URL, author, and license in an attribution text file next to the deliverable.
- Mix BGM softly and duck it under speech. Delay narration by the poster duration. Export a playable H.264/AAC MP4.

## Workflow

1. Write `story.txt` and a two-digit-keyed `visual-plan.json`. Split only at natural narrative turns; resolve pronouns and time jumps in the plan. Keep `caption` and `narration` identical for each scene.
2. Use the existing renderer wrapper to plan/generate/import the scene images. Set `STORY_VIDEO_PROJECT` to the cloned Remotion project when needed:

   ```bash
   STORY_VIDEO_PROJECT=/absolute/project \
   python3 /Users/bingo/.codex/skills/story-to-handdrawn-video/scripts/run_story_video.py \
     --input /absolute/story.txt --title "故事标题" --visual-plan /absolute/visual-plan.json --mode generate
   ```

3. Generate images with the image-generation tool. Prompt for exact story action and setting; request no embedded text. Inspect the first crop from each batch before importing all scenes.
4. Produce the opening-poster image with the image-generation tool at exactly the storyboard's aspect ratio, then add `project.opening_poster` (asset, tag, title, synopsis, takeaway) to the storyboard. The renderer displays the complete cover at frame 0; do not fade in its text. Allocate the copy to a quiet third of the frame. If the generated file has another ratio, outpaint or extend it to the project ratio without stretching or cropping subjects, then resize to the exact project dimensions. Verify the image and video dimensions with `scripts/check_cover_ratio.py` and `npm run check` before rendering.
5. Generate each TTS segment with `scripts/synthesize_qwen3.py` using the local Qwen3-TTS model and a voice-plan JSON. Use one segment for exactly one subtitle; concatenate them in scene order, keeping a short leading and trailing pause in every segment. Update scene timing from measured audio duration and render the silent picture track. Do not fall back to online Edge TTS unless the user explicitly requests it.
6. Download/select an appropriate licensed BGM, trim/fade it, then run `scripts/mix_story_audio.py` to delay the voice for the poster and sidechain-duck the music.
7. Inspect a poster frame and several scene-boundary frames. Confirm each subtitle matches both the voice and shown action, then place only the final MP4 and BGM attribution in the requested output folder.

## Audio mix

```bash
python3 scripts/mix_story_audio.py \
  --video /absolute/picture_silent.mp4 \
  --voice /absolute/narration.wav \
  --bgm /absolute/music.ogg \
  --output /absolute/final.mp4 \
  --poster-seconds 3
```

The script preserves the video stream and creates AAC audio. It deliberately makes no license claim; create an attribution file yourself.

## Non-negotiable checks

- Do not reuse a generic scene across story beats.
- Do not render a poster whose aspect ratio differs from the video canvas; `contain` would create side or top bars, while `cover` can remove important artwork.
- Do not let captions, narration, and scene meaning diverge.
- Do not use music without checking its current license and retaining attribution when required.
- Do not report a silent picture track as a completed narrated video.
- Do not expose intermediate files as final deliverables.
- Do not use a generated image's embedded text as poster copy; the renderer owns text layout.
