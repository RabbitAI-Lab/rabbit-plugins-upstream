## Description:

SEO Google helps agents use Google Search Console, PageSpeed Insights, CrUX, Indexing API, GA4, and related Google APIs to retrieve SEO performance, indexation, Core Web Vitals, organic traffic, and keyword data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External SEO practitioners, marketers, and developers use this skill to request live Google SEO data and generate actionable performance, indexation, Core Web Vitals, keyword, and traffic reports for properties they are authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward Google API actions that may affect Search Console, indexing, or sitemap state.

Mitigation: Use least-privilege credentials, avoid Search Console Owner access unless required, and require explicit user confirmation before write, delete, or administrative actions.

Risk: Google API credentials and property data may expose sensitive site, analytics, advertising, or business information.

Mitigation: Store credentials securely, scope service accounts narrowly, and only run the skill for properties the user is authorized to access.

Risk: Natural Language API analysis may send non-public page text to an external Google service.

Mitigation: Redact confidential, personal, or unpublished content before NLP analysis.

Risk: SEO conclusions may be misleading if API lag, quotas, restrictions, or unavailable field data are not explained.

Mitigation: Report data freshness, credential tier, quota limits, and API-specific caveats alongside analysis results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-google)
- [Google API Authentication Setup](references/auth-setup.md)
- [Google Search Console API Reference](references/search-console-api.md)
- [PageSpeed Insights v5 + CrUX API Reference](references/pagespeed-crux-api.md)
- [Google Indexing API v3 Reference](references/indexing-api.md)
- [GA4 Data API v1beta Reference](references/ga4-data-api.md)
- [Google Ads API - Keyword Planner Reference](references/keyword-planner-api.md)
- [Google Cloud Natural Language API Reference](references/nlp-api.md)
- [YouTube Data API v3 Reference](references/youtube-api.md)
- [Supplementary Google APIs for SEO](references/supplementary-apis.md)
- [Google API Rate Limits & Quotas](references/rate-limits-quotas.md)
- [DMA + Consent Mode v2 click-through impact diagnostic](references/dma-consent-mode-v2.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples; generated reports may be Markdown or PDF/HTML through the referenced tooling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential tier checks, data freshness notes, API quota caveats, and optional report templates.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
