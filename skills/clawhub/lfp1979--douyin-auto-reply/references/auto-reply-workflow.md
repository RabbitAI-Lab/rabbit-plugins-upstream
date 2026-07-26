# 自动回复工作流

> 用户说「对作品"xxx"进行自动回复」时的完整执行规范。
> 这是 **agent 多步流程**，不是单条 CLI 调用。

## 流程 3 步

| 步骤 | 动作 | 工具 |
|---|---|---|
| 1. 抓评论 | 拿全量 JSON | `node index.js --comment-list --title "xxx"`（title 可省略，省略选第一个作品） |
| 2. 判断需回复 + 生成文案 | 按规则筛出 target + LLM 生成 `reply_text` | 本地推理 + LLM |
| 3. 直接发送 | agent 自己准备 `replies.json` 后调 `--reply` | `node index.js --reply ...` |

⚠️ **没有人工审批节点**——agent 自己负责判断 + 文案 + 发送的完整链路。文案直接发出去，没有"先看再发"的中间步。

---

## 规则（决定哪些评论需要回复）

| # | 规则 | 关键字段 |
|---|---|---|
| 1 | **跳过作者本人的评论** | `user.is_author === true` |
| 2 | **每条非作者评论，单独判断作者是否已回复过**。已回复过的不再重复 | 见下方判断算法 |
| 3 | **判断"已回复过"必须用 `reply_to` + 时间对比** | `reply_to`、`time` |

> ⚠️ **常见错误**：以为 `top.replies[]` 数组里出现的都是"对该顶级的回复"——**错**。
> `replies[]` 是该顶级评论下**所有的二级回复**，包括二级回复之间互相回复的对话。
> 不能因为 `replies[]` 非空就跳过整个顶级，也不能因为 `replies[]` 为空就判断"作者没回过"——必须看 `reply_to` 字段。

### `reply_to` 字段语义

| `reply_to` 值 | 含义 |
|---|---|
| `null` | 直接回复该顶级评论（顶级评论下的第一条作者回复通常是 `null`） |
| `"<某人名>"` | 回复 `<某人名>` 的二级回复（这是 Douyin 的二级对话机制） |

### 边界情况

| 场景 | 判断 |
|---|---|
| 作者的顶级评论 | 跳过（规则 1） |
| 别人的顶级评论 | 单独判断：作者是否**直接回过这条顶级**（`reply_to: null` 且挂在该顶级下） |
| 别人顶级评论下的二级回复 A | 单独判断：作者是否**回过 A 这个人**（`reply_to === A.user.name` 且挂在同一顶级下）|
| 作者本人的二级回复 | 跳过（规则 1） |
| 作者回复 `reply_to: null` 但不是回这条顶级 | 不可能：`reply_to: null` 的作者回复必然是直接回该顶级 |
| 亮有一计发过 2 条，作者回了第 1 条 | 第 1 条跳过；第 2 条需要回（时间对比保证这点） |

---

## 判断算法（伪代码）

```js
// 第 1 步：收集作者的所有回复（带上下文）
const authorReplies = [];   // [{ reply, parent_id, time, reply_to, target_user_name }]
for (const top of result.comments) {
  for (const r of (top.replies || [])) {
    if (!r.user.is_author) continue;  // 只关心作者的回复
    authorReplies.push({
      reply: r,
      parent_id: top.id,
      time: r.time,
      reply_to: r.reply_to,                       // null 或 某人名
      target_user_name: r.reply_to || top.user.name,  // 被回复的对象（null=回顶级，即回 top.user.name）
    });
  }
}

// 第 2 步：逐条判断
const targets = [];
for (const top of result.comments) {
  // 规则 1：作者本人顶级 → 跳过
  if (top.user.is_author) continue;

  // 规则 2：作者是否直接回过这条顶级？
  //   条件：authorReplies 里有一条，parent_id === top.id，target_user_name === top.user.name
  //                                且 reply_to === null（因为是直接回顶级）
  //                                且 time >= top.time
  const authorRepliedTop = authorReplies.some(ar =>
    ar.parent_id === top.id &&
    ar.reply_to === null &&                      // 直接回顶级
    ar.target_user_name === top.user.name &&
    ar.time >= top.time
  );
  if (authorRepliedTop) continue;  // 顶级本身作者已回 → 跳过整条顶级

  // 顶级评论未被作者回过 → 加入 targets
  targets.push({
    level: 1,
    id: top.id,
    author: top.user.name,
    content: top.content,
  });

  // 顶级下的二级回复也要逐条判断
  for (const r of (top.replies || [])) {
    if (r.user.is_author) continue;  // 跳过作者的二级回复

    // 作者是否回过这条二级（在同一顶级下，target_user_name === r.user.name）？
    const authorRepliedReply = authorReplies.some(ar =>
      ar.parent_id === top.id &&                  // 同一顶级
      ar.target_user_name === r.user.name &&     // 作者回的是这个人
      ar.time >= r.time                          // 时间上在 r 之后
    );
    if (authorRepliedReply) continue;  // 作者已回过这条二级 → 跳过

    targets.push({
      level: 2,
      id: r.id,
      parent_id: top.id,
      author: r.user.name,
      content: r.content,
    });
  }
}
```

