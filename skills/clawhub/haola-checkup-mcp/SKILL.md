---
name: haola-checkup-mcp
display_name: 好啦体检方案 MCP
display_name_en: Haola Checkup MCP
description: 企业团检方案与报价、体检机构门店查询、体检 FAQ 与企业商务咨询。按人均预算生成分档方案，返回项目和 planId，覆盖 241 城。
version: 1.0.0
author: 北京好啦科技有限公司
homepage: https://www.ihaola.com.cn/html/mcp-quote.html
---

# 好啦体检方案 MCP

## 接入

- MCP 地址：`https://ai.ihaola.com.cn/api/mcp/haola-pe`
- 传输：Streamable HTTP
- 匿名可用 9 个公开工具
- 公开工具不校验 Authorization，Authorization 无效或过期时仍按匿名放行
- 预约、订单、体检件、就诊人等工具需要登录后的用户令牌

客户端配置：

```json
{"mcpServers":{"haola-pe":{"type":"streamable-http","url":"https://ai.ihaola.com.cn/api/mcp/haola-pe"}}}
```

## 何时使用

- 企业客户要做员工体检，需要方案与报价
- 用户要查某个城市、某个品牌的体检门店
- 用户问体检流程、报告、预约、空腹、注意事项
- 用户要咨询企业体检合作、留下联系方式

## 工具清单

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

## 企业团检报价

报价前先调用：

```json
{"uri":"objects/checkup-proposal"}
```

再调用 `plan_quotation`：

```json
{"quotes":[{"tier":"基础","budget":500,"healthConcerns":"心血管,肝功能"},{"tier":"高管","budget":1200,"healthConcerns":"心脑血管,肿瘤筛查"}]}
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
{"city":"北京","vendorids":["health100"]}
```

`city`、`province`、`district`、`hospitalCode`、`vendorids`、经纬度至少传一个。

## 体检 FAQ

调用 `faq`，`query` 用 2 到 4 个字的关键词，如 `报告`、`预约`、`空腹`。不要传完整问句。

## 企业咨询

调用 `corp_inquiry`，必填 `company`、`contact`、`phone`。可选 `employees`、`city`、`budget`、`message`。

用户接受报价或需要人工跟进时，调用 `corp_contact` 获取商务对接人信息。

## 边界

- 不编造体检项目、价格、门店或订单
- 外部调用不要传 `partnerId`
- 超出 241 城、预算过低、要发票、要合同，转 `corp_inquiry`
- 预约必须使用报价返回的 `planId`，客户端不能自己拼体检项目
