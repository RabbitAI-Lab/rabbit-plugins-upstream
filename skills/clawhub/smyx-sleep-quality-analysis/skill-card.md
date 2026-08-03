## Description: <br>
Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios. | 睡眠质量分析技能，识别入睡、浅睡、深睡、快速眼动阶段，监测体动、夜间觉醒、睡眠呼吸暂停，适用于睡眠监测场景 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to submit sleep-monitoring video files or public video URLs for cloud-based sleep quality analysis, including sleep-stage recognition, movement counts, awakenings, apnea indicators, structured reports, and report history queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sleep-monitoring videos or video URLs to the LifeEmergence cloud service. <br>
Mitigation: Use it only when the service's privacy, retention, and deletion practices are acceptable for the footage being analyzed, and avoid sensitive bedroom recordings unless those practices have been reviewed. <br>
Risk: The skill may store internal account identity, authentication tokens, and report history data locally in the workspace. <br>
Mitigation: Run it in a controlled workspace, avoid sharing that workspace, and clear local data after use when account or report history should not persist. <br>
Risk: The generated sleep report is health-related guidance and is not a substitute for clinical diagnosis. <br>
Mitigation: Treat outputs as sleep-quality reference information and route concerning apnea or sleep-health findings to qualified medical professionals. <br>


## Reference(s): <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, API Calls] <br>
**Output Format:** [Markdown and JSON structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sleep-stage metrics, movement and awakening counts, apnea indicators, recommendations, report links, and cloud report-history records.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
