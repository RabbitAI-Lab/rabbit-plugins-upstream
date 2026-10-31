## Description:

Guides Go developers in using the unofficial go-lovable client to work with Lovable project, workspace, publishing, analytics, and security APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications and agents with Lovable project and workspace APIs. It guides API reads and user-requested project or publishing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and embed URLs can expose workspace or project access.

Mitigation: Keep credentials in environment-backed secret storage, never log them, and share embed URLs only with intended recipients.

Risk: Project and publishing mutations can change or remove account resources.

Mitigation: Use only the scopes needed, prefer read-only keys for reporting, confirm the intended project, and perform mutations only when requested.

Risk: The Go client is unofficial and should be reviewed before production use.

Mitigation: Review the dependency before adopting it in production.

## Reference(s):

- [Setup and Reference](references/setup.md)
- [go-lovable on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-lovable)
- [go-lovable repository](https://github.com/psyb0t/go-lovable)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
