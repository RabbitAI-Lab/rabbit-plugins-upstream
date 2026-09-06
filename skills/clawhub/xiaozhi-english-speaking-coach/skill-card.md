## Description:

英语口语陪练 helps students practice spoken English through morning warmups, roleplay, impromptu speaking, pronunciation practice, and consent-gated speaking-profile review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education-focused agents use this skill to run structured spoken-English practice for upper-primary and middle-school students. It guides conversation practice, roleplay scenarios, impromptu speaking, pronunciation drills, and post-practice review while requiring explicit consent before reading or writing long-term speaking-profile data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student voice and speaking-profile data could be retained without appropriate consent, especially for minors.

Mitigation: Require platform enforcement of consent fields, keep profile storage off by default, save pronunciation and interest entries only after explicit confirmation, and provide profile view, export, pause, correction, and deletion controls.

Risk: Pronunciation diagnosis could be overstated when only text or ASR transcript input is available.

Mitigation: Limit phoneme-level judgments and pronunciation-profile writes to audio_with_scoring input; for text or ASR-only sessions, provide general mouth-shape guidance and practice sentences without claiming to have heard a specific error.

Risk: Learner safety issues such as self-harm, bullying, serious despair, or unsafe home situations can exceed the learning scope.

Mitigation: Stop the coaching flow and follow the crisis exception path: stabilize without judgment, state AI limits, recommend contacting a trusted adult, and provide region-appropriate emergency or support channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach)
- [晨间热身5步状态机定义](artifact/references/morning-warmup-statemachine.md)
- [中国学生高频发音弱点与纠正方法](artifact/references/pronunciation-issues.md)
- [5套真实场景完整对话脚本](artifact/references/roleplay-scripts.md)
- [分学段口语话题库](artifact/references/topic-bank.md)
- [危机例外处理](artifact/shared/crisis-exception.md)
- [平台能力与降级约定](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown-style coaching feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include practice prompts, roleplay dialogue, pronunciation guidance, consent prompts, crisis referral guidance, and profile update proposals; no executable code.]

## Skill Version(s):

2.1.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
