## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, shared lists, meals, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and families with a Skylight account use an agent to check and update their family calendar, chores, shopping lists, meal plans, and frame membership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires a Skylight account password in local configuration.

Mitigation: Prefer project-scoped configuration, restrict file permissions, and review the package before use.

Risk: The connector can change family hub data, access, invitations, and linked calendars.

Mitigation: Review confirmation previews before approving uploads, access changes, bulk deletes, invitations, or Apple calendar linking.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirmation previews may require explicit approval before a change is made.]

## Skill Version(s):

1.4.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
