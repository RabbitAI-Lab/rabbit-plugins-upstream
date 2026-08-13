## Description:

Utilizes vision and radar technology for contactless detection of falls. It triggers alarms within seconds and is suitable for home safety monitoring of elderly people living alone. | 老人跌倒检测技能，视觉/雷达无感识别摔倒倒地，秒级触发报警，适用于独居老人居家安全监测场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home-monitoring images, videos, or media URLs for possible elderly falls and to retrieve structured fall-detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring images, videos, URLs, identity values, and report requests may be sent to lifeemergence.com services.

Mitigation: Use only with explicit consent and only after the publisher provides acceptable privacy, retention, deletion, and data-handling guarantees.

Risk: The skill may silently create or reuse account identity and persist tokens or profile data.

Mitigation: Review token storage and identity behavior before installation, prefer a separate workspace, and avoid regulated care settings until the behavior is clarified.

Risk: Fall-detection output can be incorrect or incomplete and should not be treated as a sole emergency decision source.

Mitigation: Use results as safety alerts that require human confirmation and established emergency-response procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API 接口文档](artifact/references/api_doc.md)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [Markdown or JSON analysis report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links returned by the remote analysis service.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
