## Description:

Guides Go developers using the unofficial go-surge client to access Surge SMS API resources, including messages, contacts, campaigns, and phone numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Surge SMS operations, such as sending messages and managing contacts, campaigns, and phone numbers, into their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Surge API token could grant unauthorized account access.

Mitigation: Keep SURGE_API_KEY in a protected environment or secret manager; never commit or log it.

Risk: Messaging, token creation, phone-number purchases or releases, and resource changes affect a live account.

Mitigation: Review generated code and confirm live-account actions before running them.

## Reference(s):

- [go-surge setup and reference](references/setup.md)
- [go-surge project homepage](https://github.com/psyb0t/go-surge)
- [go-surge on ClawHub](https://clawhub.ai/psyb0t/skills/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Surge API token for authenticated operations.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
