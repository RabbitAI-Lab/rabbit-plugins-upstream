## Description:

A free deterministic checker for accounts-payable provisional ledgers that recalculates nine in-scope checks, cites source line numbers for findings, and runs locally without payment, registration, API keys, or network use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts-payable users run this skill before monthly close to check AP provisional ledger rows, totals, duplicate document numbers, missing fields, negative values, and invoice-status markers. It helps identify arithmetic and table-consistency issues, but it does not provide accounting, audit, tax, or invoice-validity advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic findings as accounting, audit, tax, or invoice-validity advice.

Mitigation: Use the output as a local ledger consistency check only, and have qualified finance, audit, or tax reviewers decide any accounting treatment or compliance action.

Risk: Incomplete, malformed, or headerless ledger input can lead to no conclusion or only scoped findings.

Mitigation: Provide the required AP provisional ledger headers and review any missing-input messages before relying on the result.

Risk: The free release omits several cross-period, aging, and AP-detail reconciliation checks.

Mitigation: Review the reported checks_not_run and do not rely on this release for checks it explicitly withholds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-provisional-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with source line numbers, summaries, scoped checks, missing-input guidance, and local Node.js command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; accepts JSON or pasted ledger text with required headers and rejects insufficient input instead of inventing conclusions.]

## Skill Version(s):

1.0.65 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
