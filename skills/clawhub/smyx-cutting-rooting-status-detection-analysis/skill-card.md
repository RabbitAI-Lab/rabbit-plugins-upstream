## Description: <br>
AI-powered analysis of transparent-container cutting images or videos to detect visible root primordia, estimate rooting stage, and support transplant-timing decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, propagation operators, and plant research teams use this skill to analyze transparent-container cutting images or videos, estimate rooting stage, count and locate root primordia, and decide when to keep observing or transplant. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, or URLs may be uploaded to an external cloud service during analysis. <br>
Mitigation: Use non-sensitive plant media unless the publisher clarifies endpoint ownership, retention, and cleanup. <br>
Risk: The skill may create or reuse local identity records with limited user-facing disclosure. <br>
Mitigation: Review identity handling before installation and ensure the local profile behavior is acceptable for the workspace. <br>
Risk: Remote service tokens may be stored in a local SQLite database. <br>
Mitigation: Restrict workspace access, review token storage behavior, and remove local credentials when decommissioning the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report text or JSON detail output, with optional saved result files and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs and can list cloud-hosted historical reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
