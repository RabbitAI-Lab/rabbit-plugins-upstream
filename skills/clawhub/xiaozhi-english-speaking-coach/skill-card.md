## Description:

为中国中小学生提供英语口语热身、情境对话、即兴表达和发音练习，并在获得同意后记录学习进展。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国中小学生的英语口语练习；在明确提出练习请求后，提供晨间热身、角色扮演、即兴表达、纠音练习与复盘。长期档案、提醒和跨技能共享需先确认学生或监护人的授权设置。

### Deployment Geography for Use:

Global (intended for Chinese K-12 learning)

## Known Risks and Mitigations:

Risk: Student speaking records, reminders, parent sharing or cross-skill handoffs may expose sensitive learning information without appropriate consent.

Mitigation: Confirm student or guardian consent settings before enabling these features; otherwise use current-session practice only.

Risk: Text transcripts alone cannot support reliable phoneme-level pronunciation assessment.

Mitigation: Only assess or store pronunciation weaknesses when audio scoring is available; otherwise limit feedback to observable language use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [Morning warm-up workflow](references/morning-warmup-statemachine.md)
- [Pronunciation practice guidance](references/pronunciation-issues.md)
- [Role-play scripts](references/roleplay-scripts.md)
- [Speaking topic bank](references/topic-bank.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with practice prompts and feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session recaps and, only with consent, speaking progress summaries.]

## Skill Version(s):

2.9.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
