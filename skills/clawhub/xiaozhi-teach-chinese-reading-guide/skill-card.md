## Description:

面向语文老师的现代文阅读教学设计工具，用于设计文本解读、阅读策略练习、三阶阅读任务、群文阅读活动和班级阅读力记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

语文老师使用该 skill 为小学高段和初中现代文阅读课设计文本三解、阅读策略练习、三阶阅读任务和群文阅读活动，并生成需老师确认的班级阅读力记录更新。

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: Student records and reading profiles may expose personal or classroom-sensitive information.

Mitigation: Use pseudonymous student records, avoid real names and contact details, honor consent controls, and require teacher review before saving record updates.

Risk: Generated reading questions or lesson tasks may be incorrect or unsuitable for the selected text or grade band.

Mitigation: Label AI-generated items for teacher-side checking and require human verification before classroom use, assignment use, or resource-library storage.

Risk: Reading materials may contain copyrighted textbook, workbook, or full-book content.

Mitigation: Require copyrightStatus on selected texts, store textbook and workbook items as index-only references, and do not reproduce full教材 or ebook content.

Risk: Student reflections may include self-harm, bullying, family safety, or other crisis signals outside normal learning support.

Mitigation: Stop the reading workflow, follow the bundled crisis referral protocol, direct the student toward trusted adults or local emergency channels, and avoid recording sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-reading-guide)
- [文本三解模板](references/text-three-solve.md)
- [阅读 6 大策略卡片](references/six-strategies-card.md)
- [群文阅读设计模板](references/group-text-design.md)
- [文本三解填写样板](references/three-solve-sample.md)
- [阅读策略使用样板](references/strategy-use-sample.md)
- [三阶练习设计填写样板](references/three-stage-practice-sample.md)
- [群文阅读童年议题完整范例](references/group-text-sample-childhood.md)
- [学员阅读力档案模板](references/reading-ability-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [班级教学工作空间数据契约](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured record-update proposals when consented]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include teacher-confirmed pending updates for classWorkspace records and consent-gated handoff payloads; does not reproduce full textbook content.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
