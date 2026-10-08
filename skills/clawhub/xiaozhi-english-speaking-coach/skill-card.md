## Description:

Guides Chinese K–12 learners through English speaking practice, role-play, pronunciation feedback when scored audio is available, and short progress reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 learners use this skill to practice spoken English through five-minute warm-ups, role-play, impromptu speaking, and guided review. Profile-based progress tracking and reminders require consent.

### Deployment Geography for Use:

China mainland; localize crisis resources, curriculum assumptions, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Students' voice practice or learning profiles may be retained or shared without informed consent.

Mitigation: Require explicit practice intent and consent before profile access or updates, reminders, cross-skill sharing, and parent-visible summaries; offer session-only practice.

Risk: Text transcripts can be mistaken for evidence of specific pronunciation errors.

Mitigation: Offer sound-level corrections only when audio scoring is available; otherwise limit feedback to wording, grammar, and expression.

Risk: Crisis referrals and minor-consent assumptions may not transfer outside China mainland.

Mitigation: Localize emergency resources and guardian-consent rules before deployment elsewhere; stop tutoring and direct students to appropriate local help when crisis signals arise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warm-up state machine](artifact/references/morning-warmup-statemachine.md)
- [Pronunciation issues](artifact/references/pronunciation-issues.md)
- [Role-play scripts](artifact/references/roleplay-scripts.md)
- [Speaking topic bank](artifact/references/topic-bank.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and Markdown practice summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sound-level pronunciation feedback requires scored audio; lasting profile updates require consent.]

## Skill Version(s):

2.11.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
