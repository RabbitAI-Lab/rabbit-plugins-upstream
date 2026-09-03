---
name: qq-group-homework-summarizer
display_name: QQ群作业整理
display_name_en: QQGroupHomeworkSummarizer
description: QQ群作业整理 —— 从 QQ 群「群作业」抓取指定日期的作业内容（含图片附件），生成排版规范的 A4 Word 文档（默认单页、可多页，支持多群合并、科目筛选、仅文字版），并可发送到指定邮箱或微信。This skill should be used when the user asks to organize, export, or send QQ group homework (群作业) as a document — for example "把X月X日的群作业整理成Word"、"把今天的作业导出成文档"、"把作业发到我邮箱/微信"。触发词：群作业、作业整理、作业文档、QQ作业、发作业给XX。
agent_created: true
---

# QQ群作业整理（QQGroupHomeworkSummarizer）

将 QQ 群「群作业」中某一天的内容（文字 + 图片）抓取出来，自动排成**一页 A4** 的 Word 文档，
并按需发送到邮箱或微信。

## 适用场景

- 整理某一天（或某段时间）的群作业成文档
- 导出作业并保留老师上传的图片附件
- 把作业文档发到邮箱或微信

## 核心约束（务必先理解）

| 事实 | 说明 |
|------|------|
| 登录态在**浏览器** | 需要 QQ 浏览器内已登录的 QQ 账号；**QQ 客户端的登录不共享给浏览器** |
| 列表接口**剥图** | `get_hw_list.fcg` 只返回文字，图片作业仅显示「【图片】」 |
| 图片须走**详情接口** | `get_hw_detail.fcg` 才返回 `type:"img"` 与 `url` |
| 会话层**不可用** | CLI 1.5.4 与 QQ 浏览器 21.7 扩展的会话协议不兼容，**禁止调用 `browser_start_session`**，直接调业务命令 |
| 必须在**沙箱外**运行 | 浏览器命令需 `dangerouslyDisableSandbox: true`，否则安全删除机制 fail-closed |

> 接口细节、参数、返回结构见 [references/api.md](./references/api.md)。

---

## 登录态：三态判定与恢复（必须先看）

登录态是**本 skill 最高频的故障源**（2026-09-01～09-03 连续三天、每天至少一次）。
且存在**双向误判**：既可能「bkn 有值但其实没登录」，也可能「浏览器已登录但接口仍报错」。

### 为什么 bkn 不可信

`bkn` 由 cookie 里的 `skey` 算出。**只要 cookie 没过期就一定能算出来**，
而 cookie 过期时间远长于 `ptlogin` 会话有效期。所以：

- 会话失效后，`bkn` 仍能正常输出，且**数值往往与失效前完全相同**（实测 689439289 前后不变）
- 只有**详情接口**（`get_hw_detail.fcg`）会暴露问题；列表接口校验较松，照常返回数据

### 三态判定表

| # | `bkn` | `day --refresh` | 登录页 innerText | 判定 | 处理 |
|---|-------|-----------------|------------------|------|------|
| 1 | ✅ 有值 | ✅ 成功 | （已跳转群管理页） | **正常** | 直接生成文档 |
| 2 | ✅ 有值 | ❌ `verify fail` | `QQ群 / QQ登录` | **真的没登录** | 引导用户登录 → **重探 bkn** → 再拉数据 |
| 3 | ✅ 有值 | ❌ `verify fail` | 已跳转（有昵称 +「退出」） | **已登录，但 bkn 缓存过期** | **只需重探 bkn**，不用再登录 |

> 第 3 态是最隐蔽的：用户明明点了登录，命令却照样报 verify fail，
> 极易误判成「登录没生效」而让用户反复登录。

### 判定命令

```bash
# ① 接口侧：详情接口是否报错（先重试一次再下结论，避免偶发抖动）
python scripts/qq_hw.py day <日期> --refresh

# ② 浏览器侧：直接看登录页（判定第 2/3 态的唯一可靠依据）
qqbrowser-skill browser_go_to_url --url "https://qun.qq.com/#/login"
qqbrowser-skill browser_eval_content_js --script "document.body.innerText.slice(0,300)"
```

