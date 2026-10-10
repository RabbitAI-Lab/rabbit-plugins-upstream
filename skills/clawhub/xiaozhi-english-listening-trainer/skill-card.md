## Description:

为中文中小学生按词汇水平和兴趣生成英语听力材料，并通过分步练习定位理解障碍。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中文中小学生在家长或教师适当陪同下练习与自身水平、兴趣匹配的英语听力；教学人员可用分步反馈了解学生的词义、句子结构或语速障碍。

### Deployment Geography for Use:

Mainland China (Simplified Chinese K–12 defaults; localize curriculum, consent and crisis referrals before use elsewhere)

## Known Risks and Mitigations:

Risk: Learners' interests, vocabulary history and listening progress may be read or saved across learning profiles.

Mitigation: Enable profile memory and cross-skill sharing only with student or guardian consent; honor requests not to remember, share or save a session.

Risk: Chinese K–12 curriculum and crisis-support defaults may be unsuitable outside mainland China.

Mitigation: Localize curriculum, consent procedures and crisis contacts before deployment elsewhere; use local emergency resources for learners in crisis.

Risk: Without voice playback, a text-only exercise may be mistaken for listening practice.

Mitigation: Provide a reader or device speech playback where possible; clearly label text-only practice as a temporary substitute.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [Listening topic templates](artifact/references/listening-topic-templates.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform capability and fallback guidance](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with listening passages, comprehension questions and feedback; optional spoken playback where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Practice difficulty and topic adapt to the learner; without voice playback, text-based practice is not equivalent to listening.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
