## Description:

Helps Go developers use an unofficial Lovable API client to manage projects, deployments, analytics, security findings, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and operate a Go client for Lovable projects, publishing, deployments, analytics, security scans, and workspace management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or token-bearing embed URLs may be exposed.

Mitigation: Keep keys out of logs, share embed URLs only with intended recipients, and limit key scopes to the task.

Risk: Publishing, deleting, or changing project settings can affect account resources.

Mitigation: Review code paths for these actions and perform them only when the user requests them.

## Reference(s):

- [go-lovable on ClawHub](https://clawhub.ai/psyb0t/skills/go-lovable)
- [Setup and usage reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Lovable API key for API access.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
