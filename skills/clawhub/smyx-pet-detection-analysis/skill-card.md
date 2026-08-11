## Description:

Detects cats, dogs, and birds appearing in the target area; supports video stream and image detection, suitable for home pet monitoring scenarios. | 宠物检测技能，检测出目标区域内出现的猫、狗、鸟，支持视频流和图片检测，适用于家庭宠物监控场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to detect cats, dogs, and birds in uploaded images, local video files, or media URLs for home pet monitoring, and to retrieve cloud-hosted historical detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household pet images, videos, or media URLs may be sent to the Life Emergence cloud service for analysis.

Mitigation: Use the skill only when that cloud data flow is acceptable, avoid sensitive footage, and confirm the media source is intended for upload before execution.

Risk: The skill silently creates or reuses an internal identity and can retrieve account-linked report history.

Mitigation: Review history queries for the expected account context and avoid exposing internal identity values in user-facing output.

Risk: Account tokens may be stored in the workspace data directory.

Mitigation: Restrict workspace access, rotate or remove persisted tokens when no longer needed, and avoid running the skill in shared workspaces without review.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown reports or JSON, with an optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet counts, detection details, recommendations, report links, or a Markdown table of cloud-hosted historical reports.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
