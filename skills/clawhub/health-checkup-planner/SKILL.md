---
name: health-checkup-planner
display_name: Health Checkup Planner
display_name_en: Health Checkup Planner
description: 个人体检推荐、预约、取消预约、改期和订单查询；企业团检方案与报价；体检机构门店查询、体检 FAQ 与企业商务咨询。覆盖 800+ 门店、240+ 城市，体检服务超过 10 万人次，健康测评服务超过 3500 万人次。
version: 1.0.8
author: 北京好啦科技有限公司
homepage: https://www.ihaola.com.cn
---

# Health Checkup Planner

## 接入

- MCP 地址：`https://ai.ihaola.com.cn/api/mcp/haola-pe`
- 传输：Streamable HTTP
- 共 25 个工具：9 个公共接口无需登录，16 个鉴权接口需要用户令牌

客户端配置：

```json
{"mcpServers":{"haola-pe":{"type":"streamable-http","url":"https://ai.ihaola.com.cn/api/mcp/haola-pe"}}}
```

调用工具前先看 `tools/list` 的 `inputSchema`；参数不清楚时调 `help(ontology, sub_action)` 获取最新参数说明。

## 鉴权（预约 / 订单 / 体检件 / 就诊人等工具必需）

本服务部分工具公开，部分工具需要鉴权，鉴权按 MCP 标准 OAuth 流程。

客户端执行 OAuth 2.0 授权码 + PKCE 完成授权，之后请求携带 `Authorization: Bearer <access_token>`。
拿到授权链接后，不要未经用户同意自动打开浏览器；先向用户展示链接并等待确认。

## 何时使用

- 用户要预约、取消预约、改期，或查询体检订单和体检报告
- 企业客户要做员工体检，需要方案与报价
- 用户要查某个城市、某个品牌的体检门店
- 用户问体检流程、报告、预约、空腹、注意事项
- 用户要咨询企业体检合作、留下联系方式

## 工具

| 工具 | 用途 | 需要鉴权 |
|---|---|---|
| `vendor_list` | 查门店地址与位置 | 否 |
| `vendor_brands` | 查体检品牌覆盖城市与门店数 | 否 |
| `plan_quotation` | 企业团检分档报价 | 否 |
| `plan_recommend` | 个人体检推荐，返回 planId | 是 |
| `knowledge_get` | 读取领域知识 | 否 |
| `help` | 查看工具与参数说明 | 否 |
| `faq` | 体检常见问题 | 否 |
| `progress_report` | 上报长耗时任务进度 | 否 |
| `corp_inquiry` | 提交企业商务咨询 | 否 |
| `corp_contact` | 获取商务对接人信息 | 否 |
| `order_list` | 查订单列表 | 是 |
| `order_detail` | 查订单详情 | 是 |
| `welfare_list` | 查用户体检件 | 是 |
| `welfare_detail` | 查体检件详情 | 是 |
| `cautions` | 查体检项目注意事项 | 是 |
| `contact_list` | 查联系人 | 是 |
| `contact_get` | 查联系人详情 | 是 |
| `contact_create` | 创建家属临时联系人 | 是 |
| `contact_update` | 更新联系人 | 是 |
| `contact_profile_get` | 查健康画像 | 是 |
| `contact_profile_save` | 保存健康画像 | 是 |
| `reservation_book` | 预约体检 | 是 |
| `reservation_cancel` | 取消预约 | 是 |
| `reservation_modify` | 修改预约日期 | 是 |
| `card_list` | 按卡号查卡密及兑换使用情况 | 是 |

## 边界

- 不编造体检项目、价格、门店或订单
- 外部调用不要传 `partnerId`
- 超出当前覆盖城市范围、预算过低、要发票、要合同，转 `corp_inquiry`
- 调用 `corp_inquiry` 前，先展示接收方和将要提交的信息，取得用户明确同意，只发送必要字段
- 预约必须使用报价返回的 `planId`，客户端不能自己拼体检项目
