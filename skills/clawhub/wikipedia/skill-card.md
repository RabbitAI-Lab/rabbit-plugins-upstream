## Description:

Access Wikipedia via MCP to search articles, get summaries, random facts, dinosaur facts, today's featured article, today's historical events, article categories, outgoing links, view counts, current news, most-read articles, and lead images across supported Wikipedia languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, developers, and agents use this skill to retrieve public Wikipedia and Wikimedia knowledge for research, content hooks, article discovery, trend checks, and general knowledge workflows without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server performs outbound web requests to Wikipedia and Wikimedia services.

Mitigation: Install only in environments where outbound access to Wikipedia/Wikimedia is acceptable, and apply normal network egress controls where needed.

Risk: The quote tool returns from a small English-only curated list rather than querying Wikipedia.

Mitigation: Use the quote tool for lightweight quote generation, and use article tools when a sourced Wikipedia lookup is required.

Risk: The release depends on requests>=2.28.0 rather than a fully pinned dependency set.

Mitigation: Pin and review dependencies in controlled or reproducible deployment environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Publisher profile](https://clawhub.ai/user/evanfoglia)
- [Wikipedia REST API v1](https://en.wikipedia.org/api/rest_v1/)
- [MediaWiki Action API](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text returned by MCP tools, with article links, image URLs, counts, and short structured sections where relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs depend on live public Wikipedia and Wikimedia responses; the quote tool uses an English-only curated list.]

## Skill Version(s):

1.1.10 (source: server-resolved release evidence; artifact frontmatter reports 1.1.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
