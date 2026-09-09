## Description:

Investigation workflow that turns Chinese EIA reports into investment due-diligence intelligence through structured extraction, adversarial field-credibility grading, physics-based cross-validation, process-to-equipment mapping, and an append-only provenance ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tianzhiceng297-boop](https://clawhub.ai/user/tianzhiceng297-boop)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and due-diligence teams use this skill to analyze Chinese environmental impact assessment filings, extract production-line facts, test reported numbers for regulatory distortion, infer process routes and equipment selection, and maintain a provenance-backed ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: EIA filings can contain distorted or incomplete reported numbers, leading to misleading due-diligence conclusions.

Mitigation: Apply the skill's field-credibility grading and cross-validation steps before treating reported values as reliable.

Risk: Ledger writes could add unwanted records to a project workspace.

Mitigation: Preview or confirm writes to eia-ledger/<track>.jsonl and failed-queries.md before appending records.

## Reference(s):

- [Field Credibility Grades](en/references/field-credibility.md)
- [Cross-Validation Recipes](en/references/cross-validation.md)
- [Ledger Schema](en/references/ledger-schema.md)
- [Semiconductor Equipment Mapping](en/references/mappings/semiconductor-equipment.md)
- [Worked Example: Fictional IR-Detector Company EIA](examples/format-demo-ir-detector-en.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSONL, Guidance]

**Output Format:** [Markdown reports with structured tables and optional append-only JSONL ledger entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ledger entries are scoped to the due-diligence project workspace under eia-ledger/<track>.jsonl; unresolved ontology needs may be recorded in failed-queries.md.]

## Skill Version(s):

0.1.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
