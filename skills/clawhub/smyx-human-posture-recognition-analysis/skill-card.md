## Description: <br>
Recognizes standing, sitting, lying down, bending, raised hands, running, falling, and other human poses, with abnormal posture recognition and fall-warning support for monitoring and elder-care scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and care-monitoring teams can use this skill to analyze video files or video URLs for human posture recognition, fall detection, abnormal posture alerts, and structured report retrieval. It is intended for security monitoring and elder-care workflows where reviewers still need to confirm urgent situations directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may upload sensitive video or video URLs to the publisher's cloud service for analysis. <br>
Mitigation: Use only with footage approved for that external cloud processing, and avoid private home, workplace, health, elder-care, or security footage unless the data handling is acceptable. <br>
Risk: The skill can create or reuse a local identity and associate report history with that identity. <br>
Mitigation: Review identity and report-history behavior before deployment, and run in an environment where persistent account linkage is expected. <br>
Risk: The skill can persist service tokens locally. <br>
Mitigation: Limit installation to trusted runtimes, protect local skill storage, and rotate or remove tokens if the environment is shared or decommissioned. <br>
Risk: Fall detection and abnormal posture outputs may be incomplete or inaccurate. <br>
Mitigation: Treat results as monitoring support only and require human confirmation and emergency procedures for urgent care or safety decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API interface documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, files, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text with optional saved report files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; history queries return cloud report records.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
