## Description:

Runs SERP and keyword research via the Crawlora API for Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends, returning clean JSON for rankings, snapshots, suggestions, and trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and research agents use this skill to inspect public search rankings, expand keyword ideas, and compare trend signals through Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and JSON request bodies are sent to Crawlora using the user's API key.

Mitigation: Avoid confidential keywords, private locations, sensitive job searches, or sensitive financial research unless third-party API use is acceptable.

Risk: The helper exposes finance, jobs, maps, place reviews/photos, shopping, and local-search endpoints beyond the main SERP and keyword-research description.

Mitigation: Review planned endpoint use before installation or execution, and restrict use to the documented endpoints required for the task.

Risk: The security verdict is suspicious because the skill enables broader third-party API calls than advertised.

Mitigation: Apply the server-provided security guidance during review and confirm the broader Crawlora API surface is acceptable for the deployment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and prints raw JSON responses from Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
