## Description: <br>
Analyzes child nighttime sleep video or audio from a fixed bedroom camera to report rollover frequency, crying, sleep talk, sleep quality, and possible nightmare or restless-sleep alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers and developers use this skill to submit child nighttime sleep media or URLs for cloud analysis, receive behavior statistics and sleep-quality reports, and retrieve previous reports. The output is an assistive sleep-behavior report, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child bedroom audio/video or URLs may be processed by vendor cloud APIs. <br>
Mitigation: Use only with clear guardian consent and submit media only when the vendor's retention, deletion, and encryption practices are acceptable. <br>
Risk: Analysis history may be tied to local or remote identity state, and account tokens may be stored in a workspace SQLite database. <br>
Mitigation: Avoid shared workspaces unless account separation, retention, deletion, and token-storage practices have been reviewed. <br>
Risk: The security verdict is suspicious because the skill handles highly sensitive child sleep media and identity-linked reports. <br>
Mitigation: Review carefully before installing and require organizational security review before production or shared-environment use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON analysis output from command-line execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured sleep-analysis fields, report links, and historical report tables returned by cloud APIs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
