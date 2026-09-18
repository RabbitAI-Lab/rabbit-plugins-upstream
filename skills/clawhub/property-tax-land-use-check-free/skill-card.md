## Description:

A free deterministic checker for property tax and urban land use tax worksheets that recalculates declared amounts, compares them with book tax values, and cites source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax teams use this skill before filing to recalculate property tax and urban land use tax worksheet amounts, identify table differences, and distinguish free checks from paid-only checks. It is for arithmetic and worksheet reconciliation, not tax advice or policy determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade path asks an agent to run an unpinned remote installer and begin a purchase or install workflow.

Mitigation: Verify the SkillPay source, package version, payment terms, and platform rules independently before allowing any installer, purchase, or additional skill installation.

Risk: The skill handles copied tax worksheet text.

Mitigation: Run it only in an environment appropriate for the worksheet data and review line-cited findings before relying on them.

Risk: The checker does not determine local tax policy applicability or provide tax advice.

Mitigation: Use it for worksheet recalculation and reconciliation only; have a qualified reviewer confirm deduction ratios, land tax standards, exemptions, and filing treatment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-tax-land-use-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable text or structured JSON findings with worksheet line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires worksheet text with recognizable headers; does not read .xlsx files directly.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
