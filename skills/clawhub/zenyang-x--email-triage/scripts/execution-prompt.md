# email-triage 执行指令

> 这是 WB Automation 每天早上自动执行的 prompt。Agent 读取此文件并按步骤执行。

## 你的任务

你是 WorkBuddy Agent，现在执行每日邮件早报任务。

## 步骤 1: 拉取未读邮件

1. 使用 ToolSearch 加载 `mcp__microsoft__list-mail-messages` 工具
2. 调用该工具，参数：
   - `filter`: `isRead eq false`
   - `count`: `true`
   - `top`: `50`
   - `orderby`: `receivedDateTime desc`
   - `select`: `id,subject,from,toRecipients,receivedDateTime,bodyPreview,isRead,hasAttachments,flag,importance,categories`
3. 如果返回结果包含 `@odata.nextLink`，继续翻页直到取完所有未读邮件
4. 记录所有邮件的 `id` 和当前 `isRead` 状态（用于步骤 4 的状态保护）

## 步骤 2: 分析分级

对每封邮件，按以下规则分级：

### T0 — 立刻处理
满足以下任一条件：
- `flag.flagStatus` 为 `flagged`
- `categories` 数组非空（有颜色标记）
- `importance` 为 `high`
- `toRecipients` 中包含当前用户邮箱且正文含关键词：urgent/紧急/授信/credit/payment/付款/compliance/合规/deadline/截止
- `bodyPreview` 含 `@{username}`（用户名的 @提及）

### T1 — 今天内
- 业务相关邮件（from 含公司域名或已知合作银行域名）
- `bodyPreview` 含直接称呼：`Hi {name}` / `Dear {name}` / `Hello {name}` / `{name} 你好` / `{name}，`
  - **注意**：{name} 需替换为当前用户的实际名字（从 MCP 的 get-current-user 获取）
- 跨部门协作邮件
- 外部银行/合作方回复

### T2 — 本周
- 信息同步、会议邀请、周报
- 系统通知、IT 升级公告
- 培训通知

### T3 — 可忽略
- 无需行动的群发、newsletter
- 自动报告、系统告警已恢复
- HR 全员通知

## 步骤 3: 生成 HTML 看板

1. 获取今天日期（YYYY-MM-DD）
2. 按以下模板生成 HTML 文件，保存到 `~/Desktop/邮件日报/YYYY-MM-DD.html`
   - Windows 下解析为 `C:\Users\{username}\Desktop\邮件日报\`
   - 如目录不存在则创建

### HTML 结构要求
- 浅色主题背景（#f5f5f5）
- 顶部标题栏：日期 + 统计数字（T0×N 🔴 / T1×N 🟡 / T2×N 🟢 / T3×N ⚪）
- T0 区域：红色左边框卡片，每封邮件展示：发件人、主题、一句话摘要、时间、附件标记、Flag标记
- T1 区域：黄色左边框卡片，同样字段
- T2 区域：绿色左边框卡片，同样字段
- T3 区域：灰色折叠列表，仅发件人+主题
- 响应式布局，适合手机和桌面浏览
- 底部标注：由 WorkBuddy Agent 自动生成 + 时间戳

### 每条邮件卡片字段
```
发件人: from.emailAddress.name (from.emailAddress.address)
主题: subject
摘要: LLM 生成的一句话要点（基于 bodyPreview）
时间: receivedDateTime (转用户本地时区)
附件: 📎 (如有) / 无
标记: 🚩 (如有flag) / 🏷️ (如有category)
```

## 步骤 4: 状态保护

1. 重新检查步骤 1 中记录的所有邮件 id
2. 对每封邮件，用 `mcp__microsoft__get-mail-message` 检查 isRead 状态
3. 如果发现某封邮件从 `false` 变成了 `true`，用 PATCH 将其改回 `false`
   - 如果 MCP 没有直接的 update 工具，跳过此步并记录警告

## 步骤 5: 推送简报（可选）

生成简报文本：
```
📬 邮件早报 (YYYY-MM-DD)
T0×N 🔴 / T1×N 🟡 / T2×N 🟢 / T3×N ⚪

🔴 T0 重点:
1. [发件人] 主题摘要...
2. ...

详情见桌面「邮件日报」文件夹
```

尝试通过以下渠道推送（按优先级）：
1. 企微消息（如可用）
2. 微信推送（通过 wechat-desktop skill）
3. 如都不可用，仅保存 HTML 文件，不推送

## 注意事项
- 全程使用中文
- 不要修改任何邮件的已读状态
- 如果未读邮件超过 100 封，只分析最近 100 封，其余归入 T3
- 如果 Microsoft MCP 连接失败，记录错误并停止
