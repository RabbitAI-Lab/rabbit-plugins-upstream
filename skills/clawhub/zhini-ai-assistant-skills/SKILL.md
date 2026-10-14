---
name: "zhini-ai-assistant"
description: "使用知你AI助手查询多平台客户资料、当前与历史客服会话、聊天记录、客户分群及 API Key 用量，并在用户明确确认后批量打开客户对话、发送文本或图片消息并跟踪发送进度。适用于个微、企微、视频号、微信小程序、公众号、服务号、微信客服、微信小店、抖音号、小红书、微博、网站及 H5 客服等渠道。"
---

# 知你AI助手

通过知你客服 MCP 服务，将多平台客户资料、会话及聊天记录连接到 Codex、WorkBuddy 等 AI 工具，并按用户确认执行批量打开对话和消息发送任务。

## Connection

- 官网：`https://ai.zhinikefu.com/`
- MCP endpoint：`https://mcp.h5bqb.top/mcp`
- 认证方式（二选一，由客户端连接配置决定）：
  - MCP 原生 OAuth 2.1 浏览器授权（推荐）：连接时不配置任何静态认证字段，首次访问受保护资源时由客户端打开浏览器完成知你账号授权，无需 API Key；授权可随时在官网吊销。
  - 静态 Bearer API Key：由 `ZHINI_API_KEY` 环境变量或客户端 Secret 提供，不作为提示词或工具参数传入。
- 连接器未配置或未授权时，先引导用户完成连接与授权，再执行查询；面向用户省略连接器、信任操作和本地配置细节。

## Channel coverage

支持个微、企微、视频号、微信小程序、公众号、服务号、微信客服、微信小店、抖音号、小红书、微博、网站及 H5 客服等平台渠道。

## Capability routing

根据用户意图选择对应流程；一个请求涉及多项能力时，可在保持证据链清晰的前提下组合调用。

### 当前会话分诊

适用于当前队列、等待接待、我的会话、同事会话或 AI 会话查询。

1. 需要区分“我的会话”时，先调用 `zhini_get_current_kefu` 获取 `kfid`。
2. 调用 `zhini_list_active_sessions` 获取实时队列，不把当前快照当作历史统计。
3. 选定会话后，用 `sid` 调用 `zhini_fetch_messages`，用 `uid` 调用 `zhini_get_customer_profile`。

### 客户查询与画像

适用于按姓名、手机号、微信号、渠道、客服、标签、时间或已知 `uid` 定位客户。

1. 客户名、渠道名、客服名或标签名先通过 `zhini_list_channels`、`zhini_list_kefu` 或 `zhini_search_tags` 解析为稳定 ID。
2. 将明确的结构化条件交给 `zhini_search_customers`，避免空条件查询。
3. 已知 `uid` 时直接调用 `zhini_get_customer_profile`；需要聊天内容时再调用 `zhini_fetch_messages`。
4. 多个候选时保留 `uid` 供核对，不把推断当成客户身份事实。

### 历史会话研判

适用于历史咨询、投诉、订单、退款、问题处理、关键词命中或客户前情复盘。

1. 按客户、消息关键词或 `msg_stime` 调用 `zhini_search_sessions`。
2. 关键词只用于召回候选；调用 `zhini_fetch_messages` 读取上下文后再总结。
3. 需要更多结果时按 `page` 翻页；输出会话 ID、时间范围和关键证据。
4. 已知 `uid` 时可调用 `zhini_get_customer_profile` 补充资料。

### 客户分群

适用于按标签、渠道、客服、联系人类型、性别和时间条件构建客户或会话分群。

1. 先将用户明确提到的标签、渠道和客服名称解析为稳定 ID。
2. 结构化条件使用 `zhini_search_customers`；必须按消息内容判断时使用 `zhini_search_sessions` 和 `zhini_fetch_messages`。
3. 多个相似标签或候选需要保留核对点。
4. 分页查询并记录实际条件、页码和返回数量，避免把单页结果当成完整分群。

### 客户触达与消息发送

适用于批量打开选定客户对话、发送跟进文本或图片、跟踪群发进度和管理历史任务。

1. 收件客户必须来自用户明确选定的结果或其他流程已核对候选后的确认结果；不要把整批搜索结果或分群直接当作收件人。
2. 用户要集中处理对话时，展示目标客户清单并确认后调用 `zhini_open_sessions`，将选定客户对话打开到当前客服的“我的对话”，单次最多 20 个用户；已被其他客服接待的用户不会转接。
3. 用户要发送图片时，先调用 `zhini_upload_image_for_message_sending` 上传（PNG/JPEG/GIF，解码后不超过 10 MiB），使用返回的 CDN URL 作为图片消息内容。
4. 首次调用 `zhini_create_message_sending_task` 只准备任务并返回 `confirmation_token`，**不会创建或发送**；向用户完整展示收件客户、任务标题和最终消息内容，确认后用完全相同的内容加 `confirmation_token` 与 `user_confirmed: true` 再次调用才会创建任务。
5. 创建成功后保存 `task_id`，用 `zhini_get_message_sending_task_status` 跟踪进度和逐客户结果；用 `zhini_list_message_sending_tasks` 查询历史任务；删除前先核对任务并保存所需明细，再调用 `zhini_delete_message_sending_task`。
6. 单任务最多 100 个 UID、最多 2 条消息；重试创建时携带相同的 `idempotency_key` 避免重复群发。

### API Key 用量

适用于查询当前连接的总额度、已使用量和剩余额度。

1. 调用 `zhini_get_apikey_usage`。
2. 汇总总配额、已使用量和剩余额度，并标记数据是否一致。
3. 仅展示额度摘要，不输出完整 API Key 或内部鉴权细节。

## Available tools

- `zhini_get_current_kefu`
- `zhini_list_active_sessions`
- `zhini_search_customers`
- `zhini_get_customer_profile`
- `zhini_search_sessions`
- `zhini_fetch_messages`
- `zhini_search_tags`
- `zhini_list_channels`
- `zhini_list_kefu`
- `zhini_get_apikey_usage`
- `zhini_open_sessions`
- `zhini_upload_image_for_message_sending`
- `zhini_create_message_sending_task`
- `zhini_get_message_sending_task_status`
- `zhini_list_message_sending_tasks`
- `zhini_delete_message_sending_task`

## Boundary

- 查询保持只读；批量打开对话与消息发送为受控触达操作，必须在用户明确确认后执行。
- 消息任务不会修改客户资料或标签；不接待、转接或关闭会话；不做全量导出。
- 删除消息任务不可逆，已发送的消息不会撤回；查询结果受当前凭据数据权限约束。
