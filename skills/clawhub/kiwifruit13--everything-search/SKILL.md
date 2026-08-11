---
name: everything-search
description: 开箱即用的 Windows 本地文件极速搜索引擎。通过内置 Everything 引擎毫秒级检索本机文件与文件夹，支持名称/大小/日期/类型/正则/内容等多维过滤，输出结构化 JSON。当用户需要找文件、搜索本地文件、定位文件路径、按条件筛选文件（如大于100MB的exe、最近修改的文档）时使用。
---

# Everything 本地文件搜索

基于 Everything 引擎的 Windows 本地文件极速搜索。内置 IPC 客户端与 CLI 二进制，用户机器已装 Everything 时直接复用其索引，无需额外配置。

## 任务目标

- 本 Skill 用于：Windows 系统上的本地文件极速搜索与定位
- 能力包含：文件名/路径搜索、大小过滤、日期过滤、类型过滤、正则匹配、内容搜索
- 触发条件：用户表达"找文件""搜索本地""定位路径""列出大于X的文件""最近修改的文档"等意图

## 前置准备

- 依赖说明：脚本使用 Python 标准库，无需额外安装
- 运行环境：Windows 系统（Everything 依赖 NTFS）
- 服务端要求：用户机器需运行 Everything 程序（脚本会自动尝试启动内置版本）

## Everything 查询语法

掌握查询语法是精准搜索的关键。以下是完整语法参考：

### 基础语法

| 语法 | 说明 | 示例 |
|------|------|------|
| `关键词` | 文件名包含关键词 | `报告`、`readme` |
| `*.ext` | 指定扩展名 | `*.pdf`、`*.exe` |
| `prefix*` | 前缀匹配 | `doc*`、`2024*` |
| `"精确短语"` | 精确匹配（含空格） | `"annual report"` |

### 过滤语法

| 语法 | 说明 | 示例 |
|------|------|------|
| `size:>X` | 大于指定大小 | `size:>100mb` |
| `size:<X` | 小于指定大小 | `size:<1mb` |
| `size:X-Y` | 大小范围 | `size:10mb-100mb` |
| `date:>YYYY/M/D` | 修改日期晚于 | `date:>2024/1/1` |
| `date:<YYYY/M/D` | 修改日期早于 | `date:<lastmonth` |
| `date:today` | 今天修改 | `date:today` |
| `date:thisweek` | 本周修改 | `date:thisweek` |
| `folder:` | 仅文件夹 | `folder:报告` |
| `file:` | 仅文件 | `file:*.log` |
| `parent:path` | 限定父目录 | `parent:C:\Users\Documents` |

### 大小单位

`b`（字节）、`kb`、`mb`、`gb`、`tb`

### 高级语法

| 语法 | 说明 | 示例 |
|------|------|------|
| `regex:pattern` | 正则表达式 | `regex:report_\d+\.pdf` |
| `content:keyword` | 内容搜索（需开启内容索引） | `content:密码` |
| `attrib:A` | 属性过滤（A=存档, S=系统, H=隐藏, R=只读） | `attrib:H` |
| `type:audio/video/image/doc/compressed/executable` | 文件类型 | `type:image` |

### 组合查询

多个条件用空格分隔，表示 AND 关系：

```
*.pdf size:>1mb date:>2024/1/1
folder:report parent:C:\Users
```

### 排序标记

在查询末尾添加 `sort:` 标记：

| 标记 | 说明 |
|------|------|
| `sort:name` / `sort:name-` | 名称升序/降序 |
| `sort:size` / `sort:size-` | 大小升序/降序 |
| `sort:dm` / `sort:dm-` | 修改时间升序/降序 |
| `sort:dc` / `sort:dc-` | 创建时间升序/降序 |
| `sort:path` / `sort:path-` | 路径升序/降序 |

## 搜索策略

根据用户意图构造合适的查询：

### 意图识别

