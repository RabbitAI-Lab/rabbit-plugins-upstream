## Description:

Home Assistant (home-assistant.io). Use this skill for Home Assistant requests involving reading, creating, updating, and deleting data through the OOMOL-connected Home Assistant connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and operate a connected Home Assistant instance through the OOMOL `home_assistant` connector. It supports reading entity state and configuration, running service calls and scripts, firing events, and managing UI-editable automations, scenes, and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control Home Assistant devices and make state-changing or destructive configuration changes.

Mitigation: Require explicit approval for write and destructive actions, confirm the exact target and payload, and connect Home Assistant with the minimum scopes needed.

Risk: Fallback setup includes remote installer scripts that may be executed directly in a shell.

Mitigation: Prefer installing the oo CLI through a verified package or reviewed installer before using the skill.

## Reference(s):

- [Home Assistant homepage](https://www.home-assistant.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-home-assistant)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
