## Description:

Creates Claude Code skill files with structured frontmatter, trigger-focused guidance, examples, anti-patterns, and optional library README updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to package recurring Claude Code workflows into reusable skills with clear triggers, structured instructions, examples, and review checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to create or edit skill files, including global skills that affect future sessions.

Mitigation: Review generated paths and generated skill content before accepting changes, especially for global skill locations.

Risk: The skill may suggest installing from an unpinned GitHub npx command.

Mitigation: Prefer a pinned or verified installer command before running installation steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/write-a-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown skill content with inline commands and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write SKILL.md files, update a library README, and provide install commands when appropriate.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
