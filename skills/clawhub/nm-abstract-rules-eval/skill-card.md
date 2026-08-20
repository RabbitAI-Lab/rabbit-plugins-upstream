## Description:

Evaluate Claude Code rules in .claude/rules/ for frontmatter, glob pattern, content quality, and organization audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit Claude Code rule files for valid YAML frontmatter, appropriate path globs, concise actionable guidance, naming conventions, and directory organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect .claude/rules/ content and validate symlink targets while auditing rule organization.

Mitigation: Run it only in repositories whose rule files can be reviewed, and verify symlink targets before acting on recommendations.

Risk: The related external plugin may contain agents, hooks, or commands that are outside the inspected skill artifact.

Mitigation: Review and scan the external plugin separately before installing those additional components.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-rules-eval)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Frontmatter Validation](artifact/modules/frontmatter-validation.md)
- [Glob Pattern Analysis](artifact/modules/glob-pattern-analysis.md)
- [Content Quality Metrics](artifact/modules/content-quality-metrics.md)
- [Organization Patterns](artifact/modules/organization-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands]

**Output Format:** [Markdown with inline shell command examples and scoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quality scores, validation findings, and recommendations for Claude Code rule files.]

## Skill Version(s):

1.9.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
