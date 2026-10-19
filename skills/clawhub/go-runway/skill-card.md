## Description:

Guides Go developers in using an unofficial typed client to call Runway's generation and account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Runway API calls, start media-generation tasks, poll their status, and inspect account usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runway API credentials could be exposed in code or logs.

Mitigation: Read the API key from the environment and never commit, log, or display it.

Risk: Prompts and media sent through the client leave the local environment for Runway.

Mitigation: Review inputs before sending them to Runway and avoid sharing sensitive content without authorization.

Risk: Generation can consume organization credits; cancellation or deletion can change resources.

Mitigation: Confirm credit-spending and resource-changing actions with the user before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-runway)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)
- [Package homepage listed by the skill](https://github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live API calls require Go, a Runway API key, and network access.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
