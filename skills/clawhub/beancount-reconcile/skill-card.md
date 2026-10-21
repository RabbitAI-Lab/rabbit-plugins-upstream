## Description:

Reconcile one account in a local Beancount ledger against a CSV or PDF statement. Report missing entries, duplicates, amount mismatches and date drift; confirm missing-entry writes and a passing period-end balance assertion through bea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

People maintaining Beancount ledgers use this skill to reconcile one account against a statement, review discrepancies, and confirm approved corrections with a balance assertion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions conflict about hosted financial ledgers and changes to existing records.

Mitigation: Resolve the conflict before use; agree on the target account, append-only changes, and separate authorization for hosted access or edits to existing entries.

Risk: A multi-step write can partially succeed before a later validation step fails.

Mitigation: Back up the ledger, review the destination and proposed entries, and re-read and check the ledger before resuming after a failure.

## Reference(s):

- [Shared bea command recipes](artifact/references/bea-cli.md)
- [CSV import through bea](artifact/references/bea-import.md)
- [Compatibility paths](artifact/references/compatibility.md)
- [Deduplication rules](artifact/references/dedup.md)
- [Statement export formats](artifact/references/formats.md)
- [Transaction matching rules](artifact/references/matching.md)
- [Statement normalization](artifact/references/statement-formats.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown reconciliation report with proposed Beancount entries and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports discrepancies and proposed changes for user review; writes require confirmation.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
