# File Organizer — Examples

## Example 1: Preview before organizing (dry-run)

**User request**: "帮我把下载文件夹整理一下"（先预览）

**Command** (Windows):

```powershell
powershell -ExecutionPolicy Bypass -File scripts/organize-files.ps1 -Dir . -DryRun
```

**Sample output**:

```
===== Organization Plan (9 files) =====
  [Images] 3 file(s)
  [Documents] 2 file(s)
  [Code] 1 file(s)
  [Archives] 1 file(s)
  [Others] 2 file(s)

[DRY-RUN] Preview only - nothing was moved.
```

## Example 2: Execute by type

**Before**:

```
Downloads/
├── photo1.jpg
├── photo2.png
├── report.pdf
├── notes.txt
├── script.py
├── backup.zip
└── README
```

**Command**:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/organize-files.ps1 -Dir .
```

**After**:

```
Downloads/
├── Images/      (photo1.jpg, photo2.png)
├── Documents/   (report.pdf, notes.txt)
├── Code/        (script.py)
├── Archives/    (backup.zip)
├── Others/      (README)
└── organize-report.md
```

## Example 3: Organize by date

**Command**:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/organize-files.ps1 -Dir . -ByDate -DryRun
```

Files are grouped into folders named `yyyy-MM` according to their
`LastWriteTime`, e.g. `2026-08/` for files modified in August 2026.
