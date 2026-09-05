## Description:

英语口语陪练 helps Chinese K12 learners practice spoken English through short warmups, roleplay, impromptu speaking, pronunciation drills, and consent-gated review of speaking patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and supervised education operators use this skill for English speaking practice, including morning warmups, roleplay dialogs, impromptu speeches, pronunciation practice, and post-practice feedback. It is designed for upper-primary and middle-school learners and includes consent checks before reading or writing long-term speaking profile entries.

### Deployment Geography for Use:

China mainland by default; localize crisis resources, curriculum alignment, privacy assumptions, and minor-consent rules before deployment elsewhere.

## Known Risks and Mitigations:

Risk: A crisis referral marker for a minor may be retained outside the normal profile-consent flow.

Mitigation: Before deployment, define whether the marker is session-only or persistent, require appropriate guardian or student authorization for retained safety records, and document retention and deletion handling.

Risk: Emergency resources and privacy assumptions are written for China-mainland K12 use.

Mitigation: Localize emergency contacts, curriculum assumptions, and minor-consent requirements before making the skill available in another region.

Risk: Pronunciation feedback can be overstated if the platform only provides text or ASR transcription.

Mitigation: Only make phoneme-level pronunciation judgments when an audio scoring channel is available; otherwise provide self-practice guidance and avoid writing pronunciation weaknesses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [晨间热身5步 · 状态机定义](references/morning-warmup-statemachine.md)
- [中国学生高频发音弱点与纠正方法](references/pronunciation-issues.md)
- [5套真实场景完整对话脚本](references/roleplay-scripts.md)
- [分学段口语话题库](references/topic-bank.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or markdown feedback for tutoring, practice prompts, review notes, and consent-gated profile update confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety referral guidance and profile-control responses; pronunciation judgments require an audio scoring channel.]

## Skill Version(s):

2.1.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
