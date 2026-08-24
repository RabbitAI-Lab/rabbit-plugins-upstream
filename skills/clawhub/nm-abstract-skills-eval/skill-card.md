## Description:

Evaluate Claude skill quality through auditing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to audit Claude skills for structure, content quality, token efficiency, activation reliability, tool integration, and improvement priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broad activation triggers.

Mitigation: Review and narrow triggers before installing in environments where unrelated requests could activate the skill.

Risk: The security evidence notes examples that can run or modify local files without enough safety limits.

Mitigation: Use trusted skill repositories, sandbox or allowlist benchmarked executables, and inspect auto-fix changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skills-eval)
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory skill-audit guidance and command examples; users should review proposed changes before applying them.]

## Skill Version(s):

1.9.18 (source: ClawHub release evidence; artifact SKILL.md frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
