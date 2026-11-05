## Description:

陪初中和高中学生按图名、图例、比例尺、方向与关键数值读懂地图和地理图表，并分析地理错题的错因。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初中和高中地理学习者可用本技能理解当前题目中的地图和地理图表，并定位地理错题的主要错因。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When shared record updates are enabled, the bundled schema alone does not ensure the receiving notebook accepts only geography updates tied to the original question.

Mitigation: Keep the default session-only mode; before enabling sharing, confirm the receiving notebook independently checks geography relevance and the original question.

## Reference(s):

- [Map reading guide](artifact/references/map-reading-guide.md)
- [Geography error dimension table](artifact/references/geography-error-dimension-table.md)
- [High school required geography maps](artifact/references/map-reading-hs-required.md)
- [High school elective geography maps](artifact/references/map-reading-hs-elective.md)
- [地理读图教练 on ClawHub](https://clawhub.ai/qizhitang/skills/xiaozhi-geography-map-reader)

## Skill Output:

**Output Type(s):** [Text, Guidance, Analysis]

**Output Format:** [Conversational text, with structured steps or tables when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts explanations to the learner's grade band; asks for a textual description when the map cannot be inspected and does not guess its contents.]

## Skill Version(s):

2.12.5 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
