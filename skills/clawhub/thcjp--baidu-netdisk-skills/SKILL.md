---
slug: "baidu-netdisk-skills"
name: "baidu-netdisk-skills"
version: 1.1.6
displayName: "百度网盘"
summary: "百度网盘文件管理，限 /apps/bdpan/ 目录，支持上传下载转存分享搜索与记忆备份。"
license: "Proprietary"
description: |-
  百度网盘文件管理技能，通过 bdpan 命令行工具对百度网盘进行文件操作，所有操作限制在
  /apps/bdpan/ 目录范围内。支持完整的文件生命周期管理与 Agent 记忆备份恢复能力.
  核心能力：
  - 文件操作：上传、下载、转存、分享、搜索、移动、复制、重命名、创建文件夹、删除
  - 大文件下载策略：根据文件大小自动选择直接下载或 nohup 后台下载，避免 Bash 超时
  - 分享链接处理：支持从分享链接（含提取码）转存或下载到本地
  - 记忆备份与恢复：支持 4 种 Claw 产品（kimiclaw/maxclaw/qclaw/skill-platform）的
  Agent 记忆备份、查看备份列表、按日期恢复，内置 safety net 防误操作
  - 安全机制：写操作必须用户显式确认、路径穿越防护、禁止读取敏感凭据配置

  适用场景：
  - 在百度网盘 /apps/bdpan/ 目录内管理文件（上传下载、整理归档、分享协作）
  - 从他人分享链接转存资源到自己的网盘
  - 跨设备同步 Agent 记忆（AGENTS.md、SOUL.md、MEMORY.md 等）
  - 大文件下载不阻塞 Agent 会话

  差异化：严格的触发规则与确认机制，区分只读与写操作风险等级；
  内置大文件后台下载策略；记忆恢复具备 safety net 备份保护；
  禁止路径穿越与敏感配置读取，确保操作安全.
tags:
  - Agents
  - Storage
  - Baidu
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 百度网盘

百度网盘文件管理工具，所有操作限制在 `/apps/bdpan/` 目录内。适配 Claude Code、DuClaw、Skill 平台等 Agent 环境.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 百度网盘处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 百度网盘百度网盘文件管理 | 不支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |

## 触发规则

### 网盘文件操作触发

同时满足以下条件才执行：

1. 用户消息中包含**明确指向百度网盘**的关键词，至少匹配以下之一：`百度网盘`、`百度云盘`、`bdpan`、`baidu netdisk`、`baidu pan`、`baidu drive`、`pan.baidu.com`
2. 操作意图明确（上传/下载/转存/分享/查看/搜索/移动/复制/重命名/创建文件夹/删除/登录/注销）

**不要触发的情况：**

- 用户仅说"网盘""云盘""云存储""百度云"等泛指词，未明确指向百度网盘 → 应反问"您指的是百度网盘（pan.baidu.com）吗？"再决定
- 用户在讨论其他云盘服务（OneDrive、Google Drive、阿里云盘、夸克网盘等）
- 仅复述、引用历史聊天记录中的网盘内容，而无新的操作意图

未通过触发规则时，禁止执行任何 bdpan 命令.
### 记忆备份/恢复触发

以下表达即使未提及"网盘"也应触发（仅限 kimiclaw/maxclaw/qclaw/skill-platform 环境）：

| 用户说法示例 | 触发操作 |
|----:|----:|
| "备份记忆"、"把记忆存到网盘" | backup |
| "查看记忆备份"、"备份列表" | list |
| "恢复记忆"、"回滚记忆"、"记忆回档" | restore（需确认日期） |
| "恢复 3月16号 的记忆" | restore 指定日期 |

