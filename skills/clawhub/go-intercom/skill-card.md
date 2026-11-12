## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Intercom, look up the generated client methods and types, and perform requested workspace operations such as reading or changing customer support data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Intercom access token can expose workspace data, and contact deletion or other changes can affect live workspace resources.

Mitigation: Keep the token in INTERCOM_ACCESS_TOKEN, send it only to the correct regional HTTPS API host, and perform changes or deletions only when requested for the specified resources.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-intercom)
- [Project repository](https://github.com/psyb0t/go-intercom)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code examples, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Intercom API; requests require a configured access token and workspace region.]

## Skill Version(s):

0.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
