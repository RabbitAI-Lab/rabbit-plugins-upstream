## Description:

Unofficial Go clients for Kalshi provide typed REST and WebSocket access to markets, account data, and authenticated actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this guidance to integrate Kalshi market and account data or live streams into Go applications. It also explains setup for authenticated account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real-account operations can place or cancel orders, accept quotes, transfer funds between subaccounts, or change API keys.

Mitigation: Use the demo environment while developing, and perform each real-account change only when the user explicitly requests that action.

Risk: The API private key could expose account access if it is hardcoded, committed, logged, or sent to an unintended host.

Mitigation: Keep the key out of source control and logs, protect signed headers, and attach the signer only to Kalshi API clients.

Risk: The Go client is unofficial, and its downloaded dependency code has not been fully audited in this assessment.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-kalshi)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST and WebSocket integration; application code supplies credentials and selects account actions.]

## Skill Version(s):

0.9.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
