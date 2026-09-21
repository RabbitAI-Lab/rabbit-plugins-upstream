## Description:

Help any repository-capable AI agent spend less time rediscovering files and loading unnecessary context by creating concise project maps for code, content, and operations, linked from existing agent instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asif2bd](https://clawhub.ai/user/asif2bd)

### License/Terms of Use:

MIT

## Use Case:

Developers and repository maintainers use this skill to create or refresh concise Markdown navigation maps so coding agents can find relevant source, documentation, and workflow files without repeatedly rediscovering the project structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instruction-file edits may affect future agent sessions.

Mitigation: Review changes to navigation Markdown, AGENTS.md, and CLAUDE.md before relying on the generated maps.

Risk: Project maps could expose secrets, private content, machine-specific paths, or copied file contents if generated too broadly.

Mitigation: Keep maps concise, use relative links, inspect only selected project files, and exclude secrets or private content from generated navigation documents.

Risk: Remote adoption instructions may differ from the packaged release.

Mitigation: Prefer the packaged instructions, or verify the remote source before asking an agent to fetch and apply it.

## Reference(s):

- [AI Coding Token Optimizer on ProSkills.md](https://proskills.md/skills/coding/ai-coding-token-optimizer)
- [AI Coding Token Optimizer on ClawHub](https://clawhub.ai/asif2bd/skills/ai-coding-token-optimizer)
- [Adoption by Host](references/adoption.md)
- [Mapping Patterns](references/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Guidance]

**Output Format:** [Markdown files and concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; produces project maps and agent entry-point updates without modifying application code.]

## Skill Version(s):

1.0.2 (source: frontmatter and changelog, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
