## Description:

Guides Go developers in using an unofficial typed client to call the Intercom REST API for customer support and workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add an unofficial Go client to their projects and implement requested Intercom reads or updates with typed API methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Intercom access token could be exposed or used with the wrong regional API host.

Mitigation: Use a least-privilege token, keep it out of source and logs, and select the workspace's regional HTTPS host.

Risk: Create, update, message, export, or delete calls can affect real workspace data.

Mitigation: Review the operation and target resources before running it against a real workspace.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
