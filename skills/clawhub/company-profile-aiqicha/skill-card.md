## Description:

Generates company intelligence and comparison reports from public procurement records, covering business activity, contract relationships, competitors, and public risk information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to assess a company's procurement track record, customer and supplier relationships, competitors, and publicly reported risks, or to compare two companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries are sent to Zhiliaobiaoxun and paid API requests consume account credits.

Mitigation: Review the data-sharing and credit costs before use; confirm the company identity and limit optional queries.

Risk: If no API key is configured, registration collects device-derived features after consent and stores an API credential in ~/.zlbx/config.json.

Mitigation: Set ZLBX_API_KEY yourself to avoid auto-registration, or obtain consent before registering and protect the saved credential.

Risk: Shareable HTML reports and company links include signed sk access parameters.

Mitigation: Treat generated reports and links as access-bearing artifacts and share only with intended recipients.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha)
- [API quick reference](references/api-quick.md)
- [Registration and API key guidance](references/auto-register.md)
- [Company intelligence workflow](references/workflow.md)
- [Report templates](references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown report and shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company or two-company comparison; reports cite data sources and note coverage gaps.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
