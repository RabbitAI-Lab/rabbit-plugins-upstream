## Description:

Helps agents plan and route YottaMeta skill combinations, inventory installed skills, and prepare user-approved installs and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can choose appropriate YottaMeta skills for a task, review installation plans, and inventory, install, update, or roll back skills in a selected agent or directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install and update commands can change multiple local skill directories and create state under ~/.yottaskills.

Mitigation: Review the list or dry-run first, confirm the exact --agent or --dir target, and retain local logs and rollback snapshots.

Risk: Install and update checks may access npm, and unpinned packages may change between runs.

Mitigation: Use reviewed, version-pinned package invocations for repeatable installs and allow npm network access only when needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Installation flow](references/install-flow.md)
- [Skill orchestration](references/orchestration.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance and command examples; optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes suggest skills without automatically installing them; installation and updates require explicit invocation.]

## Skill Version(s):

0.20.1 (source: release evidence, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
