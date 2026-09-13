## Description:

英语口语陪练 is a spoken-English coaching agent for Chinese K12 learners that runs short warmups, role plays, impromptu speaking, pronunciation drills, and consent-gated review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners in upper primary and middle school use this skill to practice spoken English, receive brief feedback, and build confidence in warmups, role plays, impromptu speaking, and pronunciation practice. Guardians or deploying educators should confirm consent, voice-scoring, memory, reminders, and crisis-referral settings before use.

### Deployment Geography for Use:

Mainland China K12 contexts by default; deployments elsewhere should localize emergency contacts, curriculum assumptions, and minor-data consent rules before release.

## Known Risks and Mitigations:

Risk: Voice scoring, persistent memory, reminders, cross-skill sharing, guardian consent, or crisis-referral settings may not match the deployment environment.

Mitigation: Confirm these platform settings before installation and disable or localize workflows that cannot meet the required consent and safety behavior.

Risk: The skill is designed for a mainland-China K12 context, including emergency-contact assumptions and minor-data consent expectations.

Mitigation: Localize emergency channels, curriculum assumptions, and guardian-consent rules before serving learners outside mainland China.

Risk: Pronunciation claims can be misleading when the platform has text or ASR transcripts but no voice-scoring capability.

Mitigation: Limit feedback to wording, grammar, expression, and fluency unless audio scoring is available; do not record phoneme-level pronunciation issues without scoring.

Risk: The skill can use optional student profile memory for speaking practice.

Mitigation: Read or write the speaking profile only after explicit session-level consent, and require guardian consent where the learner age band requires it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Morning warmup state machine](references/morning-warmup-statemachine.md)
- [Pronunciation issues reference](references/pronunciation-issues.md)
- [Roleplay scripts](references/roleplay-scripts.md)
- [Topic bank](references/topic-bank.md)
- [Platform conventions and localization requirements](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text with short practice prompts, feedback summaries, consent questions, and optional profile-update guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pronunciation feedback depends on platform voice scoring; cross-session profile use requires explicit consent.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
