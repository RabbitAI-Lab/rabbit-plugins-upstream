---
name: IMA 知识库模块
description: IMA 知识库操作模块。负责上传文件、添加网页/微信文章到知识库、搜索与浏览知识库内容、获取知识库信息。
allowed-tools: Bash,Read
metadata: {"openclaw":{"emoji":"📚","requires":{"bins":["node"]}}}
---

# Knowledge Base (知识库)

API base path: `openapi/wiki/v1` — 完整数据结构和接口参数详见 `references/api.md`。

## 接口决策表

| 用户意图                                      | 调用接口                                                               | 关键参数                                                                                           |
| --------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 上传文件到知识库                              | `check_repeated_names` → `create_media` → COS Upload → `add_knowledge` | `media_type`（按扩展名），`knowledge_base_id`，`file_name`，`file_size`                            |
| 上传文件到知识库的某个文件夹                  | 先定位文件夹 → 同上（`folder_id` 传入目标文件夹 ID）                   | 见「文件夹操作」章节                                                                               |
| 添加网页/微信文章到知识库                     | `import_urls`                                                          | `urls`（1-10 个），`knowledge_base_id`，可选 `folder_id`（省略则根目录）                           |
| 添加笔记到知识库                              | `add_knowledge`                                                        | `media_type=11`，`note_info.content_id=<note_id>`，`knowledge_base_id`                             |
| 添加 URL（文件型）到知识库                    | `check_repeated_names` → 下载文件 → 走"上传文件"流程                   | URL 指向 PDF/Word/PPT 等文件时，按文件方式处理                                                     |
| 检查文件名是否重复                            | `check_repeated_names`                                                 | `params[].name`，`params[].media_type`，`knowledge_base_id`，`folder_id`                           |
| 获取知识库信息                                | `get_knowledge_base`                                                   | `ids`（1-20 个，不重复）                                                                           |
| 浏览知识库内容列表 / 浏览文件夹               | `get_knowledge_list`                                                   | `knowledge_base_id`，`cursor`，`limit`(1~50)，可选 `folder_id`                                     |
| 在知识库中搜索（含文件和文件夹）              | `search_knowledge`                                                     | `query`，`knowledge_base_id`，`cursor`                                                             |
| 按关键词查找知识库（用户知道名字但不知道 ID） | `search_knowledge_base`                                                | `query`，`cursor`，`limit`(1~20)                                                                   |
| 查看/了解自己有哪些知识库                     | `search_knowledge_base`（`query` 传空字符串）                          | `query: ""`，`cursor`，`limit`(1~20)                                                               |
| 添加内容但**未指定**目标知识库                | `get_addable_knowledge_base_list` → 展示列表让用户选择                 | `cursor`，`limit`(1~50)                                                                            |
| 查看原文、分析原文、导出原文                  | `get_media_info`                                                       | `media_id`；导出/下载时在 URL 后追加 `response-content-type` + `response-content-disposition` 参数 |
| 创建文件夹                                    | `create_folder`                                                       | `knowledge_base_id`，`name`，可选 `folder_id`（父文件夹，省略则根目录）                             |
| 重命名文件/文件夹                            | `rename_knowledge`                                                    | `knowledge_base_id`，`media_id`，`name`（新名称）                                                  |
| 移动文件到其他知识库/文件夹                  | `move_knowledge`（不支持移动文件夹）                                  | `src_knowledge_base_id`，`dst_knowledge_base_id`，`infos:[{media_id}]`，可选 `dst_folder_id`       |
| 导出媒体到本地（获取下载链接）              | `export_media_for_ima_sandbox`                                        | `media_id`；返回 `url` + `headers`，下载时需带上 `headers`                                         |
| **打包导出为 zip（整库 / 文件夹 / 多文件）** | `export_kb_zip.cjs`                                                   | `--kb`/`--kb-name`，可选 `--folder-id`/`--media-ids`/`--out`/`--dry-run`；自动递归收集+下载+打包 |
| 创建知识库                                    | `create_knowledge_base`                                              | `name`(必填), `type`(1001/1002/1004), 可选 `description`/`cover-url`/`recommended-questions`；返回 `data.id` |
| 修改知识库基本信息                            | `update_knowledge_base_basic_info`                                   | `id`，自动推导 `update_fields`；可选 `name`/`cover-url`/`description`/`recommended-questions` |
| 置顶 / 取消置顶内容                          | `set_knowledge_top`                                                  | `knowledge_base_id`, `media_id`, `is_top`(true/false) |
| 给文件打标签                                  | `tag_add`                                                            | `knowledge_base_id`, `item_id`(=media_id), `tag_name`（不存在自动创建） |
| 从文件移除标签                                | `tag_remove`                                                         | `knowledge_base_id`, `item_id`, `tag_name`（仅解除关联，不删标签本身） |
| 列出 / 搜索标签                              | `tag_list`                                                           | `knowledge_base_id`, 可选 `keyword`/`cursor`, `limit`(默认50) |
| 重命名标签                                    | `tag_rename`                                                         | `knowledge_base_id`, `old_tag_name`, `new_tag_name`（新名存在则自动合并） |
| 删除标签                                      | `tag_delete`                                                         | `knowledge_base_id`, `tag_name`（不可逆） |
| 修改知识库权限                                | `update_knowledge_base_permission`                                   | `id`，自动推导 `update_fields`；可选 `visible-export-status`(1-3)/`join-type`(1-3) |
| 加入知识库                                    | `join_knowledge`                                                     | `knowledge_base_id`, `name` |
| 批量更新条目访问状态                          | `update_knowledge_access_status`                                     | `knowledge_base_id`, `infos:[{media_id}]`(≤10), `access_status`(1/2/3) |
| 广场发现 / 搜索公开知识库                    | `search_knowledge_base_in_square`                                    | `question`, `cursor`(首次空), `limit`(1-20) |

