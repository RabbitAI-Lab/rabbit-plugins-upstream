---
name: ima.plus-skill-1.0.8
description: IMA.plus 技能（V1.0.8）——笔记管理与知识库操作。支持自然语言目录路径（--path 自动解析知识库/文件夹/笔记本，无需 kb_id，解析结果分层缓存零重复调用）、上传/导出文件、打包导出知识库为 zip、创建文件夹、移动/重命名/置顶知识条目、创建与修改知识库、标签管理、权限管理、广场发现、添加网页到知识库、搜索/浏览/创建/编辑笔记。凭证单一来源：环境变量 IMA_OPENAPI_CLIENTID / IMA_OPENAPI_APIKEY（强制设置，不设置无法使用）；缓存位置 IMA_RESOLVE_CACHE（非 ima.copilot 环境强制）。
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

> **版本：V1.0.8**
>
> **运行环境**：Node.js ≥ 18.0.0（所有 .cjs 脚本 + inline JSON 解析依赖）

Unified IMA OpenAPI skill. Currently supports: **notes**, **knowledge-base**.

## ⛔ MANDATORY RULES — read before ANY operation

0. **自然语言路径优先（所有模块通用，强制）：** 用户给出知识库/文件夹/笔记本的名称或路径（如"我的知识库/项目/文档"、"存到学习笔记"）时，**一律用解析器自动转 ID，禁止让用户提供 kb_id / folder_id**。知识库用根目录 `resolve_path.cjs --path`，笔记本用 `notes/scripts/resolve_notebook.cjs --path`。面向用户永远只展示名称，禁止暴露任何 ID。
   - ⛔ **禁止擅自使用 `--kb <kb_id>`**：即使解析过程中拿到了 kb_id，**也不得主动用它调用脚本**——所有脚本调用一律走 `--path "知识库名/文件夹..."`（内部自动解析）。`--kb` 仅在**用户明确要求使用某个具体 ID** 时才允许出现。违反此规则视为流程错误。
   - 兼容参数 `--kb-name`（按名称匹配）可以正常使用，但 `--path` 是首选。

### 🔧 路径解析缓存机制（V1.0.8+，无需手动管理）

解析器会把「知识库名 → kb_id、文件夹路径 → folder_id」**分层树状持久化**到缓存文件，
按「知识库 → 子文件夹 → 孙文件夹」嵌套，同名文件夹在不同库/不同父目录各占节点，不会串库。

**缓存位置（强制检查，安装 skill 时必须确定）：**
1. 环境变量 `IMA_RESOLVE_CACHE` 显式指定（所有环境，优先级最高）
2. ima.copilot 环境未设置时默认 `/sandbox/workspace/.ima_cache/resolve_cache.json`（workspace 持久、平台不重置）
3. **其他 agent / 自建环境未设置 `IMA_RESOLVE_CACHE` → 直接报错不可用**（与凭证同等强制）。
   安装时须先设置：`export IMA_RESOLVE_CACHE=/path/to/resolve_cache.json`（可写入 ~/.bashrc 或 ~/.zshrc）

- **无过期时间**：缓存长期有效；重复解析同一路径 **0 次 API 调用**（部分命中只补查缺失层级）。
- **失效自愈**：所有消费脚本已包 `withPathRetry`——若操作因「目标不存在」（如库/夹被删或改名，`220001/invalid/不存在` 类）失败，自动失效该路径缓存 → 全 API 重新解析 → 重试一次；**重查任一层失败即报「目录位置不存在」，整个操作直接中止，不猜测后续层级**。权限（220030）/限流（200001）类错误不触发自愈。
- **手动清缓存**（一般不需要）：删除缓存文件即可，下次解析自动重建。知识库/文件夹被删除后首次操作会自愈恢复。
- 笔记本解析（`--notes` / `resolve_notebook.cjs`）同样缓存（`notebooks` 节）。

