## Description:

Helps customers read their Jobber Client Hub appointments, invoices, quotes, and work requests from the shell without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to retrieve their own Jobber Client Hub visits, invoices, quotes, and work requests as JSON for review or scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hub URL or saved page output could expose private billing and account data.

Mitigation: Treat hub URLs and saved HTML or JSON as private; do not commit or share them.

Risk: The browser bridge can fetch data through a signed-in Jobber tab.

Mitigation: Verify the extension release before installing, limit access to getjobber.com, and remove the profile or extension when no longer needed.

## Reference(s):

- [Jobber MCP on ClawHub](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Usage recipes](references/recipes.md)
- [Why not the API](references/why-not-the-api.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with shell examples and parsed JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; requires a signed-in Jobber Client Hub tab and browser bridge.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
