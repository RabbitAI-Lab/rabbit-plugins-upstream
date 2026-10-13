## Description:

Reads a customer's Jobber Client Hub appointments, invoices, quotes, and work requests through a signed-in browser tab and returns structured records for shell-based workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to look up their own Jobber Client Hub appointments, invoices, quotes, and work requests from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Jobber hub URL grants access to customer records if exposed.

Mitigation: Treat each hub URL like a password; keep it out of committed files and shared shell history.

Risk: The browser bridge receives fetch access to getjobber.com.

Mitigation: Review the CLI package and browser extension source and release before installation, and grant only the fetch capability required by the skill.

Risk: Account-changing actions or payments require separate safeguards.

Mitigation: Use this skill only for read-only lookup; handle payments and account changes directly in the hub.

## Reference(s):

- [Jobber MCP ClawHub release](https://clawhub.ai/chrischall/skills/jobber-mcp)
- [Usage recipes](artifact/references/recipes.md)
- [Client Hub access and API distinction](artifact/references/why-not-the-api.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON records and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record URLs are hub-relative and omit the hub credential; prefix the user's hub URL to open a record.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
