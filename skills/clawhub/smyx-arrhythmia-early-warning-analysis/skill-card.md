## Description:

Based on facial video, identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia/bradycardia, assists in early detection of heart health risks. | 心律失常早期预警技能，基于面部视频识别早搏、房颤、心动过速/心动过缓等异常节律，辅助心脏健康风险早发现

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and health-oriented agents use this skill to submit facial video for non-contact arrhythmia early warning analysis, including premature beat, atrial fibrillation, tachycardia, bradycardia, and overall risk screening. Agents can also retrieve cloud-stored historical reports when the user asks for prior arrhythmia warning results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video and heart-risk analysis data are sent to the publisher's cloud service.

Mitigation: Use the skill only with data the user intends to share with the publisher's service, and avoid submitting sensitive video when that data transfer is not acceptable.

Risk: The skill can create or reuse a local identity and store identity or token data for report history.

Mitigation: Review and clear the workspace data directory when persisted identities or tokens should not remain available after use.

Risk: Historical report commands query cloud-stored health reports.

Mitigation: Run historical report retrieval only when the user explicitly intends to access cloud-stored health reports for the current identity.

Risk: The analysis is an early warning aid and does not replace clinical diagnosis.

Mitigation: Treat high-risk or concerning results as screening signals and direct users to professional ECG testing or cardiology evaluation.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON analysis text with report links and historical report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured arrhythmia risk findings, recommendations, cloud report links, and saved result files when requested.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
