## Description:

A free deterministic agent skill that checks consignment settlement ledgers by recomputing stock balances, payable amounts, commissions, totals, duplicate document numbers, blanks, negative values, and reversed dates with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External retail, manufacturing, brand, finance, and operations users use this skill during monthly consignment settlement reconciliation. It helps recompute ledger formulas and surface line-cited findings while withholding conclusions when input material is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security verdict is suspicious and the packaged runner is reported as broken.

Mitigation: Require manual review before install or use, and validate the runner in a controlled environment before relying on the skill.

Risk: The instructions include an external paid install and purchase flow.

Mitigation: Do not run the external npx purchase or install command unless the publisher, package, payment flow, and platform rules have been independently verified, and require the user to confirm any wallet authorization or payment.

Risk: The free release does not perform paid-only checks such as unpaid sold items, overcharged commission, return offsets, general-ledger inventory mismatches, or physical-count differences.

Mitigation: Do not rely on the free release for those paid-only checks; disclose the unperformed checks and use independent reconciliation for those risks.

Risk: The skill handles financial reconciliation outputs that could affect settlement decisions.

Mitigation: Have a qualified human review findings against source ledgers, contracts, tax treatment, and payment records before taking commercial, legal, or collection action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/consignment-settlement-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with source-line citations, plus shell commands for running the local checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Insufficient inputs return missing-field guidance rather than unsupported conclusions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
