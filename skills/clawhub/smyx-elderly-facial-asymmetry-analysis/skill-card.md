## Description:

Analyzes frontal elderly face images or short videos to estimate facial asymmetry, mouth-corner deviation, risk level, and report links for caregiver review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-monitoring workflow developers use this skill to submit elderly frontal face images or videos for auxiliary asymmetry screening, structured indicators, history lookup, and report links. The output is not a medical diagnosis and should be reviewed before acting on health-sensitive results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive face images, videos, and health-adjacent report history through configured cloud APIs.

Mitigation: Use only with informed consent from the elderly person, caregiver, or authorized representative, and avoid regulated medical or highly private deployments until data handling controls are verified.

Risk: The artifact silently resolves or creates an identity and can persist tokens locally for later API calls.

Mitigation: Require the publisher to explain the identity flow, token retention, server-side authorization checks, and credential deletion process before installation.

Risk: The output may be interpreted as medical guidance even though the skill is an auxiliary screening tool.

Mitigation: Present results as non-diagnostic indicators and route concerning symptoms or severe asymmetry to qualified medical review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an asymmetry index, mouth-corner drop side, risk level, key facial metrics, medical follow-up hints, and historical report records returned by the configured cloud service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
