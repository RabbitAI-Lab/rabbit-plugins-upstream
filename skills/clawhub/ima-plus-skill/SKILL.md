---
name: ima.plus-skill
description: IMA.plus 技能（V1.0.3）——笔记管理与知识库操作。支持上传/导出文件、打包导出知识库为 zip、创建文件夹、移动/重命名/置顶知识条目、创建与修改知识库、标签管理、权限管理、广场发现、添加网页到知识库、搜索/浏览/创建/编辑笔记。
allowed-tools: Bash,Read
metadata:
  openclaw:
    emoji: "🔧"
    requires:
      bins:
        - node
      env:
        - IMA_OPENAPI_CLIENTID
        - IMA_OPENAPI_APIKEY
      primaryEnv: IMA_OPENAPI_CLIENTID
  security:
    credentials_usage: |
      This skill requires user-provisioned IMA OpenAPI credentials (Client ID and API Key)
      to authenticate with the official IMA API at https://ima.qq.com.
      Credentials are ONLY sent to the official IMA API endpoint (ima.qq.com) as HTTP headers.
      The file-upload flow also sends requests to COS endpoints (*.myqcloud.com) using
      short-lived, scoped temporary credentials returned by the IMA API (create_media);
      the user's Client ID / API Key are never sent to COS.
      No credentials are logged, stored in files, or transmitted to any other destination.
    allowed_domains:
      - ima.qq.com
      - '*.myqcloud.com'
---
# ima.plus-skill

> **版本：V1.0.3**
>
> **运行环境**：Node.js ≥ 18.0.0（所有 .cjs 脚本 + inline JSON 解析依赖）

Unified IMA OpenAPI skill. Currently supports: **notes**, **knowledge-base**.

## ⛔ MANDATORY RULES — read before ANY operation