### 时间对比的"边界 5 分钟"建议

`time` 字段是字符串（"06月07日 17:06"）。严格相等比较可能因格式不稳定出问题。LLM 实现时：
- 解析成 `Date` 对象（去掉中文"月"和"日"后用 `new Date(...)`）
- 给 5 分钟容差：作者回复在评论 5 分钟内也算"已回复过"（防时间精度误差）

---

## 文案生成（步骤 3）

由 LLM 根据上下文生成 `reply_text`。原则：

- **抖音风格**：10~50 字，口语化，可有 emoji
- **看上下文**：评论内容、其他回复、作者人设（看视频标题线索）
- **不要机械**：避免"感谢您的支持""已收到您的反馈"这类客服腔
- **匹配账号人设**：作者风格从作品名 / 已有回复推测（技术 / 搞笑 / 生活记录...）
- **常见意图处理**：
  - 提问 → 简明回答或反问引导私聊
  - 推荐 / 夸奖 → 礼貌感谢
  - 批评 → 理性回应，必要时解释
  - 广告 / 引流 → 已在规则层筛掉（通常这类评论会被规则 1/2 自然命中）
  - 抬杠 / 引战 → 仍按规则回，保持礼貌或俏皮化解

⚠️ **不要批量生成后立即发送**——必须先准备 `replies.json`，再调 `--reply`。

---

## 发送（步骤 3）

agent 自己生成 `reply_text` 后，转成 `replies.json`（**字段名要换**：`reply_text` → `text`，且 `author`/`content` 必须是 fetch_comments 拿到的实际值），直接调 `--reply` 发送。

⚠️ **没有审批节点**——agent 自己负责文案质量。LLM 生成的 `reply_text` 会直接发出去。

---

## 旧版"审批协议"已废弃

之前要求把待回复 JSON 发给用户、等"批准/OK/可以发"再发。**现在已取消**：
- 工作流不再等用户审批
- agent 自己判断 + 生成 + 发送全链路
- 用户只能在事后通过评论页面手动删除（不可逆）

⚠️ 风险：agent 规则判断错了（漏判作者已回复）会**重复回复**；LLM 文案不符合作者人设会发出不合适的文案。建议 agent 自己跑前**再过一遍规则 + 文案审核**。

```bash
cd <SKILL_DIR>/scripts

# 步骤 3：agent 直接发送（无审批节点、无 dry-run 中间步；title 可省略 → 选第一个作品）
node index.js --reply --title "<作品名>" \
  --replies-file ./replies.json
```

`replies.json` 格式（每条 3 个字段都是字符串）：
```json
[
  { "author": "<匹配用，作者显示名>", "content": "<匹配用，内容关键词>", "text": "<实际发送文本>" },
  ...
]
```

⚠️ `author` / `content` 是匹配关键词（必须是 fetch_comments 拿到的实际值，不能改），`text` 才是发送内容。

如果想完全用 ID 直发（绕过 author/content 匹配），用 `scripts/reply_comment.js::replyToComment` 直接调——见 [matching-rules.md](matching-rules.md) 末尾。

---

## 快捷用法（省略 --title / 用 --index）

`--title` 和 `--index` 都可省略。三种写法：

| 用户意图 | CLI |
|---|---|
| 选第一个作品 | `node index.js --comment-list`（无 `--title` / `--index`） |
| 按名字匹配 | `node index.js --comment-list --title "AI靠不住啊"` |
| 按位置选 | `node index.js --comment-list --index 3` |

**常见场景**：
- 「**抖音回复**」→ `--comment-list` 省略 `--title`，选第一个作品
- 「**抖音回复最新的视频**」→ 同上，选第一个作品（创作者中心列表顺序 = 最新在前）
- 「**抖音回复第 5 个视频**」→ `--comment-list --index 4`（0-based）

```bash
# 等价于 --comment-list --title "第一个作品名"
node index.js --comment-list

# 按序号选（0-based）
node index.js --comment-list --index 3

# 等价于 --reply --title "第一个作品名" --replies-file ./replies.json
node index.js --reply --replies-file ./replies.json
```

> ⚠️ `--title` 与 `--index` 互斥，不能同时存在。两者都省略时默认选第一个。
> ⚠️ 创作者中心的"第一个作品"顺序由抖音决定，不一定是最新发布。如果用户明确指定了作品名/位置，优先用 `--title` / `--index`。

## 完整示例（端到端）

假设用户说：「对作品"AI靠不住啊"进行自动回复」

```bash
# 步骤 1：抓评论
cd <SKILL_DIR>/scripts
node index.js --comment-list --title "AI靠不住啊"
# → 9 条评论（含 3 顶级 + 6 二级回复）
```

