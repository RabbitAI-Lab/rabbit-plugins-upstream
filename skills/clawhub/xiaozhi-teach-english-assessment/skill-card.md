## Description:

帮助英语教师设计听说读写综合测评、形成能力画像，并提出有针对性的教学建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国 K12 英语教师，辅助设计听说读写测评，依据作答证据制作能力画像和教学干预建议；等级判断及面向学生的内容须由教师审定。

### Deployment Geography for Use:

China (Chinese K12 teaching contexts)

## Known Risks and Mitigations:

Risk: Student assessment records may expose personal or sensitive information.

Mitigation: Use pseudonyms and class IDs; restrict profile updates to low-sensitivity weakness and mastery facts, and require recorded teacher consent before writeback.

Risk: Automated grades or public CSE/CEFR labels could misrepresent student ability.

Mitigation: Have teachers compare performance against CSE descriptors rather than converting scores directly, and do not publish individual proficiency labels.

Risk: Unreviewed generated questions or confidential exam materials could be mishandled.

Mitigation: Require teacher verification before adding generated items to assessments; do not input unreleased unified exam questions or copy unauthorized materials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [综合测评设计模板](references/assessment-template.md)
- [听说读写评分细则](references/four-skill-rubric.md)
- [学员能力画像模板](references/student-ability-profile-template.md)
- [高中测评蓝图示例](references/hs-assessment-blueprint.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown assessment plans, ability profiles and teaching recommendations; optional structured workspace updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher review and consent required before assessment materials or student-profile updates are saved.]

## Skill Version(s):

2.8.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
