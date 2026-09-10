## Description:

标前分析与投标尽调助手，用于在投标前拆解招标项目、采购方历史、竞争格局、价格基准、风险信号和投标建议，并基于知了标讯招中标数据输出决策报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to decide whether and how to bid on a specific tender before investing proposal effort. It supports project profiling, buyer history review, likely competitor analysis, pricing reference checks, risk review, and a concise bid/no-bid recommendation report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid, project, company, and search queries are sent to Zhiliaobiaoxun services during analysis.

Mitigation: Use the skill only when those query terms are appropriate to share with the provider, and avoid including unnecessary sensitive business context in prompts.

Risk: The skill can persist an API key in ~/.zlbx/config.json.

Mitigation: Prefer manually configured credentials when possible, restrict permissions on the credential file, and avoid pasting API keys into chat.

Risk: Generated reports and returned source links may contain signed or login-bypass URLs.

Mitigation: Review reports before sharing, remove signed links when broad distribution is not intended, and keep generated HTML reports in access-controlled locations.

Risk: Automatic registration uses device-derived identifiers for free-trial deduplication.

Mitigation: Review the auto-registration prompt before consenting, or provide an existing ZLBX_API_KEY to skip automatic registration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [Workflow](artifact/references/workflow.md)
- [API Quick Reference](artifact/references/api-quick.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration Workflow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation, with optional generated self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis normally uses 12-25 API calls; lightweight analysis uses about 5-8 API calls. Reports include cited bid or company records when available, and generated HTML reports are written locally.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
