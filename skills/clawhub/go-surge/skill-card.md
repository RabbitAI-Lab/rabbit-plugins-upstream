## Description:

Unofficial Go client for the Surge SMS API. Package surge (github.com/psyb0t/go-surge) provides typed REST methods for accounts, audiences, blasts, campaigns, toll-free campaigns, contacts, messages, phone numbers, recordings, users, tokens and verifications. Use when Go code needs Surge SMS operations or already imports go-surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that integrates with the Surge SMS API, including managing messages, contacts, campaigns, accounts, phone numbers, and verifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because three references were unresolved.

Mitigation: Review the installation and setup instructions before installing.

Risk: A bearer token could be exposed if it is hardcoded, committed, or logged.

Mitigation: Read the token from SURGE_API_KEY and do not log the token or Authorization header.

Risk: Sending messages or blasts and managing accounts, contacts, or phone numbers can affect real resources.

Mitigation: Perform these operations only when requested.

Risk: Webhook models are provided without signature verification.

Mitigation: Verify webhook signatures in the receiving application before trusting payloads.

## Reference(s):

- [Setup and API usage notes](references/setup.md)
- [go-surge source repository](https://github.com/psyb0t/go-surge)
- [go-surge package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go toolchain, Surge API token, and account ID are needed for applicable operations.]

## Skill Version(s):

0.5.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
