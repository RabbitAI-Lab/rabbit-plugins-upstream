## Description:

英语听力训练：按你的词汇量和兴趣生成一段听力材料，练完帮你定位卡在哪一层。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 English learners use this skill to generate level- and interest-matched listening practice, comprehension checks, and coaching on whether listening difficulty comes from vocabulary, sentence structure, or speed. Educators or learning platforms may use it as a guided English listening practice agent for upper primary and junior middle school learners.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent rules, and crisis-help guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Use with children can involve profile storage, cross-skill sharing, and parent-facing summaries.

Mitigation: Confirm profile storage, guardian consent, cross-skill sharing, and parent-sharing settings before deployment or use.

Risk: The skill is designed around mainland China K12 curriculum, consent assumptions, and crisis-help defaults.

Mitigation: Localize curriculum alignment, consent requirements, and crisis-help resources before deploying outside mainland China.

Risk: Learners may disclose crisis signals during a learning session.

Mitigation: Stop the learning flow and follow the bundled crisis exception and referral protocols, using local emergency channels for the learner's region.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [听力话题模板与材料生成指南](references/listening-topic-templates.md)
- [英语错因维度表](shared/english-error-dimension-table.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [AI 出题自检协议](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown or plain text coaching flow with generated listening passages, vocabulary notes, comprehension questions, diagnostic feedback, and consent-gated profile handoff data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for Chinese K12 English listening practice; profile updates and parent-facing outputs are gated by consent settings.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
