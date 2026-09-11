## Description:

企业情报/背景调查助手，基于知了标讯招投标数据为单个公司或两家公司生成企业背调、画像、客户供应商生态、中标实力、竞争格局和公开风险报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external business users, and agents use this skill to assess companies from a bidding and procurement-data perspective, including supplier due diligence, customer background checks, competitor comparisons, and lightweight commercial research. It supports single-company reports and two-company comparisons with sourced public-data notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives company queries and may receive consent-gated device fingerprint fields during free-trial registration.

Mitigation: Install only when this data sharing is acceptable; prefer a manually provided API key when possible and require explicit user consent before automatic registration.

Risk: The skill stores credentials locally for API access.

Mitigation: Store the API key with strict local permissions and avoid exposing credentials in conversation, reports, or shared files.

Risk: Generated report links can include signed login-bypass parameters.

Mitigation: Treat generated report links and HTML reports as sensitive and avoid sharing files or URLs that contain signed parameters.

Risk: Company-risk summaries can affect real organizations if public-data signals are overstated.

Mitigation: Keep risk language factual, source-linked, and non-accusatory; separate facts from inferences and state data limitations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel)
- [知了标讯 API](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [知了标讯 Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API Quick Reference](references/api-quick.md)
- [Auto Registration Flow](references/auto-register.md)
- [Report Template](references/report-template.md)
- [Seven-Step Workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report plus optional local HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve source URLs returned by the data provider, include data-boundary notes, and avoid unsourced conclusions.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
