## Description:

Access OurFamilyWizard (OFW) — messages, calendar, expenses, journal — from a shell with the fpx CLI (@fetchproxy/cli) instead of running the ofw-mcp server: capture the signed-in web app's Bearer token once via the browser bridge, then curl the REST API directly. Use when you want OFW data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OFW account holders can use shell commands to read and manage their own messages, calendar events, expenses, and journal entries without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes can permanently change, share, or delete sensitive family records without a built-in confirmation step.

Mitigation: Use only your own OFW account and approve the exact recipients, records, amounts, attachments, and visibility settings before every change; use a read-only integration for read-only tasks.

Risk: The captured Bearer token provides access to the OFW account.

Mitigation: Protect the token and revoke the browser pairing when finished.

Risk: Opening an unread message marks it as read in OFW.

Mitigation: Avoid retrieving unread message details unless marking them read is intended.

## Reference(s):

- [Request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension notes](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands, curl requests, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can make immediate, externally visible changes to shared OFW records.]

## Skill Version(s):

2.20.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
