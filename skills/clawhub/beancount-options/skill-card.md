## Description:

Guides an agent in recording options trades and lifecycle events as reviewed, validated transactions in a Beancount ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing Beancount investment ledgers can turn described options trades and lifecycle events into proposed ledger transactions and account openings, then review and confirm them before adding them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed transaction or account opening may be inaccurate, target an unintended ledger or service, or remain unvalidated.

Mitigation: Use a backed-up ledger, explicitly select or approve the ledger and service, review each proposed transaction and account opening, and require successful validation before committing entries.

## Reference(s):

- [ClawHub release](https://clawhub.ai/puncsky/skills/beancount-options)
- [Project homepage and documentation index](https://github.com/bex-co/beancount-io/tree/main/skills)
- [Bea CLI workflow](artifact/references/bea-cli.md)
- [Compatibility guidance](artifact/references/compatibility.md)
- [Single-leg options entries](artifact/references/single-leg.md)
- [Assignment entries](artifact/references/assignment.md)
- [Exercise entries](artifact/references/exercise.md)
- [Rolling options positions](artifact/references/rolling.md)

## Skill Output:

**Output Type(s):** [Beancount transactions, Account-opening directives, Guidance]

**Output Format:** [Beancount ledger syntax with concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed entries require user review and explicit confirmation; use a backed-up ledger and validate before committing.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
