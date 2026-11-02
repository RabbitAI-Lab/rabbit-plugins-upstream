## Description:

An unofficial typed Go client for the W&B Weave trace server, with guidance for recording, reading, and querying traces and related Weave resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and configure the go-weave client, then record, inspect, and query W&B Weave traces and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs may contain sensitive data sent to the configured trace server.

Mitigation: Verify the destination server and ensure trace contents are appropriate to share.

Risk: Delete and purge methods remove project data.

Mitigation: Use them only on data created by the task or named by the user, and only when requested.

Risk: The client is an unofficial dependency whose changes may affect an integration.

Mitigation: Review and pin the dependency before use.

Risk: Exposed W&B credentials could allow unauthorized access.

Mitigation: Read credentials from environment variables and never hardcode, commit, or log them.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)
- [Project homepage](https://github.com/psyb0t/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go client usage, environment-based authentication, and endpoint guidance.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
