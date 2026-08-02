## Description: <br>
Recognizes standing, sitting, lying, bending, raised-hand, running, falling, and other abnormal human postures in video inputs and returns structured reports for security monitoring and elder-care scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to submit monitoring video files or public video URLs for pose recognition, fall detection, abnormal-posture alerts, structured reporting, and history-report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive video files or video URLs may be sent to the LifeEmergence/Open API service for analysis. <br>
Mitigation: Use only on authorized footage, and avoid private home, elder-care, workplace, or camera-feed media unless remote processing is acceptable. <br>
Risk: Identity-linked report history and service tokens may be queried from cloud services and stored in the local workspace database. <br>
Mitigation: Run the skill in a controlled workspace, review local data storage, and remove generated identities, tokens, or report records when they are no longer needed. <br>
Risk: Posture and fall-warning results may be incomplete or incorrect for safety-critical situations. <br>
Mitigation: Treat results as safety-monitoring support and verify urgent events through human review or operational response procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown text or JSON with optional local output file and report export link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local video inputs are documented as mp4, avi, or mov files up to 10 MB; URL inputs are processed by the remote API service.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
