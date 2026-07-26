# 内置图标映射表

命名规范：`<功能>-<风格>.ico`
- `-outline` = 线框风格，无后缀 = 填充风格
- 避免过长的复合名，同一概念用最少的词表达

## 完整映射表

| 图标文件名 | Tabler SVG 名 | 说明 |
|-----------|--------------|------|
| `account-search-outline.ico` | `user-search` | 背调/用户搜索 |
| `alert-outline.ico` | `alert-circle` | 告警/重要 |
| `cpu-outline.ico` | `cpu` | CPU/系统 |
| `bug-outline.ico` | `bug` | 调试/Bug |
| `circle-outline.ico` | `circle` | 圆形/360 |
| `device-laptop-outline.ico` | `device-laptop` | 虚拟机/笔记本 |
| `presentation-outline.ico` | `presentation` | PPT/演示 |
| `signal-outline.ico` | `signal` | 信号/抓包 |
| `book-outline.ico` | `book` | 文档/书籍 |
| `cactus.ico` | `cactus` | 仙人掌 |
| `chart-bar-outline.ico` | `chart-bar` | 图表/统计 |
| `cloud-download-outline.ico` | `cloud-download` | 云下载 |
| `cloud-upload-outline.ico` | `cloud-upload` | 云上传 |
| `code-outline.ico` | `code` | 代码/开发 |
| `database-outline.ico` | `database` | 数据库 |
| `download-outline.ico` | `download` | 下载 |
| `edit-outline.ico` | `edit` | 编辑/笔记 |
| `file-document-outline.ico` | `file-description` | 文档/文件 |
| `file-excel-outline.ico` | `file-spreadsheet` | Excel/表格 |
| `file-word-outline.ico` | `file-text` | Word/文本 |
| `folder-outline.ico` | `folder` | 文件夹 |
| `gamepad-outline.ico` | `device-gamepad` | 游戏 |
| `heart-outline.ico` | `heart` | 收藏/喜欢 |
| `link-outline.ico` | `link` | 链接 |
| `lock-outline.ico` | `lock` | 锁定/安全 |
| `mail-outline.ico` | `mail` | 邮件 |
| `music-outline.ico` | `music` | 音乐/音频 |
| `notebook-outline.ico` | `notes` | 笔记/日记 |
| `image-outline.ico` | `photo` | 图片/设计 |
| `school-outline.ico` | `school` | 学习/学校 |
| `search-outline.ico` | `search` | 搜索 |
| `terminal-outline.ico` | `terminal` | 终端/PowerShell |
| `shield-check-outline.ico` | `shield-check` | 安全/验证 |
| `star-outline.ico` | `star` | 收藏/星标 |
| `tool-outline.ico` | `tools` | 工具 |
| `trash-outline.ico` | `trash` | 回收站 |
| `upload-outline.ico` | `upload` | 上传 |
| `video-outline.ico` | `video` | 视频 |

> 完整图标库：https://pictogrammers.com/library/icon/

---

## MDI (Material Design Icons) 参考

MDI 图标适合方案B（folder_icon_mdi.py）。

- MDI 图标查询：https://pictogrammers.com/library/mdi/
- SVG 源：`https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/{name}.svg`

### 示例映射

完整映射见 `examples/source-mapping.md`

常用 MDI 图标：

| 用途 | 推荐图标 | 适合场景 |
|------|---------|---------|
| 安全/防护 | `shield-lock`, `shield-check` | 安全工具、防病毒 |
| 开发/源码 | `code-tags`, `application-braces`, `source-repository` | IDE、源码库 |
| Windows | `microsoft-windows` | 系统、内核 |
| 调试 | `bug` | 调试器、Bug追踪 |
| 数据库 | `database` | 数据存储 |
| 网络 | `link-variant`, `lan` | API、网络工具 |
| 硬件 | `chip`, `cpu` | 驱动、硬件 |
| 聊天 | `chat`, `chat-outline` | 即时通讯 |
| 工具 | `toolbox`, `cog`, `hammer-wrench` | 通用工具箱 |
| 书籍/文档 | `book-open-variant`, `bookmark-multiple` | 文档、Wiki |
| 包管理 | `package-variant-closed`, `package-variant` | 包管理器 |
| 时间 | `calendar-clock`, `clock-outline` | 日程、时间线 |
| 文件搜索 | `file-search-outline`, `file-code` | 文件分析 |
| 终端 | `console`, `console-line` | 命令行工具 |

## 添加新图标

### Tabler 方案


1. 在 [pictogrammers.com](https://pictogrammers.com/library/icon/) 选择图标，记下图标名（如 `chart-bar`）
2. 在 `scripts/folder_icon.py` 的 `ICON_TO_TABLER` 字典中添加一行：
   ```python
   "chart-bar-outline.ico": "chart-bar"
   ```
3. 在 `scripts/icon_config.yaml` 的 `explicit_mappings` 中使用：
   ```yaml
   - folder: "统计"
     icon: "chart-bar-outline.ico"
     rgb: [33, 150, 243]
     color: "蓝"
   ```
