# 工商工具速查

POST `https://mcp-server.zhiliaobiaoxun.com/api_v2/` + 工具名。请求头：`X-API-Key`（平台Key）、`X-Client: company-registry/1.1.0`、`Content-Type: application/json`。不向客户端分发供应商Token。

五个工商接口成功有数据每次/每页 **3积分**，无结果和失败不扣费。有效会员先扣当日额度，不足时按用户的钱包续扣设置执行。只调用用户需要的能力。

## 主体参数

统一使用 `company_name` 或别名 `company`：准确企业全称、统一社会信用代码、注册号或工商数据源企业ID。平台主体ID不能代替工商数据源ID。
简称通过免费主体库消歧，有多个候选时返回 `QUERY_EMPTY` 和候选列表，需用户确认，不付费猜测。

## get_company_registry — 工商基本信息

```json
{"company_name":"北京百度网讯科技有限公司"}
```

返回 `query`、`matched_by`（exact/bidding_index/identifier）、`matched_name`、`company`、`other_candidates`。
`company` 包括：

- `tianyanchaId`：工商数据源ID，字符串，不是平台主体ID。
- `name`、`unifiedSocialCreditCode`、`businessRegistrationNumber`、`organizationCode`、`organizationType`、`legalRepresentative`。
- `registeredCapital`、`paidInCapital`：上游明确为「万」时的数值，否则null；币种见 `registeredCapitalCurrency` / `paidInCapitalCurrency`。`registeredCapitalDetail` / `paidInCapitalDetail` 包含raw/amount/unit/currency，不擅自汇率换算。
- `establishmentDate`、`approvalDate`、`operatingPeriod`（startDate/endDate，缺失日期为空）。
- `businessStatus`、`registrationAuthority`、`provinceCode`（省份简称码）、`city`、`area`、`address`、`industry`、`businessScope`、`usedName`、`nickNames`、`staffNumRange`。
- `sourceUpdatedAt`：供应商更新时间原始毫秒时间戳，缺失时不猜测。

本期工商基本信息接口不含联系方式、商标或官网。使用自有库查询时应标明数据口径与更新时间，不将历史信息称为实时数据。

## 四个分页接口

```json
{"company_name":"北京百度网讯科技有限公司","page_num":1,"page_size":20}
```

每次只查一页；`page_size`为1至20，默认20；`page_num`从1开始。返回 `total`、`items`、`page_num`、`page_size`、`has_more`、`query`、`matched_by`、`matched_name`、`queried_identifier`。以ID/信用代码查列表时 `matched_name` 可为空，不额外采购基本信息以填名。

| 工具 | items字段 |
|---|---|
| `get_company_shareholders` | tianyanchaId/tianyanchaCompanyId/name/type/typeName、subscribedCapital/paidInCapital记录数组（amount/method/date/percent）、firstShareholdingDate、hkCapital |
| `get_company_branches` | tianyanchaId/name/businessStatus/legalRepresentative/registeredCapital（含单位文本）/establishmentDate/provinceCode |
| `get_company_investments` | 分支通用字段，加unifiedSocialCreditCode/amount/amountSuffix/percent/subscriptionDate/paidInDate/organizationType/businessScope |
| `get_company_changes` | changeDate/changeItem/before/after/recordCreatedDate |

股东额外参数 `source=1`（工商登记，默认）或 `source=2`（最新公示）；响应 `shareholder_source` / `shareholder_source_name` 标明口径。type=1企业、2自然人、3其他。出资数组可能有多条历史记录，不能求和或认定首条就是当前比例。
分支不承诺信用代码；投资不等于控股；变更日期不等于记录创建日期。司法风险及复杂股权穿透本期未开放。

## 来源、时间与缓存

响应包含 `source`（内部来源标识，不在用户回复中展示原始值）、`cached`、`fetched_at`（原始取数时间）、`queried_at`（本次查询时间）。缓存默认关闭；启用后命中仍按成功查询3积分计费。取数时间不等于源数据更新时间。
供应商故障不冒充空结果，不自动重试超时请求。

## 招投标补充（按需）

| 工具 | 场景 | 积分 |
|---|---|---|
| get_company_profile | 招标/中标次数，company传全称 | 1 |
| search_company | 免费主体候选查询 | 0 |
| get_company_contacts | 招投标联系人；按原返回隐私层级展示 | 5 |
| query_bids_advanced | 中标记录，match_modes=["winner"] | 2 |
| get_company_partners | 合同客户/供应商，与企业股东不同 | 3 |

返回url原样展示，不删改免登录签名；联系人工具的脱敏号码不得自行补全。
