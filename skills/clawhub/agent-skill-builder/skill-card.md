## Description:

Build, review, or migrate an agent skill from a plain-language description -- decides invocation control (disable-model-invocation vs user-invocable), arguments (argument-hint, $ARGUMENTS), and context cost, then scaffolds, validates, and tests it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to design, scaffold, review, and migrate agent skills with explicit invocation control, argument handling, context budgeting, tool-grant guidance, validation, and testing steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or migrated skills may include broad tool grants or commands that publish, delete, push, or call external APIs.

Mitigation: Review generated SKILL.md files before installation, keep allowed-tools grants tightly scoped, require confirmation gates for external side effects, and run the bundled validator.

Risk: The skill can guide an agent to read local project guidance and existing skills while creating or migrating files.

Mitigation: Limit the source material supplied to the agent, review generated content for accidental disclosure, and avoid including credentials or private project details in skill output.

Risk: The bundled Claude Code frontmatter reference is a pinned snapshot and can become stale.

Mitigation: Follow the skill's staleness warning, use the bundled freshness checker for maintenance, and update the snapshot through reviewed changes rather than during generation.

## Reference(s):

- [Skill Frontmatter and Behavior Reference](references/claude-code-frontmatter.md)
- [Agent Skills standard](https://agentskills.io)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [Anthropic skill-creator plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with SKILL.md drafts, validation output, shell commands, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce new or migrated skill files and validator PASS/FAIL findings when used in creation, review, or migration workflows.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
