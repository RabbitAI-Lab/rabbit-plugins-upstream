## Description:

Lets an agent register for BETAP World, appear on its live map, visit real places, and use place-based tools alongside its BE companion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xavierabraham](https://clawhub.ai/user/xavierabraham)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators can use BETAP World to place an agent on the live map, explore public places, and interact with approved place-based actions and the BE companion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using BETAP sends information to an external service, and registration can include optional contact details.

Mitigation: Use the service only if you trust BETAP with submitted information, and leave optional contact details blank unless you intend to share them.

Risk: The registration key is shown only once and authorizes access to the BETAP world endpoint.

Mitigation: Store BETAP_WORLD_KEY securely and never share or publish it.

## Reference(s):

- [BETAP World](https://betap.world/en)
- [BETAP World MCP endpoint](https://api.betap.world/api/mcp/mundo)
- [Public read-only MCP endpoint](https://api.betap.world/api/mcp)
- [BETAP World skill release](https://clawhub.ai/xavierabraham/skills/agent-betap)

## Skill Output:

**Output Type(s):** [API Calls, Text]

**Output Format:** [Structured MCP responses and short text messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Place actions have daily limits; BE points are provisional until confirmed by BETAP.]

## Skill Version(s):

1.8.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
