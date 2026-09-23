## Description:

A Chinese-language junior-high math coaching skill that guides students through math problems with questions, hint ladders, similar practice problems, consent-gated records, and crisis-safety exceptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 learners use this skill to work through junior-high math problems, review mistakes, generate similar practice, and prepare for near-term exams without receiving direct answers before attempting the problem. Host platforms should use it only in the intended China-mainland tutoring context unless curriculum, consent, reminder, and crisis-referral rules are localized.

### Deployment Geography for Use:

China mainland by default; localize before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese-language, China-mainland K12 tutoring, and its curriculum assumptions, consent defaults, and crisis-referral contacts may not fit other regions.

Mitigation: Install it only for that context, or localize curriculum scope, consent rules, reminder behavior, and crisis-referral contacts before use.

Risk: The skill can handle minors' learning records, cross-skill handoffs, archiving, and reminder requests.

Mitigation: Require the host platform to enforce the stated consent checks before reading records, sharing across skills, archiving mistakes, or enqueueing reminders.

Risk: Students may request help during an active exam or ask for direct answers before attempting a problem.

Mitigation: Follow the exam refusal rule and hint ladder: do not assist active exams, ask what the student has tried first, and escalate hints gradually.

Risk: Generated similar practice problems or exam-review items could be incorrect or poorly matched.

Mitigation: Apply the bundled AI item self-check before showing generated problems and require human verification before teacher-facing reuse or resource-bank entry.

Risk: Crisis or safety signals from minors could be mishandled if treated as ordinary learning anxiety.

Mitigation: Give the crisis exception priority over tutoring, reminders, summaries, and records; route to trusted adults and local emergency or crisis resources as specified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [数学四步拍照法状态机](artifact/references/photo-4step-statemachine.md)
- [数学苏格拉底五问链学段适配指南](artifact/references/math-socrates-guide.md)
- [提示阶梯与完整示例出口](artifact/shared/hint-ladder.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Chinese-language Markdown guidance with structured handoff JSON when consent permits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no installer, executable package, shell commands, API calls, or credentials were identified in the release evidence.]

## Skill Version(s):

2.2.0 (source: evidence.json release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
