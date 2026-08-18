## Description:

Evaluate hook security, performance, and SDK compliance for audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to evaluate Claude Code hooks for security, performance, SDK compliance, reliability, and maintainability before deployment or audit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad hook, security, or performance wording outside a specific hook-audit task.

Mitigation: Confirm the audit scope before applying its guidance and ignore it for unrelated security or performance work.

Risk: The artifact contains reference command examples, but the reviewed release is documentation-only and does not provide an executable scanner.

Mitigation: Treat command examples as workflow guidance and verify any available commands with their help output before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-hooks-eval)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tables, code examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only evaluation framework; it does not execute scans or install hooks by itself.]

## Skill Version(s):

1.9.18 (source: release evidence; artifact frontmatter states 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
