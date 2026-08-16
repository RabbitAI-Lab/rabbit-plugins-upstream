## Description:

Supports identifying high-risk behaviors and health risks through video/images, including elderly falls, precursors to heart attacks and strokes, and abnormal behaviors, issuing timely warning alerts. | 高风险行为识别分析工具，支持通过视频/图片识别高危行为和健康风险，包括老人跌倒、心梗脑梗前兆、异常行为等，及时发出预警提示

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit image, video, URL, or stream inputs for high-risk behavior and health-risk analysis, including fall detection, abnormal behavior detection, health-risk assessment, alert-oriented summaries, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive image or video content, health-risk inferences, history queries, and identity-linked account data may be sent to configured external services.

Mitigation: Use only with appropriate consent and authorization, confirm the intended production endpoints before deployment, and avoid submitting sensitive or third-party footage unless policy permits it.

Risk: The skill silently creates or reuses local user identity records and stores tokens for service access.

Mitigation: Review the workspace data directory and local identity/token records before and after use, and clear persisted data when the deployment does not require reuse.

Risk: Health and safety detections may be incomplete or incorrect and are not a substitute for professional medical, emergency, or security review.

Mitigation: Treat outputs as decision-support signals, require human review for high-impact actions, and document escalation procedures for emergency or safety-sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Risk category and alert-level reference](references/risk_categories.md)
- [API interface reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk categories, confidence levels, suggestions, historical report records, and report export URLs.]

## Skill Version(s):

999.999.1003 (source: server release metadata; artifact frontmatter version 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
