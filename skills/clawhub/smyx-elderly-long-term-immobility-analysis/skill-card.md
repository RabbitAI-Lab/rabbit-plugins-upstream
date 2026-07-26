## Description: <br>
Analyzes fixed-camera home video or video URLs for solo-living elder monitoring, detects prolonged lack of visible activity, and returns structured long-term immobility alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, community elder-care teams, and developers use this skill to submit home-monitoring video for long-term no-activity analysis and to retrieve structured alert reports. It is intended as an auxiliary monitoring workflow and does not provide medical diagnosis or rescue instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Home-monitoring video or video URLs are sent to a remote Life Emergence service for processing. <br>
Mitigation: Use only with informed consent from the monitored person or authorized family, avoid visual coverage of highly sensitive areas when possible, and submit only approved video sources. <br>
Risk: The skill may silently create or reuse a local identity, log in to a remote account, and store tokens in a local SQLite database under the workspace data directory. <br>
Mitigation: Review account-linkage behavior before installation, protect the workspace data directory, and clear stored tokens or local user records when the skill is no longer needed. <br>
Risk: The security verdict is suspicious because the skill handles sensitive home video while performing remote account and token management. <br>
Mitigation: Review and scan the skill before deployment, restrict execution to trusted environments, and confirm the remote service relationship is acceptable for the organization. <br>
Risk: Long-term immobility alerts are auxiliary visual activity signals, not medical diagnoses or emergency response instructions. <br>
Mitigation: Manually verify any alert by phone or an in-person check and do not rely on the skill as the sole emergency response mechanism. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-long-term-immobility-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API error reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON text containing structured activity analysis, alert status, history records, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
