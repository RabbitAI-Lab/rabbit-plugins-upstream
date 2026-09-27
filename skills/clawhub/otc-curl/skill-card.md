## Description:

Helps agents find local events and affordable activities on On the Cheap city sites using public web requests when the dedicated MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up inexpensive local events, deal articles, dates, prices, and venues in participating On the Cheap cities when the dedicated MCP server is unavailable.

### Deployment Geography for Use:

Global; listings cover participating U.S. cities.

## Known Risks and Mitigations:

Risk: Public web requests disclose the queried city, date, and search terms to the selected site.

Mitigation: Use only public queries and avoid sending credentials or private data.

Risk: Expired articles, silently misread date paths, or truncated month views can produce misleading listings.

Mitigation: Resolve the site's expired-category ID, verify the returned day heading, and fetch day pages for complete event listings.

## Reference(s):

- [otc-curl ClawHub release](https://clawhub.ai/chrischall/skills/otc-curl)
- [Query and extraction recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with optional shell commands and event listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on public city-site content and the requested city and date.]

## Skill Version(s):

1.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