1. **UTF-8 encoding (notes writes only):** Before calling `import_doc` or `append_doc`, ALL string fields (`content`, `title`) MUST be validated as legal UTF-8. Non-UTF-8 content causes irreversible garbled text. See [Detailed Rules](#detailed-utf-8-encoding-rules) for platform-specific methods.
2. **File upload naming:** `title` MUST equal `file_name` (with extension). Never rename, shorten, translate, or modify the original filename.
3. **Unsupported file types:** Reject immediately with a clear message. Do NOT ask user "do you still want to try?" Video files, Bilibili/YouTube URLs, and `file://` URLs are not supported — tell user to use IMA desktop client.
4. **File upload integrity:** Keep file content as-is during upload. No encoding conversion for binary files (PDF, images, Excel, etc.).
5. **PowerShell 5.1 (all modules):** If running in PowerShell, detect version before first API call. PS 5.1 silently converts request Body to GBK — must use UTF-8 byte array mode. See [Detailed Rules](#powershell-51-environment-detection).

## 模块决策表

| 用户意图                                                                                   | 模块           | 读取                      |
| ------------------------------------------------------------------------------------------ | -------------- | ------------------------- |
| 搜索笔记、浏览笔记本、获取笔记内容、创建笔记、追加内容                                     | notes          | `notes/SKILL.md`          |
| 上传文件、添加网页链接、搜索知识库、浏览知识库内容、获取知识库信息、获取可添加的知识库列表 | knowledge-base | `knowledge-base/SKILL.md` |
| 查看原文、分析原文、导出原文（需要 media_id）                                              | knowledge-base | `knowledge-base/SKILL.md` |
| 打包知识库 / 某个文件夹 / 多个文件为 zip 并发给用户                                         | knowledge-base | `knowledge-base/SKILL.md` |

### ⚠️ 易混淆场景

| 用户说的                                                 | 实际意图                 | 正确路由                                                    |
| -------------------------------------------------------- | ------------------------ | ----------------------------------------------------------- |
| "把这段内容添加到知识库XX里的笔记YY"                     | 往已有**笔记**追加内容   | **notes** — 先搜索笔记获取 `note_id`，再用 `append_doc`     |
| "把这个写到XX笔记里"、"记到XX笔记"                       | 往已有**笔记**追加内容   | **notes** — `append_doc`                                    |
| "把这篇笔记添加到知识库"                                 | 将笔记关联到**知识库**   | **knowledge-base** — `add_knowledge` with `media_type=11`   |
| "上传文件到知识库"                                       | 上传**文件**到知识库     | **knowledge-base** — `create_media` → COS → `add_knowledge` |
| "新建一篇笔记记录这些内容"                               | **创建**新笔记           | **notes** — `import_doc`                                    |
| "帮我记一下"、"记录一下"、"保存为笔记"（未指定已有笔记） | 意图不明确，**需要确认** | **notes** — 先询问用户是创建新笔记还是追加到哪篇已有笔记    |
| "添加到笔记里"（未指定具体哪篇）                         | 意图不明确，**需要确认** | **notes** — 先询问用户是创建新笔记还是追加到哪篇已有笔记    |

### ⚠️ 跨模块任务 — 必须读取两个子模块

某些意图跨越 notes 和 knowledge-base 两个模块。**不要只读取一个子模块就开始执行**，必须先读取两个模块的 SKILL.md 再按顺序操作。

| 用户说的                             | 实际流程                                      | 读取顺序                                               |
| ------------------------------------ | --------------------------------------------- | ------------------------------------------------------ |
| "把知识库里的XX内容记到笔记"         | KB 搜索/读取 → Notes 创建/追加                | 先读 `knowledge-base/SKILL.md` → 再读 `notes/SKILL.md` |
| "查看原文"（知识库中的笔记类型媒体） | KB `get_media_info` → Notes `get_doc_content` | 先读 `knowledge-base/SKILL.md` → 再读 `notes/SKILL.md` |
| "把这篇笔记添加到知识库"             | Notes 搜索获取 note_id → KB `add_knowledge`   | 先读 `notes/SKILL.md` → 再读 `knowledge-base/SKILL.md` |

**规则**：如果用户意图同时涉及「笔记」和「知识库」，或者 API 响应揭示需要另一个模块（如 `media_type=11` 表示笔记类型），必须读取两个子模块再继续。

**核心判断规则**：

- 目标是**笔记的内容**（读、写、追加）→ notes 模块
- 目标是**知识库的条目**（上传文件、添加链接、关联笔记到知识库）→ knowledge-base 模块
- 目标是**获取知识库条目的原始内容**（查看原文、分析原文、导出原文）→ knowledge-base 模块（若原文是笔记，会跨模块到 notes `get_doc_content`）
- 用户提到"知识库"只是在**描述笔记的位置**（如"知识库里的那篇笔记"），真正操作对象仍是笔记 → notes 模块

## 📌 全量试错经验与避坑指南（V1.0.1，全功能实测沉淀）

> 以下每一条都来自真实接口实测（知识库 + 笔记共 30+ 接口全验证通过）。任何 AI 调用本 skill 前务必通读，遇到对应错误码可直接对照定位。**标注 `code=xxx` 的为后端业务错误（stdout JSON 的 `code` 字段）；`退出码` 为脚本进程退出码。**

### 一、知识库接口试错

| 接口 / 场景 | 试错现象 | 正确做法 |
| --- | --- | --- |
| `create_folder` | 手敲 `folder_name` → `code=51` 参数非法 | 字段名是 **`name`**（`--name` / 请求体 `name`） |
| `search_knowledge_base_in_square`（广场发现） | 误用 `query` → `code=51` | 参数是 **`question`**（且必填非空），脚本用 `--question` |
| `set_knowledge_top`（置顶 / 取消置顶） | ① 对单个**文件**置顶 → `code=220001 invalid media_id`；② `--media-id` 为空时脚本把它误判成布尔 → 请求体 `media_id` 变布尔 → `code=1 cannot unmarshal bool` | ① **仅支持文件夹层级**（`folder_...`，media_type=99），不支持单个文件；② `is_top` 是**布尔值**；③ `--media-id` 必须传真实 id |
| `export_media` / `export_media_for_ima_sandbox` | 返回 `code=220030 无权限访问该接口` | **key 权限问题，非脚本缺陷**：导出接口需 API key 开通导出权限。脚本优先用环境变量 `IMA_OPENAPI_*` 那套（当前会话注入的通常已开通，可直接导出）；`config.json` 里的旧 key 未开通才会 220030。遇 220030 引导用户到 IMA 客户端导出，或换用已开通的 key。批量打包见 `knowledge-base/scripts/export_kb_zip.cjs` |
| `update_knowledge_base_permission` | 有**真实副作用**（影响该库所有成员） | 正式库改权限前**必须向用户确认** |
| `join_knowledge` | 会**真实加入**公开库（副作用） | 调用前确认用户确实要加入；加入后需用户到 IMA 客户端退出 |
| `get_media_info` 读取原文 | 订阅知识库（普通成员）返回 `code=220030 没有权限` | 仅**个人库（创建者）**能读文件/笔记原文；订阅库只能看列表，引导用户去客户端 |
| `get_knowledge_list` 的 `folder_id` | 把 `knowledge_base_id` 当 `folder_id` 传入 → 返回根目录而非目标文件夹 | 根目录**省略** `folder_id`；子目录 ID 必须 `folder_xxxx` 开头 |
| `media_type` 枚举 | 曾误以为 `media_type=11` 是微信文章（其实是**笔记**），`6` 才是微信文章 | 速记：`1=PDF` `2=网页URL` `4=PPT` `5=Excel` `6=微信文章` `11=笔记` `16=网页视频` `99=文件夹`；拿不准先搜样例 |
| `search_*` 返回空 | `info_list:[]` 不一定是真没内容 | 换关键词 / 换接口（`get_knowledge_list` 翻文件夹）；别一次空就放弃 |
| `check_repeated_names` 重名判定 | 刚上传完短时间内查同名可能 `is_repeated=false`，过会儿才 `true`（索引延迟） | 别仅凭一次查询认定无重名 |
| `create_folder` 接口选择 | 早期误用 `add_knowledge`+`media_type=99` 建文件夹失败，误判「API 不能建文件夹」 | 正确接口是 `create_folder`（实测可成功，返回 `data.media_id` 即 `folder_id`） |
| 删除类操作 | 试图删除文件/文件夹/知识库/标签 | **IMA OpenAPI 不支持任何实体删除**，测试留痕需用户到 IMA 客户端手动清理 |
| `tag_delete` | 删除标签会移除标签及其与所有文件的关联 | **不可逆**，调用前确认；`tag_rename` 新名已存在时自动合并两组标签（同样需确认） |
| 写操作角色 | 普通成员调建库/改名/置顶/标签/权限 → `code=220030` | 需角色为创建者/协作成员/管理员 |
| 批量导出 / 打包 | 订阅库不可下载；HTML(20) 个人库也 `220030`；个人库大文件（如 103MB 无后缀音频）需按 media_type 补后缀；同名文件会覆盖 | 仅个人库（创建者）可导出；并发 ≤8，单文件失败跳过不中断；订阅库引导客户端 |
| `search_knowledge_base` 返回结构 | 按 `knowledge_base_list`/`id`/`name` 解析永远匹配不到 | 返回字段是 `info_list` / `kb_id` / `kb_name`；空 `query` 返回账号**全部**知识库（含订阅） |
| 文件夹上传 | —— | 用 `--folder <folder_id>`，支持任意层级嵌套；文件夹的 `media_id` 即其 `folder_id` |

### 二、笔记接口试错

| 场景 | 试错现象 | 正确做法 |
| --- | --- | --- |
| 写入 UTF-8 编码 | PowerShell 5.1 下乱码内容写入笔记 → **永久乱码不可恢复** | 写 `import_doc`/`append_doc` 前**强制校验**所有字符串字段为合法 UTF-8（见下方「详细规则」） |
| `update_note` 编辑块 | 对 `editable=false` 的块（图片/录音/附件/链接卡片/AI 生成块）下发 EDIT/DELETE → `code=210039` | 这类块只能作为 APPEND 锚点 |
| 模糊指令 | 用户说「有什么经验吗」可能指「笔记里有没有相关经验记录」 | 先反问确认意图（搜已有笔记 vs 其他含义） |

### 三、跨模块（笔记 ↔ 知识库）

- **意图同时涉及「笔记」和「知识库」时，必须先读两个子模块 SKILL.md 再执行**（如「把知识库里的 XX 记到笔记」= KB 搜原文 → notes 写入）。
- **口诀：先取数据，再写存储**（KB 读 → notes 写；notes 搜 → KB 关联）。
- 用户说「知识库」若只是**描述笔记的位置**（如「知识库里的那篇笔记」），真正对象仍是笔记 → 走 notes 模块。

### 四、平台与环境

- **Node 18+**（依赖全局 `fetch` 与 `node:` 前缀模块）。
- **凭证优先级**：skill 目录 `config.json` > 环境变量 `IMA_OPENAPI_CLIENTID`/`IMA_OPENAPI_APIKEY` > `~/.config/ima/`。缺凭证 → 脚本退出码 `-100`。
- **双层错误检查（必须都查）**：① 脚本执行错误（进程非 0 退出，`stderr` 的 `{"code":-100|-200,"msg":...}`）；② 后端业务错误（进程正常退出，`stdout` 的 `{"code":0,...}`，`code=0` 成功，`code≠0` 直接展示 `msg`）。
- **Windows PowerShell 5.1**：`Invoke-RestMethod` 会静默把请求 Body 从 UTF-8 转系统 ANSI（中文 Windows 为 GBK）→ 必须用 UTF-8 字节数组模式（见根 SKILL.md「PowerShell 5.1 Environment Detection」）。PowerShell 7+ 默认 UTF-8。
- **Windows cmd**：每条命令前先 `chcp 65001 >nul` 防中文参数乱码；`node` 不在 PATH 时用完整路径。
- **Linux / macOS**：默认 UTF-8，直接跑。

### 五、调用与编码习惯

- **`kb_id` 是 Base64 URL 安全变体字符串**（含 `=`、`+`、`_`），shell 极易丢字符 → 写进变量并双引号包住（`"$KB_ID"`），传入前先 `echo` 核对一次；PowerShell 别用反引号包值（反引号是转义符）。
- **模糊查询指令直接调 API，别过度读 SKILL.md**：「看看有啥」→ 立刻 `search_knowledge_base(query="")`；「XX 库里有什么」→ `get_knowledge_list(knowledge_base_id=...)`。浅读即可，调用优先。
- **文件上传命名**：`title` 必须等于 `file_name`（含扩展名），绝不改名/缩写/翻译。
- **不支持的类型**（视频、Bilibili/YouTube URL、`file://` URL）直接拒绝并引导到 IMA 客户端，不要问「还要试吗」。
- **文件上传不转码**：二进制文件（PDF/图片/Excel 等）保持原字节，服务端自行处理。

---

## Credential Check

Credentials are loaded in priority order:

1. **Skill directory `config.json`** (recommended, self-contained)
2. **Environment variables** `IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY`
3. **`~/.config/ima/` files** (legacy fallback)

**If credentials are missing**, `node ima_api.cjs ...` exits with `code: -100` and outputs the error to stderr.

### Quick setup — skill directory config.json (recommended)

Create `config.json` in the skill root:

```json
{
  "clientId": "your_client_id",
  "apiKey": "your_api_key"
}
```

Get credentials from https://ima.qq.com/agent-interface

> **Security:** Credentials only sent to `ima.qq.com`. Never written to any log or external file.

## API 调用模板

> **跨平台说明**：本 skill 的全部脚本（`.cjs`）为**单一 Node.js 实现**，Windows / Linux / macOS 命令本身完全一致；差异只在 shell 包装（捕获输出、检查退出码）与中文编码处理。下面分别给出两平台的规范写法。运行需 **Node 18+**（依赖全局 `fetch` 与 `node:` 前缀模块）。

所有请求统一为 **HTTP POST + JSON Body**，仅发往官方 Base URL `https://ima.qq.com`。

`ima_api` 已抽离到脚本：`./ima_api.cjs`

```bash
# ── Linux / macOS（bash / zsh）── 跨平台通用写法之一
# SKILL_DIR = this skill's root directory
# stdout = normal response JSON; stderr = structured error {"code":-100|-200,"msg":"..."}
resp=$(node "$SKILL_DIR/ima_api.cjs" "openapi/list_docs" '{"limit":10}' 2>&1)
if [ $? -ne 0 ]; then
  # Extract error code & msg using Node (cross-platform, no jq needed)
  err_info=$(node -e "try{const e=JSON.parse(process.argv[1]);process.stdout.write(e.code+':'+e.msg)}catch(_){process.stdout.write('-100:unknown error')}" "$resp")
  err_code="${err_info%%:*}"
  err_msg="${err_info#*:}"

  if [ "$err_code" = "-200" ]; then
    echo "[update] $err_msg" >&2
  else
    echo "[error] $err_msg" >&2
  fi
  exit 1
fi

echo "$resp"
```

> **Windows 版（PowerShell 5.1 / 7+）：**
>
> ```powershell
> # 用 & 调用避免别名/函数冲突；2>&1 合并错误流到 $resp
> $resp = & node "$env:SKILL_DIR/ima_api.cjs" 'openapi/list_docs' '{"limit":10}' 2>&1
> if ($LASTEXITCODE -ne 0) {
>     $err = $resp | ConvertFrom-Json
>     if ($err.code -eq -200) { Write-Host "[update] $($err.msg)" }
>     else { Write-Host "[error] $($err.msg)" }
>     exit 1
> }
> Write-Host $resp
> ```
>
> ⚠️ **PowerShell 5.1 中文乱码必读**：PS 5.1 会静默把请求 Body 转成系统 ANSI（中文 Windows 为 GBK），导致服务端收到乱码。必须改用 UTF-8 字节数组模式发送，详见下方「PowerShell 5.1 Environment Detection」章节。PowerShell 7+ 默认 UTF-8，无需额外处理。
>
> **Windows 版（命令提示符 cmd）：**
>
> ```cmd
> chcp 65001 >nul
> node "%SKILL_DIR%\ima_api.cjs" "openapi/list_docs" "{\"limit\":10}" 2>&1
> @REM 成功：stdout 为响应 JSON；失败：进程非 0 退出，错误信息在 stderr
> @REM 用 %ERRORLEVEL% 判断退出码；中文参数需先 chcp 65001 防止乱码
> ```
>
> **cmd 提示**：`SET SKILL_DIR=...` 后，路径用 `%SKILL_DIR%` 引用；Windows 上 `\` 与 `/` 均可作路径分隔符（Node 均接受）。若 `node` 不在 PATH，用完整路径（如 `"C:\Program Files\nodejs\node.exe"`）；脚本内部已用 `process.execPath` 调用 node 子进程，通常无需手动处理。

> **错误处理有两层，必须都检查：**
>
> **第一层 — 脚本执行错误**（进程非 0 退出，错误在 **stderr**）：
>
> - `-100`：程序错误（缺少凭证、参数非法、网络错误等），`msg` 可直接展示给用户
> - `-200`：skill 需要更新，原请求未发送，stdout 中有更新上下文 JSON
>
> **第二层 — 后端业务错误**（进程正常退出，响应在 **stdout**）：
>
> - stdout 返回 JSON `{"code": 0, "msg": "...", "data": {...}}`
> - `code=0` 表示成功，从 `data` 提取业务字段
> - `code≠0` 表示后端业务错误（如参数不合法、权限不足、资源不存在等），**直接将 `msg` 展示给用户**
> - 常见后端错误码见各子模块的「错误处理」章节


## Detailed Rules Reference

> The sections below contain full platform-specific examples for the mandatory rules above. Refer to these when you need implementation details.

### Detailed UTF-8 Encoding Rules

> **此规则为强制性要求，不可跳过。** 非法编码会导致内容在 IMA 中显示为乱码，且无法修复，必须重新写入。
>
> **适用范围：notes 模块**（`import_doc`、`append_doc` 等文本写入 API）。
>
> **不适用于 knowledge-base 模块的文件上传**：上传文件时必须保持文件原始内容，不得转码。文件以二进制方式上传，服务端自行处理。

**每次调用 notes 写入类 API（`import_doc`/`append_doc`）之前，必须对 `content`、`title` 等所有字符串字段执行 UTF-8 编码校验/转换。** 无论内容来源如何——用户直接输入、从文件读取、WebFetch 抓取、剪贴板粘贴、外部 API 返回——都不能假设已经是合法 UTF-8，必须显式确认。

#### 强制检查清单（notes 模块写入前）

在构造 notes 写入请求的 body **之前**，完成以下步骤：

1. **来自文件的内容**：先检测文件编码，转为 UTF-8 后再读入变量（注意：这是指读取文件内容作为笔记正文写入，不是上传文件到知识库）
2. **来自 WebFetch / HTTP 请求的内容**：响应可能为 GBK/Latin-1 等，必须转码
3. **来自用户输入或变量拼接的内容**：清洗非法 UTF-8 字节（`\xff\xfe` 等）
4. **标题字段同理**：`title` 也必须为合法 UTF-8

#### 各环境转码方法

**Python（推荐，几乎所有环境都有）：**

```bash
# 读取文件，自动检测编码并转为 UTF-8
content=$(python3 -c "
import sys
data = open('tmpfile', 'rb').read()
for enc in ['utf-8', 'gbk', 'gb2312', 'big5', 'latin-1']:
    try:
        sys.stdout.write(data.decode(enc))
        break
    except (UnicodeDecodeError, LookupError):
        continue
" 2>/dev/null)

# 如果内容已在变量中，清洗非法 UTF-8 字节
content=$(printf '%s' "$content" | python3 -c "import sys; sys.stdout.write(sys.stdin.buffer.read().decode('utf-8','ignore'))")
```

**Node.js：**

```bash
content=$(node -e "const fs=require('fs');const buf=fs.readFileSync('tmpfile');process.stdout.write(buf.toString('utf8'))")
# 已知编码（如 GBK）：
content=$(node -e "const fs=require('fs');process.stdout.write(new TextDecoder('gbk').decode(fs.readFileSync('tmpfile')))")
```

**Unix (macOS/Linux)：**

```bash
content=$(iconv -f "$(file -b --mime-encoding tmpfile)" -t UTF-8 tmpfile 2>/dev/null || cat tmpfile)
```

**Windows PowerShell：**

```powershell
# 读取非 UTF-8 文件并转码
$content = [System.IO.File]::ReadAllText('tmpfile', [System.Text.Encoding]::Default)
[System.IO.File]::WriteAllText('tmpfile.utf8', $content, [System.Text.Encoding]::UTF8)
```

### PowerShell 5.1 Environment Detection

> **此问题影响所有 API 调用（notes、knowledge-base 等）**
>
> **此问题极其隐蔽：PowerShell 5.1 下 `Invoke-RestMethod` 会静默将请求 Body 从 UTF-8 转为系统 ANSI 编码（中文 Windows 为 GBK），即使设置了 `Content-Type: charset=utf-8` 也无效。结果是请求看起来发送成功，但服务端收到的内容已经是乱码，且无任何错误提示。**

**当 agent 运行在 PowerShell 环境时，必须在首次 API 调用前检测版本：**

```powershell
# 检测 PowerShell 版本 — 在任何 API 调用之前执行（notes 和 knowledge-base 都需要）
if ($PSVersionTable.PSVersion.Major -le 5) {
    Write-Host "⚠️ 检测到 PowerShell 5.1，将使用 UTF-8 字节数组模式发送请求"
    $useUtf8Bytes = $true
} else {
    Write-Host "✅ PowerShell 7+，默认 UTF-8，无需额外处理"
    $useUtf8Bytes = $false
}
```

**PowerShell 5.1 下必须使用以下方式发送请求**（用 `ConvertTo-Json` 构建 JSON 以避免手动拼接的转义风险，再显式转为 UTF-8 字节数组）：

```powershell
# PowerShell 5.1 安全请求模板（适用于所有模块的所有 API 调用）
$body = @{ title = "标题"; content = $content; content_format = 1 } | ConvertTo-Json -Depth 10
if ($useUtf8Bytes) {
    # CRITICAL: 必须转为字节数组，否则中文/非ASCII内容会变成乱码
    $utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($body)
    Invoke-RestMethod -Uri $url -Method Post -Body $utf8Bytes -ContentType "application/json; charset=utf-8" -Headers $headers
} else {
    # PowerShell 7+ 可直接传字符串
    Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json; charset=utf-8" -Headers $headers
}
```

> **总结：** 在 PowerShell 5.1 环境中，**所有** API 调用（无论 notes 还是 knowledge-base）都必须将 Body 显式转为 UTF-8 字节数组。不检测版本直接发请求 = 中文内容必乱码。这是 PowerShell 5.1 的已知设计缺陷，不是 bug 可以被修复。

## 实战经验教训

本节记录使用 ima 技能过程中的踩坑经验，按层级分类。每次踩坑即时更新，避免重复犯错。

### 调用层（所有模块通用）

#### 教训 1：Windows Shell 环境差异是隐形杀手
- **坑**：中文 Windows 环境 `ls`/`cat`/`grep` 不可用，`type` 输出乱码，PowerShell 变量语法与 bash 完全不同。
- **经验**：
  - 中文 Windows → 统一用 PowerShell + UTF-8（`chcp 65001` 或 `$OutputEncoding`）
  - 跨平台命令避免依赖 Unix 工具，用 Node.js 或 Python 做解析
  - 验证：任何 shell 命令执行前先确认当前环境和编码

#### 教训 2：JSON Body 嵌套引号是定时炸弹
- **坑**：PowerShell 5.1 中 `'"{\"query\":\"\"...}'` 嵌套引号转义直接把 JSON 传成空，API 返回 `code: -100 请求 body 不是合法的 JSON`。
- **经验**：
  - **永远不要手写嵌套引号**。把 JSON 写入临时文件再 `cat | node -e ...`
  - 即使用单引号包 JSON 字符串，在 PowerShell 5.1 也会出问题
  - 安全做法：`node -e "process.stdout.write(JSON.stringify({...}))"` 构建 JSON，零转义风险

#### 教训 3：敏感信息绝不能进 shell 历史
- **坑**：用户发来 Client ID + API Key，直接在命令行用 `$API_KEY=xxx` 会留在 PowerShell 的 `Get-History` 中。
- **经验**：
  - 凭证只写一次到 `config.json`（skill 目录优先级 1），绝不进命令行
  - 任何时候用 `$env:VAR` 或 `process.env` 间接引用，不直接硬编码

#### 教训 4：脚本编码可读性 > 速度
- **坑**：`type config.json` 在 PowerShell 中文 Windows 输出乱码；`Get-Content` 配 `Out-String` 才正常。
- **经验**：
  - 统一走 `node -e "process.stdout.write(...)"` 提取字段——跨平台、无乱码
  - 不要用 shell 原生命令解析 JSON（`jq` 不一定装，PowerShell `ConvertFrom-Json` 版本差异大）

#### 教训 7：任务之间不要过度复用上下文
- **坑**：用户问「看看知识库有啥」后问「有什么经验」，我把「经验」理解为「知识库里的使用经验」，翻了 134 条内容才意识到用户问的是我自己踩的坑。
- **经验**：
  - 中文指代歧义大（"经验"=教程/踩坑/复盘，都行）
  - **0.5 秒反问一句 > API 翻 10 次**。先确认意图再做操作

#### 教训 8：cursor 游标分页，第一次必须传 `""`，不是 `null` 也不是 `"0"`
- **坑**：`{"cursor": null}` 部分接口返回 `code: -100`；`{"cursor": "0"}` 被当成字符串 "0" 跳过第一页。
- **经验**：
  - **永远用 `"cursor": ""`（空串）当起点**
  - 翻页用返回的 `next_cursor`，`is_end: true` 立刻停
  - 不同接口 cursor 初始值不同：`list_notebook` 传 `"0"`，其他传 `""`，别搞混

#### 教训 9：API 返回的 code 有两层，不要只看进程退出码
- **坑**：进程退出码 = 0 但 stdout 返回 `{"code": 220030, "msg": "..."}` 时，容易误判成功。
- **经验**：
  - **第一层**：进程退出码（`$?`）→ 脚本本身是否崩
  - **第二层**：stdout JSON 的 `code` 字段 → 业务是否成功
  - **两层都得检查！** 进程退 0 但业务 `code≠0` 仍是失败

#### 教训 16：模糊指令先反问，比猜对了更高效
- **坑**：用户说「看看知识库有啥」「有什么经验」「之间有什么」「帮我记一下」——这些都有多重解释。
- **经验**：
  - 任何含歧义的词（经验/技巧/记录/保存/添加）→ **立即反问一句**
  - 0.5 秒问一句比调用 5-8 次 API 翻数据快 10 倍
  - 不要在还没确认意图时就开始调 API

#### 教训 17：内部 ID 不要暴露给用户
- **坑**：把 `kb_id`（Base64 长串）、`media_id`、`folder_id` 直接贴在回复里，用户看不懂也用不上。
- **经验**：
  - **面向用户**：只展示知识库名称、文件标题、文件夹名
  - **内部 ID**：自己调用用，不放主展示位
  - 列表展示时把 ID 映射为可读名称后再回复

#### 教训 18：长结果主动做摘要 + 给下一步
- **坑**：一次返回 50+ 条结果直接贴出来，用户要自己筛选。
- **经验**：
  - 结果 > 10 条 → **分主题归类**（教程类/案例类/视频类/模板类）
  - 结尾主动引导："想深入哪条？" 或 "需要我打开某个看详情吗？"
  - 按 `content_count` 排序是信号——内容多的知识库往往更有用

#### 教训 19："是什么" 和 "怎么用" 是两个动作
- **坑**：用户说「看看知识库有啥」，我只列元信息就停了。用户其实可能还想知道「里面有什么实用的」。
- **经验**：
  - "看看有啥" = 列表 + 推荐热点（内容数排序、描述摘要）
  - "怎么用" = 深入一层（热门笔记、子文件夹、搜索关键词）
  - **一次回答覆盖两个意图**，比"列完等你再问"更贴心

#### 教训 20：复盘比完成更重要
- **坑**：跑通任务就直接交差，踩的坑不记下次还掉。
- **经验**：
  - 每次踩坑**当场记一条教训**到本节
  - 教训要**可迁移**（不是"这次没传 folder_id"，而是"先核对 current_path 字段再操作"）
  - 真正能记住 5 条 = 熟练

#### 教训 21：知识库文件上传优先用 upload_to_kb.cjs 一键脚本
- **坑**：手工跑 preflight → 重名检查 → create_media → cos-upload → add_knowledge 五步，还要解析 JSON、拼临时文件，繁琐且易错。
- **经验**：knowledge-base 模块已封装 `knowledge-base/scripts/upload_to_kb.cjs`，一条命令搞定；支持 `--kb` / `--kb-name` / `--folder` / `--cancel-if-dup`。

#### 教训 22：search_knowledge_base 返回 info_list，不是 knowledge_base_list
- **坑**：按 `knowledge_base_list[].id/name` 解析永远拿到空，匹配不到库名。
- **经验**：该接口结构是 `data.info_list[].kb_id / kb_name`；空 query 返回全部知识库（含订阅库）。

#### 教训 23：文件夹的 media_id 即 folder_id，支持嵌套；create_folder 接口已支持建文件夹
- **坑**：早期曾用 `add_knowledge` + `media_type=99` 尝试建文件夹，返回「文件夹不存在」/「参数错误」，误判为「API 不能建文件夹」。
- **经验**：
  - 正确接口是 `create_folder.cjs`（`openapi/wiki/v1/create_folder`），**实测可成功建文件夹**（返回 `data.media_id` 即 `folder_id`）。
  - 文件夹的 `media_id`（如 `folder_xxx`）就是上传时用的 `folder_id`，任意嵌套层级同理。
  - 注意：仍不支持通过 API **移动**文件夹（`move_knowledge` 仅支持文件，不支持文件夹）。

#### 教训 24：check_repeated_names 有索引延迟，别凭一次查询判"无重名"
- **坑**：刚传完文件立即查重名返回 false，误以为库里没有。
- **经验**：重名判定异步生效，稍后才变 true；脚本默认重名时保留两者（追加 `_YYYYMMDDHHmmss`）。

#### 教训 25：知识库批量导出/打包——订阅库权限墙，get_media_info 才是正路
- **坑**：`export_media_for_ima_sandbox` 返回 `220030 无权限`；订阅库（普通成员）`get_media_info` 也 `220030`，只有个人库（创建者）能下载。
- **经验**：先用 `knowledge-base/scripts/list_all_files.cjs --json` 拿全量文件清单，再对每个文件 `get_media_info` 拿下载链接强制下载；HTML(20) 即使个人库也 `220030`。详细沉淀见 knowledge-base 模块「实战经验教训 · 教训 25」。

### 本轮实测结论与试错记录（2026-07-21 全功能实测）

> 在知识库「测试知识库1」(`kb_id=8qXpfeutePHoMWMa8sJmIUCpaKIw5GHJtmf9eeCzVEw=`) 实测 **25 项 KB 功能 + 6 项 notes 功能**，仅 `export_media` 因后端权限未开通而失败，其余全部通过。

**实测结论**

- **脚本为单一跨平台 Node.js 实现**：19 个 `.cjs` + `ima_api.cjs` 均为纯 `node:` 内置模块、LF 行尾、Node 18+，Windows / Linux / macOS **命令本身完全一致**，差异只在 shell 包装与中文编码。Windows 唯一注意点：emoji 日志（🔎⏳✅📚）在老 cmd（GBK 代码页）下乱码，但功能不受影响；`upload_to_kb.cjs` 已用 `process.execPath` 加固 Windows 兼容。
- **全功能实测通过（除 export_media）**：get_knowledge_base / get_knowledge_list / search_knowledge / search_knowledge_base / get_addable_knowledge_base_list / tag_*（list/add/remove/rename/delete）/ create_folder×2 / upload_to_kb（含 preflight + cos-upload + create_media + add_knowledge 全链路）/ import_urls / add_knowledge（关联笔记）/ rename_knowledge / set_knowledge_top / move_knowledge / get_media_info / update_knowledge_access_status / create_knowledge_base / update_knowledge_base_basic_info / update_knowledge_base_permission / join_knowledge / search_knowledge_base_in_square；以及 notes 全部 6 个接口（search_note / list_notebook / list_note / get_doc_content / import_doc / append_doc）。

**通用试错 / 已知坑（跨模块）**

- **⚠️ IMA OpenAPI 不支持删除任何实体**：文件 / 文件夹 / 知识库 / 标签均不可通过 API 删除，测试会在库中留痕，需用户到 IMA 客户端手动清理。本轮实测在「测试知识库1」残留文件夹 A/B、关联笔记、网页、txt（已移入文件夹 B）；另新建临时库「ima.plus-skill 接口测试临时库」、真实加入公开库「Python入门教程」、对测试笔记追加了内容——均需手动清理。
- **⚠️ join_knowledge 会真实加入公开库**：有副作用，调用前确认用户确实要加入（本轮误加入「Python入门教程」需手动退出）。
- **⚠️ update_knowledge_base_permission 改权限有真实副作用**：建议在专用临时库测，避免改动正式库真实权限。
- **凭证双配置，config.json 优先**：加载优先级 `config.json` > 环境变量 `IMA_OPENAPI_CLIENTID/APIKEY` > `~/.config/ima/`。本轮 `config.json` 有效。
- **普通成员写操作返回 220030 无权限**：建库/改名/置顶/标签/权限等写操作，角色为普通成员时返回 220030，需先确认角色为创建者/协作成员/管理员。
- **export_media 接口 220030 无权限**：`export_media.cjs` 脚本逻辑正确，但后端 `export_media_for_ima_sandbox` 返回 `code=220030 无权限访问该接口`——当前 API key 未开通该导出接口权限（非脚本缺陷，详见 knowledge-base 模块「导出媒体」章节）。

### 核心心智：用 API 技能的 3 个原则

| 原则 | 含义 | 反例 |
|------|------|------|
| **不猜** | 指代、ID、路径、枚举——拿不准就问/查 | 猜 media_type=11 是微信文章 |
| **不省** | UTF-8 校验、双层 code 检查、双模块 SKILL.md | 跳过 encoding 直接写笔记 |
| **不堆** | 结果分主题、ID 内部消化、摘要 + 下一步 | 50 行 ID 列表直接贴给用户 |

> 最快的路径 = `config.json` 一次写入 + Node 统一调用 + 浅读 SKILL.md + 模糊指令先问人。
