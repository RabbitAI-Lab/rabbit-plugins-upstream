---
name: file-organizer
description: Sort and organize files in a directory by type or by modification date, with dry-run preview, duplicate-name handling, and an auto-generated organization report. Use when the user wants to clean up, sort, categorize, or organize files in a folder, or asks for a file classification/overview report.
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - powershell
---

# File Organizer

Organizes loose files in a directory into categorized subfolders, either by
file type or by modification date. Supports a dry-run mode that only previews
changes, and generates a Markdown summary report of what was moved where.

## When to use

Use this skill when the user asks to:

- Clean up / sort / organize a messy downloads or documents folder
- Group files by type (images, documents, videos, ...) or by date
- Get an overview report of what a folder contains

## Workflow

1. **Confirm scope**: Ask for the target directory (default: current
   directory) and the grouping mode (`by-type` or `by-date`).
2. **Dry-run first**: Always show a preview of the planned moves before
   touching any file.
3. **Execute**: After user confirmation, move the files into category
   subfolders.
4. **Report**: Write `organize-report.md` summarizing the result.

## Category mapping (by type)

| Extension(s) | Target folder |
|--------------|---------------|
| jpg, jpeg, png, gif, bmp, webp, svg, ico | Images |
| pdf, doc, docx, xls, xlsx, ppt, pptx, txt, md, csv, odt | Documents |
| mp4, avi, mkv, mov, wmv, flv, webm | Videos |
| mp3, wav, flac, aac, ogg, m4a | Audio |
| zip, rar, 7z, tar, gz, bz2 | Archives |
| py, js, ts, java, c, cpp, h, go, rs, html, css, json, xml, sh, ps1, sql | Code |
| *anything else* | Others |

Files without an extension (e.g. `README`) go to `Others`.

## Rules

- **Never move the script itself, category folders, or dotfiles** (files
  starting with `.`).
- **Name collisions**: if a target file already exists, append a numeric
  suffix, e.g. `photo (1).jpg`. Never overwrite.
- **Dry-run is the default first step** — show the plan as a table and wait
  for confirmation before moving anything.
- Skip empty folders; leave the folder structure of subdirectories untouched
  (only top-level loose files are organized; ask the user if they want
  recursion).

## Automated script (Windows)

```powershell
powershell -ExecutionPolicy Bypass -File scripts/organize-files.ps1 -Dir . -DryRun
powershell -ExecutionPolicy Bypass -File scripts/organize-files.ps1 -Dir . -ByDate
```

Parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-Dir` | `.` | Target directory to organize |
| `-ByType` | *on* | Group files by type (default mode) |
| `-ByDate` | off | Group files by year-month instead (e.g. `2026-08`) |
| `-DryRun` | off | Preview only; move nothing |
| `-Recurse` | off | Also organize files in subfolders |

The script prints a summary table and writes `organize-report.md` (unless in
dry-run mode).

## Notes

- Always present the dry-run table to the user and get explicit confirmation
  before moving files.
- If the folder has more than 200 files, group statistics in the report and
  keep the file list truncated.
- If the user asked to organize the workspace itself, never move the skill's
  own folder or the report file.

## Additional resources

- For sample inputs and expected outputs, see [examples.md](examples.md)
