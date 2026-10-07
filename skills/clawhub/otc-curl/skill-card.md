## Description:

Helps agents find local events and deals across On the Cheap city sites using shell queries when the onthecheap MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up free or low-cost local activities, event times, prices and venues, and searchable articles across On the Cheap city sites when the dedicated MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live website requests may return stale or incomplete event and deal listings.

Mitigation: Exclude each site's expired category, verify event dates, and fetch individual day pages for complete schedules.

Risk: Adapting the shell examples to a different site changes where requests are sent.

Mitigation: Review the commands and destination before running them, especially when changing BASE.

## Reference(s):

- [otc-curl on ClawHub](https://clawhub.ai/chrischall/skills/otc-curl)
- [Ready-to-run recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with shell examples and event or article listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings depend on live public city sites; no API key is required.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
