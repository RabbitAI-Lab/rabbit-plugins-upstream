## Description:

A Chinese K12 English-speaking coach that runs consent-gated speaking practice, role play, impromptu speech, pronunciation review, warmups, and post-practice reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, parents, teachers, and learning platforms use this skill for guided English speaking practice, pronunciation-aware coaching where supported, role-play scenarios, daily warmups, and concise learning review. The skill is intended for Chinese K12 English-learning contexts with consent controls for profile use.

### Deployment Geography for Use:

Global, subject to local guardian-consent, voice-scoring, reminder, memory, and crisis-support configuration.

## Known Risks and Mitigations:

Risk: The skill may handle minors' speaking performance and profile observations.

Mitigation: Use it only in the intended Chinese K12 English-learning context, require the appropriate guardian-consent setup, and allow profile writes only after explicit consent.

Risk: Pronunciation feedback can be misleading if the platform lacks reliable voice scoring.

Mitigation: Confirm voice-scoring support before pronunciation judgments; otherwise limit feedback to text, vocabulary, grammar, expression, and fluency.

Risk: Crisis or safety disclosures can appear during student conversations.

Mitigation: Configure local crisis-support routing for the deployment region and follow the skill's crisis referral protocol instead of continuing normal tutoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning Warmup State Machine](references/morning-warmup-statemachine.md)
- [Pronunciation Issues](references/pronunciation-issues.md)
- [Roleplay Scripts](references/roleplay-scripts.md)
- [Topic Bank](references/topic-bank.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational coaching guidance with structured feedback, consent prompts, and markdown-compatible reference text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated profile observations, practice feedback, reminder handoff text, and local crisis referral guidance when triggered.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
