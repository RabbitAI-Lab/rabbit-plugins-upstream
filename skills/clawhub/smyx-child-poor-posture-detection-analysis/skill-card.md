## Description:

Analyzes submitted videos of children at study desks to estimate posture metrics and return reminder text and structured session reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and operators of smart study lamps or desks use the skill to review study-session video, see estimated posture indicators, and receive reminder text and a session report. The estimates are for posture awareness and do not provide medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious, citing reported account and token management, video uploads to an analysis service, differences from the advertised live-monitoring workflow, and incomplete scan coverage; this does not establish malicious intent.

Mitigation: Review the external processing and account/token handling before use. Obtain a guardian's informed consent for children's video and limit uploads to footage intended for analysis.

Risk: Posture angles are visual estimates and may differ from medical measurements.

Mitigation: Treat the results as posture-awareness guidance, not a medical assessment; consult a qualified clinician for health concerns.

## Reference(s):

- [API interface notes](artifact/references/api_doc.md)
- [Skill release page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [Usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured posture summaries and reminder text; report lists may be formatted as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture estimates, session summaries, and report links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
