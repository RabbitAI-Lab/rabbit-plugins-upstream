## Description:

Guides shell-based retrieval of Credit Karma transactions using a captured browser session and direct API requests instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and account holders use this skill to retrieve and inspect their Credit Karma transactions from shell scripts without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension and shell commands can access live Credit Karma session cookies and refresh tokens.

Mitigation: Install only if comfortable granting that access; prefer an official or more contained integration when available.

Risk: Transaction data and session secrets may leak through terminal output, shell history, logs, or temporary files.

Mitigation: Treat all outputs and local traces as sensitive financial-account material; avoid persisting credentials and restrict permissions on any necessary files.

## Reference(s):

- [Credit Karma FPX release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction responses contain sensitive financial-account data.]

## Skill Version(s):

3.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
