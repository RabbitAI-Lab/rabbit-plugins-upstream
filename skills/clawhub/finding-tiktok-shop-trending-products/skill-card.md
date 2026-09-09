## Description:

Finds trending products on TikTok Shop using apidojo's TikTok scraper on Apify, returning product names, creator promotion counts, engagement signals, price ranges, and trend momentum.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External TikTok Shop sellers, affiliates, dropshippers, and e-commerce trend researchers use this skill to discover product trends by analyzing creator promotion density, engagement, pricing, and trend stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify API credentials and search keywords are used with Apify when collecting TikTok Shop trend data.

Mitigation: Install only when Apify use is intended, keep APIFY_TOKEN private, and review queries before running the actor.

Risk: Local JSON or CSV outputs may contain product, creator, engagement, pricing, or keyword data that should not be shared blindly.

Mitigation: Review generated output files before sharing or using them in downstream sourcing and commerce workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-tiktok-shop-trending-products)
- [Apify actor: apidojo/tiktok-scraper](https://apify.com/apidojo/tiktok-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown report with tables, optional shell commands, and optional JSON or CSV result files from Apify actor runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trend scores are derived from TikTok engagement fields and creator promotion counts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
