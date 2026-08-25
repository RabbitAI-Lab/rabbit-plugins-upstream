## Description:

Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness. Suitable for security surveillance and camera self-check scenarios. | 图像质量检测分析工具，检测摄像头画面出现的全黑、全白、偏色、条纹、雪花、模糊等质量问题，适用于安防监控、摄像头自检等场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and camera operations teams use this skill to analyze camera images, video frames, or URLs for quality issues such as black or white screens, color cast, stripes, noise, and blur. It can also return linked historical image-quality reports for account-associated review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images or videos may be sent to a configured cloud service for analysis.

Mitigation: Use the skill only with media approved for that service, and review the configured endpoints before running analysis.

Risk: The skill automatically creates or reuses an identity and can query account-linked report history.

Mitigation: Confirm the identity and history-access behavior is acceptable for the deployment, and restrict use to accounts authorized to view those reports.

Risk: Returned tokens may be persisted locally and the skill may read data/smyx-api-key.txt when present.

Mitigation: Protect local workspace data, rotate credentials when needed, and avoid installing the skill in shared workspaces without appropriate access controls.

Risk: The included configuration selects a dev environment.

Mitigation: Review and update endpoint configuration before commercial use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Image Quality API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports with status text, detected quality issues, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write result content to a user-specified output file; history queries produce Markdown tables from cloud results.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
