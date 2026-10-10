## Description:

Guides agents in querying and updating Zola wedding-planning data directly from a shell using authenticated API requests, without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Zola account holders and developers use this skill to inspect or manage wedding-planning records, including guests, budgets, events, RSVPs, registries, and websites, from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The long-lived Zola refresh token effectively grants account access and can leak through chats, logs, or shared terminals.

Mitigation: Keep tokens out of chats, logs, and committed files; handle them temporarily and rotate any exposed token.

Risk: Write and delete examples can change live wedding data, and incomplete update bodies can erase unrelated fields.

Mitigation: Back up or export data, confirm each production change, and read the current record before sending a complete update body.

## Reference(s):

- [Zola API endpoint recipes](references/mobile-api-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may contain private wedding-planning information.]

## Skill Version(s):

2.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
