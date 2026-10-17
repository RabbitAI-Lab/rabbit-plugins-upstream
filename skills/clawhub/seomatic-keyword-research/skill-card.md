## Description:

Uses a site's Search Console queries and SEOmatic keyword metrics to prioritize search opportunities and map intent-based keyword clusters to pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and SEO teams use this skill to identify attainable search queries, compare keyword demand and intent, and prioritize updates to existing pages or new content. It can stage proposed work for separate user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the service grants access to site search data.

Mitigation: Review OAuth or API-key permissions before connecting SEOmatic.

Risk: Keyword volume, difficulty, and SERP lookups may consume paid credits.

Mitigation: Review the available allowance and expected credit use before requesting paid lookups.

Risk: Approving a staged SEO task can trigger changes to the site.

Mitigation: Inspect each proposed task and approve only the specific changes you want to run.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/minh42/skills/seomatic-keyword-research)
- [SEOmatic](https://app.seomatic.ai)
- [SEOmatic MCP service](https://app.seomatic.ai/api/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown recommendations and keyword-to-page mapping table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can stage proposed SEO tasks; site changes require approval for each task.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata; skill file declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
