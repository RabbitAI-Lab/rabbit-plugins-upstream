## Description: <br>
依托 Google-Maps 商业数据库挖掘海外本地企业、线下门店和服务商，可按照所在区域、行业分类、商家评分筛选精准目标客户，助力外贸销售团队完成海外市场布局和线下渠道获客。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, channel development, distribution, brand, and regional market teams use this skill to find offline merchants and local businesses by geography, category, keyword, contact availability, and radius. It supports lead generation, reseller or agent sourcing, competitor location intelligence, local promotion planning, and store network analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an UPKUAJING API key and can store that key in ~/.upkuajing/.env. <br>
Mitigation: Protect the local credential file like any other secret and avoid sharing logs, screenshots, or result bundles that expose credentials. <br>
Risk: Merchant searches can make paid API calls and may create recharge orders when account balance is insufficient. <br>
Mitigation: Review pricing with the provider's price information and require explicit confirmation before large searches or recharge-order flows. <br>
Risk: Large searches can write merchant lead data, addresses, contact details, and task metadata to local files. <br>
Mitigation: Limit query scope to the business need, store result files in an access-controlled location, and delete or archive them according to the user's data-handling policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-map-merchants-search-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [OpenAPI price information](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Merchant search API reference](references/merchants-search-api.md) <br>
- [Country list API reference](references/country-list-api.md) <br>
- [Province list API reference](references/province-list-api.md) <br>
- [City list API reference](references/city-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Merchant search results are saved as local JSONL task files; geography lookups may save local JSON files.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
