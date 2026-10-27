## Description:

Provides guidance and typed Go examples for using the unofficial go-intercom client to access Intercom workspace data and perform requested operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill when working in Go projects that need Intercom workspace data or a user-requested Intercom action. It helps them install and use the unofficial go-intercom client, understand its typed methods, and handle authentication and responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the bearer token could grant access to the connected Intercom workspace.

Mitigation: Use a token limited to the required operations, read it from INTERCOM_ACCESS_TOKEN, and never hardcode, commit, or log it. Send it only to the HTTPS API host for the workspace's region.

Risk: Intercom write and delete operations can change customer or workspace data.

Mitigation: Perform changes only when requested, and specify the exact resources before requesting changes or deletions.

Risk: The Go client is unofficial and may need review before production use.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-intercom project repository](https://github.com/psyb0t/go-intercom)
- [go-intercom package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and reference guidance for the go-intercom client; no files are produced by the skill.]

## Skill Version(s):

0.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
