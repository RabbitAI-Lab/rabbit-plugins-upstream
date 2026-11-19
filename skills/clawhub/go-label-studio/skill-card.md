## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and integrate the unofficial typed Label Studio client, then call project, task, annotation, prediction, and other Label Studio API endpoints from their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports no findings in inspected Markdown but notes a missing referenced path and incomplete coverage.

Mitigation: Check whether the missing path applies to this installation and review or scan that material before use.

Risk: Runtime requests send the API token and task or annotation data to the configured Label Studio server.

Mitigation: Use a trusted server URL, HTTPS for remote servers, and keep tokens out of source control, logs, and request headers.

Risk: Create, update, and delete operations can change Label Studio server data.

Mitigation: Perform changes only when requested and only on resources within the user's scope.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the caller's Label Studio URL and API token; the client package does not read environment variables itself.]

## Skill Version(s):

0.10.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
