## Description:

Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness. Suitable for security surveillance and camera self-check scenarios. | 图像质量检测分析工具，检测摄像头画面出现的全黑、全白、偏色、条纹、雪花、模糊等质量问题，适用于安防监控、摄像头自检等场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to analyze camera images, video frames, or media URLs for visible quality problems such as black screens, white screens, color cast, stripes, snow noise, and blur. It supports security monitoring self-checks and camera maintenance review, with results intended as maintenance guidance rather than a substitute for professional hardware inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, media URLs, identity metadata, and report queries may be sent to the configured cloud service.

Mitigation: Use the skill only with media that is approved for that service, review configured endpoints before installation, and avoid sensitive camera footage unless the deployment has the required approvals.

Risk: Identity handling and local token storage may expose user or report access metadata if the workspace is shared or poorly protected.

Mitigation: Protect workspace data, review token storage behavior before deployment, and require explicit user confirmation before history report lookups.

Risk: Broad authenticated network helpers and debug logging can increase exposure if endpoints or logs are not controlled.

Mitigation: Disable debug logging, restrict allowed service URLs, and review authenticated request behavior before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured JSON or Markdown text with analysis results, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-generated report export links and history-list results from the configured service.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
