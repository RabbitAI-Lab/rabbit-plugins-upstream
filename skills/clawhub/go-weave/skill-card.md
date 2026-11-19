## Description:

An unofficial typed Go client for the W&B Weave trace server API, for sending and querying traces and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this client to record and query Weave traces and work with related resources from Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs may contain sensitive information and are sent to the configured trace server.

Mitigation: Use an approved trace server and avoid sending secrets or sensitive data unless the project is authorized to store them there.

Risk: The API includes delete and purge operations that remove project data.

Mitigation: Use delete and purge operations only on data created for the task or specifically named by the user, and only when requested.

Risk: W&B credentials could be exposed if embedded in code, committed, or logged.

Mitigation: Load credentials from WANDB_USERNAME and WANDB_API_KEY environment variables; do not hardcode, commit, or log them.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
