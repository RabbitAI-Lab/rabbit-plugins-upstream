## Description:

Helps customers read appointments, invoices, quotes, and work requests from their Jobber Client Hub using a signed-in browser tab and shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to retrieve and inspect their own Jobber Client Hub appointments, invoices, quotes, and work requests from shell scripts without installing the Jobber MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can read signed-in Jobber Client Hub pages.

Mitigation: Use it only if you trust the fpx CLI and ContextMint Bridge, and limit the profile to getjobber.com fetch access.

Risk: A shared hub URL or saved page may expose customer information.

Mitigation: Treat the hub URL and page dumps as sensitive; avoid committing or sharing them, and remove local dumps when finished.

Risk: An incorrect page type or changed page layout can make an empty result misleading.

Mitigation: Match the parser mode to the page and check empty-result warnings before treating a list as complete.

## Reference(s):

- [Jobber MCP skill listing](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Recipes](references/recipes.md)
- [Why not the Jobber API](references/why-not-the-api.md)
- [Client Hub parser](references/parse-clienthub.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Code]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; the bundled parser emits JSON records for selected Client Hub pages.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
