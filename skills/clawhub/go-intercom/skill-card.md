## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add and call the unofficial Go Intercom client for customer support and workspace data, including contacts, companies, conversations, messages, articles and tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom requests carry a bearer token, which could expose workspace data if leaked or sent to an untrusted host.

Mitigation: Read the token from INTERCOM_ACCESS_TOKEN, never hardcode, commit or log it, and send it over HTTPS only to the documented Intercom API host for the workspace region.

Risk: Sending messages, changing customer data and deleting resources affect the connected Intercom workspace.

Mitigation: Perform these operations only when requested and only for the resources the user specified.

Risk: Scanner coverage is incomplete because two references could not be resolved.

Mitigation: Review the skill and its references before installation, taking the incomplete scan coverage into account.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project homepage](https://github.com/psyb0t/go-intercom)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go client calls use typed request and response models; pagination and retries are handled by the caller.]

## Skill Version(s):

0.9.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
