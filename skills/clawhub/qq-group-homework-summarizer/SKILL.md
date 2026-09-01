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

### 1. 探测 bkn 并确认登录 ⏸️ **需人工介入**

```bash
python scripts/qq_hw.py bkn --gid <群号>            # 单群
python scripts/qq_hw.py bkn --gid <群号1>,<群号2>   # 多群（逗号分隔）
```

- 成功 → 输出 `bkn = xxxxx`，自动写入 `qq_hw.json`（`--gid` 支持逗号分隔多群）
- 提示未探测到 bkn → **浏览器内未登录 QQ**：
  1. 告知用户："请在弹出的 QQ 浏览器窗口中登录 QQ（扫码即可）"
  2. **保持会话等待，不重试、不切换方案**
  3. 用户确认登录后，重新执行本命令

### 2. 拉取作业列表

```bash
python scripts/qq_hw.py list --size 100      # → hw_list.json
```

### 3. 拉取指定日期详情（含图片 URL）

```bash
python scripts/qq_hw.py day 2026-05-11       # → hw_day_2026-05-11.json
```

列表过期时加 `--refresh`。

> ⚠️ 若接口返回 `ptlogin-ex verify fail`（retcode 2001），说明**尚未在
> https://qun.qq.com/#/login 完成登录**。脚本会**自动打开该登录页并弹出醒目提示**，
> 让你在 QQ 浏览器窗口中点击「登录」；登录成功后再重新执行本命令即可。
> （列表接口校验较松仍可用，但详情接口需要登录态才能返回图片。）

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

```
1. mcp__agent-mail__upload_attachment(file_path)  →  file_id
2. mcp__agent-mail__SendMessage(to, subject, body, file_refs=[{file_id}])
```

⚠️ 发信会返回 `CONFIRMATION_REQUIRED`：**必须先向用户展示收件人 / 主题 / 附件并征得明确同意**，
再带 `confirmation_token` 重试。**严禁未经确认自动发送。**

🖨️ **打印省纸提醒（重要）**：Epson 等打印邮箱默认会**连邮件正文一起打印**，
常常多出一张只写了两行说明的纸。发送前应提醒用户在打印服务（如 Epson Connect）的
打印设置里勾「**只打印附件 / 不打印正文**」，或把邮件正文留空、尽量简短。
这样每份作业只出 1 页，避免浪费纸张。

### 微信（企业微信 wecom 连接器）

加载 `wecomcli-message` skill 发送消息；需先上传文件时用 `wecomcli-media` 换取 media_id。

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
会话协议不兼容、pip 镜像滞后、CLI 输出双重转义、Word COM 页数统计、单页约束失效等。
