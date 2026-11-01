## Description:

Unofficial Go client for the PostGrid print and mail and address verification APIs. Package postgrid (github.com/psyb0t/go-postgrid), generated with oapi-codegen, has typed methods for contacts, templates, letters, postcards, cheques, self mailers, campaigns, mailing lists, reports, webhooks and address verification, authenticated with an API key in the X-API-Key header. Use when Go code needs to send physical mail, manage PostGrid print and mail resources or verify addresses, or already imports go-postgrid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go integrations with PostGrid for managing print and mail resources or verifying addresses. It helps them install the client, configure API-key authentication, select typed operations, and handle responses and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The PostGrid API key could be exposed in source control or logs.

Mitigation: Read POSTGRID_API_KEY from the environment and never hardcode, commit, or log it.

Risk: Live mail creation can send physical mail and incur charges; some verification and list-building operations may also be billable.

Mitigation: Use test credentials during development and confirm recipients, content, and costs before live operations. Create, send, cancel, or delete resources only when requested.

Risk: Addresses and mailing content submitted through the API are sent to PostGrid.

Mitigation: Understand which address and mailing data will be submitted and limit each operation to the requested recipients and content.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-postgrid)
- [go-postgrid repository](https://github.com/psyb0t/go-postgrid)
- [PostGrid overview](https://postgrid.readme.io/docs/overview)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated Go integration code may call PostGrid APIs; live mail and billable operations require user authorization.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
