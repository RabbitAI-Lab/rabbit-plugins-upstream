# folder-icon

为 Windows 目录下的子文件夹批量生成并应用彩色图标。支持 **Tabler Icons**（集中图标目录）和 **MDI**（图标内嵌文件夹）两种方案。

## 功能

- 🎨 **批量生成彩色 .ico 图标** — 从 Tabler/MDI SVG 源着色渲染
- 📁 **自动配置 desktop.ini** — ANSI 编码 + 相对路径引用
- 🔧 **设置文件夹属性** — `+S` 或 `+R`，确保图标生效
- 🔄 **支持 WSL 环境** — 自动路径转换 + VBScript 属性设置
- 📦 **自包含结构** — 图标目录在目标目录内，可整体迁移

## 安装

### OpenClaw 用户

```bash
clawhub install folder-icon
```

或直接放入技能目录：

```bash
git clone https://github.com/holdyounger/folder-icon.git ~/.openclaw/skills/folder-icon
```

### 目录结构

```
folder-icon/
├── SKILL.md                    # 技能主文件（含完整文档）
├── SKILL.en.md                 # 英文版技能文档
├── VERSION                     # 版本
├── scripts/
│   ├── folder_icon.py          # 方案A — Tabler Icons（集中图标目录）
│   ├── folder_icon_mdi.py      # 方案B — MDI（图标内嵌文件夹）
│   ├── folder-icon.js          # Node.js 版（方案A，WSL 路径转换）
│   └── icon_config.yaml        # 图标映射配置示例
├── references/
│   └── icon-mappings.md        # 内置图标映射表（40+ Tabler + MDI 参考）
├── examples/
│   └── source-mapping.md       # 示例映射表
└── assets/                     # 静态资源
```

## 快速开始

### 方案A：Tabler Icons（推荐用于复杂目录）

```bash
# 安装依赖
pip install svglib reportlab Pillow PyYAML requests

# 运行
python scripts/folder_icon.py "D:\目标目录"

# 仅预览
python scripts/folder_icon.py "D:\目标目录" --dry-run
```

### 方案B：MDI（适合简单扁平目录）

```bash
# 安装依赖
pip install Pillow cairosvg

# 运行
python scripts/folder_icon_mdi.py "D:\目标目录"
```

### 配置映射（方案A）

编辑 `scripts/icon_config.yaml`：

```yaml
icon_dir: '.folder-icons'
explicit_mappings:
  - folder: "文档"
    icon: "book-outline.ico"
    rgb: [33, 150, 243]
    color: "蓝"
```

## 两种方案对比

| 方案 | SVG 来源 | 图标位置 | 文件夹属性 | 适用场景 |
|------|---------|----------|-----------|---------|
| **A. Tabler** (默认) | Tabler Icons CDN | 集中 `.folder-icons/` 目录 | `+S` (System) | 便于整体迁移、批量管理 |
| **B. MDI** | Material Design Icons | 每个子文件夹内 `folder.ico` | `+R` (ReadOnly) | 结构扁平、独立不依赖外部路径 |

## 使用场景

- **项目目录美化** — 为不同类型的项目文件夹设置不同图标
- **资料分类** — 书籍、文档、代码、游戏各自有醒目标识
- **批量管理** — 一次配置，自动为所有子文件夹生成图标

## 许可证

MIT
