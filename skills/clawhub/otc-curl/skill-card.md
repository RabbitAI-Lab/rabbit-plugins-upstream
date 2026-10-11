## Description:

Find local events and inexpensive activities on On the Cheap city sites using public web pages and WordPress APIs when the onthecheap MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for free or inexpensive local events and deals can search On the Cheap city sites without the onthecheap MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may go to an unintended city site.

Mitigation: Check the city BASE value before running curl commands.

Risk: Expired deals or incomplete or misdated event listings may mislead users.

Mitigation: Resolve the site's expired category, confirm day-page dates, and fetch full day pages instead of treating the month grid as complete.

## Reference(s):

- [otc-curl on ClawHub](https://clawhub.ai/chrischall/skills/otc-curl)
- [On the Cheap extraction recipes](references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash examples and event or deal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [City-specific public listings and article links; availability and prices should be checked at the source.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
