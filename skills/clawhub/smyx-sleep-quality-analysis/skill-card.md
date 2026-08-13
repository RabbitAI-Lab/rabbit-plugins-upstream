## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios. | 睡眠质量分析技能，识别入睡、浅睡、深睡、快速眼动阶段，监测体动、夜间觉醒、睡眠呼吸暂停，适用于睡眠监测场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze sleep-monitoring video files or URLs for sleep stage, body movement, nighttime awakening, and sleep apnea indicators, and to retrieve cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep-monitoring videos, URLs, and report queries may be sent to the Life Emergence cloud service.

Mitigation: Use only with recordings and report queries that the user is comfortable processing through that cloud service.

Risk: The skill can silently create or reuse identities and stores tokens locally.

Mitigation: Avoid shared workspaces unless identity separation is clear, and review how local tokens and database entries are deleted before use.

Risk: Historical report queries can expose sensitive sleep or medical-adjacent history.

Mitigation: Confirm the intended account context before querying historical reports, especially for private bedroom or medical-adjacent recordings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown reports or JSON sleep-analysis results, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes mp4, avi, or mov inputs up to 10 MB; historical reports are queried from the cloud service.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
