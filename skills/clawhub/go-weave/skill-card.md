## Description:

Guides Go projects in using the go-weave client to send and retrieve traces and related data through the W&B Weave trace server API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and configure the go-weave client, authenticate to a chosen Weave trace server, and work with traces and related Weave APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs may contain sensitive information, and credentials could be exposed if mishandled.

Mitigation: Use a trusted HTTPS trace server, minimize sensitive trace data, and keep credentials out of source code and logs.

Risk: Delete and purge operations can remove project data.

Mitigation: Use these operations only on data created by the task or named by the user, and only when requested.

Risk: The downloaded Go dependency was not independently verified.

Mitigation: Review the dependency source and version before relying on it.

## Reference(s):

- [Project homepage](https://github.com/psyb0t/go-weave)
- [Package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Go code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
