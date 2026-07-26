## Description: <br>
Analyzes driver face video from an in-cabin DMS camera to detect eye state, blink rate, prolonged eye closure, microsleep indicators, and fatigue warning signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, fleet operators, and safety engineers use this skill to analyze driver-facing video or image inputs for blink-rate, eye-closure, PERCLOS, and fatigue-warning indicators. It can also return cloud-hosted history and report links for prior fatigue analysis jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver face video and identity-linked report history may be sent to the LifeEmergence cloud service. <br>
Mitigation: Use the skill only with documented driver or employee consent, approved data-processing terms, and a retention policy for local files and cloud reports. <br>
Risk: The skill silently manages user identity and tokens while supporting historical report lookup. <br>
Mitigation: Run it in a controlled workspace or service account, restrict history access to authorized users, and review where tokens and reports are stored before deployment. <br>
Risk: Fatigue warnings can be unreliable when driver eyes are obscured, lighting is poor, frame rate is low, or video quality is insufficient. <br>
Mitigation: Treat outputs as auxiliary safety indicators, confirm camera quality before use, and require human driving judgment and safe-rest procedures after alerts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis) <br>
- [Driver fatigue detection API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report history, exported report URLs, fatigue-level indicators, warning types, and recommended driver-safety actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
