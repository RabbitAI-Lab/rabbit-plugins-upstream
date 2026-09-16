## Description:

Operates LIFX lights and scenes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and automation agents use this skill to inspect LIFX connector schemas, list lights and scenes, validate colors, and control light power, scenes, effects, brightness, color, infrared, and transitions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code during first-time setup.

Mitigation: Review and independently verify the installer before running it; do not run the remote installer pipeline unless the source is trusted.

Risk: Some light-changing actions are under-labeled as safe reads.

Mitigation: Treat toggle_power and turn_effects_off as write actions and confirm the selector and intended effect with the user before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lifx)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [LIFX homepage](https://www.lifx.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live LIFX action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
