## Description: <br>
Analyzes in-cabin DMS driver face video for facial flushing and sweat/reflection indicators, then returns visual health-risk reminders and suggested rest or escalation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, fleet operators, and developers use this skill to analyze driver face video from DMS cameras for visual indicators of facial flushing or abnormal sweating. The output is an assistive health-risk reminder and structured report, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver face video or video URLs are sent to the configured lifeemergence.com cloud service for analysis. <br>
Mitigation: Use only with informed driver or employee consent, appropriate privacy controls, and policies for retention, access, and encryption of video and reports. <br>
Risk: The skill can create or reuse a persistent local identity and stores service tokens for cloud requests. <br>
Mitigation: Run it in an isolated workspace, restrict access to local skill data, and review or remove stored identity and token data when deprovisioning. <br>
Risk: The security scan verdict is suspicious because sensitive biometric-style analysis is linked to persistent identities and service tokens. <br>
Mitigation: Review the skill and cloud-service trust boundary before deployment, and install it only when the data-sharing model is acceptable. <br>
Risk: Visual flushing and sweating indicators may be affected by lighting, tinted windows, skin-tone variation, occlusion, masks, or infrared-only video. <br>
Mitigation: Treat results as assistive visual alerts, combine them with baseline and duration checks, and avoid using the skill as a sole medical or safety decision system. <br>


## Reference(s): <br>
- [Driver Flushing/Sweat Detection API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown-wrapped structured JSON with report links; optionally saved to a text output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and historical report lists.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
