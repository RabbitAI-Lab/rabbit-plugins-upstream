## Description:

Guides agents to capture an existing Credit Karma browser session with fpx and use curl to retrieve transaction pages and refresh access tokens through Credit Karma endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve Credit Karma transaction data from a shell or script when they do not want to run the Credit Karma MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live Credit Karma session cookies, access tokens, refresh tokens, and financial transaction data.

Mitigation: Use it only with a trusted local CLI and browser extension, keep tokens in memory or secure temporary files, and avoid sharing or logging credentials and saved responses.

Risk: Financial credentials or transaction responses may be exposed if written to shared temporary paths or files with weak permissions.

Mitigation: Avoid persisting ACCESS, REFRESH, CKAT, CKTRKID, and response files; if persistence is necessary, use files you control with restrictive permissions.

Risk: A suspected token or cookie exposure could allow access to a signed-in Credit Karma session.

Mitigation: Revoke the session by signing out or reauthenticating, then capture a fresh CKAT and CKTRKID pair before continuing.

## Reference(s):

- [Credit Karma requests for fpx + curl](references/requests.md)
- [Credit Karma skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance for handling session capture, transaction pagination, token refresh, and response checks.]

## Skill Version(s):

2.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
