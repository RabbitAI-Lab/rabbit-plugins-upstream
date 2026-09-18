## Description:

LIFX helps agents read and control LIFX lights and scenes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect LIFX action schemas, list lights and scenes, validate colors, and control light state through OOMOL-connected LIFX accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, reviewed method and do not let an agent run the remote installer automatically.

Risk: Some LIFX actions can change light state even though they are not tagged as writes in the artifact.

Mitigation: Require explicit user confirmation before any state-changing action, including toggle_power and turn_effects_off.

## Reference(s):

- [LIFX homepage](https://www.lifx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [LIFX ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lifx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON responses from LIFX connector actions.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
