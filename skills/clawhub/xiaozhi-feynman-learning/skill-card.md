## Description:

通过学生讲解、举例和迁移来检验对知识点的理解，并指出掌握程度和理解盲区。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国 K12 学生及陪同使用的家长或教师，以费曼式讲解和追问自测单个知识点，获得掌握度评估与下一步建议。

### Deployment Geography for Use:

China; other regions require localized curricula, safety referrals, and consent rules.

## Known Risks and Mitigations:

Risk: Chinese K12 curriculum and safety referrals may be inappropriate in other regions.

Mitigation: Use in the intended tutoring context or localize curriculum assumptions, crisis referrals, and consent rules before deployment.

Risk: Student mastery records and retest reminders can expose sensitive learning information.

Mitigation: Require explicit consent for profile sharing and reminders; honor view, correction, deletion, pause, sharing-control, and export requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)
- [Feynman five-step state machine](references/feynman-5jump-statemachine.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies a mastery tier and understanding gaps; profile updates and retest reminders require explicit consent.]

## Skill Version(s):

2.11.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
