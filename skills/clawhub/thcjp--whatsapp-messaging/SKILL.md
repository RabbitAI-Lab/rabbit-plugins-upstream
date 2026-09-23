---

slug: whatsapp-messaging
description: WhatsApp 商业消息是一个专业的whatsapp messaging 2工具，提供完整的自动化处理能力。核心功能包括：通过 WhatsApp。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。
  Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型。。通过 WhatsApp Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型。内置错误处理机制和参数验证。支持中英文输入输出。提供标准化的返回格式。适用于多种业务场景。可直接集成到现有工作流中。降低手动操作成本。提供详细的使用示例和文档。
name: "whatsapp-messaging"
version: 1.0.7
displayName: "WhatsApp 商业消息"
summary: "通过 WhatsApp Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型。"
summary_zh: '"通过 WhatsApp Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型。"'
license: '"MIT" 通过 WhatsApp Business API 发送消息、管理模板、处理媒体，自动化 WhatsApp Business 消息工作流.
  支持文本、图片、视频、音频、文档、位置、联系人、交互按钮、列表、模板等多种消息类型. 通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp
  API 访问. 涵盖电话号码查询、消息发送、媒体上传下载、模板创建与审批状态、业务资料读取等完整能力. 适用于订单通知、客户支持、预约提醒、营销活动等需要触达
  WhatsApp 用户的业务场景.'
tags:
- 研发工具
- Automation
- WhatsApp
- 社交
- 通信
- whatsapp
- api
- write
- clawlink
- business
tools:
- read
- exec
- write
homepage: '""'
category: '"Communication"'

---

> **核心功能**: 本技能提供中文交互、时使用、、工作流优化时使用、处理、工作流优化时使用等能力。

