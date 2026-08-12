## Description:

Home Assistant (home-assistant.io). Use this skill for Home Assistant reading, creating, updating, and deleting tasks through the OOMOL-connected connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Home Assistant state, history, registries, services, calendars, events, templates, and configuration, then perform controlled writes for services, scripts, automations, and scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control Home Assistant and may create, replace, or delete automations, scenes, and scripts.

Mitigation: Use a Home Assistant account whose permissions match the actions the agent should be allowed to perform, and require user confirmation before write or destructive actions.

Risk: Configuration changes could break or misconfigure automations, scenes, or scripts.

Mitigation: Inspect live action schemas before payload construction and use Home Assistant validation or configuration checks before storing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-home-assistant)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Home Assistant](https://www.home-assistant.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Home Assistant connector responses as JSON and may propose configuration changes for user approval.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
