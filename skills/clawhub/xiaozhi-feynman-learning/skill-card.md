## Description:

通过让学生用自己的话讲解、举例和迁移知识点，检验理解深度并指出卡住的位置。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students use guided explanations and follow-up questions to check whether they can explain, apply, and critically examine a concept. The skill returns a mastery level and the point where understanding breaks down, rather than teaching new material or generating a full practice set.

### Deployment Geography for Use:

Global (designed for mainland China; localize language, curriculum, consent, and crisis resources elsewhere)

## Known Risks and Mitigations:

Risk: A student's mastery record or reminder could be shared without the intended permission.

Mitigation: Keep results in the current session by default; check the student's explicit request and the relevant sharing or reminder consent before any handoff.

Risk: Chinese-language curriculum assumptions or mainland China crisis resources may not fit students elsewhere.

Mitigation: Localize language, curriculum, consent rules, and crisis-support resources before use outside mainland China or with non-Chinese-speaking students.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Five-jump assessment state machine](references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language conversational text with a mastery level and identified sticking point]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A minimal mastery record or retest reminder may be handed off only with the required student request and sharing or reminder consent.]

## Skill Version(s):

2.8.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
