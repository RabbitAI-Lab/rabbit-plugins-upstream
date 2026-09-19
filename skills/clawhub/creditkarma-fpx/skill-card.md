## Description:

Query Credit Karma transactions from a shell with the fpx CLI by capturing a signed-in session cookie and using curl against Credit Karma transaction and refresh endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve Credit Karma transaction data from their own signed-in account in shell workflows without running the creditkarma-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires extracting and reusing live Credit Karma financial session cookies and refresh tokens in shell commands.

Mitigation: Use it only for your own Credit Karma account on a trusted machine, avoid shared terminals, shell history, logs, and predictable temp files, and revoke or sign out of the session if tokens may have been exposed.

Risk: Session values such as CKAT, CKTRKID, ACCESS, and REFRESH can provide access equivalent to an active signed-in financial session.

Mitigation: Keep session values in shell variables when possible and store them only in files with restrictive permissions when persistence is unavoidable.

## Reference(s):

- [Credit Karma requests for fpx + curl](references/requests.md)
- [Credit Karma GraphQL endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma OAuth refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guidance for handling Credit Karma transaction JSON and access-token refresh responses.]

## Skill Version(s):

3.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
