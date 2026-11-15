## Description:

Provides Go developers with an unofficial, typed client for reading and managing Zulip messages, users, channels, subscriptions, events, uploads, and organization settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working in Go can use this skill to integrate the unofficial go-zulip package into an application for reading and sending messages or managing Zulip users, channels, subscriptions, events, and organization resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because one local reference could not be resolved.

Mitigation: Review the unresolved reference and the skill contents before installing.

Risk: Zulip credentials and request content are sent to the configured server, and message or organization changes can affect other users.

Mitigation: Use a trusted HTTPS Zulip server, keep credentials in environment variables without logging them, and make changes only to resources the user requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-zulip package documentation](https://pkg.go.dev/github.com/psyb0t/go-zulip)
- [go-zulip project](https://github.com/psyb0t/go-zulip)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage guidance and examples for the typed Go API client; no generated project files.]

## Skill Version(s):

0.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
