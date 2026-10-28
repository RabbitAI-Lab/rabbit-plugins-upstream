# 在线笔记备份、双向同步与恢复

## 目录

- [工作模式](#工作模式)
- [同步范围与在线结构](#同步范围与在线结构)
- [连接 Notion](#连接-notion)
- [连接 FlowUs](#连接-flowus)
- [日常同步](#日常同步)
- [多实例共享同一记忆库](#多实例共享同一记忆库)
- [冲突与删除](#冲突与删除)
- [定时同步](#定时同步)
- [恢复与平台切换](#恢复与平台切换)
- [安全和故障处理](#安全和故障处理)

## 工作模式

Team Memory 没有 `.team-memory-notebook.json` 时完全按本地模式运行，不访问网络。

- `backup`：本地 Markdown 是唯一可信源；只推送本地变化。在线直接编辑会报告为 `remote-drift`，不拉回本地。
- `bidirectional`：在线已提交修订可以成为变更输入。每次读取前同步，每次本地写入后再次同步。
- 每套主库同时只能连接一个 Notion 或 FlowUs 根页面。连接另一平台前先执行 `disconnect`。

切换模式：

```bash
python3 scripts/notebook-sync.py mode backup
python3 scripts/notebook-sync.py mode bidirectional
python3 scripts/notebook-sync.py plan
```

切换后先看 `plan`，确认没有意外冲突再运行 `sync`。

## 同步范围与在线结构

默认同步以下可读 Markdown：

- `skill-config.yaml`
- `data/members/`
- `data/stakeholders/`
- `data/upward/`
- `data/company/`
- `data/manager/`
- `data/sources/`（完整文字谈话、来源信息和拆解映射）
- `data/tasks/`
- `data/archive/`
- `data/insights/`
- `data/team-memory-overview.md`

不上传 token、`.index/`、`.backup/`、`.reports/`、`.sync/`、`import/`、附件、SQLite、JSONL、SVG 和模板。

`.sync/` 不整库上传；其中未解决冲突的 local/remote/base 正文和必要脱敏元数据会单独进入恢复载荷。恢复时先校验这些正文，再重建待处理冲突状态；机器身份、锁、日志和凭据不随之复制。

远端目录固定为：

```text
团队记忆 · {repository-id}
├── 00 使用说明与同步状态
├── 01 成员
├── 02 相关方
├── 03 向上管理与公司战略
├── 04 待办与复盘
├── 05 洞察与归档
├── 06 管理者思考
├── 07 对话与资料原文
├── 90 冲突与待确认删除
└── 99 恢复索引与事务记录
```

每个文件保留当前页面和一个“上一版”页面。再次更新时，新的旧版会顶替原上一版，不持续堆积历史。

v2 协议同时保存可读页面和原文恢复载荷。载荷以 Base64 分片存入系统目录的纯文本 JSON 代码块，manifest 保存分片顺序、原始字节长度、SHA-256 及当前/上一版引用。正文、原文载荷和 manifest 在同一事务提交；token、锁、缓存和日志不进入载荷。恢复使用经过校验的原始字节，可读页面不承担保真恢复职责。

首次新版本同步旧库时，在远端租约保护下升级主槽与备用槽并回读验证，然后才提交正文变化。旧客户端无法改写新 manifest；同一主库的其他机器也需升级 skill。旧备份仍可读取恢复，但如果没有原文载荷，只能恢复其转换后的 Markdown，脚本会明确提示保真度限制。

## 连接 Notion

1. 在 Notion 创建 integration，启用读取、插入和更新内容权限。
2. 把准备作为父目录的页面共享给该 integration。
3. 把 token 放进环境变量，不要把 token 写进命令或配置文件：

```bash
export TEAM_MEMORY_NOTION_TOKEN="..."
python3 scripts/notebook-sync.py connect \
  --provider notion \
  --parent "NOTION_PARENT_PAGE_ID" \
  --mode backup
```

需要双向同步时把模式改为 `bidirectional`。需要 macOS 后台同步时，可在连接时加入 `--store-keychain`；脚本把 token 存入系统钥匙串，配置文件只保存钥匙串引用。

续接已经由 Team Memory 创建的在线根页面：

```bash
python3 scripts/notebook-sync.py connect \
  --provider notion \
  --resume "TEAM_MEMORY_ROOT_PAGE_ID" \
  --mode bidirectional
```

不要用普通 Notion 页面作为 `--resume`；它必须包含 Team Memory 控制信息。

`connect` 只创建或绑定在线结构，不会立即上传本地内容。连接成功后先运行 `plan`，确认同步方向，再运行首次 `sync`。

## 连接 FlowUs

FlowUs V2 API 需要有效 token、付费空间和相应 `pages/blocks` scopes。免费空间返回 403 时，同步器会停止并解释原因。参见 [官方认证与权限](https://flowus.cn/developer-api/v2/zh/getting-started/authentication-and-scopes)。

```bash
export TEAM_MEMORY_FLOWUS_TOKEN="..."
python3 scripts/notebook-sync.py connect \
  --provider flowus \
  --parent "FLOWUS_PARENT_PAGE_ID" \
  --mode backup
```

续接方式与 Notion 相同：

```bash
python3 scripts/notebook-sync.py connect \
  --provider flowus \
  --resume "TEAM_MEMORY_ROOT_PAGE_ID" \
  --mode bidirectional
```

FlowUs 可读页使用 Team Memory 模板需要的 Markdown 子集。HTML 等无法安全显示的本地正文使用纯文本原文展示，其原始字节仍进入恢复载荷。在线页出现未知块或不完整内容时仍停止同步，避免把无法读取的在线改动当成成功。

写入会保留粗体、行内代码、链接、任务、列表、引用、代码块和表格，并在页面/块变更中传递 `ETag`/`If-Match`；遇到 409 时中止当前事务，不覆盖并发编辑。

与 Notion 相同，连接完成后先运行 `plan`，确认后再运行首次 `sync`。

## 日常同步

查看状态和只读预览：

```bash
python3 scripts/notebook-sync.py status
python3 scripts/notebook-sync.py plan
```

执行完整同步：

```bash
python3 scripts/notebook-sync.py sync
```

只推送或只拉取：

```bash
python3 scripts/notebook-sync.py push
python3 scripts/notebook-sync.py pull
```

v2.8.1 起，双向拉取区分“其他实例已提交的文件”和“人在可读页面上的新编辑”：前者验证原文载荷后按原始字节写入本地，保留 CRLF、末尾空行、Markdown 字面符号及原文校验关系；不会因为下载而重写云端载荷或轮换上一版。普通业务页面的新编辑仍可作为双向输入，接受后更新对应原文载荷。

完整谈话原文、拆解映射等 `sources/conversations/` 文件通过 skill 的修订流程更新；在线直接修改这些文件会进入冲突处理，不能绕过来源校验。拉取的载荷先整体校验，缺片或损坏会在写本地业务文件前停止。拉取完成后自动刷新本机查询索引。

`pull` 只允许双向模式。`push` 遇到在线独有变化时只报告，不覆盖；`pull` 遇到本地独有变化时只报告，不推送。

同步顺序：本地文件锁、凭据/API 检查、远端租约、读取最新 manifest、三方比较、备份、写页面、最后提交 manifest。租约为 120 秒，任何网络请求和长时间 `Retry-After` 等待期间都会每 30 秒检查并续期。

文件页采用写时复制：先创建新的当前版和上一版页，再提交引用它们的 manifest；提交前不就地覆盖旧页。manifest 使用主槽和备用槽交替写入，读取时选择写序号最新的完整副本。因此单次 FlowUs 整页替换或 manifest 提交中断时，下次 `sync` 仍能从另一槽的事务记录回滚，不会把半完成状态当作成功。

原文载荷也写时复制并在提交前回读校验；仅换行或末尾空白发生变化也会更新备份。谈话吸收和普通本地记录完成后运行同步。网络失败时保留本地结果，明确提示“云端待备份”，不把本地保存误报成云端已完成。没有连接时保持纯本地；后台定时任务默认关闭。

旧分片不会在 manifest 提交前立即回收；它们先进入事务的待清理清单，提交成功后再清理。`plan` 始终是只读操作，不会顺便执行这些清理。

双向模式预同步失败时：

- 可以读取本地数据，但要标注“在线同步失败，内容可能过期”。
- 不要让智能体静默写入。
- 用户明确同意离线写入后先登记原因，再修改本地文件：

```bash
python3 scripts/notebook-sync.py offline-write --note "远端暂不可用，用户同意先记录本地观察"
```

- 恢复网络时立即运行 `sync`，由三方比较决定合并或进入冲突区；成功同步后待同步标记自动清除。

## 多实例共享同一记忆库

- 所有实例安装 v2.8.1 或更高兼容版本，各自维护独立的本地副本；保留每端自己的机器身份和同步状态，不复制 `.sync/` 作为另一端的状态。
- 第一端创建在线库；其他端先取得已有数据，再用 `connect --resume` 续接同一个 **Team Memory 根页面 ID**。同一普通父文件夹下分别执行 `connect --parent` 会创建不同的库。
- 每端设置 `bidirectional`；`backup` 只推送本地内容，不能实现多端相互读取。首次接入前先看 `plan`；本地若已有不同数据，需要核对并处理差异，不能覆盖已有本地记录。
- 读取前同步、写入后同步。其他端仅改变原文的换行/空白也能被识别；双方同时修改原文时保留冲突，不选择一方覆盖。
- 后台定时同步仍默认关闭，按需启用；它不能代替写入前后的同步协议。

## 冲突与删除

列出和查看冲突：

```bash
python3 scripts/notebook-sync.py conflicts list
python3 scripts/notebook-sync.py conflicts show CONFLICT-ID
```

选择一方或人工合并稿：

```bash
python3 scripts/notebook-sync.py conflicts resolve CONFLICT-ID --use local
python3 scripts/notebook-sync.py conflicts resolve CONFLICT-ID --use remote
python3 scripts/notebook-sync.py conflicts resolve CONFLICT-ID --use merged --file /absolute/merged.md
python3 scripts/notebook-sync.py sync
```

冲突解决先写入本地，之后由普通同步事务提交。在线冲突页不会静默覆盖源页面。

一端删除只生成墓碑：

```bash
python3 scripts/notebook-sync.py deletions list
python3 scripts/notebook-sync.py deletions restore DELETE-ID
python3 scripts/notebook-sync.py deletions confirm DELETE-ID
```

`confirm` 在获取远端租约后递增 manifest 修订，同时回收当前页和上一版页，删除本地同步基线。本地安全副本放入不上传的 `data/.backup/deletions-confirmed/`。远端墓碑对所有机器生效；另一台机器不能因为仍保留旧文件就将其静默复活。

全损恢复时，活动文件恢复到原路径；待确认墓碑内容放入 `data/archive/pending-deletions/`，并恢复到本地删除状态。该目录不在普通同步发现范围内。

## 定时同步

默认关闭。首版自动安装仅支持 macOS `launchd`：

```bash
python3 scripts/notebook-sync.py schedule set --every 15m
python3 scripts/notebook-sync.py schedule set --every 1h
python3 scripts/notebook-sync.py schedule set --every 24h
python3 scripts/notebook-sync.py schedule set --daily 02:30
python3 scripts/notebook-sync.py schedule status
python3 scripts/notebook-sync.py schedule off
```

安装定时任务时，若当前连接仍引用环境变量，脚本会把当前 token 转存到 macOS 钥匙串。没有可读取 token 时停止，不把 token 写入 plist。

日志位于 `data/.sync/logs/`，不会上传或进入完整导出包。

`schedule status` 同时检查配置开关、plist 是否存在、launchd 服务是否已加载、是否正在运行和最近退出码。如果 `bootstrap` 失败，新 plist 和本次配置会回滚。

## 恢复与平台切换

从当前连接恢复到新的空目录：

```bash
python3 scripts/notebook-sync.py restore --output /absolute/empty-team-memory
```

如果本地数据和 `.team-memory-notebook.json` 都已丢失，可直接从远端根页面恢复：

```bash
export TEAM_MEMORY_NOTION_TOKEN="..."
python3 /path/to/team-memory/scripts/notebook-sync.py restore \
  --provider notion \
  --remote-root "TEAM_MEMORY_ROOT_PAGE_ID" \
  --mode backup \
  --output /absolute/empty-team-memory
```

FlowUs 把 `--provider` 改为 `flowus` 并设置 `TEAM_MEMORY_FLOWUS_TOKEN`。`--remote-root` 必须指向 Team Memory 创建的根页面。

恢复命令先获取远端租约，从两个 manifest 槽中选择最新完整副本，拒绝带未完成事务的状态。原文载荷必须全部通过顺序、数量、长度和 SHA-256 校验，缺片或损坏会在写文件前停止。全部读完后再次校验 manifest 修订号和写序号，再向空目录写入原始字节并生成新的主库锁和非敏感连接配置。索引和本机同步状态重建，定时同步保持关闭。

如果旧配置的 `settings.data-path` 指向其他机器或旧位置，恢复时将工作配置重定位到本次恢复目录；原配置字节另存为 `data/archive/restore-origin/{revision}/skill-config.original.md`。业务正文保持原样，工作配置的路径适配会明确报告。

需要整体回退到每个文件紧邻的上一版时，恢复到另一个空目录：

```bash
python3 scripts/notebook-sync.py restore \
  --version previous \
  --output /absolute/previous-team-memory
```

只要任一文件尚无上一版，上一版恢复就会在写文件前停止。注意“上一版”按文件轮换，不代表同一个全库时间点；恢复后必须运行 `doctor.py`，核对跨文件引用和待办来源。

恢复后运行：

```bash
python3 /path/to/team-memory/scripts/doctor.py --skill-dir /absolute/empty-team-memory
python3 /path/to/team-memory/scripts/rebuild-index.py --skill-dir /absolute/empty-team-memory
python3 /path/to/team-memory/scripts/notebook-sync.py --skill-dir /absolute/empty-team-memory plan
```

切换平台：

```bash
python3 scripts/notebook-sync.py sync
python3 scripts/notebook-sync.py disconnect
# 再连接另一个平台并以本地主库初始化
```

`disconnect` 只解除本地绑定并停用对应定时任务，不删除远端页面。

## 安全和故障处理

- 连接前确认在线空间的成员、分享范围和数据合规要求；团队记忆可能包含绩效和投诉信息。
- `.team-memory-notebook.json` 不含 token，但包含远端页面 ID；不要把它公开发布。
- `export-data.py` 只写入脱敏同步摘要，不导出钥匙串凭据和 `data/.sync/`。
- Notion/FlowUs 返回 429 时，同步器遵守 `Retry-After` 并退避重试；认证和权限错误不会无限重试。
- 远端 manifest 截断、未知块、仓库 ID 不一致或未完成事务时运行：

```bash
python3 scripts/doctor.py --online
```

- 不要手工修改 `99 恢复索引与事务记录`、系统锁和上一版页面。普通内容页允许在线编辑。
- 不要手工复制连接配置来制造第二个在线主库；跨机器应使用 `connect --resume` 连接同一个根页面。

平台协议依据：

- [Notion Markdown 页面 API](https://developers.notion.com/guides/data-apis/working-with-markdown-content)
- [Notion Enhanced Markdown 格式](https://developers.notion.com/guides/data-apis/enhanced-markdown)
- [Notion 请求限制](https://developers.notion.com/reference/request-limits)
- [FlowUs V2 API 概览](https://flowus.cn/developer-api/v2/zh/getting-started/overview)
- [FlowUs 认证与权限](https://flowus.cn/developer-api/v2/zh/getting-started/authentication-and-scopes)
- [FlowUs 并发、ETag 与幂等约定](https://flowus.cn/developer-api/v2/zh/reference/conventions)
