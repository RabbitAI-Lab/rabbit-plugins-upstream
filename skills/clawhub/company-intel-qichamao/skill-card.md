## Description:

Generates company intelligence reports and two-company comparisons from bidding records, covering business activity, customers, suppliers, competitors, and public risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts assess a company's bidding track record, commercial relationships, competitive position, and publicly reported risks, or compare two companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can contain signed access links and generated HTML has a link-escaping flaw.

Mitigation: Treat reports and signed links as sensitive; review generated HTML and links before opening or sharing.

Risk: Automatic trial registration uses a hashed device identifier and can save an API key locally.

Mitigation: Require informed consent before registration; preconfigure your own ZLBX_API_KEY to avoid it, and protect any saved key.

Risk: Company intelligence queries consume account credits.

Mitigation: Check the stated credit estimate before running a report or optional contact lookup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/company-intel-qichamao)
- [API quick reference](artifact/references/api-quick.md)
- [Company intelligence workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Account registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML report]

**Output Format:** [Markdown report in the conversation with an optional shareable HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company or two-company comparison; includes cited bidding records and source links when available.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
