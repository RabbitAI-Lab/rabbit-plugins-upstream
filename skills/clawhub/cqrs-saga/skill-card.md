## Description:

Orchestrates a python-cqrs saga whose finished steps compensate on failure, with persistent state and recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vadikko2](https://clawhub.ai/user/vadikko2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build multi-step workflows across services or databases, with compensation for completed steps and persistent recovery after failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crash can leave a completed side effect and its stored checkpoint out of sync, so recovery may skip work that did not commit.

Mitigation: Keep the step effect and checkpoint in the same transaction, or reconcile the effect before recovery continues.

Risk: A repeated or parallel saga for the same business item can duplicate its workflow history and side effects.

Mitigation: Use one stable saga ID per business ID and check that another worker is not already running the saga before recovery.

Risk: A remote action may succeed before a timeout prevents its result from being checkpointed, leaving compensation without the resource ID.

Mitigation: Use an idempotency key and look up or reconcile uncertain remote results before treating the action as undone.

## Reference(s):

- [Saga recovery](references/recovery.md)
- [ClawHub skill page](https://clawhub.ai/vadikko2/skills/cqrs-saga)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Python code, Configuration instructions]

**Output Format:** [Markdown guidance with Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
