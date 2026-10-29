## Description:

Unofficial Go client for the Surge SMS API. Package surge (github.com/psyb0t/go-surge) provides typed REST methods for accounts, audiences, blasts, campaigns, toll-free campaigns, contacts, messages, phone numbers, recordings, users, tokens and verifications. Use when Go code needs Surge SMS operations or already imports go-surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when adding the go-surge package to a Go project or working with an existing integration. It guides setup and typed Surge SMS API operations, including message handling, account resources, pagination, and response checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surge API credentials could be exposed through source code, commits, or logs.

Mitigation: Read the bearer token from SURGE_API_KEY and do not hardcode, commit, or log it.

Risk: Sending messages, buying or releasing phone numbers, and changing or deleting account resources can affect live services and incur costs.

Mitigation: Perform these actions only when explicitly requested, and review the target account and operation before execution.

Risk: Webhook payload models do not verify webhook signatures.

Mitigation: Implement signature verification separately before trusting webhook events.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-surge)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-surge)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration guidance and examples; the skill does not write files.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
