## Description:

Runs SERP and keyword research through the Crawlora API for Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends, returning clean JSON for rankings, SERP snapshots, keyword suggestions, and trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO analysts, and research agents use this skill to collect search-engine rankings, SERP snapshots, keyword suggestions, and Google Trends signals as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, trend requests, and the Crawlora API key are sent to Crawlora's API.

Mitigation: Use the skill only for queries and credentials that are acceptable under Crawlora's privacy and retention practices, and avoid confidential research terms unless those practices meet the user's requirements.

Risk: A missing or invalid Crawlora API key prevents API requests from succeeding.

Mitigation: Set CRAWLORA_API_KEY in the environment before use and keep the key out of prompts, command arguments, committed files, and query parameters.

Risk: Some search endpoints may return rate-limit, challenge, or unsupported-route responses.

Mitigation: Retry within documented limits, switch to another supported search engine endpoint when appropriate, and consult the bundled endpoint reference for supported routes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/serp-keyword-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends public search terms and trend requests to Crawlora's API.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
