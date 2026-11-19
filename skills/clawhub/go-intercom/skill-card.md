## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with Intercom customer support and workspace data, and to perform requested Intercom operations through the typed Go client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can access workspace data and perform actions such as sending messages, changing customer data, or deleting resources.

Mitigation: Use only the Intercom token scopes needed for the requested operations, and perform writes or deletions only when requested.

Risk: The security assessment has medium confidence and partial coverage because two references could not be resolved.

Mitigation: Review the referenced guidance and confirm the required token scopes before using the skill.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project repository](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, API Calls, Configuration instructions, Guidance]

**Output Format:** [Go code and concise setup or API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the selected Intercom regional HTTPS endpoint and an access token supplied through INTERCOM_ACCESS_TOKEN.]

## Skill Version(s):

0.10.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
