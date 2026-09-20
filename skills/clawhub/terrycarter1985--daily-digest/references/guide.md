# Daily Digest Reference

## File Patterns

Daily log files follow: `memory/YYYY-MM-DD.md`
- Example: `memory/2026-09-16.md`

## Key Sections to Extract

| Section | Source | Priority |
|---------|--------|----------|
| Key Events | Daily log | High |
| Decisions | Daily log | High |
| Files Touched | Daily log (grep for file paths) | Medium |
| Pending Items | Daily log + MEMORY.md | High |
| Memory Updates | MEMORY.md diff (if git available) | Low |

## Edge Cases

- No daily file → skip events, still report MEMORY.md changes
- Multiple daily files → merge chronologically
- MEMORY.md unchanged → omit Memory Updates section

## Integration Points

- Pairs well with `cron` for automated end-of-day generation
- Output can be sent via `message` tool to any channel
- Can be chained with `tts` for voice briefings
