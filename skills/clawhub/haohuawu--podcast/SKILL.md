---
name: podcast
description: >
  Use when the user wants to turn an article/blog/text into a published podcast episode:
  triggers like "生成播客""做一期播客""博客转播客""文章转播客""发布/更新播客""blog to
  podcast", or when they hand over a URL / text / a batch of source material to be turned
  into an audio show. ALSO use for maintaining published episodes: "只改 shownotes"
  "更新单集描述""换封面""修 RSS feed""小宇宙没更新" (update_metadata / --init paths).
  SKIP: plain read-this-text-aloud TTS requests - call TTS directly, this pipeline is overkill.
license: MIT-0
version: 1.0.0
metadata:
  openclaw:
    emoji: "🎙️"
    requires:
      bins: ["python3", "ffmpeg", "ffprobe"]
      env: ["DOUBAO_TTS_API_KEY", "TOS_ACCESS_KEY", "TOS_SECRET_KEY", "TOS_BUCKET", "TOS_REGION"]
    install:
      - kind: brew
        package: ffmpeg
        bins: ["ffmpeg", "ffprobe"]
        label: "ffmpeg (audio pipeline)"
---

# Article to Podcast: Generate & Publish

## The big picture

One episode = one **slug** (`YYYYMMDD_lowercase_english_title`, e.g. `20260715_my_episode`).
You generate it (translate Chinese titles into short English first). It is the episode's
stable primary key: local directory, TOS directory, RSS guid and all file keys derive from
it. **Immutable once published** — republishing under a new slug makes Xiaoyuzhou show a
duplicate episode; to fix content, rerun the same slug (guid unchanged, episode number kept).

```
Skill layout                          Data flow
podcast/
  SKILL.md                            source article
  scripts/        # see Scripts         │  (1-3) you write script.md + notes.md [+ images/]
  references/     # specs & recipes     ▼
    script-spec.md  notes-spec.md     $TMPDIR/podcasts/{slug}/       # artifacts + resume state
    images-guide.md                     script.md  notes.md  podcast.mp3
    source-fetching-guide.md            clips_cache/{md5}.wav  manifest.json
  assets/                               │  (5) generate_podcast.py   (PODCAST_WORKDIR overrides)
    config.schema.json                  ▼
    mic_tap.b64.txt  # narration entry cue (CC0 sample, decoded to WAV at runtime)
  tests/          # pytest suite
                                        │
                                        ▼
                                      TOS {bucket}/podcasts/         # single source of truth
                                        config.json  episodes.json  feed.xml
                                        cover_YYYYMMDD.png
                                        episodes/{slug}/podcast_{hash}.mp3, script.md,
                                                        notes.md, article.md, images/
```

Two state layers, two lifetimes:

- **TOS `podcasts/`** — the single source of truth, stateless across environments.
  `episodes.json` is pulled → updated → pushed on every publish; **never hand-edit it, never
  rebuild the feed with inline Python** — `update_metadata.py` is the tool for that.
  Write order is codified in `podcast_store.publish_state`: episodes.json before feed.xml.
  Every push is a full rewrite, so `publish_state` guards it: episodes other than the
  target slug must be byte-identical to the live state, and the rendered feed is
  re-parsed and checked item-by-item against episodes.json before anything touches TOS
  (the old episodes.json is backed up to `podcasts/backups/` first). A blocked push
  prints the affected slugs; intentional bulk migrations pass `--force-state`.
- **`$TMPDIR/podcasts/{slug}/`** (Python `tempfile.gettempdir()` — `/tmp/podcasts` on
  Linux, per-user `T/podcasts` on macOS; `PODCAST_WORKDIR` overrides it —
  host-agnostic) — build artifacts AND resume
  state in one directory.
  The publish script uploads `script.md`/`notes.md`/`article.md`/`images/` from the
  directory containing the `--script` file — **keep them next to script.md** or they are
  silently not archived.
  Every synthesized chunk is cached as
  `md5(voice|rate|context|text).wav` the moment it succeeds; `manifest.json` records
  script/audio md5. A rerun after ANY mid-pipeline failure (bad segment, network, upload)
  re-bills only failed/changed chunks; unchanged script + intact mp3 skips TTS entirely
  (`--no-upload` preview → publish rerun costs zero). `--force` overrides everything.

## Workflow

