## Description: <br>
Plan public transit trips globally using Wheels Router (Hong Kong) and Transitous (worldwide). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anscg](https://clawhub.ai/user/anscg) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to search for locations and plan public transit routes. It is especially detailed for Hong Kong transit, with broader global routing through Transitous-backed coverage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place searches, coordinates, and travel times may reveal sensitive location or travel patterns to the external routing service. <br>
Mitigation: Use the skill only when sharing that travel context is acceptable, and avoid entering sensitive locations unless necessary. <br>
Risk: MCP client setup may execute helper packages through npx. <br>
Mitigation: Use a trusted MCP client configuration and pin or preinstall helper packages where the client allows it. <br>
Risk: Worldwide transit coverage and route detail can vary by city. <br>
Mitigation: Verify important travel plans against local transit sources before time-sensitive use. <br>


## Reference(s): <br>
- [Wheels Router Skill Page](https://clawhub.ai/anscg/skills/wheels-router) <br>
- [Wheels Router MCP Endpoint](https://mcp.justusewheels.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON and shell command examples; MCP tool calls return structured location and route data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses search_location and plan_trip MCP tools; route quality and detail vary by city and data source.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
