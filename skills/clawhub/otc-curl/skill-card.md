## Description:

Provides curl and jq recipes to find local events and affordable activities across On the Cheap city sites when the onthecheap MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents seeking free or low-cost local activities use this skill to search articles and retrieve daily event listings from On the Cheap city sites without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live requests may reach sites outside the intended On the Cheap network.

Mitigation: Keep target URLs within the intended public city sites and review retrieved content.

Risk: Expired deals, incorrectly parsed dates, or truncated month calendars can misrepresent available events.

Mitigation: Resolve the site's expired-category ID, verify day-page dates, and use full day pages for complete event listings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/otc-curl)
- [Ready-to-run recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and local-event or article summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on live public website responses.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
