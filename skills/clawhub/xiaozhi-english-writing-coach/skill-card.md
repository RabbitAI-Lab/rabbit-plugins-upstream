## Description:

An English writing coach for upper-primary and middle-school learners that reviews full paragraphs or essays across grammar, vocabulary, and logic, then uses guided questions to help students revise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners use this skill to get structured feedback on full English writing submissions, practice realistic writing scenarios, and build sentence-pattern awareness. With consent enabled, it can update a learning profile and produce progress summaries.

### Deployment Geography for Use:

Chinese mainland K12 contexts by default; localize crisis-referral contacts, curriculum assumptions, and minor-data consent practices before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can update or summarize learner profile information for minors.

Mitigation: Confirm learner and guardian consent settings before use, including profile storage, cross-skill sharing, parent-visible summaries, and reminders.

Risk: The skill is designed around Chinese mainland K12 curriculum, safety contacts, and minor-data assumptions.

Mitigation: Localize crisis-referral contacts, curriculum expectations, and consent practices before deploying outside the intended region.

Risk: Generated practice prompts, feedback, or rewrite suggestions could be inaccurate, over-advanced, or too directive for the learner.

Mitigation: Keep feedback focused on a few concrete issues, use the artifact's hint ladder and AI-item checks, and avoid writing full arguments, paragraphs, or essays for the student.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-writing-coach)
- [Vocabulary upgrade reference](artifact/references/vocabulary-upgrade.md)
- [English error dimension table](artifact/shared/english-error-dimension-table.md)
- [Platform conventions and localization guidance](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text coaching responses with structured feedback sections, guided questions, optional progress summaries, and consent-gated profile update guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; responses may rely on platform memory, OCR, and cross-session statistics when those capabilities are available and consent is enabled.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
