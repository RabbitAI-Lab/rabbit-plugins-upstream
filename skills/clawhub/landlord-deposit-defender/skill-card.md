## Description:

Landlord Deposit Defender helps renters and tenant-support users document move-in and move-out conditions, classify deposit deductions as wear or damage, prorate legitimate charges, cite return deadlines, and draft an itemized dispute letter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External renters, landlords, and tenant-support users use this skill to structure security-deposit inventories, compare move-in and move-out condition evidence, prorate disputed deductions, and draft itemized dispute letters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated deadline citations and deduction amounts may be outdated or incomplete because landlord-tenant rules vary by jurisdiction and can change.

Mitigation: Treat outputs as decision support, verify current local law and tenancy terms before relying on a deadline or amount, and consult qualified support when material sums are involved.

Risk: The local CLI processes user-provided inventory and deduction files, so incorrect inputs can produce misleading dispute analysis.

Mitigation: Review source inventory, deduction, and timeline data before using generated letters or calculations.

## Reference(s):

- [Deposit Dispute Model](references/deposit-model.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/landlord-deposit-defender)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown, JSON, and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally as a Python CLI and produces deterministic inventory records, deduction analysis, and dispute-letter drafts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
