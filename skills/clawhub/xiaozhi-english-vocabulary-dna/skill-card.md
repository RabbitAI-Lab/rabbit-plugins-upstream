## Description:

英语词汇复习：按间隔重复排到期日，每天把到期的词合并成一张词卡；初中按义教词表，高中按课标词表的三档（义教、必修、选择性必修）。触发语："帮我记单词"、"把这个词存进词汇库"、"我单词背了就忘"、"下周要学新课了"、"启动词汇预热"、"帮我复习词汇"、"我的词汇库里有什么"。核心功能：三种入库方式 + SM-2 间隔重复排到期日 + 每日一张到期词卡（提醒由 IM 提醒统一发送）+ 课前预热雷达 + 个人遗忘速度调整。不处理：句子语法错误的追问（转英语语法突破教练）、整段作文批改（转英语写作进化教练）、发音是否标准（转英语口语陪练）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to save English vocabulary, review due words with spaced repetition, and preview vocabulary for upcoming lessons. It adapts review prompts to the learner's school level and vocabulary progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved learning records, sharing, or reminders may retain or expose student data when enabled without the intended consent.

Mitigation: Use session-only mode when persistence is unwanted; enable records, sharing, and reminders only when wanted, and follow guardian-consent controls for younger students.

Risk: Reminder delivery and storage depend on separate integrations that were not included in this review, so those features may be unavailable on a given platform.

Mitigation: Check platform capabilities, use session-only review when integrations are unavailable, and avoid promising proactive reminders unless reminder support is enabled.

## Reference(s):

- [English High-School Vocabulary](references/english-hs-vocabulary.md)
- [Vocabulary Radar Topics](references/vocabulary-radar-topics.md)
- [Vocabulary Records and Consent Controls](shared/vocab.md)
- [Platform Capability Fallbacks](shared/platform-conventions.md)
- [ClawHub Skill Release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Conversational text, vocabulary review cards, and learning summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily reviews are consolidated into one due-word card; saved records and reminders depend on platform capabilities and user consent.]

## Skill Version(s):

2.12.5 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
