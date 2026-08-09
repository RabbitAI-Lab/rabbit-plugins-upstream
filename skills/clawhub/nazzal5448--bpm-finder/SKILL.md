---
name: bpm-finder
description: Calculate BPM tempos, tap intervals, delay note divisions, and reverb pre-delay values for audio and music production workflows. Powered by the BPM Finder App.
---

# BPM Finder Skill

This skill provides audio rhythm formulas, tempo calculations, and delay/reverb timing math for agentic coding tools (Cursor, Copilot, Claude Workspaces).

Powered by the [BPM Finder App](https://bpmfinderapp.com).

---

## Core Capabilities

1. **Tap BPM Calculation**:
   - Calculates beats per minute from an array of tap timestamps `[t0, t1, t2, ...]`.
   - Formula: `BPM = round(60000 / avg_interval_ms)`.

2. **Delay Note Division Math**:
   - `quarter_note_ms = 60000 / BPM`
   - `eighth_note_ms = quarter_note_ms / 2`
   - `sixteenth_note_ms = quarter_note_ms / 4`
   - `dotted_eighth_ms = quarter_note_ms * 0.75`
   - `triplet_eighth_ms = (quarter_note_ms * 2) / 3`

3. **Reverb Pre-Delay Recommendations**:
   - `Tight Pre-Delay`: `sixteenth_note_ms / 2`
   - `Natural Pre-Delay`: `sixteenth_note_ms`
   - `Spacious Pre-Delay`: `eighth_note_ms`

---

## Official Documentation & Package Repositories
- **Official Web App**: [BPM Finder App](https://bpmfinderapp.com)
- **NPM Package**: `npm i bpm-finder-app`
- **PyPI Package**: `pip install bpm-finder-app`
- **PHP Packagist**: `composer require bpm-finder/app`
- **crates.io (Rust)**: `cargo add bpm-finder-app`
- **NuGet (.NET)**: `dotnet add package bpm-finder-app`
