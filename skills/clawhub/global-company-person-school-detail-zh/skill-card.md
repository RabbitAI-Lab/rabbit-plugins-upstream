## Description: <br>
查询跨境魔方全球企业数据库中的学校详情，包括学校名称、类型、地理位置、网站和社交媒体链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, researchers, analysts, and data enrichment teams use this skill to look up detailed school records by school ID when verifying education history, researching institutions, or enriching organization datasets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs paid API lookups and account recharge actions through the Upkuajing service. <br>
Mitigation: Confirm each billed lookup or recharge action before execution and review pricing or payment URLs before use. <br>
Risk: The skill depends on a private UPKUAJING_API_KEY that may be stored locally. <br>
Mitigation: Keep the API key private, prefer protected environment configuration, and avoid sharing the local credential file contents. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/upkuajing/skills/global-company-person-school-detail-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [School detail API reference](references/school-detail-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON responses and concise Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; school detail lookups are paid API calls and return fee metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
