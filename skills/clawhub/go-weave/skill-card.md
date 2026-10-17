## Description:

Guides Go developers in using an unofficial typed client to record and query W&B Weave traces and related project data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add W&B Weave tracing to applications and read or manage trace-server data through the go-weave client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go dependency may not have the same support or review as an official W&B client.

Mitigation: Review the dependency before installing it and pin an approved version.

Risk: W&B API credentials or trace contents could be exposed through source code, logs, or unintended trace-server destinations.

Mitigation: Keep WANDB_API_KEY out of source control and logs, and check the trace server URL before sending data.

Risk: Delete and purge methods can remove project data.

Mitigation: Use them only for data the user explicitly identified and asked to remove.

## Reference(s):

- [go-weave setup and reference](references/setup.md)
- [go-weave project](https://github.com/psyb0t/go-weave)
- [ClawHub go-weave release](https://clawhub.ai/psyb0t/skills/go-weave)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a configurable trace server URL and W&B credentials supplied through environment variables.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
