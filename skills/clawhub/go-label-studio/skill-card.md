## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with a self-hosted or cloud Label Studio installation. It helps them install and configure the unofficial typed client, call API operations, and handle responses, pagination, credentials, and data-changing requests safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and annotation or task data are sent to the Label Studio server configured by the caller.

Mitigation: Use a trusted server URL, use HTTPS for remote installations, and keep API tokens out of source control, logs, and request-header output.

Risk: Create, update, or delete operations can change projects, tasks, annotations, storage connections, webhooks, or users on the server.

Mitigation: Run data-changing operations only when requested and only on resources within the user’s scope.

Risk: The available security review is incomplete because a referenced AGENTS.md file was unavailable to the scanners.

Mitigation: Review the available skill instructions and relevant repository guidance before installing or applying the client.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-label-studio)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
