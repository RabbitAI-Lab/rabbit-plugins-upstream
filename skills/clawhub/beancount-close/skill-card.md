## Description:

Close an accounting period in a local Beancount ledger by reconciling each active account through beancount-reconcile, checking assertions and recurring gaps, reviewing flags, then proposing a commit with the period reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and bookkeeping practitioners use this skill to close a Beancount accounting period by reconciling active accounts, checking assertions and recurring gaps, and reporting unresolved items before proposing a documented commit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A recurring-charge pattern may suggest a missing transaction that did not occur.

Mitigation: Confirm the charge against a statement or other source evidence, review any separately proposed entry, and approve that entry independently from the close commit.

Risk: Approved ledger changes and financial details remain in Git history.

Mitigation: Review the selected ledger, every proposed change, and the exact commit contents; commit only when they are accurate and appropriate to retain in that repository.

## Reference(s):

- [ClawHub release](https://clawhub.ai/puncsky/skills/beancount-close)
- [Close checklist](references/close-checklist.md)
- [bea CLI recipes](references/bea-cli.md)
- [Installation guide](https://github.com/bex-co/beancount-io/blob/main/docs/skills/installation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Period-specific close report with reconciliation status, checks, recurring gaps, flags, and a proposed commit message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports incomplete or unverified work; a commit requires an explicit approval and passing ledger check; does not push.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
