## Description:

Guides Go developers using an unofficial Interactive Brokers Web API client to access account data, market data, and user-requested order operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate with the Interactive Brokers Web API through a local Client Portal Gateway or OAuth, including account queries, market data, and explicitly requested order actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order-changing calls can act on a real brokerage account.

Mitigation: Use paper trading during development and perform only the exact order actions the user requests.

Risk: Disabling TLS certificate verification outside a verified local gateway exposes brokerage traffic.

Mitigation: Skip verification only for a verified local gateway with a self-signed certificate; keep verification enabled for other hosts.

Risk: OAuth tokens grant access to a brokerage session.

Mitigation: Read tokens from secure user-managed sources; never hardcode, commit, or log them.

## Reference(s):

- [go-ibkr setup and reference](references/setup.md)
- [go-ibkr package documentation](https://pkg.go.dev/github.com/psyb0t/go-ibkr)
- [ClawHub go-ibkr release](https://clawhub.ai/psyb0t/skills/go-ibkr)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Go toolchain and a user-managed Interactive Brokers authentication session.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
