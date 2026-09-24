## Description:

Guides an agent through reading HoneyBook client-portal data from a shell by capturing an authorized browser session with fpx and then using curl against HoneyBook API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect HoneyBook contracts, invoices, proposals, payment methods, and workspace status from authorized portal sessions without running the HoneyBook MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches users to extract and reuse browser session credentials.

Mitigation: Use only with explicit authorization on accounts and machines the user controls, avoid logging captured values, and delete temporary session captures immediately.

Risk: Captured AUTH_TOKEN, USER_ID, trusted-device values, and session files can function like account credentials.

Mitigation: Treat captured values as secrets and keep them out of world-readable files, shell history, logs, and shared artifacts.

Risk: The artifact describes a message-sending flow that can send real HoneyBook communications.

Mitigation: Do not use the message-sending flow unless intentionally sending a real communication; prefer a preview-capable flow when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [HoneyBook request examples](references/requests.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-handling cautions and HTTP error-handling guidance.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
