## Description:

Analyzes children's classroom or desk videos for visual signs of drowsiness and returns a fatigue score and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and parents use the skill to review children's learning-session videos, check fatigue indicators and report history, and decide when a break or closer observation is needed. It is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's videos or video URLs are sent to cloud services.

Mitigation: Obtain guardian or school consent and verify the service's retention and deletion practices before use.

Risk: The skill may silently create or reuse an identity and store service tokens locally.

Mitigation: Review local data storage, protect workspace access, and clear stored credentials when no longer needed.

Risk: Automatic access to prior reports may expose children's sensitive history.

Mitigation: Limit report access to authorized users and review report-sharing behavior before installation.

Risk: Visual fatigue estimates may be mistaken for medical diagnoses.

Mitigation: Use reports only as observational aids; rely on adult judgment and seek professional care for persistent concerns.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or Markdown summary with fatigue indicators, score, level, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list previous reports or save a report to a file.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
