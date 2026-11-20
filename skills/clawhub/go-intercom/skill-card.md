## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen, providing typed methods for Intercom workspace data and actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Go package to connect applications to an Intercom workspace, read support and customer data, and perform requested workspace actions such as updating records or replying to conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Intercom access token can access workspace data, and supported calls can send messages or change or delete records.

Mitigation: Use only the scopes needed for the requested work, keep the token in INTERCOM_ACCESS_TOKEN, send it only to the workspace's official regional HTTPS API host, and perform only explicitly requested actions on the specified resources.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-intercom on GitHub](https://github.com/psyb0t/go-intercom)
- [go-intercom package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
