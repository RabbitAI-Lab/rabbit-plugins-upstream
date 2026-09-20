## Description:

Wikipedia MCP lets agents query Wikipedia and Wikimedia Commons for article summaries, search results, article metadata, media, pageviews, current events, and multilingual public knowledge without an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP server to retrieve public Wikipedia and Wikimedia knowledge, media metadata, edit activity, pageview trends, and discovery links for research, content preparation, and general knowledge workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries and article titles are sent to Wikipedia and Wikimedia services.

Mitigation: Avoid submitting confidential or sensitive queries unless that external network disclosure is acceptable.

Risk: The Python dependency declaration allows any requests version greater than or equal to 2.28.0.

Mitigation: Pin and scan dependencies in managed deployments before installation or promotion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1 endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text and Markdown-formatted MCP tool responses with source links, tables, summaries, counts, and media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are read-only lookup results from public Wikipedia and Wikimedia services; some tools accept language, date, limit, article title, category, media type, or location parameters.]

## Skill Version(s):

1.6.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
