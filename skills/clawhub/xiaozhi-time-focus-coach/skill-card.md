## Description:

时间与专注力教练帮助学生记录学习用时、运行番茄钟、分析黄金时段和分心规律，并在明确同意后保存专注档案或加入提醒队列。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students in Chinese K12 study settings use this skill to plan focused study sessions, record actual learning time, review distractions, and build a lightweight focus history when appropriate consent is present. Operators and guardians should use it only where the platform enforces the consent, localization, and data-boundary rules described by the release evidence.

### Deployment Geography for Use:

Global, with China Mainland defaults that must be localized before use elsewhere

## Known Risks and Mitigations:

Risk: The release evidence flags a loose cross-skill handover schema for a child-focused tool that can write long-term profile data and enqueue reminders.

Mitigation: Deploy only on runtimes that enforce the SKILL.md consent checks, recipient restrictions, and extensions.focus allowlist before profile writes or reminder handoffs.

Risk: The skill is designed for minors and can process study routines, distractions, and focus history.

Mitigation: Keep long-term memory, reminders, and cross-skill sharing disabled by default; require explicit student consent and guardian consent where the age band requires it.

Risk: Crisis referral content uses China Mainland defaults that may be unsafe or misleading outside that region.

Mitigation: Localize emergency and youth-support channels before non-China deployment, and ask the user for their country or region before giving crisis contact details.

Risk: Focus analytics may overstate conclusions when based on sparse or self-reported data.

Mitigation: Label conclusions with confidence, keep insufficient samples in the current session only, and avoid writing long-term golden-slot conclusions until the evidence threshold is met.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [focus-archives-template.md](references/focus-archives-template.md)
- [pomodoro-statemachine.md](references/pomodoro-statemachine.md)
- [dna-profile.schema.json](shared/dna-profile.schema.json)
- [handover-protocol.schema.json](shared/handover-protocol.schema.json)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)
- [platform-conventions.md](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational Markdown with structured study-time summaries, focus-session prompts, profile snippets, and reminder handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce pending profile or reminder records only after explicit consent and user confirmation.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
