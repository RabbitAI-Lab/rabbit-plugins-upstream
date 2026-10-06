## Description:

Generates personalized English listening practice for Chinese school students and helps identify vocabulary, sentence-structure, pace, and, for older students, speaker-intent difficulties.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary through high school use this skill to practice English listening with grade- and interest-matched passages, comprehension questions, targeted feedback, and optional progress tracking. Parents and educators can support younger students during practice.

### Deployment Geography for Use:

Mainland China; localize privacy, guardian consent, crisis referrals, and curriculum before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Student profile and learning-history data may be used without appropriate privacy or guardian consent.

Mitigation: Check local privacy and guardian-consent requirements; enable profile access and cross-skill sharing only with consent, and honor requests not to retain a session.

Risk: Crisis guidance and school content designed for mainland China may be inappropriate elsewhere.

Mitigation: Before deployment in another region, localize crisis referrals and curriculum; confirm the student's location before suggesting emergency resources.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [Listening topic templates](references/listening-topic-templates.md)
- [English error dimensions](shared/english-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and Markdown listening passages, questions, feedback, and progress summaries; audio when supported by the host platform]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts vocabulary, topic, and pace to grade and consented profile data; offers text-based alternatives when audio is unavailable.]

## Skill Version(s):

2.10.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
