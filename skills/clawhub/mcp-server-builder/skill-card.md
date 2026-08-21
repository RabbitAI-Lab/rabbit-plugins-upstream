## Description:

Build MCP servers (Model Context Protocol) that wrap your data and tools, using a FastMCP template and a working example wrapper for the Northcap x402 pay-per-call signals API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create MCP servers that expose service or data endpoints as agent tools. The included example demonstrates an authenticated wrapper for the Northcap x402 pay-per-call signals API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The example sends the user-provided X402_API_KEY in outbound requests to the configured API endpoint.

Mitigation: Verify the endpoint before use, keep the key tightly scoped with spending limits, and avoid logging or committing the key.

Risk: Setting X402_ALLOW_HTTP=1 can send a spending-capable API key over plain HTTP.

Mitigation: Use HTTPS for API_BASE and enable HTTP only when the deployment intentionally accepts that exposure.

Risk: The bundled example endpoint may not match a user's intended service.

Mitigation: Replace the example API_BASE and tool functions when adapting the template for another service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/mcp-server-builder)
- [Northcap Group publisher profile](https://clawhub.ai/user/northcap-group)
- [Configured Northcap signals API endpoint](https://show-zum-anyway-sanyo.trycloudflare.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated guidance is centered on a FastMCP server template that can be adapted to custom endpoints.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
