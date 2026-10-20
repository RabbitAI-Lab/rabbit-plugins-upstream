## Description:

Reconcile one account in a local Beancount ledger against a CSV or PDF statement. Report missing entries, duplicates, amount mismatches and date drift; confirm missing-entry writes and a passing period-end balance assertion through bea. Use for checking whether an account matches its statement. Skip bulk imports, single manual entries (beancount-add), analytics, multi-account close orchestration, edits to existing entries, and ledgers hosted on Beancount.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and bookkeepers use this skill to reconcile one Beancount account against a CSV or PDF statement, review discrepancies, and confirm proposed missing entries and a period-end balance assertion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial-record instructions may extend beyond the stated local, append-only scope.

Mitigation: Confirm the selected local ledger is the only target, keep existing entries unchanged, make a backup, approve each proposed write, and review any hosted-service handoff or metadata edit separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-reconcile)
- [Matching guidance](references/matching.md)
- [Statement formats](references/statement-formats.md)
- [Deduplication guidance](references/dedup.md)
- [Supported formats](references/formats.md)
- [bea CLI guidance](references/bea-cli.md)
- [CSV import guidance](references/bea-import.md)
- [Compatibility guidance](references/compatibility.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with reconciliation summaries, proposed Beancount transactions, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One account per run; proposed ledger writes require user approval.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
