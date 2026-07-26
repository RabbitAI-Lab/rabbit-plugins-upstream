## Description: <br>
依托 LinkedIn 数据库，结合岗位职位、所属企业、所在地区筛选目标人员，帮助销售团队、招聘专员及商务拓展人员精准挖掘企业决策者和潜在商务联系人。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, sales teams, and B2B lead builders use this skill to search LinkedIn person records by name, company, title, industry, geography, and contact-signal filters through the Upkuajing API. It supports small searches and larger paged searches that save task results locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can create billing exposure. <br>
Mitigation: Confirm current pricing and expected call count before paid or large searches, and wait for explicit user approval before running them. <br>
Risk: API credentials are stored locally and could be exposed if the environment file is shared. <br>
Mitigation: Keep ~/.upkuajing/.env private, avoid pasting the API key into chat or logs, and rotate the key if exposure is suspected. <br>
Risk: Search results may include professional and contact-related person data stored in local task output files. <br>
Mitigation: Delete local task_data outputs when no longer needed and ensure searches, storage, and outreach comply with applicable legal and privacy obligations. <br>
Risk: Request or response logging can capture sensitive query inputs or returned data if enabled. <br>
Mitigation: Keep API logging disabled unless needed for troubleshooting, and protect or delete any generated logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-search-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [LinkedIn person list API reference](references/linkedin-person-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON task summaries; retrieved records are saved as JSONL files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; searches can return task_id, status, totals, fee information, and a local result file path.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
