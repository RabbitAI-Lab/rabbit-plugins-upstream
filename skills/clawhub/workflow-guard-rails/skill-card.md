## Description:

A horizontal safety layer for multi-step agent workflows that adds pre-execution checks, checkpointing, side-effect queues, retry budgets, result validation, audit logs, and rule accumulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to wrap recurring or unattended agent workflows that send, publish, delete, write, pay, or otherwise create external side effects. It helps them define pre-checks, validation gates, retry budgets, checkpoints, audit logs, and human review points before releasing workflow results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be loaded for broad workflow-safety terms even when checkpointing, validation, retries, or external side-effect control are not relevant.

Mitigation: Use it for workflows where those controls are needed, and avoid applying it to unrelated single-shot prompts or pure data transforms.

Risk: Audit logging can capture workflow evidence and human confirmations that may include sensitive operational details.

Mitigation: Limit audit logs to necessary evidence, follow local access and retention controls, and avoid recording secrets or unrelated personal data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/workflow-guard-rails)
- [Guardian Patterns](references/guardian-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with checklist-style guardian reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no executable tool calls or generated files are declared by the artifact.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
