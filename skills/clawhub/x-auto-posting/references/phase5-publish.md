# Phase 5 Reference — 发布执行

## TOC

- §1 Content Verification Gate（发布前强制检查）
- §2 导航到 compose
- §3 填写正文
- §4 上传图片 / 视频（可选）
- §5 发布前截图确认
- §6 点击发布与 tweet_id 捕获
- §7 发布记录写入
- §8 已知陷阱

---

## §1 Content Verification Gate

发布前执行以下检查，**任意一项不通过，禁止发布，提示用户修正**：

| 检查项 | 通过条件 |
|--------|----------|
| 字符数 | `x_char_count(text) <= 280`（算法见 `phase4-writing.md §2.1`） |
| 正文非空 | `len(text.strip()) > 0` |
| 正文不含 http:// | 全部外链必须 https |
| 正文不含联系方式 | 不含微信号、手机号（`[+]?\d{8,}`）、WhatsApp/Telegram/QQ 号 |
| Hashtag 数量 | 最多 2 个（`#\w+` 计数） |
| Mention 数量 | 最多 1 个（`@\w+` 计数；回复场景例外） |
| 媒体路径（带图时） | 文件存在且大小 ≤ 5MB（图片） / 512MB（视频） |

检查通过后方可执行 §2。

---

## §2 导航到 compose

```bash
browser-act --session <session_name> network clear
browser-act --session <session_name> navigate "https://x.com/compose/post"
browser-act --session <session_name> wait stable
```

**为什么用 `/compose/post` 而非 home 内联 compose？**
- 内联 compose 与背景 timeline 共享同一个 `tweetTextarea_0`，事件分发容易被 timeline 的 React 子树抢走
- `/compose/post` 打开的是独立模态，`[role="dialog"][aria-labelledby="modal-header"]` 内的 compose 状态隔离更干净
- 关闭模态只需 `browser-act back` 或 `browser-act navigate x.com/home`

**脚本如何区分两个 compose**：`scripts/fill-compose.py` 和 `scripts/clear-compose.py` 内部都是先遍历所有可见 `[role="dialog"]`，找到其中的 `tweetTextarea_0`，找不到才回退到全局选择器。

---

## §3 填写正文

### 3.1 主路径 — CDP 键盘输入

X compose 使用 Draft.js。它的 `EditorState` 只接受真实键盘事件，不响应 `execCommand('insertText')` 或合成 `beforeinput`/`input` 事件（这些在 DOM 层写入会被 Draft.js 的下一轮渲染覆盖，Post 按钮保持 disabled）。唯一可靠的路径是 CDP 键盘协议，即 `browser-act input`。

```bash
# Step 1：获取 compose 索引
browser-act --session <session_name> state
# 输出中找类似下面这行：
#   *[8]<div aria-label=Post text role=textbox required=false />
# 索引会随页面变化，每次填写前现取

# 自动化提取索引（bash / Git Bash — 不使用 -P 以兼容 Windows 的 unibyte locale）：
IDX=$(browser-act --session <session_name> state 2>&1 \
    | grep "Post text role=textbox" \
    | sed 's/.*\[\([0-9]*\)\].*/\1/' | head -1)

# PowerShell：
$IDX = (browser-act --session <session_name> state 2>&1 `
    | Select-String 'Post text role=textbox') `
    -replace '.*\[(\d+)\].*','$1' | Select-Object -First 1
```

```bash
# Step 2：click 聚焦 + input 输入（必须分两步）
COMPOSE_IDX=8    # 从 step 1 解析得出
browser-act --session <session_name> click $COMPOSE_IDX
# 短暂停顿（约 200-500ms）让焦点落定，避免下一步首字符丢失
browser-act --session <session_name> input $COMPOSE_IDX "<TWEET_TEXT>"
```

**关于首字符丢失**：`click` 和 `input` 合并到一条 `&&` 连续执行时，`browser-act input` 内部会先 click 再 type，与 step 2 的 click 冲突，可能丢第一个字符。分开两步 + 一点等待可减少发生概率但不能完全消除。稳妥做法：

1. 分两步执行（`click` 独立一行，`input` 独立一行）+ 约 1 秒等待
2. 传入文本时在最前面多加一个字符（如一个空格或 `.`）作为"炮灰位"
3. 填完后再通过 `verify-post-ready.py` 返回的 `compose_text` 核对，发现缺失则 `clear-compose.py` + 重填一次

Phase 5 §1 Content Gate 已按 `x_char_count(text) <= 280` 验证原文；`input` 步骤前加的炮灰字符不计入 Gate，但会占用 Draft.js 的字符计数。如果原文已接近 280，炮灰会顶到上限，这时采用方案 (3) 的"重填"而非方案 (2)。

```bash
# Step 3：验证 Draft.js 已接收 + Post 按钮 enabled
python scripts/verify-post-ready.py | browser-act --session <session_name> eval --stdin
```

返回：

```json
{
  "compose_text": "<TWEET_TEXT>",
  "compose_length": 217,
  "post_enabled": true,
  "post_button_found": true,
  "media_attached": 0
}
```

