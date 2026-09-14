## Description:

Runs SERP and keyword research via the Crawlora API, returning clean JSON for Google, Bing, Brave, DuckDuckGo, and Yahoo search results plus Google Trends interest-over-time and related or rising queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO analysts, and marketing researchers use this skill to capture SERP snapshots, compare search engines, expand keyword ideas, and inspect Google Trends signals through Crawlora's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and trend queries are sent to Crawlora for third-party processing.

Mitigation: Use only queries your organization permits sending to Crawlora, and avoid secrets, credentials, private customer data, or highly sensitive research topics.

Risk: The helper requires a Crawlora API key.

Mitigation: Store the key in CRAWLORA_API_KEY, avoid hardcoding or committing it, and rotate it if exposure is suspected.

Risk: Search providers may return challenge pages, rate limits, or low-confidence results.

Mitigation: Retry later, switch supported engines, respect documented rate limits, and review returned ranking data before acting on it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/serp-keyword-research)
- [Crawlora website](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and transmits search or trend query content to the Crawlora API.]

## Skill Version(s):

1.0.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
