## Description: <br>
调取 LinkedIn 个人档案里面的院校详细资料，获取目标人员就读院校、求学履历和相关学术信息，辅助外贸拓客以及猎头开展背景调研。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External recruiting, research, sales, and data-enrichment users can use this skill to retrieve detailed school records from LinkedIn-derived data by school ID, including name, type, location, website, and social links. The lookup supports education verification, institutional research, and academic network analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls may incur account charges, and the skill includes helper commands for recharge and payment URLs. <br>
Mitigation: Confirm every billable lookup or recharge action before execution and use the vendor pricing reference or price-info command for current pricing. <br>
Risk: The skill reads and can write the Upkuajing API key in ~/.upkuajing/.env. <br>
Mitigation: Prefer manual API-key provisioning, restrict local file permissions, and avoid sharing the key or the credential file. <br>
Risk: The skill contacts the vendor service for school lookups and version checks. <br>
Mitigation: Install only when vendor network access is acceptable for the intended environment and review outbound access policies before deployment. <br>


## Reference(s): <br>
- [LinkedIn 学校详情 API 参考](references/linkedin-school-detail-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-school-detail-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a single school-detail result stream with fee information from the vendor response.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
