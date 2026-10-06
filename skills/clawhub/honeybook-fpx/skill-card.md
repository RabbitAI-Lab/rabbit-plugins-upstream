## Description:

Guides agents in reading HoneyBook client-portal contracts, invoices, proposals, payment methods, and workspace data using a browser session and shell commands without the HoneyBook MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized HoneyBook users can capture their signed-in portal session and retrieve client files, workspace details, and saved payment-method information through shell-based API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing and replaying a live session exposes an account token, user ID, and client data to the agent and browser-bridge tooling.

Mitigation: Use only with an account you are authorized to access and only if you trust the agent and browser bridge; limit access to the live session.

Risk: The temporary session file and request headers contain reusable credentials.

Mitigation: Treat them as account credentials, avoid shared machines, keep them out of logs, and promptly remove temporary files.

Risk: The documented messaging flow sends a real email to a vendor.

Mitigation: Do not run the messaging flow unless you intend to send the email; review its recipient and content first.

## Reference(s):

- [HoneyBook FPX release on ClawHub](https://clawhub.ai/chrischall/skills/honeybook-fpx)
- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return sensitive HoneyBook client data as JSON; the messaging example can send a real email.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
