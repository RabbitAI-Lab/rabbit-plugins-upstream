## Description:

Unofficial Go client for the Surge SMS API. Package surge (github.com/psyb0t/go-surge) provides typed REST methods for accounts, audiences, blasts, campaigns, toll-free campaigns, contacts, messages, phone numbers, recordings, users, tokens and verifications. Use when Go code needs Surge SMS operations or already imports go-surge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when Go applications need to call the Surge SMS API to manage accounts, audiences, campaigns, contacts, messages, phone numbers, recordings, users, tokens, or verifications. It guides installation and typed client usage in an existing Go project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and flagged API deletion entries; the client also supports operations that modify or remove real Surge resources.

Mitigation: Review the API operations and referenced material before use, and make resource-changing or deletion requests only when explicitly intended.

Risk: Surge bearer tokens could be exposed if included in source code, committed, or logged.

Mitigation: Read the token from SURGE_API_KEY or a secret store, and never hardcode, commit, or log the token or Authorization header.

Risk: The client includes webhook payload models but does not verify webhook signatures.

Mitigation: Verify webhook signatures in the receiving application before trusting event payloads.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)
- [Source repository](https://github.com/psyb0t/go-surge)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage examples and API operation guidance for an existing Go project.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
