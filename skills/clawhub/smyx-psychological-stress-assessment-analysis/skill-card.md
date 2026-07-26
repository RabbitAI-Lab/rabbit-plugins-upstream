## Description: <br>
Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency for mental health monitoring scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to submit face image or video media for a psychological stress assessment report covering stress index, anxiety tendency, and depression tendency. The skill is intended for mental health monitoring and screening support, not clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face media and inferred mental-health results are sent to the publisher's remote service and may be linked to local or cloud identity state. <br>
Mitigation: Use only with clear subject consent, review the publisher's data handling terms, and confirm retention, deletion, token, and identity-linking controls before production use. <br>
Risk: Stress, anxiety, and depression tendency outputs may be mistaken for clinical conclusions. <br>
Mitigation: Present results as screening or monitoring support only and route persistent or concerning results to qualified mental-health professionals. <br>
Risk: History-report queries can expose prior psychological assessment records associated with the resolved user identity. <br>
Mitigation: Limit access to authorized users and review who can retrieve report history before enabling the skill in shared, workplace, school, or clinical settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON psychological stress assessment report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured stress, anxiety, and depression tendency results, report links, and history-report tables; documented media inputs include image or video files and remote media URLs with a 10 MB file-size limit.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact SKILL.md declares 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
