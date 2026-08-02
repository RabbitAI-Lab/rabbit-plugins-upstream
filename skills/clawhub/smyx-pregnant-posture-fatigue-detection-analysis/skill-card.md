## Description: <br>
Uses fixed home-camera image or video input to detect prolonged standing, bending, and related posture signals for a pregnant woman, then returns posture metrics, fatigue-risk reminders, and report links for health reference rather than medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and care-application integrators use this skill to analyze fixed-camera pregnancy activity footage for standing duration, bending frequency, posture status, fatigue reminders, and historical report lookup. Outputs are health-reference observations and reminders, not medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send highly sensitive pregnancy-related home camera footage or video URLs to configured cloud services. <br>
Mitigation: Use it only with explicit informed consent from the monitored person and household, and prefer privacy-preserving capture modes and careful storage controls. <br>
Risk: Automatic account linkage, token persistence, and broad history-report access can expose sensitive report history if installed without review. <br>
Mitigation: Review configuration and access expectations before deployment, and prefer narrow, explicit invocations for analysis and history queries. <br>
Risk: Visual posture and fatigue-risk observations may be incomplete or inaccurate and are not medical diagnosis. <br>
Mitigation: Present outputs as health-reference reminders only, and direct users to qualified clinical care for symptoms, discomfort, or pregnancy concerns. <br>


## Reference(s): <br>
- [Skill API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and JSON analysis results with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include posture classification, standing-duration metrics, bending-frequency metrics, alert type, reminder text, recommended action, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
