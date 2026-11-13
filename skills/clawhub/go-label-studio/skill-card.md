## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External developers use this skill to integrate Go applications with Label Studio through the unofficial typed API client, including reading or managing projects, tasks, annotations, predictions, and related resources. It guides setup, authentication, endpoint selection, and safe handling of requests to a chosen Label Studio server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send the configured API token and task or annotation data to the chosen Label Studio server.

Mitigation: Keep the token out of source code and logs, verify the server is trusted, and use HTTPS for remote servers.

Risk: Create, update, and delete calls can change projects, tasks, annotations, storage connections, webhooks, or users on the server.

Mitigation: Confirm the target server and resource scope, and perform data-changing operations only when requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [GitHub repository](https://github.com/psyb0t/go-label-studio)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance; callers supply the Label Studio server URL and API token.]

## Skill Version(s):

0.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
