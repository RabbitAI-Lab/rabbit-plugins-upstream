## Description:

Screens startup launches, public traction signals, verified revenue profiles, and crowdfunding campaigns using Product Hunt, TrustMRR, and Kickstarter through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and analysts use this skill to build dated launch research briefs from public Product Hunt, TrustMRR, and Kickstarter data for startup screening, launch comparison, acquisition research, and campaign tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Startup search terms, product slugs, Kickstarter project identifiers, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for public startup launch research and avoid confidential diligence notes, secrets, or private account data.

Risk: Public launch metrics, revenue-profile fields, reviews, comments, and campaign data can be incomplete, self-reported, revised, or point-in-time.

Mitigation: Preserve collection timestamps and source URLs, keep each evidence type separate, and avoid treating these signals as investment guarantees, delivery proof, or valuation support.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown briefs with inline shell command examples and source-specific cautions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public launch, revenue-profile, and crowdfunding data returned as JSON by Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
