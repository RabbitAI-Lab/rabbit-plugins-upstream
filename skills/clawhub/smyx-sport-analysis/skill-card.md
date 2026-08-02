## Description: <br>
Analyzes outdoor sports event videos to identify participant injury, physical discomfort, posture, and environmental safety risks and returns structured safety reports with warnings and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Event operators, safety teams, and agent users use this skill to analyze uploaded or URL-based outdoor sports videos for potential injuries, physical distress, unsafe posture, environmental hazards, and historical report lookup. The output supports triage and safety review, but it is not a substitute for medical diagnosis or emergency response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send uploaded videos, video URLs, and user identifiers to lifeemergence.com cloud services. <br>
Mitigation: Use only with videos and URLs approved for third-party cloud processing, especially when footage may include people, health information, private locations, or restricted resources. <br>
Risk: The skill creates or reuses local identity records and stores tokens in a workspace data directory. <br>
Mitigation: Avoid shared workspaces unless account linkage and local token storage are acceptable; clear local skill data when rotating users or credentials. <br>
Risk: The analysis may be used for health or safety decisions but is not a medical diagnosis. <br>
Mitigation: Treat results as safety review support and require qualified human review and emergency procedures for suspected injury or health distress. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Analysis API Error Reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted structured analysis reports, with optional report links and saved text output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; accepts local video files or video URLs; supported local formats are mp4, avi, and mov with a documented 10 MB limit.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
