## Description:

引导学生读懂地理地图与图表，并分析地理错题的具体错因。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆初高中地理学习者，帮助学生依据图名、图例、方向、比例尺和关键数值解读地图与图表，并定位错题原因。

### Deployment Geography for Use:

Mainland China; localize curriculum, minor-consent rules, and crisis referrals before use elsewhere.

## Known Risks and Mitigations:

Risk: Student learning records may be exposed through optional memory, cross-skill sharing, parent summaries, or reminders.

Mitigation: Keep records off by default, request specific consent before each handoff, and honor pause, deletion, and sharing controls.

Risk: Mainland China emergency contacts, grade bands, and minor-consent rules may not apply in other regions.

Mitigation: Confirm the student's location and localize crisis referrals, curriculum, consent requirements, and labels before deployment elsewhere.

Risk: Unclear maps or unsupported visual input can lead to misleading geography guidance.

Mitigation: Ask for the title, legend, scale, direction, and key values when the image cannot be read; do not guess missing details.

## Reference(s):

- [地理读图指南](references/map-reading-guide.md)
- [地理错因维度表](references/geography-error-dimension-table.md)
- [平台与地域适配约定](shared/platform-conventions.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown, Structured handoff data]

**Output Format:** [Chinese-language conversational text or Markdown; optional consent-gated structured handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses progressive hints and evidence from the supplied map; optional learning-record sharing and reminders require consent.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
