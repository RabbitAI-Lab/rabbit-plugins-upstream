## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Intercom workspaces, look up API operations and response types, and perform explicitly requested support or customer-data actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending messages, changing customer data, or deleting resources affects the connected Intercom workspace.

Mitigation: Use a token scoped to the needed operations and act only on resources explicitly requested by the user.

Risk: A bearer token could be exposed or sent to the wrong API host.

Mitigation: Read the token from INTERCOM_ACCESS_TOKEN, keep it out of source control and logs, and use the official HTTPS host for the workspace's region.

Risk: The Go client is unofficial and its dependency version may need review before production use.

Mitigation: Review and pin the dependency version before adding it to a production project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-intercom)
- [Project repository](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
