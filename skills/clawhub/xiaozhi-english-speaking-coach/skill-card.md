## Description:

英语口语陪练为小学高段和初中学习者提供晨间热身、角色扮演、即兴演讲、纠音练习和经同意的口语档案复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External student learners use this skill to practice spoken English through short warmups, roleplay, impromptu speaking, pronunciation drills, and focused review. It is aimed at upper-primary and middle-school English practice, with profile-based follow-up only after user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child speech or oral-profile data could be stored, shared across skills, used for reminders, or shown to parents without sufficiently explicit consent.

Mitigation: Require explicit user or guardian opt-in before oral-profile storage, cross-skill sharing, reminders, or parent sharing, and keep visible controls to view, correct, delete, pause, or export the profile.

Risk: Broad voice triggers could start a practice flow before the learner clearly intends profile access or state saving.

Mitigation: Use explicit practice commands or ask for confirmation before reading profile data or saving practice state.

Risk: Pronunciation weaknesses could be recorded from ASR text even though audio scoring is required for reliable pronunciation judgments.

Mitigation: Record pronunciation weaknesses only when audio scoring is available; for text or ASR-only sessions, provide general pronunciation guidance without claiming observed phoneme errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warmup state machine](references/morning-warmup-statemachine.md)
- [Roleplay scripts](references/roleplay-scripts.md)
- [Topic bank](references/topic-bank.md)
- [Pronunciation issues](references/pronunciation-issues.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational text and Markdown practice plans, feedback, summaries, and profile-control prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pronunciation feedback is limited to platforms with audio scoring; otherwise the skill provides text-level coaching and practice guidance.]

## Skill Version(s):

2.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
