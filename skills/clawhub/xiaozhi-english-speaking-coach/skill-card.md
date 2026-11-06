## Description:

为小学高段至高中学习者提供英语口语热身、角色扮演、即兴演讲、发音练习与复盘，并仅在获得同意后保存长期口语记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

外部英语学习者（小学高段至高中）可用它进行晨间口语热身、角色扮演、即兴演讲和表达复盘，逐步建立开口练习习惯。跨会话档案与提醒仅在取得相应同意并由平台支持时使用。

### Deployment Geography for Use:

China (designed for mainland China K–12; localize safety contacts, curriculum, and minor-data consent before use elsewhere)

## Known Risks and Mitigations:

Risk: Speaking practice can involve sensitive student speech and learning-profile information.

Mitigation: Use session-only practice unless the student explicitly agrees to profile access or each profile write; for younger students, follow the guardian-consent and adult-supervision requirements. Review the host platform's speech-data handling before enabling memory or reminders.

Risk: Text transcription alone cannot support reliable phoneme-level pronunciation judgments.

Mitigation: Give pronunciation judgments and store pronunciation weaknesses only when speech-scoring support is available; otherwise provide practice guidance without claiming to have assessed the student's pronunciation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warm-up workflow](artifact/references/morning-warmup-statemachine.md)
- [Role-play scripts](artifact/references/roleplay-scripts.md)
- [Pronunciation practice reference](artifact/references/pronunciation-issues.md)
- [Speaking topic bank](artifact/references/topic-bank.md)
- [Platform capability limits](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational practice prompts, feedback, and short progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term profile access and reminders require consent and host-platform support; pronunciation diagnosis requires speech-scoring support.]

## Skill Version(s):

2.12.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
