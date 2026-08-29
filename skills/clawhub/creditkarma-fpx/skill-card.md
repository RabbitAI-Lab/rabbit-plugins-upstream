## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing signed-in session cookies once and using curl against Credit Karma transaction and refresh endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to retrieve Credit Karma transaction data in shell workflows without running the creditkarma-mcp server. It provides setup guidance, curl commands, request bodies, pagination handling, and token refresh steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires access to Credit Karma session cookies, refresh tokens, and transaction history.

Mitigation: Run it only in a private local environment, avoid shared machines, keep tokens out of logs and persistent files, clean up temporary response files, and revoke or sign out if credentials may have been exposed.

## Reference(s):

- [Credit Karma requests for fpx + curl](artifact/references/requests.md)
- [Credit Karma GraphQL transactions endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma token refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for cookie capture, GraphQL pagination, auth-error checks, and token refresh; command results may include sensitive financial transaction data.]

## Skill Version(s):

2.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
