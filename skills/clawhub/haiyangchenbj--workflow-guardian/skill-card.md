## Description:

Wrap multi-step agent workflows with pre-execution checks, side-effect queues, result validation, retry budgets, checkpointing, audit logs, and failure-rule accumulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add conservative workflow guardrails around repeated or multi-step agent automation, especially when failures could create broken outputs, duplicate side effects, or unrecoverable state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External writes, sends, deletes, payments, or other irreversible actions can execute before workflow output is validated.

Mitigation: Pause for human confirmation where required and route external actions through a side-effect queue that releases only after validation passes.

Risk: Workflow runs can report success even when generated output is incomplete, malformed, or otherwise invalid.

Mitigation: Use independent assertions, schema or invariant checks, retry budgets, and human escalation when validation continues to fail.

Risk: Machine-checkable guards may not catch style, semantic, or judgment drift.

Mitigation: Pair the guardian with an appropriate review layer for subjective or domain-judgment decisions.

## Reference(s):

- [Guardian Patterns](artifact/references/guardian-patterns.md)
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/workflow-guardian)

## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown guidance and structured guardian reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pre-check status, checkpoint counts, side-effect queue status, validation results, retry usage, audit-log status, proposed guard rules, and a release or hold verdict.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
