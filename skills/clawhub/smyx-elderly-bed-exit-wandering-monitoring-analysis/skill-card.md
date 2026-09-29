## Description:

Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods. It is suitable for night-time safety monitoring in nursing homes and for elderly people living alone. | 老人离床徘徊监测技能，识别夜间起床离床、长时间徘徊、长时间静止不动异常行为，适用于养老院、独居老人夜间安全监测

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, caregivers, and agent operators use this skill to analyze nighttime elderly-monitoring video or image inputs for bed-exit events, prolonged wandering, and extended immobility. It can also query cloud history for prior monitoring reports and return structured results with report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive care-setting video, identity selection, cloud history, and cached cloud tokens.

Mitigation: Review before installing in any real care setting, obtain consent from the monitored person or authorized caregiver, and treat local workspace data as sensitive.

Risk: The local skill may pass locally supplied open_id or mobile identity values to cloud services.

Mitigation: Verify that the cloud service authenticates users independently and does not trust locally supplied identity values.

Risk: Elderly-monitoring outputs can be safety-relevant but are not a substitute for in-person confirmation.

Mitigation: Use analysis and alerts as care-support signals and require caregivers or family members to verify abnormal events promptly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write requested output to a local file; history-list mode returns cloud report records.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
