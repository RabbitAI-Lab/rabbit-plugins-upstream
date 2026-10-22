---
name: haola-checkup-mcp
display_name: 好啦体检方案 MCP
display_name_en: Haola Checkup MCP
description: 企业团检方案与报价、体检机构门店查询、体检 FAQ 与企业商务咨询。覆盖 800+ 门店、240+ 城市，体检服务超过 10 万人次，健康测评服务超过 3500 万人次。
version: 1.0.2
author: 北京好啦科技有限公司
homepage: https://www.ihaola.com.cn/html/mcp-quote.html
---

# 好啦体检方案 MCP

## 安装

OpenClaw 2026.5.4 使用 skill slug 安装，不要加发布者前缀：

```bash
openclaw skills install haola-checkup-mcp
```

## 接入

- MCP 地址：`https://ai.ihaola.com.cn/api/mcp/haola-pe`
- 传输：Streamable HTTP
- 匿名可见 24 个工具：9 个公开工具无需登录，17 个工具需要用户令牌
- 公开工具不校验 Authorization，Authorization 无效或过期时仍按匿名放行
- 需要登录的工具在未登录调用时返回 401

客户端配置：

```json
{"mcpServers":{"haola-pe":{"type":"streamable-http","url":"https://ai.ihaola.com.cn/api/mcp/haola-pe"}}}
```

## 鉴权（预约 / 订单 / 体检件 / 就诊人等工具必需）

这些工具未登录返回 HTTP 401，且响应头带
`WWW-Authenticate: Bearer resource_metadata="https://ai.ihaola.com.cn/.well-known/oauth-protected-resource/api/mcp/haola-pe"`。
按标准 OAuth 2.0 授权码 + PKCE（公共客户端）自行拿令牌，不要停在 401 上问用户：

1. 取授权服务器元数据（RFC 8414）：
   `GET https://ai.ihaola.com.cn/.well-known/oauth-authorization-server`
   → authorization_endpoint / token_endpoint / registration_endpoint
   → grant_types=["authorization_code","refresh_token"]
   → token_endpoint_auth_methods_supported=["none"]（公共客户端，无 secret，必须 PKCE）
   → code_challenge_methods_supported=["S256"]，scopes_supported=["haola-pe"]

2. 动态注册客户端（RFC 7591）：
   `POST https://ai.ihaola.com.cn/api/auth/oauth/register`
   body: `{"client_name":"<任意>","redirect_uris":["http://127.0.0.1:<空闲端口>/callback"],"grant_types":["authorization_code","refresh_token"],"response_types":["code"],"token_endpoint_auth_method":"none"}`
   → 拿到 client_id

3. 生成 PKCE：code_verifier = 随机 43–128 字符；code_challenge = S256(verifier)；
   同时生成随机 state，并在 127.0.0.1:<端口> 起一个本地 HTTP 回调服务接收 GET /callback。

4. 拼授权链接交给用户登录（会 302 到
   `https://www.ihaola.com.cn/launch/haolaPeBot/mcpAuth?...` 登录页）：
   `{authorization_endpoint}?response_type=code&client_id=…&redirect_uri=…&scope=haola-pe&code_challenge=…&code_challenge_method=S256&state=…`

5. 用户登录授权后回调到 redirect_uri 并带 `code`；从回调里取 code。

6. 换令牌（application/x-www-form-urlencoded）：
   `POST https://ai.ihaola.com.cn/api/auth/oauth/token`
   `grant_type=authorization_code&code=<code>&redirect_uri=…&client_id=…&code_verifier=…`
   → 返回 access_token + refresh_token

7. 之后所有鉴权工具调用都带 `Authorization: Bearer <access_token>`；
   过期用 `grant_type=refresh_token` 刷新。

- 匿名工具（vendor_* / faq / knowledge_get / help / plan_quotation / corp_* / progress_report）不需要令牌。
- 预约链路：plan_recommend 拿 planId → contact_create/list 建就诊人 → reservation_book 下单。

