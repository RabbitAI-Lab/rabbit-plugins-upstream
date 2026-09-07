## Description:

This skill helps QA teams identify testing and automation technical debt, assess maintenance and rewrite costs, and create phased repayment plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and test automation teams use this skill when test assets are unstable, expensive to maintain, or accumulating automation debt. It helps inventory debt, analyze impact, plan repayment, and define prevention strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic refactoring or maintenance-cost prompts may activate the skill outside a QA technical-debt task.

Mitigation: Confirm the request is actually about testing or automation debt before inspecting files or running shell commands.

Risk: Debt analysis could be misused as the sole basis for release blocking or production-impact decisions.

Mitigation: Review conclusions with development and product owners before changing release or operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-tech-debt-management)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with structured analysis tables and action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include debt inventories, impact analysis, repayment plans, prevention strategies, and QA test-case tables.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
