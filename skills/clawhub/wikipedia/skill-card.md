## Description:

Access Wikipedia via MCP to search articles, get summaries, random facts, dinosaur facts, today's featured article, historical events, categories, outgoing links, view counts, current news, most-read articles, images, media lists, and notable quotes with multi-language support across 10 wikis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users can use this MCP skill to add Wikipedia-backed lookup, research, content discovery, daily history, trend, image, media, and article navigation tools to an agent. It is useful when an agent needs public encyclopedic context or links back to source articles without requiring an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article titles, search queries, and pageview dates are sent to Wikipedia and Wikimedia APIs.

Mitigation: Avoid using secrets, sensitive internal project names, or confidential lookup terms when calling the skill.

Risk: Dependency resolution may vary over time because requirements.txt specifies requests>=2.28.0.

Mitigation: Pin dependencies in the deployment environment when reproducible installs are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API endpoints used by the skill](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint used by the skill](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API endpoint used by the skill](https://wikimedia.org/api/rest_v1/metrics/pageviews)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with source links, article metadata, image URLs, media entries, pageview counts, and setup snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live data returned by Wikipedia or Wikimedia APIs and can vary by language, date, and article availability.]

## Skill Version(s):

1.1.12 (source: server evidence and SERVER_VERSION in src/server.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
