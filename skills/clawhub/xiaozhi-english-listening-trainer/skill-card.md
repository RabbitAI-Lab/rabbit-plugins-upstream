## Description:

为中文 K12 学生生成按词汇量和兴趣定制的英语听力材料，并通过四步练习定位词义、句式或语速卡点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

External Chinese-speaking upper-primary and middle-school learners use this skill to practice personalized English listening. It generates level-matched listening passages, comprehension checks, vocabulary notes, and guidance for diagnosing whether a listening problem comes from word meaning, sentence structure, or speed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use educational profile data and cross-skill vocabulary handoff for personalization.

Mitigation: Enable profile, cross-skill sharing, guardian consent, deletion, and export controls before deployment, and honor the skill's consent checks before writing profile data.

Risk: Younger learners may use the skill without appropriate adult oversight.

Mitigation: Apply the documented prerequisite that upper-primary use requires a parent or teacher present.

Risk: A learning session may surface self-harm, bullying, severe distress, or family-safety signals beyond the skill's tutoring scope.

Mitigation: Stop the tutoring flow and follow the bundled crisis exception protocol, including referral to trusted adults or local emergency channels when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [listening-topic-templates.md](artifact/references/listening-topic-templates.md)
- [ai-item-check.md](artifact/shared/ai-item-check.md)
- [english-error-dimension-table.md](artifact/shared/english-error-dimension-table.md)
- [crisis-exception.md](artifact/shared/crisis-exception.md)
- [platform-conventions.md](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text tutoring flow with listening passages, comprehension questions, vocabulary notes, reports, and consent-gated handoff guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports profile-aware personalization, consent-gated vocabulary/profile handoff, and degraded text-only practice when audio capabilities are unavailable.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
