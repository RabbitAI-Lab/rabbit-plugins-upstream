## Description:

CJG Skill Forge is a meta-skill for creating, upgrading, reviewing, recasting, consolidating, and clarifying WorkBuddy or AI agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to build new agent skills, upgrade existing skills, review quality with a rubric, consolidate overlapping local skills, and make skill instructions clearer for agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad authority in skill-building workflows and can run target skill code.

Mitigation: Use it on trusted skills or in a sandbox, and review execution steps before running smoke tests or validation commands.

Risk: Local usage logging is on by default and cloud sync can persist or sync behavioral logs when explicitly enabled.

Mitigation: Keep cloud sync off unless anonymous feedback upload is desired, and use the documented controls to view, disable, or delete local signals.

Risk: Proposal approval and publishing workflows could introduce incorrect or misleading changes if accepted without review.

Mitigation: Review proposed changes, scan the skill before deployment, and require explicit approval before publishing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Skill Forge Pipeline](references/pipeline.md)
- [Forge Modes](references/forge-modes.md)
- [Skill Review Rubric](references/skill-review-rubric.md)
- [Skill Consolidation](references/skill-consolidation.md)
- [Clarity Coverage](references/clarity-coverage.md)
- [Security Audit](references/security-audit.md)
- [Cloud Config Schema](references/cloud-config-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and optional generated files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce review reports, forge plans, recast plans, clarity edits, validation commands, and release-preparation guidance.]

## Skill Version(s):

3.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
