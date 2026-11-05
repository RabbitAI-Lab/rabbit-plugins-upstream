## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate an application with Intercom's REST API for customer support and workspace data. It helps them install the typed client, configure authentication and region-specific endpoints, and make requested API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Intercom bearer token could be exposed or sent to the wrong service.

Mitigation: Read the token from `INTERCOM_ACCESS_TOKEN`, never log or commit it, and use HTTPS with the API host for the workspace's region.

Risk: Messages, customer-data changes, and deletions affect the connected Intercom workspace.

Mitigation: Perform only the actions requested by the user and limit each action to the requested resources.

Risk: The Go client is unofficial and its implementation was outside this review.

Mitigation: Review and pin the dependency before use, and grant the token only the permissions the task needs.

## Reference(s):

- [Setup and API Reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project repository](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
