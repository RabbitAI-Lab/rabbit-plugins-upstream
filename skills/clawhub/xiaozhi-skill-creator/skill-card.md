## Description:

帮助学习类 SKILL 的开发者用四层结构、隐私与安全边界及五步测试流程编写和改进提示词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向学习类 SKILL 开发者及有编程或提示词基础的高中生，提供角色、规则、记忆和输出的编写模板，以及测试和排查行为不稳定的方法。不提供学科辅导或练习题。

### Deployment Geography for Use:

Mainland China; localize crisis contacts, curriculum assumptions and minor-data consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: Emergency contacts in templates may be inappropriate outside mainland China.

Mitigation: Confirm the user's region and replace crisis referral contacts before deploying student-facing skills elsewhere.

Risk: Curriculum and minor-data consent defaults may not fit other regions.

Mitigation: Check local curricula and guardian-consent requirements before using the templates with students.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Skill templates library](artifact/references/skill-templates-library.md)
- [Crisis exception and regional guidance](artifact/shared/crisis-exception.md)
- [Platform and privacy conventions](artifact/shared/platform-conventions.md)
- [Shared terminology and consent definitions](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Chinese Markdown with copyable SKILL prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text guidance only; no executable code or platform runtime dependency.]

## Skill Version(s):

2.6.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
