# 故障排查

## 按退出码 / 现象分桶

### `Error: exit(2)`（浏览器启动前的 stderr）

CLI 参数错。脚本 exit(2) 并往 stderr 打原因。常见：

| stderr 包含 | 修复 |
|---|---|
| `未知参数: <flag>` | 检查拼写，参考 [cli.md](cli.md) 找合法 flag |
| `必须指定 --comment-list 或 --reply` | 加动作 flag |
| `--title <视频名> 是必需的` | 加 `--title "<视频标题>"` |
| `--reply 必须配合...` | 加 `--replies-file` / `--replies` / `--author+--content+--text` 任一 |
| `回复列表来源互斥` | 一次只能用一个来源 flag |
| `--replies-file 文件不存在` | 检查路径，Windows 用 `.\replies.json` 别用 `/replies.json` |
| `--replies 不是合法 JSON` | PowerShell 用**单引号**包 JSON：`--replies '[{...}]'` |
| `replies[<i>] 字段缺失或类型错误` | `author/content/text` 三字段必须都是**字符串** |

### 卡登录 5 分钟后报错

`waitForLogin()` 轮询「选择作品」按钮。失败 = 要么没登录，要么页面不对。

1. **Chromium 窗口里是否登录了抖音创作者中心？**
   看持久化 profile 目录 `<SKILL_DIR>/scripts/user-data/`。从没登录过的话，浏览器会停在登录页。
2. **页面是不是对的？**
   需要的 URL 是 `https://creator.douyin.com/creator-micro/interactive/comment`。
   如果停在 dashboard，左侧导航点「互动管理 > 评论管理」。
3. **按钮文字变了？**
   选择器是 `getByRole('button', { name: '选择作品' })`。如果抖音改了文案，改 `scripts/work-list-actions.js::waitForLogin()`。

### 回复 `reason: "not-found"`

0 条评论匹配 `author + content`。

1. 先跑 `node index.js --comment-list --title "..."`。
2. 找到目标评论，复制**完整**的 `user.name` 和一段内容片段。
3. 更新回复条目。**提示**：`user.name` 里可能有不可见的 `\n` 或其它字符——复制稳定前缀而不是整名。

### 回复 `reason: "ambiguous"`

多条评论匹配。JSON 里有 `candidates` 数组，每条带 id / level / user / content。

选项：
- 收窄关键词（更具体的 `author` 或 `content`）。
- 如果候选都是同一个作者但内容片段不同，给 `content` 加更多字。
- 想无视关键词直接回某条指定评论——agent 自己写一段调用 `scripts/reply_comment.js::replyToComment` 的小脚本按 `id` 直接发（绕过 author/content 匹配）。

### 回复 `reason: "toolbar-failed" / "input-failed" / "send-failed"`

打开工具栏 / 输入 / 发送时的 DOM 层错误。`detail` 通常会指明失败步骤，`screenshot` 字段给 PNG 路径方便看图。

常见原因：
- **回复过程中页面滚动或刷新**（网络抖动）。重试即可。
- **连续多条触发反爬**。加大 `--delay-ms`。
- **DOM 结构变了**（抖音更新）。看截图——如果工具栏 / 输入框 / 发送按钮长得不一样，可能需要更新 `scripts/selectors.js` / `scripts/reply_comment.js` 里的选择器。

### 回复成功但页面看不到

抖音创作者中心的评论列表更新很懒。再跑一次 `--comment-list` 或手动刷新浏览器标签。回复其实发出去了（看 JSON 的 `ok: true` 和 `target_id`）。

### 找不到 playwright 模块

```
Error: Cannot find module 'playwright'
```

在 skill 目录装：

```bash
cd <SKILL_DIR>/scripts
npm install
npx playwright install chromium
```

### 浏览器起不来（沙箱 / 系统问题）

- Windows：确认 Edge / Chromium 能正常起。
- Linux：`npx playwright install --with-deps chromium`。
- macOS：先 `xcode-select --install`，再 `npx playwright install chromium`。
- Headless 问题：CLI 默认 `headless: false`（需要看到浏览器才能登录）。如果非要 headless，改 `scripts/index.js` 里 `chromium.launchPersistentContext(..., { headless: false })` → `true`。

## 自动回复工作流相关问题

### 「对作品"xxx"自动回复」时漏回某些评论

按 [auto-reply-workflow.md](auto-reply-workflow.md) 的算法逐条核对：
- 顶级评论漏回 → 检查是否误判了"作者已回过"。必须用 `reply_to === null` 且 `time >= top.time` 判断，**不能用 `top.replies[]` 是否非空**
- 二级回复漏回 → 检查是否误判。必须用 `reply_to === r.user.name` 且 `time >= r.time` 判断
- 时间解析错 → `"06月07日 17:06"` 解析成 Date 时注意中文月份字符

### 「对作品"xxx"自动回复」时重复回复了

多半是：
- 时间对比漏掉，作者回复时间 < 评论时间也被判为"已回复"
- 抓评论后又跑了独立的 `--reply` 命令两次

工作流本身**保证不重复**（步骤 2 筛出的 target 是 agent 生成的确定列表，规则筛过的）。

### 规则判断错了，导致重复回复

skill 不再有人工审批节点，规则判断错了会**直接**重复回复。如果发生：
- 重新跑步骤 1 抓评论，确认 author/content 关键词没撞到作者已回复的评论
- 必要时手动从抖音端删除重复回复

## 数据落盘位置

- **`<SKILL_DIR>/scripts/user-data/`** — Chromium 持久化 profile（cookies、localStorage）。删了它会强制重新登录。
- **不写结果文件** — JSON 返回只走 stdout。

## 何时让用户介入

| 情况 | 用户操作 |
|---|---|
| 持续登录超时 | 手动登录、确认 URL、重试 |
| 弹窗 / 提示框挡住交互 | 在浏览器里手动关掉 |
| 多账号 / 不同创作者 | 每个账号用独立的 `user-data/`——复制整个 `scripts/` 目录到独立 skill 实例，分别 install / login |