## Description:

A Chinese-language English speaking coach that guides K–12 learners through warm-ups, role-play, impromptu speaking, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 learners practice spoken English through short warm-ups, conversations, speeches, and review. Educators or caregivers can support younger learners; persistent progress tracking requires consent.

### Deployment Geography for Use:

Mainland China; localize crisis contacts, curriculum assumptions, and minor-consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: A minor's speaking performance or learning profile could be retained or shared without appropriate consent.

Mitigation: Require opt-in profile access, reminders, and cross-skill sharing; obtain guardian consent where required and allow session-only practice.

Risk: Mainland China crisis contacts and consent or curriculum assumptions may not fit other locations.

Mitigation: Localize emergency resources, curriculum, and minor-consent rules before deployment elsewhere; confirm location before giving emergency numbers.

Risk: Transcribed speech alone cannot support reliable phoneme-level pronunciation judgments.

Mitigation: Give expression-level feedback only unless a speech-scoring service is available; do not save pronunciation weaknesses inferred from text.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warm-up workflow](artifact/references/morning-warmup-statemachine.md)
- [Role-play scripts](artifact/references/roleplay-scripts.md)
- [Pronunciation issues](artifact/references/pronunciation-issues.md)
- [Platform capabilities and fallbacks](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with structured practice recaps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional consent-based progress tracking; phoneme-level feedback requires speech scoring.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