抓到的数据里**作者（飞龙）的回复**：
- `c2-r1` 飞龙作者 `reply_to: null` time="06月07日 16:10" → 直接回 c2
- `c2-r5` 飞龙作者 `reply_to: "亮有一计"` time="06月07日 18:02" → 回 c2-r4
- `c3-r1` 飞龙作者 `reply_to: null` time="06月07日 15:39" → 直接回 c3

```js
// 步骤 2：按算法筛 targets
// c1  (？)        → 没人回过 → 需要回
// c2  (橙子)      → 飞龙 c2-r1 reply_to:null time>=c2.time → 顶级已被回 → 跳过整条
//   c2-r1 飞龙    → 作者本人 → 跳过
//   c2-r2 橙子    → 飞龙没回过橙子（c2-r5 是回亮有一计不是橙子）→ 需要回
//   c2-r3 中西    → 飞龙没回过中西 → 需要回
//   c2-r4 亮有一计 → 飞龙 c2-r5 reply_to:"亮有一计" time>=c2-r4.time → 已被回 → 跳过
//   c2-r5 飞龙    → 作者本人 → 跳过
// c3  (poppis)    → 飞龙 c3-r1 reply_to:null time>=c3.time → 顶级已被回 → 跳过整条
//   c3-r1 飞龙    → 作者本人 → 跳过

// targets = [
//   { level:1, id:"c1",   author:"？",         content:"其实他说的都对..." },
//   { level:2, id:"c2-r2", author:"橙子~AI代充", content:"去蹭kimi还有千问" },
//   { level:2, id:"c2-r3", author:"中西合徂集", content:"用qwen或者DeepSeek" },
// ]
```

```js
// 步骤 2：LLM 生成文案
// c1 (？: 其实他说的都对...)       → "哈哈是的，import/require 混用那段确实是我没说清楚"
// c2-r2 (橙子: 去蹭kimi还有千问)    → "确实！kimi 试过，文心一言偶尔也能蹭"
// c2-r3 (中西: 用qwen或者DeepSeek)  → "qwen 之前用过几次，确实能打"
```

```json
// 步骤 2 结束：准备好 replies.json
[
  { "id": "c1",    "level": 1, "author": "？",         "content": "其实他说的都对...",   "reply_text": "哈哈是的..." },
  { "id": "c2-r2", "level": 2, "author": "橙子~AI代充",  "content": "去蹭kimi还有千问",     "reply_text": "确实！kimi 试过..." },
  { "id": "c2-r3", "level": 2, "author": "中西合徂集",  "content": "用qwen或者DeepSeek",   "reply_text": "qwen 之前用过..." }
]
```

```bash
# 步骤 3：直接发送（无审批节点、无 dry-run 中间步）
node index.js --reply --title "AI靠不住啊" --replies-file ./replies.json

# 检查返回 JSON 的 replies[]，每条 ok:true 或 reason: <错误>
```

---

## 完整示例（按 `--index`）

假设用户说：「对第 3 个作品（`--index 2`）自动回复」。

```bash
# 步骤 1：抓评论（按 0-based 序号选作品）
cd <SKILL_DIR>/scripts
node index.js --comment-list --index 2
# → 拿全量 JSON，知道 video.title 后再走步骤 2/3
```

抓到的数据假设 video.title="野兔子科普"，筛出 3 条 target：

```json
// 步骤 2 结束：准备好 replies.json
[
  { "id": "c1",    "level": 1, "author": "兔兔小耳朵",  "content": "是家兔",   "reply_text": "谢谢科普🙏" },
  { "id": "c2-r3", "level": 2, "author": "@妞妞",      "content": "几十块",   "reply_text": "几十块这么划算😄" },
  { "id": "c3",    "level": 1, "author": "挖掘机李哥",  "content": "宠物兔在野外", "reply_text": "感谢关心🐰💕" }
]
```

```bash
# 步骤 3：直接发送（用 --index 跟步骤 1 一致）
node index.js --reply --index 2 --replies-file ./replies.json
```

⚠️ **步骤 1 和步骤 3 的 `--index` 必须一致**（都选同一个作品），否则会发到不同的作品。

### 批量跑多个作品

假设用户说：「对前 2 个作品自动回复」，agent 需要**循环**跑完整流程：

```bash
for i in 0 1; do
  cd <SKILL_DIR>/scripts
  node index.js --comment-list --index $i   # 步骤 1：抓
  # ... agent 本地按规则筛 + LLM 生成 replies.json ...
  node index.js --reply --index $i \
    --replies-file ./replies.json          # 步骤 3：发
done
```

每次循环抓 → 判断 → 文案 → 发送，**`--index` 保持一致**。agent 自己决定每个作品抓完后是否继续下一个。

---

## 与"单独 --reply"用法的关系

这个工作流**复用** `--reply` CLI，但**调用方是 agent**，不是用户直接敲命令行。

- 简单场景（用户自己知道 author + content + text）→ 用户直接敲 `node index.js --reply ...`，不需要走工作流
- 复杂场景（用户给视频名让 agent 全自动判断 + 生成 + 发送）→ 走这个工作流