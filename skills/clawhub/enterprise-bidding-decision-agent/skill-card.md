## Description:

Analyzes a specific bidding opportunity with Zhiliaobiaoxun historical tender data to produce a decision report covering whether to bid, expected competitors, pricing guidance, buyer patterns, and bid-failure risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and bidding teams use this skill to assess a concrete tender, compare buyer and competitor signals, estimate pricing posture, and generate a concise bid/no-bid decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can register accounts with a device fingerprint and store credentials locally.

Mitigation: Require user consent before automatic registration, prefer a user-supplied ZLBX_API_KEY, and review permissions on ~/.zlbx/config.json if the skill creates it.

Risk: Generated reports may preserve signed access links and report contents.

Mitigation: Treat sk and auto-login links as access-bearing links and share generated HTML reports only with intended recipients.

Risk: Bid recommendations can be misleading when source data is incomplete or stale.

Mitigation: Keep the report's data-gap section, cite supporting tender or company records, and make final commercial decisions only after independent review.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent)
- [API quick reference](references/api-quick.md)
- [Bidding analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Automatic registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report, optional self-contained HTML report file, and concise user guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis is documented as approximately 12-25 API calls; quick analysis is documented as approximately 5-8 API calls. Reports must identify data gaps and include a disclaimer.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
