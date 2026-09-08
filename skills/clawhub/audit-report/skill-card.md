## Description:

Use when the user wants audit findings turned into a stakeholder-ready document — severities, page counts, first-seen/fixed history — as a Markdown or CSV deliverable rather than a working diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External users, SEO teams, and developers use this skill to package validated site audit findings into stakeholder-ready Markdown reports, with CSV findings tables when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports could include site, query, or SEO data from configured third-party or paid connectors.

Mitigation: Use the skill only for sites and exports the user is authorized to analyze, and get review before using paid or third-party connectors.

Risk: The artifact references provider-selection.md, but that supporting document is not included in this package.

Mitigation: Confirm connector-selection expectations from the user's installed Groundcrew files or proceed with the included connector and reporting references only.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown report file and optional CSV findings table, with returned file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SHIP, FIX, BLOCK, and UNDECIDED verdicts; labels facts as Measured, User-provided, or Estimated.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
