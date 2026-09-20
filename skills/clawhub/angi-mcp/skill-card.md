## Description:

Read angi.com from a shell with the fpx CLI to find home-service pros by trade and city, inspect provider profiles, ratings, reviews, and list trade or city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to gather Angi public directory data through fpx, curl, node, and jq workflows, including provider search results, profile reviews, ratings breakdowns, and taxonomy lookups. Users may also run optional signed-in account examples only when they deliberately want to read their own Angi projects or reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional my.angi.com examples can read private account data from an approved signed-in browser session.

Mitigation: Pair the my.angi.com host and run those commands only when the user explicitly wants the agent to read their own Angi projects or reviews.

Risk: Fetching relies on fpx and the Transporter extension relaying requests through an open browser tab.

Mitigation: Keep host pairing narrow, confirm the intended Angi tab is open, and avoid widening cookie, storage, or header scope.

Risk: Angi page payload fields are undocumented and may be duplicated, absent, or drift over time.

Mitigation: Resolve trade and city slugs from sitemaps, dedupe search records by id, and treat extracted fields as observed page data rather than a stable API contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi public site](https://angi.com/)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi geo sitemap example](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples, JavaScript extractor usage, and JSON or text pipeline outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflows use fpx, curl, node, and jq; optional signed-in account examples can access private account data from an approved browser session.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
