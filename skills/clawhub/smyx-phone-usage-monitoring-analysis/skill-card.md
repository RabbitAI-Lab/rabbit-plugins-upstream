## Description:

Analyzes workplace images and video for employee phone use, returning detection results, usage statistics, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace administrators use the skill to review images or video for employee phone use, view usage summaries and warnings, and retrieve historical monitoring reports. Results should inform human review rather than determine employee discipline alone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace surveillance and third-party cloud processing can expose sensitive employee images, video, and report history.

Mitigation: Obtain appropriate legal approval and employee notice before use; restrict access and retention, and approve cloud processing of workplace media.

Risk: Automatically stored or reused identity tokens may link monitoring reports to a user without clearly surfacing that behavior.

Mitigation: Review identity handling and access controls before installation; protect tokens and historical reports as sensitive data.

Risk: Phone-use detections and compliance assessments may be inaccurate or taken out of context.

Mitigation: Require human review and do not use the skill as the sole basis for employee discipline.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Phone usage monitoring API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results in JSON or readable report text; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include usage counts and durations, warnings, recommendations, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
