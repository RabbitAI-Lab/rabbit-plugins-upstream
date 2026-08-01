## Description: <br>
Analyzes in-cabin driver face video or image input to identify facial flushing and sweat or glare indicators, then returns visual health-risk reminders, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Fleet operators, vehicle safety teams, and developers use this skill to submit driver face video or image evidence to a cloud analysis service and receive visual-only alerts about facial flushing or abnormal sweating. It is intended as an assistive driver health reminder, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver face video or video URLs may be sent to configured Life Emergence cloud services and linked to a persistent local identity. <br>
Mitigation: Use only with explicit driver notice and consent, documented retention rules, restricted workspace access, and a process to revoke tokens and delete historical reports. <br>
Risk: The skill automatically creates or reuses a local identity and can store backend tokens for cloud history access. <br>
Mitigation: Deploy in a governed environment, rotate or revoke tokens when access changes, and clear local identity and token storage when decommissioning the skill. <br>
Risk: Visual flushing and sweating alerts may be mistaken for clinical conclusions. <br>
Mitigation: Present results only as visual health reminders, avoid medical diagnosis claims, and direct users to professional medical evaluation when symptoms or safety concerns exist. <br>
Risk: Lighting, tinted glass, skin-tone variation, masks, and infrared-only camera feeds can reduce reliability. <br>
Mitigation: Use color RGB DMS input with stable lighting, maintain baseline and duration checks, and review alerts before operational or employment decisions. <br>


## Reference(s): <br>
- [Driver flushing and sweat detection API documentation](references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report text with JSON-style structured analysis, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a caller-specified output file; history queries return structured cloud report records.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
