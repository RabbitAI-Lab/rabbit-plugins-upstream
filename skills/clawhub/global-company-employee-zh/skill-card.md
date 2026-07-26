## Description: <br>
依托全球企业数据库查询企业员工清单与人员规模（Headcount），摸清企业内部组织架构，帮外贸销售、猎头从业者挖掘目标企业潜在对接人员。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, B2B lead builders, and market researchers use this skill to retrieve employee lists, role titles, and headcount signals for a company ID from Upkuajing's global company database. It supports talent research, account mapping, decision-maker discovery, and lead qualification workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs paid Upkuajing API lookups and paginated requests can create repeated charges. <br>
Mitigation: Confirm each billable lookup in a separate user message before execution, and use the pricing endpoint or linked price page for current cost information. <br>
Risk: The skill can read or create a local API key file under ~/.upkuajing/.env. <br>
Mitigation: Keep the API key out of shared transcripts, review local file permissions, and avoid printing .env contents unless the user explicitly needs to inspect them. <br>
Risk: The skill contacts third-party Upkuajing services and can cache version-check data under the user's home directory. <br>
Mitigation: Install and run it only when third-party network calls and local cache files are acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-employee-zh) <br>
- [公司员工列表 API 参考](references/company-employee-list-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; API responses may include employee records, pagination cursors, and fee information.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
