# 匹配规则 & 评论 ID

## 评论 ID 格式

由 `fetch_comments.js` 注入 `data-comment-id` 锚点时生成。

| 类型 | 格式 | 示例 |
|---|---|---|
| 顶级评论 | `c<N>` | `c1`、`c2`、`c3`... |
| 二级回复 | `c<N>-r<M>` | `c1-r1`、`c2-r4`... |

`<N>` 是**顶级评论**的 1-based 序号，`<M>` 是该顶级评论下回复的 1-based 序号。每次 `fetchComments` 都会重置——切视频后会得到全新一套 ID。

## `--title` 匹配

实现在 `work-list-actions.js::clickWorkByName(page, name)`。

- 忽略大小写的**子串**匹配视频标题。
- 空标题（`hasTitle: false`）不参与匹配候选。
- 多条匹配时取第一条（默认 `index: 0`）。
- 零匹配时抛错，错误信息列出前 10 个可选标题。

## `author` + `content` 匹配（`--reply` 用）

实现在 `process_one_video.js::reply()`。

对回复列表里的每条，匹配器：

1. **同时扫顶级评论和它们的二级回复**。
2. 保留同时满足以下条件的候选：
   - `user.name` 包含 `author`（子串匹配，当前实现区分大小写）
   - `content` 包含 `content`（子串匹配）
3. **0 候选** → 该条目记 `reason: "not-found"`。
4. **>1 候选** → 该条目记 `reason: "ambiguous"`，`candidates` 列出所有匹配。
5. **1 候选** → 发回复（直接发送，无 dry-run 中间步）。

### 实操要点

- `author` 匹配的是**显示名**，抖音上常带 `\n` 或奇怪后缀。**用稳定前缀**（前 2~4 个字）而不是完整名字。
- `content` 匹配的是**评论正文**（可能含换行），挑一句独特的短语。
- 如果收窄不到一条，先跑 `--comment-list` 拿到所有评论 ID，再挑特定 ID——这时 agent 自己写一段调用 `scripts/reply_comment.js::replyToComment` 的小脚本按 `id` 直接发（绕过 author/content 匹配）。

## 防爬间隔语义

`--delay-ms` 是 `--reply` 一次调用中**多条回复之间**的间隔。**首条不等待**。

- 默认 5000 ms 对个人低频使用足够安全。
- 创作者回复自己评论区的反爬较松，多数场景不需要加大。
- 设太大（>30 秒）会让单次 `--reply` 运行很长——但 `waitForLogin` 的 5 分钟超时是**每次脚本调用**计的，不是每条回复计的，单次长跑不受影响。