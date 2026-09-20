## Description:

Runs SERP and keyword research via the Crawlora API, covering Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends signals, and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and research analysts use this skill to collect search result snapshots, keyword suggestions, and Google Trends signals through Crawlora instead of scraping search result pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, trend terms, and request bodies are sent to Crawlora and may be used to query upstream search services.

Mitigation: Avoid confidential names, secrets, regulated personal data, or private investigation terms unless that external sharing is acceptable.

Risk: The skill requires a Crawlora API key to call the external API.

Mitigation: Keep the key in the CRAWLORA_API_KEY environment variable and do not hardcode it, commit it, or place it in prompts or query parameters.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/serp-keyword-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in the CRAWLORA_API_KEY environment variable.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
