## Description:

Helps agents select YottaMeta skill combinations, inventory installed skills, and manage installation and distribution across local agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose related YottaMeta skills for a task, inspect local installations, and preview or manage installations, updates, and links across agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation, updates, links, and removal can change skills across multiple local agents.

Mitigation: Review target agents and directories, run --dry-run before Hub link, remove, or update operations, and confirm intended changes.

Risk: Global installation may copy the skill into more agents than intended.

Mitigation: Prefer host-native OpenClaw installation or an exact-version npm command; avoid install.sh -g unless broad installation is intended.

Risk: Downloaded packages and optional providers may run local processes with the user's privileges.

Mitigation: Review packages with lifecycle behavior and any provider.json before enabling them; use exact versions when installing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Publisher-listed project homepage](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](references/orchestration.md)
- [Local skill Hub guide](references/hub.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown guidance and commands; CLI text or JSON for inventory and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation and Hub operations can also modify local skill directories after user confirmation.]

## Skill Version(s):

0.29.9 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
