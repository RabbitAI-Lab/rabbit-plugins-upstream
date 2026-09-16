## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing signed-in session cookies once, then using curl against Credit Karma transaction and refresh endpoints instead of running the creditkarma-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically skilled users use this skill to retrieve Credit Karma transaction data in shell workflows without installing or running the MCP server. It provides command guidance for cookie capture, GraphQL transaction pagination, and access-token refresh.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Credit Karma session cookies, access tokens, refresh tokens, and transaction records as raw shell data.

Mitigation: Use only on a trusted machine, avoid shared shells and logs, prefer in-memory shell variables, and store any necessary files with private permissions.

Risk: Session or refresh tokens may be exposed through shell history, temporary files, command output, or copied logs.

Mitigation: Disable or scrub shell history for sensitive commands, avoid writing outputs to shared temporary directories, and re-sign in or revoke sessions if exposure is suspected.

Risk: The workflow depends on a third-party CLI and browser extension path for cookie capture.

Mitigation: Pin and verify CLI dependencies before use and review the installed extension and CLI behavior in the target environment.

Risk: Credit Karma's internal endpoints, persisted query hashes, and response shapes can change without notice.

Mitigation: Check HTTP status and in-body error codes before trusting results, and re-derive request hashes or update parsing when endpoint behavior changes.

## Reference(s):

- [Credit Karma requests for fpx + curl](references/requests.md)
- [Credit Karma GraphQL endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma OAuth refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers fpx setup, cookie capture, curl requests, jq parsing, cursor pagination, and token refresh handling.]

## Skill Version(s):

2.8.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
