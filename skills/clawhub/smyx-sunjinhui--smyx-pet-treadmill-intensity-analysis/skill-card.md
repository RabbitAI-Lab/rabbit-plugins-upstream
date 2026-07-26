## Description: <br>
Analyzes pet treadmill videos, optionally with heart-rate band data, to estimate exercise intensity and produce structured pacing suggestions for dog or cat fitness, weight-loss, and rehabilitation contexts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, trainers, rehabilitation operators, and developers use this skill to analyze pet treadmill videos or video URLs, receive low/medium/high exercise intensity assessments, view motion and heart-rate indicators, and query prior reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet treadmill videos or video URLs are sent to the provider's cloud service, and report history is associated with an automatically managed identity. <br>
Mitigation: Use only footage appropriate for cloud processing, avoid sensitive household video, and review the provider's handling of stored report history before deployment. <br>
Risk: Local token or user state may persist under the workspace data directory. <br>
Mitigation: Run in a controlled workspace, rotate or remove local state between users when needed, and review stored credentials before sharing the environment. <br>
Risk: Exercise intensity output is not a veterinary diagnosis or treatment plan. <br>
Mitigation: Present results as training guidance only and require human or veterinary review for health, injury, or rehabilitation decisions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-treadmill-intensity-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and JSON-like structured analysis text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and history tables from the provider cloud service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
