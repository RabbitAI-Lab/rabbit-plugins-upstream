## Description:

An English vocabulary study skill that stores learner-selected words, schedules SM-2 spaced review due dates, prepares one daily due-vocabulary card, and supports pre-class vocabulary warm-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper-primary and middle-school English use this skill to build a personal vocabulary library, receive consent-gated due-word review cards, and warm up new classroom vocabulary before lessons. Learning agents can use it to generate vocabulary prompts, update vocabulary mastery records, and queue a single merged daily reminder when consent allows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term vocabulary records and reminder schedules may expose student learning data if enabled without appropriate student or guardian consent.

Mitigation: Confirm profile, cross-skill sharing, reminder, and guardian consent before writing records or queuing reminders; provide view, correction, pause, delete, export, and sharing-control paths.

Risk: Vocabulary reminders can become intrusive if a student stops responding.

Mitigation: Limit the skill to one daily vocabulary card merged by the reminder system and pause vocabulary reminders after three consecutive nonresponses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [Vocabulary radar topic templates](artifact/references/vocabulary-radar-topics.md)
- [Spaced review schedule](artifact/shared/ebbinghaus-schedule.md)
- [Shared vocabulary and consent rules](artifact/shared/vocab.md)
- [English error dimension table](artifact/shared/english-error-dimension-table.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured handoff payload examples for vocabulary cards, profile updates, and reminder queue entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses consent-gated long-term vocabulary records and a single merged daily vocabulary reminder when platform reminder support is available.]

## Skill Version(s):

2.1.12 (source: server release metadata and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
