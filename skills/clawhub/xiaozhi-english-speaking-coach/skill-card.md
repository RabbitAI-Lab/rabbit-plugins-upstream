## Description:

An English-speaking coach that guides short warm-ups, role-play and speaking practice, then offers supportive feedback and, with consent, tracks learning progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students practice spoken English through short conversations, role-play, impromptu speaking and optional pronunciation exercises. The coach provides a recap and can maintain a learning profile or schedule reminders only with the required consent.

### Deployment Geography for Use:

Global; adapt minor-consent requirements and crisis resources to the user's location.

## Known Risks and Mitigations:

Risk: Speaking assessments and learning history may expose sensitive information, especially for children.

Mitigation: Require explicit consent before accessing or updating a learning profile, sharing items with other skills, or scheduling reminders; obtain guardian consent where needed.

Risk: Text or transcription alone cannot reliably support phoneme-level pronunciation judgments.

Mitigation: Provide pronunciation-specific feedback only when speech-assessment capability is available; otherwise limit feedback to the learner's words and expression.

Risk: Crisis guidance and consent expectations may not fit learners outside Mainland China.

Mitigation: Confirm the learner's location and relevant guardian permissions, then provide locally appropriate help resources before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warm-up workflow](references/morning-warmup-statemachine.md)
- [Pronunciation practice reference](references/pronunciation-issues.md)
- [Role-play scripts](references/roleplay-scripts.md)
- [Speaking topic bank](references/topic-bank.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with structured speaking feedback and optional progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pronunciation-specific feedback requires speech assessment; profile updates and reminders require consent.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