### `search_knowledge_base` vs `get_addable_knowledge_base_list`

| 场景                                             | 使用接口                                       | 原因                               |
| ------------------------------------------------ | ---------------------------------------------- | ---------------------------------- |
| 用户说了知识库名称（如"添加到产品文档库"）       | `search_knowledge_base`                        | 按名称搜索，找到 ID 后继续操作     |
| 用户想浏览/了解某个知识库                        | `search_knowledge_base` → `get_knowledge_base` | 先搜到 ID，再获取详情              |
| 用户想查看自己有哪些知识库（无具体关键词）       | `search_knowledge_base`（`query: ""`）         | 空 query 返回用户的所有知识库列表  |
| 用户要添加内容但**没说添加到哪个知识库**         | `get_addable_knowledge_base_list`              | 列出有权限添加的知识库，让用户选择 |
| 用户说"添加到知识库"但上下文中无法确定哪个知识库 | `get_addable_knowledge_base_list`              | 同上，不要猜测，让用户选择         |

**绝不要**在用户已明确指定知识库名称时调用 `get_addable_knowledge_base_list`。

---

> **⚠️ Windows / Linux 调用差异**：本 skill 所有 `.cjs` 脚本与 `ima_api` 调用的跨平台写法（三平台命令一致，仅 shell 包装与中文编码不同）详见下方「📌 脚本 / ima_api 调用的跨平台写法」章节。下文示例默认用 bash 写法，Windows 等价命令照该章节替换即可。

## 写入类工作流

### ⛔ 文件上传安全门（仅适用于文件上传 → `add_knowledge` 流程）

以下 4 条规则**仅**在上传文件到知识库时适用。搜索、浏览、获取信息等读取操作不受影响。

```
GATE 1 [TYPE CHECK]
  Run preflight-check.cjs FIRST. pass=false → reject immediately.
  NEVER ask "do you still want to try?" for unsupported types.
  Video files, Bilibili/YouTube URLs, file:// URLs → tell user to use IMA desktop client.

GATE 2 [NAMING]
  add_knowledge title MUST equal file_name (with extension).
  NEVER rename, shorten, translate, or modify the original filename.
  Example: file is "音频.mp3" → title="音频.mp3", file_name="音频.mp3"

GATE 3 [DUPLICATES]
  Call check_repeated_names BEFORE create_media for ALL file uploads.
  is_repeated=true → ask user: keep both (append timestamp) or cancel.
  "Replace" is NOT supported.
  Timestamp format: {name}_YYYYMMDDHHmmss.{ext}

GATE 4 [UPLOAD EXIT]
  cos-upload.cjs non-zero exit → STOP immediately.
  Do NOT call add_knowledge. Report error to user.
```

### 上传文件到知识库

完整流程：前置检查 → 重名检查 → 创建媒体 → COS 上传 → COS 验证 → 添加知识。

