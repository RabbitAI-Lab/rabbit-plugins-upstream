## Description:

Query Credit Karma transactions from a shell by using fpx to capture a signed-in browser session once, then using curl for transaction reads and token refreshes without running the creditkarma-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to retrieve Credit Karma transaction data in shell workflows when the MCP server is unavailable or unnecessary. It provides setup, request, pagination, token refresh, and response-handling guidance for working with a signed-in Credit Karma session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles Credit Karma session cookies, access tokens, refresh tokens, and financial transaction data in a shell environment.

Mitigation: Keep tokens in shell variables when possible, avoid shell tracing, use private temporary directories and restrictive permissions for any files, delete outputs promptly, and avoid shared machines.

Risk: The browser extension and shell tool need access to Credit Karma session cookies.

Mitigation: Install only after reviewing the toolchain and accepting that access, prefer a pinned and reviewed fpx version, restrict browser site access, and refresh or revoke the Credit Karma session if a token may have been exposed.

Risk: The skill relies on unpublished Credit Karma endpoints and request details that may change without notice.

Mitigation: Check HTTP status and in-body error codes before trusting responses, refresh only on documented auth failures, and re-derive request hashes or recapture the browser session when the documented flow no longer works.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Credit Karma](https://www.creditkarma.com)
- [Credit Karma transactions endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma token refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cookie-capture, pagination, token-refresh, and error-handling guidance.]

## Skill Version(s):

2.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
