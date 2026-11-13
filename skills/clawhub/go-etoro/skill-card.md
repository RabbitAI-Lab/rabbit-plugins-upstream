## Description:

Helps Go developers use the unofficial go-etoro REST and WebSocket clients for eToro account, market, portfolio, and streaming data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to integrate go-etoro into a project for eToro REST requests and WebSocket updates. It is suited to reading account and market data and, when explicitly requested, using supported account or social actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated endpoints can make money transfers and publish or modify social content.

Mitigation: Default to read-only calls and make transfers or social actions only when the user explicitly requests that exact action.

Risk: API credentials could be exposed through source code, commits, or request logs.

Mitigation: Read keys from ETORO_API_KEY and ETORO_USER_KEY environment variables; do not hardcode, commit, or log them, and send them only to the documented eToro endpoints.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-etoro source repository](https://github.com/psyb0t/go-etoro)
- [go-etoro Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration examples and API usage guidance]

## Skill Version(s):

0.6.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
