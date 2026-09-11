## Description:

元阁 yotta-skills helps agents route tasks to YottaMeta skill combinations, inventory installed skills, and install or update the YottaMeta skill family from npm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to list, route, install, update, and inventory YottaMeta skills across supported agent environments. It is intended for managing skill combinations and local skill directories, not for creating new skill content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update skills from npm, including automated family updates.

Mitigation: Use pinned versions and a trusted registry, review the install plan first, and avoid update --auto until supply-chain controls are stronger.

Risk: The skill asks to persist orchestration rules into permanent agent memory files.

Mitigation: Do not allow writes to AGENTS.md, CLAUDE.md, or equivalent persistent memory without explicit human review.

Risk: The pre-install scan is informational and may not block unsafe packages.

Mitigation: Treat scan output as advisory and perform manual review before installing or updating skills.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [README](README.md)
- [Orchestration planner](references/orchestration.md)
- [Skill family list](references/skill-list.md)
- [Install flow](references/install-flow.md)
- [FAQ](references/faq.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown, terminal text, JSON, and shell command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install or update skill files in a target directory and may update a local skill registry during install, update, inventory, or re-index workflows.]

## Skill Version(s):

0.7.2 (source: frontmatter, package.json, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
