## Description:

Search Viator tours, activities, attractions, availability, pricing, and destination reference data through the Viator MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-focused agents and their developers use this skill to search Viator products, compare activities and attractions, check availability and pricing, and return booking links for users to complete on Viator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can run remote package code without an exact trusted version pin.

Mitigation: Review the MCP package before use and pin installation to a trusted exact version.

Risk: A Viator API key may be exposed if stored directly in shared MCP configuration.

Mitigation: Use a protected environment or secret manager for VIATOR_API_KEY and rotate the key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full Viator API-derived records, booking URLs, pricing, availability, destination identifiers, and troubleshooting guidance.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
