## Description:

Provides a typed Go client and practical guidance for calling the Label Studio API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the client to integrate applications with Label Studio for projects, tasks, annotations, predictions, and related API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task data are sent to the configured Label Studio server.

Mitigation: Use a narrowly scoped API token and verify the HTTPS server address before making requests.

Risk: API operations can change Label Studio projects, tasks, annotations, and other resources.

Mitigation: Authorize changes only for intended resources and review the target operations before running them.

Risk: The Go dependency is unofficial.

Mitigation: Review and pin the dependency before using it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
