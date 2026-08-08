## Description:

Creates automation command skills for Claude Code projects - imperative slash-command prompts in `.claude/skills/`, not knowledge or reference skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to create explicit slash-command skills for multi-step automation workflows such as deploys, commits, releases, migrations, and cross-repo operations. It emphasizes phased execution, approval gates, error handling, and audit checks for command skills that may cause side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated command skills may later commit, deploy, modify repositories, or invoke external tooling when a user asks for those commands.

Mitigation: Review generated command skills before use and require explicit approval checkpoints before file writes, commits, pushes, deploys, or other side effects.

Risk: Generated skill guidance could be incorrect or misleading for a target repository's conventions.

Mitigation: Audit the generated SKILL.md against the target project, run relevant tests or scans, and confirm cross-repo discovery and error-handling steps before deployment.

## Reference(s):

- [Command Skill Design Patterns](references/design-patterns.md)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/command-skill-creator)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/command-skill-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML frontmatter and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing command skill drafts and audit guidance; review generated skills before use.]

## Skill Version(s):

0.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
