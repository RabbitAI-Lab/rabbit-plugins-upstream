## Description:

Helps Go developers use the unofficial go-weave client to record and query W&B Weave traces and related project data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the go-weave client, authenticate with W&B, and write code that records or queries traces and related Weave resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: W&B API credentials could be exposed in source code or logs.

Mitigation: Read WANDB_API_KEY from the environment; do not commit or log credentials or request headers.

Risk: Trace inputs or outputs could contain data not intended for the configured server.

Mitigation: Review trace content before sending it to W&B or a self-hosted trace server.

Risk: Delete or purge operations could remove project data.

Mitigation: Use delete and purge endpoints only when removal is explicitly intended.

## Reference(s):

- [go-weave setup and reference](references/setup.md)
- [go-weave package documentation](https://pkg.go.dev/github.com/psyb0t/go-weave)
- [go-weave project homepage](https://github.com/psyb0t/go-weave)
- [go-weave ClawHub release](https://clawhub.ai/psyb0t/skills/go-weave)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use Go, W&B credentials, and a configured trace server.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
