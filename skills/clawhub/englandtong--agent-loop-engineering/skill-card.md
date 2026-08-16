## Description:

Execute an authorized software goal through low-context, bounded-autonomous AI coding loops with persistent state, proactive repair, automatic and functional evidence, layered stage review, independent final acceptance, safe workspace boundaries, and resumable handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to carry clear software goals through bounded Controller, Developer, and Stage Reviewer loops. It is for implementation, debugging, verification, repair, resumable handoff, and compact evidence tracking when scope and acceptance criteria are known.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive autonomous code changes beyond the user's intended scope if the goal, boundaries, or acceptance criteria are unclear.

Mitigation: Use it only after a clear goal, Non-Goals, write scope, and observable acceptance criteria are recorded; stop at authority changes or protected-boundary decisions.

Risk: A coding loop may overstate completion if it relies only on plans, build success, or partial checks.

Mitigation: Require automatic evidence, functional evidence for runtime claims, and independent final acceptance for Standard or Full governed work.

Risk: Long-running or parallel agent work can increase cost and coordination risk.

Mitigation: Use bounded stages, compact context, one coordinating writer, no more than three active workers by default, and stop after repeated no-progress failure signatures.

Risk: The workflow is not appropriate for secrets, production data, paid resources, destructive Git operations, deployments, or writes outside the project.

Mitigation: Treat those cases as hard stops unless the user gives separate explicit authority and a concrete scope, impact, rollback, and evidence plan.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/agent-loop-engineering)
- [Evidence And Completion](artifact/references/en/evidence-and-completion.md)
- [Execution Loop](artifact/references/en/execution-loop.md)
- [Safety And Context](artifact/references/en/safety-and-context.md)
- [Isolated Delegation](artifact/references/en/isolated-delegation.md)
- [Automation And Handoff](artifact/references/en/automation-and-handoff.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured state fields, YAML/JSON examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project-local state updates, evidence summaries, command results, and next-action handoff details when authorized.]

## Skill Version(s):

2.1.1 (source: artifact/SKILL.md and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
