## Description:

An unofficial Go client and usage guide for calling Runway's API with typed methods for generation, task management, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Runway generation and account APIs into an existing project, including constructing authenticated requests, handling typed responses, and polling tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and other request inputs are sent to Runway when API calls are made.

Mitigation: Send only prompts and media that are approved for sharing with Runway.

Risk: Generation can spend organization credits, and cancellation or deletion can affect tasks and other Runway resources.

Mitigation: Keep paid generation and destructive actions explicitly user-directed, and limit them to resources the user created or named.

Risk: An API key can be exposed if it is hardcoded, committed, logged, or included in request output.

Mitigation: Read the key from RUNWAYML_API_SECRET, protect it, and avoid logging or printing request headers.

Risk: The client depends on an unofficial third-party package.

Mitigation: Pin a reviewed dependency version before relying on it in a project.

## Reference(s):

- [go-runway setup and reference](artifact/references/setup.md)
- [go-runway package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)
- [go-runway source repository](https://github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may include authenticated API requests; generation endpoints can spend organization credits.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