```bash
# ── Step 1: preflight-check.cjs ← ⛔ GATE 1 ──
# 有扩展名时自动推断；无扩展名时需传 --content-type
PREFLIGHT=$(node knowledge-base/scripts/preflight-check.cjs \
  --file "/path/to/report.pdf")
echo "$PREFLIGHT"
# pass=false → 终止，将 reason 展示给用户。NEVER ask "want to try?"

# ── Step 2: Extract fields ──
FILE_NAME=$(echo "$PREFLIGHT" | node -e "const d=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(d.file_name)")
FILE_EXT=$(echo "$PREFLIGHT" | node -e "const d=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(d.file_ext)")
FILE_SIZE=$(echo "$PREFLIGHT" | node -e "const d=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(String(d.file_size))")
MEDIA_TYPE=$(echo "$PREFLIGHT" | node -e "const d=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(String(d.media_type))")
CONTENT_TYPE=$(echo "$PREFLIGHT" | node -e "const d=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(d.content_type)")

# ── Step 3: check_repeated_names ← ⛔ GATE 3 ──
# MANDATORY for ALL file uploads (media_type 1/3/4/5/7/9/13/14/15/20/21).
# is_repeated=true → ask user: keep both (append _YYYYMMDDHHmmss) or cancel.
ima_api "openapi/wiki/v1/check_repeated_names" "{
  \"params\": [{\"name\": \"$FILE_NAME\", \"media_type\": $MEDIA_TYPE}],
  \"knowledge_base_id\": \"<kb_id>\"
}"
# folder_id is optional — omit for root, include for subfolder

# ── Step 4: create_media ──
CREATE_MEDIA_RESP=$(ima_api "openapi/wiki/v1/create_media" "{
  \"file_name\": \"$FILE_NAME\",
  \"file_size\": $FILE_SIZE,
  \"content_type\": \"$CONTENT_TYPE\",
  \"knowledge_base_id\": \"<kb_id>\",
  \"file_ext\": \"$FILE_EXT\"
}")
# Extract media_id, url, and cos_credential fields. code≠0 → terminate.
# COS_URL is the file's accessible URL — used for verification in Step 6.

# ── Step 5: cos-upload.cjs ← ⛔ GATE 5 (non-zero = STOP) ──
# ⚠️ Large files may exceed default 120s timeout — set --timeout explicitly.
node knowledge-base/scripts/cos-upload.cjs \
  --file "/path/to/report.pdf" \
  --secret-id "<cos_credential.secret_id>" \
  --secret-key "<cos_credential.secret_key>" \
  --token "<cos_credential.token>" \
  --bucket "<cos_credential.bucket_name>" \
  --region "<cos_credential.region>" \
  --cos-key "<cos_credential.cos_key>" \
  --content-type "$CONTENT_TYPE" \
  --start-time "<cos_credential.start_time>" \
  --expired-time "<cos_credential.expired_time>" \
  --timeout 300000
# ⛔ Non-zero exit → STOP HERE. Do NOT proceed to step 7.

# ── Step 6: add_knowledge ← ⛔ GATE 2 (title = file_name) ──
# ONLY execute if Step 5 succeeded (exit code 0).
# add_knowledge will verify the file was uploaded — no separate verify step needed.
ima_api "openapi/wiki/v1/add_knowledge" "{
  \"media_type\": $MEDIA_TYPE,
  \"media_id\": \"<media_id>\",
  \"title\": \"$FILE_NAME\",
  \"knowledge_base_id\": \"<kb_id>\",
  \"file_info\": {
    \"cos_key\": \"<cos_credential.cos_key>\",
    \"file_size\": $FILE_SIZE,
    \"file_name\": \"$FILE_NAME\"
  }
}"
```

### 一键快速上传（推荐）

封装脚本 `knowledge-base/scripts/upload_to_kb.cjs` 把「前置检查 → 重名检查 → create_media → cos-upload → add_knowledge」五步合成一条命令，自动处理重名、JSON 解析与临时文件拼接——无需手工跑多步、也无需手动提取字段。目标知识库由 `--kb` / `--kb-name` 显式指定（脚本不替用户选库）。

```bash
# 必须显式指定目标知识库（脚本不自动选择，避免误传）
#   --kb <knowledge_base_id>     按 id 指定
#   --kb-name <知识库名称>        按名称匹配
node knowledge-base/scripts/upload_to_kb.cjs --file /path/to/file.pdf --kb <knowledge_base_id>

# 指定知识库（id）
node knowledge-base/scripts/upload_to_kb.cjs --file a.pdf --kb <knowledge_base_id>

# 按名称匹配知识库（search_knowledge_base 取首个匹配）
node knowledge-base/scripts/upload_to_kb.cjs --file a.pdf --kb-name "我的知识库"

# 上传到指定文件夹
node knowledge-base/scripts/upload_to_kb.cjs --file a.pdf --folder <folder_id>

# 重名行为（GATE 3）
#   默认：保留两者，文件名自动追加 _YYYYMMDDHHmmss
#   --cancel-if-dup：检测到重名时直接取消上传
node knowledge-base/scripts/upload_to_kb.cjs --file a.pdf --cancel-if-dup
```

脚本内部复用本 skill 的 `ima_api.cjs`（统一鉴权）、`preflight-check.cjs`（类型检查）、`cos-upload.cjs`（COS 上传），不重复实现底层逻辑；双重 code 检查（进程退出码 + 业务 `code`）均已覆盖，任意一步失败立即终止并给出可读错误。**目标知识库必须显式通过 `--kb` 或 `--kb-name` 传入**——两者都未提供时脚本直接报错退出，绝不替用户猜测或自动挑选（无论库多库少）。

#### 批量上传时的重复处理

可一次性检查所有文件名（最多 2000 个）：

```bash
# ⛔ GATE 3 — batch check
ima_api "openapi/wiki/v1/check_repeated_names" '{
  "params": [
    {"name": "report.pdf", "media_type": 1},
    {"name": "slides.pptx", "media_type": 4},
    {"name": "data.xlsx", "media_type": 5}
  ],
  "knowledge_base_id": "<kb_id>",
  "folder_id": "<folder_id>"
}'
# 根目录时省略 folder_id。
# is_repeated=true → "以下文件已存在同名：report.pdf。是否保留两者？（不支持替换）"
# 保留两者 → append _YYYYMMDDHHmmss；取消 → remove from upload list
```

