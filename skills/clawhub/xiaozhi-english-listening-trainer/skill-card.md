## Description:

为小学高段和初中学习者生成按词汇量、兴趣话题和语速分层的英语听力练习，并通过四步练习定位词义、句式或语速卡点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to create personalized English listening passages, comprehension questions, vocabulary follow-up, and coaching feedback. It is aimed at Chinese-language upper-primary and middle-school English listening practice.

### Deployment Geography for Use:

Global; review China-focused educational and crisis-resource assumptions before use outside mainland China.

## Known Risks and Mitigations:

Risk: The skill is intended for learners and includes China-focused crisis-resource assumptions.

Mitigation: Before use with minors or outside mainland China, confirm local crisis contacts, guardian expectations, parent sharing, reminders, and profile-sharing settings.

Risk: Listening profiles and cross-skill learning data could be written or shared without appropriate consent.

Mitigation: Only write or share profile data when the configured consent fields allow profile storage, cross-skill sharing, and parent-visible output.

Risk: Unavailable platform capabilities could make generated listening, statistics, or speech feedback misleading.

Mitigation: Use the documented fallbacks: text or reading-mode practice when speech is unavailable, session-only counts when history is unavailable, and no phoneme-level pronunciation feedback without audio scoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [听力话题模板与材料生成指南](references/listening-topic-templates.md)
- [英语错因维度表](shared/english-error-dimension-table.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational Markdown with generated listening passages, comprehension questions, vocabulary notes, coaching feedback, and consent-gated profile handoff examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on platform memory, speech, scoring, and statistics capabilities; documented fallbacks are used when those capabilities are unavailable.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
