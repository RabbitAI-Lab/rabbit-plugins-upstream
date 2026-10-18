## Description:

Guides users through retrieving Credit Karma transactions from a signed-in browser session using fpx for cookie capture and curl for API requests, without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Credit Karma account holders use this skill to retrieve and paginate their transactions in shell scripts without running the Credit Karma MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A browser extension and shell commands access live financial-account session cookies and reusable access and refresh tokens.

Mitigation: Review the extension before installing, keep credentials out of logs and shell history, avoid shared machines, and re-sign in or revoke sessions if credentials may have leaked.

Risk: Transaction responses and temporary output files can expose sensitive financial data.

Mitigation: Restrict file permissions, avoid world-readable temporary files, and delete sensitive outputs when no longer needed.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in Credit Karma browser session and the fpx browser extension.]

## Skill Version(s):

3.3.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
