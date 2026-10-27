## Description:

Writes Go code with go-bfl (package bfl, github.com/psyb0t/go-bfl), an unofficial generated client for the Black Forest Labs FLUX API. Use when a Go program submits FLUX image or video generation tasks, polls task results, calls the image and video tools, reads credits or manages fine-tunes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go applications with the unofficial go-bfl client for submitting and polling Black Forest Labs FLUX tasks, using FLUX tools, checking credits, and managing fine-tunes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed or sent to an untrusted host.

Mitigation: Load BFL_API_KEY from the environment, never log it, and only send it to the API or a validated HTTPS polling host.

Risk: Generation requests spend credits, and deleting a fine-tune changes account state.

Mitigation: Make paid submissions and account changes only when requested, and do not blindly retry a submission with an uncertain result.

Risk: The bundled guidance does not assess the full external Go dependency.

Mitigation: Review and pin the third-party dependency before relying on it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-bfl)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-bfl)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-bfl)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
