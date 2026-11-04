## Description:

An unofficial typed Go client for connecting applications to W&B Weave traces and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add the go-weave Go client to a project, authenticate with W&B, and record or query Weave traces and related project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace inputs and outputs are sent to the configured W&B trace server and may contain sensitive data.

Mitigation: Use a trusted HTTPS server and send only trace data you intend to share.

Risk: W&B credentials could be exposed, and delete or purge calls can remove project data.

Mitigation: Read credentials from environment variables, never commit or log them, and limit destructive calls to data the user named or the task created.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-weave source repository](https://github.com/psyb0t/go-weave)
- [go-weave package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
