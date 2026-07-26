---
name: opcmenu
description: 独行录（opcmenu.com）——中国一人公司（OPC）的发现与合作网络。用此技能把独行录接进你的 agent（WorkBuddy / OpenClaw / Claude Code 等均可），以用户身份发需求 / 接需求 / 找合作 / 搜主理人 / 搜产品 / 完成入驻 / 读写资料 / 导出数据卡。当用户提到「独行录 / opcmenu / 接入独行录 / 找需求 / 找合作 / 找主理人 / 一人公司 / OPC 社区 / 园区补贴 / 发动态 / 我的创客主页」或写工具报「未登录 / invalid_token / 密钥失效」时使用。
---

# 独行录 / opcmenu

独行录是一人公司（OPC）主理人的「个人 + 产品」主页平台，核心玩法是需求互换——主理人之间互相发需求、接需求、谈成合作，构建 OPC 之间的产业链。

- MCP 端点：`https://mcp.opcmenu.com/mcp`（Streamable HTTP）
- REST API：`https://api.opcmenu.com/v1`（OpenAPI 描述：https://api.opcmenu.com/openapi.yaml ）
- 全站机读导航：https://opcmenu.com/llms.txt （任何产品/主理人/需求页 URL 加 `.md` 即纯文本）

读公开信息（需求信息流、搜产品 / 主理人、园区、榜单）免密钥；以「我」的身份读写（发需求 / 接洽 / 私信 / 改资料）需要登录密钥。

## 第一步：拿登录密钥（手机号验证码，全程可由 agent 代办）

不要把密钥打印到对话里。

1. 要到手机号，发送验证码：
   ```
   curl -fsS -X POST https://api.opcmenu.com/v1/auth/request-sms \
     -H 'content-type: application/json' -H 'x-opc-client: agent' \
     -d '{"phone":"<手机号>","purpose":"login"}'
   ```
2. 要到 6 位验证码，换长效密钥（按「这台设备」新建一条，可随时在 opcmenu.com/dashboard 吊销）：
   ```
   curl -fsS -X POST https://api.opcmenu.com/v1/auth/agent \
     -H 'content-type: application/json' -H 'x-opc-client: agent' \
     -d '{"phone":"<手机号>","code":"<验证码>","client":"agent","deviceName":"<主机名或agent名>"}'
   ```
   返回 JSON 的 `data.token` 即密钥；`data.devices` 是该用户已接入的设备列表。

## 第二步：接进你的 agent（按宿主选一种）

**A. 支持 MCP 的 agent（WorkBuddy / CodeBuddy / Claude Code / 其它 MCP 客户端）**——在 MCP 配置里加一个 Streamable HTTP 服务器：

```json
{
  "mcpServers": {
    "opcmenu": {
      "type": "http",
      "url": "https://mcp.opcmenu.com/mcp",
      "headers": { "Authorization": "Bearer <token>" }
    }
  }
}
```

Claude Code 可直接执行：

```
claude mcp add --transport http opcmenu https://mcp.opcmenu.com/mcp --scope user \
  --header "Authorization: Bearer <token>"
```

只逛不登录：去掉 `headers` 即为匿名只读。

**B. 不走 MCP 的 agent（含 OpenClaw 直接 curl）**——按 https://api.opcmenu.com/openapi.yaml 直接调 REST，写接口带 `Authorization: Bearer <token>` 头即可，语义与 MCP 工具一一对应。

## 接好之后：能做什么

MCP 工具共 100+，每个工具的描述里写了何时用 / 组合链 / 失败语义，照着调即可。按业务域的代表工具：

- 需求互换（核心玩法，优先想到这里）：`list_needs_feed` 看需求信息流（一人一卡，登录后带匹配度）· `search_needs` 搜需求 · `search_people` 按「能提供什么」搜主理人 · `create_need` 发需求（发布即展示，自动向量撮合）· `contact_need`「找他聊聊」（返回 conversationId，直接接 `send_message` 继续谈）· `complete_need` 双方各确认一次即完成 · `list_my_needs` / `get_need_recommendations` 管理自己的需求、看谁能满足
- 产品 / 主理人：`search_products` · `get_product` · `get_creator` · `create_product` · `update_my_product`
- 我的资料 / 数据卡：`get_my_profile` · `update_my_profile` · `add_profile_link` · `get_my_card`（结构化数据卡，可拿去填别处）
- 入驻：`get_onboarding_status` · `complete_onboarding`
- 私信：`list_my_conversations` · `read_messages` · `send_message` · `get_conversation_needs`（开聊前一步拿全双方需求上下文）
- 动态 / 社区：`list_posts` · `create_post` · `create_post_comment`
- 活动：`list_activities` · `register_for_activity` · `create_activity`
- 园区：`list_parks` · `get_park` · `list_city_policies`（城市补贴政策）· `checkin_park`
- 分享：`get_share_card_manifest`（返回 shareText + 链接，可直接转发）

用法上发挥 agent 的长处：把工具串成链（看 feed → 接洽 → 发消息）、批量盘点、结构化导出、替用户代办。示例：

- 「看看需求广场里有没有我能接的，有合适的先跟我确认，再替我发起联系。」
- 「帮我发个需求：找能提供跨境电商供应链资源的主理人。写好先给我过目再发布。」
- 「盘点我的未读私信，每条附上围绕哪个需求在聊，替我草拟回复。」
- 「帮我在独行录完成入驻：先看我还差哪步，再把资料和产品填详细。」

内容一律先过后审：发布即展示，不存在「等待审核」。写操作（发需求 / 发消息 / 接洽 / 发动态）在发送前把内容给用户确认。

## 故障排查

- 写工具报 `invalid_token / 未登录`：密钥被吊销或过期，回到「第一步」重新换发；替换旧设备时可用新密钥调 `POST /v1/me/devices/revoke` 吊销旧条目。
- MCP 连接报 406：客户端没带 `Accept: application/json, text/event-stream` 头，属客户端配置问题。
- 更多接入方式与示例：https://opcmenu.com/connect ；一键安装脚本：`curl -fsSL https://opcmenu.com/install.sh | sh`（macOS/Linux，适配 Claude Code）。
