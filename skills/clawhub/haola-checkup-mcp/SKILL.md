---
name: haola-checkup-mcp
display_name: 好啦体检方案 MCP
display_name_en: Haola Checkup MCP
description: 企业团检方案与报价、体检机构门店查询、体检 FAQ 与企业商务咨询。覆盖 800+ 门店、240+ 城市，体检服务超过 10 万人次，健康测评服务超过 3500 万人次。
version: 1.0.4
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

调用工具前先看 `tools/list` 的 `inputSchema`；参数不清楚时调 `help(ontology, sub_action)` 获取最新参数说明。

## 鉴权（预约 / 订单 / 体检件 / 就诊人等工具必需）

这些工具未登录返回 HTTP 401，响应头带：

`WWW-Authenticate: Bearer resource_metadata="https://ai.ihaola.com.cn/.well-known/oauth-protected-resource/api/mcp/haola-pe"`

按 MCP 标准 OAuth 流程完成授权。客户端根据 `resource_metadata` 发现授权服务器，执行 OAuth 2.0 授权码 + PKCE，之后请求携带 `Authorization: Bearer <access_token>`。
拿到授权链接后，不要未经用户同意自动打开浏览器；先向用户展示链接并等待确认。

- 匿名工具（vendor_* / faq / knowledge_get / help / plan_quotation / corp_* / progress_report）不需要令牌。
- 预约链路：plan_recommend 拿 planId → contact_create/list 建就诊人 → reservation_book 下单。

## 何时使用

- 企业客户要做员工体检，需要方案与报价
- 用户要查某个城市、某个品牌的体检门店
- 用户问体检流程、报告、预约、空腹、注意事项
- 用户要咨询企业体检合作、留下联系方式

## 无需登录的工具

| 工具 | 用途 |
|---|---|
| `plan_quotation` | 企业团检分档报价 |
| `knowledge_get` | 取领域知识 |
| `vendor_brands` | 各体检品牌覆盖的城市与门店数 |
| `vendor_list` | 具体门店地址与位置 |
| `faq` | 体检常见问题 |
| `corp_inquiry` | 提交企业商务咨询 |
| `corp_contact` | 取商务对接人姓名、电话、邮箱、二维码 |
| `help` | 查看当前可用工具和参数 |
| `progress_report` | 长耗时步骤向用户报进度 |

## 需要登录的工具

`order_list`、`welfare_list`、`template_stats`、`plan_recommend`、`welfare_detail`、`template_detail`、`template_list`、`cautions`、`order_detail`、`contact_list`、`contact_get`、`contact_create`、`contact_update`、`reservation_book`、`reservation_cancel`、`reservation_modify`、`card_list`

## 企业团检报价

报价前先调用 `knowledge_get` 加载《企业团检方案顾问》引导词，再调用 `plan_quotation`。

展示时逐档列出项目和金额，不合并成笼统描述。

## 门店查询

先用 `vendor_brands` 确认品牌短码和覆盖城市，再用 `vendor_list` 查门店。

外部调用 `vendorids` 仅支持 `health100`、`haolaruici`。具体筛选参数看 `tools/list` 或 `help(ontology="vendor", sub_action="list")`。

## 体检 FAQ

调用 `faq` 回答体检常见问题。

## 企业咨询

企业合作、报价跟进等需求调用 `corp_inquiry`。用户需要人工对接时调用 `corp_contact`。

## 边界

- 不编造体检项目、价格、门店或订单
- 外部调用不要传 `partnerId`
- 超出当前覆盖城市范围、预算过低、要发票、要合同，转 `corp_inquiry`
- 预约必须使用报价返回的 `planId`，客户端不能自己拼体检项目
