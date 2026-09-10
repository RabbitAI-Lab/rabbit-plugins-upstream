## Description:

Analyzes a specific tender project for bid-rejection risk, restrictive signals, buyer history, likely competitors, pricing benchmarks, and go/no-go recommendations using ZhiLiao BiaoXun bid data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to assess whether a concrete procurement opportunity is worth bidding on, including redline risks, competitive openness, incumbent suppliers, and pricing guidance. It is intended for decision-support reports based on public tender and award records, not for making unsourced allegations about buyers or competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and project search terms are sent to the provider service during analysis.

Mitigation: Use the skill only for projects where sharing those search terms with the provider is acceptable.

Risk: The skill may store an API key in ~/.zlbx/config.json.

Mitigation: Prefer a user-managed ZLBX_API_KEY environment variable, and keep any local credential file protected with restrictive filesystem permissions.

Risk: Auto-registration sends a device-linked identifier based on limited local device features.

Mitigation: Preconfigure ZLBX_API_KEY to skip auto-registration, or review the auto-registration prompt before consenting.

Risk: Generated HTML reports and API-returned sk or auto-login links can contain sensitive shareable access links.

Mitigation: Treat exported reports and signed links as sensitive and share them only with intended recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [ZhiLiao BiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiao BiaoXun account and registration service](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation, with optional self-contained HTML report file generated from structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis normally uses 12-25 API calls; quick analysis uses 5-8 API calls. The skill can generate an HTML report under the user's home directory and may preserve API-returned signed links in report outputs.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
