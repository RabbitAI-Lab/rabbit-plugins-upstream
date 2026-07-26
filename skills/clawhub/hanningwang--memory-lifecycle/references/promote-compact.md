# Promote & Compact — Execution Checklists

Both operations follow the same pattern: filter → evidence → dedup → resolve conflicts. Promote moves entries up (daily → MEMORY.md); compact prunes MEMORY.md down.

---

## Promote (Daily → MEMORY.md)

> Triggered by: compaction flush step 4, periodic review, or "promote memory"

1. Backup MEMORY.md → `memory/.memory-backup.md`

2. Read daily files from last 7 days (`memory/YYYY-MM-DD.md`)

3. Read current MEMORY.md

4. For each daily entry, check against MEMORY.md — skip if same meaning already exists:

| Entry type | Action |
|-----------|--------|
| EXPLICIT preference or correction | Promote with `from:YYYY-MM-DD` |
| User correction ("not X, actually Y") | Promote + supersede old MEMORY.md entry |
| INFERRED, appears across 3+ different daily files | Promote with `from:{earliest date}` |
| INFERRED, 1-2 days only | Skip — not stable enough |
| Contradicts existing MEMORY.md entry | Promote newer, update/remove old |
| Detailed procedure / analysis | Create project workspace + pointer (not inline) |
| Project-related decision | Promote + append to `memory/projects/{name}/decisions.md` if workspace exists |
| Credential detected | Reject — replace with pointer, log warning |

5. Entry format: `- {content} | EXPLICIT or INFERRED | from:YYYY-MM-DD`

6. Conflict resolution: newer > older, EXPLICIT > INFERRED, user correction > all

7. Log each promote/skip decision with one-line reason to `memory/.lifecycle.log`

---

## Compact (MEMORY.md Pruning)

> Triggered by: MEMORY.md > 30K chars, or "compact memory"

1. Backup MEMORY.md → `memory/.memory-backup.md`

2. Read current MEMORY.md

### Decay

| Entry type | Action |
|-----------|--------|
| Non-`[perm]`, not relevant 60+ days | Delete |
| In Progress `[x]` older than 7 days | Delete |
| In Progress `[ ]` not updated 60 days | Delete |
| `[perm]` | Never touch |

Relevance heuristics:
- References a project no longer in `## Projects` → not relevant
- About a tool/library no longer in use → not relevant
- When in doubt, keep it

### Supersede

Contradictions on same topic → keep newer, delete older.

### Merge

Related entries saying similar things → combine without losing meaning. Keep the most recent `from:` date.

### Lint

- Each `## Projects` pointer → check target path exists
- Each `memory/projects/` dir → check MEMORY.md has pointer
- Report issues, do not auto-fix

### Finish

3. Write cleaned MEMORY.md

4. Append summary to `memory/.lifecycle.log`: what was decayed, superseded, merged, lint warnings
