## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing a signed-in browser session cookie once, then calling the Credit Karma GraphQL transactions endpoint directly with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to retrieve their own Credit Karma transaction data through shell commands without installing or running the Credit Karma MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses signed-in Credit Karma cookies, raw access tokens, refresh tokens, and transaction data in shell commands.

Mitigation: Use only on a trusted machine for your own account, avoid shell history and logs, keep secrets in shell variables where possible, and delete transaction and token outputs promptly.

Risk: Temporary files or copied command output can expose financial-session tokens and transaction details.

Mitigation: Replace fixed shared temporary paths with private files using 0600 permissions, and re-sign in or revoke the browser session if a token may have been exposed.

## Reference(s):

- [Credit Karma requests for fpx + curl](artifact/references/requests.md)
- [Credit Karma GraphQL endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma OAuth refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes commands for cookie capture, token refresh, GraphQL pagination, and transaction projection.]

## Skill Version(s):

2.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
