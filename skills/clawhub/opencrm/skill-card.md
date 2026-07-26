## Description: <br>
管理雄韬 XTOCN CRM 客户数据：新增客户（支持企查查/天眼查文本解析）、查询客户（精确/模糊/分页）、修改客户工商信息与联系方式（PATCH 语义）、设置分类标签（分组/等级/行业/来源）。同时支持线索、联系人、跟进记录的创建与查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtoyun](https://clawhub.ai/user/xtoyun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
CRM operators and business teams use this skill through an agent to create, query, edit, and categorize XTOCN CRM customer records, leads, contacts, and follow-up records. The skill requires OPENCRM_KEY and can change live CRM data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated write calls can create or edit live CRM customer, lead, contact, and follow-up records. <br>
Mitigation: Confirm the target company and changed fields with the user before write operations, especially customer add, edit, category update, lead add, contact add, and follow-up add actions. <br>
Risk: The OPENCRM_KEY grants access to the XTOCN CRM API. <br>
Mitigation: Install and run the skill only in environments intended to access that CRM account, and avoid exposing the key in prompts, logs, or user-visible output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xtoyun/skills/opencrm) <br>
- [Publisher profile](https://clawhub.ai/user/xtoyun) <br>
- [XTOCN CRM API base URL](https://my.xtocn.com/api) <br>
- [Field reference](references/fields.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, shell commands, markdown] <br>
**Output Format:** [Markdown guidance with API request details and CRM response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses OPENCRM_KEY for authenticated XTOCN CRM API access; write operations can create or edit live CRM records.] <br>

## Skill Version(s): <br>
1.0.4 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