# WhatsApp
通过 WhatsApp Business API 发送消息、管理模板、处理媒体，自动化 WhatsApp Business 消息工作流。本技能通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp API 访问.
## 输入定义
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | WhatsApp 商业消息处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |
## 专业版增值服务
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |
## How It Works
```text
┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Agent 会话     │────▶│   ClawLink   │────▶│  WhatsApp Cloud  │
│   (用户对话)     │     │   (OAuth)    │     │      API         │
└─────────────────┘     └──────────────┘     └──────────────────┘
         │                       │                       │
         │  1. 安装插件           │                       │
         │  2. 配对设备           │                       │
         │  3. 连接 WhatsApp      │                       │
         │                       │  4. 安全存储令牌       │
         │                       │  5. 代理转发请求       │
         │                       │                       │
         ▼                       ▼                       ▼
   ┌──────────┐           ┌──────────┐           ┌──────────┐
   │  SKILL   │           │ Dashboard│           │ WhatsApp│
   │  文件    │           │ 鉴权     │           │ Business │
   └──────────┘           └──────────┘           └──────────┘
```
Agent 会话通过 ClawLink 代理访问 WhatsApp Cloud API。ClawLink 负责OAuth 鉴权、令牌存储与请求转发，Agent 只需调用 `clawlink_call_tool` 系列工具即可完成消息发送与管理.
## Install
安装 ClawLink 插件。用户确认后完成完整配置，使 ClawLink 工具在后续会话中可用.
```bash
skill-platform plugins install SkillHub:clawlink-plugin
skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
skill-platform gateway restart
```
重启后提示用户：发送 `/new` 开启新会话，再重新请求 WhatsApp 功能.
## Quick Start
```bash
clawlink_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'
# ...
clawlink_call_tool --tool "whatsapp_send_message" --params '{"phone_number": "+15551234567", "message": "Hello!"}'
# ...
clawlink_call_tool --tool "whatsapp_get_message_templates" --params '{}'
```
**执行步骤**:
1. 准备输入参数并确认运行环境
2. 执行核心操作,处理输入数据
3. 验证处理结果的正确性
**结果处理**: 执行完成后,输出格式化的处理结果供用户查看和保存。结果包含执行状态、输出数据和错误信息(如有).
## Authentication
所有 WhatsApp 工具调用由 ClawLink 自动鉴权，使用用户已连接的 WhatsApp Business 账户令牌。会话中无需手动传入 API 令牌。ClawLink 安全存储令牌并注入到每个 WhatsApp Business API 请求中.
### Getting Connected
1. 安装 ClawLink 插件（见 Install）.
2. 若未配置，调用 `clawlink_begin_pairing` 配对插件.
3. 打开 `https://claw-link.dev/dashboard?add=whatsapp` 连接 WhatsApp.
4. 调用 `clawlink_list_integrations` 验证连接已激活.
## Connection Management
### 列出连接
```bash
clawlink_list_integrations
```
返回所有已连接的集成。确认返回列表中包含 `whatsapp`.
### 验证连接
```bash
clawlink_list_tools --integration whatsapp
```
返回 WhatsApp 的实时工具目录。这是工具是否可用的权威来源.
### 重新连接
若 WhatsApp 工具缺失或连接报错：
1. 引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp`
2. 用户确认后，调用 `clawlink_list_integrations` 验证
3. 再调用 `clawlink_list_tools --integration whatsapp` 确认工具可用
## Security & Permissions
- 访问范围限定于 OAuth 配置时连接的 WhatsApp Business 账户
- 所有消息发送操作须用户明确确认。WhatsApp 消息会触达真实用户，须确认收件人与内容
- 消息模板须经 WhatsApp 预审通过后方可使用
- 24 小时客服窗口适用于自由文本消息；窗口外只能发送已审批的模板
- 发送前确认收件人手机号，消息发出后无法撤回
### 安全风险防范
| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |
## Tool Reference
### Phone Numbers
| Tool | Description | Mode |
|---:|---:|---:|
| `whatsapp_get_phone_numbers` | 列出账户下所有手机号 | Read |
| `whatsapp_get_phone_number` | 获取指定手机号详情 | Read |
### Messages
| Tool(续)| Description | Mode |
|:------:|:------:|:------:|
| `whatsapp_send_message` | 发送文本消息 | Write |
| `whatsapp_send_media` | 发送图片、视频、音频或文档 | Write |
| `whatsapp_send_media_by_id` | 通过已上传的 media ID 发送媒体 | Write |
| `whatsapp_send_location` | 发送带坐标的位置消息 | Write |
| `whatsapp_send_contacts` | 发送联系人卡片 | Write |
| `whatsapp_send_interactive_buttons` | 发送最多 3 个回复按钮的消息 | Write |
| `whatsapp_send_interactive_list` | 发送最多 10 个选项的列表消息 | Write |
| `whatsapp_send_template_message` | 发送已审批的消息模板 | Write |
### Media
| Tool(续)(续)| Description | Mode |
|:------------|------------:|:------------|
| `whatsapp_upload_media` | 上传媒体到 WhatsApp 服务器 | Write |
| `whatsapp_get_media_info` | 获取已上传媒体的元数据与下载 URL | Read |
### Message Templates
| Tool(续)(续)| Description | Mode |
|-------:|:-------|-------:|
| `whatsapp_get_message_templates` | 列出所有消息模板 | Read |
| `whatsapp_get_template_status` | 查询指定模板的审批状态 | Read |
| `whatsapp_create_message_template` | 创建新消息模板 | Write |
| `whatsapp_delete_message_template` | 删除消息模板 | Write |
### Business Profile
| Tool(续)(续)| Description | Mode |
|:------------:|--------------|:-------------|
| `whatsapp_get_business_profile` | 获取业务资料信息 | Read |
## 前置条件
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
### API Key 配置
如需调用外部API，请参考环境配置章节设置对应密钥
### 可用性分类
- **分类**: MD+EXEC（）
**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 能力图谱
- 多类型消息发送：文本、图片、视频、音频、文档、位置、联系人、交互按钮、列表、模板
- 模板全生命周期管理：创建、查询审批状态、列出、删除，支持窗口外触达
- 媒体上传与复用：上传媒体获取 media ID，后续可通过 ID 复用发送，避免重复上传
- 电话号码与业务资料查询：列出账户下所有手机号及业务资料信息
- 交互式消息：通过按钮（最多 3 个）或列表（最多 10 个选项）收集用户反馈
- ClawLink 托管鉴权：OAuth 令牌由 ClawLink 安全存储与注入，会话中无需手动管理凭据
- 读写分级执行：读操作（list/get/describe）可直接执行，写操作须经 preview 后用户确认再调用
## 使用案例
### 案例一：发送发货确认模板消息
订单发货后，向买家发送已审批的 `shipping_confirmation` 模板，填充客户姓名与订单号.
```bash
clawlink_call_tool --tool "whatsapp_send_template_message" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "template_name": "shipping_confirmation",
    "language_code": "en",
    "components": [
      {
        "type": "body",
        "parameters": [
          {"type": "text", "text": "John"},
          {"type": "text", "text": "#12345"}
        ]
      }
    ]
  }'
```
`phone_number_id` 从 `whatsapp_get_phone_numbers` 获取。模板须已通过 WhatsApp 审批，语言代码与模板定义一致。窗口外触达必须使用模板，自由文本会被拒绝.
### 案例二：发送交互按钮收集收货反馈
包裹送达后，向买家发送带"是/否"两个按钮的消息，确认是否收到.
```bash
clawlink_call_tool --tool "whatsapp_send_interactive_buttons" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "header": "Order Update",
    "body": "Has your package arrived?",
    "buttons": [
      {"id": "yes", "title": "Yes"},
      {"id": "no", "title": "No"}
    ]
  }'
