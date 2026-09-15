## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts, suitable for home pet monitoring scenarios. | 宠物禁区预警技能，监测禁止区域闯入、攀爬餐桌、翻垃圾桶行为并实时报警，适用于家庭宠物监控场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet owners use this skill to analyze home monitoring videos for restricted-zone intrusions, table climbing, or trash rummaging and to retrieve prior warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet-monitoring footage and report history may be sent to a remote service.

Mitigation: Use the skill only with footage approved for remote processing, and review the service's retention and identity-handling practices before deployment.

Risk: The security summary flags unsafe default network and storage settings.

Mitigation: Configure HTTPS production endpoints and store any tokens or identity material in a protected secret store before broad use.

Risk: Analysis alerts are an aid for home monitoring and may not replace direct confirmation.

Mitigation: Confirm the physical scene after an alert before taking action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Structured analysis report or history table, with JSON output available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; supports mp4, avi, and mov inputs up to 10MB; default alert threshold is 0.6.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
