## Description:

Checks important site URLs against Google Search Console indexing data, explains exclusions, reviews sitemaps, and proposes fixes for approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and SEO practitioners use this skill to identify important pages missing from Google Search, understand the indexing reason, and review proposed corrections before approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting SEOmatic grants access to Search Console and site SEO data.

Mitigation: Confirm that SEOmatic is trusted before connecting, and use OAuth where possible.

Risk: Incorrect robots.txt, noindex, redirect, or canonical changes may reduce search visibility.

Mitigation: Review each staged task and the affected URL before approval; do not approve changes on the user's behalf.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/minh42/skills/seomatic-indexing-check)
- [SEOmatic](https://app.seomatic.ai)
- [Connect Google Search Console](https://app.seomatic.ai/connect/gsc)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-URL indexing findings, an indexed-page count, and proposed fixes; changes require user approval.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
