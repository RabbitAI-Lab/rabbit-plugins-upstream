## Description:

Helps agents research markets, companies, financial filings, SEO, audiences, creators, ads, and public social activity through AIsa.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use AIsa to retrieve market and company intelligence, financial data, search visibility metrics, and public creator and social information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends running an unverified remote installer with local user privileges.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI from a trusted, verified source.

Risk: AIsa requests may transmit sensitive or regulated data to a connected service.

Mitigation: Avoid submitting secrets or regulated data unless your organization approves that use.

## Reference(s):

- [AIsa skill on ClawHub](https://clawhub.ai/oomol/skills/oo-aisa)
- [AIsa](https://aisa.one)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Text or Markdown summaries; structured results may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected AIsa action and connected account access.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
