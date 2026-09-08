## Description:

Search Google Trends for keyword interest and trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to convert Google Trends requests into Dataify API calls and return trend results for keyword interest, regional interest, related topics, related queries, and optional raw formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Trends query terms, filters, and the Dataify API token are sent to Dataify.

Mitigation: Configure the token through the environment rather than chat, avoid sensitive search terms, and install only when Dataify is an acceptable processor for the intended queries.

Risk: The skill is scoped to Google Trends and may produce misleading results if used as a general web search tool.

Mitigation: Use it only for Google Trends data and route general web search requests to a separate search-capable tool.

Risk: Missing, rejected, or insufficient-credit Dataify credentials can prevent successful retrieval.

Mitigation: Verify that DATAIFY_API_TOKEN is configured without printing its value and use Dataify account management for invalid tokens or credit issues.

## Reference(s):

- [Dataify Google Trends API Reference](references/google_trends_api.md)
- [Dataify skill page](https://clawhub.ai/dataify-server/skills/dataify-google-trends)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)
- [Dataify Dashboard](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API results]

**Output Format:** [Markdown guidance with shell commands, plus Dataify API response output as JSON, HTML, light JSON, or CSV when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token supplied through DATAIFY_API_TOKEN or an explicit token argument; query terms and filters are sent to Dataify.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
