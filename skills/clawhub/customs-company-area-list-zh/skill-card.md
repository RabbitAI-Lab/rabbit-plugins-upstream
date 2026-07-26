## Description: <br>
查询公司海关贸易区域列表数据，返回国家/地区的贸易次数、金额、数量、重量和占比，用于市场分析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
外贸团队、市场分析人员和代理开发者用此技能按公司和角色查询国家/地区级贸易分布，评估市场覆盖、重点出口市场和区域贸易占比。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the UpKuajing API key in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Use only on trusted machines, keep the file permissions restricted, and avoid sharing logs or file contents that may expose the key. <br>
Risk: The skill can make paid API calls and can create recharge payment URLs. <br>
Mitigation: Require a separate, explicit user confirmation before fee-incurring queries, recharge orders, or new-key workflows. <br>
Risk: The skill performs a version check against UpKuajing during API use. <br>
Mitigation: Run it only in environments where that outbound check is acceptable and where UpKuajing API access is expected. <br>


## Reference(s): <br>
- [公司贸易区域列表 API 参考](references/customs-company-area-list-api.md) <br>
- [UpKuajing](https://www.upkuajing.com) <br>
- [UpKuajing Developer Platform](https://developer.upkuajing.com/) <br>
- [UpKuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid API calls require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
