## Description:

Guides Go developers in using an unofficial, typed Zulip REST API client to read and send messages and manage users, streams, subscriptions, events, uploads, and organization settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial go-zulip client to a Go project, authenticate against a trusted Zulip server, and call typed endpoints for messaging and organization administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and request data are sent to the configured Zulip server.

Mitigation: Verify the trusted HTTPS server address, protect the API key, and use a bot account with only the permissions the integration needs.

Risk: Sending, editing, or deleting messages and changing organization settings can affect live Zulip resources.

Mitigation: Perform these actions only when requested and on the resources specified by the user.

Risk: The external Go dependency is outside the bundled skill guidance review.

Mitigation: Review and pin the dependency before deployment.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [go-zulip project homepage](https://github.com/psyb0t/go-zulip)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-zulip)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-zulip)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration guidance and code examples; the skill itself produces no files.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
