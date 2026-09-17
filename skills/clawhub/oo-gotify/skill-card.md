## Description:

Gotify (gotify.net). Use this skill for Gotify requests such as reading instance information and sending messages through an OOMOL-connected Gotify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Gotify instance through the OOMOL oo CLI, including checking health and version information and sending messages after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Prefer the official install guide or a signed/package-manager installation path, review installer scripts before running them, and avoid elevated terminals unless independently reviewed.

Risk: The send_message action changes Gotify state by creating a message.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [Gotify homepage](https://gotify.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gotify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
