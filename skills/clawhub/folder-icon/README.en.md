# folder-icon

Batch-generate and apply colorful custom icons to Windows subfolders. Supports two approaches: **Tabler Icons** (centralized icon directory) and **MDI** (icons embedded in each folder).

## Features

- 🎨 **Batch generate colorful .ico files** — colorize SVG from Tabler/MDI source
- 📁 **Auto-configure desktop.ini** — ANSI encoding + relative path references
- 🔧 **Set folder attributes** — `+S` or `+R` to ensure icons take effect
- 🔄 **WSL support** — automatic path conversion + VBScript attribute setting
- 📦 **Self-contained** — icon directory inside target folder, portable

## Installation

### OpenClaw Users

```bash
clawhub install folder-icon
```

Or clone directly into your skills directory:

```bash
git clone https://github.com/holdyounger/folder-icon.git ~/.openclaw/skills/folder-icon
```

## Quick Start

### Option A: Tabler Icons (recommended for complex directories)

```bash
# Install dependencies
pip install svglib reportlab Pillow PyYAML requests

# Run
python scripts/folder_icon.py "D:\TargetDirectory"

# Preview only
python scripts/folder_icon.py "D:\TargetDirectory" --dry-run
```

### Option B: MDI (for simple flat directories)

```bash
# Install dependencies
pip install Pillow cairosvg

# Run
python scripts/folder_icon_mdi.py "D:\TargetDirectory"
```

### Configuration (Option A)

Edit `scripts/icon_config.yaml`:

```yaml
icon_dir: '.folder-icons'
explicit_mappings:
  - folder: "Documents"
    icon: "book-outline.ico"
    rgb: [33, 150, 243]
    color: "Blue"
```

## Comparison

| Option | SVG Source | Icon Location | Folder Attribute | Use Case |
|--------|-----------|---------------|-----------------|----------|
| **A. Tabler** (default) | Tabler Icons CDN | Central `.folder-icons/` | `+S` (System) | Portable, batch management |
| **B. MDI** | Material Design Icons | Per-folder `folder.ico` | `+R` (ReadOnly) | Flat structure, no external deps |

## License

MIT
