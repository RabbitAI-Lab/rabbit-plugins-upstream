## Description:

Analyzes adult facial images or short videos for visible fatigue-related features and returns a 0–100 fatigue/stress index with a report and guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use the skill to assess visible fatigue-related features in consenting adults' face images or short videos and review scores, suggestions, and past reports. Results are for personal awareness, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adult face media and fatigue/stress results are sent to a cloud service and may be sensitive.

Mitigation: Obtain informed consent from the person depicted and review the service's data retention practices before use.

Risk: Automatic identity creation, local token storage, and cloud report-history access can expose private records, especially on shared devices.

Mitigation: Review local account and token storage, access controls, and report-history authorization before deployment, particularly for workplace or shared-camera use.

Risk: A face-based fatigue/stress score may be misleading and is not a clinical assessment.

Mitigation: Treat results as personal guidance rather than a diagnosis; account for lighting, makeup, and variation between images.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 index, fatigue category, suggestions, and report links where available.]

## Skill Version(s):

1.0.9 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
