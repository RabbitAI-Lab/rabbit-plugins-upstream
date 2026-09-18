## Description:

A local deterministic checker for scrap and offcut sale settlement ledgers that recalculates settlement quantity, settlement amount, ledger revenue, balances, totals, duplicate weighbridge tickets, blanks, and negative values, with source line references for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, accounting, and internal audit users can run this skill during month-end close or audit preparation to check scrap sale settlement ledgers against arithmetic and ledger consistency rules. It is aimed at manufacturing and construction workflows where weighbridge, settlement, inventory balance, and ledger revenue fields need line-level review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a paid upgrade path that can prompt remote payment tooling and purchase authorization.

Mitigation: Use the free local checker without running payment onboarding commands unless the user explicitly requests the paid edition and independently verifies the payment provider, package, merchant, and terms.

Risk: Users may overread an arithmetic pass as proof that all scrap revenue, tax, contract, or audit obligations are satisfied.

Mitigation: Treat outputs as deterministic ledger checks only; review contracts, tax treatment, source documents, and audit conclusions separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/scrap-sale-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON from a local Node.js runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields rather than conclusions.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
