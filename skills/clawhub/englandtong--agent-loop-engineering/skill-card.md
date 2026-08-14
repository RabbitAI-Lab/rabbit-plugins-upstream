## Description:

Execute an authorized software goal through low-context, bounded-autonomous AI coding loops with persistent state, proactive repair, automatic and functional evidence, layered stage review, independent final acceptance, safe workspace boundaries, and resumable handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to carry an authorized coding goal through bounded Controller, Developer, and Stage Reviewer loops while keeping compact state, evidence, and handoff records. It is intended for clear targets with acceptance criteria, not for vague requirement discovery or final independent QA acceptance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to make project-local code changes and maintain repository execution records.

Mitigation: Use it only with a clear authorized goal, acceptance criteria, allowed changes, protected boundaries, and required evidence.

Risk: Credential, customer-data, deployment, destructive Git, or system-level work could exceed the intended release posture.

Mitigation: Stop before those actions unless there is separate explicit approval, scoped authority, rollback planning, and appropriate evidence.

Risk: An executing agent may overstate completion if final acceptance is not independent.

Mitigation: Require task-local evidence and a separate agent, task, or human reviewer for Standard and Full final acceptance.

## Reference(s):

- [Agent Loop Engineering skill page](https://clawhub.ai/englandtong/skills/agent-loop-engineering)
- [Execution Loop 2.1](artifact/references/en/execution-loop.md)
- [Evidence And Completion 2.1](artifact/references/en/evidence-and-completion.md)
- [Safety And Context 2.1](artifact/references/en/safety-and-context.md)
- [Automation And Handoff 2.1](artifact/references/en/automation-and-handoff.md)
- [Legacy State Migration 2.1](artifact/references/en/migration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown status reports, code edits, shell commands, JSONL loop records, and YAML or Markdown state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains compact execution state and evidence links; final Standard or Full acceptance remains outside the executing agent.]

## Skill Version(s):

2.1.0 (source: artifact/SKILL.md and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