```
0. First-time init (once per channel)     [you + user + script]
   Collect real values per assets/config.schema.json — confirm EVERY value with the
   user, never invent — write a JSON instance. The channel cover is private
   material, NOT shipped with the skill: pass your own 1400-3000px square PNG:
   python3 scripts/generate_podcast.py --init --config /tmp/channel-config.json --cover /path/to/cover.png

1. Fetch source                            [you]
   web_fetch the URL / use provided text. JS-rendered pages & X articles: see
   references/source-fetching-guide.md.

2. Write script.md                         [you]  (spec: references/script-spec.md)
   - [ ] Two-host deep-dive, NOT an interview (EP1: interview-style draft was fully rewritten)
   - [ ] Audit section-by-section against the source: every concept/case/number lands
         somewhere; never "simplify" on the user's behalf — the dry-run char count is a
         price quote, not a trimming target (real lesson: a survey post lost half its content)
   - [ ] Multiple sources: write article.md integrating them, get user review, THEN
         write the script from it (EP6)
   - [ ] Externally generated scripts: strip non-dialogue content first (EP12; the
         validator also rejects URLs in dialogue)

3. Write notes.md (REQUIRED) + images      [you]  (spec: references/notes-spec.md)
   - [ ] Check the source article for images (JS-rendered pages hide <img> from curl —
         use the browser flow, see references/images-guide.md); download into images/ NEXT TO
         script.md — the publish script only uploads from there
   - [ ] Image URLs in notes.md must match TOS filenames exactly:
         episodes/{slug}/images/{filename} (EP14: local numbering prefixes → five 404s)
   - [ ] Timeline draft: python3 scripts/generate_timeline.py --script script.md --estimate

4. Confirm with the user (billing gate)    [user]
   python3 scripts/generate_podcast.py --script script.md --slug {slug} --dry-run
   Show the outline + net billable chars (cache-aware). TTS bills per character;
   rework is cheapest at this gate. Format check runs automatically at step 5; for
   early feedback: scripts/validate_podcast.py --script script.md --notes notes.md

5. Synthesize + publish (one command)      [script]
   python3 scripts/generate_podcast.py --script script.md --slug {slug} --notes notes.md
   Preflight validates everything (env, TOS, config, script/notes format) BEFORE the
   first paid TTS call. Auto-uploads podcast_{hash}.mp3, script.md, notes.md,
   article.md (if any), images/ to episodes/{slug}/.

6. Post-publish: calibrate the timeline    [you + script]
   python3 scripts/generate_timeline.py --script script.md --mp3 podcast.mp3 --calibrate
   Paste real timestamps into notes.md, then:
   python3 scripts/update_metadata.py --slug {slug} --notes notes.md
```

## Usage

```bash
# 0) First time only (--cover: your channel's square PNG, private, not shipped)
python3 scripts/generate_podcast.py --init --config /tmp/channel-config.json --cover /path/to/cover.png

# 1) Estimate billable characters (free; cache-aware net billing)
python3 scripts/generate_podcast.py --script script.md --slug 20260715_my_episode --dry-run

# 2) Synthesize and publish (--notes REQUIRED unless you pass --no-notes explicitly)
python3 scripts/generate_podcast.py --script script.md --slug 20260715_my_episode --notes notes.md

# 3) Synthesize without publishing (preview); rerun same slug to publish (no re-billing)
python3 scripts/generate_podcast.py --script script.md --slug 20260715_my_episode --no-upload

# 4) Metadata-only update (notes/description) — never re-runs TTS
python3 scripts/update_metadata.py --slug 20260715_my_episode --notes notes.md
```

All flags: `--host-voice` / `--guest-voice` (voice ids, else `DOUBAO_TTS_*_VOICE` env, else
defaults), `--no-postprocess` (skip the audio filter chain), `--force` (ignore caches, full
resynthesis), `--skip-validate` (bypass format check — only for confirmed false positives),
`--no-notes` (explicitly publish without shownotes).

### Recovery

- **A segment failed / network died / upload broke** → fix the cause, rerun the SAME
  command. Preflight re-checks, cached chunks replay for free, only failed/changed chunks
  are re-billed; if the script is unchanged and mp3 intact, TTS is skipped entirely.
  The failing text is printed in the log; common causes: very long unpunctuated strings,
  flagged words.
- **Preflight refused to run** → it lists ALL problems at once (env vars, missing --init,
  bad format, missing notes); fix and rerun. Nothing has been billed at that point.
- **Want a clean slate** → `--force`, or delete `$TMPDIR/podcasts/{slug}/` (`PODCAST_WORKDIR`
  overrides the base path).
- **Published episode needs a content fix** → rerun the same slug with the fixed script
  (audio re-synthesized only for changed chunks, feed guid stays, no duplicate episode).
  Only notes/description changed → `update_metadata.py`, zero TTS.

## Scripts

**Always use these scripts instead of writing inline Python** — they handle config,
cover_url, episodes.json state and feed regeneration correctly.

CLI entry points:

