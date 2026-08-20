---
name: music-practice-buddy
description: "Analyze instrumental practice recordings to detect timing accuracy, pitch stability, tempo consistency, and dynamic range. Generates practice reports with targeted exercise recommendations. Use when practicing an instrument and wanting objective feedback on performance."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [music, practice, audio-analysis, timing, pitch, instruments, musicians]
---

# Music Practice Buddy

## Overview

Music Practice Buddy listens to your practice recordings and tells you what you can't hear yourself: timing inconsistencies, pitch drift, tempo fluctuations, and dynamic imbalances. It provides objective, measurable feedback that accelerates the practice loop — record, analyze, adjust, improve.

Most musicians practice for years without knowing *exactly* what to fix. They sound "off" but can't pinpoint why. This tool turns vague feelings into specific, actionable data: "Your tempo drifted 8% faster in measures 17–24" or "Your pitch dropped 15 cents on high notes."

## When to Use

- You practice an instrument (guitar, piano, violin, voice, etc.) and want objective feedback
- You're preparing for a performance, audition, or exam
- You want to track improvement over time
- You're self-teaching and don't have a teacher's ear
- **Don't use for:** mastering/production analysis (this is practice feedback, not mixing tools)

## How It Works

1. **Audio Loading** — Reads WAV files (mono/stereo, any sample rate)
2. **Tempo Detection** — Estimates BPM using onset detection and autocorrelation
3. **Timing Analysis** — Detects note onsets, measures inter-onset intervals, flags inconsistencies
4. **Pitch Tracking** — Extracts fundamental frequency over time using autocorrelation
5. **Dynamic Analysis** — Measures RMS energy envelope, flags volume imbalances
6. **Report Generation** — Produces a scored report with strengths, weaknesses, and exercises

## Quick Start

```bash
# Analyze a practice recording
python scripts/practice_buddy.py analyze recording.wav

# Analyze with a target BPM for comparison
python scripts/practice_buddy.py analyze recording.wav --target-bpm 120

# Compare two recordings to track improvement
python scripts/practice_buddy.py compare week1.wav week2.wav

# Generate a practice plan based on analysis
python scripts/practice_buddy.py plan recording.wav --instrument guitar --minutes 30

# View practice history and improvement trends
python scripts/practice_buddy.py history
```

## Analysis Metrics

### Timing Score (0–100)

Measures how consistent your note timing is:
- **90–100**: Professional-level consistency
- **70–89**: Solid — minor inconsistencies
- **50–69**: Developing — noticeable rushing/dragging
- **Below 50**: Needs work — significant timing issues

### Pitch Stability Score (0–100)

Measures how steady your pitch is:
- Based on frequency variation around the mean
- Lower variation = higher score

### Tempo Consistency (0–100)

Measures how steady your overall tempo is:
- Compares detected BPM across different sections
- Flags acceleration or deceleration

### Dynamic Range (dB)

Measures the difference between loudest and quietest moments:
- **6–12 dB**: Good dynamic control for practice
- **>18 dB**: May indicate inconsistent technique
- **<3 dB**: May sound flat or mechanical

## Workflow: The Practice Loop

### Step 1: Record
Record yourself practicing a piece, scale, or exercise (WAV format).

### Step 2: Analyze
```bash
python scripts/practice_buddy.py analyze practice_session.wav
```

### Step 3: Review the report
The report highlights your weakest area with specific data.

### Step 4: Get a targeted plan
```bash
python scripts/practice_buddy.py plan practice_session.wav --instrument guitar --minutes 20
```

### Step 5: Practice the exercise, then re-record
```bash
python scripts/practice_buddy.py compare before.wav after.wav
```

## Report Output Example

```
╔══════════════════════════════════════════════╗
║       🎵 PRACTICE ANALYSIS REPORT            ║
╠══════════════════════════════════════════════╣
║  Duration: 2:34 | Sample Rate: 44100 Hz     ║
╠══════════════════════════════════════════════╣
║  📊 SCORES                                   ║
║  Timing:     72/100  ████░░░░░░  Developing  ║
║  Pitch:      85/100  ████████░░  Solid       ║
║  Tempo:      68/100  ████░░░░░░  Developing  ║
║  Dynamics:   78/100  ██████░░░░  Solid       ║
║  ────────────────────────────────────        ║
║  OVERALL:    76/100  Solid with gaps         ║
╠══════════════════════════════════════════════╣
║  📝 ANALYSIS                                 ║
║  • Detected BPM: ~118 (target: 120)         ║
║  • Tempo drifted +5% in the second half      ║
║  • 3 timing gaps > 50ms detected             ║
║  • Pitch stable with minor dips on high notes║
╠══════════════════════════════════════════════╣
║  🎯 RECOMMENDED FOCUS: Timing               ║
║  → Practice with a metronome at 60% speed   ║
║  → Focus on transitions between sections     ║
╚══════════════════════════════════════════════╝
```

## Common Pitfalls

1. **Recording in a noisy room.** Background noise corrupts onset detection and pitch tracking. Record in the quietest space available.
2. **Analyzing recordings with effects.** Reverb, distortion, and delay confuse the analyzer. Record dry (no effects) for practice analysis.
3. **Comparing scores across different pieces.** A complex piece naturally scores lower than a simple one. Compare apples to apples — same piece, different attempts.
4. **Obsessing over a single score.** One practice session is a data point, not a verdict. Track trends over weeks.
5. **Skipping the metronome.** If timing score is low, the metronome is your fastest path to improvement. Don't practice without it.

## Verification Checklist

- [ ] `practice_buddy.py analyze recording.wav` produces a report with 4 scores
- [ ] `practice_buddy.py analyze recording.wav --target-bpm 120` compares to target
- [ ] `practice_buddy.py compare before.wav after.wav` shows score differences
- [ ] `practice_buddy.py plan recording.wav --instrument piano --minutes 30` generates exercises
- [ ] `practice_buddy.py history` shows logged sessions

## References

- `references/audio-concepts.md` — how onset detection, pitch tracking, and tempo estimation work
- `references/practice-methodology.md` — evidence-based practice techniques for each weakness type
