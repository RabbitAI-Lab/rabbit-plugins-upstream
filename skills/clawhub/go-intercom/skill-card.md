## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Intercom workspaces through typed API methods for customer support, messaging, conversations, and related data. It helps implement requested Intercom operations in projects using the go-intercom client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom messages, updates, and deletions can affect live customer or workspace data.

Mitigation: Perform changes only when requested, confirm the intended resources, and limit the token to the operations needed.

Risk: The client sends bearer credentials and workspace data to an Intercom API host.

Mitigation: Read the token from INTERCOM_ACCESS_TOKEN, use HTTPS, and select the API host for the workspace’s region.

Risk: The dependency is unofficial and not affiliated with Intercom.

Mitigation: Review the selected release before adding it to a project.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [go-intercom repository](https://github.com/psyb0t/go-intercom)
- [go-intercom package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Intercom API request code for user-requested workspace operations.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
