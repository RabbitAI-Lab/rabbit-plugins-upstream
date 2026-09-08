## Description:

Reads HoneyBook client-portal data from a shell via fpx session capture and curl requests to api.honeybook.com, covering contracts, invoices, proposals, payment methods, and workspace status without requiring the HoneyBook MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read HoneyBook client-portal data from scripts or machines where the HoneyBook MCP server is unavailable. It helps agents produce shell setup steps and curl-based read requests after the user has intentionally captured an active browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches reuse of HoneyBook browser session secrets, including authentication tokens and user identifiers.

Mitigation: Use only on a trusted single-user machine, avoid shared terminals and world-readable temporary files, and clean up captured session files after use.

Risk: The artifact describes a message-sending path that can send a real vendor email.

Mitigation: Do not use the message-sending flow unless the user explicitly intends to send email; prefer workflows with a preview step.

Risk: Captured session data may expose contracts, invoices, payment-method metadata, messages, notes, and attachments.

Mitigation: Limit use to authorized HoneyBook sessions and review command output before storing, sharing, or pasting it into other systems.

## Reference(s):

- [HoneyBook request examples](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that read live HoneyBook data when the user supplies an active session.]

## Skill Version(s):

0.10.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
