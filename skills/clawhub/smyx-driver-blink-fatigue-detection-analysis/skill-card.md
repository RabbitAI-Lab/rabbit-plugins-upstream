## Description: <br>
Analyzes in-cabin driver face video to estimate blink rate, eye-closure duration, microsleep indicators, and fatigue-warning outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to submit driver-monitoring video or URLs for remote fatigue analysis and to retrieve structured fatigue reports. It is intended for driver-assistance workflows in vehicles, fleets, ride-hailing, and related safety-monitoring contexts, not for medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver videos may contain biometric and workplace privacy-sensitive information and are sent to remote LifeEmergence services for analysis. <br>
Mitigation: Use only with informed driver consent, approved cloud-processing terms, and data-handling controls appropriate for driver video. <br>
Risk: The skill can create or reuse an identity automatically and stores authentication tokens in a local workspace database. <br>
Mitigation: Install only in workspaces where local token storage is acceptable; restrict filesystem access and rotate or remove stored credentials when decommissioning the skill. <br>
Risk: Broad natural-language triggers can retrieve cloud report history associated with the resolved identity. <br>
Mitigation: Limit use to authorized operators and review report-history access before deployment in shared or multi-user workspaces. <br>
Risk: Fatigue warnings depend on video quality and visibility of the driver's eyes and are not medical or sleep-disorder diagnoses. <br>
Mitigation: Treat results as driver-assistance signals; require clear DMS video, avoid obstructed or glare-heavy inputs, and keep human safety judgment in the loop. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis) <br>
- [Driver fatigue API reference](references/api_doc.md) <br>
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown text with structured JSON-style fatigue metrics, warnings, recommendations, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return a current analysis result or a cloud report-history listing; results depend on remote service availability and input video quality.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
