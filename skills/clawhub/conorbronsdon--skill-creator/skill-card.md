## Description:

Generate a new Claude Code skill from a plain-language description; decide invocation control, arguments, context cost, scaffolding, and testing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn plain-language requests into Claude Code skill drafts with appropriate invocation controls, argument handling, context-budget guidance, installation steps, and review prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills can include tool grants, hooks, dynamic command injection, or actions that affect external systems.

Mitigation: Review generated skill files before saving or installing them, with special attention to tool grants, hooks, command execution, and external side effects.

Risk: Generated authoring guidance can be incorrect or too broad for a specific workspace.

Mitigation: Compare the generated skill against local conventions, existing skills, and the pinned frontmatter reference before release.

## Reference(s):

- [Skill Frontmatter & Behavior Reference](reference.md)
- [Claude Code Skills documentation](https://code.claude.com/docs/en/skills)
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/skill-creator)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with fenced code blocks and review prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local skill scaffolding guidance; generated skills should be reviewed before saving or installing.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
