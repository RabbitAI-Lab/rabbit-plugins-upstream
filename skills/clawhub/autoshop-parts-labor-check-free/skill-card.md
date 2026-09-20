## Description:

Checks auto repair work order parts and labor settlement tables by recalculating part subtotals, labor fees, work order totals, duplicate part rows, negative quantities or hours, and missing required fields, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External auto repair service advisors, parts inventory staff, and settlement accountants use this skill to check copied work order tables before customer settlement or periodic reconciliation. It helps identify arithmetic and table-consistency issues while leaving price fairness, installation verification, and accounting treatment to separate review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker can identify arithmetic and table-consistency issues but does not determine whether prices are fair, parts were installed, labor occurred, or accounting treatment is correct.

Mitigation: Use the output as a settlement consistency aid and verify price basis, installation evidence, labor records, and accounting handling with the relevant invoices, work orders, contracts, or shop procedures.

Risk: The skill processes auto repair settlement data through a local Node.js command and file input.

Mitigation: Run it only in an environment approved for the input data and review the disclosed local execution and file-reading behavior before use.

Risk: Chinese-language inputs and outputs may be unsuitable for reviewers who cannot validate the required table columns and findings.

Mitigation: Have a Chinese-reading reviewer confirm column mapping, missing-field messages, and source-row citations before relying on the result.

Risk: The free release omits overcharge attribution, cross-store or cross-order summary ledgers, and sorted remediation lists.

Mitigation: Treat those areas as out of scope for this release and perform separate analysis when attribution or aggregated remediation planning is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/autoshop-parts-labor-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Chinese human-readable text or JSON from a local Node.js CLI, with findings citing source row numbers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a text work order table with required columns; returns insufficient-input guidance instead of conclusions when the material cannot support checks.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
