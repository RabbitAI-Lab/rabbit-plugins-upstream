## Description:

Guides developers using an unofficial Go client to access Lovable projects, workspaces, publishing, analytics, and security data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add a typed Go client for Lovable API operations, including reading project and workspace data and performing user-requested project or publishing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lovable API credentials or token-bearing embed URLs could be exposed.

Mitigation: Keep API keys in environment variables, avoid logging authorization headers or embed URLs, and share embed URLs only with intended recipients.

Risk: Project changes, deletions, and publishing actions can alter account resources or access.

Mitigation: Use the narrowest practical API-key scope and confirm the workspace, project, and requested action before executing writes or creating embed URLs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-lovable)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-lovable)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for typed API requests and response handling; no automatic API execution.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
