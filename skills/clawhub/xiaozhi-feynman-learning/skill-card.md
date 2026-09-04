## Description:

用"讲给小智听"来检验学生是否真的学会了某个概念（数学函数、物理受力、英语时态、语文文言实词都适用）。学生说“我来给你讲讲今天学的”“我觉得我懂了你测测我”“帮我检验一下我学没学会”“AI都讲明白了我应该会了吧”时可激活。产出是掌握度判定（会复述/会解释/真正掌握）与卡住位置，不做错因归档（转错题本）、不讲新知识（转对应学科教练）、不出成套练习。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language students use this skill to test whether they truly understand a concept by explaining it, giving examples, answering why, and transferring the idea to a new context. The agent returns a mastery judgment, stuck point, next-step guidance, and optional learning-profile writeback when the platform and consent controls allow it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning-progress records and cross-skill sharing can expose student learning data if storage, sharing, deletion, guardian-consent, or reminder controls are not enforced.

Mitigation: Before installation, verify that those platform controls are active and keep writebacks limited to confirmed fields such as concept, subject, mastery depth, stuck point, date, and next suggestion.

Risk: Crisis referral guidance is localized for mainland China and may be unsuitable in other regions.

Mitigation: Localize emergency and youth-support contacts before use outside mainland China, while preserving the skill's instruction to stop tutoring flow and direct the learner to trusted adults and urgent help when needed.

Risk: The skill is designed for Chinese-language student tutoring and may be less suitable for other languages or non-student contexts.

Mitigation: Use it primarily in Chinese-language tutoring scenarios or localize prompts, grade-band assumptions, examples, and safety guidance before broader deployment.

Risk: Generated check questions or transfer examples can be incorrect or outside the learner's grade band.

Mitigation: Apply the bundled AI item self-check protocol before presenting generated items, and require teacher review before adding generated items to teacher-facing resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)
- [Feynman 4+1 jump state machine](references/feynman-5jump-statemachine.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Grade bands](shared/grade-bands.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Published Learning DNA schema URL](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown with optional structured learning-record and handover entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce mastery labels, stuck-point summaries, next-step suggestions, privacy-control responses, and consent-gated writeback or reminder handoff entries.]

## Skill Version(s):

2.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
