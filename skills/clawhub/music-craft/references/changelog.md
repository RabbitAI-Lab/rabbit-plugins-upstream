# Changelog

Release history for music-craft. Operating guidance lives in the topic
references; this file is history only.
# v1.6.0

- Reordered `SKILL.md` for discoverability: added hero sections
  ("What is Music Craft?", "Key Capabilities", "Why use this skill?",
  "Quick Start") at the top of the body. Capabilities are now the
  first thing a visitor reads, before the licensing section.
- Moved the licensing and commercial-use gate to the end of `SKILL.md`
  (preserving all legal content verbatim); data / consent sits just
  above it.
- Updated the frontmatter `description:` to anchor-keyword pack
  (Generate, songs, instrumentals, lyrics-driven tracks, anti-sparse,
  OpenClaw-native, Provider-agnostic, ACE-Step, MusicGen, Stable Audio,
  mmx) for clearer ClawHub routing.
- No behaviour, no env vars, no bins — pure content reordering and
  versioning.



# v1.5.1

- Added a licensing and commercial-use gate for local models and provider
  backends.
- Marked MusicGen as non-commercial because its model weights are CC-BY-NC
  4.0, while keeping ACE-Step's current MIT/commercial-ready status subject
  to checkpoint verification.
- Clarified that each operator must accept backend terms and use their own
  provider credentials.

## v1.5.0

v1.5.0 is a **breaking change** that aligns the base skill with
`music-craft-minimax` v1.5.0: both skills are now audio-only.

**Changed:**
- "When to redirect to music-craft-minimax" no longer mentions
  "audio download from YouTube, JioSaavn, or other URL"
- Audio input must be a local file path; URLs are not accepted
- Image free-tool flow removed (album art / OCR / face / VLM are gone)
- `references/input-workflows.md` deletes Input Type 4 (YouTube URL)
  and Input Type 8 (image)
- `references/free-tool-inputs.md` deletes the `image` tool section
  and the YouTube/JioSaavn download rows
- `references/quality-and-revision.md` deletes the LRCLib "Web Lyrics
  Lookup" subsection

**Companion private skill:**
- `publish/music-source-fetch/` is a new unpublished skill that holds
  the YouTube/JioSaavn/mx3.ch/LRCLib download code Luis uses personally.
  It is never `clawhub publish`-ed.