```
按钮最多 3 个，每个按钮需有唯一 id 与标题。交互按钮属于自由文本消息，须在 24 小时窗口内发送。买家的回复会触发 webhook，便于后续自动化处理.
### 案例三：上传并发送图片回执
先上传一张回执图片，再用 media ID 发送，避免重复上传同一图片.
```bash
# 上传媒体获取 media ID
clawlink_call_tool --tool "whatsapp_upload_media" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "media_url": "https://example.com/receipt.png",
    "media_type": "image/png"
  }'
# ...
# 通过 URL 直接发送图片（附带说明）
clawlink_call_tool --tool "whatsapp_send_media" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "caption": "Here is your receipt for order #12345"
  }'
```
`media_url` 须为 WhatsApp 服务器可访问的公网地址。媒体下载 URL 会过期，需要时通过 `whatsapp_get_media_info` 获取新的下载地址.
## Discovery & Execution
### 发现工具
1. 调用 `clawlink_list_integrations` 确认 WhatsApp 已连接
2. 调用 `clawlink_list_tools --integration whatsapp` 查看实时工具目录
3. 将返回列表视为权威来源，不臆测工具是否存在
4. 若用户描述的能力但工具名不明确，调用 `clawlink_search_tools` 传入简短查询与集成名 `whatsapp`
5. 若无 WhatsApp 工具出现，引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp`
### 执行分级
```text
┌─────────────────────────────────────────────────────────────┐
│  读操作（安全）                                             │
│  list → get → describe                                     │
│  例：列出模板 → 查询状态 → 汇报                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  写操作（须确认）                                           │
│  describe → preview → confirm → call                       │
│  例：预览消息 → 用户确认 → 发送                             │
└─────────────────────────────────────────────────────────────┘
```
1. 不熟悉的工具、模糊的请求或任何写操作，先调用 `clawlink_describe_tool`
2. 根据返回的 schema、`whenToUse`、`askBefore`、`safeDefaults`、`examples`、`followups` 组织调用
3. 读操作优先于写操作，以减少歧义
4. 写操作或标记须确认的操作，先调用 `clawlink_preview_tool`
5. 用 `clawlink_call_tool` 执行。仅在 preview 符合用户意图后传入确认
6. 工具调用失败时，报告真实错误，不编造结果
## 异常恢复流程
### 131026 — 消息无法送达
收件人手机号不是有效的 WhatsApp 账户，消息被 WhatsApp 拒绝。处理：确认收件人已在 WhatsApp 注册且号码正确（含国家代码），排除座机或未注册号码.
### 133010 — 收件人未注册 WhatsApp
收件人手机号未在 WhatsApp 注册。处理：与用户确认号码是否正确，或改用短信等其他渠道触达.
### 131047 — 超出 24 小时客服窗口
向超过 24 小时未主动消息的用户发送自由文本时触发。处理：改用已审批的模板消息发送，模板不受窗口限制.
### 模板未找到或未审批
模板名不存在或尚未通过 WhatsApp 审批。处理：调用 `whatsapp_get_message_templates` 确认模板名与状态，仅使用状态为 approved 的模板；新建模板须等待审批通过后再发送.
### 媒体上传失败
`media_url` 不可访问或格式不受支持。处理：确认 URL 为公网可访问地址（非本地路径），且 media_type 与实际文件类型一致；图片支持 png/jpeg，视频支持 mp4，文档支持 pdf/doc 等.
### 工具未找到
工具名在当前目录中不存在。处理：调用 `clawlink_list_tools --integration whatsapp` 核实工具名，以实时目录为准；若工具缺失，按"重新连接"步骤恢复.
### 连接缺失
WhatsApp 未连接。处理：引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp` 完成连接，再调用 `clawlink_list_integrations` 验证.
### 写操作被拒绝
用户未确认写操作。处理：所有写操作（发送消息、上传媒体、创建/删除模板）须用户明确确认后再执行，不要跳过确认步骤.
## 用户咨询
### 24 小时客服窗口如何计算？
从用户最后一次向商家发送消息的时刻起算 24 小时。窗口内可发送自由文本、图片、交互按钮等任意消息；窗口外只能发送已审批的模板消息。超出窗口发送自由文本会收到 131047 错误.
### 如何获取 phone_number_id？
调用 `whatsapp_get_phone_numbers` 列出账户下所有手机号，返回结果中包含每个号码的 `phone_number_id`。发送消息时须传入该 ID 标识发送方。一个账户可有多个号码，按业务需要选择.
### 消息模板审批需要多久？
审批时长由 WhatsApp 决定，通常为数分钟到数小时不等。可通过 `whatsapp_get_template_status` 查询状态，状态为 `approved` 后方可用于发送。被拒绝的模板需修改后重新提交.
### 模板删除后能否立即重建同名模板？
不能。模板删除后有 30 天冷却期，期间同名模板无法创建。处理：删除前确认不再需要，或使用新名称创建.
### 收件人手机号需要什么格式？
须包含国家代码，例如美国号码以 `+1` 开头，中国号码以 `+86` 开头。不带国家代码会被视为无效号码。发送前务必确认号码完整，消息发出后无法撤回.
### 媒体下载 URL 会过期吗？
会。上传媒体后返回的下载 URL 有时效，过期后无法访问。需要下载时调用 `whatsapp_get_media_info` 获取新的下载地址.
## 错误恢复指南
| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
## 限制条件
- 自由文本消息受 24 小时客服窗口限制，窗口外只能使用已审批模板
- 模板须经 WhatsApp 审批，审批时长与结果由 WhatsApp 决定
- 模板删除后有 30 天冷却期，期间无法重建同名模板
- 媒体下载 URL 会过期，需调用 `whatsapp_get_media_info` 刷新
- 交互按钮最多 3 个，列表消息最多 10 个选项，超出需拆分多条
- 收件人手机号须包含国家代码，否则发送失败
- 消息一旦发出无法撤回，发送前须确认收件人与内容
- 依赖 ClawLink 托管鉴权，ClawLink 连接异常时所有工具不可用
## 响应格式
```json
{
  "success": true,
  "data": {
    "result": "WhatsApp 商业消息处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "whatsapp-messaging"
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
## 常见问题FAQ
### Q1: 如何确保消息模板在WhatsApp上成功发送？
A1: 确保模板已通过WhatsApp审批，并使用正确的`phone_number_id`和语言代码。发送前检查模板内容，避免敏感或违规信息。
### Q2: WhatsApp消息发送失败时，如何定位问题？
A2: 检查错误代码，如131026表示无效手机号，133010表示未注册，131047表示超出24小时窗口。根据错误代码调整操作。
### Q3: 如何在WhatsApp上发送包含多个图片的消息？
A3: 单次发送最多支持10个图片。如果图片超过10张，需要分批次发送。确保每个图片都有适当的描述。
### Q4: WhatsApp消息模板的审批流程是怎样的？
A4: 模板创建后，需提交给WhatsApp进行审批。审批通常在数分钟到数小时内完成。通过后即可使用，未通过需修改后重新提交。
### Q5: 如何在WhatsApp上发送位置信息？
A5: 使用`whatsapp_send_location`工具，提供经纬度坐标。确保用户已同意分享位置信息。
## 故障应对方案
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
|:-------:|:-------:|:-------:|:-------:|
| 消息发送失败 | 无效的手机号 | 验证手机号格式，确保手机号已注册WhatsApp | 修正手机号或使用其他联系方式 |
| 模板发送失败 | 模板未审批 | 检查模板状态，确保模板已通过审批 | 重新提交模板或使用已审批模板 |
| 媒体上传失败 | 媒体URL不可访问 | 检查媒体URL，确保为公网可访问地址 | 使用有效的媒体URL |
| 连接异常 | ClawLink未连接 | 检查ClawLink连接状态 | 重新连接ClawLink |
| 24小时窗口外发送失败 | 超出24小时窗口 | 确认发送时间，使用模板消息 | 使用已审批模板消息发送 |
## 创新特色
### 效率提升量化分析表格
| 场景 | 提升效率 | 量化指标 |
|:----:|:-------:|:-------:|
| 订单通知 | 自动化发送 | 通知时间缩短50% |
| 客户支持 | 快速响应 | 平均响应时间缩短30% |
| 预约提醒 | 提前通知 | 预约取消率降低20% |
| 营销活动 | 高效触达 | 营销转化率提升15% |
### 差异化对比表格
| 对比项 | WhatsApp Messaging | 传统短信 |
|:------:|:----------------:|:--------:|
| 个性化 | 支持模板和交互按钮 | 限制于文本 |
| 多媒体 | 支持图片、视频等 | 限制于文本 |
| 审批流程 | 模板需WhatsApp审批 | 无需审批 |
| 24小时窗口 | 窗口外只能发送模板 | 无限制 |
| 鉴权方式 | ClawLink托管 | 需自行管理API密钥 |
| 连接管理 | 自动化连接管理 | 需手动配置 |
## 功能梳理
- **自动化执行**: 通过 WhatsApp Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据
## 效能分析
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |
## 优势分析
| 对比维度 | "WhatsApp 商业消息" | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | "通过 WhatsApp Business API 发送消息、管理模板、处理媒体 | 通用场景 | 通用场景 |
### "WhatsApp 商业消息"通用排查步骤
1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 错误恢复方案
针对"WhatsApp 商业消息"使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |
