## Description:

IT信息化商机雷达 helps agents find early IT, Xinchuang, digital government, software, systems integration, cloud, data center, cybersecurity, and smart city opportunities by scanning proposed projects, purchase intentions, expiring service contracts, and ranking leads by value and urgency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales teams, and business-development agents use this skill to discover and prioritize early public-sector and enterprise IT opportunities in China. It produces ranked opportunity lists with next-step follow-up guidance from proposed-project, purchase-intention, and expiring-contract data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search terms and opportunity filters to a third-party service.

Mitigation: Install only when this data sharing is acceptable, and avoid entering sensitive internal strategy or confidential customer information as search terms.

Risk: Auto-registration can persist credentials and uses a hashed device identifier when a user has not provided an API key.

Mitigation: Prefer a user-provided ZLBX_API_KEY to skip auto-registration; otherwise confirm consent before registration and review the local credential file.

Risk: Generated sk and auto-login links can grant access through links embedded in chat output or HTML reports.

Mitigation: Treat generated links and exported reports as sensitive, and share them only with recipients who should have access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown opportunity lists, optional self-contained HTML reports, configuration guidance, and concise follow-up recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include signed sk links returned by the third-party service; HTML reports are written as local files when full scans are run.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
