## Description:

Guides developers in using the unofficial go-tinker Go client to call the Thinking Machines Tinker training and sampling API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working in Go use this skill to install and use a typed client for Tinker model training, sampling, and related API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial third-party Go dependency may not be the module a developer intends to trust.

Mitigation: Verify the module source before installing or adding it to a project.

Risk: A Tinker API key could be exposed through committed code or logs.

Mitigation: Read TINKER_API_KEY from the environment and never commit the key or print request headers.

Risk: Training calls can incur compute charges, and unloading can change remote model state.

Mitigation: Run these operations only when requested and only on models the task created or the user identified.

## Reference(s):

- [go-tinker on ClawHub](https://clawhub.ai/psyb0t/skills/go-tinker)
- [Setup and API reference](references/setup.md)
- [go-tinker Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-tinker)
- [go-tinker project homepage](https://github.com/psyb0t/go-tinker)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes installation steps, client setup, and guidance for handling API responses and futures.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
