## Description:

依托全球企业数据库，结合姓名、任职公司、所属行业以及个人资料 URL 筛选目标人员，助力外贸从业者找到采购负责人、企业对接人员以及高层决策人。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, B2B lead builders, and cross-border business users use this skill to search global company person records by name, company, industry, country, contact availability, or profile URL. It helps identify contacts, candidates, decision makers, and lead data through the Upkuajing API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs and returned lead data are sent through Upkuajing's API.

Mitigation: Use the skill only when this data sharing is acceptable for the intended sourcing, sales, or lead-generation workflow.

Risk: API calls can incur charges, especially when requesting more than 20 results.

Mitigation: Confirm paid operations before execution and use the pricing command or pricing page for current cost information.

Risk: The API key is stored locally in ~/.upkuajing/.env.

Mitigation: Protect the local environment file, avoid sharing the key, and rotate or remove it if exposure is suspected.

Risk: Generated task_data files may contain personal or business lead data.

Mitigation: Review, retain, share, and delete result files according to the user's data handling requirements.

Risk: Error reports may include context from failed requests.

Mitigation: Do not include secrets in error reports and submit reports only after user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-search-zh)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Developer Platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [全球企业库找人列表搜索 API 参考](references/global-company-person-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses, JSONL result files, and concise Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are appended to task_data result files and include task IDs, status, total hits, request IDs, file paths, and fee information.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
