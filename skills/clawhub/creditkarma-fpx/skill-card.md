## Description:

Query Credit Karma (creditkarma.com) transactions from a shell with the fpx CLI (@fetchproxy/cli) instead of running the creditkarma-mcp server, by capturing the signed-in session cookie once and calling the GraphQL transactions endpoint directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and personal finance automation users use this skill to capture an existing Credit Karma browser session and fetch transaction data from shell scripts without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Credit Karma session cookies plus raw access and refresh tokens.

Mitigation: Use it only on trusted machines, keep tokens in session-scoped shell variables where possible, avoid writing tokens or transaction responses to shared temporary locations, remove any temporary files created by examples, and sign out or revoke sessions if exposure is suspected.

Risk: The workflow depends on a CLI and browser extension that can access Credit Karma cookies.

Mitigation: Review the tooling before installation, use a pinned and verified dependency, and avoid pairing or running the workflow on shared machines.

Risk: The requests use reverse-engineered Credit Karma endpoints and safelisted operation hashes that may change without notice.

Mitigation: Treat failures and schema drift as operational errors, re-check the documented request shape before use, and avoid relying on the workflow for critical financial operations without human review.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for cookie capture, token refresh, paginated GraphQL requests, and response inspection.]

## Skill Version(s):

2.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
