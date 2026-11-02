## Description:

Guides Go developers using the unofficial go-zulip client to call the Zulip REST API for messages, users, channels, subscriptions, events, uploads, and organization administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with Zulip, including reading and sending messages, managing channels and subscriptions, handling events and uploads, and performing explicitly requested organization changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zulip API credentials can permit account impersonation, and requests send credentials and content to the configured server.

Mitigation: Keep API keys secret, use only the trusted Zulip HTTPS server, and use an account or bot with only the permissions needed.

Risk: Sending or changing messages, users, channels, or organization settings affects the Zulip organization.

Mitigation: Make changes only when requested and only to clearly identified resources.

Risk: The Go client is unofficial and is installed as a project dependency.

Mitigation: Review and pin the dependency before adopting it.

## Reference(s):

- [Setup and API usage reference](artifact/references/setup.md)
- [Declared project homepage](https://github.com/psyb0t/go-zulip)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-zulip)
- [Zulip API key documentation](https://zulip.com/api/api-keys)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-zulip)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains API request setup and response handling; the Go library itself does not write files.]

## Skill Version(s):

0.3.0 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
