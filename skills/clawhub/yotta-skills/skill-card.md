## Description:

Helps agents plan combinations of YottaMeta skills, find installed skills, and manage installation, updates, and distribution across local agent directories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use it to choose a combination of YottaMeta skills, inspect local installations, and preview or perform skill installation and updates across agent directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk install or update can change multiple agent skill directories without an enforced confirmation step.

Mitigation: Run a dry-run preview and separately confirm the target directories and skill list before executing any bulk change.

Risk: Installation may run package lifecycle code or commands from an untrusted provider configuration.

Mitigation: Prefer the official install or update path or a version-pinned package, and avoid untrusted provider.json commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in skill metadata)](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](artifact/references/orchestration.md)
- [Hub guide](artifact/references/hub.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations can include skill combinations, install status, and previews; installation commands may modify local skill directories.]

## Skill Version(s):

0.30.2 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
