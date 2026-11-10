## Description:

Guides Go developers in using unofficial typed REST and WebSocket clients for eToro's public API and market data streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate eToro account and market data APIs or stream live market, order, and position updates in Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials can expose private financial information if disclosed.

Mitigation: Read keys from environment variables; never hardcode, commit, or log them, and send them only to the documented eToro endpoints.

Risk: Transfers and social actions can move money or publish content.

Mitigation: Keep usage read-only by default and perform each financial or publishing action only when the user explicitly requests that exact action.

Risk: The security assessment covers the supplied guidance, not the external Go implementation or downloaded dependencies.

Mitigation: Review and pin dependencies before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [Project homepage](https://github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use environment variables for API credentials.]

## Skill Version(s):

0.6.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
