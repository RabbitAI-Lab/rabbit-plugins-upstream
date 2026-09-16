## Description:

Operates Sensibo devices through an OOMOL-connected account by listing devices, reading AC state, and setting AC state when explicitly confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support agents use this skill to manage Sensibo-connected air-conditioning devices through OOMOL without handling raw Sensibo tokens. It supports reading device details and current or previous AC states, then changing full AC state payloads after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI, which may be risky if the installer source is not verified.

Mitigation: Review the skill before installing, prefer a trusted and pinned oo CLI release or official package manager, and inspect or verify any installer before running it.

Risk: The set_ac_state action changes Sensibo device state.

Mitigation: Confirm the exact payload and expected AC state change with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sensibo)
- [Sensibo Homepage](https://home.sensibo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require confirming the exact AC state payload and effect.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