**区分原则：** 操作对象是否为 Agent 记忆文件（AGENTS.md、SOUL.md、MEMORY.md、memory/*.md 等）.
## 已知限制

1. **登录**：必须使用 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）`，禁止直接调用 `bdpan login` 及其任何子命令/参数
2. **Token/配置**：禁止读取或输出 `~/.config/bdpan/config.json` 内容（含 access_token 等敏感凭据）
3. **更新/登录**：更新必须由用户明确指令触发，禁止自动或静默执行；Agent 禁止使用 `--yes` 参数执行 update.sh 或 login.sh
4. **环境变量**：Agent 禁止主动设置 `BDPAN_CONFIG_PATH`、`BDPAN_BIN` 等环境变量
5. **路径安全**：禁止路径穿越（`..`、`~`）、禁止访问 `/apps/bdpan/` 范围外的绝对路径
6. **记忆备份约束**：禁止直接用裸 `bdpan upload/download` 操作记忆目录；必须通过 `memory-backup.sh` 脚本执行

## 前置检查

每次触发时按顺序执行：

1. **安装检查**：`command -v bdpan`，未安装则告知用户并确认后执行 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）`
2. **登录检查**：`bdpan whoami`，未登录则引导执行 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）`
3. **路径校验**：验证远端路径在 `/apps/bdpan/` 范围内

## 确认规则

| 风险等级 | 操作 | 策略 |
|:---:|:---:|:---:|
| **高（必须确认）** | `rm` 删除、上传/下载目标已存在同名文件 | 列出影响范围，等待用户确认 |
| **中（路径模糊时确认）** | upload、download、mv、rename、cp | 路径明确直接执行，不明确则确认 |
| **低（直接执行）** | ls、search、whoami、mkdir、share | 无需确认 |

**额外规则：**

- 操作意图模糊（"处理文件"→确认上传还是下载）→ 必须确认
- 序数/代词引用有歧义（"第N个"、"它"）→ 必须确认
- 用户取消意图（"算了"、"取消"）→ 立即中止

## 核心能力
### 查看状态与列表
```bash
bdpan whoami                                          # 查看登录状态
bdpan ls [目录路径] [--json] [--order name|time|size] [--desc] [--folder]
```

**输入**: 用户提供查看状态与列表所需的指令和必要参数.
**处理**: 解析查看状态与列表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回查看状态与列表的处理结果,包含执行状态码、结果数据和执行日志.
### 上传
```bash
bdpan upload <本地路径> <远端路径>
```

**关键约束：** 单文件上传远端路径必须是文件名，禁止以 `/` 结尾。文件夹上传：`bdpan upload ./project/ project/`.
步骤：确认本地路径存在 → 确认远端路径 → `bdpan ls` 检查远端是否已存在 → 执行.
**输入**: 用户提供上传所需的指令和必要参数.
**输出**: 返回上传的处理结果,包含执行状态码、结果数据和执行日志.
### 下载
**直接下载：**

```bash
bdpan download <远端路径> <本地路径>
```

**大文件下载策略（重要）：** Agent 的 Bash 工具有执行超时限制，必须根据文件大小选择策略：

1. **获取文件大小**：用 `bdpan ls --json <远端路径>` 获取 `size` 字段（字节）
2. **按大小分策略**：

| 文件大小 | 策略 | 执行方式 |
|:------|------:|:------|
| ≤ 50MB | 直接下载 | `bdpan download`，Bash timeout 设为 300000（5 分钟） |
| > 50MB | 后台下载 | 使用 `nohup` 后台执行，Agent 轮询进度 |

**大文件（> 50MB）后台下载流程：**

```bash
# 启动后台下载
nohup bdpan download <远端路径> <本地路径> > /tmp/bdpan-dl-$$.log 2>&1 & echo $!
# 轮询进度
kill -0 <PID> 2>/dev/null && echo "running" || echo "done"; ls -l <本地路径> 2>/dev/null; tail -5 /tmp/bdpan-dl-<PID>.log 2>/dev/null
# 清理日志
rm -f /tmp/bdpan-dl-<PID>.log
```

**分享链接下载（先转存再下载）：**

```bash
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/
bdpan download "https://pan.baidu.com/s/1xxxxx" ./downloaded/ -p abcd       # 提取码单独传入
bdpan download "https://pan.baidu.com/s/1xxxxx?pwd=abcd" ./downloaded/ -t my-folder  # 指定转存目录
```

**输入**: 用户提供下载所需的指令和必要参数.
**输出**: 返回下载的处理结果,包含执行状态码、结果数据和执行日志.
### 转存
将分享文件转存到网盘，**不下载到本地**：

```bash
bdpan transfer "https://pan.baidu.com/s/1xxxxx" -p <提取码> [-d 目标目录] [--json]
```

**输入**: 用户提供转存所需的指令和必要参数.
**处理**: 解析转存的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回转存的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `转存` 选项

### 分享
```bash
bdpan share <路径> [路径...] [--period <天数>] [--json]
```

**--period 参数：** 0=永久, 1, 7, 30（默认：7）。根据用户语义意图选择有效期。永久链接需提示用户注意文件安全。付费接口，需在百度网盘开放平台购买服务.
**处理**: 解析分享的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回分享的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `分享` 选项

### 搜索
```bash
bdpan search <关键词> [--category 0-7] [--no-dir|--dir-only] [--page-size N] [--page N] [--json]
```

category：0=全部 1=视频 2=音频 3=图片 4=文档 5=应用 6=其他 7=种子.
**输入**: 用户提供搜索所需的指令和必要参数.
**处理**: 解析搜索的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回搜索的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `搜索` 选项

### 移动 / 复制 / 重命名 / 创建文件夹
```bash
bdpan mv <源路径> <目标目录>
bdpan cp <源路径> <目标目录>
bdpan rename <路径> <新名称>       # 第二参数是文件名，非完整路径
bdpan mkdir <路径>
```

**处理**: 解析移动 / 复制 / 重命名 / 创建文件夹的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回移动 / 复制 / 重命名 / 创建文件夹的处理结果,包含执行状态码、结果数据和执行日志.
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`baidu-netdisk-skills`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 路径规则

| 场景 | 格式 | 示例 |
|---:|:---|---:|
| **命令参数** | 相对路径（相对于 `/apps/bdpan/`） | `bdpan upload ./f.txt docs/f.txt` |
| **展示给用户** | 中文名 | "已上传到：我的应用数据/bdpan/docs/f.txt" |

映射关系：`我的应用数据` ↔ `/apps`。**禁止：** 命令中使用中文路径、展示时暴露 API 路径.
## 记忆备份与恢复

仅支持 4 种 Claw 产品（kimiclaw、maxclaw、qclaw、skill-platform），自动检测当前环境.
**网盘存储路径：** `/apps/bdpan/agent-memory/<agent>/<device>/manual/<timestamp>/`

**备份内容：** 7 个 Workspace 文件 + `memory/*.md` + `manifest.json`

```bash
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） backup                    # 备份
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） list                      # 查看备份列表
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） restore 2026-03-16        # 恢复指定日期
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） restore 2026-03-16 --force  # 强制恢复
```

**恢复安全机制：** 恢复前列出将被覆盖的文件清单 → 默认需用户输入 `y` 确认 → 恢复前自动将当前记忆备份到 `.backup-before-restore/<timestamp>/` 防误操作.
## 工作流程

1. **触发判定**：检查关键词与操作意图是否满足触发规则.
2. **前置检查**：bdpan 安装 → 登录状态 → 路径校验.
3. **风险分级**：按确认规则判断操作风险等级.
4. **确认执行**：高风险操作展示影响范围等待确认；低风险直接执行.
5. **结果呈现**：展示操作结果，路径用中文名呈现，隐藏 API 路径与敏感配置.
## 案例展示

### 案例 1：从分享链接下载大视频文件

**用户请求**：帮我把这个百度网盘分享链接里的视频下载到本地，链接是 https://pan.baidu.com/s/1abcXYZ?pwd=w9k3

**执行流程**：

```bash
# 1. 前置检查
bdpan whoami
# ...
# 2. 转存分享链接到网盘（写操作，需确认）
# 向用户展示：将转存 https://pan.baidu.com/s/1abcXYZ 到 /apps/bdpan/downloaded/，确认后执行
bdpan download "https://pan.baidu.com/s/1abcXYZ?pwd=w9k3" ./downloaded/
# ...
# 3. 转存后获取文件大小
bdpan ls --json ./downloaded/
# ...
# 4. 根据大小选择下载策略（假设视频 > 50MB，使用后台下载）
nohup bdpan download ./downloaded/video.mp4 ./local-video.mp4 > /tmp/bdpan-dl-$$.log 2>&1 & echo $!
# ...
# 5. 轮询进度并报告用户
kill -0 <PID> 2>/dev/null && echo "running" || echo "done"; tail -5 /tmp/bdpan-dl-<PID>.log
```

**输出说明**：转存成功后告知用户文件大小与预计下载时间，后台下载期间定期报告进度，完成后告知本地路径.
### 案例 2：备份与跨设备恢复 Agent 记忆

**用户请求**：把当前 Agent 的记忆备份到网盘，然后我在另一台设备上要恢复到今天的备份.
**执行流程**：

```bash
# 设备 A：备份记忆
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） backup
# ...
# 设备 B：查看可用备份
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） list
# ...
# 设备 B：恢复指定日期（需确认）
# 向用户展示：将覆盖 AGENTS.md、SOUL.md、MEMORY.md 等 7 个文件 + memory/*.md
bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件） restore 2026-07-20
```

**输出说明**：备份时展示 manifest 内容与存储路径；恢复前列出将被覆盖的文件清单，确认后执行，自动生成 safety net 备份。非 4 种 Claw 环境报错退出.
### 案例 3：搜索并整理文档文件

**用户请求**：帮我搜索网盘里的 PDF 文档，把找到的都移动到 docs 文件夹，然后分享这个文件夹.
**执行流程**：

```bash
# 1. 搜索文档类文件（只读）
bdpan search ".pdf" --category 4 --json
# ...
# 2. 创建目标文件夹（低风险，直接执行）
bdpan mkdir docs
# ...
# 3. 逐个移动（写操作，需确认）
# 向用户展示：将移动 N 个 PDF 到 docs/，确认后执行
bdpan mv ./file1.pdf docs/
bdpan mv ./file2.pdf docs/
# ...
# 4. 分享文件夹（低风险，但分享为付费接口）
bdpan share docs/ --period 30 --json
```

**输出说明**：搜索结果列出文件名与路径；移动前展示影响范围；分享返回链接、提取码、有效期，提示永久链接注意安全.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| `bdpan: command not found` | 未安装 bdpan 工具 | 引导用户确认后执行 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）` |
| `未登录` / `whoami 失败` | Token 过期或未登录 | 引导执行 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）` 重新登录 |
| 路径穿越被拦截 | 路径含 `..`、`~` 或绝对路径越界 | 拒绝执行，提示操作仅限 `/apps/bdpan/` 范围内相对路径 |
| 命令路径含中文 | 命令参数误用中文路径（如"我的应用数据/..."） | 提示命令须用相对路径，展示时再用中文名 |
| 上传远端路径以 `/` 结尾 | 单文件上传远端路径格式错误 | 提示远端路径须为文件名而非目录，修正后 |
| 远端文件不存在 | `bdpan ls` 返回空，下载/移动目标缺失 | 用 `bdpan search <文件名>` 搜索确认，或检查路径拼写 |
| 分享链接格式无效 | 链接非 `pan.baidu.com/s/` 格式或已失效 | 提示用户检查链接格式，确认是否需要提取码（`-p` 参数） |
| 大文件下载超时 | 未按大小策略执行，Bash 超时中断 | 改用 nohup 后台下载，轮询进度，设 timeout 为 300000 |
| 同名文件已存在 | 上传/下载目标路径已有同名文件 | 列出现有文件，询问覆盖还是重命名，确认后执行 |
| 记忆备份环境不支持 | 当前非 kimiclaw/maxclaw/qclaw/skill-platform | 报错说明不支持当前环境，不执行备份/恢复操作 |
| 分享接口报付费错误 | 百度网盘开放平台服务未购买 | 提示分享为付费接口，需在开放平台购买服务后使用 |
| 直接调用 bdpan login 被拦截 | Agent 误用裸 `bdpan login` 命令 | 禁止该调用，必须通过 `（请参考skill目录中的脚本文件）` 执行登录 |

## 常见问题

### Q1：大文件下载总是超时怎么办？
A：先用 `bdpan ls --json <远端路径>` 获取文件 `size` 字段。超过 50MB 的文件必须使用 `nohup bdpan download ... > /tmp/bdpan-dl-$$.log 2>&1 &` 后台下载，Agent 轮询 `kill -0 <PID>` 与日志判断进度。Bash 工具 timeout 设为 300000（5 分钟）仅适用于 ≤50MB 的小文件.
### Q2：从分享链接下载和转存有什么区别？
A：`bdpan download "https://pan.baidu.com/s/xxx?pwd=yyy" ./local/` 会先转存到网盘再下载到本地；`bdpan transfer "https://pan.baidu.com/s/xxx" -p yyy` 只转存到网盘不下载本地。若只需保存到网盘用 transfer，需本地文件用 download.
### Q3：分享链接的有效期怎么选？
A：根据语义意图选择 `--period`：用户说"永久/不过期/一直能用"用 `--period 0`（提示注意安全）；指定天数选最接近的 1/7/30；未表达偏好默认 `--period 7`。永久链接无法自动过期，需提醒用户文件安全.
### Q4：记忆恢复会覆盖现有记忆吗？能撤销吗？
A：会覆盖。恢复前会列出所有将被覆盖的文件清单，默认需用户输入 `y` 确认。同时自动将当前本地记忆备份到 `<workspace>/.backup-before-restore/<timestamp>/`，若恢复有误可从该 safety net 目录手动找回。非交互环境必须加 `--yes` 才执行.
### Q5：哪些操作需要用户确认？
A：高风险操作（`rm` 删除、同名文件覆盖）必须确认；中风险操作（upload/download/mv/rename/cp）路径明确时直接执行，路径模糊时确认；低风险操作（ls/search/whoami/mkdir/share）无需确认。写操作即使上下文延续也必须重新确认.
### Q6：为什么不能访问 /apps/bdpan/ 以外的路径？
A：安全限制。所有操作限定在 `/apps/bdpan/` 范围内，禁止路径穿越（`..`、`~`）和越界绝对路径。这是为了防止误操作系统其他目录。展示给用户时路径映射为中文名（`我的应用数据/bdpan/...`）.
### Q7：用户发了 32 位十六进制字符串是什么？
A：可能是百度网盘授权码。先确认"这是百度网盘授权码吗？确认后将执行登录流程"，确认后执行 `bash ${CLAUDE_SKILL_DIR}/（请参考skill目录中的脚本文件）`（不使用 `--yes`，保留安全确认环节）.
## 补充限制说明

- 所有操作限制在 `/apps/bdpan/` 目录范围内，不支持访问其他网盘路径.
- 分享功能为百度网盘开放平台付费接口，需购买服务.
- 记忆备份/恢复仅支持 4 种 Claw 产品环境.
- 登录必须通过 `（请参考skill目录中的脚本文件）`，禁止直接调用 `bdpan login`.
- 大文件下载受 Bash 超时限制，需使用 nohup 后台策略.
- 禁止读取或输出 `~/.config/bdpan/config.json` 等敏感凭据配置.
## 触发条件

- 用户明确提及百度网盘/bdpan/baidu drive 等关键词且有文件操作意图时激活.
- 用户请求记忆备份/恢复时（仅限 4 种 Claw 环境）激活.
- 用户仅提及泛指词（"网盘""云盘"）时需反问确认后再决定是否触发.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "百度网盘处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "baidu-netdisk-skills"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
