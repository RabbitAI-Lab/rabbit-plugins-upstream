## Description:

Look up Lowdown's daily observations of an MCP Registry server, including reachability, HTTP status, tool count, and tool-schema changes, through a public read-only API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[petshopbros](https://clawhub.ai/user/petshopbros)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check dated observations of MCP Registry servers, including response status and changes in listed tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Looking up a server discloses its name to lowdown-proxy.vercel.app.

Mitigation: Only query server names you are comfortable sharing with that service.

Risk: Single daily probes can be mistaken for continuous uptime or a security rating.

Mitigation: Include observation dates and describe results as limited observations, not guarantees or ratings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/petshopbros/skills/lowdown-mcp-lookup)
- [Lowdown API schema](https://lowdown-proxy.vercel.app/openapi.json)
- [Lowdown daily observations and raw data](https://github.com/PetShopBros/lowdown-data)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain-language summary of dated observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the latest observation date and relevant status, tool count, or schema changes; does not provide an uptime guarantee or security rating.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
