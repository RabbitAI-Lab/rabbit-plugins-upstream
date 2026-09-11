## Description:

Wikipedia MCP lets agents search and retrieve Wikipedia and Wikimedia content, including article summaries, full extracts, links, page views, current events, nearby articles, media, and multi-language entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this MCP skill to give an agent Wikipedia-backed lookup, discovery, media, trends, and current-events capabilities without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia queries, article titles, and nearby-search coordinates may be sent to Wikimedia services.

Mitigation: Avoid sensitive queries or coordinates, and use approved network controls in stricter environments.

Risk: The Python dependency is declared as requests>=2.28.0 rather than pinned with hashes.

Mitigation: Pin and hash the requests dependency before deployment where reproducibility or supply-chain control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)
- [Wikimedia pageviews API endpoint](https://wikimedia.org/api/rest_v1/metrics/pageviews)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links]

**Output Format:** [Markdown strings returned by MCP tool calls, often with source links, image URLs, tables, or lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool calls may perform external requests to Wikimedia services and return current or date-sensitive content.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
