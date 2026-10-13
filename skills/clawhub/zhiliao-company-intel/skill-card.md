## Description:

Produces company background reports from Chinese tender and award records, including customer relationships, competitors, and an optional two-company comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, procurement, and due-diligence users assess a company or compare two companies using public tender and award records, with a conversational report and a shareable local HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trial registration uses a hashed device identifier.

Mitigation: Obtain user consent before registration, or use an existing API key to skip registration.

Risk: Registration persists an API key under the user's home directory.

Mitigation: Restrict access to the key file and do not include the key in reports or shared messages.

Risk: Shareable HTML reports can contain signed links that bypass normal login.

Mitigation: Share reports only with intended recipients and review embedded links before distribution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel)
- [API quick reference](references/api-quick.md)
- [Report workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Account registration and key handling](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML files]

**Output Format:** [Conversational report and local HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company or two-company comparison; reports may contain signed access links.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
