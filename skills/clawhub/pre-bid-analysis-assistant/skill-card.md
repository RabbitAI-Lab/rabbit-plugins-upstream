## Description:

Analyzes a specific tender using historical procurement data to inform bid decisions, competitor assessment, pricing, and risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams and procurement analysts use this skill to assess a specific tender, compare historical awards and likely competitors, estimate a pricing range, and decide whether to bid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent API key is stored locally and used to access an external procurement service.

Mitigation: Use a preconfigured key where possible, restrict access to the local credential file, and avoid including the key in reports or messages.

Risk: Optional trial registration sends a hashed device identifier to the vendor.

Mitigation: Request user consent before registration; use an existing API key or manual registration if device fingerprinting is unwanted.

Risk: Shareable reports and citations can contain signed links that bypass login.

Mitigation: Treat exported HTML and citation URLs as sensitive and share only with intended recipients.

Risk: Incomplete or outdated procurement data may affect bid and pricing recommendations.

Mitigation: Flag missing data and uncertainty, verify underlying tender records, and independently review the decision before bidding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant)
- [Analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [API quick reference](references/api-quick.md)
- [Registration and privacy workflow](references/auto-register.md)
- [Publisher skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML]

**Output Format:** [Markdown bid-decision report with HTML export in full mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY; API queries consume account credits. Reports may contain signed citation links.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
