## Description:

Turn rental-unit move-out or turnover inspection findings (reports, photos, notes) into a priced, vendor-ready make-ready scope using the Tektolo property turnover engine. Use when someone needs a turnover task list, a cost estimate, what to send each vendor, or an owner approval estimate for a US rental unit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tektolo](https://clawhub.ai/user/tektolo)

### License/Terms of Use:

MIT-0

## Use Case:

Rental property managers and owners use this skill to turn US move-out inspection findings into prioritized make-ready tasks, regional cost estimates, and vendor-ready work scopes. It also helps prepare estimates for owner approval and revise them using decisions or vendor pricing.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Inspection descriptions and optional business pricing are sent to Tektolo, which reports retaining anonymized estimate records; the hosted service itself was not audited.

Mitigation: Remove tenant names, addresses, and other personal details, share only necessary information, and review Tektolo's privacy policy before use.

Risk: Incorrect or uncertain findings and assumptions can make estimates misleading.

Mitigation: Review and confirm the findings and assumptions before relying on estimates, and treat cost ranges as estimates rather than quotes.

## Reference(s):

- [Tektolo Property Turnover Capability](https://tektolo.com/capabilities/property-turnover)
- [Tektolo Property Turnover MCP Server](https://tektolo.com/mcp)
- [Property Turnover Issue Catalog](https://tektolo.com/catalog.json)
- [Property Turnover Web Tool](https://tektolo.com/tools/rental-property/property-turnover)
- [ClawHub Skill Release](https://clawhub.ai/tektolo/skills/property-turnover)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, HTML, Excel workbooks]

**Output Format:** [Estimate summaries, assumptions, review notes, prioritized task lists, and per-trade vendor scopes; downloadable JSON, CSV, HTML, XLSX, and ZIP deliverables may also be provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides regional low, expected, and high estimates, source citations, assumptions, unknowns, and safety refer-outs. AI-read findings are drafts for review; estimates are not vendor quotes. Supports US properties only and does not diagnose hazardous conditions or provide deposit or tenant-charge legal advice.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
