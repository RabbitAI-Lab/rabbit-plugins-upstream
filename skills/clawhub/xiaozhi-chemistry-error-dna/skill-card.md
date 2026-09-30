## Description:

帮助初中至高中必修起点的学生分析化学错题根因，识别六类薄弱环节并生成经授权的学习档案与弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking secondary-school students use the skill to pinpoint recurring chemistry misconceptions, practice specific weak areas, and review their error patterns. With consent, it can maintain a chemistry learning profile and prepare reports or reminders.

### Deployment Geography for Use:

China mainland by default; localize curriculum, minor-consent settings, and crisis resources for use elsewhere.

## Known Risks and Mitigations:

Risk: A minor's chemistry error profile or report could be retained or shared without their intended consent.

Mitigation: Check profile, cross-skill, reminder, and parent-sharing permissions before recording or sharing; honor pause, correction, export, and deletion requests.

Risk: Sparse history could be presented as a reliable diagnosis of a student's abilities.

Mitigation: Label limited evidence as insufficient, avoid invented counts, and verify weak areas through independent practice before changing profile status.

Risk: Crisis guidance or minor-consent defaults may not suit users outside China mainland.

Mitigation: Confirm the student's location before providing local emergency contacts and adapt curriculum and consent settings before deploying elsewhere.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)
- [Chemistry error dimension table](references/chemistry-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Skill handover schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Chinese-language explanations, weakness reports, practice prompts, and consent-gated structured profile updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical statistics require existing records; profile sharing, reminders, and parent summaries require appropriate consent.]

## Skill Version(s):

2.8.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
