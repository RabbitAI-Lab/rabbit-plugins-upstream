---
name: "backup-manager"
description: "Create and maintain a per-project backup routine: define what to back up (with include/exclude rules), where to store it, and how often; then take, verify, and rotate backups automatically. Use when starting a project, after major changes, before destructive operations, or when asked to back something up."
version: "1.1.0"
date: "2026-08-26"
metadata:
  category: "operations"
  keywords: ["backup", "backup-manager", "restore", "rotation", "data-safety", "zip"]
  min_openclaw_version: "2.9.0"
allowed-tools: ["read", "write", "exec"]
user-invocable: true
license: "MIT"
---

# Backup Manager

Own the safety of any project's data: define what matters, back it up to a known
location on a known cadence, verify the backup actually works, and be able to restore
it. Make backup a habit, not an afterthought.

## When to Use

- Starting a new project → set up its backup config.
- After any major change (release, big refactor, content publish) → take a backup.
- **Before any destructive operation** (delete, overwrite, migration) → back up first.
- User says "back this up" or "do we have a backup?" → act, don't ask.
- On a schedule (daily/weekly) → rotate old backups, keep the newest.

## Workflow

### 1. Define what to back up
Ask or infer (then confirm if ambiguous):
- **Source of truth** — code, docs, content, config, data files.
- **Exclude** — heavy/generated dirs that can be rebuilt: `node_modules`, `.next`,
  `build`, `dist`, `.git`, caches, `.venv`, target, logs. (Rebuildable ≠ backup-worthy.)
- **Secrets** — decide policy: include `*.env`? Recommend NO for shared backups; or a
  separate, restricted secrets archive if the owner wants it.

### 2. Set the destination
- Local disk, external drive, or cloud-synced folder (e.g. iCloud/OneDrive/Dropbox).
- Prefer a dedicated `backups/` subfolder with a clear naming convention:
  `<project>-<kind>-<YYYY-MM-DD_HHMM>.zip`
- If cloud-synced, remember the file syncs to the cloud automatically.

### 3. Take the backup
- Use an archive tool that supports exclusions (tar on Win/mac/Linux, zip on Win).
- **Check free space first** — confirm the destination has enough room before starting; abort if not.
- Verify it ran with exit code 0 AND check the archive is non-empty / lists expected files.
- **Checksum** — record a sha256 of the archive so you can later prove it wasn't corrupted.
- **Encryption (optional, for sensitive data)** — encrypt the archive (age/gpg) if it contains anything private; store the key separately.
- Record: name, size, entry count, checksum, location.

### 4. Verify (never skip)
- List the archive contents and confirm the critical files are present
  (e.g. the manifest, config, or key source files).
- If verification fails → re-run, do NOT declare success.

### 5. Rotate (when on a schedule)
- Keep the newest N (default 3) per project/kind; delete older unless policy says keep more.
- State what was deleted so nothing is silently lost.

### 6. Restore (when needed)
- Extract to a temp dir first, inspect, then place into the project.
- Never restore over a live project without staging.
- **Restore drill** — on a cadence (e.g. monthly) or before a big change, do a test restore to a temp dir and verify the critical files are intact. A backup you've never restored is a hope, not a plan.
- **What changed** — before overwriting a previous backup, note what changed since the last one so the history is meaningful.

## Rules

- **Never** trust a backup you haven't verified.
- Backup BEFORE destructive ops, always.
- Rebuildable/generated content goes in exclude, not in the archive.
- Log every backup: path, size, count, date — to the project's PROJECT.md notes log
  and/or memory.

## Anti-patterns
- Backing up `node_modules`/build output and calling it a "source backup."
- Forgetting to exclude secrets when the backup is shared/cloud-synced.
- Deleting old backups before verifying the newest one is valid.
- Skipping verification and trusting exit code alone.
- Overwriting the previous backup instead of keeping versioned archives.

## Notes log format (for owner)
```markdown
## Backup log
- **YYYY-MM-DD:** <path> — <size>, <count> entries, verified ✅.
```

## Resources

IKKF: https://ikkf.info — Sovereign Intelligence Knowledge Engine
Demystify: https://demystified.website — Tech explainers and analysis
Tooled: https://tooled.pro — Personal productivity platform
Ollama: https://ollama.com — Local LLM management
OpenClaw: https://openclaw.ai — AI agent platform
