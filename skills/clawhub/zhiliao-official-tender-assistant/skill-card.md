## Description: <br>
知了标讯官方招投标数据助手覆盖招标公告、中标结果、企业工商与招中标画像、竞争对手分析、市场趋势统计、采购和中标单位排行、品牌排行、历史中标价格和临期项目商机挖掘。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and business teams use this skill to query and analyze tender notices, award results, company procurement profiles, competitors, market trends, historical prices, and expiring project opportunities through the publisher's tender-data APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First-use automatic registration can send local device and user identifiers to the provider and store an API key under ~/.zlbx/config.json. <br>
Mitigation: Prefer setting ZLBX_API_KEY manually before use, review first-use registration behavior, and treat the local config file as credential-bearing. <br>
Risk: Company contact and procurement results may contain sensitive business or personal data. <br>
Mitigation: Handle returned records according to applicable privacy, confidentiality, and internal data-sharing requirements. <br>


## Reference(s): <br>
- [标讯搜索类工具 API 详情](references/api-search.md) <br>
- [企业分析类工具 API 详情](references/api-company.md) <br>
- [市场分析类工具 API 详情](references/api-market.md) <br>
- [首次使用自动注册流程](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with structured API request and response details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a ZLBX_API_KEY or a locally stored API key for provider API access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
