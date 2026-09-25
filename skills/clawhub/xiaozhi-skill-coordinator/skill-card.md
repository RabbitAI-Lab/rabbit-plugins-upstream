## Description:

为中文 K12 学习请求选择合适的学习技能、避免重复协作，并在用户请求时汇总经授权的学习月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆的学生及陪同使用的家长或老师，按学习问题分配合适的学习技能、检查学习环节，并按需生成经授权的全景月报。

### Deployment Geography for Use:

China (mainland); deployment elsewhere requires localizing curriculum, consent practices, and crisis contacts

## Known Risks and Mitigations:

Risk: Sharing a student's learning records, reminders, or reports beyond the intended audience.

Mitigation: Confirm consent for cross-skill sharing, reminders, parent or teacher visibility, and long-term records; use only the summaries needed for the task.

Risk: An incomplete monthly report could appear to reflect unavailable historical data.

Mitigation: When cross-session statistics are unavailable, summarize only information supplied in the current session and clearly state the coverage limit.

Risk: China-specific crisis contacts may be inappropriate outside mainland China.

Mitigation: Confirm the student's region and localize crisis referral contacts before use elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week learning coordination example](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Platform and regional conventions](shared/platform-conventions.md)
- [Crisis referral guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON handoffs]

**Output Format:** [Chinese-language text or Markdown reports; structured JSON for authorized handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly reports are on request; cross-skill summaries and reminder handoffs require applicable consent.]

## Skill Version(s):

2.4.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
