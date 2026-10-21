## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with a Label Studio installation using a typed API client. It helps with endpoint selection, authentication, request and response handling, and safe local integration testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending API credentials or task data to an unintended Label Studio server.

Mitigation: Verify the configured server URL, use HTTPS for remote servers, and keep tokens limited to the resources needed.

Risk: Unrequested changes to projects, tasks, annotations, storage, webhooks, or users.

Mitigation: Perform data-changing operations only when requested and within the user's resource scope.

Risk: Installing an unofficial third-party dependency.

Mitigation: Review and pin the dependency before installation.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Go code examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the selected Label Studio endpoints and caller requirements]

## Skill Version(s):

0.2.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
