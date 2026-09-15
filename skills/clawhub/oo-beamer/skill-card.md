## Description:

Use Beamer through an OOMOL-connected account to read post data, retrieve feed URLs, and create changelog posts with confirmed payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Beamer account actions through the OOMOL oo CLI, including listing posts, counting unread posts, generating feed URLs, and creating changelog posts after confirming the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute shell or PowerShell content directly.

Mitigation: Review the oo CLI installation path, prefer official package-manager or verified download instructions, and avoid piping remote scripts directly into a shell.

Risk: The create_post action changes Beamer state.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-beamer)
- [Beamer homepage](https://www.getbeamer.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo connector schema checks, oo connector run commands, and Beamer action payloads.]

## Skill Version(s):

1.0.3 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
