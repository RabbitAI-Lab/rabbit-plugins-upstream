## Description:

Wikipedia MCP lets agents search Wikipedia and Wikimedia, retrieve article summaries, media, page views, news, events, categories, links, revisions, translations, and structured infobox facts across supported languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users install this MCP server to let agents perform Wikipedia and Wikimedia research, collect article facts and media, inspect article structure and links, and surface current or historical content without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches, article titles, dates, coordinates, and other lookup terms may be sent to public Wikipedia or Wikimedia services.

Mitigation: Avoid secrets, confidential internal names, and sensitive private research terms when using the skill.

Risk: The skill depends on the Python requests package and outbound HTTP access to Wikimedia services.

Mitigation: Pin the dependency in managed environments and restrict outbound access to Wikipedia and Wikimedia domains where appropriate.

Risk: Returned content reflects public Wikipedia and Wikimedia data, which may be incomplete, inaccurate, or changed after retrieval.

Mitigation: Verify important facts against the returned source links before relying on them in high-impact contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links, Media metadata]

**Output Format:** [Markdown-style text with article links, summaries, lists, tables, media URLs, and counts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP tool responses; supported inputs vary by tool and include titles, queries, language codes, dates, limits, coordinates, radius, and media type filters.]

## Skill Version(s):

1.6.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
