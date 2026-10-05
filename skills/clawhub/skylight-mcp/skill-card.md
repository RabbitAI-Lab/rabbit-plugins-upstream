## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendar events, chores, shared lists, meals, and frame content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Skylight account holders and their agents use this connector to check and update a family calendar, chores and rewards, shopping lists, meal plans, and other shared frame content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can access sensitive Skylight account and family-hub data.

Mitigation: Use project-scoped configuration and review the npm package before providing account credentials.

Risk: Optional Apple Calendar linking and local uploads can share additional account or file data.

Mitigation: Enable these features only when needed, limit upload directories, and review the confirmation preview before approving.

Risk: Changes to access, recurring entries, or shared content can affect other family members.

Mitigation: Use explicit Skylight wording for sensitive actions and confirm the intended scope and affected items before proceeding.

## Reference(s):

- [Skylight MCP on ClawHub](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight MCP npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, MCP tool calls]

**Output Format:** [Markdown guidance and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private family-hub data; some changes require confirmation.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