**innerText 判读**：
- `QQ群 / QQ登录` → **未登录**（第 2 态）
- 自动跳转到 `https://qun.qq.com/#/member-manage/base-manage`，含昵称与「退出」按钮 → **已登录**（第 3 态）

### 🔑 关键动作：登录后必须先重探 bkn

用户点完登录后，`qq_hw.json` 里缓存的仍是**旧会话的 bkn**，而 skey 已经变了。
**不重探就去拉数据，必然再次 verify fail。**

```bash
# 用户点登录 → 先刷新 bkn（数值会变化，如 689439289 → 196315760）→ 再拉数据
python scripts/qq_hw.py bkn --gid <群号>
python scripts/qq_hw.py day <日期> --refresh
```

### 失效的时间规律（实测）

- 登录态会**多次失效**，不是一天只发生一次
- 也会在**工作窗口中途掉线**（16:17 正常 → 17:19 失效 → 重新登录后 18:08 又正常）
- 因此定时任务**每一轮都要重新校验登录态**，不能凭上一轮的结果推断

---

## 流程

### 0. 环境准备（首次）

```bash
# 1. 先比对官方源与本地镜像源版本，避免镜像滞后装到旧版（旧版协议不兼容）：
pip index versions qqbrowser-skill --index-url https://pypi.org/simple   # 官方源最新版
pip index versions qqbrowser-skill                                        # 本地镜像源版本
# 2. 按比对结果安装：
#    - 两源版本一致 → 用本地镜像源：  pip install --upgrade qqbrowser-skill
#    - 版本不一致   → 用官方源：    pip install --index-url https://pypi.org/simple --upgrade qqbrowser-skill
#    - 安装失败     → 改用阿里云源：pip install --index-url https://mirrors.aliyun.com/pypi/simple/ --upgrade qqbrowser-skill
qqbrowser-skill install          # 安装/校验 QQ 浏览器本体
pip install python-docx pillow   # 文档生成依赖

qqbrowser-skill serve --daemon   # 启动 daemon
qqbrowser-skill status           # 确认 Daemon is running 且 Connected clients: 1
```

> **CLI 不在 PATH 时（隔离 venv 安装的常见情况）**：`qq_hw.py` 默认用 `qqbrowser-skill`，
> 找不到会抛 `FileNotFoundError: [WinError 2]`。先用 `QQB_CLI` 环境变量指向可执行文件绝对路径，
> 例如本机：
> ```bash
> QQB_CLI="C:/Users/<你的用户名>/.workbuddy/binaries/python/envs/default/Scripts/qqbrowser-skill.exe" \
>   python scripts/qq_hw.py bkn --gid <群号>
> ```
> daemon 刚启动时 `Connected clients` 可能为 0（扩展还没连上），**等变为 ≥1 再探测 bkn**，
> 否则会误判成「未登录」。首次探测失败可先重试一次再下结论。

### 1. 探测 bkn 并确认登录 ⏸️ **需人工介入**

```bash
python scripts/qq_hw.py bkn --gid <群号>            # 单群
python scripts/qq_hw.py bkn --gid <群号1>,<群号2>   # 多群（逗号分隔）
```

- 成功 → 输出 `bkn = xxxxx`，自动写入 `qq_hw.json`（`--gid` 支持逗号分隔多群）
- 提示未探测到 bkn → **浏览器内未登录 QQ**：
  1. 告知用户："请在弹出的 QQ 浏览器窗口中登录 QQ（扫码即可）"
  2. **保持会话等待，不重试、不切换方案**
  3. 用户确认登录后，**先重新执行本命令刷新 bkn**，再拉数据