**Gate**：
- `post_enabled` 必须为 `true` 才可继续
- `compose_text` 应与传入文本一致（允许末尾一个换行差异）
- `compose_length` 与 `x_char_count(text)` 对比——Draft.js 报的 length 可能与 X 的 280 字符算法不同（URL 按 23 计数），以 `verify-post-ready.py` 的 `compose_length` 仅作辅助，字符限超标由 §1 Content Gate 提前拦住

**Gate 失败应对**：
- `post_enabled=false` 且 `compose_text` 正确 → 不在 `/compose/post` 模态内；重新 `browser-act navigate "https://x.com/compose/post"` 后重试 step 1-3
- `post_enabled=false` 且 `compose_text` 缺字符 → CDP 键盘事件未全部落到正确元素；`scripts/clear-compose.py` 清空后重新 step 2
- `post_enabled=false` 且 `compose_length > 280` → 文本超长被 X 自动禁用，回 Phase 4 改稿

### 3.2 辅助：含换行或特殊字符的文本

`browser-act input` 的命令行参数 `"<TWEET_TEXT>"` 使用 shell 引用传递，对多行文本需要小心：

- Windows PowerShell：`browser-act input 8 @'...'@`（here-string）或分多次 input 拼接
- bash：`browser-act input 8 "$(cat text.md)"` 可直接传入文件内容

如果使用 shell here-string 仍有引号转义问题，**拆成多段 input**：

```bash
browser-act --session <session_name> input 8 "第一段文字"
browser-act --session <session_name> keys "Enter"
browser-act --session <session_name> input 8 "第二段文字"
```

### 3.3 不使用的 JS 路径（仅诊断）

`python scripts/fill-compose.py` 通过合成事件写入 compose。**Draft.js 当前版本不认**，会导致 Post 按钮保持 disabled。该脚本保留用于：
- 验证 DOM 定位逻辑（compose textarea 是否找得到）
- 未来 X 换掉 Draft.js 时作为候选路径

任何 Phase 5 正式流程**都不要**依赖 `fill-compose.py` 作为主入口。

---

## §4 上传图片 / 视频（可选）

仅当 draft 标记了 `media_path` 时执行。

### 4.1 注入文件

```bash
python scripts/inject-media.py "/absolute/path/to/cover.png" | browser-act --session <session_name> eval --stdin
```

返回：

```json
{
  "injected": true,
  "filename": "cover.png",
  "mime": "image/png",
  "size_bytes": 102400,
  "preview_visible": true
}
```

**等待媒体处理完成**：

```bash
browser-act --session <session_name> wait --selector '[data-testid="attachments"] img' --state attached --timeout 15000
```

对于视频，X 需要在服务端完成转码后 Post 按钮才可用。若 `post_enabled` 在填入视频后变为 `false`，再等待 10-30 秒后重检。

### 4.2 图片 / 视频格式限制

| 类型 | 允许扩展名 | 单文件上限 | 备注 |
|------|------------|------------|------|
| 图片 | jpg / jpeg / png / webp | 5 MB | 单推文最多 4 张 |
| GIF | gif | 15 MB | 单推文最多 1 张 |
| 视频 | mp4 / mov | 512 MB | 时长 ≤ 140s（免费账号） |

超限文件 X 会静默拒绝（`preview_visible: false` 且 `post_enabled` 不翻 true）。压缩后重试。

### 4.3 多张图片

需要传 2-4 张时，分次调用脚本，每次传一个 path。两次之间等待 1-2 秒以免事件合并导致丢失。

---

## §5 发布前截图确认

```bash
browser-act --session <session_name> screenshot "workspaces/x-posting/<date>/drafts/<slug>/pre_publish.png"
```

向用户展示截图路径并调用 AskUserQuestion 工具：

```
发布前确认截图已保存：workspaces/x-posting/<date>/drafts/<slug>/pre_publish.png
- 正文是否与预期一致？
- 图片/视频是否正确显示？
- Post 按钮是否为可点击的深色状态？

选项：
- confirm — 点击发布
- abort — 取消发布，保留为草稿
- edit — Other 提供修改指令，回到 Phase 4
```

用户选 `confirm` 才进入 §6。

---

## §6 点击发布与 tweet_id 捕获

### 6.1 点击发布

```bash
browser-act --session <session_name> network clear  # 清空流量记录方便捕获 CreateTweet
python scripts/click-post.py | browser-act --session <session_name> eval --stdin
browser-act --session <session_name> wait stable --timeout 15000
```

### 6.2 从 CreateTweet 响应提取 tweet_id

```bash
browser-act --session <session_name> network requests --type xhr,fetch --filter CreateTweet --method POST --format json > tmp/create_reqs.json

REQ_ID=$(python -c "import json; d=json.load(open('tmp/create_reqs.json','r',encoding='utf-8')); print([r['request_id'] for r in d['requests'] if 'CreateTweet' in r['url']][-1])")

browser-act --session <session_name> network request $REQ_ID --format json | python scripts/parse-create-tweet.py > tmp/new_tweet.json
```

