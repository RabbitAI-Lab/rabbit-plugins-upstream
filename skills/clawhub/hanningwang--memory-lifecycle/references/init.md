# Init — Execution Checklist

> Triggered by: first-time setup, or `memory/.lifecycle.log` does not exist.

1. Read current MEMORY.md (if exists)

2. Scan for credentials → replace with location pointers, count replacements

3. Restructure into sections (User / Projects / Team / Knowledge / Rules / In Progress)
   - Add `| EXPLICIT` or `| INFERRED` to each entry
   - Suggest `[perm]` candidates for user confirmation (do not add without asking)

4. Create directory: `memory/projects/`

5. Create `memory/.lifecycle.log` with initial entry: `[{YYYY-MM-DD}] init (v1)`

6. Write restructured MEMORY.md

7. Check `openclaw.json` for `memoryFlush` config — if missing, show user the block from [flush-prompt.md](flush-prompt.md) and ask before adding

8. Report: entries restructured, credentials replaced, [perm] candidates, flush prompt status
