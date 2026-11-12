## Description:

Analyzes videos of vehicle drivers to identify unsafe driving behaviors. It generates professional analysis reports to help enhance road safety awareness. | 安全驾驶行为分析工具，针对机动车驾驶人员的驾驶行为进行视频分析，识别不安全驾驶行为，输出专业分析报告，提升道路交通安全意识

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers and road safety teams use this skill to review driving footage for fatigue, distraction, seat belt use, posture, and other unsafe behaviors, then receive a structured assessment with safety suggestions. They can also request a list of previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage may be processed externally, and the export-only behavior and consent expectations are unclear.

Mitigation: Clarify where footage is processed and whether it leaves the local environment; obtain appropriate consent and authorization before submitting footage.

Risk: The skill creates or reuses user identities and handles credentials, with account and storage practices not sufficiently clear.

Mitigation: Clarify account creation, identity association, and credential storage before use; avoid submitting sensitive credentials until these practices are understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured driving behavior assessment with findings and safety suggestions; Markdown tables for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link; prior report lists are retrieved from the service.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
