## Description:

A local Chinese-language checker for lease liability and deferred government grant worksheets that runs two built-in checks per contract directory and prints one conclusion line per contract with source file and line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

General ledger accountants use this skill before monthly amortization reviews and annual settlement work to check exported lease and deferred-income worksheet materials. It helps identify arithmetic and reconciliation issues across contract folders, but it does not replace accounting judgment, audit work, tax advice, or document authenticity review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a clean result as an audit opinion or proof that contracts, subsidy documents, bank records, tax treatment, or unexecuted subchecks were reviewed.

Mitigation: Use results as local worksheet checks only; have qualified accounting, audit, or tax reviewers evaluate business judgment, document authenticity, tax treatment, and checks outside the free package scope.

Risk: Incomplete or poorly structured input may cause checks to be skipped rather than proving there are no issues.

Mitigation: Review the per-contract status and not-run sections, and provide exported worksheet text with one contract per directory before relying on the findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lease-deferred-pack-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, shell commands, guidance]

**Output Format:** [Console text followed by structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite contract name, check name, source file, line number, severity, and numeric details when available.]

## Skill Version(s):

1.0.16 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
