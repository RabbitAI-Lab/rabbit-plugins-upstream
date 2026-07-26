## Description: <br>
依托全球企业数据库，结合姓名、任职公司、所属行业以及个人资料 URL 筛选目标人员，助力外贸从业者找到采购负责人、企业对接人员以及高层决策人。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead builders use this skill to search global company-person records by name, company, industry, geography, profile URL, and contact availability. It helps an agent prepare and run paid UPKUAJING API searches, handle account setup or recharge flows, and explain results or next steps to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a paid UPKUAJING API account for searches, account setup, and recharge flows. <br>
Mitigation: Review pricing and expected call counts before paid queries, and require explicit user confirmation before cost-incurring actions. <br>
Risk: The API key may be stored in a plaintext file under the user's home directory. <br>
Mitigation: Limit access to the local credentials file, avoid exposing the key in chat or logs, and rotate the key if it may have been shared. <br>
Risk: Search results and task data may be saved locally and can contain business-contact information. <br>
Mitigation: Store result files only where appropriate, review them before sharing, and use the data only for lawful business-contact searches. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/global-company-person-search-zh) <br>
- [全球企业库人物列表 API reference](references/global-company-person-list-api.md) <br>
- [UPKUAJING homepage](https://www.upkuajing.com) <br>
- [UPKUAJING developer platform](https://developer.upkuajing.com/) <br>
- [UPKUAJING OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API/script results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; searches may create or append local result files and can return task IDs, file URLs, account information, pricing information, or payment URLs.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version, SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
