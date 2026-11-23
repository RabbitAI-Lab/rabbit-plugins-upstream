## Description:

Provides Go developers with a typed client and guidance for sending and querying traces and related resources on the W&B Weave trace server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to the W&B Weave trace server, record and query traces, and work with related Weave resources from a Go project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs may contain sensitive information and are sent to the configured trace server.

Mitigation: Review trace data and the configured server URL before sending requests; use a dedicated or self-hosted server when appropriate.

Risk: W&B credentials could be exposed if API keys are hardcoded, committed, or logged.

Mitigation: Load credentials from WANDB_USERNAME and WANDB_API_KEY environment variables, and never commit or log them or request headers.

Risk: Delete and purge endpoints can remove project data.

Mitigation: Call these endpoints only for data created by the task or named by the user, and only when deletion was requested.

## Reference(s):

- [Setup and endpoint reference](artifact/references/setup.md)
- [GitHub project](https://github.com/psyb0t/go-weave)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance for a Go project.]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
