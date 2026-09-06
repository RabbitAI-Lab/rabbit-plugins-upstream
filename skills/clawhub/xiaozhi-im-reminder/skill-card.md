## Description:

IM智能提醒 coordinates consent-based learning reminders by accepting queued review, error-practice, plan, and exploration tasks from other skills, merging due items into a daily summary, and sending reminders only when the student explicitly asks for reminder actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and education-agent operators use this skill to schedule, merge, pause, inspect, and cancel learning reminders for spaced review, error review, study plans, exploration tasks, and daily confirmations. It is intended for Chinese K12 learning workflows where reminders must respect consent, quiet hours, and daily notification limits.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: Reminder intake may process cross-skill learning data without the intended consent boundary if production rules rely on reminder consent alone.

Mitigation: Require both reminder consent and cross-skill sharing consent before accepting reminder_enqueue payloads, and discard or refuse intake when either consent signal is missing or false.

Risk: Reminder content received from another skill may contain untrusted or inappropriate text that would later be sent to the learner.

Mitigation: Validate reminder text as untrusted content before scheduling or sending, and keep generated practice items subject to the artifact's AI item self-check protocol.

Risk: Learning reminders can become intrusive for minors if they ignore quiet hours, daily budgets, or non-response behavior.

Mitigation: Enforce grade-band quiet hours, the daily limit of one merged summary plus at most one immediate reminder, and automatic pause after three unanswered reminders of the same type.

Risk: A learner may disclose self-harm, abuse, bullying, or other safety-critical signals during reminder interactions.

Mitigation: Stop the normal reminder flow and follow the bundled crisis referral protocol: respond without judgment, state AI limits, point to trusted adults and local emergency channels, and avoid recording sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [间隔复习序列参数与提醒间隔计算](references/ebbinghaus-schedule.md)
- [全库统一词表](shared/vocab.md)
- [学段参数表](shared/grade-bands.md)
- [Xiaozhi multi-agent handover protocol schema](shared/handover-protocol.schema.json)
- [Reminder enqueue example](shared/reminder-enqueue.example.json)
- [Platform conventions and degradation paths](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese reminder messages, daily queue summaries, consent-control responses, and JSON-compatible handover guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained by explicit reminder consent, cross-skill sharing consent, daily reminder budgets, and grade-band quiet hours.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
