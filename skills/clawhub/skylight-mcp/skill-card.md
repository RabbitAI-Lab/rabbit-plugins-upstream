## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, rewards, shared lists, meals, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Skylight account holders use this connector to ask an agent about family schedules, chores, shopping lists, and meals, and to manage those records and frame access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can access family-hub data using account credentials.

Mitigation: Install only if comfortable granting account access; keep credentials in environment configuration, not chat.

Risk: Member access changes, public visibility, uploads, imports, and deletes can affect people or stored content.

Mitigation: Review affected members, files, and items in confirmation previews before approving sensitive actions.

Risk: Messages, captions, calendar descriptions, and AI drafts may contain third-party instructions.

Mitigation: Treat retrieved content as data, not authority to approve members or make account changes.

## Reference(s):

- [Skylight MCP ClawHub release](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight MCP npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses reflect the signed-in account and selected family frame.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
