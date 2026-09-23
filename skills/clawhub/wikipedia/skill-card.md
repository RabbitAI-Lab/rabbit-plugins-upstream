## Description:

Wikipedia MCP gives agents read-only access to Wikipedia and Wikimedia search, article summaries, media, pageviews, current events, citations, contributors, and multilingual article data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users can use this skill to let an agent retrieve public encyclopedia summaries, article metadata, media, citations, quality signals, contributors, pageviews, and current events from Wikipedia and Wikimedia services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, dates, and coordinates are sent to Wikipedia and Wikimedia services.

Mitigation: Avoid secrets or sensitive internal research topics in queries and install only where public API disclosure is acceptable.

Risk: Responses depend on public, collaboratively edited Wikipedia and Wikimedia content that may be incomplete or change over time.

Mitigation: Use returned source links, article quality, contributors, and references outputs to verify important claims before relying on results.

Risk: The skill depends on live public APIs and the requests package.

Mitigation: Pin dependencies in controlled environments and plan for API availability or response format changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted text with article links, media URLs, tables, citation lists, and short summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public Wikipedia and Wikimedia lookups; most tools support en, de, es, fr, ja, zh, pt, it, ru, and nl.]

## Skill Version(s):

1.6.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