以下 JSON 示例是 MCP `tools/call` 的 `params`。调用时把 `name` 和 `arguments` 放入 `params`。

## 何时使用

- 企业客户要做员工体检，需要方案与报价
- 用户要查某个城市、某个品牌的体检门店
- 用户问体检流程、报告、预约、空腹、注意事项
- 用户要咨询企业体检合作、留下联系方式

## 无需登录的工具

| 工具 | 用途 | 必填参数 |
|---|---|---|
| `plan_quotation` | 企业团检分档报价 | `quotes` |
| `knowledge_get` | 取领域知识，不传 uri 时列出可用知识 | 无 |
| `vendor_brands` | 各体检品牌覆盖的城市与门店数 | 无 |
| `vendor_list` | 具体门店地址与位置 | 至少一个筛选条件 |
| `faq` | 体检常见问题 | 无 |
| `corp_inquiry` | 提交企业商务咨询 | `company`、`contact`、`phone` |
| `corp_contact` | 取商务对接人姓名、电话、邮箱、二维码 | 无 |
| `help` | 查看当前可用工具和参数 | 无 |
| `progress_report` | 长耗时步骤向用户报进度 | `text` |

## 需要登录的工具

`order_list`、`welfare_list`、`template_stats`、`plan_recommend`、`welfare_detail`、`template_detail`、`template_list`、`cautions`、`order_detail`、`contact_list`、`contact_get`、`contact_create`、`contact_update`、`reservation_book`、`reservation_cancel`、`reservation_modify`、`card_list`

## 企业团检报价

报价前先调用 `knowledge_get` 加载《企业团检方案顾问》引导词：

```json
{
  "name": "knowledge_get",
  "arguments": {
    "uri": "objects/checkup-proposal"
  }
}
```

再调用 `plan_quotation`：

```json
{
  "name": "plan_quotation",
  "arguments": {
    "quotes": [
      {"tier": "基础", "budget": 500, "healthConcerns": "心血管,肝功能"},
      {"tier": "高管", "budget": 1200, "healthConcerns": "心脑血管,肿瘤筛查"}
    ]
  }
}
```

`quotes` 每项字段：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `budget` | number | 是 | 人均预算，单位元 |
| `healthConcerns` | string | 是 | 健康诉求，逗号分隔 |
| `tier` | string | 否 | 档名，仅标识该档 |
| `populations` | array | 否 | `man` / `lady` / `girl`，默认三人 |

返回 `data.list`，每档包含 `tier`、`budget`、`planList`、`combinedPrice`、`discount`。`planList` 按人群分组，每项包含 `population`、`price`、`items`、`planId`。

展示时逐档列出项目和金额，不合并成笼统描述。

## 门店查询

先调用 `vendor_brands`，返回品牌短码、品牌名、覆盖城市数、门店数。

再调用 `vendor_list`：

```json
{
  "name": "vendor_list",
  "arguments": {
    "city": "北京",
    "vendorids": ["health100"]
  }
}
```

`city`、`province`、`district`、`hospitalCode`、`vendorids`、经纬度至少传一个。

## 体检 FAQ

调用 `faq`：

```json
{
  "name": "faq",
  "arguments": {
    "query": "报告"
  }
}
```

`query` 用 2 到 4 个字的关键词，如 `报告`、`预约`、`空腹`。不要传完整问句。

## 企业咨询

调用 `corp_inquiry`：

```json
{
  "name": "corp_inquiry",
  "arguments": {
    "company": "某某科技有限公司",
    "contact": "张先生",
    "phone": "13800000000"
  }
}
```

`company`、`contact`、`phone` 必填。可选 `employees`、`city`、`budget`、`message`。

用户接受报价或需要人工跟进时，调用 `corp_contact` 获取商务对接人信息。

## 边界

- 不编造体检项目、价格、门店或订单
- 外部调用不要传 `partnerId`
- 超出当前覆盖城市范围、预算过低、要发票、要合同，转 `corp_inquiry`
- 预约必须使用报价返回的 `planId`，客户端不能自己拼体检项目
