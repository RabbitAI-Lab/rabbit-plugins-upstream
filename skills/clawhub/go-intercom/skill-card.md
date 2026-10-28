## Description:

An unofficial typed Go client for Intercom's REST API, covering admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate the typed go-intercom client into applications that read Intercom workspace data or perform specifically requested Intercom actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom requests can expose workspace or customer data, send messages, or change or delete resources.

Mitigation: Use a token with only the permissions needed, select the workspace region, limit actions to requested resources, avoid logging credentials or customer data, and consider pinning a reviewed dependency version.

## Reference(s):

- [go-intercom setup and reference](artifact/references/setup.md)
- [go-intercom repository](https://github.com/psyb0t/go-intercom)
- [go-intercom package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance for the Go client; actions require an Intercom token and workspace region.]

## Skill Version(s):

0.5.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
