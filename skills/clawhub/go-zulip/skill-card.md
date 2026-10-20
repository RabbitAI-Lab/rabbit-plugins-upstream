## Description:

Guides Go developers in using an unofficial typed client to read and send Zulip messages and manage Zulip resources through its REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on Go applications use this skill to integrate with a trusted Zulip server, including reading or sending messages and managing users, channels, subscriptions, or events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Zulip API key or message content could be disclosed to an unintended server or through logs.

Mitigation: Keep the API key out of source and logs, and connect only to a trusted HTTPS Zulip server.

Risk: Generated code may send, edit, delete, upload, or change organization settings.

Mitigation: Review those actions and their target resources before running the code.

## Reference(s):

- [go-zulip setup and reference](references/setup.md)
- [go-zulip package documentation](https://pkg.go.dev/github.com/psyb0t/go-zulip)
- [Project homepage listed by the skill](https://github.com/psyb0t/go-zulip)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-zulip)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for selecting generated Zulip API methods and checking responses.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
