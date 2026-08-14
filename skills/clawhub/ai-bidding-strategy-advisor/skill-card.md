## Description:

AI投标策略顾问 helps users analyze a specific procurement project and produce bid/no-bid, pricing, competitor, buyer-profile, risk, and action recommendations grounded in Zhiliaobiaoxun bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to evaluate a concrete bid opportunity, estimate competitive pricing, identify likely competitors, profile the buyer, and prepare a decision report. The skill is intended for procurement strategy support, not as a substitute for independent commercial, legal, or compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a trial account and store a local API key if no API key is already configured.

Mitigation: Prefer configuring ZLBX_API_KEY before use; require explicit user consent before auto-registration or local credential storage.

Risk: The skill sends bidding query terms such as project names, buyer names, and company names to Zhiliaobiaoxun APIs and may include signed access links in generated reports.

Mitigation: Use the skill only for data that may be queried with the provider, and share generated reports and signed links only with intended recipients.

Risk: Bidding recommendations can be incomplete or misleading when source data is missing, stale, or interpreted as a definitive allegation.

Mitigation: Require reports to identify data gaps, separate facts from inferences, avoid accusatory language, and receive human review before business action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor)
- [API quick reference](artifact/references/api-quick.md)
- [Bidding analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report file and supporting JSON input for rendering]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include source citations, data-gap notes, estimated API credit usage, and signed access links returned by the provider API.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