> ⚠️ 本节最容易被误判，详见下方「[登录态：三态判定与恢复](#登录态三态判定与恢复必须先看)」。
> 核心结论：**`bkn` 探测成功 ≠ 已登录**；反过来，**浏览器已登录也仍可能 verify fail**（bkn 缓存没刷新）。

### 2. 拉取作业列表

```bash
python scripts/qq_hw.py list --size 100      # → hw_list.json
```

### 3. 拉取指定日期详情（含图片 URL）

```bash
python scripts/qq_hw.py day 2026-05-11       # → hw_day_2026-05-11.json
```

列表过期时加 `--refresh`。

> ⚠️ 若接口返回 `ptlogin-ex verify fail`（retcode 2001），先按上方
> 「[登录态：三态判定与恢复](#登录态三态判定与恢复必须先看)」排查，不要直接认定未登录。

> 📌 **老师用「消息」而非「群作业」布置科目时，接口拉不到**（2026-09-01 数学作业即如此）。
> 处理方式：让用户把内容发来，**手动补一条**进 `hw_day_<日期>.json`，再直接跑 `docx`：
> ```json
> {
>   "id": "<自拟唯一 id>", "title": "X月X日XX作业", "ts": <Unix 秒>,
>   "course": "<科目>", "pub": "<发布人>", "fbname": "<昵称>",
>   "group_id": "<群号>", "manual": true,
>   "c": [{"t": "str", "s": "1. xxx\n2. yyy"}]
> }
> ```
> ⚠️ `ts` 要插在已有条目之间以保持时间顺序。
> ⚠️ **补完后千万不要再跑 `day --refresh`**，否则整份 JSON 被覆盖、手动补的内容丢失。

### 4. 生成 docx（支持多群 / 筛选 / 文字版 / 多页）

```bash
python scripts/qq_hw.py docx 2026-05-11                     # 默认：单页、全部科目、含图片
python scripts/qq_hw.py docx 2026-05-11 --courses 语文,数学 # 仅指定科目
python scripts/qq_hw.py docx 2026-05-11 --text-only         # 仅文字版（不插图）→ 作业_2026-05-11_文字版.docx
python scripts/qq_hw.py docx 2026-05-11 --allow-multi       # 允许分页（内容过多时）
```

| 参数 | 说明 |
|------|------|
| `--courses 语文,数学` | **科目筛选**（逗号分隔）；默认当天全部科目 |
| `--text-only` | **仅文字版**，跳过图片下载与插入 |
| `--allow-multi` | **允许多页**：内容过多放不下一页时使用，**必须先征得用户同意** |
| `--scale N` | 单页模式下压缩图片高度的系数（>1 更保守） |

> 多页逻辑：默认仍按单页排版。若 `pages` 校验发现 >1 页，**先询问用户是否允许多页**；
> 用户同意后再加 `--allow-multi` 重新生成（图片按自然高度排，允许分页）。

### 4.5 转为 PDF（**发送默认用 PDF**）

PDF 是 Epson 等打印邮箱最稳的格式。**默认一律把作业以 PDF 附件发送**，docx 仅作本地留存
（打印前记得提醒用户在打印服务里设为「**只打印附件**」，见下方「打印省纸提醒」）。

**两级生成策略（按优先级）**：
1. **优先**调用**本地已安装的 PDF 转换 skill**（如 `pdf`、`pdfkit-py` 等）做 docx → PDF；
   它是纯 Python 方案、不依赖本机 Word、跨机器更稳。
2. 本地 PDF skill **不可用或转换失败**时，**回退**到脚本内置的 Word COM 方案：

```bash
python scripts/qq_hw.py pdf 2026-05-11      # → 作业_2026-05-11.pdf（Word COM 回退）
```

> Word COM 方案的中文路径坑（直接 SaveAs 中文名被静默吞、8.3 短路径等）见
> troubleshooting.md §10。docx 单页则 PDF 也单页，页数以步骤 5 校验 docx 为准。

### 5. 校验页数（**必做**）

```bash
python scripts/qq_hw.py pages 作业_2026-05-11.docx
```

- `PAGES=1` → 完成
- `PAGES=2` → 加大 `--scale`（默认 1.15，试 1.3～1.5）后重新生成：

```bash
python scripts/qq_hw.py docx 2026-05-11 --scale 1.4
```

---

## 排版规范

| 元素 | 规范 |
|------|------|
| 文首 | 日期标题，居中，微软雅黑 14pt |
| 每条作业 | **Heading 2**，微软雅黑 13pt；**仅保留科目名**——去掉 `^\d{1,2}月\d{1,2}日` 前缀，**不加编号**、**不显示发布人昵称**（多群时保留「（群xxx）」标注） |
| 具体内容 | **编号列表 + 正文样式 + 宋体 10.5pt**；剥掉原文自带的 `1. 2. 3.` 前缀，**每条作业独立编号（从 1 开始）**——手工编号 + 悬挂缩进（避免 Word「List Number」跨科目连续计数） |
| 图片 | **竖图（宽<高）两两横排**，横图单独成行 |

**单页约束的关键**：必须在**样式层**把 `Normal / Heading 2 / List Number` 的
`space_before/after` 归零、`line_spacing` 设为 1.0（样式自带 1.15 倍行距会撑到第二页）；
页边距 0.8cm；表格单元格边距清零。

---

## 发送

### 邮箱（Agent Mail 连接器）

🚨 **第一步必须用精确名加载工具**（2026-09-02 踩坑修正）：MCP 工具是**延迟注册**的，
用 `ToolSearch(queries=[...])` **模糊搜索搜不到 `mcp__agent-mail__*`**（只能搜到内置的
`agent_mail_upload_attachment` / `agent_mail_download_attachment`），会误判成「没有发信工具」。
正确做法：

```
ToolSearch(tool_names=["mcp__agent-mail__SendMessage", "mcp__agent-mail__GetMe"])
```

拿到 schema 后再 `DeferExecuteTool("mcp__agent-mail__SendMessage", {...})`。
**不要**再去 app.asar 里翻 HTTP 端点——本机没有对应的本地 HTTP 服务，纯属浪费时间。

调用序列：

```
1. agent_mail_upload_attachment(file_path)          →  file_id
2. mcp__agent-mail__SendMessage(
     to=[{"email": "<打印邮箱>"}],                  # 注意是对象数组，不是字符串数组
     subject="作业_<日期>",
     body=" ",                                      # 空字符串会校验失败，传一个空格
     file_refs=[{"file_id": "<上一步的 file_id>"}],
     skip_confirmation=true                         # 仅当用户已预先授权
   )                                                →  {"queued": true}
3. 可选校验：mcp__agent-mail__ListMessages(dir="sent", limit=1)
```

⚠️ 未经用户明确授权时**不要**传 `skip_confirmation`：`SendMessage` 会返回
`CONFIRMATION_REQUIRED`，此时**必须先向用户展示收件人 / 主题 / 附件并征得明确同意**，
再带 `confirmation_token` 重试。定时任务等无人值守场景由用户预先授权，可直接 skip。

账号上下文（`mcp__agent-mail__GetMe`）可查别名、scopes（需含 `mail:send`）、
日发送配额（50/天）、附件上限（单文件 20MB）。

**回退通道：企业微信邮件** `wecom-cli mail send`（先加载 `wecomcli-email` skill）:

```bash
wecom-cli mail send --json '{
  "to": {"emails": ["<打印邮箱>"]},
  "subject": "作业_<日期>",
  "file_path": "<正文 .md 绝对路径>",
  "content_type": "markdown",
  "attachments": [{"file_path": "<PDF 绝对路径>"}]
}'
```

- 正文想留空就把 `.md` 写成**一个空格**（空字符串会被接口判校验失败）。
- 附件路径含中文时先 `cp` 成 ASCII 文件名再传，更稳。
- 当前该通道返回 **850003 授权过期**（机器人「邮件」权限过期，与消息权限是两套），
  需用户在企微「工作台 → 智能机器人」给机器人重新授权邮件权限。
- 两条通道都不通时：**不要写已发送标记**，只发企微告警 + 保留现场文件，等下次调度重试。

🖨️ **打印省纸提醒（重要）**：Epson 等打印邮箱默认会**连邮件正文一起打印**，
常常多出一张只写了两行说明的纸。发送前应提醒用户在打印服务（如 Epson Connect）的
打印设置里勾「**只打印附件 / 不打印正文**」，或把邮件正文留空、尽量简短。
这样每份作业只出 1 页，避免浪费纸张。

### 微信（企业微信 wecom 连接器）

加载 `wecomcli-message` skill 发送消息；需先上传文件时用 `wecomcli-media` 换取 media_id。

> ⚠️ **`sessions list` 经常返回 `sessions_count: 0`**（本机连续多日为 0）。
> 此时按 skill 规则兜底：用 `wecom-cli identity whoami` 返回的**授权真人用户 ID** 作为 `chat_id`
> 发给用户本人，不要因为「找不到「本地助理」会话」就放弃推送。

---

## 无人值守定时任务（自动化运维要点）

本节是 2026-09-01～09-03 每天定时跑通「群作业 → PDF → 打印邮箱」沉淀出的经验。

### 调度窗口要收窄

❌ 反例：`FREQ=HOURLY` 全天跑 —— 累计空转 **42+ 次**（凌晨、上午全在跑，纯浪费）。

✅ 正解：直接把时段写进 rrule，让闸门只在真正需要的时间被触发：

```
FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15,16,17,18;BYMINUTE=0,30
```

> 即使 rrule 已限定，仍建议在任务 prompt 里保留一道**时间窗闸门**（第 0 步），
> 双保险避免边界情况空跑。

### 幂等标记（必做）

发送成功后**立即**在工作区写 `hw_auto_sent_<日期>.flag`，下一轮开头检查到就跳过。
这让截止时间之后的重复调度天然安全，**也避免同一天重复打印**。

```
检查 hw_auto_sent_<TODAY>.flag → 存在即直接结束，不拉作业、不发邮件、不推送
```

### 失败时不要写标记

两条邮件通道（Agent Mail / 企微邮件）**都不通时，绝不写已发送标记**；
只发企微告警 + 保留现场文件（`作业_<日期>.pdf` / `.docx`），等下一轮重试。
写了标记会导致当天再也发不出去。

### 缺科兜底策略

三科（语文/数学/英语）未集齐时的推荐策略：

| 条件 | 行为 |
|------|------|
| 缺科 且 未到截止时间 | **不发送**，推送「已收到 XX，仍缺 XX，XX 点前每半小时复查」 |
| 缺科 且 已到截止时间 | 按**已收到科目强制生成发送**（需用户预先授权），**主题与推送里标注缺科** |
| 当天一条作业都没有 | 不发送，推送说明 |

强制发送时 `--courses` 只传已收到的科目，主题形如 `作业_2026-09-03（缺英语）`。

### 每轮都要重新校验登录态

登录态会在窗口中途掉线，**不能凭上一轮成功就跳过本轮校验**（见上方三态判定）。

### 打印省纸

Epson 打印邮箱会连正文一起打印 → 多打一张纸。
**邮件正文留空（传一个空格）**，并提醒用户在打印服务里勾「只打印附件」。

---

## 脚本

`scripts/qq_hw.py` 单入口，子命令：`bkn` / `list` / `day` / `docx` / `pdf` / `pages`。
`bkn`/`list`/`day` 的 `--gid` 支持**逗号分隔多群**；`docx` 支持 `--courses`（科目筛选）、
`--text-only`（仅文字）、`--allow-multi`（多页）。
多群数据**自动按（群号, hw_id）去重**，避免同群号重复拉取产生重复条目。
`scripts/count_pages.ps1` 供 `pages` 子命令调用（需本机装有 Word）。

## 示例 Prompt

- 「把 <群号> 群 5月14日的作业整理成 Word，一页，发到我邮箱 xxx@xx.com」
- 「帮我把 QQ 群里今天的作业导成文档，图片要保留，然后微信发给我」
- 「某天的作业文档超过一页了，把图片缩小点重新生成」
- 「把 <群号1> 和 <群号2> 两个群今天的作业一起整理成一份 Word」
- 「只要今天语文和数学的作业，生成文字版（不要图片）」
- 「作业太多了放不下一页，帮我生成多页的版本」

## 故障排查

见 [references/troubleshooting.md](./references/troubleshooting.md)，覆盖：
会话协议不兼容、pip 镜像滞后、CLI 输出双重转义、Word COM 页数统计、单页约束失效、
**登录态三态判定**、**MCP 工具延迟注册**、**定时任务运维**等。
