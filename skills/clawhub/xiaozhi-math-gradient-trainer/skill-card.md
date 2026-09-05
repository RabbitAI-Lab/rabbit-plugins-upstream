## Description:

初中数学分层进阶练习技能，用 5 层难度定位学生当前练习层级，并逐层生成进阶训练、复测反馈和成长日记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External middle-school learners use this skill to find the current practice level for a math topic, train with scaffolded harder problems, and summarize progress after confirmation. It is also useful for guardians or learning platforms that need consent-aware math progress records and optional reminder handoff.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: The skill may create or update math progress records for minors.

Mitigation: Require current student or guardian consent before profile writeback, and provide view, correction, deletion, pause, sharing-control, and export paths.

Risk: Optional study reminders could be sent outside the intended reminder controls.

Mitigation: Route reminders only through the reminder service and respect pause, consent, daily budget, and quiet-hour controls.

Risk: Generated math problems may be invalid, over-level, or misleading.

Mitigation: Apply the bundled AI item self-check before presenting generated practice items, including self-solving, uniqueness, sufficient conditions, friendly values, and grade-level checks.

Risk: Deployment outside the intended China Mainland K12 context could expose incorrect curriculum assumptions or crisis contacts.

Mitigation: Localize curriculum scope, consent requirements, and crisis referral channels before use in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [Initial math gradient level reference](references/gradient-levels.md)
- [AI-generated item self-check protocol](shared/ai-item-check.md)
- [Hint ladder and worked-example exit rules](shared/hint-ladder.md)
- [Platform capability conventions](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational guidance, math practice prompts, Markdown summaries, and structured JSON handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated progress writeback and reminder queue handoff content; no hidden execution or data exfiltration was reported by security evidence.]

## Skill Version(s):

2.1.6 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
