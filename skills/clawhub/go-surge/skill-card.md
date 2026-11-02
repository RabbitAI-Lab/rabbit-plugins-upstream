## Description:

Unofficial Go client for the Surge SMS API. Package surge (github.com/psyb0t/go-surge) provides typed REST methods for accounts, audiences, blasts, campaigns, toll-free campaigns, contacts, messages, phone numbers, recordings, users, tokens and verifications. Use when Go code needs Surge SMS operations or already imports go-surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use the unofficial Go client for Surge SMS API operations, including messages, contacts, campaigns, accounts, phone numbers, and verification codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go client is unofficial and its implementation and upstream files are outside this artifact review.

Mitigation: Review and pin the dependency before use.

Risk: The API token and supported operations can affect real accounts, send messages, incur costs, or change resources.

Mitigation: Keep the token out of source control and logs, and require explicit authorization before sending, purchasing, releasing, or changing account resources.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [go-surge repository](https://github.com/psyb0t/go-surge)
- [go-surge package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
