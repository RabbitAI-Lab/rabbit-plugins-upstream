## Description:

Unofficial Go client for the Lovable API, generated with oapi-codegen. Package lovable (github.com/psyb0t/go-lovable) provides lovable.NewClientWithResponses with a typed ...WithResponse method for every endpoint, authenticated with a Lovable-API-Key header or Bearer token. Use when Go code needs to manage Lovable projects, publishing, deployment status, preview embed URLs, analytics, security scans, personal data findings, workspaces, groups or members, or already imports github.com/psyb0t/go-lovable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Lovable's API for project and workspace management, publishing, analytics, and security data through an unofficial typed client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and token-bearing embed URLs can expose workspace access if disclosed.

Mitigation: Use minimally scoped keys, keep credentials out of logs, and share embed links only with intended recipients.

Risk: Publishing, deletion, and settings changes can affect account resources.

Mitigation: Verify the target project and perform these changes only when explicitly requested.

Risk: The Go client is an unofficial dependency.

Mitigation: Review and pin the dependency before adoption.

## Reference(s):

- [go-lovable: setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-lovable)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-lovable)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
