## Description:

Analyzes submitted videos for child safety hazards such as climbing, playing with fire, contact with electrical sources, and dangerous activity near windows, then returns a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare staff can submit supported video clips to review possible child safety hazards and receive a structured report as an aid to direct supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option still sends videos for cloud processing, which may expose sensitive footage.

Mitigation: Avoid sensitive footage until the service's storage, retention, and access practices are confirmed; use an isolated workspace and dedicated credentials.

Risk: The bundled code does not support the promised instant safety alerts, so relying on it for live supervision could leave hazards unnoticed.

Mitigation: Treat this as submitted-video analysis, maintain direct supervision, and promptly confirm any reported hazard against the footage.

## Reference(s):

- [Skill API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON reports, text summaries, and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include detected behavior counts, risk indicators, suggestions, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
