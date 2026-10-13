## Description:

Produces company bidding-history and performance reports from procurement records, with source links and optional side-by-side company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business users review a company's awarded contracts, customers, competitors and publicly reported risks to assess its bidding record or compare two companies. Reports link cited awards to their source notices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External procurement lookups consume trial or paid credits.

Mitigation: Tell users the estimated credit cost before running a report and limit optional lookups.

Risk: Account registration sends device-derived information, and the API key may be stored locally.

Mitigation: Get consent before registration; use a preconfigured key when available and protect the local credentials file.

Risk: Locally saved HTML reports can contain signed, no-login links to platform pages.

Mitigation: Review report contents and access to signed links before sharing or retaining reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile)
- [API quick reference](references/api-quick.md)
- [Report workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Account registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML]

**Output Format:** [Markdown report in chat and a locally saved, shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cited procurement records and signed links to company and notice pages.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