### 添加网页/微信文章到知识库

```bash
# 无需 GATE 3-5（非文件上传）
# 添加到根目录（不传 folder_id）
ima_api "openapi/wiki/v1/import_urls" '{
  "knowledge_base_id": "<kb_id>",
  "urls": [
    "https://example.com/article",
    "https://mp.weixin.qq.com/s/xxxxx"
  ]
}'

# 添加到指定文件夹
ima_api "openapi/wiki/v1/import_urls" '{
  "knowledge_base_id": "<kb_id>",
  "folder_id": "<folder_id>",
  "urls": ["https://example.com/article"]
}'
# 返回 results 映射：{ "<url>": { url, ret_code, media_id } }
```

### 添加笔记到知识库

```bash
ima_api "openapi/wiki/v1/add_knowledge" '{
  "media_type": 11,
  "note_info": { "content_id": "<note_id>" },
  "title": "笔记标题",
  "knowledge_base_id": "<kb_id>"
}'
```

### 添加 URL 到知识库（自动检测文件型 URL）

URL 可能指向网页或可下载文件。检测逻辑 → see `references/api.md §URL Type Detection`。

**文件型 URL 处理流程**：

```bash
# 1. 探测 URL 类型
CONTENT_TYPE=$(curl -sI -L "<url>" | grep -i "^content-type:" | tail -1 | awk '{print $2}' | tr -d '\r')

# 2. 下载到临时目录
TEMP_DIR=$(mktemp -d)
curl -sL -o "$TEMP_DIR/paper.pdf" "<url>"

# 3. preflight-check.cjs ← ⛔ GATE 1
PREFLIGHT=$(node knowledge-base/scripts/preflight-check.cjs \
  --file "$TEMP_DIR/paper.pdf" --content-type "$CONTENT_TYPE")
# pass=false → terminate

# 4. Follow "上传文件到知识库" workflow (Steps 3-7 with all gates)

# 5. Clean up
rm -rf "$TEMP_DIR"
```

**文件名推断**（优先级）：Content-Disposition header → URL path → last URL segment + Content-Type extension

---

---

## 文件夹操作

知识库内容以文件夹层级组织。`folder_id` 始终以 `folder_` 前缀开头。

**核心规则**：

- 操作根目录时 **省略 `folder_id` 字段**，不要传该参数
- **不要将 `knowledge_base_id` 作为 `folder_id` 传入**
- `get_knowledge_list` 返回的 `current_path`（`FolderInfo[]`）= 面包屑

### 定位文件夹（用户只给了名称）

```bash
# 方法 1：搜索（推荐）
ima_api "openapi/wiki/v1/search_knowledge" '{
  "query": "文件夹名称",
  "knowledge_base_id": "<kb_id>",
  "cursor": ""
}'
# 从 info_list 找匹配文件夹，取 media_id 作为 folder_id

# 方法 2：逐级浏览
ima_api "openapi/wiki/v1/get_knowledge_list" '{
  "knowledge_base_id": "<kb_id>",
  "cursor": "",
  "limit": 50
}'
```

---

## 知识库管理（建文件夹 / 重命名 / 移动 / 导出）

封装脚本见 `knowledge-base/scripts/`，与一键上传脚本同源，统一复用 `ima_api.cjs` 鉴权；
目标知识库一律通过 `--kb` / `--kb-name` 显式指定（脚本不替用户选库）。

### 📌 调用指令速查（Linux / Windows PowerShell / Windows cmd）


> 文件位置目录**硬编码为相对路径** `knowledge-base/scripts/`（相对 skill 根目录），不要改成抽象变量。`ima_api.cjs` 位于 skill 根目录。三平台命令**本身完全一致**，差异只在 shell 包装与中文编码。
>
> **`SKILL_DIR` 取值**（仅 PowerShell / cmd 包装需要）：skill 根目录绝对路径。Linux 用 `export SKILL_DIR=<绝对路径>`；PowerShell 用 `$env:SKILL_DIR="<绝对路径>"`；cmd 用 `SET SKILL_DIR=<绝对路径>`。Windows 下 `\` 与 `/` 均可作路径分隔符（Node 均接受）。

| 调用方式 | Linux（bash / zsh） | Windows PowerShell | Windows cmd |
| --- | --- | --- | --- |
| **直接调脚本**（如建文件夹） | `node knowledge-base/scripts/create_folder.cjs --kb <kb_id> --name "新文件夹"` | 同 Linux：`node knowledge-base/scripts/create_folder.cjs --kb <kb_id> --name "新文件夹"` | 先 `chcp 65001 >nul`，再同 Linux |
| **`ima_api` 包装**（直接打接口） | `node ima_api.cjs "openapi/wiki/v1/<endpoint>" '<json>'` | `& node "$env:SKILL_DIR/ima_api.cjs" 'openapi/wiki/v1/<endpoint>' '<json>'` | `node "%SKILL_DIR%\ima_api.cjs" "openapi/wiki/v1/<endpoint>" "<json>"` |

- **Windows cmd**：每条命令前先 `chcp 65001 >nul` 防中文参数乱码；若 `node` 不在 PATH，用完整路径（如 `"C:\Program Files\nodejs\node.exe"`）。
- **Windows PowerShell 5.1**：请求 Body 会被静默转 GBK，必须用 UTF-8 字节数组模式（见根 SKILL.md「PowerShell 5.1 Environment Detection」）；PowerShell 7+ 默认 UTF-8 无需额外处理。
- **Linux / macOS**：默认 UTF-8，直接跑即可。

### 创建文件夹 — create_folder.cjs

```bash
# 在根目录建文件夹（必须指定知识库）
node knowledge-base/scripts/create_folder.cjs --kb <knowledge_base_id> --name "新文件夹"

