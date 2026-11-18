## Description:

Unofficial Go client for the Label Studio API, generated with oapi-codegen. Package labelstudio (github.com/psyb0t/go-label-studio) provides labelstudio.NewClientWithResponses with a typed ...WithResponse method for every endpoint: projects, tasks, annotations, predictions, imports, exports, storage, ML backends, webhooks, users, organizations and workspaces. Auth is an Authorization: Token header added through a request editor, against a self-hosted or cloud server URL. Use when Go code needs to call the Label Studio API, or already imports go-label-studio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with a Label Studio installation through the go-label-studio client, including project, task, annotation, prediction, storage, and administration operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan classified the skill as benign with medium confidence because inspection was partial and a reference to AGENTS.md could not be resolved.

Mitigation: Review that repository guidance if it is relevant to your use before relying on the skill.

Risk: API credentials and task or annotation data are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL and HTTPS for remote servers; keep the token in configuration such as LABEL_STUDIO_API_KEY and never hardcode, commit, or log it.

Risk: Create, update, and delete operations change Label Studio server data.

Mitigation: Perform data-changing operations only when requested and on resources within the user's scope.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Source repository](https://github.com/psyb0t/go-label-studio)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance for the Go client; the caller supplies the Label Studio server URL and API token.]

## Skill Version(s):

0.10.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
