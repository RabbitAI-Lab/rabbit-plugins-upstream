## Description:

Monitors Huawei AppGallery app versions, update notes, ratings, and recent negative reviews from a user-provided spreadsheet, then generates a PDF summary report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jasoncod](https://clawhub.ai/user/jasoncod)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, product, and app-market monitoring teams use this skill to batch-check Huawei AppGallery listings from an attached Excel file and receive a PDF report covering version activity, update notes, and recent negative reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dedicated trigger phrase can start a batch AppGallery workflow as soon as it is paired with a spreadsheet attachment.

Mitigation: Use the trigger only when the attached spreadsheet is intended for this skill and review the generated report before relying on it.

Risk: GUI-driven AppGallery lookups may produce missing or stale rows when listings, comments, or page structure are unavailable during collection.

Mitigation: Review any recorded gaps in the report and rerun affected app lookups when market data completeness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jasoncod/skills/appmarketmonitor)
- [ClawHub publisher profile](https://clawhub.ai/user/jasoncod)
- [Huawei AppGallery](https://appgallery.cloud.huawei.com)

## Skill Output:

**Output Type(s):** [text, files, guidance]

**Output Format:** [PDF report with tabular app-market findings and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes an attached spreadsheet of app names and optional Android update dates; uses phone GUI automation and PDF generation tools.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
