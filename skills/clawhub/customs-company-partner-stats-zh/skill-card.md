## Description: <br>
通过企业 ID 查询海关数据中的贸易伙伴结构、HS 编码明细、产品分布和月度贸易日期，帮助外贸团队、采购代理和分析师分析合作伙伴与供应链关系。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade teams, sourcing agents, and analysts use this skill to query company-level customs trade partner distributions and inspect partner, product, HS code, and monthly activity patterns. It supports partner identification, product mix analysis, and trade network intelligence from Upkuajing customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts upkuajing.com and uses a paid API key for data queries. <br>
Mitigation: Provision the API key deliberately, keep it private, and require explicit confirmation before any paid query. <br>
Risk: The skill can store an API key in ~/.upkuajing/.env and includes account recharge/order helper flows. <br>
Mitigation: Prefer manual key provisioning, verify local file permissions, and confirm recharge actions separately before use. <br>
Risk: The security summary notes an automatic version check with local persistence. <br>
Mitigation: Review the version-check behavior before deployment in restricted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-partner-stats-zh) <br>
- [Publisher profile](https://clawhub.ai/user/upkuajing) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [公司贸易伙伴趋势 API 参考](references/customs-company-partner-stats-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [JSON responses with markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API queries require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
