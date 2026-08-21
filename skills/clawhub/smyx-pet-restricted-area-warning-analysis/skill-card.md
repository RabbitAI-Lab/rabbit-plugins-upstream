## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts, suitable for home pet monitoring scenarios. | 宠物禁区预警技能，监测禁止区域闯入、攀爬餐桌、翻垃圾桶行为并实时报警，适用于家庭宠物监控场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze pet monitoring videos or video URLs for restricted-area entry, table climbing, and trash rummaging. It returns structured warning reports and can retrieve cloud-hosted historical warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-monitoring footage or video URLs may be sent to the publisher's cloud service.

Mitigation: Use only media appropriate for third-party cloud processing and confirm publisher data handling and retention expectations before installation.

Risk: The skill may create or reuse an internal account, query cloud report history, and store authentication tokens in a local shared database.

Mitigation: Run the skill in an environment where shared local token storage and cloud report access are acceptable, and review stored credentials during deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured text reports, Markdown tables for history lists, and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, warning summaries, detection counts, confidence values, and saved output files when requested.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
