## Description:

Uses Cue to assess publicly disclosed Chinese equity funds across manager track record, performance attribution, investment style, risk, holdings, fees, and fund size.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and financial advisers use this skill to prepare due-diligence reports on publicly disclosed Chinese equity funds before evaluating a fund or its manager. It analyzes historical performance and risks, not future returns or trade timing.

### Deployment Geography for Use:

Global; analysis covers publicly disclosed Chinese A-share equity funds.

## Known Risks and Mitigations:

Risk: The skill runs an external Cue runner that may change independently of the skill.

Mitigation: Review the external runner before first use in sensitive environments.

Risk: Fund queries and a Cue API key are sent to the Cue service.

Mitigation: Use a Cue-scoped key and avoid sharing it with other services.

Risk: Optional Word or PDF export instructions include package installation with sudo.

Mitigation: Run optional package-install commands only when those export formats are needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-fund-due-diligence)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown due-diligence report with source and original-report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cover fund manager, performance attribution, style, risk, holdings, fees, and fund size; optional Word or PDF export.]

## Skill Version(s):

1.0.10 (source: server-resolved release evidence; artifact frontmatter says 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
