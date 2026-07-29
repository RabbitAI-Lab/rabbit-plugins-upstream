# Script Format

Standard formatting conventions for the full keynote script. Use this layout for every section.

---

## Header (top of every script document)

```
KEYNOTE: [event name]
DATE: [show date]
SPEAKER(S): [name(s)]
RUNTIME TARGET: [min]
VERSION: [V1 / V2 / Locked]
LAST EDIT: [date / editor]
STATUS: [Draft / Rehearsal / Locked]
```

## Per-segment format

```
═══════════════════════════════════════════════════════════════
SEGMENT 03 — CUSTOMER STORY: ACME CORP
SPEAKER: SATYA (CEO)        DURATION: 4:00        SLIDE RANGE: 12–18
═══════════════════════════════════════════════════════════════

[SLIDE 12 IN — Assertion: "Acme grew 3x in 18 months on our platform."]

SATYA:
Three years ago, Acme was running on legacy infrastructure.
They had eight engineers and one big problem.

[BEAT]

Today, that team has shipped 47 product launches.
Their CEO is here with us. Please welcome Lisa Park.

[CUE: WALK-ON MUSIC 02 — "Lisa Walk-On"]
[CUE: CAMERA 3 — wide stage]
[CUE: LIGHTING — Look 04, full stage]

[LISA ENTERS STAGE RIGHT]

[SLIDE 13 IN — "Acme + [Brand]: Built for what's next"]

LISA:
Thanks, Satya. Let me start with what's broken in our industry...

[VIDEO ROLLS — VID-003 "Acme highlight" — 1:15]
[LOWER THIRD: "Lisa Park, CEO, Acme Corp"]

[PAUSE — let video land]

LISA:
That clip was filmed last Tuesday...

═══════════════════════════════════════════════════════════════
```

## Formatting rules

### Speaker copy (the words spoken)
- **Plain text, mixed case.** Not all caps.
- **Short sentences.** ≤ 15–20 words each.
- **Contractions on.**
- **One idea per line.** Line break = beat break.
- **Pronunciation guides inline:** `Saoirse (SUR-sha)`.

### Stage directions
- **Square brackets, on their own line.** `[PAUSE]`, `[BEAT]`, `[GESTURE TO SCREEN]`.
- **Inline brackets allowed for short cues:** "Today we're announcing — [pause for applause] — the next generation..."

### Cue callouts
- **ALL CAPS, square brackets, separate line.** `[CUE: VIDEO 003 — "Customer story"]`
- **One cue per line.**
- **Be specific:** include filename, take number, duration if relevant.

### Slide markers
- **`[SLIDE 12 IN — assertion]`** when slide changes.
- **`[BUILD]`** for in-slide builds.
- **Include the assertion text** so the prompter operator can sync.

### Speaker labels
- **Speaker name in ALL CAPS, followed by colon.**
- **One blank line before / after speaker change.**

### Section breaks
- **Triple equals (`═══`)** or visible divider between segments.
- **Segment header** includes name, speaker, duration, slide range.

## What goes in the script vs. the ROS

| Goes in script | Goes in ROS |
|---|---|
| Speaker words | Minute-by-minute timing |
| Stage directions for speaker | Operator cues |
| Inline cue callouts | Full technical cue list |
| Pronunciation | Mic types, lighting looks, camera shots |
| Slide assertion text | Slide filenames, build counts |
| Pauses, beats, applause holds | Comms channel assignments |

The script tells the speaker what to do.
The ROS tells the crew what to do.
They reference each other but don't duplicate.

## Teleprompter-only version

For show day, generate a teleprompter-cleaned version that strips:
- Cue callouts (operator-only)
- Stage directions for crew
- Lower-third text

…and keeps only what the speaker reads, in large-format scrolling text. See `references/speaker-development.md` for formatting specifics.

## Version control

- File naming: `KEYNOTE_[EVENT]_[YYMMDD]_V[X]_[STATUS].docx`
- Single source of truth in one shared location (Google Doc, Notion).
- Comments-only access for stakeholders past V2.
- Producer owns the master; one merge per day max.