# 按名称匹配知识库
node knowledge-base/scripts/create_folder.cjs --kb-name "我的知识库" --name "新文件夹"

# 在指定父文件夹下建子文件夹
node knowledge-base/scripts/create_folder.cjs --kb <knowledge_base_id> --name "子文件夹" --folder <parent_folder_id>
```

返回 `data.media_id`，即新文件夹的 `folder_id`。

> **⚠️ 实测坑（2026-07-22）**：`create_folder` 的字段名是 `name`（新文件夹名），**不是** `folder_name`。首次手敲成 `folder_name` 时后端返回 `code=51`（参数非法）。凡建文件夹一律用 `--name` / 请求体 `name`，本决策表与下方脚本示例均以此为准。

### 重命名文件/文件夹 — rename_knowledge.cjs

```bash
node knowledge-base/scripts/rename_knowledge.cjs --kb <knowledge_base_id> --media-id <media_id> --name "新名称"
node knowledge-base/scripts/rename_knowledge.cjs --kb-name "我的知识库" --media-id <media_id> --name "新名称"
```

### 移动文件 — move_knowledge.cjs

```bash
# 移动到另一个知识库（可指定目标文件夹）
node knowledge-base/scripts/move_knowledge.cjs \
  --src-kb <src_kb_id> --dst-kb <dst_kb_id> \
  --media-id <media_id> [--dst-folder <dst_folder_id>]

# 按名称匹配源/目标知识库；多个文件用逗号分隔
node knowledge-base/scripts/move_knowledge.cjs \
  --src-kb-name "源库" --dst-kb-name "目标库" \
  --media-id id1,id2,id3
```

⚠️ **只支持移动文件，不支持移动文件夹**。`infos` 最多 10 个。返回 `data.move_results` 逐文件结果。

### 导出媒体 — export_media.cjs

```bash
# 获取下载链接（含所需 header）
node knowledge-base/scripts/export_media.cjs --media-id <media_id>

# 直接下载到本地
node knowledge-base/scripts/export_media.cjs --media-id <media_id> --download --out /path/to/save.pdf
```

返回 `data.media_type` 与 `data.media_content_url_info.{url, headers}`；`--download` 时按 `headers` 请求并落盘。

> **⚠️ 实测坑（2026-07-21）**：`export_media.cjs` 脚本逻辑正确，但后端接口 `export_media_for_ima_sandbox` 实测返回 `code=220030 无权限访问该接口`——当前 API key 未开通该导出接口权限，**非脚本缺陷**。若遇此报错，引导用户到 IMA 客户端导出，或确认 API key 是否已申请该接口权限。

> **删除限制**：IMA OpenAPI **不支持任何实体删除**（文件 / 文件夹 / 知识库均不可删），需到 IMA 客户端手动操作。

## 知识库扩展管理（创建 / 改名 / 置顶 / 标签 / 权限 / 广场发现）

> 以下封装脚本统一复用 `ima_api.cjs` 鉴权；目标知识库一律通过 `--kb` / `--kb-name` 显式指定（脚本不替用户选库）。
> ⚠️ **普通成员写操作（建库 / 改名 / 置顶 / 标签 / 权限）会返回 220030 无权限**，需先确认用户角色为创建者 / 协作成员 / 管理员。
> ⚠️ **不可逆操作**：`tag_delete` / `tag_rename` 调用前必须向用户显式确认（`tag_rename` 新名已存在时会自动合并两组标签）。

### 创建知识库 — create_knowledge_base.cjs

```bash
# type: 1001=个人, 1002=共享, 1004=订阅（发布到广场）
node knowledge-base/scripts/create_knowledge_base.cjs --name "我的知识库" --type 1001
node knowledge-base/scripts/create_knowledge_base.cjs --name "团队库" --type 1002 --description "资料汇总" --recommended-questions "有哪些文档?,怎么用?"
```

返回 `data.id`（新建知识库的 kb_id）。

### 修改知识库基本信息 — update_knowledge_base_basic_info.cjs

```bash
node knowledge-base/scripts/update_knowledge_base_basic_info.cjs --kb <kb_id> --name "新名称"
node knowledge-base/scripts/update_knowledge_base_basic_info.cjs --kb-name "我的知识库" --description "新简介" --recommended-questions "问题1,问题2"
```

按提供的字段自动推导 `update_fields`（1-名称 2-封面 3-简介 4-推荐问题）；至少提供一个待更新字段。

### 置顶 / 取消置顶内容 — set_knowledge_top.cjs

```bash
node knowledge-base/scripts/set_knowledge_top.cjs --kb <kb_id> --media-id <media_id> --is-top true
node knowledge-base/scripts/set_knowledge_top.cjs --kb-name "我的知识库" --media-id <media_id> --is-top false
```

`is_top` 取 `true` / `false`。

> **⚠️ 实测坑（2026-07-22）**：`set_knowledge_top` 的 `is_top` 是**布尔值**（脚本已正确处理）。**仅支持文件夹层级**——对文件夹（`folder_...`，media_type=99）置顶（`--is-top true`）与取消置顶（`--is-top false`）均实测成功；对**单个文件**（如 txt，media_type=13）置顶返回 `code=220001 invalid media_id`，API 不支持对单个文件置顶。注意 `--media-id` 必须传真实 id，若为空脚本会将其误判为布尔，导致请求体 `media_id` 变布尔、后端报 `code=1 cannot unmarshal bool into Go value of type string`。

### 标签管理

```bash
# 打标签（标签不存在时自动创建；文件夹 media_type=99 不支持打标签）
node knowledge-base/scripts/tag_add.cjs --kb <kb_id> --media-id <media_id> --tag-name "重要"

