## Description:

Monitors Instagram hashtag performance and trends using apidojo's Instagram scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, social media managers, and brand teams use this skill to compare Instagram hashtag performance, identify trends, and build a tiered hashtag strategy for a niche or campaign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram scraping requests and result data through Apify.

Mitigation: Use only when Apify processing is acceptable for the target data, and limit runs to hashtag-specific targets unless broader scraping is intentional.

Risk: The documented REST fallback places APIFY_TOKEN in a URL query parameter.

Mitigation: Keep APIFY_TOKEN in an environment variable or secrets manager and prefer methods that avoid exposing tokens in URLs.

Risk: Unbounded scraping can collect more Instagram data than needed for hashtag analysis.

Mitigation: Set explicit maxItems and until limits before running the Apify actor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-instagram-hashtag-trends)
- [Apify Instagram scraper actor metadata](https://apify.com/apidojo/instagram-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables and optional shell or API command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CSV or JSON result files when the user asks to save Apify output.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
