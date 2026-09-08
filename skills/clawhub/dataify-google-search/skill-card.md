## Description:

Search Google web results through Dataify and return structured SERP output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to turn Google web search requests into Dataify Scraper API calls and receive concise, source-linked search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search query parameters and API token authorization are sent to Dataify.

Mitigation: Install only when Dataify is an acceptable search provider and use a session-scoped DATAIFY_API_TOKEN unless persistent configuration is intended.

Risk: Searches may consume Dataify account credits.

Mitigation: Confirm high-volume, multi-page, cache-bypassing, or JavaScript-rendered searches before execution because those choices can materially change cost.

Risk: Raw JSON or HTML responses may expose more response details than a concise result summary.

Mitigation: Return compact, user-facing summaries by default and provide raw output only when explicitly requested.

## Reference(s):

- [Dataify Google Search API Reference](references/google_search_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-search)
- [Dataify Dashboard](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with source links, shell commands, configuration guidance, or raw JSON/HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for live API calls; default output is concise search results rather than the full response envelope.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
