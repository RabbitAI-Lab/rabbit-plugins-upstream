## Description:

面向语文老师的文言文与古诗词教学设计工具，帮助设计诵读正音、训诂、串讲、主题讨论、文化背景联结和班级古文积累记录，同时避免输出整篇逐字串讲、完整现代文翻译或替代老师批改。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers and teaching assistants use this skill to plan classical Chinese and poetry lessons, including reading rhythm, vocabulary and syntax explanation, thematic discussion, cultural context, and student accumulation records. The skill produces teacher-facing lesson structure and discussion material rather than full translations or automated grading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may work with class teaching records and optional student progress writeback.

Mitigation: Use it only in environments that enforce consent checks, privacy controls, and teacher confirmation before storing or sharing student-related data.

Risk: Classroom materials may include AI-generated items or partial translation scaffolds that require policy review.

Mitigation: Require teacher review before classroom use, resource-bank entry, or publication, and confirm that generated material follows the classroom policy on translation support.

Risk: Student-facing or parent-facing output could expose protected student information if sharing consent is not checked.

Mitigation: Check parent-sharing and cross-skill-sharing consent before producing shareable feedback, and route crisis signals through the bundled referral protocol.

Risk: Modern textbook annotations, translations, or teaching-aid designs may be copyrighted.

Mitigation: Do not copy protected editions; label citation status and keep teacher-facing outputs to frameworks, prompts, and key-sentence scaffolds.

## Reference(s):

- [文言文常用实词虚词速查](references/classical-vocab-quick-ref.md)
- [文言文训诂四法速查卡](references/exegesis-method-card.md)
- [文言文诵读三阶与节奏训练指南](references/recitation-rhythm-guide.md)
- [诗词意象速查](references/poetry-image-catalog.md)
- [主题讨论问题设计题库](references/theme-discussion-question-bank.md)
- [学员古文积累档案模板](references/classical-accumulation-profile-template.md)
- [串讲样板模板](references/serial-explain-sample-template.md)
- [班级教学工作空间数据契约](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-classical-guide)
- [Publisher profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured teaching plans, tables, checklists, discussion prompts, and JSON-compatible class-record fields when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is expected before writing student-related records or using AI-generated classroom items.]

## Skill Version(s):

2.1.12 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
