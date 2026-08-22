---
name: batch-file-rename
description: Batch rename files with pattern substitution, prefix/suffix addition, sequential numbering, case conversion, and extension changes. Dry-run by default for safety. Use when you need to rename multiple files at once, standardize naming conventions, add sequence numbers, or convert file extensions in bulk.
metadata:
  openclaw:
    emoji: "🔁"
---

# Batch File Rename

Safely rename multiple files with preview-first semantics.

## When to use it

- Standardize filenames across a directory (e.g., all lowercase, spaces → underscores)
- Add sequential numbers (`photo_001.jpg`, `photo_002.jpg`, …)
- Add prefixes or suffixes to batches of files
- Replace patterns in filenames (e.g., `draft_` → `final_`)
- Change extensions in bulk (`.JPG` → `.jpg`, `.md` → `.txt`)
- Revert accidental renames via generated undo script

## Prerequisites

- `bash` 4+
- `python3` (optional, for Unicode-safe slugify)
- No external dependencies required

## Quick Start

### 1. Dry-run (always do this first)

```bash
bash scripts/batch-rename.sh --dir /path/to/files --dry-run
```

Output example:
```
[DRY-RUN] photo 1.JPG → photo_001.JPG
[DRY-RUN] photo 2.JPG → photo_002.JPG
[DRY-RUN] photo 3.JPG → photo_003.JPG
3 files will be renamed
```

### 2. Add sequential numbers

```bash
bash scripts/batch-rename.sh --dir ./photos --number --prefix "vacation_" --start 1 --digits 3
```

### 3. Pattern substitution

```bash
bash scripts/batch-rename.sh --dir ./docs --replace "draft_" --with "final_"
```

### 4. Change case + extension

```bash
bash scripts/batch-rename.sh --dir ./files --lowercase --ext-lower
```

### 5. Full options

```bash
bash scripts/batch-rename.sh [OPTIONS]

Options:
  --dir DIR        Target directory (required)
  --dry-run        Preview changes without renaming
  --number         Add sequential numbers
  --prefix P       Prepend P to each filename
  --suffix S       Append S before extension
  --start N        Starting number for --number (default: 1)
  --digits N       Pad width for --number (default: 3)
  --replace FROM   Replace FROM pattern in filenames
  --with TO        Replace with TO (default: empty)
  --lowercase      Convert filenames to lowercase
  --uppercase      Convert filenames to uppercase
  --ext-lower      Convert extensions to lowercase
  --ext-upper      Convert extensions to uppercase
  --glob PAT       Only match files matching PAT (default: *)
  --undo FILE      Undo using a previous rename log
  --log FILE       Write rename log to FILE (default: <dir>/.rename-log-<timestamp>)
  -h, --help       Show this help
```

## Safety Features

1. **Dry-run by default** — always preview before committing
2. **Collision detection** — aborts if two files would get the same name
3. **Rename log** — every real run writes a log that can `--undo`
4. **No overwrite** — refuses to overwrite existing files

## Undo

Every real run generates `<dir>/.rename-log-<timestamp>`:

```
RENAME|photo 1.JPG|photo_001.JPG
RENAME|photo 2.JPG|photo_002.JPG
```

Undo:
```bash
bash scripts/batch-rename.sh --undo ./photos/.rename-log-20260816-231500
```

## Examples

### Standardize a download folder

```bash
bash scripts/batch-rename.sh --dir ~/Downloads --lowercase --ext-lower --replace " " --with "_"
```

### Number photos for a gallery

```bash
bash scripts/batch-rename.sh --dir ./gallery --number --prefix "img_" --digits 4 --start 100
```

### Convert .JPG to .jpg in place

```bash
bash scripts/batch-rename.sh --dir ./photos --ext-lower --glob "*.JPG"
```

## Script

See `scripts/batch-rename.sh` for the full implementation.
