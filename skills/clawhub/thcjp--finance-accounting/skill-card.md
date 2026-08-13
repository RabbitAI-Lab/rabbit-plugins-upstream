## Description:

Provides finance and accounting document support, including bookkeeping, reconciliation, tax calculations, and generation of balance sheets, income statements, and cash-flow statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft and automate finance and accounting workflows such as bookkeeping records, bank reconciliation, tax calculations, and financial report generation. Outputs should be reviewed by a qualified human before use in accounting, tax, invoice, or reconciliation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read, write, and command execution permissions can expose or alter sensitive finance files.

Mitigation: Limit the agent to explicit files and workflows, avoid broad directory access, and review commands before execution.

Risk: Accounting, tax, invoice, or reconciliation outputs may be incorrect or incomplete.

Mitigation: Manually verify outputs with appropriate financial, accounting, or tax review before relying on them.

Risk: Real API keys or external service credentials could be exposed if provided without review.

Mitigation: Avoid providing real API keys unless the exact commands and services have been reviewed, and prefer scoped credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finance-accounting)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce finance reports, reconciliation summaries, tax forms, generated document guidance, and command examples; outputs require human review before operational use.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
