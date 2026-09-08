## Description:

Search Bing Videos for video results. Do not use for general Bing web search or media-file downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Bing Videos search requests into Dataify Scraper API calls and return video result data. It supports query, market, language, freshness, duration, resolution, source-site, price, cache, and output-format filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Dataify API token for live Bing Videos searches.

Mitigation: Use a session-scoped DATAIFY_API_TOKEN where possible, do not paste the token into chat, and avoid persistent shell configuration unless intentionally required.

Risk: Search queries are sent to Dataify's scraper API during live execution.

Mitigation: Run dry-run previews for parameter review when needed and avoid submitting sensitive search terms unless that external API use is acceptable.

## Reference(s):

- [Dataify Bing Videos API Reference](references/api.md)
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-bing-videos)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Markdown, JSON, Guidance]

**Output Format:** [Markdown, JSON, or raw API response text depending on the requested output mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live calls require DATAIFY_API_TOKEN; dry runs can emit parsed payload JSON or a Markdown parameter table without network access.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
