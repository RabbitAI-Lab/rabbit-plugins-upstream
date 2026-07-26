# 示例映射表

## 项目背景

为目标目录下 20 个子文件夹批量生成自定义文件夹图标，使用 **MDI (Material Design Icons)** 方案。

## 映射表

| 文件夹 | MDI 图标 | 背景色 | 说明 |
|---|---|---|---|
| `ProjectA` | `shield-lock` | `#E84D39` | 安全工具，红色盾牌 |
| `ProjectB` | `application-braces` | `#0078D4` | C++项目，蓝色花括号 |
| `ProjectC` | `blur` | `#9C27B0` | UI磨砂效果，紫色 |
| `ProjectD` | `floor-plan` | `#FF9800` | 户型生成工具，橙色 |
| `ProjectE` | `lock-open-variant` | `#F44336` | Ark工具，红色解锁 |
| `ProjectF` | `calendar-clock` | `#2196F3` | 时间回溯，蓝色时钟 |
| `ProjectG` | `chat` | `#07C160` | 聊天UI，绿色 |
| `ProjectH` | `ferry` | `#4CAF50` | 摆渡工具，绿色 |
| `ProjectI` | `language-csharp` | `#68217A` | C#版，C#品牌紫 |
| `ProjectJ` | `microsoft-windows` | `#0078D4` | Windows内核，微软蓝 |
| `ProjectK` | `bug` | `#FF5722` | 调试工具，橙色臭虫 |
| `ProjectL` | `link-variant` | `#1565C0` | API使用，深蓝链接 |
| `ProjectM` | `chip` | `#37474F` | 驱动示例，灰蓝芯片 |
| `ProjectN` | `hexadecimal` | `#1A237E` | 内核研究，深蓝16进制 |
| `ProjectO` | `file-search-outline` | `#795548` | 规则匹配，棕色搜索 |
| `ProjectP` | `dot-net` | `#512BD4` | .NET相关，.NET紫色 |
| `repos` | `source-repository-multiple` | `#333333` | Git仓库，暗灰 |
| `docs` | `bookmark-multiple` | `#E91E63` | 文档指南，粉色书签 |
| `deps` | `package-variant-closed` | `#009688` | 包管理，青色 |
| `wiki` | `book-open-variant` | `#607D8B` | 知识库，蓝灰书籍 |

## 执行步骤（复现记录）

```python
# 1. 安装依赖
pip install Pillow cairosvg

# 2. 运行脚本
python skills/folder-icon/scripts/folder_icon_mdi.py "D:\目标目录" --force

# 3. 刷新图标缓存
taskkill /f /im explorer.exe
del /a /q "%localappdata%\Microsoft\Windows\Explorer\iconcache*"
start explorer.exe
```

## 注意点

- 脚本写入 `folder.ico` 后在 WSL 侧会丢失 Windows 文件属性，脚本会自动用 VBScript 重设
- 每个 desktop.ini 使用 `IconResource=folder.ico,0`（同目录引用）
- 文件夹设置 `+R` (ReadOnly) 属性，desktop.ini 设置 `+H +S` 属性
- ICO 包含 16/24/32/48/64/128/256 共 7 种尺寸，全部 PNG 内嵌
- SVG 源来自 MDI GitHub：`https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/{name}.svg`

## 效果

刷新后在文件资源管理器中选择 **超大图标** 视图，每个文件夹显示对应的彩色 MDI 图标，清晰无锯齿。
