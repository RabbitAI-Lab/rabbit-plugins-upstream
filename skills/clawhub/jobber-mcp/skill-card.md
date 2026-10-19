## Description:

Reads a customer's Jobber Client Hub appointments, invoices, quotes, and work requests using a signed-in browser tab and shell commands, without the Jobber MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers of businesses using Jobber can read their own appointments, invoices, quotes, and work requests from a signed-in Client Hub tab and use the results in shell scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hub URL grants access to private customer information, including invoice data.

Mitigation: Keep hub URLs private; do not commit or share them or saved hub pages, and delete local copies when no longer needed.

Risk: The CLI and browser extension access a signed-in Jobber tab.

Mitigation: Install only if comfortable granting that access; restrict the bridge to getjobber.com and the fetch capability.

Risk: An incorrect page kind can return an empty list, and amounts extracted from display text can be inaccurate.

Mitigation: Match the parser kind to the page, heed empty-result warnings, and verify important amounts in the hub.

## Reference(s):

- [Jobber MCP ClawHub release](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Usage recipes](references/recipes.md)
- [Why not the Jobber API](references/why-not-the-api.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON]

**Output Format:** [Shell commands and JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only records with hub-relative URLs; no payments, writes, or PDF downloads.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
