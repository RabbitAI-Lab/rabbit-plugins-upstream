## Description:

Queries a company's bid-award history, performance evidence, customer and supplier ecosystem, competitors, and public-risk signals to produce traceable company intelligence reports from Zhiliaobiaoxun bid data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, bid teams, and business-development analysts use this skill to review a company's public bid-award record, verify claimed project experience, compare two companies, and generate a report with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration can collect device-derived fields and provision an account when no API key is configured.

Mitigation: Prefer setting ZLBX_API_KEY yourself, or require explicit user consent before registration and limit collection to the documented platform, architecture, and hashed MAC fields.

Risk: The skill stores credentials locally when it creates or reuses an API key.

Mitigation: Review local credential storage before use and avoid exposing API keys in chat, logs, or generated reports.

Risk: Generated HTML reports and returned company or announcement URLs may contain signed no-login links.

Mitigation: Share reports only with intended recipients and preserve signed links only where the audience is authorized to view them.

Risk: Bid lookups and optional contact lookups consume paid credits and may expose business-contact data.

Mitigation: Tell the user the expected credit cost before running searches and request contact lookups only for legitimate business purposes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun agent portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown company intelligence reports in chat, optional HTML report files, and concise setup or recharge guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for paid API access; reports include source URLs returned by the API and may include signed no-login links.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
