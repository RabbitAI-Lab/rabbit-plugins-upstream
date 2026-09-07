## Description:

Discovers e-commerce and DTC brands on Instagram and TikTok using apidojo's Apify scrapers, then returns outreach-ready handles, follower counts, bios, product categories, and engagement rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, partnership, wholesale, and SaaS teams use this skill to build outreach lists of e-commerce and DTC brands active on Instagram or TikTok. It helps define category filters, run Apify-based social scraping, filter for commercial brand signals, and rank prospects by engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected hashtag or search inputs and resulting scraping jobs are sent to Apify.

Mitigation: Install only when that data sharing is acceptable for the intended outreach workflow.

Risk: REST examples place APIFY_TOKEN in command URLs, which can expose the token in shell history, logs, notebooks, or chat transcripts.

Mitigation: Prefer the Apify MCP path or helper script flow that keeps APIFY_TOKEN out of URLs, and use scoped or replaceable Apify tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-ecommerce-brands-for-outreach)
- [Apify Instagram scraper actor](https://apify.com/apidojo/instagram-scraper)
- [Apify TikTok scraper actor](https://apify.com/apidojo/tiktok-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table with summary notes and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CSV or JSON file output when the helper script path is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
