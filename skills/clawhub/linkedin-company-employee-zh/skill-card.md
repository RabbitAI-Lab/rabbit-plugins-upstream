## Description: <br>
调取 LinkedIn 企业主页数据获取员工清单与整体人员规模，剖析企业内部组织架构，挖掘潜在商务联系人以及核心岗位决策人员。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead builders use this skill to retrieve LinkedIn-sourced employee records for a known company ID, including person IDs and job titles. It supports talent research, organization analysis, contact enrichment, and lead qualification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Upkuajing API workflow for employee-list queries. <br>
Mitigation: Confirm expected fees and pricing before running queries, especially when paginating through additional result pages. <br>
Risk: The skill uses or creates an UPKUAJING_API_KEY and may store it in ~/.upkuajing/.env. <br>
Mitigation: Keep the API key out of conversation logs and shared outputs, and review local credential storage before deployment. <br>
Risk: The skill can generate a recharge payment URL when directed. <br>
Mitigation: Treat recharge flows as user-approved billing actions and verify account context before opening or sharing payment links. <br>


## Reference(s): <br>
- [LinkedIn company employee list API reference](references/linkedin-company-employee-list-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns paginated employee-list data with fee information when the API call succeeds.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
