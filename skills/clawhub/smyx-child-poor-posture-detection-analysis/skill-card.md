## Description:

Analyzes child study-area images or videos through a configured service to estimate poor-posture indicators, produce structured results, and return reminder text and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze child study-area posture media, estimate visual posture metrics such as head tilt and Cobb-angle approximation, and retrieve structured reports or reminder text. It is intended for habit-support workflows, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's posture videos or URLs may be sent to a configured remote service.

Mitigation: Use only with guardian consent and an explicit plan for retention, deletion, access control, and report sharing.

Risk: The skill silently creates and reuses a local identity and may persist tokens for service access.

Mitigation: Review the workspace identity file and local token database before deployment; clear or rotate persisted credentials when changing users or environments.

Risk: Configuration may include development or non-production service endpoints.

Mitigation: Review and replace service configuration before commercial use, especially any HTTP or development endpoints.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Shared API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze a local video file or URL, and can list historical report records returned by the configured service.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
