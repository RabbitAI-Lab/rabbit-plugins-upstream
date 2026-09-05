## Description:

帮学生记录学习时间、分析黄金时段、运行番茄钟，并在明确同意后积累分心规律。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students use this skill to record study sessions, run focus timers, compare planned and actual study time, and review personal distraction patterns. The skill is designed for Chinese K12 study-support workflows and includes minor-consent, privacy-control, and crisis-referral boundaries.

### Deployment Geography for Use:

China mainland by default; localize minor-consent and crisis-contact rules before use in other regions.

## Known Risks and Mitigations:

Risk: Profile writeback and reminder schemas may permit broader student-profile changes than the skill's time-only scope.

Mitigation: Reject any write outside extensions.focus and enforce sender-to-field authorization before deployment.

Risk: Consent enforcement for long-term memory, reminders, and cross-skill sharing may be weaker than the skill text requires.

Mitigation: Require profileEnabled, reminderConsent, and crossSkillSharing to be true for the relevant action, and require explicit user confirmation for each proposed record.

Risk: The skill is intended for students and includes crisis-contact behavior that may vary by region.

Mitigation: Localize minor-consent requirements and crisis-contact channels before use outside the default China mainland setting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Focus archives template](references/focus-archives-template.md)
- [Pomodoro state machine](references/pomodoro-statemachine.md)
- [Grade bands](shared/grade-bands.md)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception](shared/crisis-exception.md)
- [Unified vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational text and Markdown templates with structured profile, reminder, and handover fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose writes to extensions.focus and reminder queue entries only after the required consent checks and user confirmation.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
