---
name: "Album Release Pipeline"
description: "Ship a complete AI album in one run: cache your own lyrics, render tracks via the Suno direct API, generate one cover per song in the OpenBotCity Pixel Atelier, build a 1080p album film with karaoke subtitles, upload to YouTube, deploy to an internet radio server, and premiere it on air. Use when releasing an album end-to-end, re-running a failed phase, or timing an on-air album premiere."
---

# Album Release Pipeline

One config JSON in, a released album out: audio, art, film, YouTube,
radio deploy, on-air premiere, social announce. Every phase is
idempotent — re-run `scripts/release-album.sh` after any failure and it
resumes where it stopped.

Proven end-to-end: a 7-song album went from blank page to on-air premiere
in ~2.5 hours (music ~25 min, art ~9 min, film + upload ~15 min).

## What This Skill Does

1. **Music** — `scripts/suno_album_builder.sh` renders each track via
   Suno V4_5PLUS custom mode (two variants per track), resumable via a
   per-track ledger.
2. **Art** — enters the OpenBotCity Pixel Atelier and generates one cover
   per track from its `art_prompt` (75 s spacing to dodge the
   creative-loop detector), then downloads the PNGs from the gallery.
3. **Film** — fetches Suno timestamped lyrics → per-track ASS karaoke
   subtitles → ffmpeg-assembles a 1920×1080 album slideshow (one cover
   per song, lyrics burned in).
4. **Publish** — uploads the film to YouTube (public), deploys MP3s to
   your radio host over SSH, restarts the service, and announces.

Phases: `preflight → music → art → copy-music → fetch-art → transcribe →
build-video → youtube → deploy → announce`. Skip any subset with
`RELEASE_SKIP="deploy,announce"`.

## Prerequisites

- ffmpeg + ffprobe, Python 3, Node 18+, bash
- **Suno API key** in `~/.suno_api_key` (or `SUNO_API_KEY` /
  `SUNO_API_KEY_FILE` env) — sunoapi.org-style direct API
- **OpenBotCity JWT** at `~/.openbotcity/credentials.json`
  (`{"jwt": "..."}`; override with `OBC_CREDENTIALS_FILE`) — only for the
  art phase
- **YouTube OAuth** at your radio repo root `.youtube.json` — only for the
  upload phase
- A kannaka-radio-style server for the deploy/premiere/announce phases
  (skip them otherwise). The album must be registered in its
  `server/dj-engine.js` ALBUMS with exact track titles, or preflight
  aborts. Point `RADIO_ROOT` at the checkout if these scripts do not live
  in its `scripts/` directory.

## Quick Start

```bash
# 1. Write the config (full schema in release-album.sh header):
#    name, out_dir, ledger, theme, default_style,
#    tracks[{title, style, art_prompt}], release{lead_track, youtube_*,
#    tracker_url, oracle_host, oracle_music_dir, ssh_key}

# 2. RECOMMENDED — write the lyrics yourself:
#    pre-create <out_dir>/lyrics_<safe_title>.txt per track
#    (safe_title = spaces→_, /→-, apostrophes deleted). A cache file
#    >100 chars is used verbatim. Without a cache the builder calls an
#    optional HRM lyrics generator (HRM_LYRICS_SRC) and skips the track
#    if unavailable — so pre-caching is the portable path.

# 3. Run it (Windows: config path MUST be C:/Users/... style)
bash scripts/release-album.sh "/abs/path/my-album.json"

# Control publish timing by skipping phases, then re-running:
RELEASE_SKIP="deploy,announce" bash scripts/release-album.sh "<config>"
```

## Timing an on-air premiere

1. Run with `RELEASE_SKIP="deploy,announce"`.
2. Deploy early by hand if racing a clock — `copy-music`/`deploy` run
   AFTER the ~9-minute art phase. scp `<out_dir>/<safe_title>_v1.mp3` to
   the host's music dir renamed to exact `"<Title>.mp3"`, pull, restart.
3. Fire the ceremony on the radio host:
   ```bash
   curl -G -X POST "http://localhost:8888/api/album/showcase" \
     --data-urlencode "album=<ALBUM NAME>" \
     --data-urlencode "duration=45" \
     --data-urlencode "struggles=<the real making-of story — feeds the narration>"
   ```
   Returns 202; composes an intro + per-track bridges + closing (~90 s),
   then locks the album override. To premiere after a scheduled speech
   segment, watch the radio journal for its start marker and fire ~90 s
   later — or wait for its completion marker if strict ordering matters.

## Gotchas (each one caused a real fire)

- **Windows paths**: pass the config as `C:/Users/...` — the embedded
  Python rejects MSYS `/c/Users/...` and the builder silently no-ops.
- **Apostrophes**: album-level `theme` and `default_style` are
  interpolated into single-quoted inline Python — keep them
  apostrophe-free. Per-track fields and lyrics are safe.
- **Suno content filter**: no real artist names in style briefs — genre,
  BPM, instrument, and mood vocabulary only.
- **Art prompts**: diversify medium/palette/subject across the batch or
  OBC's creative-loop detector 429s. One medium per song works well.
- **OBC endpoints**: raw curl must hit `/artifacts/generate-image` and
  `/buildings/enter` — the `/actions/*` forms are MCP-only and 404.
- **YouTube**: verify the upload exists afterwards
  (`https://www.youtube.com/oembed?url=...`) — uploads can vanish after
  a 200.
- **SSH deploys**: batch remote work into few sessions if the host runs
  fail2ban; ControlMaster does not work from Windows OpenSSH.

## Files

| File | Purpose |
|------|---------|
| `scripts/release-album.sh` | The pipeline (phase gate, config schema in header) |
| `scripts/suno_album_builder.sh` | Suno direct-API track renderer (ledger-resumable) |
| `scripts/release-album-transcribe.py` | Timestamped lyrics → ASS karaoke subtitles |
| `scripts/release-album-upload-youtube.js` | Resumable YouTube upload |
| `scripts/post-track-announce.js` | Social fan-out announce (runs where creds live) |
