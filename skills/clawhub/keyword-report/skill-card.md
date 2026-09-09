## Description:

Use when the user wants a periodic keyword position report, including quick wins, striking distance, and movement since the last period, from Search Console data or the TrustGrowth keyword lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

SEO operators, marketers, and site owners use this skill to generate source-labeled keyword movement reports for a specific reporting period. It emphasizes changes, actionable next steps, and clear labels for measured, user-provided, and estimated data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may work with SEO exports and optional configured services such as Search Console, analytics, TrustGrowth, Ahrefs, Semrush, or PageSpeed.

Mitigation: Review connector use before sharing credentials, approve paid API batches before execution, and avoid exposing API keys in reports or logs.

Risk: Two referenced guidance files are missing from this package, which can make connector selection and paid-index handling less explicit.

Mitigation: Confirm connector-selection and paid-index procedures from current vendor documentation before using those paths, and report unavailable measurements as unknown.

Risk: Keyword reports can mix first-party measurements, user-provided exports, and third-party estimates.

Mitigation: Keep labels, source names, and observation dates visible, and avoid comparing deltas across different measurement sources or labels.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown report with source-labeled tables; optional CSV detail export when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish Measured, User-provided, and Estimated values and preserve source and observation date for keyword positions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
