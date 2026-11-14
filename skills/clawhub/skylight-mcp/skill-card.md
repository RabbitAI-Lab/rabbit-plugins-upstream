## Description:

Read and manage a signed-in Skylight family hub, including calendars, chores, reward stars, shared lists, and meal plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Households using Skylight can ask an agent to check and manage family calendar events, chores, rewards, shared lists, and meals, as well as related messages, photos, and frame settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review has medium confidence because two local references could not be resolved, so their contents were not assessed.

Mitigation: Resolve and review those references before relying on the clean verdict.

Risk: The skill may activate for broad meal, chore, or shopping requests.

Mitigation: Review the MCP setup and decide whether these household triggers fit your needs.

Risk: The skill uses Skylight account credentials supplied through its MCP environment configuration.

Mitigation: Keep credentials in the MCP environment and out of chat; follow the skill's instruction not to request an Apple app-specific password as a tool argument.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight MCP npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight MCP project repository (linked in the skill documentation)](https://github.com/chrischall/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language summaries, answers, confirmation previews, and action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content reflects the user's Skylight household data and requested actions.]

## Skill Version(s):

1.6.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
