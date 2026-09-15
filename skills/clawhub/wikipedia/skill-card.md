## Description:

Accesses Wikipedia through MCP to search articles, retrieve summaries and media, inspect links, categories, revisions and pageviews, and surface daily or current-events content across supported language editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to add read-only Wikipedia lookup, media discovery, pageview research, article graph exploration, and daily knowledge hooks to MCP-capable workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia queries, article titles, dates, and coordinates are sent to public Wikimedia services.

Mitigation: Use the skill only where those lookup terms are acceptable to disclose to Wikimedia-operated services.

Risk: The HTTP dependency is declared as requests>=2.28.0 rather than pinned to a reviewed version.

Mitigation: Install in an isolated Python environment and pin requests to an approved version for managed deployments.

Risk: The quote tool returns from a small local English-only curated list rather than Wikipedia.

Mitigation: Treat quote output as local helper content and verify attribution before using it as a source.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1 endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API endpoint](https://wikimedia.org/api/rest_v1/metrics/pageviews/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Markdown-formatted text with source links and optional image or media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses may include links to public Wikimedia pages and media; the quote tool is a local English-only curated add-on.]

## Skill Version(s):

1.6.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
