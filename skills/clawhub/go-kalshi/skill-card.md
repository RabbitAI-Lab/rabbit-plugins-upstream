## Description:

Provides an unofficial typed Go client and guidance for Kalshi REST, WebSocket data, and request signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to read Kalshi market and account data, stream market updates, and work with account actions through the unofficial client. Use the demo environment while developing, protect private keys, and make real account changes only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can access an account and perform real transactions when requested.

Mitigation: Use the demo environment while developing and make account changes only when the user explicitly requested them.

Risk: API private keys authorize signed requests.

Mitigation: Keep private keys in environment variables or a user-provided file; never hardcode, commit, or log them.

Risk: The integration is unofficial and depends on a third-party Go module.

Mitigation: Review the dependency version before adding it and confirm that the unofficial client meets the project’s needs.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-kalshi)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST, WebSocket, and authentication examples.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
