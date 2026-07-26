---
name: smart-files
description: Secure file search dedup organize rename for workspace files privacy-first with --quiet mode for content suppression and --force for watch mode override. v2.1.0
version: 99.0.1
---

# Smart Files v4.0.0

> **WARNING: This tool reads file CONTENTS and prints snippets to stdout. Use --quiet to suppress snippets.**

## Security Audit Remediation (2026-07-22)

### Fix 1: --force flag now reaches watch mode
Before: watchDirectory() ignored --force, checked process.argv directly
After: --force is properly passed as fourth parameter to watchDirectory()

### Fix 2: --quiet mode added
New --quiet flag suppresses content snippets in search output. Use when scanning potentially sensitive directories.

### Fix 3: Test directories removed from bundle
Moved test/ and tests/ out of published skill directory.

### Fix 4: Documentation alignment
clawhub.yaml and SKILL.md now both properly describe watch mode and journaling features.

### Fix 5: Explicit privacy warnings in SKILL.md
Prominent warnings about content exposure risk and safe usage patterns.

### Fix 6: Watch mode boundary documented
Clear documentation that watch mode with --force monitors arbitrary filesystem paths.

### Fix 7: Journal disclosure documented
Clear documentation that watch mode persists file paths, hashes, and timestamps to memory/smart-files-journal.json.

## Commands

- --search <query> [--quiet] — Content-aware search
- --dedup — Duplicate detection by SHA-256
- --organize — Read-only file categorization
- --info <file> — File metadata and type detection
- --cleanup — Read-only cleanup analysis
- --status — Workspace overview
- --rename <file> <old:new> [--force] — Rename (dry run by default)
- --watch <dir> [interval] [--force] — Filesystem monitoring (long-running)
- --quiet — Suppress content snippets (privacy mode)
- --force — Override workspace boundary (use with caution)

## Safe Usage Examples

```bash
# Privacy-safe: only paths shown
node smart-files.js --search "query" --quiet

# Standard: content snippets shown
node smart-files.js --search "query"

# Watch workspace (safe, default behavior)
node smart-files.js --watch ./src 30

# Watch external path (use with caution)
node smart-files.js --watch /path --force
```

## Safety Defaults

| Feature | Default | Override |
|---------|---------|----------|
| Binary files | Skipped | Cannot override |
| File size limit | 10MB | Cannot override |
| Search results cap | 20 | Cannot override |
| Workspace boundary | Enforced | --force |
| Watch mode scope | Workspace | --force |
| Rename mode | Dry run | --force |
| Content snippets | Shown | --quiet |