# Run-of-Show (ROS)

The minute-by-minute operating document. The show caller runs the show from this. Every cue lives here.

---

**Event:** ________________ **Date:** ________________ **Doors:** ________________ **Show start:** ________________ **Show end:** ________________

## Header info
- **Producer:**
- **Show caller:**
- **Technical director:**
- **Stage manager:**
- **Show callers on comms channel:**

## ROS schema

| # | Timecode | Duration | Segment | Speaker | Script ref | Deck / file | Slide range | Video file | Demo state | Mic | Lighting look | Camera | Confidence monitor | Lower third | Music cue | B-roll fallback | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | -00:30:00 | 30:00 | Doors open / pre-roll | — | — | PRE_ROLL.mp4 | — | PRE_ROLL.mp4 (loop) | — | — | House lights up | — | Countdown | — | Bed track 01 (loop) | — | Producer | Locked |
| 02 | -00:05:00 | 5:00 | Voice of god / final seating | VOG | VOG_script.docx | — | — | — | — | VOG mic | House to 30% | — | Countdown 5:00 | — | Bed → silence | — | Stage mgr | Locked |
| 03 | 00:00:00 | 1:30 | Show open video | — | — | — | — | OPEN_001_v3.mov | — | — | Lights to 0 / video look | Camera 1 wide | Slide 1 preview | — | Score embedded | — | Video op | Locked |
| 04 | 00:01:30 | 0:30 | Walk-on CEO | CEO (Satya) | KEYNOTE_v8.docx p.2 | Master deck | 1 | — | — | Lav A (mic check) | Look 02 — warm wash | Cam 1 wide → Cam 3 close | Slide 1 (assertion) | "Satya Nadella, CEO, [Company]" | Walk-on sting 01 | If late: extend bed | Show caller | Locked |
| 05 | 00:02:00 | 4:00 | Opening message | Satya | KEYNOTE_v8.docx pp.3–6 | Master deck | 2–7 | — | — | Lav A | Look 03 | Cam 3 | Current slide | — | — | — | Producer | Locked |
| 06 | 00:06:00 | 4:00 | Customer story | Satya + Lisa | KEYNOTE_v8.docx pp.7–11 | Master deck | 8–14 | VID_003.mov (1:15 in) | — | Lav A + Lav B | Look 04 | Cam 1 → Cam 3 | Current slide | "Lisa Park, CEO, Acme Corp" | Walk-on sting 02 | If video fails: extend Q&A | Producer | In review |
| 07 | 00:10:00 | 6:00 | Product demo | Satya | KEYNOTE_v8.docx pp.12–14 | Demo machine 1 | — | DEMO_BACKUP_v2.mov (on failure) | Reset state confirmed -10 min | Lav A | Look 03 | Cam 3 + Demo capture | Demo state | — | Bed under | DEMO_BACKUP_v2.mov | Demo op + Producer | Pending |
| ... |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Column definitions
- **#** — segment number, locked once approved.
- **Timecode** — running time from show start (negative for pre-roll).
- **Duration** — planned length.
- **Segment** — short label.
- **Speaker** — who's on stage / on mic.
- **Script ref** — exact script document + page.
- **Deck / file** — playback source.
- **Slide range** — which slides are live.
- **Video file** — filename with version.
- **Demo state** — what state is the demo in?
- **Mic** — which mic, primary + backup.
- **Lighting look** — preset name.
- **Camera** — primary shot, cut points.
- **Confidence monitor** — what the speaker sees downstage.
- **Lower third** — exact text.
- **Music cue** — music in/out.
- **B-roll fallback** — what runs if this beat collapses.
- **Owner** — single accountable name.
- **Status** — Draft / In review / Approved / Locked.

## ROS quality bar
- ☐ Every cell is filled or marked N/A
- ☐ Every cue has an owner
- ☐ Total duration matches show length
- ☐ Every transition is named
- ☐ Every demo and video has a B-roll fallback
- ☐ Mic assignments include backup
- ☐ All filenames are final (no placeholders)
- ☐ All speakers approved their segments
- ☐ Tech rehearsal sign-off complete
- ☐ Show caller has marked up their personal copy

## Lock discipline
- ROS lock at T-minus 5 days.
- Any change after lock requires producer approval AND a re-circulated change log.
- Printed copies in producer pouch, show caller booth, stage manager wing, podium.

## Contingency rows (sprinkled in or separate sheet)
- **Delay package** — what plays if the show start slips 2–10 minutes.
- **Speaker freeze** — bridge content, host vamp.
- **Demo failure** — backup recording.
- **Technical outage** — house host vamps / B-roll loop / camera-only speech.
- **Breaking news** — modified open / acknowledged context.
