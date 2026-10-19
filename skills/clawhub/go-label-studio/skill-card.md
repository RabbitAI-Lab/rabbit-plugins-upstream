## Description:

Guides Go developers in using an unofficial typed client to access Label Studio APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Label Studio for projects, tasks, annotations, imports, exports, and related API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial Go dependency may not meet a project's trust requirements.

Mitigation: Review and approve the module before installation.

Risk: API credentials and task data could be sent to an unintended server or exposed in logs.

Mitigation: Verify the configured server URL, use HTTPS remotely, and keep API keys out of code and logs.

Risk: Create, update, or delete calls can change Label Studio data.

Mitigation: Review the requested operation and resource scope before making changes.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples depend on a Go project and a configured Label Studio server.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
