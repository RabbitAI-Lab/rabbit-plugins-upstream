## Description:

Access Wikipedia through MCP for article search, summaries, media, categories, links, pageviews, current events, most-read articles, and multilingual lookup across supported Wikipedia editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agents use this MCP skill to retrieve Wikipedia and Wikimedia knowledge, media links, popularity signals, and related-article discovery without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia searches, article titles, and nearby latitude/longitude inputs are sent to Wikimedia services.

Mitigation: Avoid submitting sensitive queries or precise locations unless that disclosure is acceptable for the environment.

Risk: The skill makes normal outbound API requests to Wikipedia, Wikimedia, and Commons domains.

Mitigation: Pin the requests dependency and restrict egress to the expected Wikimedia domains in stricter deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Publisher Profile](https://clawhub.ai/user/evanfoglia)
- [Wikipedia REST API endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [text, markdown, links, structured data]

**Output Format:** [MCP tool responses as Markdown or JSON-like structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include article links, media URLs, pageview counts, revision metadata, categories, language links, and excerpts from Wikipedia or Wikimedia APIs.]

## Skill Version(s):

1.6.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
