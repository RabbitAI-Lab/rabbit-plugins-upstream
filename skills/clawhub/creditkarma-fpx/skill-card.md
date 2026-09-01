## Description:

Query Credit Karma transactions from a shell by using fpx to capture signed-in session cookies once, then calling Credit Karma GraphQL and refresh endpoints with curl instead of running the creditkarma-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users use this skill to retrieve their Credit Karma transaction data from shell scripts or environments where the MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles Credit Karma session cookies, bearer tokens, refresh tokens, and private transaction history.

Mitigation: Use a dedicated browser profile where possible, keep tokens in shell variables, avoid shared machines, clear shell history and temporary files, and re-sign in or revoke sessions if exposure is suspected.

Risk: The artifact examples write request, transaction, and refresh outputs to temporary files.

Mitigation: Review commands before execution, use paths with restrictive permissions for any temporary files, and remove transaction and refresh outputs after use.

## Reference(s):

- [Credit Karma requests for fpx + curl](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that handle session cookies, bearer tokens, refresh tokens, and transaction responses.]

## Skill Version(s):

2.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
