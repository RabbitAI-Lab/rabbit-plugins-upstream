## Description:

Provides a typed Go client for recording and querying traces through the W&B Weave trace server API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining Go applications use the skill to install and integrate a typed client for recording, reading, and querying W&B Weave traces and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs may contain sensitive information and are sent to the configured trace server.

Mitigation: Use an approved hosted, dedicated, or self-hosted endpoint, and exclude or redact credentials and sensitive content before sending traces.

Risk: The client includes delete and purge operations that remove project data.

Mitigation: Use these operations only on data created by the task or specifically named by the user, and only when requested.

Risk: HTTP Basic authentication uses a W&B username and API key.

Mitigation: Read credentials from WANDB_USERNAME and WANDB_API_KEY; do not hardcode, commit, or log them.

## Reference(s):

- [Setup and endpoint reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-weave)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover client setup, authentication, API calls, streaming responses, and error handling.]

## Skill Version(s):

0.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
