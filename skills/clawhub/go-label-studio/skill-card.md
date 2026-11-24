## Description:

Provides an unofficial typed Go client and usage guidance for calling the Label Studio API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the go-label-studio client and read or manage Label Studio projects, tasks, annotations, and other API resources from Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan coverage was partial because a referenced AGENTS.md file was unavailable.

Mitigation: Review the available skill materials and resolve the missing reference before relying on the scan as complete.

Risk: API credentials and task or annotation data are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL, use HTTPS for remote servers, and keep API tokens out of source code and logs.

Risk: Creating, updating, or deleting resources changes data on the Label Studio server.

Mitigation: Perform data-changing calls only when requested and on resources within the user's scope.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project repository](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage examples configure the client and make requests to the supplied Label Studio server.]

## Skill Version(s):

0.11.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