# 移除标签（仅解除文件↔标签关联，不删标签本身）
node knowledge-base/scripts/tag_remove.cjs --kb <kb_id> --media-id <media_id> --tag-name "重要"

# 列出 / 搜索标签
node knowledge-base/scripts/tag_list.cjs --kb <kb_id> --keyword "重要" --limit 50

# 重命名标签（新名已存在会自动合并，调用前确认）
node knowledge-base/scripts/tag_rename.cjs --kb <kb_id> --old-tag-name "旧名" --new-tag-name "新名"

# 删除标签（不可逆，调用前确认）
node knowledge-base/scripts/tag_delete.cjs --kb <kb_id> --tag-name "待删标签"
```

### 权限管理

```bash
# 修改导出状态：1=不可查看不可导出 2=可查看不可导出 3=可查看可导出
node knowledge-base/scripts/update_knowledge_base_permission.cjs --kb <kb_id> --visible-export-status 3

# 修改加入类型：1=直接加入 2=管理员批准 3=付费加入
node knowledge-base/scripts/update_knowledge_base_permission.cjs --kb-name "我的知识库" --join-type 1

# 批量更新条目访问状态（infos 最多 10 个，逗号分隔）
node knowledge-base/scripts/update_knowledge_access_status.cjs --kb <kb_id> --media-id id1,id2,id3 --access-status 3
```

权限接口按提供的字段自动推导 `update_fields`（1-导出状态 2-加入类型）。

> **⚠️ 实测坑（2026-07-21）**：`update_knowledge_base_permission` 改权限有**真实副作用**（影响该库所有成员）。本轮实测在临时库「ima.plus-skill 接口测试临时库」验证，避免改动正式库真实权限。**正式库改权限前务必向用户确认**，否则可能影响协作成员访问。

### 加入知识库与广场发现

```bash
# 在广场搜索公开知识库（用于定位 kb_id）
node knowledge-base/scripts/search_knowledge_base_in_square.cjs --question "Python 教程" --limit 20

# 加入知识库（需同时传 kb_id 与名称）
node knowledge-base/scripts/join_knowledge.cjs --kb <knowledge_base_id> --name "知识库名称"
```

> **⚠️ 实测坑（2026-07-21）**：`join_knowledge` 会**真实加入**该公开库（有副作用）。本轮实测真实加入了「Python入门教程」，需用户到 IMA 客户端手动退出。调用前务必确认用户确实要加入。

`search_knowledge_base_in_square` 无 `is_end` 字段，以返回 `next_cursor` 为空为终止。

> **⚠️ 实测坑（2026-07-22）**：广场发现的参数是 `question`（且必填非空），**不是** `query`。首次误用 `query` 时后端返回 `code=51`。脚本 `--question` 已封装正确字段，直接传 `--question "关键词"` 即可。

---

## 查询类工作流（无安全门限制）

### 获取知识库信息

```bash
ima_api "openapi/wiki/v1/get_knowledge_base" '{"ids": ["<kb_id>"]}'
```

### 浏览知识库内容

```bash
# 根目录
ima_api "openapi/wiki/v1/get_knowledge_list" '{"knowledge_base_id": "<kb_id>", "cursor": "", "limit": 20}'

# 指定文件夹
ima_api "openapi/wiki/v1/get_knowledge_list" '{"knowledge_base_id": "<kb_id>", "folder_id": "<folder_id>", "cursor": "", "limit": 20}'
# 翻页：用 next_cursor，is_end=true 时停止
```

### 搜索知识库内容 / 搜索知识库列表

```bash
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "关键词", "knowledge_base_id": "<kb_id>", "cursor": ""}'

