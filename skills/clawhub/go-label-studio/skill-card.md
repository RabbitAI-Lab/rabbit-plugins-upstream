## Description:

Provides an unofficial typed Go client and integration guidance for calling the Label Studio API with token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Label Studio for projects, tasks, annotations, predictions, and related API workflows. It provides typed client usage and authentication guidance for a self-hosted or cloud installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation data could be sent to an unintended Label Studio server.

Mitigation: Use a trusted server URL, use HTTPS for remote servers, and keep the API token out of source control and logs.

Risk: Create, update, and delete operations can change Label Studio server data.

Mitigation: Make data-changing requests only when requested and only for resources within the user's scope.

Risk: This is an unofficial client dependency.

Mitigation: Review and pin the dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go client integration examples and guidance; the agent does not make API calls itself.]

## Skill Version(s):

0.4.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
