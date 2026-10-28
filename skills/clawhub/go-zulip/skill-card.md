## Description:

Guides Go developers in using the unofficial go-zulip client to read and manage Zulip data through its REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Zulip for reading messages and users, sending messages, and managing organization resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zulip request credentials and content are sent to the configured server.

Mitigation: Use a trusted HTTPS Zulip server, keep API keys out of source control and logs, and use an account or bot with only the permissions needed.

Risk: Sending or changing Zulip messages and organization resources can have effects beyond the local project.

Mitigation: Perform sensitive changes only when requested and on specified resources; review and pin the unofficial dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-zulip source repository](https://github.com/psyb0t/go-zulip)
- [go-zulip package documentation](https://pkg.go.dev/github.com/psyb0t/go-zulip)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-zulip)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage examples and API reference guidance; the skill itself produces no files.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
