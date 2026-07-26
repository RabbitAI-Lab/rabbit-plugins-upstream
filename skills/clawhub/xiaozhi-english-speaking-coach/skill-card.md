## Description: <br>
A Chinese-language English speaking coach that guides learners through short warmups, role play, impromptu speaking, pronunciation review, Socratic prompts, and permission-based follow-up from a learner profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners use this skill as an English speaking practice coach for morning warmups, role-play conversations, short speeches, pronunciation practice, and progress review. It is designed for coached dialogue and feedback, with profile-based continuity only when the user permits tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses broad activation rules and may track pronunciation weaknesses, fluency patterns, vocabulary, milestones, and topic preferences across sessions. <br>
Mitigation: Use it for explicit coaching requests and enable continuous tracking or reminders only when the platform provides clear controls to view, limit, and delete the stored learner profile. <br>
Risk: Pronunciation scoring and stuck-silence prompts depend on audio analysis capabilities that may not be available in all channels. <br>
Mitigation: When only text or ordinary ASR is available, downgrade to vocabulary, grammar, expression, and fluency review, and tell the learner that phoneme-level pronunciation cannot be assessed in that mode. <br>


## Reference(s): <br>
- [晨间热身5步 · 状态机定义](references/morning-warmup-statemachine.md) <br>
- [中国学生高频发音弱点与纠正方法](references/pronunciation-issues.md) <br>
- [5套真实场景完整对话脚本](references/roleplay-scripts.md) <br>
- [分年级口语话题库](references/topic-bank.md) <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-speaking-coach) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational coaching text with Markdown-formatted feedback and practice prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend learner-profile updates, reminders, or follow-up practice only when the user permits tracking.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
