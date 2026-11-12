## Description:

Helps Go developers use the unofficial typed go-label-studio client to call Label Studio APIs with token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with a self-hosted or cloud Label Studio installation. It guides them in configuring the typed client, authentication, and API calls for reading or managing Label Studio resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security analysis is marked partial because a reference to AGENTS.md could not be resolved.

Mitigation: Review the skill instructions and setup details before installation if that missing repository context could affect your use.

Risk: Runtime requests send API credentials and task data to the configured Label Studio server, and API methods can change server data.

Mitigation: Use a trusted server URL and HTTPS for remote installations, protect the API token, and make changes only to resources within the user's scope when requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go module repository](https://github.com/psyb0t/go-label-studio)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples configure a caller-supplied Label Studio URL and token; API calls may read or change server resources.]

## Skill Version(s):

0.8.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
