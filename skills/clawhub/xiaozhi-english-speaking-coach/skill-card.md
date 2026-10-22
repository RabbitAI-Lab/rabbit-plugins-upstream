## Description:

为中国 K12 学生提供英语口语热身、角色扮演、即兴演讲和练后反馈，并在获得同意后记录进步。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, junior high and senior high school practice spoken English through short conversations, roleplay and speeches, then receive age-appropriate feedback. Pronunciation assessment requires audio scoring; profile reads and progress records require consent.

### Deployment Geography for Use:

Mainland China (default); localize crisis contacts and consent practices before use elsewhere.

## Known Risks and Mitigations:

Risk: A minor's speech, interests or learning profile could be retained or shared without appropriate permission.

Mitigation: Verify guardian consent and profile/cross-skill sharing settings; obtain session-specific permission before reading or saving progress.

Risk: Text transcripts alone cannot support reliable pronunciation judgments.

Mitigation: Only assess individual sounds when audio scoring is available; otherwise offer general practice guidance without recording a pronunciation weakness.

Risk: Crisis contact advice may be inappropriate outside Mainland China.

Mitigation: Confirm the learner's location and use localized crisis and emergency contacts; stop practice and refer concerning disclosures to trusted adults and appropriate help.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warmup state machine](references/morning-warmup-statemachine.md)
- [Roleplay scripts](references/roleplay-scripts.md)
- [Pronunciation practice guidance](references/pronunciation-issues.md)
- [Age-appropriate speaking topics](references/topic-bank.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with structured practice feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Practice summaries and optional consent-gated progress notes; pronunciation judgments only with audio scoring.]

## Skill Version(s):

2.11.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
