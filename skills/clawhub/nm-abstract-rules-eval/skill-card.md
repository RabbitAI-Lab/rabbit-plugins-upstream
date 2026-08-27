## Description:

Evaluates Claude Code rules in `.claude/rules/` for frontmatter validity, glob patterns, content quality, and organization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit Claude Code rule files for valid frontmatter, appropriate glob patterns, concise guidance, organization quality, and token efficiency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms such as rules and validation may activate the skill in unintended contexts.

Mitigation: Review activation behavior before installing, especially in environments with similarly named skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-rules-eval)
- [Homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Frontmatter Validation](modules/frontmatter-validation.md)
- [Glob Pattern Analysis](modules/glob-pattern-analysis.md)
- [Content Quality Metrics](modules/content-quality-metrics.md)
- [Organization Patterns](modules/organization-patterns.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown analysis with scoring and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code is included; output is guidance for improving rule files.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
