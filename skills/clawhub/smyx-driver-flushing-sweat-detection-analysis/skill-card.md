## Description:

Analyzes in-cabin DMS driver face video for facial flushing and sweat-reflection signals, then returns visual health-risk reminders and rest or medical-care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers, fleet operators, and developers use this skill to analyze driver-face video or report history for visual signs of facial flushing and abnormal sweating. It supports health-adjacent driver safety reminders, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-face video and health-adjacent reports are processed through vendor cloud APIs.

Mitigation: Use only with confirmed driver or employee consent, approved report access controls, and reviewed retention terms.

Risk: The skill silently creates and persists identity tokens for API access.

Mitigation: Protect the workspace data directory and local token database, and confirm token rotation or revocation procedures before deployment.

Risk: Broad report-history queries could expose driver or fleet health events beyond the intended scope.

Mitigation: Limit history queries to authorized accounts, drivers, fleets, and time ranges, and audit access to exported report links.

Risk: Visual flushing or sweating alerts may be mistaken for medical diagnosis.

Mitigation: Present results as visual abnormality reminders only and direct users to professional medical evaluation when symptoms or concerns exist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Driver flushing and sweat detection API documentation](references/api_doc.md)
- [General analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-style structured analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health-risk reminder text, recommended actions, report links, and structured history results.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
