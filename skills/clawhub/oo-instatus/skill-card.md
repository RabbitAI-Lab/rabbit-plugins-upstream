## Description:

Instatus (instatus.com). Use this skill for ANY Instatus request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Instatus status pages through an OOMOL-connected account. It supports reading status data and creating, updating, or deleting components, incidents, and incident updates after checking the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a signed or checksum-verified installation path where available, and run the remote installer only after trusting the OOMOL installer endpoint.

Risk: Write and destructive actions can change or remove Instatus data.

Mitigation: Confirm the exact payload, target object, and intended effect before running write or destructive connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instatus)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Instatus homepage](https://instatus.com)
- [OOMOL Instatus connection setup](https://console.oomol.com/app-connections?provider=instatus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
