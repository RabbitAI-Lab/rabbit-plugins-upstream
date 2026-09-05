## Description:

Helps students maintain an English vocabulary profile, schedule spaced review with SM-2 style intervals, and produce one consent-controlled daily vocabulary card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning-support agents use this skill to save English words from pasted text, images when OCR is available, or conversation, then review due words through one daily card. It also supports lesson vocabulary preview, vocabulary health summaries, and consent-controlled sharing with related learning skills.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of safety contacts, curriculum assumptions, and minor-consent rules before student-facing use.

## Known Risks and Mitigations:

Risk: The skill can maintain vocabulary progress and reminder data for students, including younger learners or shared family chat accounts.

Mitigation: Enable profile, reminder, cross-skill, and parent-sharing consent only when those data flows are desired; use the built-in view, correct, delete, pause, sharing-control, and export controls.

Risk: Vocabulary reminders could become excessive or feel unsolicited if reminder consent and response state are ignored.

Mitigation: Queue at most one daily vocabulary card through the reminder system, require reminder consent, and pause vocabulary reminders after three consecutive non-responses until the student asks to resume.

Risk: The skill is designed around Mainland China K12 curriculum, safety contacts, and minor-consent assumptions.

Mitigation: Localize emergency contacts, curriculum mapping, grade-band assumptions, and minor-consent rules before using it in another region.

Risk: Spaced-repetition outputs could overstate memory science or present retention percentages as learner-specific facts.

Mitigation: Use SM-2 style due-date scheduling without promising exact retention rates, and present vocabulary health summaries as counts and confidence-labeled observations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang)
- [Vocabulary radar topics](references/vocabulary-radar-topics.md)
- [Shared vocabulary and consent conventions](shared/vocab.md)
- [Platform capability and deployment conventions](shared/platform-conventions.md)
- [Spaced review schedule parameters](shared/ebbinghaus-schedule.md)
- [Crisis exception guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown/text responses with vocabulary-card content and optional JSON handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses consent-controlled profile updates and reminder queue entries when the hosting platform supports those capabilities.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
