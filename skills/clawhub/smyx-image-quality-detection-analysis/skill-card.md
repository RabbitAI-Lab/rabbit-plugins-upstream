## Description:

Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness. Suitable for security surveillance and camera self-check scenarios. | 图像质量检测分析工具，检测摄像头画面出现的全黑、全白、偏色、条纹、雪花、模糊等质量问题，适用于安防监控、摄像头自检等场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to analyze camera images, video frames, or URLs for image-quality defects such as black screens, white screens, color cast, stripes, noise, and blur. It returns structured results, maintenance-oriented guidance, and report links for camera self-check and security monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images or videos may be sent to a remote service for analysis.

Mitigation: Use the skill only with media that is approved for remote processing, and review data-handling requirements before installation.

Risk: URL inputs may be passed to a backend service for fetching.

Mitigation: Submit only trusted URLs and confirm the remote fetching behavior is acceptable for the deployment environment.

Risk: The skill can create or reuse an internal identity and store tokens in a local SQLite database.

Mitigation: Review local credential storage, filesystem permissions, and account lifecycle behavior before use.

Risk: The published artifact appears configured with private development HTTP endpoints.

Mitigation: Correct or explicitly approve endpoint configuration before normal use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis results, including detected issues, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file input, URL input, optional result-file output, and historical report listing.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
