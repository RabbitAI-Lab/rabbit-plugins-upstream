## Description:

Use this skill to operate Home Assistant through OOMOL-connected actions for reading, creating, updating, and deleting Home Assistant data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Home Assistant state and perform Home Assistant operations through an OOMOL-connected account. It supports device control, service calls, events, scripts, templates, logs, registries, calendars, and UI-managed automations, scenes, and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands can fetch and execute remote scripts.

Mitigation: Do not let an agent run installer commands automatically; use a verified package or inspect and verify the installer first.

Risk: The skill can control Home Assistant devices and edit or delete automations, scenes, and scripts.

Mitigation: Use it only when you trust OOMOL and require explicit confirmation for service calls, script execution, event firing, writes, and deletes.

Risk: Some state-changing Home Assistant actions may not be fully tagged as writes in the skill text.

Mitigation: Treat any action that changes device state, fires events, executes scripts, or modifies configuration as confirmation-required even if it is not tagged.

## Reference(s):

- [Home Assistant](https://www.home-assistant.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-home-assistant)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Home Assistant action payloads, schema inspection commands, and confirmation requests for writes or destructive changes.]

## Skill Version(s):

1.0.5 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
