## Description:

Analyzes Chinese EIA filings for investment due diligence by extracting structured production-line facts, grading regulatory-gaming risk, cross-validating capacity, yield, and emissions, inferring process and equipment signals, and recording sourced findings in an optional ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tianzhiceng297-boop](https://clawhub.ai/user/tianzhiceng297-boop)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and due-diligence teams use this skill to turn Chinese EIA reports and disclosures into structured investigation reports. It helps verify capacity claims, infer process routes and equipment tiers, back-calculate yield from material balance, audit regulatory-gaming patterns, and preserve provenance for deal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local eia-ledger may contain confidential due-diligence facts from EIA analysis.

Mitigation: Keep the eia-ledger directory in a private, access-controlled project area and avoid committing it to public repositories.

Risk: A user may only want a read-only analysis but the full workflow includes ledger persistence.

Mitigation: Ask the agent to skip Phase 6 when only a report is needed.

Risk: Cross-validation and equipment-route conclusions may be inferred from EIA-caliber evidence rather than directly disclosed facts.

Mitigation: Require source, page, quote, disclosure date, game_risk, and status fields for recorded facts, and keep disclosed facts separate from inferred conclusions.

## Reference(s):

- [Field Credibility Reference](references/field-credibility.md)
- [Cross-Validation Recipes](references/cross-validation.md)
- [Ledger Schema](references/ledger-schema.md)
- [Semiconductor Equipment Mapping](references/mappings/semiconductor-equipment.md)
- [Fictional IR-Detector Format Demo](examples/format-demo-ir-detector-en.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown investigation report with tables and optional append-only JSONL ledger records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Phase 6 can create an eia-ledger directory in a private project workspace; skip Phase 6 for a read-only report.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter, CHANGELOG.md, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
