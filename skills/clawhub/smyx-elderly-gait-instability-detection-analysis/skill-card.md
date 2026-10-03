## Description:

Analyzes walking videos to summarize gait metrics and screen for low, medium, or high fall risk in older adults.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care teams use walking footage to review gait measures, fall-risk screening results, and historical reports. Results support monitoring, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or private video URLs are sent to the Life Emergence cloud service.

Mitigation: Obtain consent from the recorded person or caregiver and avoid sensitive signed or private URLs unless intended.

Risk: The skill can create or reuse a local identity, store tokens, and access sensitive cloud report history with limited user control.

Mitigation: Review account, token storage, and report-history access controls before production use.

Risk: Fall-risk screening results may be mistaken for a medical diagnosis.

Mitigation: Treat results as screening information and seek professional assessment for clinical decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)
- [Gait analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured gait report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gait metrics, low/medium/high fall-risk screening, and optional report links; historical reports may be retrieved from the cloud.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
