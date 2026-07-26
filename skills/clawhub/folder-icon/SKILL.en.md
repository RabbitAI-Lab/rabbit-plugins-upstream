---
name: folder-icon
description: Batch-generate and apply colorful custom icons to Windows subfolders. Two approaches: (A) Tabler Icons — centralized icon directory with relative path references (default, portable); (B) MDI Icons — icons placed inside each subfolder (folder.ico), no external directory needed. Use when: "batch set folder icons", "set folder icon", "color-code folders". Output: .ico files + desktop.ini (ANSI encoded, relative paths) + attribute setup. Windows only.
---

# folder-icon Skill

Batch-generate and apply colorful custom icons to subfolders.

Supports **two approaches**:

| Option | SVG Source | Icon Location | Folder Attribute | Use Case |
|--------|-----------|---------------|-----------------|----------|
| **A. Tabler** (default) | [Tabler Icons](https://pictogrammers.com/library/icon/) | Central `.folder-icons/` directory | `+S` (System) | Portable, batch management |
| **B. MDI** | [Material Design Icons](https://pictogrammers.com/library/mdi/) | Per-folder `folder.ico` | `+R` (ReadOnly) | Flat structure, no external deps |

> **Design principle**: Option A places the icon directory inside the target folder (e.g., `.folder-icons/`), making the structure self-contained and portable.
> Option B has no separate icon directory, suitable for one-time setup or when you don't want hidden folders.

## Directory Structure

```
folder-icon/
├── SKILL.md              # This file
├── scripts/
│   ├── folder_icon.py    # Core script — Option A (Tabler)
│   ├── folder_icon_mdi.py# Add-on script — Option B (MDI)
│   └── icon_config.yaml  # Icon mapping config example
├── references/
│   └── icon-mappings.md  # Built-in icon mapping table
└── examples/
    └── source-mapping.md # Example mapping table
```

---

## Option A: Tabler (recommended for complex directories)

```bash
# Standard usage (icon directory defaults to .folder-icons/ inside target)
python skills/folder-icon/scripts/folder_icon.py "D:\TargetDirectory"

# Preview only
python skills/folder-icon/scripts/folder_icon.py "D:\TargetDirectory" --dry-run

# Force regenerate
python skills/folder-icon/scripts/folder_icon.py "D:\TargetDirectory" --force

# Custom icon directory name
python skills/folder-icon/scripts/folder_icon.py "D:\TargetDirectory" --icon-dir "my-icons"
```

### Workflow

1. Read `scripts/icon_config.yaml` (SVG source, folder→icon mappings)
2. Icon output directory defaults to `TargetDirectory/.folder-icons/` (override with `--icon-dir`)
3. Iterate subfolders, generate colored .ico per mapping (download SVG from Tabler CDN → colorize → render)
4. Write `desktop.ini` for each subfolder (**ANSI encoded**, IconResource uses **relative path**)
5. Set folder `+S` attribute + desktop.ini `+S +H` attributes
6. Prompt user to refresh Explorer

### Configuration Mapping

```yaml
explicit_mappings:
  - folder: "Documents"
    icon: "book-outline.ico"
    rgb: [33, 150, 243]
    color: "Blue"
```

### Dependencies

```bash
pip install svglib reportlab Pillow PyYAML requests
```

---

## Option B: MDI (for simple flat directories)

```bash
python skills/folder-icon/scripts/folder_icon_mdi.py "D:\TargetDirectory"
```

### Key Differences

- **Icon location**: Each subfolder holds its own `folder.ico`; `desktop.ini` references `folder.ico,0` (same directory)
- **Folder attribute**: Uses `+R` (ReadOnly) instead of `+S` (System)
- **SVG source**: [Material Design Icons](https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/)
- **Visual style**: Colored rounded-square background + white MDI icon
- **ICO sizes**: 7 sizes (16-256), rendered from 512x512 SVG
- **No config file**: Icon mapping is in a Python dict (suitable for one-time setup)

### Dependencies

```bash
pip install Pillow cairosvg
```

---

## Key Implementation Details (common)

- **desktop.ini encoding**: Must be `encoding='ansi'`, otherwise Windows Explorer cannot read it
- **IconResource path**: Option A uses relative paths (e.g., `..\.folder-icons\book-outline.ico`); Option B uses `folder.ico,0`
- **attrib command**: Paths with spaces must be quoted (e.g., `attrib +R "D:\My Games"`)

### Folder Attribute Setup

- **Option A**: Folder `+S` + desktop.ini `+S +H`
- **Option B**: Folder `+R` + desktop.ini `+H +S`
- Both attribute combinations make desktop.ini effective in Windows Explorer
- WSL-written files lose Windows attributes; use **VBScript** or **attrib (cmd.exe)** to set them

### VBScript Attribute Example

```vbs
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

' Option B: Folder +R, desktop.ini +H+S
Dim folder: Set folder = fso.GetFolder("D:\path\to\folder")
folder.Attributes = folder.Attributes Or 1  ' +R (ReadOnly)

Dim ini: Set ini = fso.GetFile(folder.Path & "\desktop.ini")
ini.Attributes = ini.Attributes Or 2 Or 4 ' +H +S (Hidden + System)
```

### Refresh Icon Cache

```batch
taskkill /f /im explorer.exe
del /a /q "%localappdata%\Microsoft\Windows\Explorer\iconcache*"
del /a /q "%localappdata%\IconCache.db"
start explorer.exe
```

Or press **F5** to refresh.

---

## Icon List

- Option A icon mappings: see `references/icon-mappings.md` (40+ common Tabler icons)
- Option B example mapping: see `examples/source-mapping.md`

## FAQ

**Q: desktop.ini not working, icons not showing?**
→ Verify: ① desktop.ini is ANSI encoded; ② IconResource path is correct; ③ Folder has `+S` (Option A) or `+R` (Option B) attribute; ④ desktop.ini has `+S +H` attributes

**Q: Icon colors wrong?**
→ Option A's `svg_colorize()` only replaces `currentColor`, `stroke`, `fill`; gradients (`stop-color`) and `stroke="none"` are preserved

**Q: WSL attribute setup not working?**
→ WSL's chmod/drvfs cannot set Windows attributes; use Windows-native `attrib` cmd.exe or VBScript

**Q: Icons appear blurry?**
→ Ensure ICO contains at least 4 sizes (16/32/48/256). Option B includes 7 sizes. Restart Explorer and clear cache, then retry
