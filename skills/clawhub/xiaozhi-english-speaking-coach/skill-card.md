## Description:

A Chinese-language English speaking coach offering short warm-ups, role-play, speech practice, and consent-based progress reviews for school-age learners.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

School-age English learners use guided conversation, role-play, pronunciation practice, and brief reviews to build speaking confidence. Parents or teachers should supervise younger learners and authorize any persistent learning profile.

### Deployment Geography for Use:

Global; designed for mainland China and requires localization of consent rules and crisis contacts elsewhere.

## Known Risks and Mitigations:

Risk: A minor's speech and learning profile may contain sensitive information.

Mitigation: Require explicit practice intent and consent before profile access or each update; obtain guardian authorization where required and offer session-only practice.

Risk: Text or speech transcripts cannot establish precise pronunciation errors.

Mitigation: Reserve phoneme-level feedback and persistent pronunciation records for platforms with scored audio; otherwise limit feedback to the words and expressions available.

Risk: Consent thresholds, curriculum assumptions, and crisis contacts may not apply outside mainland China.

Mitigation: Check local guardian-consent requirements and adapt curriculum, language defaults, and emergency referrals before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Speaking topic bank](artifact/references/topic-bank.md)
- [Role-play scripts](artifact/references/roleplay-scripts.md)
- [Pronunciation practice reference](artifact/references/pronunciation-issues.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured practice feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional, consent-gated session summaries and speaking-profile updates; phoneme-level feedback requires scored audio.]

## Skill Version(s):

2.6.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