| Script | Purpose |
|--------|---------|
| `generate_podcast.py` | Full pipeline: preflight → parse → TTS (cached, resumable) → post-process → upload → episodes.json + feed. Modes: `--init`, `--dry-run`, `--no-upload`, `--force`. |
| `update_metadata.py` | Notes/description update without TTS: upload notes.md → episodes.json description → rebuild feed. Also the correct tool for any manual feed rebuild. |
| `generate_timeline.py` | Timeline: `--estimate` from char counts (260 chars/min), `--calibrate` against the real MP3 via ffprobe. |
| `validate_podcast.py` | script.md / notes.md format compliance. Runs automatically inside publish preflight; standalone run for early feedback. |

Library modules (import-only, no CLI): `script_md.py` (the ONLY script.md parser — parsing
semantics live here), `script_synthesis.py` (Doubao TTS client + ffmpeg pipeline; audio
post-processing chain documented in its header), `podcast_store.py` (TOS state layer, key
constants, write-order invariant), `rss_feed.py` (RSS 2.0, stdlib-only), `tos_uploader.py`
(TOS client). Tests: `tests/` (pytest; run with
`uv run --with pytest --with requests --with markdown python -m pytest tests -q`).

## Configuration

Channel config fields: `assets/config.schema.json` (authoritative; `--init` validates and
exits with itemized errors). `cover_url` is an OUTPUT of `--init` (it uploads the PNG
passed via `--cover` as dated `cover_YYYYMMDD.png`), not something to collect. To change
channel info or cover, rerun `--init`.

| Env var | Required for | Notes |
|------|---------|------|
| `DOUBAO_TTS_API_KEY` | synthesis | [Doubao speech console](https://console.volcengine.com/speech) |
| `TOS_ACCESS_KEY` / `TOS_SECRET_KEY` | init/publish | Volcano Engine AK/SK |
| `TOS_BUCKET` / `TOS_REGION` | init/publish | e.g. cn-shanghai |
| `DOUBAO_TTS_HOST_VOICE` / `DOUBAO_TTS_GUEST_VOICE` | optional | defaults: liufei (male) / tianmeiyueyue (female) |
| `PODCAST_WORKDIR` | optional | local base dir for build artifacts + resume state (one directory per episode), default `$TMPDIR/podcasts` (Python `tempfile.gettempdir()` — `/tmp/podcasts` on Linux, per-user `T/podcasts` on macOS) |

Dependencies: system `ffmpeg`/`ffprobe`; Python `requests` + `tos` + `markdown`. If the
environment lacks them, run `uv run scripts/generate_podcast.py ...` (PEP 723 inline metadata).

## Format specs

- script.md: [`references/script-spec.md`](references/script-spec.md) — segments
  `## 第 N 段 · 子标题`, roles `**主持人**`/`**嘉宾**`/`**旁白**`, title
  `{English} -- {中文副标题}`, the closing H2 line IS synthesized into audio.
- notes.md: [`references/notes-spec.md`](references/notes-spec.md) — opening hook line,
  内容速览 / 时间轴 / 原文链接 sections.

Both are enforced by `validate_podcast.py` (inline in publish preflight).

## Gotchas

Rules the scripts CANNOT enforce — apply them at the step where they occur (checklists
above); this list is the rationale archive.

Content:
- Two-host deep-dive, not an interview; open with "欢迎收听本期节目" (EP1: an
  interview-style script shipped mismatched against the published mp3)
- Content fidelity first: audit section-by-section against the source; length follows
  content (lesson: a survey post once lost nearly half its content to "simplification")
- Multi-source episodes: article.md summary → user review → script (EP6: writing straight
  from 4 articles gave uneven coverage)
- Keep Chinese punctuation in Chinese scripts — the TTS models prosody on it; converting
  to ASCII punctuation degrades intonation

Publishing:
- **Cover updates MUST use a new filename**: platforms cache the cover URL; overwriting
  the same key does nothing. `--init` handles this with `cover_YYYYMMDD.png`
  (2026-07-15 lesson: overwrote cover.png, platforms never refreshed)
- Metadata-only change → `update_metadata.py`, not a publish rerun (a rerun no longer
  re-bills TTS thanks to the manifest, but update_metadata is faster and more direct)
- Archive uploads come from the `--script` file's parent directory: keep notes.md /
  article.md / images/ next to script.md
- The slug is immutable once published; fix content by rerunning the same slug

TTS & audio:
- Any segment that still fails after retries aborts the whole run (never publish with
  silent holes). Fix the script and rerun the same command — cached chunks are free,
  only the failed chunk is re-billed
- A lost script.md cannot be recovered from audio (no ASR access); make sure script.md
  is on disk before synthesis, and never `rm -rf` its path

## Xiaoyuzhou integration

1. First time: submit the feed URL (printed by `--init` and every publish) in the
   Xiaoyuzhou podcaster console; claim verification code goes to the config email
2. After that: every publish updates the feed and Xiaoyuzhou picks up new episodes
   automatically
