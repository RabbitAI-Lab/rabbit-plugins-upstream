## Description:

Wires a python-cqrs domain event, notification, transactional outbox, and transactional inbox, and runs independent domain handlers concurrently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vadikko2](https://clawhub.ai/user/vadikko2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Python applications with python-cqrs use this skill to wire in-process domain events, notifications, transactional outbox and inbox delivery, or independent parallel handlers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Best-effort notifications can be dropped, including when the default broker is used.

Mitigation: Configure a real broker for best-effort messages; use the transactional outbox when delivery must survive with the business transaction.

Risk: Inbox delivery or a crash before status commit can cause a handler to run again.

Mitigation: Keep effects idempotent and acknowledge only after the inbox write commits.

Risk: Repeatedly failing delivery rows can leave the selectable batch after five failures.

Mitigation: Inspect rows that have reached the documented failure limit and follow the application's retry and recovery process.

## Reference(s):

- [Delivery notes](references/delivery.md)
- [ClawHub release page](https://clawhub.ai/vadikko2/skills/cqrs-eda)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Python code snippets and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
