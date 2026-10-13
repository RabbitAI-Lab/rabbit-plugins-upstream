## Description:

Finds early IT procurement opportunities across proposed projects, purchase intentions, and expiring service contracts, then ranks leads and suggests follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to identify and prioritize early IT and domestic-technology procurement leads by industry or region, with suggested next steps for each opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials stored locally during registration may be exposed if the configuration file is shared or accessible to others.

Mitigation: Review credential storage before installing; prefer a preconfigured API key and keep local configuration private.

Risk: Generated reports and links may contain sk or sid tokens that grant access without normal login.

Mitigation: Treat reports and URLs as sensitive; share HTML reports only with intended recipients who should have that access.

Risk: Search queries and consented device-deduplication data are sent to zhiliaobiaoxun.com.

Mitigation: Review external data sharing before use, and use a preconfigured API key to avoid automatic registration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar)
- [API quick reference](artifact/references/api-quick.md)
- [Opportunity scanning workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Registration and privacy guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML report, Guidance]

**Output Format:** [Ranked Markdown opportunity list and, for full scans, a shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists opportunity sources, dates, prioritization reasons, links, and follow-up actions; a full scan requires an API key and may consume credits.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
