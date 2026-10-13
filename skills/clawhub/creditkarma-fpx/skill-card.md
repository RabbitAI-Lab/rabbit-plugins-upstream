## Description:

Guides users through capturing a signed-in Credit Karma session and querying transactions from a shell with fpx and curl instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users of Credit Karma can retrieve and paginate their transaction data from a shell or script without running the Credit Karma MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser session cookies and access or refresh tokens can grant access to sensitive financial data.

Mitigation: Use only on a trusted machine with your own account; keep credentials out of shell history, logs, shared files, and pasted transcripts, and restrict permissions on any saved credentials.

Risk: Saved responses can expose private transaction and account details.

Mitigation: Avoid world-readable temporary files and redact financial details before sharing output.

## Reference(s):

- [Creditkarma Fpx on ClawHub](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and JSON transaction response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use a signed-in browser session to obtain financial transactions.]

## Skill Version(s):

3.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
