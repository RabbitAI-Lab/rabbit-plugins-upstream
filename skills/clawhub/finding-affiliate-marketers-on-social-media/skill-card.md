## Description:

Finds affiliate marketers and performance marketing creators on Instagram and TikTok using apidojo scrapers, returning creator handles, affiliate signal strength, niche focus, engagement rates, promo-code counts, classifications, and relevance scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External affiliate program managers, e-commerce teams, and network managers use this skill to find social media creators who may be running affiliate or performance marketing campaigns for a product category, niche, brand program, or competitor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can place an Apify token in URL query parameters when using REST examples.

Mitigation: Prefer secure token handling through environment variables or trusted tooling, and avoid logging URLs that contain credentials.

Risk: Search terms and scraped result datasets are processed through Apify.

Mitigation: Avoid submitting sensitive brand, competitor, or campaign research terms unless Apify handling and retention are acceptable for the use case.

Risk: The skill claims Instagram and TikTok coverage, while the documented workflow is primarily Instagram-focused.

Mitigation: Confirm the selected Apify actor and platform coverage before relying on TikTok-specific findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-affiliate-marketers-on-social-media)
- [Apify actor: apidojo/instagram-scraper](https://apify.com/apidojo/instagram-scraper)
- [Apify actor: apidojo/tiktok-scraper](https://apify.com/apidojo/tiktok-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries with optional shell commands, JSON, or CSV files from Apify datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include creator handles, platform, affiliate signal strength, niche focus, engagement rate, promo-code count, classification, and relevance score.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter version 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
