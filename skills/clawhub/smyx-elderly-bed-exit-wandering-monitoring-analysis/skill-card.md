## Description:

Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods. It is suitable for night-time safety monitoring in nursing homes and for elderly people living alone. | 老人离床徘徊监测技能，识别夜间起床离床、长时间徘徊、长时间静止不动异常行为，适用于养老院、独居老人夜间安全监测

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, nursing-home operators, and developers use this skill to submit nighttime monitoring video or public video URLs for bed-exit, wandering, and prolonged-stillness analysis and to retrieve cloud-stored historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive local videos, public video URLs, identifiers, and report history may be sent to lifeemergence.com services.

Mitigation: Use only with explicit authorization from the monitored person or responsible caregiver, and confirm that cloud processing and retention are acceptable for the deployment.

Risk: The skill can silently create or reuse an identity and store service tokens locally.

Mitigation: Run in an isolated workspace, review local account and token storage before deployment, and remove local credential state when the skill is no longer needed.

Risk: Behavior-recognition results may be incomplete or incorrect in a care setting.

Mitigation: Treat results as safety-care support only and require human confirmation before making care or emergency decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [JSON or Markdown text with structured analysis results, history lists, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4, avi, or mov files up to 10 MB, public video URLs, and cloud history queries.]

## Skill Version(s):

1.0.16 (source: server release evidence; artifact SKILL.md frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
