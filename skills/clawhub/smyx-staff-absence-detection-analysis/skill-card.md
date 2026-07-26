## Description: <br>
Real-time monitoring of personnel on-duty status in specific areas based on computer vision and human pose estimation, automatically detects abnormal statuses such as leaving posts and absent from work, supports custom threshold settings, and triggers early warning immediately when abnormality is detected. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, safety, and facilities teams use this skill to analyze workplace images or video for staff absence, post-leaving, and on-duty status signals in monitored areas such as factory stations, security rooms, and service windows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends workplace surveillance images or videos and report history to a configured cloud service. <br>
Mitigation: Use only with approved workplace monitoring data, confirm organizational authorization for cloud processing, and review retention and deletion practices before deployment. <br>
Risk: The skill can silently create or reuse an account-linked identity with persisted tokens. <br>
Mitigation: Review how default identities and stored tokens are managed, restrict who can query historical reports, and rotate or remove credentials when access changes. <br>
Risk: Security evidence marks the release suspicious because of sensitive media transfer and account-linked report access. <br>
Mitigation: Perform a deployment security review and install only when those data-sharing and access-control behaviors are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis) <br>
- [Personnel absence monitoring API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports, JSON analysis responses, report links, and command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include status classifications, absence counts, accumulated absence duration, threshold settings, report history tables, and links to cloud-hosted reports.] <br>

## Skill Version(s): <br>
1.0.9 (source: ClawHub release evidence; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
