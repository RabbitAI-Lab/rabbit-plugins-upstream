## Description:

为中国大陆中小学英语学习者按词汇水平和兴趣生成听力练习，并通过分步提问定位理解障碍。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生在家长或教师支持下进行个性化英语听力练习，获取适合学段的话题材料、理解题和针对词义、句式或语速困难的反馈。

### Deployment Geography for Use:

Mainland China (localize curriculum, crisis contacts, and minor-consent rules before use elsewhere)

## Known Risks and Mitigations:

Risk: Curriculum assumptions, crisis contacts, and minor-consent rules may not fit other regions or languages.

Mitigation: Localize these elements before use outside Simplified Chinese Mainland China K12 learning.

Risk: Learning records or information from other skills may be shared without the learner's intended consent.

Mitigation: Read or write shared profiles only when profile and cross-skill sharing are both enabled; honor requests not to retain a session.

Risk: A text-only fallback may be mistaken for actual listening practice.

Mitigation: Clearly label reading-only exercises as a fallback when speech playback is unavailable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [Listening topic templates](artifact/references/listening-topic-templates.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and Markdown listening exercises]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listening passages, vocabulary notes, comprehension questions, and targeted feedback; audio depends on platform capabilities.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
