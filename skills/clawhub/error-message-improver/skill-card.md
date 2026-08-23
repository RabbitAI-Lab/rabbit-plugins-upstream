## Description:

Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what to do next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and users use this skill to rewrite or structure error messages so troubleshooting steps are clearer and more actionable. It can produce tailored answers, reusable checklists, workflows, analysis, code changes, or implementation support for error-message improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill allows implicit invocation with broad trigger wording, which could route unrelated troubleshooting or support requests into this workflow.

Mitigation: Narrow or disable implicit invocation so the skill runs only for explicit requests about improving, rewriting, or structuring user-facing error messages.

Risk: The skill is prompt-only and may propose clearer wording or implementation changes that still misstate the underlying failure or remediation path.

Mitigation: Review generated messages against the actual system behavior, available diagnostics, and user support requirements before release.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Publisher Profile](https://clawhub.ai/user/kyro-ma)
- [Tiered enforcement of missing values in apply_xmap() by .to in-degree](https://github.com/cynthiahqy/xmap/issues/48)
- [error-messages](https://segmentfault.com/t/error-messages)
- [I'm becoming AI-blind](https://news.ycombinator.com/item?id=49402160)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code blocks, checklists, workflows, analysis, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, limits, success criteria, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260823.40325 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
