## Description:

Provides unofficial, typed Go REST and WebSocket clients for eToro’s public API, with examples for account data and live market streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with eToro’s public REST API or WebSocket streams for account and market data. It guides setup, authentication, endpoint discovery, and handling API responses and stream messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API credentials could be exposed through source code, logs, or printed request headers.

Mitigation: Read keys from ETORO_API_KEY and ETORO_USER_KEY environment variables; do not hardcode, commit, or log them, and do not print requests with their headers.

Risk: Credentials could be sent to a host other than eToro’s documented API endpoints.

Mitigation: Use only https://public-api.etoro.com and wss://ws.etoro.com/ws, and do not attach the keys to requests sent elsewhere.

Risk: Some API operations can transfer money or publish, modify, or delete content.

Mitigation: Call such operations only when the user requests that exact action; default to read-only endpoints.

Risk: Security review completeness is partial because some path-like references were unresolved.

Mitigation: Review unresolved referenced paths before installing.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [Project homepage](https://github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST and WebSocket clients; details depend on the selected API operation and account credentials.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
