## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers using Go can add typed access to Intercom's REST API for customer support and workspace data. They can use it to inspect resources and, when requested, send messages or make changes to specified Intercom records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An over-scoped or exposed Intercom bearer token could allow access to customer and workspace data.

Mitigation: Use a token scoped to the needed operations, keep it in INTERCOM_ACCESS_TOKEN, and never hardcode, commit, or log it.

Risk: Sending messages, changing customer data, or deleting resources can affect the connected workspace.

Mitigation: Limit actions and changes to the resources the user explicitly requested.

Risk: Credentials could be sent to the wrong API host or an untrusted pagination host.

Mitigation: Use the HTTPS API host for the workspace's region and do not attach the bearer token to an untrusted host.

Risk: A changed dependency version may alter client behavior.

Mitigation: Consider pinning a reviewed dependency version.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-intercom)
- [Project homepage](https://github.com/psyb0t/go-intercom)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the requested Intercom operation, workspace region, and available Go project context.]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
