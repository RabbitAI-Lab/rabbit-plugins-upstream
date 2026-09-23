## Description:

英语口语陪练 helps Chinese-speaking K12 learners practice spoken English through short warmups, roleplay, impromptu speaking, pronunciation coaching, and consent-based progress memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, parents, and educators use this skill to run structured English speaking practice for Chinese-speaking upper-primary and middle-school students. It guides practice sessions, gives feedback, escalates safety concerns, and only reads or writes long-term oral-practice records after the required consent checks.

### Deployment Geography for Use:

China mainland by default; localize safety channels, curriculum assumptions, and minor-consent rules before deployment elsewhere.

## Known Risks and Mitigations:

Risk: The skill may process student speech, transcripts, pronunciation observations, progress records, or vocabulary handoffs.

Mitigation: Use it only where platform consent flags are configured; require explicit consent before reading or writing profile data, cross-skill sharing, parent-visible output, or reminders.

Risk: Minor learners may use the skill without the required guardian or teacher involvement.

Mitigation: For upper-primary learners and other cases requiring guardian consent, confirm the appropriate adult involvement before entering long-term profile or practice flows.

Risk: Pronunciation feedback can be misleading when the platform only provides text or ASR transcripts.

Mitigation: Only make phoneme-level pronunciation judgments and write pronunciation weaknesses when audio_with_scoring is available; otherwise limit feedback to vocabulary, grammar, expression, and fluency.

Risk: Safety or crisis signals can appear during student conversations.

Mitigation: Stop the learning workflow on self-harm, severe distress, abuse, bullying, or family-safety signals; provide AI-boundary language and localized adult or emergency support guidance.

Risk: The artifact's default curriculum, consent, and crisis-channel assumptions are China-mainland specific.

Mitigation: Localize emergency contacts, curriculum expectations, and minor-consent requirements before deploying outside mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [晨间热身5步 · 状态机定义](references/morning-warmup-statemachine.md)
- [中国学生高频发音弱点与纠正方法](references/pronunciation-issues.md)
- [5套真实场景完整对话脚本](references/roleplay-scripts.md)
- [分学段口语话题库](references/topic-bank.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [英语错因维度表](shared/english-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational text and Markdown-style structured summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pronunciation judgments require audio_with_scoring; profile memory, cross-skill sharing, parent-visible output, and reminders require explicit consent and platform support.]

## Skill Version(s):

2.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
