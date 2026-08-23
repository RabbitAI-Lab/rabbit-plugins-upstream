---
name: file-tidy
description: >-
  纯本地文件整理工具——按类型或日期批量归类、批量重命名、清理空目录与重复文件、平铺嵌套目录。
  零第三方依赖、跨平台（Windows/macOS/Linux）、无需任何 API Key，所有破坏性操作默认预览、显式 --apply 才执行。
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F9F9"
    requires:
      bins:
        - python3
    homepage: https://clawhub.ai
---

# File Tidy · 文件整理助手

一个安全、零依赖的本地文件整理 CLI。适合在用户想把杂乱的下载目录、桌面或项目文件夹
整理成有序结构时使用。所有移动/删除/重命名操作**默认只预览（dry-run）**，加上 `--apply`
才会真正执行，避免误删。

## 何时使用

- 用户想“整理/归类/归档”某个文件夹（如下载目录、桌面、桌面截图堆）
- 用户想“批量重命名”一堆文件（加前缀、序号、转小写、空格改连字符）
- 用户想“删除重复文件”或“清理空目录”
- 用户想把多层嵌套目录“平铺”成一层

**不要**在用户未明确指向某个目录时使用本 skill；操作前先确认目标路径。

## 前置要求

- 已安装 `python3`（无需 pip 安装任何第三方包，全部使用标准库）

## 安装方式

无需安装。直接调用脚本：

```bash
python3 <skill_dir>/file_tidy.py --help
```

## 子命令

### 1. organize —— 归类文件

```bash
# 按扩展名归类到 Images/Documents/Videos/... 子目录（仅预览）
python3 <skill_dir>/file_tidy.py organize ~/Downloads --by ext

# 按修改日期归类到 2026/2026-08/ 子目录
python3 <skill_dir>/file_tidy.py organize ~/Downloads --by date

# 确认无误后真正执行
python3 <skill_dir>/file_tidy.py organize ~/Downloads --by ext --apply
```

`--by` 取值：`ext`（按文件类型）| `date`（按修改年月）。
`--depth` 仅 date 模式可用：`month`（默认，YYYY-MM）| `year`（仅 YYYY）。

### 2. rename —— 批量重命名

```bash
# 加前缀 + 序号，如 report-01.txt、report-02.txt
python3 <skill_dir>/file_tidy.py rename ~/Photos --prefix trip --sequence

# 转小写、空格改连字符（仅预览）
python3 <skill_dir>/file_tidy.py rename ~/Photos --lowercase --spaces-to-dash

# 递归处理子目录
python3 <skill_dir>/file_tidy.py rename ~/Photos --lowercase --recursive --apply
```

可用标志：`--prefix <text>`、`--suffix <text>`、`--sequence`（追加两位序号）、
`--lowercase`、`--spaces-to-dash`、`--recursive`。

### 3. clean —— 清理空目录与重复文件

```bash
# 列出空目录与重复文件（只读，安全）
python3 <skill_dir>/file_tidy.py clean ~/Downloads

# 删除空目录 + 重复文件（保留每组中路径字典序最小的）
python3 <skill_dir>/file_tidy.py clean ~/Downloads --empties --dupes --apply
```

`--empties` 删除空目录；`--dupes` 删除重复文件（按 sha256 比对，保留第一个）。
默认仅报告，不删除。

### 4. flatten —— 平铺嵌套目录

```bash
python3 <skill_dir>/file_tidy.py flatten ~/Project --apply
```

把目标目录内所有层级的文件移动到根目录（重名自动加 `(1)`、`(2)` 后缀）。

### 5. duplicates —— 仅列出重复文件

```bash
python3 <skill_dir>/file_tidy.py duplicates ~/Downloads
```

## 安全约定

> 本 skill 的核心安全原则：**默认 dry-run**。除非用户明确说“执行/应用/确认”，
> 否则先以预览模式运行并向用户展示将要发生的改动，再决定是否加 `--apply`。

- 移动/重命名遇到同名冲突时，自动追加 `(1)`、`(2)` 后缀，绝不静默覆盖
- 重复文件删除始终保留每组中字典序最小的路径
- 不读取、不上传任何文件内容；纯本地运行，无网络请求、无 API Key

## 参数速查

| 子命令 | 关键参数 | 说明 |
|--------|----------|------|
| `organize` | `--by ext\|date`、`--depth month\|year` | 归类 |
| `rename` | `--prefix`、`--suffix`、`--sequence`、`--lowercase`、`--spaces-to-dash`、`--recursive` | 重命名 |
| `clean` | `--empties`、`--dupes` | 清理 |
| `flatten` | （无） | 平铺 |
| `duplicates` | （无） | 列出重复 |
| 通用 | `--apply` | 真正执行（否则仅预览） |

## License

MIT-0（ClawHub 发布默认许可）。可自由使用、修改、再分发，无需署名。
