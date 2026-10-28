## Description:

Unofficial Go client for the Lovable API, generated with oapi-codegen. Package lovable (github.com/psyb0t/go-lovable) provides lovable.NewClientWithResponses with a typed ...WithResponse method for every endpoint, authenticated with a Lovable-API-Key header or Bearer token. Use when Go code needs to manage Lovable projects, publishing, deployment status, preview embed URLs, analytics, security scans, personal data findings, workspaces, groups or members, or already imports github.com/psyb0t/go-lovable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that connects to Lovable projects and workspaces, reads project data, and performs requested management or publishing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed workspace credentials or preview embed URLs could grant access to Lovable resources.

Mitigation: Load keys from the environment, use only the required scopes, never log credentials, and share embed links only with intended recipients.

Risk: Project updates, deletion, publishing changes, and publishing or unpublishing affect account resources or access.

Mitigation: Perform these operations only when requested and confirm the intended project before making account changes.

Risk: This is an unofficial client with a Go dependency that may change.

Mitigation: Review and pin the Go dependency before use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-lovable)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise setup or usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code may perform Lovable account changes when requested; credentials and embed links must be kept private.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