# 搜索知识库列表（按名称）
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "关键词", "cursor": "", "limit": 20}'

# 查看所有知识库
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```

### 获取可添加的知识库列表

**仅当用户未指定目标知识库时使用**。

```bash
ima_api "openapi/wiki/v1/get_addable_knowledge_base_list" '{"cursor": "", "limit": 20}'
```

### 获取媒体原文内容

```bash
RESPONSE=$(ima_api "openapi/wiki/v1/get_media_info" '{"media_id": "<media_id>"}')
```

**处理分支**：

| 条件                                                    | 处理                                                              |
| ------------------------------------------------------- | ----------------------------------------------------------------- |
| `media_type=11` 且 `notebook_ext_info.notebook_id` 存在 | 将 `notebook_id` 作为 `note_id` 调用 notes 模块 `get_doc_content` |
| `url_info.url` 非空                                     | 用 `url` + `headers`（如有）请求原文                              |
| `url_info` 为空，或请求失败，或 `code≠0`                | 提示用户「请使用ima客户端查看原文」                               |

**强制下载并指定文件名**：当需要将 `url_info.url` 返回的链接作为下载链接（而非在线预览）时，可在 URL 后追加以下查询参数：

```
response-content-type=application/octet-stream&response-content-disposition=attachment;filename="<desired_filename>"
```

示例：用户要求"导出"或"下载"某个知识库文件时，将 `get_media_info` 返回的 `url` 拼接上述参数，即可让浏览器/客户端以指定文件名下载，而非在线打开。

### 获取知识库全部文件目录 — list_all_files.cjs

递归遍历整个知识库（含任意层级子文件夹），输出**全部文件的目录树**（路径、media_id、media_type），用于「打包导出」「全量盘点」「批量处理」等需要先拿到完整文件清单的场景。

```bash
# 按 kb_id 列举
node knowledge-base/scripts/list_all_files.cjs --kb <kb_id>

# 按知识库名称列举（内部走 search_knowledge_base 解析）
node knowledge-base/scripts/list_all_files.cjs --kb-name "谈水君的知识库"

# 输出 JSON（便于下游脚本解析 / 批量下载打包）
node knowledge-base/scripts/list_all_files.cjs --kb <kb_id> --json

