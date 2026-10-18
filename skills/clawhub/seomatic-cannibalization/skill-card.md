## Description:

Identifies competing pages for the same search queries using the connected site's Search Console data and recommends SEOmatic fixes for approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and SEO teams use this skill to find meaningful keyword overlap, compare competing pages, choose a preferred page, and propose consolidation, retargeting, redirects, or internal links for approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved SEO changes, especially redirects, can affect traffic and indexed URLs.

Mitigation: Review each staged task and its target URL before approval; explicitly confirm any redirect.

Risk: Recommendations without connected Search Console data could misidentify competing pages.

Mitigation: Connect the site's Search Console account and use its query and page data rather than guessing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/minh42/skills/seomatic-cannibalization)
- [SEOmatic](https://app.seomatic.ai)
- [Connect Google Search Console](https://app.seomatic.ai/connect/gsc)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query and page metrics, a recommended winning page and fix, and optionally up to five SEOmatic tasks staged for approval.]

## Skill Version(s):

1.0.1 (source: server release metadata; skill frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
