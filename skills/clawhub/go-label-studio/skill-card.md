## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can integrate applications with a self-hosted or cloud Label Studio instance to read or manage projects, tasks, annotations, predictions, and other supported API resources. Use the generated typed client and its reference docs to build and check API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and annotation or task content are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL, HTTPS for remote servers, and a token scoped to the intended resources; keep credentials out of source control and logs.

Risk: Creating, updating, or deleting resources changes Label Studio server data.

Mitigation: Keep data-changing calls explicitly user-directed and limited to resources within the user's scope.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project repository](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Go client integration examples and commands; no files are produced by the library itself.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
