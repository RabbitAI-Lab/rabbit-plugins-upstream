## Description:

Guides software development and skill-building work through requirement clarification, design confirmation, critical self-checks, task decomposition, dual-stage review, and evidence-backed validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to structure coding, refactoring, bug fixing, and skill-development tasks before execution. It helps agents ask for clarification, propose designs with self-checks, coordinate subagent reviews, and finish with command-backed validation evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may propose edits to project instruction files or workflow gates that affect future agent behavior.

Mitigation: Review proposed edits before accepting them, especially changes to persistent project instructions, validation gates, or release workflows.

Risk: The skill enforces an opinionated process with clarification, design confirmation, review, validation commands, and commits.

Mitigation: Install and use it only when that development workflow matches the team or project expectations.

## Reference(s):

- [Superpowers](https://github.com/obra/superpowers)
- [Architecture Patterns](artifact/references/architecture-patterns.md)
- [Anti-rationalization Table](artifact/references/anti-rationalization.md)
- [Subagent Review Templates](artifact/references/subagent-review-templates.md)
- [ClawHub Skill Page](https://clawhub.ai/muippt/skills/redskill-upload-mu-dev-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with checklists, tables, task descriptions, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged plans, review instructions, validation checklists, and commit or verification guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter declares 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
