## Description:

Access Wikipedia through MCP tools for article search, summaries, random facts, dinosaur and prehistory facts, featured articles, historical events, article extracts, categories, and multilingual lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and content teams use this MCP server to let an agent retrieve Wikipedia search results, article summaries, full extracts, categories, and daily knowledge hooks across supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and requested article titles are sent to Wikipedia.

Mitigation: Review queries for sensitive content before use and apply outbound network policy appropriate for the deployment.

Risk: The release does not explicitly document outbound network scope or provide a dependency lockfile.

Mitigation: Document the Wikipedia endpoints used by the skill and prefer pinned dependencies or a lockfile for governed deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1 endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown and plain text returned by MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include source links and article images; search terms and requested article titles are sent to Wikipedia.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
