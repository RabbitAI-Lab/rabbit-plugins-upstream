## Description:

Checks project billing and collection ledgers for row-level arithmetic, total reconciliation, duplicate rows, blanks, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and project operations users apply this skill during monthly closing, reconciliation, or inventory checks to review project billing and collection ledgers before downstream accounting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic and consistency findings as a complete accounting, legal, invoice-validity, or revenue-recognition review.

Mitigation: Use the output as a ledger-checking aid and verify invoice validity, payment terms, contract scope, and accounting treatment against authoritative records and applicable policy.

Risk: The release help text mentions anonymous usage statistics, while the security evidence says the inspected version did not contain network code to send them.

Mitigation: Review network behavior when updating or redistributing the skill, especially if usage-statistics code is later added.

Risk: The free release omits several checks that are listed as withheld.

Mitigation: Review the reported withheld checks before relying on a clean result, and run additional review for over-billing, over-collection, aging, progress mismatch, or zero-contract cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-billing-collection-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON findings with source-row references and summary status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs executed checks, withheld checks, missing-input guidance when applicable, and a disclaimer that findings are arithmetic and consistency aids.]

## Skill Version(s):

1.0.48 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
