## Description:

初中到高一的物理建模教练（高中部分目前覆盖高一必修第一册），用三步法（识别现象→选择模型→数学表达）训练学生从"看到题就套公式"变成"先判断物理模型再列式"。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 learners and tutoring agents use this skill to practice physics modeling: identifying the phenomenon, choosing the correct model, and expressing the relationship mathematically. It is intended for middle school through first-year high school physics support, not for full answer substitution during active exams.

### Deployment Geography for Use:

Mainland China-aligned Chinese-language K12 tutoring contexts

## Known Risks and Mitigations:

Risk: The skill handles minors and can create profile or reminder handoffs.

Mitigation: Enable profile, sharing, and reminder features only after confirming student and guardian consent settings, especially for parent-visible outputs.

Risk: Students may try to use the skill during active exams or restricted assessments.

Mitigation: Follow the bundled hint-ladder rule: refuse to discuss the active exam item and invite the student to return after the assessment for review.

Risk: A learner may disclose self-harm, abuse, severe despair, or another crisis signal during tutoring.

Mitigation: Stop tutoring flow and follow the bundled crisis referral protocol, including location-appropriate emergency guidance and referral to trusted adults.

Risk: Generated practice items can contain unsuitable difficulty, incomplete conditions, or incorrect answers.

Mitigation: Apply the bundled AI item self-check protocol before presenting generated exercises or variants to students.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-modeling-coach)
- [ClawHub publisher profile: qizhitang](https://clawhub.ai/user/qizhitang)
- [Physics Modeling Patterns](artifact/references/physics-modeling-patterns.md)
- [High School Physics Book 1 Model Cards](artifact/references/physics-hs1-models.md)
- [AI Item Self-Check Protocol](artifact/shared/ai-item-check.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform Conventions and Consent Controls](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Chinese-language conversational text or Markdown, with structured handoff or profile updates only when consent conditions are met.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not produce shell commands or executable code; may produce tutoring prompts, model-selection guidance, generated practice items after self-check, and consent-gated profile or reminder handoffs.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
