## Description:

Finds Chinese procurement intentions before tenders open, alongside proposed projects and expiring contracts, and ranks opportunities with suggested follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams search Chinese public procurement plans by sector, region and budget to identify opportunities one to three months before tendering, track their progress and prioritize outreach. The skill can also scan proposed projects and upcoming contract renewals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement search terms are sent to an external paid API and queries consume credits.

Mitigation: Review the search scope and estimated credit use before scanning; avoid entering confidential terms.

Risk: The API key may be stored locally and exposed if reports or credentials are shared.

Mitigation: Prefer a managed secret for ZLBX_API_KEY; restrict access to local credentials and never include the key in reports.

Risk: Optional trial registration hashes a device MAC address for deduplication.

Mitigation: Obtain consent before registration, or supply an existing API key to skip device registration.

Risk: Report links can include signed, login-free access tokens or auto-login links.

Mitigation: Treat generated reports and signed links as sensitive and share only with intended recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API quick reference](artifact/references/api-quick.md)
- [Scanning workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Trial registration and account access](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Ranked Markdown opportunity list and optional HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and follow-up actions; full scans generate a shareable HTML file.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
