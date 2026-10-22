## Description:

Creates or repairs a reusable Beangulp importer from bank-export samples, with reviewed golden files and a passing test harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers use this skill to create or repair Python Beangulp importers for bank-export formats and validate them with reviewed golden-file tests. It keeps authoring separate from importing transactions into a live ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An importer can misread transaction dates, signs, or amounts and produce incorrect entries.

Mitigation: Compare generated golden files with the source sample and review representative rows before approving the importer.

Risk: Bank-export samples may contain private financial details.

Mitigation: Redact private details before sharing samples or committing them to the test corpus.

Risk: A wired importer may be mistaken for approval to import transactions into a real ledger.

Mitigation: Review the runner diff explicitly; treat any real-ledger import as a separate, deliberate action.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/puncsky/skills/beancount-importer-author)
- [Metadata homepage (beancount-io skills)](https://github.com/bex-co/beancount-io/tree/main/skills)
- [Beangulp API reference](references/beangulp-api.md)
- [bea CLI reference](references/bea-cli.md)
- [Import deduplication reference](references/dedup.md)

## Skill Output:

**Output Type(s):** [Code, Files, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Python importer code, Beangulp golden-file tests, configuration changes, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated golden files against source rows; wiring requires approval, and running imports into a live ledger is separate.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
