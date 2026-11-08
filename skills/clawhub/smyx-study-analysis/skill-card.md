## Description:

Analyzes children's and students' learning behavior from video and provides structured reports and family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and educators can use the skill to review a child's study-session video and receive observations about attention, posture, and study habits, with suggestions for home learning. Its documentation describes the results as family education guidance, not a substitute for assessment by a teacher or mental-health professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the export-only setting and API-address option do not behave as documented, and credential-bearing requests need destination restrictions.

Mitigation: Have the publisher address these controls before use with children's footage, and limit credential-bearing requests to approved HTTPS destinations.

Risk: Study videos and associated data are uploaded for cloud analysis; the stated immediate deletion of original videos is unverified.

Mitigation: Confirm the service's data retention and deletion terms before uploading footage, and use only footage approved for this service.

Risk: Account creation, token storage, deletion, and report identity handling are not fully explained in the security guidance.

Mitigation: Clarify those practices with the publisher and use a dedicated workspace to avoid sharing report identity.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Text]

**Output Format:** [Structured analysis report in JSON; Markdown tables for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior observations, family education suggestions, risk indicators, and cloud report links.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
