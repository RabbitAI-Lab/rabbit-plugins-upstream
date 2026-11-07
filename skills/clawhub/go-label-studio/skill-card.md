## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go integrations that call a self-hosted or cloud Label Studio installation through the unofficial typed client. It guides setup, authentication, endpoint selection, pagination, response handling, and safe testing of integration code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or annotation and task data could be sent to an unintended or untrusted server.

Mitigation: Use a trusted HTTPS server and a token limited to the resources needed; verify the configured server belongs to the intended installation.

Risk: Requests that create, update, or delete Label Studio data can have unintended effects.

Mitigation: Make server changes only when explicitly requested and within the user's scope.

Risk: The separately downloaded Go package was outside the security audit.

Mitigation: Review and pin the Go package version before adoption.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance for the caller's selected Label Studio installation.]

## Skill Version(s):

0.7.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
