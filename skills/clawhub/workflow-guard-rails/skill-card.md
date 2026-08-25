## Description:

Workflow Guardian helps agents wrap multi-step workflows with pre-execution checks, side-effect queues, validation, retry budgets, checkpointing, audit logs, and failure-rule accumulation to reduce false successes, duplicate external actions, unrecoverable crashes, and silent drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to add guardrails around recurring or multi-step agent workflows, especially when external writes, sends, publishes, deletes, retries, or long-running drift could create user-visible failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill adds validation, checkpointing, audit logging, and confirmation prompts that can increase workflow overhead.

Mitigation: Apply it to multi-step or side-effecting workflows where the added checks are justified, and budget the extra validation step before release.

Risk: Machine-checkable guards cannot fully detect style, semantic, or judgment errors.

Mitigation: Route subjective or policy-sensitive decisions to a separate human or review skill instead of relying only on automated assertions.

Risk: A side-effect queue only protects actions routed through it.

Mitigation: Require external actions such as send, publish, pay, delete, or external writes to pass through the queue before execution.

## Reference(s):

- [Guardian Patterns](references/guardian-patterns.md)
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/workflow-guard-rails)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, guard rules, validation patterns, and guardian reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concrete checkpoints, validation assertions, retry budgets, side-effect queue handling, audit-log entries, and human-confirmation prompts.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
