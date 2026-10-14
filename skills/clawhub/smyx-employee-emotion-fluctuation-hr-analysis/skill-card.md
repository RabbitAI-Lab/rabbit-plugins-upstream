## Description:

Analyzes workplace camera video to compare observed expressions and behavior with historical baselines and produce employee emotion-fluctuation alerts for HR review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized HR teams use workplace video to review anonymized changes in employee expressions and behavior and prepare supportive check-ins. The reports are intended for HR care, not employment decisions or clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace video analysis may expose sensitive employee information or proceed without meaningful consent.

Mitigation: Use only where legally approved, provide clear employee notice and opt-out, and restrict report access to authorized HR staff.

Risk: Office video or video URLs and reports may be sent to external services.

Mitigation: Review and approve configured endpoints, data handling, and authorization controls before supplying footage or video links.

Risk: Automatic account identity and retained local token or user records may expand access or leave sensitive data behind.

Mitigation: Review the local data directory, identity lifecycle, and permissions; limit access and retention to approved HR workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [HR report API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report or Markdown report list; optional JSON-style output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes emotion-fluctuation alerts, care suggestions and links to reports when available.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
