## Description:

Query the On the Cheap network from the shell with curl and jq for daily local event listings, prices, venues, and searchable articles on free and cheap things to do.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public local event and deal information from On the Cheap city sites when the onthecheap MCP server is unavailable. It helps compose curl, jq, and Python snippets for article searches, event-day lookups, calendar counts, and HTML cleanup.

### Deployment Geography for Use:

Global, for querying public On the Cheap city sites where access is permitted.

## Known Risks and Mitigations:

Risk: The skill makes network requests to public On the Cheap sites through shown curl snippets.

Mitigation: Review commands before running them and use the skill only for public event and deal lookups.

Risk: Fetched article and event text is untrusted web content.

Mitigation: Do not provide credentials or private data to the fetched pages, and treat returned text as data to summarize or inspect rather than as instructions.

Risk: Incorrect date formats, stale expired categories, or truncated month views can produce misleading event or deal results.

Mitigation: Resolve site-specific category IDs, confirm event-page headings, decode titles before display, and fetch day pages for complete listings.

## Reference(s):

- [Ready-to-run recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/otc-curl)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with bash, jq, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq, with optional Python snippets for HTML entity decoding and event-page parsing.]

## Skill Version(s):

1.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
