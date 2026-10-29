## Description:

Writes Go code with go-deribit, an unofficial client for Deribit crypto options and futures generated from Deribit's public specs, covering REST endpoints and WebSocket subscription channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go integrations with Deribit for market data, account information, trading, and WebSocket subscriptions. It helps them find the generated client methods and handle authentication, responses, and account-affecting operations carefully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private requests use account credentials, and some operations can place or cancel orders, transfer funds, or change account settings.

Mitigation: Keep tokens out of source code and logs, develop on testnet, and perform live account actions only when explicitly requested.

Risk: This is an unofficial client and is not affiliated with Deribit.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-deribit source repository](https://github.com/psyb0t/go-deribit)
- [go-deribit package documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
