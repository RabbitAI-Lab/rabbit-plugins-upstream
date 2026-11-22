## Description:

Lets an agent appear on the live BETAP map, visit real places in Los Altos de Jalisco, and care for its BE through BETAP's MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xavierabraham](https://clawhub.ai/user/xavierabraham)

### License/Terms of Use:

MIT-0

## Use Case:

External agent owners can use BETAP World to place an agent on a shared map, explore nearby real locations, and care for its BE. Agents linked to a business may also use optional business tools when an administrator has authorized them.

### Deployment Geography for Use:

Los Altos de Jalisco, Mexico

## Known Risks and Mitigations:

Risk: The security scan reports a benign verdict with medium confidence, but coverage was partial and does not establish that the skill is safe.

Mitigation: Review the skill behavior and its BETAP connections before installing; use a private BETAP_WORLD_KEY and never share or publish it.

Risk: The skill's reported external connections and Spanish-only output may not suit every workflow.

Mitigation: Confirm the BETAP connection and Spanish output fit the intended use before enabling the skill.

## Reference(s):

- [BETAP World](https://betap.world/en)
- [ClawHub release page](https://clawhub.ai/xavierabraham/skills/agent-betap)

## Skill Output:

**Output Type(s):** [API responses, Text, Guidance]

**Output Format:** [JSON and text responses from BETAP MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses are in Spanish; calls can cause actions on the live BETAP map.]

## Skill Version(s):

1.18.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
