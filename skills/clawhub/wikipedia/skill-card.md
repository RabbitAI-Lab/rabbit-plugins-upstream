## Description:

Access Wikipedia via MCP to search articles, get summaries, random facts, dinosaur facts, today's featured article, today's historical events, article categories, outgoing links, view counts, current news, and most-read articles across 10 supported Wikipedia languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and research workflows use this skill to retrieve Wikipedia and Wikimedia information for article lookup, summaries, historical context, category and link discovery, pageview analysis, current events, and trending article research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill adds a persistent mcporter server entry that can make outbound requests to Wikipedia and Wikimedia when invoked.

Mitigation: Install it only in environments where outbound Wikipedia/Wikimedia access is acceptable, and review the mcporter entry before deployment.

Risk: Returned article text, current events, links, and pageview data are external web content.

Mitigation: Review outputs before relying on them in sensitive workflows or publishing them downstream.

Risk: The runtime depends on the Python requests package.

Mitigation: Pin or review the requests dependency according to the deployment environment's dependency-management policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Publisher profile](https://clawhub.ai/user/evanfoglia)
- [Wikipedia REST API](https://{lang}.wikipedia.org/api/rest_v1)
- [MediaWiki Action API](https://{lang}.wikipedia.org/w/api.php)
- [Wikimedia pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/...)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown text responses with links, article summaries, lists, and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses may contain external Wikipedia or Wikimedia content and outbound links.]

## Skill Version(s):

1.1.8 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
