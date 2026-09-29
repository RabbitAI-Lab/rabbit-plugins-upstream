## Description:

Helps agents read a customer's Jobber Client Hub appointments, invoices, quotes, and work requests from a signed-in browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers of businesses using Jobber can ask an agent to retrieve and summarize their own Client Hub visits, invoices, quotes, and requests, or prepare commands to inspect that data in scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hub URL or saved page output can expose private billing and appointment details.

Mitigation: Keep hub URLs out of shared history and committed files; protect saved HTML and JSON like private billing data.

Risk: The browser bridge can read data from the signed-in Jobber tab.

Mitigation: Verify the CLI and extension sources, approve only the needed fetch capability, and limit extension site access to getjobber.com.

Risk: An empty parsed list may reflect a mismatched page and parser, not an absence of records.

Mitigation: Match the parser kind to the fetched page and check its warning output before treating an empty list as complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Usage recipes](references/recipes.md)
- [Client Hub parser](references/parse-clienthub.mjs)
- [Why not the Jobber API](references/why-not-the-api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Text or Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only customer hub data; parsed lists can include appointments, invoices, quotes, and work requests.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
