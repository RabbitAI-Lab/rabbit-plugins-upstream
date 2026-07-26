---
name: folder-icon
description: 为 Windows 目录下的子文件夹批量生成并应用彩色图标。支持两种方案：(A) Tabler Icons — 集中图标目录 + 相对路径引用（默认，可整体迁移）；(B) MDI Icons — 图标直接放在每个子文件夹内部（folder.ico），无需独立图标目录。使用场景："批量设置文件夹图标"、"设置文件夹 icon"、"为目录设置图标"、"文件夹图标配色"。输出：生成 .ico 文件 + 写入 desktop.ini（ANSI 编码、相对路径） + 设置属性。仅限 Windows。
---

# folder-icon Skill

为目录下的子文件夹批量生成并应用彩色图标。

支持**两种方案**：

| 方案 | SVG来源 | 图标位置 | 文件夹属性 | 适用场景 |
|------|---------|----------|-----------|---------|
| **A. Tabler** (默认) | [Tabler Icons](https://pictogrammers.com/library/icon/) | 集中 `.folder-icons/` 目录 | `+S` (System) | 便于整体迁移、批量管理 |
| **B. MDI** | [Material Design Icons](https://pictogrammers.com/library/mdi/) | 每个子文件夹内 `folder.ico` | `+R` (ReadOnly) | 结构扁平、独立不依赖外部路径 |

> **设计原则**：方案A的图标目录放在目标目录内部（如 `.folder-icons/`），整个结构自包含、可整体迁移。
> 方案B无单独图标目录，适合一次性设置或不想在目录中增加隐藏文件夹的场景。

## 目录结构

```
folder-icon/
├── SKILL.md              # 本文件
├── scripts/
│   ├── folder_icon.py    # 核心脚本——方案A（Tabler）
│   ├── folder_icon_mdi.py# 附加脚本——方案B（MDI）
│   └── icon_config.yaml  # 图标映射配置示例
├── references/
│   └── icon-mappings.md  # 内置图标映射表
└── examples/
    └── source-mapping.md # 示例映射表
```

---

## 方案A：Tabler（推荐用于复杂目录）

```bash
# 标准用法（图标目录默认 .folder-icons/，在目标目录内）
python skills/folder-icon/scripts/folder_icon.py "D:\目标目录"

# 仅预览
python skills/folder-icon/scripts/folder_icon.py "D:\目标目录" --dry-run

# 强制重新生成
python skills/folder-icon/scripts/folder_icon.py "D:\目标目录" --force

# 自定义图标目录名
python skills/folder-icon/scripts/folder_icon.py "D:\目标目录" --icon-dir "my-icons"
```

### 流程

1. 读取 `scripts/icon_config.yaml`（SVG 来源、文件夹→图标映射）
2. 图标输出目录默认为 `目标目录/.folder-icons/`（可通过 `--icon-dir` 覆盖目录名）
3. 遍历目标目录子文件夹，按映射生成彩色 .ico（从 Tabler CDN 下载 SVG → 着色 → 渲染）
4. 为子文件夹写入 `desktop.ini`（**ANSI 编码**，IconResource 为**相对路径**，从子文件夹指向目标目录内的图标目录）
5. 设置文件夹 `+S` 属性 + desktop.ini `+S +H` 属性
6. 完成后提示用户刷新 Explorer

### 配置映射

```yaml
explicit_mappings:
  - folder: "文档"
    icon: "book-outline.ico"
    rgb: [33, 150, 243]
    color: "蓝"
```

### 依赖

```bash
pip install svglib reportlab Pillow PyYAML requests
```

---

## 方案B：MDI（适合简单扁平目录）

```bash
python skills/folder-icon/scripts/folder_icon_mdi.py "D:\目标目录"
```

### 核心区别

- **图标位置**：每个子文件夹自己持有 `folder.ico`，`desktop.ini` 引用 `folder.ico,0`（同目录）
- **文件夹属性**：使用 `+R` (ReadOnly) 而非 `+S` (System)，更符合资源管理器图标显示约定
- **SVG来源**：[Material Design Icons](https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/)（raw.githubusercontent.com）
- **背景色**：彩色圆角方块 + 白色MDI图标，风格统一鲜明
- **ICO 尺寸**：7种（16-256），从 512x512 SVG 渲染，清晰度高
- **无依赖配置文件**：图标映射直接写在 Python 字典中（适合一次性设置）

### MDI 图标命名

MDI SVG 源 URL：`https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/{name}.svg`

查询图标：https://pictogrammers.com/library/mdi/

### 依赖

```bash
pip install Pillow cairosvg
```

---

## 关键实现细节（通用）

- **desktop.ini 编码**：必须 `encoding='ansi'`，否则 Windows Explorer 无法读取
- **IconResource 路径**：方案A用相对路径（如 `..\.folder-icons\book-outline.ico`）；方案B直接用 `folder.ico,0`
- **attrib 命令**：路径含空格时必须加引号（如 `attrib +R "D:\My Games"`）

### 文件夹属性设置要点

- **方案A**：文件夹 `+S` + desktop.ini `+S +H`
- **方案B**：文件夹 `+R` + desktop.ini `+H +S`
- 两种属性组合在 Windows 上都能使 desktop.ini 生效
- WSL 写入的文件会丢失 Windows 文件属性，务必用 **VBScript** 或 **attrib（cmd.exe）** 设置

### VBScript 设置属性示例

```vbs
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

' 方案B：文件夹 +R，desktop.ini +H+S
Dim folder: Set folder = fso.GetFolder("D:\path\to\folder")
folder.Attributes = folder.Attributes Or 1  ' +R（ReadOnly）

Dim ini: Set ini = fso.GetFile(folder.Path & "\desktop.ini")
ini.Attributes = ini.Attributes Or 2 Or 4 ' +H +S（Hidden + System）
```

### 刷新图标缓存

```batch
taskkill /f /im explorer.exe
del /a /q "%localappdata%\Microsoft\Windows\Explorer\iconcache*"
del /a /q "%localappdata%\IconCache.db"
start explorer.exe
```

或按 **F5** 刷新。

---

## 图标列表

- 方案A图标映射见 `references/icon-mappings.md`（40+ 个常用 Tabler 图标）
- 方案B的示例映射见 `examples/source-mapping.md`

## 常见问题

**Q: desktop.ini 无效，图标不显示？**
→ 确认：① desktop.ini 为 ANSI 编码；② IconResource 路径正确；③ 文件夹有 `+S`(方案A)或`+R`(方案B)属性；④ desktop.ini 有 `+S +H` 属性

**Q: 图标颜色不对？**
→ 方案A的 `svg_colorize()` 仅替换 `currentColor`、`stroke`、`fill`，渐变（`stop-color`）和 `stroke="none"` 保留原样

**Q: WSL 设置属性不生效？**
→ WSL 的 chmod/drvfs 无法设置 Windows 属性，必须用 Windows 本地的 `attrib` cmd.exe 或 VBScript 设置

**Q: 图标显示模糊？**
→ 确认 ICO 包含至少 4 种尺寸（16/32/48/256）。方案B内置 7 种尺寸。重启 Explorer 清除缓存后重试