## Description:

Unofficial Go client for the Surge SMS API. Package surge (github.com/psyb0t/go-surge) provides typed REST methods for accounts, audiences, blasts, campaigns, toll-free campaigns, contacts, messages, phone numbers, recordings, users, tokens and verifications. Use when Go code needs Surge SMS operations or already imports go-surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External Go developers use this skill to integrate Go applications with Surge SMS through the unofficial go-surge package, including account, contact, campaign, messaging, phone-number, and verification operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surge tokens grant access to live account resources, and some operations can send messages, create verifications, buy or release phone numbers, or change account and contact data.

Mitigation: Use a suitably restricted token, keep it in SURGE_API_KEY, never hardcode, commit, or log it, and perform side-effecting operations only when explicitly requested.

Risk: The unofficial Go dependency and repository-only references were not verified in the supplied security review.

Mitigation: Review and pin the dependency before use.

Risk: Webhook payload models do not provide signature verification, so payload authenticity is not established by the client.

Mitigation: Implement and validate webhook signature verification separately before trusting received events.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-surge repository](https://github.com/psyb0t/go-surge)
- [go-surge package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
