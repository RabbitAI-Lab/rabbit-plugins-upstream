## Description: <br>
Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability. No wearable devices are required; monitoring is achieved solely through camera footage. | 无感生命体征监测分析技能，非接触检测心率、呼吸、血氧、心率变异性，无需穿戴设备，通过摄像头画面即可监测 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and health-support workflows can use this skill to analyze camera video for non-contact heart rate, respiration, blood oxygen, and heart-rate-variability reporting. Results should be treated as health reference information, not as a replacement for professional medical measurement or diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends face or video footage, derived vital-sign information, URLs, and internally generated identity data to a third-party cloud service. <br>
Mitigation: Use it only with informed consent and after reviewing the service's privacy, retention, account, and deletion practices. <br>
Risk: The security verdict is suspicious because the skill performs sensitive health-data processing with silent identity creation, token persistence, and cloud history access. <br>
Mitigation: Review the security summary and guidance before installation, restrict use with sensitive data, and avoid relying on outputs for medical decisions. <br>
Risk: Vital-sign estimates from camera footage may be unsuitable for diagnosis or emergency decisions. <br>
Mitigation: Treat outputs as health reference information and direct users to professional medical measurement or care for abnormal or urgent results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata; SKILL.md frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