| 用户表达 | 搜索策略 |
|---------|---------|
| "找/搜/定位 xxx" | 直接搜索关键词 |
| "大于 X 的文件" | 添加 `size:>X` |
| "最近修改/今天的文件" | 添加 `date:today` 或 `date:thisweek` |
| "所有 PDF/图片/视频" | 使用 `*.pdf` 或 `type:image/video` |
| "某个目录下的文件" | 添加 `parent:path` |
| "隐藏文件/系统文件" | 添加 `attrib:H` 或 `attrib:S` |
| "文件名包含空格" | 使用 `"精确短语"` |

### 结果解读

- `is_folder: true` 表示文件夹，`false` 表示文件
- `size` 为字节数，可转换为 KB/MB/GB 展示
- `date_modified` 为修改时间，可用于排序或筛选
- `total` 是命中总数，`returned` 是本次返回数，差异大时提示用户可分页

### 分页处理

当 `total > returned` 时，使用 `--offset` 参数获取后续结果：

```bash
python scripts/search.py "*.pdf" -n 50 --offset 50
```

## 操作步骤

1. 解析用户意图，构造 Everything 查询语法
2. 调用搜索脚本：
   ```bash
   python scripts/search.py "<查询语法>" -n <数量> [--offset <偏移>] [-e <引擎>]
   ```
3. 解析 JSON 输出，根据用户需要格式化展示
4. 若结果过多，提示用户可添加过滤条件或分页查看

## 使用示例

### 示例 1：查找大文件

- 场景：用户说"找出所有大于 100MB 的文件"
- 查询构造：`size:>100mb`
- 脚本调用：
  ```bash
  python scripts/search.py "size:>100mb" -n 20 -e ipc
  ```
- 预期产出：按大小降序返回大文件列表
- 关键要点：添加 `sort:size-` 可按大小降序排列

### 示例 2：查找最近修改的文档

- 场景：用户说"今天修改过的 Word 文档"
- 查询构造：`*.docx date:today`
- 脚本调用：
  ```bash
  python scripts/search.py "*.docx date:today" -n 50
  ```
- 预期产出：今天修改的所有 .docx 文件
- 关键要点：`date:today` 精确匹配今天，`date:thisweek` 匹配本周

### 示例 3：定位特定路径下的文件

- 场景：用户说"在 D:\Projects 下找所有 Python 文件"
- 查询构造：`*.py parent:D:\Projects`
- 脚本调用：
  ```bash
  python scripts/search.py "*.py parent:D:\Projects" -n 100
  ```
- 预期产出：指定目录下的所有 .py 文件
- 关键要点：`parent:` 限定搜索范围，避免全盘搜索

## 资源索引

- 脚本：见 [scripts/search.py](scripts/search.py)（纯引擎调用，输出 JSON）
- 资产：见 [assets/](assets/)（Everything64.dll、es.exe、Everything.exe 等二进制文件）

## 注意事项

- 仅支持 Windows 系统（Everything 依赖 NTFS 文件系统）
- 用户机器需运行 Everything 程序；若未运行，脚本会尝试启动内置版本
- 内容搜索（`content:`）需要用户在 Everything 中手动开启内容索引
- 网络驱动器默认不被索引
- 某些系统目录需要管理员权限才能索引

### CLI 引擎局限

默认使用 IPC 引擎，支持全部搜索运算符。仅在强制指定 `-e cli` 时使用 CLI 引擎（es.exe），该引擎存在以下局限：

| 运算符 | CLI 支持 | 说明 |
|--------|---------|------|
| `folder:` / `file:` | ✅ | 正常支持 |
| `size:>X` / `size:<X` | ❌ | 返回 0 条结果 |
| `ext:xxx` | ❌ | 返回 0 条结果 |
| `date:>YYYY/M/D` | ❌ | 返回 0 条结果 |
| `regex:` | ❌ | 不支持正则 |

**规避方案**：使用默认引擎（auto/ipc）即可避免此问题。如需大小/日期过滤，请勿使用 `-e cli`。
