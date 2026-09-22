## Description:

Access Wikipedia via MCP - search articles, get summaries, random facts, dinosaur facts, today's featured article, today's historical events, article categories, outgoing links, view counts, current news, and most-read articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content teams use this MCP skill to retrieve Wikipedia and Wikimedia lookup results for research, content hooks, article discovery, media discovery, and general knowledge workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, dates, coordinates, and language choices are sent to public Wikimedia services.

Mitigation: Avoid sending private, sensitive, or regulated queries through this skill unless that disclosure is acceptable.

Risk: The external_links tool can return untrusted off-wiki URLs.

Mitigation: Treat returned external URLs as untrusted and review them before opening, sharing, or using them as authoritative sources.

Risk: Deployments that install unpinned dependencies may not be reproducible.

Mitigation: Use pinned or locked dependency versions for production and other repeatable deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1](https://{lang}.wikipedia.org/api/rest_v1)
- [MediaWiki Action API](https://{lang}.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [text, markdown, links, media metadata, guidance]

**Output Format:** [Markdown and plain text MCP tool responses with article links, counts, summaries, tables, and media metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are read-only lookup results from public Wikimedia services; some tools return date-sensitive or language-specific content.]

## Skill Version(s):

1.6.9 (source: server release metadata; artifact frontmatter says 1.1.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
