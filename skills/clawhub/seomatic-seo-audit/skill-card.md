## Description:

Audits a connected site's search performance, indexing, technical health, and AI-search visibility, then prioritizes fixes for user review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and SEO teams use this skill to review connected Search Console and site-audit data, identify prioritized SEO fixes, and optionally stage changes for approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the SEOmatic service exposes site and Search Console data to the connector.

Mitigation: Connect only when intended and review OAuth or API-key access before authorizing it.

Risk: Incomplete crawl coverage or missing data may lead to overstated audit conclusions.

Mitigation: Report partial coverage and missing sources explicitly, and base findings only on returned data.

Risk: Suggested site changes may be unsuitable or incorrect.

Mitigation: Review staged fixes and require user approval before any live change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/minh42/skills/seomatic-seo-audit)
- [SEOmatic](https://app.seomatic.ai)
- [SEOmatic connector setup](https://app.seomatic.ai/dashboard/settings?tab=ai-agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown audit summary and prioritized fix list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses connected site data; identifies partial crawl coverage and separates suggested fixes from approved changes.]

## Skill Version(s):

1.0.1 (source: ClawHub release; skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
