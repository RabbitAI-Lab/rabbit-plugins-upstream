## Description:

Analyzes frontal face images or videos through a cloud service for facial asymmetry and produces screening reports and report-history links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and elder-care staff can submit a frontal face image or short video to review facial asymmetry indicators and request earlier reports. Results are screening aids, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Elderly face images or videos are sent to a configured cloud service.

Mitigation: Obtain the monitored person's explicit consent and use the skill only with a trusted publisher and service.

Risk: Automatic triggers may analyze images or retrieve health-related history without clear user control.

Mitigation: Require a specific, authorized request before analysis or history retrieval; avoid broad automatic triggers.

Risk: Internally managed identities and arbitrary open-id values can expose another person's reports.

Mitigation: Do not pass arbitrary open-id values; restrict report access to authorized identities.

Risk: Stored local tokens and report links can reveal sensitive account and health data.

Mitigation: Treat tokens and report links as sensitive; limit access and avoid sharing them in logs or responses.

Risk: Facial screening results may be mistaken for a clinical diagnosis.

Mitigation: Treat findings as screening guidance only and seek prompt professional care for suspected stroke symptoms.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Text with structured results; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or save results to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
