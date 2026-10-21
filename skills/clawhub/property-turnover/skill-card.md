## Description:

Turns US rental-unit move-out inspection findings into priced, vendor-ready make-ready scopes using Tektolo's property turnover engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tektolo](https://clawhub.ai/user/tektolo)

### License/Terms of Use:

MIT-0

## Use Case:

Property managers and rental owners use this skill to turn US move-out reports, photos, and notes into turnover cost estimates, trade-specific scopes, and owner approval summaries.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Rental inspection details may be sent to Tektolo and, for AI reading, Azure OpenAI.

Mitigation: Avoid submitting names, faces, street addresses, or other personal details; describe conditions and rooms instead.

Risk: Unconfirmed AI readings and estimated prices may be mistaken for verified findings or firm quotes.

Mitigation: Show AI-read findings for user confirmation before quoting totals, and label prices as estimates rather than contractor quotes or legal deposit decisions.

Risk: Hazardous conditions could require professional assessment beyond a turnover estimate.

Mitigation: Refer suspected mold, asbestos, lead, gas, electrical, or structural hazards to qualified professionals rather than diagnosing or pricing remediation.

## Reference(s):

- [Property turnover capability and schemas](https://tektolo.com/capabilities/property-turnover)
- [Tektolo issue catalog](https://tektolo.com/catalog.json)
- [Property turnover web tool](https://tektolo.com/tools/rental-property/property-turnover)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary with estimate ranges, trade scopes, assumptions, and optional download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AI-read findings are drafts pending user confirmation; estimates are not contractor quotes.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
