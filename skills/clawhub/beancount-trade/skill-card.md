## Description:

Records described investment events in a Beancount ledger with reviewed lots and cost basis, proposing entries for confirmation before writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People maintaining Beancount ledgers use this skill to record stock, fund, and crypto trades and related investment events, including realized-gain reports. It proposes entries for review before writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a conflict: the skill requires approval before bookkeeping changes but directs access to online financial ledgers despite advertising local-only use.

Mitigation: Resolve the hosted-ledger conflict before installing, or restrict the skill to a named local ledger with hosted tools unavailable. Keep a ledger backup and review the exact entries before approving writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/puncsky/skills/beancount-trade)
- [Project homepage (listed in release metadata)](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [text, code, shell commands]

**Output Format:** [Beancount ledger entries and human-readable proposals or realized-gain reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries are proposed for confirmation before writing; realized-gain reports are read-only.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