1. **UTF-8 encoding (notes writes only):** Before calling `import_doc` or `append_doc`, ALL string fields (`content`, `title`) MUST be validated as legal UTF-8. Non-UTF-8 content causes irreversible garbled text. See [Detailed Rules](#detailed-utf-8-encoding-rules) for platform-specific methods.
2. **File upload naming:** `title` MUST equal `file_name` (with extension). Never rename, shorten, translate, or modify the original filename.
3. **Unsupported file types:** Reject immediately with a clear message. Do NOT ask user "do you still want to try?" Video files, Bilibili/YouTube URLs, and `file://` URLs are not supported — tell user to use IMA desktop client.
4. **File upload integrity:** Keep file content as-is during upload. No encoding conversion for binary files (PDF, images, Excel, etc.).
5. **PowerShell 5.1 (all modules):** If running in PowerShell, detect version before first API call. PS 5.1 silently converts request Body to GBK — must use UTF-8 byte array mode. See [Detailed Rules](#powershell-51-environment-detection).
6. **副作用操作必须显式确认（不得自行执行）：** `join_knowledge`（真实加入公开库）、`tag_delete` / `tag_rename`（不可逆；新名已存在时自动合并）、`update_knowledge_base_permission`（影响全库成员）、`append_doc` 追加已有笔记（不可撤销修改）——调用前必须得到用户明确同意，不确定时先问。

## 🚀 高频操作快查表（30 秒上手）

| 用户意图 | 直接执行 |
| --- | --- |
| 上传文件到知识库 | `node knowledge-base/scripts/upload_to_kb.cjs --path "库名/文件夹" --file <路径>` |
| 打包知识库/文件夹为 zip | `node knowledge-base/scripts/export_kb_zip.cjs --path "库名/文件夹" --out /path/out.zip` |
| 列出知识库内容 | `node knowledge-base/scripts/list_all_files.cjs --path "库名"` |
| 创建文件夹 | `node knowledge-base/scripts/create_folder.cjs --path "库名/父夹" --name "新夹"` |
| 新建笔记 | `node notes/scripts/notes_create.cjs --content "内容" --path "笔记本名"` |
| 追加笔记 | `node notes/scripts/notes_append.cjs --note-id <id> --content "内容"` |

> 路径一律用 `--path "知识库名/文件夹..."` 自然语言，禁止 kb_id。其余操作见各模块 SKILL.md 与脚本头部 Usage 注释。

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

## ⚠️ 出错时查这里（按需读取）

遇到后端错误码（`220030` / `51` / `210039` / `220001` 等）或任何异常现象，**先读 `references/troubleshooting.md`** 对照定位——那里汇总了全部实测沉淀的错误码对照表、权限边界、批量导出 SOP 与已知坑。正常执行时无需读取该文件。

## ⚙️ 安装配置总览（必读）

安装本 skill 只需配置 **两件事**（均为环境变量，强制设置，不设置无法使用）：

| # | 配置项 | 环境变量 | 未设置时 |
|---|--------|----------|----------|
| 1 | 凭证 | `IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY` | 报错不可用（`code=-100`） |
| 2 | 缓存保存位置 | `IMA_RESOLVE_CACHE` | ima.copilot 默认 workspace 缓存；**其他环境报错不可用** |

- ✅ **ima.copilot 环境：零配置直接可用**（平台已注入凭证 + 默认 `/sandbox/workspace/.ima_cache/` 缓存）
- ⚠️ **其他 agent / 自建环境**：按下方「Credential Check」设置凭证、按「路径解析缓存机制」设置缓存位置，**两件都配好才能用**

## Credential Check（凭证获取与配置）

### 凭证从哪来（必读）

凭证有 **两种来源，任选其一** 设置到环境变量即可：

1. **ima app 内 copilot 会话环境变量中的凭证**（`IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY`）
   ——这套凭证**已开通导出权限**（`export_media` / `export_media_for_ima_sandbox` 可用），推荐。
2. **https://ima.qq.com/agent-interface 申请的 API key**——普通功能（上传/建库/打标签/移动/搜索等）可用；
   ⚠️ 但**导出类接口可能返回 `code=220030 无权限`**（导出权限未开通，非脚本缺陷），需要打包导出时请用来源 1 的凭证。

> ⛔ **凭证强制从环境变量读取，单一来源，不设置技能无法使用**：
> 不再支持 config.json / ~/.config/ima/ 等任何文件配置与自动降级。

- ✅ **ima.copilot 环境**：平台已自动注入 `IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY`，直接可用，无需任何配置。
- ⚠️ **自建环境（自己的电脑 / 服务器）**：必须先主动设置环境变量（来源 1 或 2 任一），否则所有脚本报错退出（`code=-100`，提示未设置凭证）。

### 自建环境设置方式

**Linux / macOS**（写入 shell 配置文件，永久生效）：

```bash
# ~/.bashrc 或 ~/.zshrc 末尾追加（替换成你自己的凭证值）
export IMA_OPENAPI_CLIENTID="你的 clientId"
export IMA_OPENAPI_APIKEY="你的 apiKey"
source ~/.bashrc
```

**Windows**：系统设置 → 环境变量 → 新建 `IMA_OPENAPI_CLIENTID` / `IMA_OPENAPI_APIKEY`。

### 一步获取凭证（完整指令）

> 在 **ima app** 中打开 **copilot** 对话，原样发送以下指令：

```
请把环境变量里的 IMA 凭证发给我：IMA_OPENAPI_CLIENTID 和 IMA_OPENAPI_APIKEY 的值（我要配置 ima.plus-skill 技能的 clientId 和 apiKey）
```

copilot 会从运行环境变量读取并返回 `clientId`（= `IMA_OPENAPI_CLIENTID`）与
`apiKey`（= `IMA_OPENAPI_APIKEY`）。拿到后按上方方式 export 到自建环境。

### 验证

```bash
node knowledge-base/scripts/export_kb_zip.cjs --path "<你的个人库名>" --dry-run
```

能列出文件清单即凭证有效。

### 安全提醒

- 该凭证绑定你的账号且已开通导出权限，**切勿外泄、切勿打包进公开分发的 zip**
- 凭证只发送到 `ima.qq.com`，不写入任何日志、配置文件或外部文件
- 凭证失效 / 导出报 220030 时，重新执行「一步获取凭证」更新环境变量即可

## API 调用模板

> **先看「高频操作快查表」**：常用操作（上传/打包/标签/文件夹/笔记新建追加）已有封装脚本，直接调用脚本即可，无需手写 API。
> 以下模板仅用于**无脚本覆盖的操作**（笔记块编辑/移动/导出、自定义查询等）。

> **跨平台说明**：本 skill 的全部脚本（`.cjs`）为**单一 Node.js 实现**，Windows / Linux / macOS 命令本身完全一致；差异只在 shell 包装（捕获输出、检查退出码）与中文编码处理。**zip 打包为纯 Node 实现**（zlib + 手写 zip 结构），不依赖系统 `zip`/`tar` 命令，Windows 直接可用（含中文文件名 UTF-8）。下面分别给出两平台的规范写法。运行需 **Node 18+**（依赖全局 `fetch` 与 `node:` 前缀模块）。

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

### 核心心智：用 API 技能的 3 个原则

| 原则 | 含义 | 反例 |
|------|------|------|
| **不猜** | 指代、ID、路径、枚举——拿不准就问/查 | 猜 media_type=11 是微信文章 |
| **不省** | UTF-8 校验、双层 code 检查、双模块 SKILL.md | 跳过 encoding 直接写笔记 |
| **不堆** | 结果分主题、ID 内部消化、摘要 + 下一步 | 50 行 ID 列表直接贴给用户 |

> 最快的路径 = 凭证一次配置（问 copilot 拿环境变量凭证）+ Node 统一调用 + 浅读 SKILL.md + 模糊指令先问人。
