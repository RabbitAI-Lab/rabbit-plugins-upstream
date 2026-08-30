## Description:

Read HoneyBook client-portal data, including contracts, invoices, proposals, payment methods, and workspace status, from a shell with fpx and curl after capturing an authorized vendor browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized HoneyBook access use this skill to capture a portal session once and issue read-only curl requests for client portal data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches extraction and reuse of long-lived HoneyBook session credentials that can read sensitive client data.

Mitigation: Use only with authorization, on a private machine, avoid shared /tmp files and shell history, never commit or share captured data, delete captured data immediately, and prefer an official or more contained integration when available.

Risk: Copied commands can place captured session material in temporary files or shell variables.

Mitigation: Keep session values out of shared locations, avoid persisting captured JSON, remove temporary files after extraction, and do not expose token values in logs or command history.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API request examples; requires user-supplied authorized session values.]

## Skill Version(s):

0.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
