## Description: <br>
Using a fixed home camera to capture frontal facial images or short videos of the elderly, the system uses AI facial-landmark detection to analyze features such as the height difference between left/right mouth corners, the symmetry of nasolabial folds (smile lines), and the asymmetry of eyebrow lifts, and computes a facial asymmetry index (0-100%). | 通过家庭固定摄像头拍摄老年人正面面部图像或视频，利用AI面部关键点检测技术分析左右嘴角的高度差、鼻唇沟（法令纹）的对称性、眉毛抬高的差异等特征，计算面部不对称指数（0-100%）。该技能可作为脑卒中（中风）前兆的辅助筛查工具，提示家属或护理人员关注老年人是否存在面瘫、口角歪斜等神经系统异常，及时就医。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, elder-care operators, and developers use this skill to analyze frontal elder face images or short videos for facial-asymmetry indicators, mouth-corner deviation, risk level, and report links. The output is an auxiliary screening aid and does not replace professional medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive face images, videos, health-related report metadata, and cloud history access. <br>
Mitigation: Use only with informed consent from the elderly person or an authorized caregiver, and review data handling before use in care settings. <br>
Risk: Cloud analysis and history lookup may send face images, videos, and report metadata to LifeEmergence services. <br>
Mitigation: Confirm the service endpoint, retention expectations, and privacy controls before processing real elder-care data. <br>
Risk: The skill can create or reuse a local identity and persist service tokens in workspace data. <br>
Mitigation: Limit access to the workspace, protect persisted tokens, and clear local identity or token data when no longer needed. <br>
Risk: Facial-asymmetry output is an auxiliary screening signal and could be mistaken for a diagnosis. <br>
Mitigation: Present results as geometry-based risk indicators and direct users to professional medical evaluation for suspected stroke or facial paralysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with risk indicators and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save results to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
