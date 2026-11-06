## Description:

在学习者明确同意后，IM智能提醒会为其他技能提供的学习事项排期、合并并发送提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

供学生或监护人按需管理复习、计划任务和探索活动提醒。用户可确认提醒类型、时间和共享范围，并查看、暂停或调整提醒。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reminders or cross-skill sharing could be enabled with unclear consent or preferences.

Mitigation: Confirm reminder type, time, frequency, and sharing preferences before creating reminders; keep pause and cancellation controls available.

Risk: Scheduling, storage, or deletion behavior may vary by platform, and the separate learning-DNA dependency was not assessed.

Mitigation: Explain platform limits and verify the separate dependency before relying on scheduling or data-control behavior.

Risk: Users may not expect generated practice questions or an additional exam-day message.

Mitigation: Set expectations when enabling reminders and make the timing and source of practice content clear.

## Reference(s):

- [间隔复习计划](artifact/references/ebbinghaus-schedule.md)
- [学段与免打扰时段](artifact/shared/grade-bands.md)
- [提醒共享与队列协议](artifact/shared/handover-protocol.schema.json)
- [提醒预算与共享约定](artifact/shared/vocab.md)
- [危机转介流程](artifact/shared/crisis-exception.md)
- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [发布者页面](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese text or Markdown, including reminder messages, merged daily summaries, and queue status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminders are created only with consent; scheduling and data controls depend on the host platform.]

## Skill Version(s):

2.12.6 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