返回：

```json
{
  "id": "2053123456789012345",
  "url": "https://x.com/SisilyNora/status/2053123456789012345",
  "author": "SisilyNora",
  "text": "...",
  "created_at": "Fri May 09 04:15:10 +0000 2026"
}
```

### 6.3 失败兜底

| 症状 | 可能原因 | 应对 |
|------|---------|------|
| CreateTweet 响应含 `errors` 且含 `"duplicate_tweet"` | X 近期发过同样内容 | 改写后重试 |
| `rest_id` 缺失 | 推文被 shadowban / 风控隐藏 | `browser-act navigate https://x.com/{handle}` 检查自己主页是否可见；若可见，手动补录 tweet_id |
| 无 CreateTweet 请求 | Post 按钮未真正触发 | 检查 click 返回；`browser-act screenshot` 确认页面状态 |
| CreateTweet 返回 403 / 429 | 触发风控 | **立即停止本次 run**，记录到 `workspaces/x-posting/tracking/incidents.log`，等待至少 24h 再恢复发帖 |

---

## §7 发布记录写入

### 7.1 更新 `published.json`

追加到 `workspaces/x-posting/tracking/published.json`：

```json
{
  "id": "2053123456789012345",
  "url": "https://x.com/SisilyNora/status/2053123456789012345",
  "text": "...",
  "char_count": 217,
  "has_media": true,
  "media_paths": ["/abs/path/to/cover.png"],
  "source_topic_id": "2045568934254960835",
  "source_topic_url": "https://x.com/ctatedev/status/2045568934254960835",
  "keyword": "browser automation",
  "published_at": "2026-05-09T04:15:10Z",
  "status": "published",
  "tracking": {
    "metrics_24h": null,
    "metrics_7d": null,
    "last_checked": null
  }
}
```

### 7.2 更新 `session_state.json`

```json
{
  "posting": {
    "daily_limit": 3,
    "min_interval_hours": 2,
    "last_posted_at": "2026-05-09T04:15:10Z",
    "today_count": 1
  }
}
```

`today_count` 以每日 00:00 本地时间归零（读取时比较 `last_posted_at` 与当前时间的日期）。

### 7.3 更新 keywords.json

Phase 1 记录的 `pending_keyword` 生效，`last_index += 1`（在文件级持久化）。

### 7.4 排程 24h 追踪

在对话中提醒用户：

```
发布成功：https://x.com/{handle}/status/{id}
24 小时后可运行 `/x-auto-posting 追踪效果` 查看初始数据。
如希望自动排程，可用 /schedule 定时执行。
```

---

## §8 已知陷阱

1. **Draft.js 不认合成事件**：`document.execCommand('insertText')` + `beforeinput`/`input` InputEvent 可以改 DOM，但 Draft.js `EditorState` 不更新，Post 按钮保持 disabled。必须用 CDP 键盘协议（`browser-act input`）才能让 Draft.js 接收文本。这是本 Skill Phase 5 §3 主路径的全部原因
2. **内联 compose vs 模态 compose 选择器冲突**：home 页同时存在两个 `tweetTextarea_0` 和两个 Post 按钮（inline 的 `tweetButtonInline` 和 modal 的 `tweetButton`）。验证按钮状态时必须定位到正确 scope（脚本 `verify-post-ready.py` 已处理，手写临时 JS 要注意）
3. **首字符丢失**：`browser-act input <N> "text"` 内部会先 click 再 type。如果目标元素没有事先被聚焦且 click+type 间隔太短，第一个字符可能丢。应对：先独立 `browser-act click <N>`，再 `browser-act input <N> "..."`，两步分开
4. **Offline 模式点击 Post**：HAR 离线捕获请求后恢复在线，X 的 retry 逻辑可能自动补发请求导致真实发布。处理：`network offline off` 后**立即 `navigate`** 到其他页面（如 `/home`），中断 retry
5. **`x-client-transaction-id`**：所有 GraphQL 写操作（CreateTweet、DeleteTweet）都需此签名头，且每请求动态生成。本 Skill 不重现该头，全部走"填表 + 点击"路径
6. **发布后页面不跳转**：X 在 compose 模态内发布成功后仅关闭模态，不导航到新推文。从 `CreateTweet` 响应中拿 ID 是唯一可靠方式，不要尝试从 `location.href` 解析
7. **视频转码延迟**：上传视频后 X 会在后台转码，期间 Post 按钮可能时而 enabled 时而 disabled。`wait --selector "[data-testid=attachments] video" --state attached` 确认预览显示再 click post
8. **Hashtag 下拉联动**：X compose 输入 `#` 后出现的 hashtag 建议下拉**不响应程序化输入**。直接在文本中嵌入 `#tagname` 即可，不要尝试触发下拉选择
9. **home 内联 compose 是折叠状态**：`/home` 右上角的 compose 框 Post 按钮**总是 disabled** 直到用户点击输入区激活——这是 X 的 UX，不是 bug。始终用 `/compose/post` 打开独立 modal 来发推
