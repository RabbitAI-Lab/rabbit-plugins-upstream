## Description:

Analyzes video for mental-health indicators and provides structured reports and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking mental-health insights use the skill to analyze video for emotional and behavioral patterns, receive a structured report, and review their historical reports. Results are informational and do not replace clinical assessment or care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive video, biometric cues, and mental-health inferences are sent to external services without a clear consent boundary.

Mitigation: Obtain informed consent before use and confirm where data is sent, who can access it, and how it is retained and deleted.

Risk: The skill silently creates or reuses an identity and stores authentication tokens locally, linking report history to that identity.

Mitigation: Review account creation and token storage before installation; restrict access to credentials and historical reports.

Risk: Mental-health findings may be mistaken for a clinical diagnosis.

Mitigation: Treat reports as informational only and seek qualified professional care for diagnosis or treatment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured text or JSON analysis report; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report-export link or be saved to a local file.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
