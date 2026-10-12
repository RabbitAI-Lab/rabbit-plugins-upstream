## Description:

Estimates livestock body size and weight from side-view images or videos and helps track fattening progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and their agents use side-view livestock media to estimate body dimensions, weight, and fattening stage, or to retrieve previous analysis reports. Estimates are a monitoring aid, not a substitute for weighing animals or making husbandry decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm media, media URLs, and report-history requests are sent to an external service.

Mitigation: Review data sensitivity and obtain authorization before submitting farm media or querying account history.

Risk: The skill may create or reuse a cloud identity automatically and stores service tokens in a local workspace database.

Mitigation: Review identity creation before use and restrict access to the workspace database and cloud account.

Risk: Visual body-size and weight estimates can be unreliable when the view is obscured or lacks a scale reference.

Mitigation: Use clear side views with a known-size reference and verify consequential decisions with physical measurements.

## Reference(s):

- [Livestock estimation API reference](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured estimation results and report links; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on clear side views and a known-size reference; optional output file.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
