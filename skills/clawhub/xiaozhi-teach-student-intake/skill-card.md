## Description:

把试听从"体验课"变成一次双向诊断，并按最小化原则给新学员建档。适用于老师说"新学员要试听""安排一节试听""试听课怎么上""学员档案怎么建""家长/孩子想学什么""试听完怎么记录""试听后怎么跟进"。流程：确认监护人同意 → 收最小必要信息 → 5W 需求访谈 → 5-10 分钟前测评 → 设计诊断式试讲 → 记录 5 维度观察 → 判断是否适配 → 建正式学员卡。范围到建档为止：不排课、不写课后记录、不登记课上练习与学校作业、不做阶段报告、不谈续费与流失挽回，也不收集或存储任何联系方式。排课与课节状态转 schedule-manager，课后记录转 lesson-log，续费/阶段报告/流失跟进转 renewal-report。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

独立教师可用此技能为新学员开展试听与需求诊断，并在取得监护人同意后创建最少必要的学员档案。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Student profiles concern minors and may be saved without guardian consent.

Mitigation: Confirm guardian consent and review the profile and package entries before saving.

Risk: Identifying or contact details in student records could expose a child's identity or enable direct contact.

Mitigation: Keep identifying details, contact information, and emergency contacts outside these records; retain only the minimum learning information.

Risk: Retention dates may be missed, and the instructions are unclear about whether diagnostic observations should persist.

Mitigation: Set and act on retention deadlines, and clarify observation retention before saving diagnostic notes.

## Reference(s):

- [学生基本信息表](references/student-basic-info-form.md)
- [需求访谈 5W 清单](references/needs-interview-5w-checklist.md)
- [需求画像卡](references/needs-profile-card.md)
- [诊断卡模板](references/diagnosis-card-template.md)
- [试听课五段结构](references/trial-lesson-5-segment-structure.md)
- [试听观察记录](references/trial-observation-record.md)
- [试听转化跟进话术](references/followup-scripts-trial-conversion.md)
- [正式学员档案模板](references/formal-student-profile-template.md)
- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Publisher profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Chinese text and Markdown drafts, plus structured student profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts; student records should use pseudonyms and omit contact details.]

## Skill Version(s):

2.12.6 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
