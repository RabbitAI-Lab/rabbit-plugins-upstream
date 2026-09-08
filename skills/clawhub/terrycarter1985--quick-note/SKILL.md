---
name: quick-note
description: Create timestamped quick notes in a daily notes directory. Use when the user wants to jot down a short note, log a quick thought, or append to today's note file without opening an editor. Triggers on phrases like "quick note", "jot this down", "add a note", or "log this".
---

# Quick Note

Create timestamped markdown notes quickly.

## Usage

Run the script with the note text:

```bash
python3 scripts/make_note.py "Your note text here"
```

Options:
- `--dir <path>` — notes directory (default: `./notes`)
- `--tag <tag>` — add a tag prefix (can repeat)

## Output

Appends a line to `<dir>/YYYY-MM-DD.md` with format:

```
- HH:MM [tag] Your note text here
```

Creates the directory and file if they don't exist.

## Notes

- Notes are plain markdown bullet points
- One file per day makes review easy
- Tags help filter notes later
