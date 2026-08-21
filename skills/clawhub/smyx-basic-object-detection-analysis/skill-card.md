## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels appearing in the target area. Supports video stream and image detection, suitable for general security surveillance scenarios. | 基础目标检测技能，检测出目标区域内出现的人、车、非机动车、宠物、包裹，支持视频流和图片检测，适用于通用安防监控场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security operations teams, and external users can use this skill to run object detection on surveillance images, videos, or media URLs and receive structured detection reports. It is suited to general monitoring scenarios such as communities, industrial parks, and warehouses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload images, videos, or media URLs to external cloud services for analysis.

Mitigation: Use only media that is approved for third-party processing, and avoid sensitive images, surveillance footage, or account data unless the workspace owner has reviewed the service path and policy requirements.

Risk: The skill may create or reuse an internal identity and fetch historical cloud reports with limited user control.

Mitigation: Review identity handling before deployment, restrict execution to trusted workspaces, and confirm that history retrieval behavior matches the intended user's authorization model.

Risk: The skill may store service tokens in a local SQLite database.

Mitigation: Run in an isolated workspace, protect the workspace data directory, and rotate or clear tokens after evaluation or when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [smyx_analysis API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or JSON analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured object counts, confidence information, historical report tables, risk notes, recommendations, and report links.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
