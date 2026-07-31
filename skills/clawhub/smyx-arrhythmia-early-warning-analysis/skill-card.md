## Description: <br>
Based on facial video, identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia/bradycardia, assists in early detection of heart health risks. | 心律失常早期预警技能，基于面部视频识别早搏、房颤、心动过速/心动过缓等异常节律，辅助心脏健康风险早发现 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and health application agents use this skill to screen facial video for early warning signs of arrhythmia risk and to retrieve prior cloud-generated screening reports. The output is screening guidance only and is not a substitute for professional ECG testing or diagnosis by a cardiology clinician. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facial videos, URLs, and inferred heart-risk results may be sent to the Life Emergence cloud service. <br>
Mitigation: Use the skill only when users understand that sensitive facial and health-related data is processed by the external service. <br>
Risk: The skill silently creates or reuses a local identity and stores authentication tokens in the workspace. <br>
Mitigation: Review workspace token storage and identity handling before deployment, and restrict access to environments where the skill runs. <br>
Risk: Arrhythmia output can be mistaken for a medical diagnosis. <br>
Mitigation: Present results as early warning screening information and direct high-risk users to professional ECG testing and cardiology evaluation. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Structured analysis report, JSON detail output, or Markdown table for historical report lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk or recognition results, recommendations, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
