## Description:

Guides Go developers using an unofficial eToro client for typed REST requests and WebSocket market-data streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add eToro account and market-data requests or live WebSocket subscriptions to Go projects. It helps identify typed client methods, set up authentication, and handle responses and streamed updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed through committed code or request logs.

Mitigation: Load ETORO_API_KEY and ETORO_USER_KEY from environment variables; do not commit or log keys or authenticated request headers.

Risk: Transfers can move real money, while posts and deletes can change public content.

Mitigation: Default to read-only calls and require an explicit user request for each transfer or content-changing action.

Risk: An unofficial client or generated integration code may behave unexpectedly.

Mitigation: Review generated code and transaction or publishing paths before enabling high-impact operations.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [Skill-listed Go client homepage](https://github.com/psyb0t/go-etoro)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance defaults to read-only operations and calls for checking API response status.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
