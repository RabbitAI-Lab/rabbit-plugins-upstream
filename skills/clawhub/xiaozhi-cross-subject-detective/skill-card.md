## Description:

用一个真实主题在一周内串联多门学科，找出学科之间的联结。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K12 students, guardians, teachers, or learning agents use this skill to guide a week-long interdisciplinary project: selecting a real topic, exploring it from several subject perspectives, identifying links, and summarizing the project record. It is intended for cross-subject inquiry and concept-map growth, not single-subject problem solving, mistake analysis, or writing a report on the student's behalf.

### Deployment Geography for Use:

Global, with localization required for crisis referral channels and with intended use in Chinese K12 learning contexts.

## Known Risks and Mitigations:

Risk: Student project records, profile memory, or cross-skill sharing could expose learning data to an unintended audience.

Mitigation: Before enabling memory or sharing, confirm record visibility, guardian consent requirements, and deletion or export controls.

Risk: The skill is intended for Chinese K12 learning contexts and may require localization for student-safety escalation paths.

Mitigation: Deploy only in the intended context unless crisis-referral channels and responsible-adult escalation guidance are localized for the user's region.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cross-subject-detective)
- [跨学科侦探周项目记录模板](references/detective-project-template.md)
- [跨学科概念关联标准模板库](shared/cross-subject-connections.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [学段参数表](shared/grade-bands.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown and structured study-record guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project records, cross-subject connection summaries, concept-graph writeback guidance, and privacy-control prompts.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
