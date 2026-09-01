## Description:

Analyzes office workstation images or video to report prolonged sitting and posture-warning signals such as neck-forward angle, back curvature, shoulder asymmetry, screen distance, and standing activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace health teams, and developers use this skill to analyze office workstation video or image inputs for prolonged sitting and posture warning reports. It is intended for behavior-oriented workplace health reminders, not medical diagnosis or rehabilitation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office video and report history may be handled by the provider's cloud API.

Mitigation: Require employee notice and consent, define access controls for historical reports and export links, review retention and deletion practices, and avoid sensitive recordings unless the cloud handling is acceptable.

Risk: The skill silently creates and persists user identity tokens for analysis and report history.

Mitigation: Review identity and token storage behavior, backend endpoints, and organizational approval requirements before workplace deployment.

Risk: Posture warnings could be mistaken for medical advice.

Mitigation: Present results as visual activity and posture reminders only, and direct users with neck, back, or other health concerns to qualified professionals.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report with posture metrics, warning type, reminder text, summary, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return current analysis results or a Markdown table of historical cloud reports.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
