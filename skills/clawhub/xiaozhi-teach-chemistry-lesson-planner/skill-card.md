## Description:

为中国初高中化学教师生成以宏观现象、微观解释和化学符号为主线的教案草稿，支持课时统筹、初高衔接、复习课和讲评课，并要求教师在使用前复核。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初高中化学教师用它起草新授课、复习课和讲评课教案，安排三重表征、提问链和实验位，并结合班级情况调整课时。教案与生成的题目须由教师审核后用于课堂。

### Deployment Geography for Use:

中国大陆；用于其他地区前须适配课程标准、危机求助渠道、法律引用及数据同意规则。

## Known Risks and Mitigations:

Risk: Lesson plans or AI-generated questions may be inaccurate or unsuitable for a class.

Mitigation: Teachers review plans and check generated items before classroom use.

Risk: An experiment slot could be mistaken for an executable lab procedure.

Mitigation: Treat slots as planning prompts only; teachers verify safety and use the dedicated lab guide for procedures.

Risk: Student records or unreleased examination material could be disclosed.

Mitigation: Use pseudonyms or seat numbers and do not input examination material before all sittings are complete.

Risk: Chinese curricula, crisis contacts and consent practices may not apply elsewhere.

Mitigation: Localize these assumptions before deployment outside Chinese K12 settings.

## Reference(s):

- [初高中化学课程对照](references/chemistry-curriculum-map.md)
- [高中必修课程对照](references/chemistry-hs2-curriculum-map.md)
- [高中选择性必修课程对照](references/chemistry-hs3-curriculum-map.md)
- [实验安全约定](shared/lab-safety.md)
- [教学工作区数据结构](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown lesson-plan drafts and teaching guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts require teacher review; experiment slots are not operating procedures.]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
