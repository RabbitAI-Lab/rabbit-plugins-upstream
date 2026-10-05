## Description:

Guides agents to read and parse a customer's Jobber Client Hub appointments, invoices, quotes, and work requests using a signed-in browser session without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to inspect their own Jobber Client Hub appointments, invoices, quotes, and work requests from a shell or script without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Client Hub URL and fetched invoice or appointment data can expose private account information.

Mitigation: Treat the URL and output as credentials or private data; avoid shared shell history and committed files, and remove saved HTML when no longer needed.

Risk: Fetching through a signed-in browser requires trusting the CLI and browser extension with access to Jobber pages.

Mitigation: Install only if you trust @fetchproxy/cli and ContextMint Bridge, and limit extension site access to getjobber.com.

Risk: Selecting the wrong parser kind can return an empty list that appears to mean there are no records.

Mitigation: Match the parser kind to the fetched page and investigate empty-result warnings before relying on the result.

## Reference(s):

- [Jobber Client Hub recipes](references/recipes.md)
- [Client Hub parser](references/parse-clienthub.mjs)
- [Why not the Jobber API](references/why-not-the-api.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/jobber-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples and JSON parsing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The parser yields JSON records from read-only Client Hub pages; each business has a separate hub.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
