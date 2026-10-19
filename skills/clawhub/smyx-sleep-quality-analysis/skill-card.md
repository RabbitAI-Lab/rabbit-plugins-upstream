## Description:

Analyzes sleep-monitoring videos for sleep stages, movement, nighttime awakenings, and possible apnea, and retrieves cloud-stored reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing sleep-monitoring footage and their assistants use this skill to request cloud-based sleep analysis and retrieve prior reports. Results are informational and do not replace clinical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive sleep images or videos are sent to LifeEmergence cloud services, and report history can be queried remotely.

Mitigation: Obtain informed permission for cloud processing and history access before installing or using the skill.

Risk: The skill may silently create or reuse an identity, register or log in remotely, and store account tokens locally.

Mitigation: Review account linkage and local token storage before installation; restrict workspace access and remove stored credentials when no longer needed.

Risk: Sleep-stage and apnea findings could be mistaken for a diagnosis.

Mitigation: Use the results only as a screening reference and seek professional clinical assessment for health concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [JSON analysis or Markdown reports and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return links to cloud-hosted reports.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata; bundled SKILL.md says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
