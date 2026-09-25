## Description:

Plans and routes YottaMeta skill combinations, inventories installed skills, and provides commands to preview, install, and update them for supported agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can choose combinations of YottaMeta skills for a task, inspect what is installed, and preview or run installation and updates in a selected agent skills directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating downloads skill packages and can replace directories in the selected agent skills path.

Mitigation: Review the target directory and preview changes first; prefer pinned versions or OpenClaw/QClaw host-native install and update commands.

Risk: Bypassing the pre-install scan weakens the checks applied to downloaded skills.

Mitigation: Avoid --skip-scan except for an explicitly understood emergency path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands; optional CLI output in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing recommends combinations without automatically installing missing skills.]

## Skill Version(s):

0.19.20 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
