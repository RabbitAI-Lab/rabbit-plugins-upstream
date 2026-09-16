## Description:

Access Wikipedia via MCP to search articles, retrieve summaries, facts, featured content, historical events, categories, links, view counts, current news, most-read articles, and structured infobox data across supported language editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, writers, and developers use this skill to retrieve Wikipedia and Wikimedia information for research, content hooks, discovery, trend checks, media lookup, and quick fact extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia search terms, article titles, dates, and coordinates are sent to Wikipedia or Wikimedia APIs.

Mitigation: Avoid sensitive queries or precise locations in restricted environments, and use only where outbound Wikimedia access is acceptable.

Risk: Returned public encyclopedia content may be incomplete, outdated, edited recently, or unsuitable as a sole authority for high-impact decisions.

Mitigation: Review article links and corroborate important claims with primary or authoritative sources before relying on the output.

Risk: The Python dependency should be reviewed in stricter deployment environments.

Mitigation: Pin and scan the requests dependency before installation where supply-chain controls require it.

Risk: The quote tool returns English-only curated quotes rather than Wikipedia data.

Mitigation: Do not treat quote results as live Wikipedia responses or multilingual content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)
- [Wikimedia pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown text with source links, image URLs, lists, and structured fact tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns read-only Wikipedia and Wikimedia lookup results; no API key is required.]

## Skill Version(s):

1.6.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
