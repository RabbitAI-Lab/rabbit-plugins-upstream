## Description:

An unofficial typed Go client for the Intercom REST API, with operations for customer support and workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate applications with Intercom for customer support and workspace data, including reading or changing resources when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom bearer tokens could be exposed through source code or logs.

Mitigation: Read the token from INTERCOM_ACCESS_TOKEN and do not hardcode, commit, or log it or an Authorization header.

Risk: Messages, customer data changes, and deletions affect the connected workspace.

Mitigation: Perform these actions only when requested and only for the resources the user identifies.

Risk: A wrong API host or untrusted pagination URL could receive credentials or target the wrong region.

Mitigation: Use HTTPS and the API host for the workspace's region, and do not attach the bearer token to an untrusted pagination host.

Risk: The unofficial Go dependency may need review, and this release review does not audit downloaded dependency code.

Mitigation: Review and pin the dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-intercom package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [go-intercom project](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