# 同时获取每个文件的下载链接（额外逐个调 get_media_info，较慢；订阅库会标 url_error）
node knowledge-base/scripts/list_all_files.cjs --kb <kb_id> --with-url
```

- 目标知识库必须显式指定（`--kb` 或 `--kb-name` 二选一必填），脚本**绝不自动选库**（避免误列/误导出错误库）。
- 递归规则：文件夹条目 `media_type=99`，其 `media_id` 即 `folder_id`，直接作为子目录继续遍历；`media_type≠99` 记为文件。
- 默认输出树形文本（含类型标签）；`--json` 输出结构化数组 `[{type,title,media_id,media_type,path,url?}]`。
- 限深 20 层、单目录上限 50 页（2500 条）保护，防止超大知识库（如万级条目）无限遍历。
- ⚠️ 订阅库（普通成员）只能列出文件清单；`--with-url` 拿到的 url 多为空 / `220030`（权限墙），仅个人库（创建者）能真正下载。

> 完整批量导出/打包经验（权限边界、同名防覆盖、并发限制）见 `references/troubleshooting.md`「六、批量导出打包 SOP」。

---

## 分页

所有列表/搜索接口使用**游标分页**：首次 `cursor: ""`，检查 `is_end`，用 `next_cursor` 翻页，`is_end=true` 停止。

## 响应处理

统一结构 `{ "code": 0, "msg": "...", "data": { ... } }`。`code=0` 成功；`code≠0` 直接展示 `msg` 给用户。

## 用户体验

- **隐藏内部 ID**：面向用户展示中**永远不要暴露** `knowledge_base_id`、`media_id`、`folder_id`。使用知识库名称、文件标题、文件夹名称。
- **精简进度**：不要逐步暴露内部操作（"正在创建媒体…正在上传 COS…"）。只报告：
  - 上传文件：`"正在上传 report.pdf…"` → `"已添加到知识库「产品文档库」✓"`
  - 添加网页：`"正在添加…"` → `"已添加到「产品文档库」✓"`
  - 失败时展示 `msg`
- **批量操作**：汇总结果，如 `"3 个文件已添加到「产品文档库」，1 个失败（data.xlsx: 文件大小超限）"`
- **格式化展示**：

  **知识库列表**（`search_knowledge_base` / `get_addable_knowledge_base_list`）：

  > 搜索知识库后，用返回的 ID 列表调用 `get_knowledge_base` 获取描述信息，一并展示。

  ```
  📚 搜索结果（共 3 个知识库）：
  1. **产品文档库** — 存放产品相关的所有文档资料
  2. **技术方案库** — 各项目技术方案汇总
  3. **竞品分析库**
  ```

  **知识库内容列表**（`get_knowledge_list`）：

  ```
  📂 知识库「产品文档库」内容：
  📁 设计文档/          (3 个文件, 1 个子文件夹)
  📁 会议纪要/          (12 个文件)
  📄 产品需求文档.pdf
  📄 技术方案.docx
  📄 数据分析.xlsx
  --- 第 1 页，还有更多内容 ---
  ```

  **搜索结果**（`search_knowledge`）：

  ```
  🔍 在知识库「产品文档库」中搜索「排期」的结果：

  1. 📄 Q1排期表.xlsx (文件夹: 项目管理/)
     > ...包含**排期**计划的详细信息...
  2. 📄 开发排期讨论.pdf (文件夹: 会议纪要/)
  3. 📁 排期模板/ (文件夹: 根目录)
  ```

  **知识库详情**（`get_knowledge_base`）：

  ```
  📚 产品文档库
  📝 描述：存放产品相关的所有文档资料
  💡 推荐问题：
     - 最新的产品需求是什么？
     - 技术方案有哪些？
  ```

## 注意事项

- `get_knowledge_base` 接受 1-20 个 ID；单个 ID 也需包装为数组
- **文件夹是知识条目的一种**：返回结果中同时包含文件和文件夹
- 文件扩展名必须正确提取，用于 `media_type` 检测和 `file_ext` 字段（无点号，如 `pdf`）
- COS 上传时 `--content-type` 应传入文件的实际 MIME 类型，非 `application/octet-stream`
- 当用户提供 URL 添加到知识库时，必须先检测是否文件型 URL → see `references/api.md §URL Type Detection`
- MediaType 枚举和文件大小限制 → see `references/api.md §MediaType` and `§文件大小限制`

> 遇到错误码（220030 / 51 / 210039 / 220001 等）或异常现象，先读 `references/troubleshooting.md` 对照定位（含权限边界、批量导出 SOP、已知坑）。

## 打包导出为 zip（整库 / 文件夹 / 多文件）

将知识库内容导出并打包成 zip 发给用户。复用 `export_media_for_ima_sandbox` 逐个拿下载链接，按原目录结构落盘后整体压缩（脚本：`knowledge-base/scripts/export_kb_zip.cjs`）。

### 何时用

- 用户说「把 XX 知识库打包 / 导出成 zip」「把这个文件夹打包」「打包这几个文件」
- 范围是**整个知识库**、**某个文件夹（递归子内容）**、或**指定的多个文件**三选一

### 凭证说明（重要）

导出接口 `export_media_for_ima_sandbox` 需要 **API key 开通导出权限**才能用。能否成功，完全取决于当前所用 key：

- 本脚本**优先使用环境变量 `IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY`**（当前会话注入的这套通常已开通导出），其次才回退 `config.json` / `~/.config/ima`。
- 若所用 key 未开通，接口返回 `code=220030 无权限访问该接口`——这是 **key 权限问题，不是脚本缺陷**，引导用户到 IMA 客户端导出，或换用已开通导出权限的 key。
- 注：`config.json` 里那套 key 常是未开通导出的旧 key（实测会 220030）；用环境变量那套通常能直接导出。

### 命令

```bash
# ① 整个知识库
node knowledge-base/scripts/export_kb_zip.cjs --kb-name "我的知识库"
# 或已知 kb_id
node knowledge-base/scripts/export_kb_zip.cjs --kb <kb_id>

# ② 指定文件夹（递归子内容）—— 先用 list_all_files.cjs 拿到 folder_id
node knowledge-base/scripts/export_kb_zip.cjs --kb <kb_id> --folder-id folder_xxxx

# ③ 指定多个文件（media_id，逗号分隔；跨文件夹也会保留各自原路径）
node knowledge-base/scripts/export_kb_zip.cjs --kb <kb_id> --media-ids id1,id2,id3

# 常用选项
#   --dry-run      只列出将导出的文件，不下载（先确认范围，再实跑）
#   --out <path>   zip 输出路径（默认 outputs/知识库导出_<时间戳>.zip）
#   --keep         打包后保留临时下载目录（默认清理）
```

### 行为

- 递归收集文件清单，按知识库**原始目录结构**落盘（保留文件夹层级）
- **同名文件自动加序号**（`_1` / `_2` …）避免互相覆盖
- 逐个导出下载；失败的如实报告，不影响其余文件；**全部失败则不生成 zip**
- 中文 / 空格 / 括号等文件名以 UTF-8 写入 zip

### 后续发送

脚本输出 `zip 路径: <path>` 后，用 `provide_file` 工具把该 zip 发给用户（链接约 72 小时有效）。

### 边界

- **网页 / 公众号 / 网页视频类（media_type 2/6/16/20）** 常无可用下载链接，会 FAIL（如实报告即可）
- **订阅知识库（普通成员角色）** 通常无权导出，可能整体 220030
- 超大文件（如百 MB 音频）会真实下载，耗时随体积增加，属正常

