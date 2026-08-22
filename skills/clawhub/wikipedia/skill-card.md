## Description:

Access Wikipedia via MCP - search articles, get summaries, random facts, dinosaur facts, and today's featured article, with multi-language support across 10 wikis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this MCP server to retrieve Wikipedia search results, article summaries, random articles, daily featured articles, on-this-day events, and topic-specific facts without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries are sent to Wikipedia as part of normal tool operation.

Mitigation: Avoid submitting sensitive or confidential queries unless that external disclosure is acceptable.

Risk: The Python requests dependency is declared without an exact version pin.

Mitigation: Pin or lock dependencies before deployment when reproducibility or supply-chain control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1 endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls]

**Output Format:** [Markdown text returned through MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Wikipedia source links and may include thumbnail image Markdown for article summaries.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
