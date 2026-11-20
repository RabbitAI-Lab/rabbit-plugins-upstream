## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this unofficial client to add typed calls to a trusted Label Studio installation for managing projects, tasks, annotations, and related API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation content are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL, use HTTPS for remote servers, and keep the API key in configuration such as LABEL_STUDIO_API_KEY without logging it.

Risk: Create, update, and delete operations can change projects, tasks, annotations, storage connections, webhooks, or users on the server.

Mitigation: Run data-changing operations only when requested and only for resources within the user's scope.

Risk: The supplied security review could not resolve the referenced local AGENTS.md, leaving guidance for generated-client changes unchecked.

Mitigation: Locate and review that repository guidance before modifying generated client files.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, API usage guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance depend on the user's Label Studio server and requested operation.]

## Skill Version(s):

0.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
