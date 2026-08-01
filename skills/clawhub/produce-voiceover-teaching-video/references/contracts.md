# Artifact contracts

## Job layout

```text
video-job/
  job.json
  00-source/source-manifest.json
  01-intake/input-report.json
  02-timing/audio-report.json, timing.json, segments.json, subtitles.srt
  03-editorial/editorial-brief.json
  04-storyboard/storyboard.json
  05-visuals/visual-manifest.json, assets/
  06-edit/composition-report.json, proxy.mp4, chunks/
  07-qc/qc-report.json
  08-delivery/final.mp4, cover.png, publish-copy.json
```

## Common report envelope

Every stage JSON uses:

```json
{
  "schema_version": 1,
  "stage": "01-intake",
  "worker": "intake-and-rights",
  "status": "pass",
  "input_hash": "sha256",
  "outputs": {},
  "issues": []
}
```

Use `needs-human` for editorial taste or missing rights confirmation. Use `fail` for unreadable input, unsupported format, factual mismatch, synchronization errors, render failures, or invalid delivery media.

## Editorial brief minimum fields

`audience`, `promise`, `problem`, `teaching_steps`, `examples`, `caveats`, `verified_facts`, `prohibited_copy`, `cta`, and `rights_notes`.

## Timing segment minimum fields

`segment_id`, `start`, `end`, `text`, `confidence`, and optional `words`. Times are seconds from the prepared narration start.

## Storyboard beat minimum fields

`beat_id`, `start`, `end`, `timing_segment_ids`, `teaching_goal`, `visual_id`, `visual_kind`, `source_id`, `on_screen_text`, `safe_bounds`, and `transition`.

## Visual manifest minimum fields

`visual_id`, `path`, `kind`, `width`, `height`, `source_id`, `license`, `used_by_beats`, and `sha256`.

## Publish copy minimum fields

`title`, `description`, `hashtags`, `pinned_comment`, `reply_prompt`, `cover_title`, and `cover_subtitle`. Do not place hashtags inside `description`.
