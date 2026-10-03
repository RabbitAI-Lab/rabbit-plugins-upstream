## Description:

Guides agents in reading HoneyBook client-portal contracts, invoices, proposals, payment methods, and workspace status through a signed-in browser session and shell requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and HoneyBook clients with an active vendor portal session can inspect shared files, project status, and payment information from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing a live HoneyBook session in a shared temporary file can expose long-lived credentials.

Mitigation: Use a private temporary directory with restrictive permissions, delete captures immediately, and never paste tokens into logs or chat.

Risk: The workflow can access private client and business records in the active portal session.

Mitigation: Use only with an authorized session and limit or redact retrieved records before sharing.

Risk: The documented message-sending request can email the vendor despite the skill's read-oriented description.

Mitigation: Do not run the message-sending POST flow unless explicitly intending to email the vendor; preview the message first.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve private HoneyBook business records; review outputs before sharing.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
