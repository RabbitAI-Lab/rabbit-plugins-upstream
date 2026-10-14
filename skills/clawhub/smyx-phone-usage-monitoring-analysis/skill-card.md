## Description:

Analyzes workplace images and videos for employee phone use and produces monitoring findings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace administrators use this skill to review authorized office images or videos for phone-use behavior, view usage findings and recommendations, and retrieve past monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee images, videos, media URLs, and identity-linked reports are sent to a cloud service.

Mitigation: Use only for authorized workplace monitoring after legal and privacy review; notify employees and define retention and deletion procedures.

Risk: Service identities are created or reused without user-facing prompts, and access tokens are stored locally.

Mitigation: Review service-account permissions and local token storage, restrict access, and rotate credentials as needed.

Risk: Phone-use detections and compliance scores may be mistaken for conclusive employee misconduct.

Mitigation: Have a person review results and workplace context; do not use automated findings as the sole basis for personnel decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Phone usage monitoring API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report text or JSON, including findings, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be saved to a local file; historical report lists are retrieved from the cloud service.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
