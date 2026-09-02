## Description:

Access Wikipedia via MCP to search articles, retrieve summaries and extracts, fetch current and historical daily content, inspect categories and links, view pageview trends, get most-read articles, and retrieve lead image URLs across 10 supported Wikipedia languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to perform Wikipedia-backed research, gather article summaries or full extracts, discover related topics, monitor article popularity, and create content hooks from featured articles, current events, historical events, top reads, and lead images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries are sent to public Wikipedia and Wikimedia APIs.

Mitigation: Use the skill only when it is acceptable for query terms to be shared with Wikipedia/Wikimedia.

Risk: Unpinned dependencies or an incorrect mcporter path can reduce reproducibility or start the wrong local server file.

Mitigation: Pin the requests dependency and verify the mcporter path before enabling the skill in sensitive or reproducible environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API endpoint](https://{lang}.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://{lang}.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API endpoint](https://wikimedia.org/api/rest_v1/metrics/pageviews)

## Skill Output:

**Output Type(s):** [text, markdown, URLs, configuration]

**Output Format:** [Markdown text with article links, image URLs, lists, counts, and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are generated from public Wikipedia and Wikimedia APIs; supported languages are en, de, es, fr, ja, zh, pt, it, ru, and nl.]

## Skill Version(s):

1.1.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
