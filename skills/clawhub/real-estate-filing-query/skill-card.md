## Description:

Guides collection and analysis of publicly disclosed property listings and filing prices, producing Excel reports, period comparisons, and anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Real-estate analysts and developers use this workflow to organize publicly disclosed project listings, track filing prices and sales status, and compare results across reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated collection may violate site rules or access nonpublic data.

Mitigation: Confirm that automation is permitted, use only public disclosures, and stop when access requires authentication or is prohibited.

Risk: Raw response caches may retain details beyond the aggregate report.

Mitigation: Delete or redact raw API debug caches after troubleshooting.

Risk: Missing permits or building units can undercount listings and distort comparisons.

Mitigation: Check every permit and building-unit combination, deduplicate records, and validate totals before reporting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chriskinhaha/skills/real-estate-filing-query)
- [Real-estate collection guide](references/real-estate-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Excel reports, JSON snapshots]

**Output Format:** [Markdown guidance, five-sheet XLSX workbook, and aggregate JSON history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-level analysis includes period comparisons and anomaly alerts; a raw response cache is optional for troubleshooting.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
